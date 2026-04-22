##Push a single lab as a branch
```
git subtree split --prefix="001_documentation/001_first_steps" -b 001_documentation__001_first_steps
git push origin 001_documentation__001_first_steps
```


##Workflow after adding/editing a lab
Every time you update a lab, you just re-run the split and force-push that one branch:
```
# make changes, commit to main
git add .
git commit -m "update 001_first_steps"

# re-split and push only that branch
git subtree split --prefix="001_documentation/001_first_steps" -b 001_documentation__001_first_steps
git push origin 001_documentation__001_first_steps --force
```