git config --global user.name GL27
git config --global user.email gabyliang2001@gmail.com

git pull --unshallow

git remote add upstream https://github.com/wusimon51/PyHW.git
git fetch upstream

git merge --no-edit upstream/main
git push origin main