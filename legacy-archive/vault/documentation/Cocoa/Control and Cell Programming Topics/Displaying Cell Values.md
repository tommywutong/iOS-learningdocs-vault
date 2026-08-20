---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Tasks/DisplayingCellValues.html
archived_at: '2026-07-15T07:13:48.375602Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Control and Cell Programming Topics](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)


[Next](Changing%20the%20Cell%20for%20a%20Control.md)[Previous](Validating%20Control%20Entries.md)

# Displaying Cell Values

Every [NSCell](https://developer.apple.com/documentation/appkit/nscell) that displays text has a value associated with it. The `NSCell` object stores that value as an object of potentially any type, displays it as an `NSString` object, and returns it as a primary value or string object, according to what’s requested (`intValue`, `floatValue`, `stringValue`, and so on). Formatters are objects associated with `NSCell` objects (through `setFormatter:`) that translate a cell’s object value to its it textual representation and convert what users type into the underlying object. `NSCell` objects have built-in formatters to handle common string and numeric (`int`, `float`, `double`) translations. In addition, you can implement your own formatters to provide specialized object translation; see _[Data Formatting Guide](../Data%20Formatting%20Guide/Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazds2i)_.

The text that an `NSCell` object displays and stores can be an attributed string. Several methods help to set and get attributed-string values, including `setAttributedStringValue:` and `setImportsGraphics:`.

[Next](Changing%20the%20Cell%20for%20a%20Control.md)[Previous](Validating%20Control%20Entries.md)

