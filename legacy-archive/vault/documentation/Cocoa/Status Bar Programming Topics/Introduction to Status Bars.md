---
title: Status Bar Programming Topics
apple_id: 10000073i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/StatusBar/StatusBar.html
archived_at: '2026-07-15T07:19:22.716205Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Status%20Bars.md)

# Introduction to Status Bars

Status bars display a collection of status items that provide interaction with or feedback to the user, such as a menu or an image reflecting an application’s state. A system-wide status bar resides at the right side of the menu bar and is the only status bar currently available.

Use status items sparingly and only if the alternatives (such as a Dock menu, preference pane, or status window) are not suitable. Because there is limited space in the menu bar in which to display status items, status items are not guaranteed to be available at all times. For this reason, do not rely on them being available and always provide a user preference for hiding your application’s status items to free up space in the menu bar.

For more information on when to use the status bar, see _Aqua Human Interface Guidelines_.

The capabilities of status bars are discussed in [About Status Bars](About%20Status%20Bars.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe4tklkdjjbeursdinea). Sample code and a discussion of how to create status items are in [Creating Status Items](Creating%20Status%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe4tmlkcijbuiqkhjbba).

[Next](About%20Status%20Bars.md)

