# pull all branches from Github repository
git clone repository_url
git fetch --all # fetch all branches from the remote repository
git branch -r # list all remote branches
git branch --track branch_locally_want_to_name origin/branch_name # create and track local branches for each remote branch

# loop through all remote branches and create local branches for each
for branch in $(git branch -r | grep -v '\->'); do
    git branch --track ${branch#origin/} $branch
done

# pull all branches
git pull --all

# Create new branch that not affect the main and current branches
git switch main
git pull #puu the latest changes
git switch -c new_branch_name

# delete branch
git branch -d branch_name # delete the branch safety
git branch -D branch_name # delete a branch locally with umnerged changes
git push origin --delete branch_name # delete a branch remotely

# all commands
git branch # check list branch
git swith -c other_branch # switch to other branch
git status # check current status those are new files/folders for check or uncheck
git push # push this new commit into repository
git push -- set-upstream origin/branch_name
git reset --hard origin/branch_name # pull new version repository

# save current log
    # use commit
    git add .
    git commit -am "describe information for this commit"
    git log -n # to see n log of commit

    # use stash
    git stash push -m "Stashing changes before switching branches"
    git stash list
        git stash apply stash@{number} # reapply the changes stashed in stash@{number} without removing them from the stash list
        git stash pop stash@{numbe} # apply the changes and also remove the stash from the list

# delete/squash commit history
=======
# delete commit historyr

git log -5 # list the latest commits
    git rebase -i commit_id # drop commit
        #if use powershell, the notepad will appear then we edit by replacing "drop" at the first line
        #editor in command line, use vi/vim to edit and replace 'drop' with commit that need to drop
        #use :wq! to escape editor in command line

        #in mac os, press "dd" at line want to drop, then press "esc" and type ":wq!" and press "Enter" then       
    git rebase -i HEAD~2 # remove the latest 2 commits
git push --force
