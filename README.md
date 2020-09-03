# Goal
The goal of this tool is to allow one to quickly post to your github pages jekyll site. Jekyll allows for super easy formatting of blog posts and pages, but it's not easy to make posts on the go. QuickBlog allows you to achieve that without giving up your easy Jekyll site.

# How it works
QuickBlog works uses one easy bash script (publish_posts.sh) to achieve two big steps:
1. Converts files in the 'blogPosts' folder to jekyll formatted posts saved in your site's git repo.
2. Makes a commit with the new blog posts and pushes the commit to your site.

If you really want to get fancy, use a free open-source tool like [Syncthing](https://syncthing.net/) to sync the blogPosts folder between your computer and your phone. That way, you can make posts from your phone!

# Setup instructions
1. Make sure your github pages repo is cloned onto your computer.
2. Clone this repo to your computer as well.
3. In `create_post.py` on line 44, change `../madCode.github.io/_posts/` to the path to your own github.io repo's _posts folder.
4. In `publish_posts.sh` change `cd ../madCode.github.io` to cd into your github.io repo

Test break! Make a few markdown posts in the blogPosts folder and run first `create_post.py`, to make sure posts are being created where and how you want, and then `publish_posts.sh` to make sure posts are being pushed appropriately. Customize whatever you need to customize. If you're satisfied, you can stop here.

5. Let's have some fun with this. If you're on Linux or Mac, open up a terminal and type `nano crontab -e`. [Cron jobs](https://en.wikipedia.org/wiki/Cron) are basically tasks you can schedule your computer to run regularly. In your crontab editor type:
```
MAILTO="<your email or leave blank>"
0 */1 * * * cd ~/<path_to_>/quickBlog && ./publish_posts.sh >> log.txt
```
Then save and exit. You should see a message about a cron job being "loaded". This will run `./publish_posts.sh` every hour. You can use [crontab guru](crontab.guru/) to figure out exactly what schedule you want. You can also change the `publish_posts` script to just run `create_post` and not push your commits.

6. Download a markdown editor like [Markor](https://gsantner.net/project/markor.html) onto your phone. 
7. Set up [Syncthing](https://syncthing.net/) and share your blogPosts folder to your phone.

Test break! Create a post on your phone and watch it get Syncthing-ed over to your computer and automatically pushed to the web. It's like magic! (Or at least like a slow wordpress :grimace: :sweat-smile:)