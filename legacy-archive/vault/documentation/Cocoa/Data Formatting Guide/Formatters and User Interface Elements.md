---
title: 数据格式化指南
apple_id: 10000029i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/Articles/dfCells.html
archived_at: '2026-07-15T07:14:34.424213Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [数据格式化指南](Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md)


[下一页](Creating%20a%20Custom%20Formatter.md)[上一页](Number%20Formatters.md)

# 格式化器与用户界面元素

本文介绍如何在 Cocoa 中将格式化器与单元格关联。本文不适用于 iOS。

在 Cocoa 中，显示文本但以任意对象作为其内容的用户界面单元格可以使用格式化器来处理输入和输出。当单元格被显示时，它会将任意对象转换为文本表示形式。单元格显示对象的方式取决于该单元格是否关联了格式化器。如果单元格没有格式化器，它会使用对象的[本地化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23)表示形式来显示内容。如果单元格有格式化器，它会从格式化器获取格式化后的字符串。当用户在单元格中输入文本时，单元格会使用其格式化器将文本转换为底层对象。

使用格式化器最简单的方式是在 Interface Builder 中，将其从调色板拖到诸如文本字段或表格视图列之类的控件上。

要以编程方式创建格式化器对象并将其附加到单元格，你需要分配一个格式化器实例，并根据需要设置其格式或样式。然后使用 `NSCell` 的 [setFormatter:](https://developer.apple.com/documentation/appkit/nscell/1531115-formatter) 方法将该格式化器实例与单元格关联。以下代码示例创建并配置了一个 `NSNumberFormatter` 实例，并使用 `setFormatter:` 方法将其应用于 `NSTextField` 对象的单元格。

```objc
NSNumberFormatter *numberFormatter = [[NSNumberFormatter alloc] init];
[numberFormatter setNumberStyle:NSNumberFormatterCurrencyStyle];
[[textField cell] setFormatter:numberFormatter];
```

类似地，你也可以以编程方式创建并配置 `NSDateFormatter` 对象实例。以下示例创建了一个日期格式化器，然后将其与某个表单（`contactsForm`）的各个单元格关联。

```objc
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
[dateFormatter setDateStyle:NSDateFormatterMediumStyle];
[dateFormatter setTimeStyle:NSDateFormatterNoStyle];
[[contactsForm cells] makeObjectsPerformSelector:@selector(setFormatter:)
         withObject:dateFormatter]
```

当带有格式化器对象的单元格被复制时，新单元格会对该格式化器对象建立一个强引用，而不是复制它。

当单元格需要显示或编辑其值时，它会将对象传递给格式化器，由格式化器返回格式化后的字符串。当用户输入字符串，或以编程方式向单元格写入字符串（使用 `setStringValue`）时，单元格会从格式化器获取对应的对象。

`NSControl` 提供了[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)方法，用于处理 `NSFormatter` 的 `getObjectValue:forString:errorDescription:`、`isPartialStringValid:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:` 以及 `isPartialStringValid:newEditingString:errorDescription:` 方法实现中返回的错误。这些委托方法分别是 `control:didFailToFormatString:errorDescription:` 和 `control:didFailToValidatePartialString:errorDescription:`。

[下一页](Creating%20a%20Custom%20Formatter.md)[上一页](Number%20Formatters.md)

