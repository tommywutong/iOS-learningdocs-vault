---
title: Repositories Organizer Help
apple_id: TP40010350
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/recipes/xcode_help-repositories_organizer/articles/cloning_repository.html
archived_at: '2026-07-18T02:39:18.010339Z'
---
> 导航：[总目录](../../README.md) · [recipes](../../_indexes/recipes.md) · [Repositories Organizer Help](Repositories%20Organizer%20Help%20%28Legacy%29.md)



# Checking Out or Cloning a Repository

Check out or clone a repository to create a copy on your local system.

![bullet](../../_unindexed/Resources/1282/Images/task_2x.png)To check out or clone a repository

1. In the repositories organizer, click the Add button and choose Checkout or Clone Repository.
2. Enter the pathname or URL for the file.
3. When the “Host is reachable” indicator turns green, click the Next button.
4. Enter a local name for the repository and click Clone (or Checkout) to copy it.
5. Choose a location and click the highlighted Clone (or Checkout) button to save the local repository.

   The video shows cloning a Git repository for the Sketch sample code project.

By abstracting common repository operations, Xcode supports both Git and Subversion (SVN) repositories with a single, unified graphical user interface and workflow. Depending on your choice, this one operation checks out (for SVN) or clones (for Git) the repository and integrates it with your project.

Cloning a Git repository in Xcode sets up a complete repository on your local system and integrates that repository with your workspace so that you can quickly start using it. This approach gives you the benefits of distributed version control, including full commit rights, whether you’re online or not.

An SVN checkout operation does not create a local repository. You must have a network connection to the repository server to be able to commit changes.

For SVN, you must also provide the relative paths to the `trunk`, `branches`, and `tags` directories. To do so, click the name of the new repository in the repositories organizer and fill in the associated fields. If your SVN server requires authentication, fill in the user name and password as well.

### Related Articles

- About the Organizer Window
