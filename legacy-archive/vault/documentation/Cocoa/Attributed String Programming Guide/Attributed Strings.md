---
title: 属性字符串编程指南
apple_id: 10000036i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/Concepts/AttrStrings.html
archived_at: '2026-07-15T05:25:49.706973Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [属性字符串编程指南](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)


[下一页](Creating%20Attributed%20Strings%20in%20Cocoa.md)[上一页](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)

# 属性字符串

属性字符串对象管理字符字符串及与之相关联的一组属性（例如字体和字距），这些属性适用于字符串中的单个字符或某段字符范围。`NSAttributedString` 和 `NSMutableAttributedString` 这两个类分别声明了只读属性字符串和可修改属性字符串的编程接口。Foundation Kit 定义了基本功能，而额外的 Objective-C 方法则定义在 Application Kit 中。Application Kit 还使用 `NSMutableAttributedString` 的一个子类 `NSTextStorage`，为扩展的文本处理系统提供存储（参见 _[文本系统存储层概述](../Text%20System%20Storage%20Layer%20Overview/Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4do2i)_）。

`NSAttributedString` 和 `NSMutableAttributedString` 分别与其 Core Foundation 对应类型 CFAttributedString 和 CFMutableAttributedString 实现了免费桥接（toll-free bridged）。这意味着 Foundation 中的属性字符串在函数或方法调用中可与相应的桥接 Core Foundation 类型互换使用。因此，在某个方法中如果看到 `NSMutableAttributedString *` 类型的参数，你可以传入一个 `CFMutableAttributedStringRef` 类型的变量；同样，在某个函数中如果看到 `CFAttributedStringRef` 类型的参数，你也可以传入一个 `NSAttributedString`（或 `NSMutableAttributedString`）实例。

`NSAttributedString` 并不是 `NSString` 的子类。它内部包含一个 `NSString` 对象，并将属性应用于该对象。这样可以避免简单字符串与属性字符串之间因语义差异而产生歧义，保护属性字符串的使用者。例如，无法简单地在 `NSString` 与属性字符串之间定义相等性。属性字符串类均采用了 `NSCopying` 和 `NSMutableCopying` 协议，因而可以方便地在两种类型之间进行转换。

`NSAttributedString` 和 `NSMutableAttributedString` 在 `NSString` 的基本内容存储之上增加了若干功能：

- 将任意的、由程序员自定义的属性与字符范围相关联。
- 在发生更改后仍能保持属性与字符之间的映射关系（`NSMutableAttributedString`）。
- 支持 RTF，包括文件附件和图形。
- 可在 `NSView` 对象中绘制（注意 Application Kit 同样为 `NSString` 添加了绘制方法）。
- 支持语言学单位（单词）和行的计算。

属性字符串通过名称来标识属性，并将其值作为不透明的 `id` 存储在一个 `NSDictionary` 对象中。例如，文本字体会以 `NSFont` 对象的形式存储在名为 `NSFontAttributeName` 的属性名下。你可以在属性字符串中的任意字符范围上，以任意名称关联任意对象值。

可变属性字符串会在字符被添加、删除以及属性被更改时持续跟踪属性映射关系。它允许你使用 `beginEditing` 和 `endEditing` 方法将成批的编辑操作分组，并通过 `fix...` 系列方法来整合对属性—字符映射关系的更改。

[下一页](Creating%20Attributed%20Strings%20in%20Cocoa.md)[上一页](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)

