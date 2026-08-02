---
title: Tab View Programming Topics
apple_id: 10000074i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2003-11-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TabView/Tasks/UsingTabViewDelegate.html
archived_at: '2026-07-15T07:19:59.240832Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Tab View Programming Topics](Introduction%20to%20Tab%20Views.md)


[Next](Document%20Revision%20History.md)[Previous](Setting%20Tab%20View%20Appearance.md)

# Using a Tab View Delegate

NSTabView defines delegate messages to allow the delegate to control or react to changes in selection and changes in the number of tabs:

- `tabViewDidChangeNumberOfTabViewItems:` informs the delegate that the number of tab view items in the tab view has changed.
- `tabView:didSelectTabViewItem:` informs the delegate that the specified tab view item has been selected.
- `tabView:shouldSelectTabViewItem:` informs the delegate that the specified tab view item is about to be selected. The delegate can return `NO` to prevent the selection.
- `tabView:willSelectTabViewItem:` informs the delegate that the specified tab view item will be selected. The delegate can perform tasks related to the selection, but cannot prevent it.

[Next](Document%20Revision%20History.md)[Previous](Setting%20Tab%20View%20Appearance.md)

