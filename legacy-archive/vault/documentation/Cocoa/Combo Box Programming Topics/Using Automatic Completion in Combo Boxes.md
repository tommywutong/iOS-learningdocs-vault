---
title: Combo Box Programming Topics
apple_id: 10000020i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/Tasks/AutocompletionComboBoxes.html
archived_at: '2026-07-15T07:13:41.848552Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Combo Box Programming Topics](Introduction%20to%20Combo%20Boxes.md)


[Next](Document%20Revision%20History.md)[Previous](Setting%20the%20Combo%20Box%E2%80%99s%20Value.md)

# Using Automatic Completion in Combo Boxes

A combo box can perform automatic completion, trying to complete what the user enters into the text field with an item from the pop-up list. If it does, every time the user enters characters at the end of the text field, the combo box calls the NSComboBoxCell method `completedString:`. If `completedString:` returns a string that’s longer than the existing string, the combo box replaces the existing string with the returned string, and selects the additional characters. If the user adds characters somewhere besides the end of the string or deletes characters, the combo box does not try to complete it.

The default implementation of `completedString:` first checks whether the combo box uses a data source and whether the data source responds to `comboBox:completedString:` or `comboBoxCell:completedString:`. If so, the combo box cell returns that method’s return value. Otherwise, this method goes through the combo box’s items one-by-one and returns the first item which starts with the string that the user entered. This comparison is case-sensitive.

To read and set whether a combo box performs completion, use `completes` and `setCompletes:`. By default, it does not.

[Next](Document%20Revision%20History.md)[Previous](Setting%20the%20Combo%20Box%E2%80%99s%20Value.md)

