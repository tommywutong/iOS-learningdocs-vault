---
title: Box Programming Topics
apple_id: 10000017i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2003-02-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Box/Tasks/SettingBoxTitle.html
archived_at: '2026-07-15T07:11:22.868464Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Box Programming Topics](Introduction%20to%20Boxes.md)


[Next](Setting%20a%20Box%E2%80%99s%20Border%20Appearance.md)[Previous](Introduction%20to%20Boxes.md)

# Setting a Box’s Title

You can have a box with no title or with a title positioned in one of six places. To set the title’s location, use `setTitlePosition:` with one of options listed below. By default, it’s `NSAtTop`.

|  |  |  |
| --- | --- | --- |
| `NSAboveTop`NSAboveTop | `NSAtTop`NSAtTop | `NSBelowTop`NSBelowTop |
| `NSAboveBottom`NSAboveBottom | `NSAtBottom`NSAtBottom | `NSBelowBottom`NSBelowBottom |
| `NSNoTitle`NSNoTitle |  |  |

To set the title’s font, use `setTitleFont:`. By default, it’s the Control Content font, which you can set in the Fonts tab of the Appearance panel in the Preferences application. Note that the title appears inside the box, so changing the size of the font will affect the size of the box’s content rectangle.

To set the title, use `setTitle:`. By default, it’s “Title”. If the title is longer than the box’s width, the title is clipped.

[Next](Setting%20a%20Box%E2%80%99s%20Border%20Appearance.md)[Previous](Introduction%20to%20Boxes.md)

