---
title: 属性字符串编程指南
apple_id: 10000036i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/Tasks/ChangingAttrStrings.html
archived_at: '2026-07-15T05:25:51.871896Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [属性字符串编程指南](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)


[下一页](Drawing%20Attributed%20Strings.md)[上一页](Accessing%20Attributes.md)

# 更改属性字符串

`NSMutableAttributedString` 声明了若干用于更改字符和属性的方法。你必须注意，在将属性值传给属性字符串之后，不要再修改这些属性值。此外，如果你修改了属性字符串，还可能需要修复由此引入的不一致问题。

`NSMutableAttributedString` 声明了若干用于更改字符和属性的方法，例如基础方法 `replaceCharactersInRange:withString:` 和 `setAttributes:range:`，或者更为便捷的 `addAttribute:value:range:`、`applyFontTraits:range:` 等方法。

下面的示例展示了如何为属性字符串中的选定范围指定链接属性、为文本添加下划线并将其颜色设为蓝色。请注意，_链接属性的值可以由你自行定义，如何在链接被选中时解释该值也由你决定_——参见[访问属性](Accessing%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge3dclkciffeeqsdijeq)——不过通常会使用字符串或 URL 作为值。关于示例中 `beginEditing` 和 `endEditing` 的作用说明，请参阅[修复不一致问题](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge3deljrg43danby)。

```objc
NSMutableAttributedString *string; // assume string exists
NSRange selectedRange; // assume this is set

NSURL *linkURL = [NSURL URLWithString:@"http://www.apple.com/"];

[string beginEditing];
[string addAttribute:NSLinkAttributeName
               value:linkURL
               range:selectedRange];

[string addAttribute:NSForegroundColorAttributeName
               value:[NSColor blueColor]
               range:selectedRange];

[string addAttribute:NSUnderlineStyleAttributeName
               value:[NSNumber numberWithInt:NSSingleUnderlineStyle]
               range:selectedRange];
[string endEditing];
```

赋予属性字符串的属性值会成为该字符串的所有物，其他对象不应“绕过属性字符串”对其进行修改。这样做可能导致属性字符串内部状态变得不一致。主要有以下两个原因：

- 属性值在属性字符串中的传播方式是不可预测的。如果你更改了该值，实际被编辑到的属性字符串范围可能比你想象的要大。事实上，该值可能已经被复制到撤销栈中，或者复制到了完全不同的文档中，等等。
- 属性字符串会对属性进行缓存和去重（uniquing），这一机制假定属性值不会发生变化。也就是说，一旦某个属性值被设置，就默认其 `isEqual:` 和 `hash` 不会再改变。

如果你必须更改属性值，并且确定这一更改会正确地应用于相应范围，可以采取以下两种策略：

- 使用一个 `isEqual:` 和 `hash` 并不依赖于你要修改的那些值的属性值。
- 使用间接方式：将属性值用作查找键，指向一个可以更改实际值的表。例如，这可能适用于实现类似“样式表”的属性。

用于更改可变属性字符串的所有方法都会正确更新字符与属性之间的映射关系，但更改之后仍可能产生一些不一致情况。以下是一些属性一致性要求的示例：

- 段落样式必须适用于整个段落。
- 特定文字体系只能被分配支持它的字体。例如，汉字和阿拉伯字符不能使用 Times-Roman 字体，必须重新分配支持这些文字体系的字体。
- 从字符串中删除附件字符时，需要释放相应的附件对象。同样，移除附件对象时，也需要从字符串中删除相应的附件字符。
- 一个将所有语言关键字都显示为粗体的代码编辑应用程序，可以在用户更改字体或编辑文本时自动指定该属性。

Application Kit 对 `NSMutableAttributedString` 的扩展定义了一些方法，用于在发生更改时修复这些不一致情况。这样可以在较底层清理属性，向更高层隐藏潜在的问题，并在属性发生变化时非常干净地更新显示。共有四个用于修复属性的方法和两个用于对编辑更改进行分组的方法：

- `fixAttributesInRange:`
- `fixAttachmentAttributeInRange:`
- `fixFontAttributeInRange:`
- `fixParagraphStyleAttributeInRange:`
- `beginEditing`
- `endEditing`

第一个方法 `fixAttributesInRange:` 会调用其余三个 `fix...` 方法，分别用于清理已删除的附件引用、字体属性和段落属性。各方法的具体说明解释了每种情况下的清理内容。

`NSMutableAttributedString` 提供了 `beginEditing` 和 `endEditing` 方法，供 `NSMutableAttributedString` 的子类重写。这些方法使子类的实例能够记录或缓冲一组更改，并在收到 `endEditing` 消息时进行自我清理。`endEditing` 方法还允许接收者通知任何观察者自身已发生更改。例如，`NSTextStorage` 对 `endEditing` 的实现会修复已更改的属性，然后通知其布局管理器需要重新排版并重新显示文本。默认实现则什么也不做。

[下一页](Drawing%20Attributed%20Strings.md)[上一页](Accessing%20Attributes.md)

