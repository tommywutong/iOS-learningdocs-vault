---
title: Combo Box Programming Topics
apple_id: 10000020i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/Tasks/ManagingComboBoxList.html
archived_at: '2026-07-15T07:13:42.349992Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Combo Box Programming Topics](Introduction%20to%20Combo%20Boxes.md)


[Next](Setting%20the%20Combo%20Box%E2%80%99s%20Value.md)[Previous](Providing%20Data%20for%20a%20Combo%20Box.md)

# Managing the Combo Box’s List

There are a number of ways that you can affect a combo box’s list’s appearance, as well as controlling them programatically.

These methods let you control the list’s appearance.

- To choose whether the pop-up list has a vertical scroll bar, use `setHasVerticalScroller:`. When there’s no scroll bar, the user can still scroll to items that aren’t displayed by holding the mouse at the top or bottom of the list. And when there is a scroll bar, the scroll bar is shown even when all items can be displayed in the visible portion of the list.
- To set the number of items displayed in the pop-up list, use `setNumberOfVisibleItems:`. The default is 5.
- To set the amount of space that surrounds each item in the list, use `setIntercellSpacing:` with an argument of type NSSize. The width component is the size in points of the list’s left and right margins. The height component is the space in points above and below each list item.
- To set the height of each list item, use `setItemHeight:`.

These methods let you manipulate the list’s selection:

- To select a particular item, use `selectItemAtIndex:` or `selectItemWithObjectValue:`.
- To retrieve the selected item, use `indexOfSelectedItem` or `objectValueOfSelectedItem`.
- To deselect an item, use `deselectItemAtIndex:`.

Note that changing the list’s selection does not change the content’s of the combo box’s text field. For more information, see [Setting the Combo Box’s Value](Setting%20the%20Combo%20Box%E2%80%99s%20Value.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgi2tmlkdjjbeeq2kijea).

These methods let you scroll the list. The list doesn’t need to be visible to use these methods:

- To scroll the list so that a particular item is as close to the top as possible, use `scrollItemAtIndexToTop`.
- To scroll the list so that a particular item is visible, use `scrollItemAtIndexToVisible`.

[Next](Setting%20the%20Combo%20Box%E2%80%99s%20Value.md)[Previous](Providing%20Data%20for%20a%20Combo%20Box.md)

