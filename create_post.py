import os
from datetime import datetime
from os import listdir
from os.path import isfile, join, splitext, basename
from converted_files import posted

def post_file(f):
	if f[0] == '.' or 'DRAFT' in f:
		# if it's a dotfile (aka a system file) or "DRAFT" is in the title, don't post it
		return False
	return f not in posted and isfile(join('blogPosts', f))

def get_timestamp(filename):
	return os.stat(join('blogPosts', filename)).st_ctime

def get_filename(timestamp, title):
	dt_object = datetime.fromtimestamp(timestamp)
	return dt_object.strftime('%Y-%m-%d-') + "-".join(title.split(' '))

def get_title(filename):
	return " ".join(splitext(basename(filename))[0].split('-'))

def get_file_info(f):
	timestamp = get_timestamp(f)
	title = get_title(f)
	return {'path': f, 'timestamp': timestamp, 'filename': get_filename(timestamp, title), 'title': title}

def timestamp_for_post(timestamp):
	dt_object = datetime.fromtimestamp(timestamp)
	return dt_object.strftime('%Y-%m-%d %H:%M:%S')

def update_saved_files_list():
	files = ['"' + p +'"' for p in posted] + ['"' + "-".join(f['title'].split(' ')) +'.md"' for f in file_infos]
	writeFile = open('converted_files.py', "w+")
	writeFile.write('posted = [{filenames}]'.format(filenames=", ".join(files)))
	writeFile.close()

file_infos = [get_file_info(f) for f in listdir('blogPosts') if post_file(f)]

for file_info in file_infos:
	read_file = open(join('blogPosts', file_info['path']), "r")
	post = read_file.read()
	tagline = post[:50].replace('\n', ' ').replace(':', '-') + '...'
	writeFile = open('../madCode.github.io/_posts/{filename}.markdown'.format(filename=file_info["filename"]), "w+")
	header = '---\nlayout: post\ntitle: {title}\ntagline: {tagline}\ntags: microblog\ncategory: microblog\nmaintag: microblog\ndate: {timestamp}\n---\n'.format(title=file_info["title"], tagline=tagline, timestamp=timestamp_for_post(file_info["timestamp"]))
	writeFile.write(header)
	writeFile.write(post)
	writeFile.close()

update_saved_files_list()