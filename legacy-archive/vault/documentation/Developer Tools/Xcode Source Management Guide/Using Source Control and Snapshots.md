---
title: Xcode Source Management Guide
apple_id: TP40006828
resource_type: Guide
platform: iOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeSourceManagement/50-Using_Surce_Control_and_Snapshots/source_control_and_snapshots.html
archived_at: '2026-07-15T07:28:40.119005Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Source Management Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Snapshots.md)

# Using Source Control and Snapshots

Source control and snapshots let you keep track of changes you make to your source files. However, they are not made to work together. Snapshots provide an undo/redo mechanism with local change stores. Source control provides the benefits of snapshots but with a more robust back end and support for multiple developers.

You may want to use source control to work on a project in which other developers also work. That way, you can stay up to date with the changes your colleagues make. But you may also want to undo/redo changes you make locally. If you choose to do so, you should keep the following in mind:

- When your source control system places metadata in your project root (through `.svn` or `CVS` directories, for example), restoring an entire snapshot restores these metadata, as well, which may result in potentially serious synchronization problems with the repository.

  Therefore, if you’re using source control and snapshots in the same project, you should never restore entire snapshots. Instead, you should restore individual files or changes.
- If you restore a snapshot made before a commit operation, you revert the affected files to a state prior to the commit.

  Therefore, after performing a commit that would cause such reversion, you should take measures to ensure that the next commit operation involving those files does not revert changes published by other developers.

[Next](Document%20Revision%20History.md)[Previous](Snapshots.md)

