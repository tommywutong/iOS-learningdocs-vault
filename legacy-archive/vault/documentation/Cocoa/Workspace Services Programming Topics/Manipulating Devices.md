---
title: Workspace Services Programming Topics
apple_id: 10000100i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2009-06-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Workspace/Articles/ManipulatingDevices.html
archived_at: '2026-07-15T07:21:21.937022Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Workspace Services Programming Topics](Introduction%20to%20Workspace%20Services.md)


[Next](Receiving%20Workspace%20Notifications.md)[Previous](Manipulating%20Applications.md)

# Manipulating Devices

This task explains how to track available storage
devices and their associated volumes.

NSWorkspace provides several methods for tracking the status
of storage devices:

- To retrieve the names of local mounted volumes,
  use the `mountedRemovableMedia` and `mountedLocalVolumePaths` methods.
- To wait until new removable devices have been mounted and
  then retrieve their pathnames, use the `mountNewRemovableMedia` method.

Also, to retrieve the Finder display names for volumes, use
NSFileManager’s `displayNameAtPath:` method.

[Next](Receiving%20Workspace%20Notifications.md)[Previous](Manipulating%20Applications.md)

