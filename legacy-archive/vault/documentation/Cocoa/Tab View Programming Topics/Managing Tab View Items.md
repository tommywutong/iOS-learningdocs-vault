---
title: Tab View Programming Topics
apple_id: 10000074i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2003-11-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TabView/Tasks/ManagingTabViewItems.html
archived_at: '2026-07-15T07:19:58.249164Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tab View Programming Topics](Introduction%20to%20Tab%20Views.md)


[Next](Setting%20Tab%20View%20Appearance.md)[Previous](How%20Tab%20Views%20Work.md)

# Managing Tab View Items

These methods let you add and remove tab view items:

- To add a tab view item at the end of the tab view item array, use `addTabViewItem:`
- To insert a tab view item to a specific position in the tab view item array, use `insertTabViewItem:atIndex:`
- To remove a tab view item, use `removeTabViewItem:`

These methods let you access tab view items:

- To return the index of a tab view item, use `indexOfTabViewItem:` or `indexOfTabViewItemWithIdentifier:`
- To return a specific tab view item at a specific index, use `tabViewItemAtIndex:` or `tabViewItemAtPoint:`
- To return an array of tab view items, use `tabViewItems`.
- To return the number of tab view items, use `numberOfTabViewItems`.

These methods select tab view items:

- To select the first or last tab view item in the array, use `selectFirstTabViewItem:` or `selectLastTabViewItem:`.
- To select the tab view item immediately before or after the currently selected item, use `selectPreviousTabViewItem:` or `selectNextTabViewItem:`.
- To select a tab view item at a specific index, use `selectTabViewItemAtIndex:`.
- To select the tab view item at the same index as the selected item in another control, use `takeSelectedTabViewItemFromSender:`
- To return the currently selected tab view item, use `selectedTabViewItem:`.

[Next](Setting%20Tab%20View%20Appearance.md)[Previous](How%20Tab%20Views%20Work.md)

