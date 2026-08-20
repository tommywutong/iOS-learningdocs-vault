---
title: Combo Box Programming Topics
apple_id: 10000020i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/Tasks/SettingComboBoxValue.html
archived_at: '2026-07-15T07:13:43.352967Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Combo Box Programming Topics](Introduction%20to%20Combo%20Boxes.md)


[Next](Using%20Automatic%20Completion%20in%20Combo%20Boxes.md)[Previous](Managing%20the%20Combo%20Box%E2%80%99s%20List.md)

# Setting the Combo Box’s Value

When you set or retrieve a combo box’s value with the standard NSControl methods (such as `setStringValue:`, `stringValue`, `setFloatValue:`, and `floatValue`), you’re setting or retrieving the value of the combo box’s text field, and not the current selection of the list. Programmatically changing the combo box’s value does not change what’s selected in the combo box’s list. Conversely, programmatically changing what’s selected in the list does not change the text field’s value. If you want the text field value and the list selection to match up, you need to set them individually.

For example, say you want to initialize the combo box’s list and text field to the list’s third item. This code does that for a combo box that maintains an internal item list:

```
[myComboBox selectItemAtIndex:2]; // First item is at index 0
[myComboBox setObjectValue:[myComboBox objectValueOfSelectedItem]];
```

This code does that for a combo box with an external data source:

```
[myComboBox selectItemAtIndex:2];
[myComboBox setObjectValue:
    [myComboBoxDataSource comboBox:myComboBox
        objectValueForItemAtIndex:[myComboBox indexOfSelectedItem]]];
```

And this code initializes the combo box’s text field to “Red” and selects it from the list if available. Note that this works for combo boxes with either internal or external data sources:

```
[myComboBox setStringValue:@"Red"];
[myComboBox selectItemWithObjectValue:@"Red"];
```

[Next](Using%20Automatic%20Completion%20in%20Combo%20Boxes.md)[Previous](Managing%20the%20Combo%20Box%E2%80%99s%20List.md)

