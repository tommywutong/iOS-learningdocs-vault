---
title: Workspace Services Programming Topics
apple_id: 10000100i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2009-06-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Workspace/Articles/WorkspaceNotifications.html
archived_at: '2026-07-15T07:21:22.957672Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Workspace Services Programming Topics](Introduction%20to%20Workspace%20Services.md)


[Next](Document%20Revision%20History.md)[Previous](Manipulating%20Devices.md)

# Receiving Workspace Notifications

Workspace notifications are posted when:

- applications are launched and terminated
- volumes are mounted or unmounted
- the Finder performs file operations
- the Finder becomes the active application or resigns as the active application
- the user logs out or shuts down the computer
- the computer wakes from sleep.

Instead of going through the application’s default notification center as most notifications do, `NSWorkspace` notifications are posted to a notification center provided by the `NSWorkspace` object. To receive `NSWorkspace` notifications, your application must register an observer with the `NSWorkspace` notification center, returned by the [notificationCenter](https://developer.apple.com/documentation/appkit/nsworkspace/1525071-notificationcenter) method.

The code fragment in Listing 1 registers a method `observerMethod` with the `NSWorkspace` notification center to receive all `NSWorkspace` notifications:

__Listing 1__  Registering for workspace notifications

```
NSNotificationCenter *notCenter;

// Assume -observerMethod:(id)aNotification exists
notCenter = [[NSWorkspace sharedWorkspace] notificationCenter];
[notCenter addObserver:self
           selector:@selector(observerMethod:)
           name:nil object:nil]; // Register for all notifications
```

[Next](Document%20Revision%20History.md)[Previous](Manipulating%20Devices.md)

