---
title: Cocoa 编码规范
apple_id: 10000146i
resource_type: Guide
platform: watchOS|iOS|macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CodingGuidelines/Articles/APIAbbreviations.html
archived_at: '2026-07-15T07:13:25.781956Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Cocoa 编码规范](Introduction%20to%20Coding%20Guidelines%20for%20Cocoa.md)


[下一页](Tips%20and%20Techniques%20for%20Framework%20Developers.md)[上一页](Naming%20Properties%20and%20Data%20Types.md)

# 可接受的缩写与首字母缩略词

一般来说，设计编程接口时不应该缩写名称（参见[总体原则](Code%20Naming%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dcljrgaydcnzvge)）。不过，下面列出的这些缩写（abbreviation）要么已经约定俗成，要么过去一直在用，因此你可以继续使用它们。关于缩写还有另外两点需要说明：

- 与标准 C 库中沿用已久的形式相同的缩写是允许的，例如“`alloc`”和“`getc`”。
- 在参数名中你可以更自由地使用缩写（例如“`imageRep`”、“`col`”（表示“column”）、“`obj`”和“`otherWin`”）。

| 缩写 | 含义与说明 |
| --- | --- |
| alloc | Allocate，分配。 |
| alt | Alternate，备选。 |
| app | Application，应用程序。例如全局应用程序对象 NSApp。不过在[委托](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14)方法、通知等场合，“application”要完整拼写。 |
| calc | Calculate，计算。 |
| dealloc | Deallocate，释放。 |
| func | Function，函数。 |
| horiz | Horizontal，水平。 |
| info | Information，信息。 |
| init | Initialize，初始化（用于[初始化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21)新对象的方法）。 |
| int | Integer，整数（指 C 的 `int`；对于 [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) 类型的值，请用 `integer`）。 |
| max | Maximum，最大值。 |
| min | Minimum，最小值。 |
| msg | [Message](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)，消息。 |
| nib | Interface Builder 归档文件。 |
| pboard | Pasteboard，粘贴板（但仅用于常量）。 |
| rect | Rectangle，矩形。 |
| Rep | Representation，表示形式（用于类名，如 `NSBitmapImageRep`）。 |
| temp | Temporary，临时。 |
| vert | Vertical，垂直。 |

你可以用计算机行业中通用的缩写和首字母缩略词（acronym）来代替它们所表示的词。下面是一些较为知名的首字母缩略词：

- ASCII
- PDF
- XML
- HTML
- URL
- RTF
- HTTP
- TIFF
- JPG
- PNG
- GIF
- LZW
- ROM
- RGB
- CMYK
- MIDI
- FTP

[下一页](Tips%20and%20Techniques%20for%20Framework%20Developers.md)[上一页](Naming%20Properties%20and%20Data%20Types.md)

