#/usr/bin/sh

git add . || echo Failed while git add
echo Changes?
read changes
git commit -m "$changes" || echo Failed while committing changes
git push heroku master || echo Failed while push to heroku
