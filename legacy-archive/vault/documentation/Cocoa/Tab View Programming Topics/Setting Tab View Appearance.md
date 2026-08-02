---
title: Tab View Programming Topics
apple_id: 10000074i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2003-11-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TabView/Tasks/SettingTabViewAppearance.html
archived_at: '2026-07-15T07:19:58.745041Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tab View Programming Topics](Introduction%20to%20Tab%20Views.md)


[Next](Using%20a%20Tab%20View%20Delegate.md)[Previous](Managing%20Tab%20View%20Items.md)

# Setting Tab View Appearance

These methods let you change the appearance of a tab view:

- To change the font used for tab labels, use `setFont:`
- To change the tab view’s size , use `setControlSize:` with an argument of either `NSRegularControlSize` or `NSSmallControlSize`.
- To change the tab view’s tint, use `setControlTint:` with an argument of either `NSDefaultControlTint` or `NSClearControlTint`.
- To choose whether to allow a tab view to truncate the tab labels, use `setAllowsTruncatedLabels:`.
- To choose the tab view’s border style and whether it has visible tabs, use `setTabViewType:` with one of these as arguments:

  - `NSTopTabsBezelBorder`. The view includes tabs and has a bezeled border. This is the default.
  - `NSNoTabsBezelBorder`. The view does not include tabs and has a bezeled border.
  - `NSNoTabsLineBorder`. The view does not include tabs and has a lined border.
  - `NSNoTabsNoBorder`. The view does not include tabs and has no border.

These methods let you change the appearance of a tab view item:

- To set the tab view item’s label, use `setLabel:`.
- To set the tab view item’s color, use `setColor:`.

[Next](Using%20a%20Tab%20View%20Delegate.md)[Previous](Managing%20Tab%20View%20Items.md)

