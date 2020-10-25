# Test Role - Continuous Integration

* Other Roles - [Requirements.md](Requirements.md)
, [Design.md](Design.md)
, [Code.md](Code.md)
, [Test.md](Test.md)



* File: Milestone_4/Test.md

* URL: https://github.com/Eshop-project/CS-350/blob/master/docs/plan/Milestone_4/Test.md

* Documents: doc/plan/Milestone_4

* Git Repo: https://github.com/Eshop-project/CS-350/


### Build and Test with every push

Through the process of deducing our issues with the code, everyone contributed to the build of the guest user and therefore we were all merging to a repo on Git and committing and pulling and pushing. Through this process I had a part in pulling code that was constantly being updated and checking the validity of the work. Making sure no errors were being thrown and when errors did show, I posted about them in the issues log.

### Implement Travis (CI tool) or Code Coverage

File for the continuous integration workflow is [here](https://github.com/Eshop-project/CS-350/tree/master/.github/workflows).
The integration of the workflow is contained in a pylint file that should check all python code for bugs and quality. The issue is we'll need a check for the html, javascript, and CSS. This is not the biggest priority due to the fact that almost everything is tied into the Django framework, so we don't need to worry about everything else as much because if there are errors in the python, this is what we want to catch first, while other files of other code will be cosmetic issues, at best.

### Document release process

The current django project submitted is the current release.
