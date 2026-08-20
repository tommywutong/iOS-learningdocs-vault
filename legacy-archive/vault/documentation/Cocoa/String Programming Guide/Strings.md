---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/Strings.html
archived_at: '2026-07-15T07:19:32.680664Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Creating%20and%20Converting%20String%20Objects.md)[上一页](Introduction%20to%20String%20Programming%20Guide.md)

# 字符串

在 Cocoa 和 Cocoa Touch [框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)中，字符串对象用于表示字符串。把字符串表示成[对象](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ValueObject.html#//apple_ref/doc/uid/TP40008195-CH51)，使你能够在任何使用其他对象的地方使用字符串。这样做还带来了封装的好处：字符串对象可以为了效率而采用任意所需的编码和存储方式，同时对外仅表现为字符数组。

字符串对象在实现上是一个 Unicode 字符数组（换句话说，就是一段文本）。[不可变](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)字符串是指在创建时就已确定、此后无法更改的文本。要创建和管理不可变字符串，请使用 `NSString` 类。要构造和管理创建之后仍可修改的字符串，请使用 `NSMutableString`。

你用 `NSString` 和 `NSMutableString` 创建出来的对象称为字符串对象（在不会引起混淆时，也可以简称为字符串）。术语 _C 字符串_ 指的是标准 C 的 `char *` 类型。

字符串对象对外表现为一个 Unicode 字符数组。你可以用 [length](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/length) 方法确定它包含多少个字符，并用 [characterAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/characterAtIndex:) 方法取出指定位置的字符。这两个“原始（primitive）”方法提供了对字符串对象的基本访问能力。不过，字符串大多是在更高的层面上使用的，此时字符串被当作单个整体来处理：你会拿字符串互相比较、在其中搜索子串、把它们组合成新的字符串，等等。如果你需要逐个字符地访问字符串对象，就必须理解 Unicode 字符编码——尤其是与组合字符序列相关的问题。详情请参阅：

- _The Unicode Standard, Version 4.0_。The Unicode Consortium 著。波士顿：Addison-Wesley，2003 年。ISBN 0-321-18578-1。
- Unicode 联盟网站：[http://www.unicode.org/](http://www.unicode.org/)。

[下一页](Creating%20and%20Converting%20String%20Objects.md)[上一页](Introduction%20to%20String%20Programming%20Guide.md)

