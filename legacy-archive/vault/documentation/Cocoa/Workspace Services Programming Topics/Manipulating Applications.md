---
title: Workspace Services Programming Topics
apple_id: 10000100i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2009-06-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Workspace/Articles/ManipulatingApplications.html
archived_at: '2026-07-15T07:21:21.456673Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Workspace Services Programming Topics](Introduction%20to%20Workspace%20Services.md)


[Next](Manipulating%20Devices.md)[Previous](Manipulating%20Files.md)

# Manipulating Applications

This task explains how to use NSWorkspace to manipulate
applications. For information on how to use the `.app` extension,
see [Use of .app Extension](Use%20of%20.app%20Extension.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaydglkciffeorkkifeq).

The NSWorkspace methods `launchApplication:` and `launchApplication:showIcon:autoLaunch:` launch applications using Launch Services.
The application name can include or omit the `.app` extension.

The `fullPathForApplication:` method
returns the full path for an application, specified with or without
the `.app` extension.

To hide all other applications, you can use the `hideOtherApplications` method.
Since the user usually has access to this functionality through
other means, you should rarely have to invoke this method.

[Next](Manipulating%20Devices.md)[Previous](Manipulating%20Files.md)

