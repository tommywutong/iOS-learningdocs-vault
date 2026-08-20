---
title: Combo Box Programming Topics
apple_id: 10000020i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/Tasks/ProvidingComboBoxData.html
archived_at: '2026-07-15T07:13:42.858420Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Combo Box Programming Topics](Introduction%20to%20Combo%20Boxes.md)


[Next](Managing%20the%20Combo%20Box%E2%80%99s%20List.md)[Previous](How%20Combo%20Boxes%20Work.md)

# Providing Data for a Combo Box

The NSComboBox control can be set up to populate the pop-up list either from an internal item list or from an object that you provide, called its data source. Specify which to use with `setUsesDataSource:`. By default, a combo box uses the internal list.

If you specify that a combo box uses an external data source and then try to invoke a method that uses the internal list—such as `addItemWithObjectValue:`—the method throws an exception.

An external data source declares the methods that the combo box uses to access its data. Use one if an internal list isn’t efficient for your data. An external data source can store its items in any way, but it must be able to identify them by an integer index.

To specify that combo box uses an external data source, first use `setUsesDataSource:` with `YES` as the argument, then use `setDataSource:` with your data source object as the argument. If you use `setDataSource:` before `setUsesDataSource:`, `setDataSource:` throws an exception.

The data source must define these methods. The method `setDataSource:` logs a warning if its argument doesn’t implement them.

- `numberOfItemsInComboBox:` returns how many items to display.
- `comboBox:objectValueForItemAtIndex:` returns the object that corresponds to the specified index.

The data source can optionally define these methods. The method `setDataSource` doesn’t check for them and the combo box invokes them only if they’re available.

- `comboBox:indexOfItemWithStringValue:` returns the index for the item that matches the specified string. If this method is available, the combo box performs incremental searches when the user types into the text field with the pop-up list displayed.
- `comboBox:completedString:` returns a string that begins with the specified string. If autocompletion is enabled, the combo box tries to complete what the user enters into the text field with an item from the pop-up list. If this method isn’t available and autocompletion is enabled, the combo box goes through each item one-by-one to find a completion.

And here are some NSComboBox methods your data source may need if it loads data in the background:

- `noteNumberOfItemsChanged` informs the combo box that the number of items in the data source has changed.
- `reloadData` marks the combo box as needing redisplay, so it reloads the data for the visible pop-up items and draws the new values.

The combo box treats objects provided by its data source as values to be displayed in the combo box’s pop-up list. If these objects aren’t of common value classes—such as strings, numbers, and so on—you’ll need to create a custom NSFormatter to display them. See _[Data Formatting Guide](../Data%20Formatting%20Guide/Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazds2i)_ for more information.

NSComboBox provides a complete set of methods that allow you to add, insert, and delete items in the internal item list for combo boxes that don’t use a data source:

- To add one or more items to the end of the list, use `addItemWithObjectValue:` or `addItemsWithObjectValues:`
- To insert an item into the middle of the list, use `insertItemWithObjectValue:atIndex:`
- To find the index for a particular object, use `indexOfItemWithObjectValue:`.
- To find the object at a particular index, use `itemObjectValueAtIndex:`.
- To remove items from the list, use `removeAllItems`, `removeItemAtIndex:`, or `removeItemWithObjectValue:`.
- To retrieve an array of all the list’s items, use `objectValues`.
- To retrieve the number of items in the list, use `numberOfItems`.

If `usesDataSource` returns `YES` and you use any of the above methods, the method will throw an exception. By default, `usesDataSource` returns `NO`.

[Next](Managing%20the%20Combo%20Box%E2%80%99s%20List.md)[Previous](How%20Combo%20Boxes%20Work.md)

