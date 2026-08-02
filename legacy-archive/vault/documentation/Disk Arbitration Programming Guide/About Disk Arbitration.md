---
title: Disk Arbitration Programming Guide
apple_id: TP40009310
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: DiskArbitration
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/DriversKernelHardware/Conceptual/DiskArbitrationProgGuide/Introduction/Introduction.html
archived_at: '2026-07-15T07:31:54.598466Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](Using%20Disk%20Arbitration%20Notification%20and%20Approval%20Callbacks.md)

# About Disk Arbitration

The Disk Arbitration framework notifies your app when disks appear and disappear and lets your app influence that process. With Disk Arbitration, your app can:

- Detect when new disks appear
- Prevent mounting
- Mount a volume with different flags or on a different mount point
- Unmount a volume
- Watch for changes in volume names

Disk Arbitration is a low-level framework based on Core Foundation.

You should read this document if you need to handle unknown media, disable the normal mount process for certain devices, or otherwise monitor or manipulate the mounting or unmounting of volumes.

At a high level, you can use the Disk Arbitration framework to:

- Receive notification of disk-related events (disk ejection, for example) and participate in the arbitration process (_preventing_ disk ejection, for example).
- Obtain information about disks and manipulate disks (requesting that a disk be ejected, for example).

### Working with Disk Arbitration Session Objects

With session objects, you can receive notification when a disk appears, a mount or unmount occurs, or a disk disappears. You can also register an approval callback to block those operations.

For example, your app might register for notification when a disk appears, and if the disk matches a specific GUID, it might automatically make a backup copy of specific files on that external disk.

### Working with Disk Objects

A disk object represents a particular disk or partition. You can eject it, obtain information about it, or mount and unmount the associated volume or volumes. But first, you must obtain an object corresponding to a particular disk.

[Next](Using%20Disk%20Arbitration%20Notification%20and%20Approval%20Callbacks.md)

