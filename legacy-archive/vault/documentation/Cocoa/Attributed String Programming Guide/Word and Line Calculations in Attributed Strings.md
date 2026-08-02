---
title: 属性字符串编程指南
apple_id: 10000036i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/Tasks/WordCalcAttrStrings.html
archived_at: '2026-07-15T05:25:54.130535Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [属性字符串编程指南](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)


[Next](Standard%20Attributes.md)[Previous](Formatted%20Documents%20and%20Attributed%20Strings.md)

# 属性字符串中的单词与行计算

Application Kit 对 `NSAttributedString` 的扩展支持文本编辑器中常见的行为：通过 [doubleClickAtIndex:](https://developer.apple.com/documentation/foundation/nsattributedstring/1534748-doubleclickatindex) 方法实现双击选中单词，并通过 [nextWordFromIndex:forward:](https://developer.apple.com/documentation/foundation/nsattributedstring/1535305-nextwordfromindex) 方法查找单词边界。它还通过 [lineBreakBeforeIndex:withinRange:](https://developer.apple.com/documentation/foundation/nsattributedstring/1526887-linebreak) 方法计算换行位置。

[Next](Standard%20Attributes.md)[Previous](Formatted%20Documents%20and%20Attributed%20Strings.md)

