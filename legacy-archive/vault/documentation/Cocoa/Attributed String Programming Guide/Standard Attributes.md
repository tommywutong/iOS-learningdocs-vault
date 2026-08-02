---
title: 属性字符串编程指南
apple_id: 10000036i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/Articles/standardAttributes.html
archived_at: '2026-07-15T05:25:49.196072Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [属性字符串编程指南](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)


[下一页](Document%20Revision%20History.md)[上一页](Word%20and%20Line%20Calculations%20in%20Attributed%20Strings.md)

# 标准属性

表 1 中列出的标识符都是包含属性名称的全局 `NSString` 常量。值类（value class）指的是与该属性对应的值所属的类。

__表 1__  Table of standard attributes

| 属性标识符 | 值类 | 默认值 |
| --- | --- | --- |
| `NSAttachmentAttributeName` | `NSTextAttachment` | none (no attachment) |
| `NSBackgroundColorAttributeName` | `NSColor` | none (no background) |
| `NSBaselineOffsetAttributeName` | `NSNumber`, as a float | 0.0 |
| `NSFontAttributeName` | `NSFont` | Helvetica 12-point |
| `NSForegroundColorAttributeName` | `NSColor` | black |
| `NSKernAttributeName` | `NSNumber`, as a float | 0.0 |
| `NSLigatureAttributeName` | `NSNumber`, as an int | 1 (standard ligatures) |
| `NSLinkAttributeName` | `id` | none (no link) |
| `NSParagraphStyleAttributeName` | `NSParagraphStyle` | (as returned by `NSParagraphStyle`’s [defaultParagraphStyle](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1532681-default) method) |
| `NSSuperscriptAttributeName` | `NSNumber`, as an int | 0 |
| `NSUnderlineStyleAttributeName` | `NSNumber`, as an int | none (no underline) |

以下几个属性的具体含义无法仅凭名称直观得知：

- 基线偏移（baseline offset）属性是一个以像素为单位的实际距离，表示字符相对于基线向上（正偏移值）或向下（负偏移值）移动的距离。
- 字距（kerning）属性表示后一个字符相对于其由当前字符字体所定义的默认偏移量应移动多少；正的字距值表示进一步移动，负的字距值表示更靠近当前字符。
- 连字（ligature）属性决定了显示字符串时应使用哪种连字。值为 0 表示只使用对正确渲染文本必不可少的连字，1 表示使用标准连字，2 表示使用所有可用的连字。哪些连字属于标准连字取决于文字体系，也可能取决于字体。例如，阿拉伯文本中许多字符序列都需要连字，此外还拥有一整套用于组合字符的附加连字。英文文本没有必需的连字，通常只有两个标准连字，即“fi”和“fl”——其余的都被视为更高级或更花哨的连字。
- 链接（link）属性指定一个任意对象，当用户点击与 `NSLinkAttributeName` 属性关联的文本范围时，该对象会被传给 `NSTextView` 的 `clickedOnLink:atIndex:` 方法。文本视图的委托对象可以实现 `textView:clickedOnLink:atIndex:` 或 `textView:clickedOnLink:` 来处理该链接对象。否则，默认实现会检查该链接对象是否为 `NSURL` 对象，如果是，则在该 URL 对应的默认应用程序中打开它。
- 上标（superscript）属性表示上标和下标的一个抽象级别。属性字符串的使用者可以按需自行解释该值，可以为每个级别调整相同或不同幅度的基线偏移，也可以更改字体大小，或者两者兼而有之。
- 下划线（underline）属性只定义了两个值，`NSNoUnderlineStyle` 和 `NSSingleUnderlineStyle`，但可以将它们与 `NSUnderlineByWordMask` 及 `NSUnderlineStrikethroughMask` 组合，以扩展其行为。通过以不同组合方式对这些值进行按位或（OR）运算，你可以指定不显示下划线、单条下划线、单条删除线、同时显示下划线和删除线，以及是否对空白字符也绘制该线条。

[下一页](Document%20Revision%20History.md)[上一页](Word%20and%20Line%20Calculations%20in%20Attributed%20Strings.md)

