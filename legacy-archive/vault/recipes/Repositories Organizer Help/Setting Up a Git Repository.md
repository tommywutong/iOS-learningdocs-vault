---
title: Repositories Organizer Help
apple_id: TP40010350
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/recipes/xcode_help-repositories_organizer/articles/SettingupaGitRepositoryfromtheCommandLine.html
archived_at: '2026-07-18T02:39:15.459980Z'
---
> 导航：[总目录](../../README.md) · [recipes](../../_indexes/recipes.md) · [Repositories Organizer Help](Repositories%20Organizer%20Help%20%28Legacy%29.md)



# Setting Up a Git Repository

Use command-line commands to set up a Git repository for an existing project.

![bullet](../../_unindexed/Resources/1282/Images/task_2x.png)To set up a Git repository

1. Use the `cd` command to switch to your project directory, making it the current working directory.
2. Enter `git init` to create an empty repository.
3. Enter `git add .` to copy your project files into the repository.
4. Enter `git commit -m "Initial commit"` to commit all the files.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```
// Step 1$ cd /Users/me/sample_code/Sketch // Step 2$ git initInitialized empty Git repository in /Users/me/sample_code/Sketch/.git/ // Step 3$ git add . // Step 4$ git commit -m "Initial commit"[master (root-commit) 173067e] Initial commit... 74 files changed, 10198 insertions(+) create mode 100644 .DS_Store create mode 100644 Arrow.tiff create mode 100644 Circle.tiff create mode 100644 Cross.tiff create mode 100644 Draw2App.icns create mode 100644 Draw2File.icns create mode 100644 English.lproj/Draw2.nib/classes.nib... create mode 100644 Sketch.xcodeproj/xcuserdata/ernest.xcuserdatad/xcdebugger/Breakpoints.xcbkptlist create mode 100644 Sketch.xcodeproj/xcuserdata/ernest.xcuserdatad/xcschemes/Sketch.xcscheme create mode 100644 Sketch.xcodeproj/xcuserdata/ernest.xcuserdatad/xcschemes/xcschememanagement.plist create mode 100644 TextGraphic.tiff
```

To set up a repository for an existing project, you have to use the command-line shell implemented by the Terminal utility app.

### Related Articles

- [Setting Up a Subversion Repository](Setting%20Up%20a%20Subversion%20Repository.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydgnjqfvbuqmznknltc)
- [Checking Out or Cloning a Repository](Checking%20Out%20or%20Cloning%20a%20Repository.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydgnjqfvbuqmjnknltc)
