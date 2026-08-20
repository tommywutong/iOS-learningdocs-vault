---
title: 数据格式化指南
apple_id: 10000029i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/Articles/CreatingACustomFormatter.html
archived_at: '2026-07-15T07:14:33.924047Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [数据格式化指南](Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md)


[下一页](Document%20Revision%20History.md)[上一页](Formatters%20and%20User%20Interface%20Elements.md)

# 创建自定义格式化器

你可以创建 `NSFormatter` 的自定义子类，以格式化日期和数字之外的其他数据表示形式。

要创建 `NSFormatter` 的子类，你至少必须[重写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57)以下方法：

- [stringForObjectValue:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSFormatter/Description.html#//apple_ref/occ/instm/NSFormatter/stringForObjectValue:)
- [getObjectValue:forString:errorDescription:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSFormatter/Description.html#//apple_ref/occ/instm/NSFormatter/getObjectValue:forString:errorDescription:)

在第一个方法中，你将单元格的对象转换为字符串表示形式；在第二个方法中，你将字符串转换为与该单元格关联的对象。

你也可以重写 [attributedStringForObjectValue:withDefaultAttributes:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSFormatter/Description.html#//apple_ref/occ/instm/NSFormatter/attributedStringForObjectValue:withDefaultAttributes:) 方法，将对象转换为带有关联属性的字符串。例如，如果你希望负的金额以红色显示，可以让该方法返回一个带有红色文本属性的字符串。在 `attributedStringForObjectValue:withDefaultAttributes:` 中，通过调用 `stringForObjectValue:` 获取不带属性的字符串，然后对该字符串应用相应的属性。

如果用于编辑的字符串必须与用于显示的字符串不同——例如，货币字段的显示版本带有美元符号，而编辑版本没有——除了 `stringForObjectValue:` 之外，还应实现 `editingStringForObjectValue:`。

在 OS X 中，你可以使用 [isPartialStringValid:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:](https://developer.apple.com/documentation/foundation/nsformatter/1415263-ispartialstringvalid) 和 [isPartialStringValid:newEditingString:errorDescription:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSFormatter/Description.html#//apple_ref/occ/instm/NSFormatter/isPartialStringValid:newEditingString:errorDescription:) 方法，在用户每次按键时编辑单元格的文本内容，并阻止用户输入无效字符。你可以将这种动态编辑应用于诸如社会安全号码之类的场景：数据录入者只需输入一次数字，因为格式化器会自动插入分隔符字符。

[下一页](Document%20Revision%20History.md)[上一页](Formatters%20and%20User%20Interface%20Elements.md)

