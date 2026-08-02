---
title: Repositories Organizer Help
apple_id: TP40010350
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/recipes/xcode_help-repositories_organizer/articles/CommittingFilestoaRepository.html
archived_at: '2026-07-18T02:39:07.874809Z'
---
> 导航：[总目录](../../README.md) · [recipes](../../_indexes/recipes.md) · [Repositories Organizer Help](Repositories%20Organizer%20Help%20%28Legacy%29.md)



# Committing Files to a Repository

Commit changed files to ensure that those changes are preserved and managed as part of a repository.

![bullet](../../_unindexed/Resources/1282/Images/task_2x.png)To commit files to a repository

1. Ensure that you have saved all file changes.
2. Choose File > Source Control > Commit.
3. In the confirmation dialog, deselect any files that you do not wish to commit.
4. Review and edit (as appropriate) any changes to be committed.
5. Enter a commit comment.
6. Click Commit.

   The video shows committing changes in four files in the Sketch project to a local Git repository

You can use the confirmation dialog to compare your new version with any past version and to make any necessary edits in the current version. Any changes you make as you review a file are included in the committed file and saved in your project.

If you’re using Subversion, a commit operation copies the changes from selected files into the remote Subversion repository. Therefore, you must be connected to the repository before you can commit changes. (For details, see your repository administrator.)

If you’re using Git, the commit operation adds your changes to your local working copy. If you're using a remote Git repository, you have to perform a push operation to add your committed changes to the shared repository.

A commit comment is required; the Commit button is disabled until you enter one. Good comments are specific, but concise; suggested content includes a brief description of the changes, what they are meant to accomplish, and URLs or ID numbers of any relevant bugs. The version editor displays the affected code together with your name and commit comment, so you can omit information that’s in code comments or that’s obvious from looking at the line of code.

### Related Articles

- About the Organizer Window
- [Viewing Changes for a Specific Commit Version](Viewing%20Changes%20for%20a%20Specific%20Commit%20Version.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydgnjqfvbuqmjtfvjvomi)
- [Checking Out or Cloning a Repository](Checking%20Out%20or%20Cloning%20a%20Repository.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydgnjqfvbuqmjnknltc)
