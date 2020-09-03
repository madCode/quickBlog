#!/bin/bash
python3 create_post.py
cd ../madCode.github.io
git add .
git commit -m "publishing blog posts: $(date)"
git push