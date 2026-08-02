---
title: Toolbar Programming Topics for Cocoa
apple_id: 10000109i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Tasks/SubclassingTBItem.html
archived_at: '2026-07-15T07:20:55.291622Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Toolbar Programming Topics for Cocoa](Introduction%20to%20Toolbars.md)


[Next](Techniques%20for%20Toolbar%20Management.md)[Previous](Selectable%20Toolbar%20Items.md)

# Subclassing NSToolbarItem

To provide enabling behavior or to modify click-through behavior on a view item, you must override `validate` and may want to override `isEnabled` and `setEnabled:`.

To enable multiple copies of the item in the toolbar, you must override `allowsDuplicatesInToolbar` to return `YES`.

Your subclass must conform to the NSCopying protocol.

[Next](Techniques%20for%20Toolbar%20Management.md)[Previous](Selectable%20Toolbar%20Items.md)

