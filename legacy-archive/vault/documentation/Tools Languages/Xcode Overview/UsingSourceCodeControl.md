---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/UsingSourceCodeControl.html
archived_at: '2026-07-27T06:57:08.203320Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](GettingaHands-OnIntroduction.md)[Previous](UsingUndo.md)

## Using Source Code Control

Use commands in the Source Control menu to manage your project files with a source code repository. A repository saves multiple versions of each file onto disk, storing historical metadata about each version of each file. Source control allows you to keep track of file changes at a fine level of detail. Source control also helps you coordinate efforts if you work with a team of programmers.

A source control system helps you reconstruct past versions of a project. You can commit a file to your repository each time you make a major change. If you introduce bugs, you can use the Xcode version editor to compare the new version of the file with a past version that worked correctly, to locate the source of the trouble.

When multiple people work on a project, source control helps prevent conflicts and helps resolve conflicts should they arise. By keeping a central repository that holds the master copy of the software, the source control system allows each programmer to work on a local copy with no risk of corrupting the master. With a file checkout system, you can ensure that two people don’t work on the same code at the same time. If two people do change the same code, the system helps you merge the two versions.

You can also branch from a stable version of your project, add new features and make other changes to the branch, and then merge and reconcile those changes back into the stable version of your project.

Xcode supports two popular source control systems: Git and Subversion. Subversion (often abbreviated svn) is always server based. The server is typically on a remote computer (although it is possible to install the server locally). Git can be used purely as a local repository, or you can install a Git server on a remote computer to share a repository among team members.

If you are working alone, it’s easiest to use Git, because you won’t need to set up a server. When you create a project, Xcode automatically sets up a Git repository for you.

（原归档配图获取待重试：`CreateGitRepo_2x.png`）

In addition to performing continuous integrations, the Xcode service, available with OS X Server, hosts Git repositories.

If your repository is on a server, choose Source Control > Check Out to create a local working copy of the project on your computer. If you use a local Git repository, you don’t check out a working copy, because your local repository is your master copy.

When you are satisfied with changes you've made to a file, choose Source Control > Commit to ensure that those changes are preserved in the repository. You are required to provide a comment explaining the nature of your commit. If your Git repository is on a server, the commit operation adds your changes to your local repository. Perform a push operation to add your committed changes to the Git repository on the server. For example, when you choose Source Control > Commit on your development Mac, select the “Push to remote” option, specify the remote repository in the pop-up menu, and click Commit Files.

For help on connecting to and working with source code repositories, see [Xcode Help](https://help.apple.com/xcode).

### Viewing File Status

You can see the source control status of your files in the project navigator. The status is shown as a badge next to the filename.

（原归档配图获取待重试：`LocalModifiedFiles_2x.png`）

### Comparing File Versions to Revert Lines of Code

Choose View > Version Editor > Show Comparison View to compare versions of files saved in a repository. Use the jump bars to choose file versions based on their position within a repository. Each jump bar controls the selection for the content pane above it. To display a version, browse through the hierarchy to find it, then click to choose it. Shaded areas indicate changes between versions.

（原归档配图获取待重试：`VersionEditorWithChanges_2x.png`）

Use the version timeline to choose file versions based on their chronological order. Click the Timeline Viewer icon (（原归档配图获取待重试：`TimeLineIcon_2x.png`）) at the bottom of the center column to display the timeline between the two editing panes. Move the pointer up or down through the timeline to browse the available versions. When you find the version you want, click the left or right disclosure button to display that version in the corresponding editor pane.

You can edit the current working copy of the file in the version editor. If you want to revert changes between versions, you can copy code from an older version and paste it into the current version.

### Creating a Branch to Isolate Risky Changes

After you’ve worked on a project for awhile, you are likely to have a body of reliable, stable code. You can choose Source Control > _Working Copy_ > New Branch to create a copy of that code. Then you can work on new features and other changes without destabilizing your existing code base. When you are satisfied with your changes, you can merge them back into the body of stable code. Use Source Control > _Working Copy_ > Merge from Branch and Source Control > _Working Copy_ > Merge into Branch to combine and reconcile differences between versions of your project.

[Using Undo](UsingUndo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnrwfvjvomi)

[Getting a Hands-On Introduction](GettingaHands-OnIntroduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnryfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](GettingaHands-OnIntroduction.md)[Previous](UsingUndo.md)
