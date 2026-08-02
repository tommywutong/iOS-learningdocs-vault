---
title: Workspace Services Programming Topics
apple_id: 10000100i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2009-06-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Workspace/Articles/WorkspaceServices.html
archived_at: '2026-07-15T07:21:23.434729Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Workspace Services Programming Topics](Introduction%20to%20Workspace%20Services.md)


[Next](Use%20of%20.app%20Extension.md)[Previous](Introduction%20to%20Workspace%20Services.md)

# About Workspace Services

The NSWorkspace class provides an interface between Cocoa
applications and the OS X “workspace,” which consists primarily
of the services provided by the Finder.

NSWorkspace provides access to services for files, applications,
devices, user defaults, and a few other system features. Each application
has one shared instance of NSWorkspace, which you access through
the `sharedWorkspace` method.

NSWorkspace also provides notifications related to its services.
Unlike most notifications, all NSWorkspace notifications are posted
to NSWorkspace’s own notification center instead of the application’s
default notification center.

[Next](Use%20of%20.app%20Extension.md)[Previous](Introduction%20to%20Workspace%20Services.md)

