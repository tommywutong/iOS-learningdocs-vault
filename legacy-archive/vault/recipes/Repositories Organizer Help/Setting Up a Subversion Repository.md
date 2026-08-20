---
title: Repositories Organizer Help
apple_id: TP40010350
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/recipes/xcode_help-repositories_organizer/articles/SettingupaSubversionRepositoryfromtheCommandLine.html
archived_at: '2026-07-18T02:39:15.874342Z'
---
> 导航：[总目录](../../README.md) · [recipes](../../_indexes/recipes.md) · [Repositories Organizer Help](Repositories%20Organizer%20Help%20%28Legacy%29.md)



# Setting Up a Subversion Repository

Use command-line commands to set up a Subversion repository.

![bullet](../../_unindexed/Resources/1282/Images/task_2x.png)To set up a Subversion repository

1. Use the `mkdir` command to create a directory with three subdirectories named `branches`, `tags`, and `trunk` to hold a temporary copy of your project.
2. Copy the project directory into the `trunk` subdirectory.
3. Create a directory for the Subversion repository.
4. Use the `svnadmin create` command to create an empty Subversion repository.
5. Use the `svn import` command to import your project directory into the new Subversion repository.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```
// Step 1$ mkdir /Sketch_svn_tmp$ mkdir /Sketch_svn_tmp/trunk$ mkdir /Sketch_svn_tmp/branches$ mkdir /Sketch_svn_tmp/tags // Step 2$ cp -R /Users/me/sample_code/Sketch /Sketch_svn_tmp/trunk // Step 3$ mkdir /svn_rep // Step 4$ svnadmin create /svn_rep/Sketch_svn // Step 5$ svn import /Sketch_svn_tmp file:///svn_rep/Sketch_svn -m "Initial import"Adding         /Sketch_svn_tmp/trunkAdding         /Sketch_svn_tmp/trunk/SketchAdding         /Sketch_svn_tmp/trunk/Sketch/SKTGraphicView.hAdding  (bin)  /Sketch_svn_tmp/trunk/Sketch/Cross.tiffAdding         /Sketch_svn_tmp/trunk/Sketch/SKTAppDelegate.h...Adding         /Sketch_svn_tmp/trunk/Sketch/NSColor_SKTScripting.mAdding         /Sketch_svn_tmp/branchesAdding         /Sketch_svn_tmp/tags Committed revision 1.
```

To set up a Subversion repository, you have to use the command-line shell implemented by the Terminal app.

If you don’t have an existing project, use Xcode to create a project before setting up your repository.

### Related Articles

- [Setting Up a Git Repository](Setting%20Up%20a%20Git%20Repository.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydgnjqfvbuqmrnknltc)
