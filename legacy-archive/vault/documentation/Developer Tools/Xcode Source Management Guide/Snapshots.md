---
title: Xcode Source Management Guide
apple_id: TP40006828
resource_type: Guide
platform: iOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeSourceManagement/40-Snapshots/snapshots.html
archived_at: '2026-07-15T07:28:39.579988Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Source Management Guide](Introduction.md)


[Next](Using%20Source%20Control%20and%20Snapshots.md)[Previous](Source%20Control.md)

# Snapshots

Snapshots allow you to save project state at particular points in time, which you can restore entirely or partially at a later point. Snapshots provide a multifile undo/redo mechanism that lets you experiment freely with your source files. A snapshot stores the state of a directory tree at the time it was taken. The changes you make can be easily reverted by restoring your project to a snapshot you made before the experiment.

At any particular time, a project can access only one snapshot store. A _snapshot store_ is the set of snapshots taken from one or more projects with the same project root. (See General Project Attributes to learn how to set a project’s project root.)

Xcode stores snapshots in your home directory:

```
~/Library/Application Support/Developer/Shared/SnapshotRepository.sparseimage
```

This chapter shows how to use locally stored snapshots to manage changes to multiple files.

The Snapshots window (Figure 3-1) is where you view your project’s snapshots.

__Figure 3-1__  The Snapshots window

!

The Snapshots window contains the following items:

- __Snapshot list.__ Lists the snapshots accessible to the project, which is determined by the _project root_ (see [Managing Source in Xcode](Source%20Management%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmobvfvjvomi) for details about the project root).
- __Name.__ The name of the snapshot. Xcode automatically names snapshots based on where you perform the Make Snapshot command.
- __Date.__ The date the snapshot was taken.
- __Archive.__ The filename of the snapshot.
- __Comments.__ Comments you add to the snapshot.
- __Changes pane.__ The differences between a file in the selected snapshot and the file in the project or another snapshot.

To make a snapshot, choose File > Make Snapshot.

You may want to change the snapshot name to reflect special circumstances.

To change the name of a snapshot, select the snapshot in the Snapshots list, and enter the new name in the Name field.

When you select a snapshot in the Snapshot window, the changed file list shows the differences between the snapshot and the current state of the project. That is, Xcode compares the snapshot against the project.

Sometimes you may need to know what changed between two snapshots. You can view the differences between two snapshots by selecting them in the Snapshot list.

To restore the project to the state represented by a particular snapshot, select the snapshot in the Snapshot list, and click Restore.

To restore a single file in a snapshot:

1. In the Snapshot list, select the desired snapshot.
2. In the file list, select the file to restore, and click Restore.
3. Click the Restore button.

To restore a single change instead of an entire file:

1. In the Snapshot list, select the desired snapshot.
2. In the file list, select the desired file.
3. In the changes pane, copy the text to restore.
4. Open the file into which you want to restore the copied text.
5. Paste the text in the appropriate location, and save the file.

From time to time, you may want to prune a snapshot store. You can do this by deleting individual snapshots or deleting the snapshot store.

To delete a snapshot, In the Snapshots window, select the snapshot you want to delete, and click Delete in the toolbar.

To delete a snapshot store, first Quit Xcode. Then in the Finder, navigate to the directory that contains the snapshot store (see [Snapshots](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dqmryfvbuqmjqgayc2u2xge) for details), and delete the `SnapshotRepository.sparseimage` file.

[Next](Using%20Source%20Control%20and%20Snapshots.md)[Previous](Source%20Control.md)

