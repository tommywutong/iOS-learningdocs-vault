---
title: 属性列表编程指南
apple_id: 10000048i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/AboutPropertyLists/AboutPropertyLists.html
archived_at: '2026-07-15T07:18:02.536786Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [属性列表编程指南](Introduction%20to%20Property%20Lists.md)


[下一页](Creating%20Property%20Lists%20Programmatically.md)[上一页](Quick%20Start%20for%20Property%20Lists.md)

# 关于属性列表

属性列表（property list）是 Cocoa 和 Core Foundation 使用的一种结构化数据表示形式，它提供了一种便捷的方式来存储、组织和访问标准类型的数据。人们通常把它口头称作“plist”。OS X 和 iOS 上的应用程序及其他软件大量使用属性列表。例如，OS X 的 Finder 就通过 [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4) 用属性列表来存储文件和目录的属性。iOS 上的应用程序在自己的 Settings bundle 中用属性列表定义要展示给用户的选项列表。本节解释什么是属性列表，以及什么时候应该使用它。

属性列表建立在一种用于表达简单数据层次结构的抽象之上。属性列表中的数据项只能是有限的几种类型。有些类型表示基本值，另一些则是值的容器。基本类型有字符串、数字、二进制数据、日期和布尔值。容器类型有数组（值的带索引的[集合](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10)）和字典（其中每个值都由一个键来标识的集合）。容器既可以包含基本类型，也可以包含其他容器。因此，你可以有一个由字典构成的数组，而其中每个字典又可以包含其他数组和字典，以及各种基本类型。这个层次结构的顶端是根属性列表对象，它几乎总是一个字典或数组。不过要注意，根属性列表对象并非必须是字典或数组；例如，你可以只有一个字符串、数字或日期，这个基本值本身就能构成一个属性列表。

由这个基本抽象衍生出属性列表数据的静态表示和属性列表的运行时表示。属性列表的静态表示用于存储，可以是 XML，也可以是二进制数据。（二进制版本是 XML 属性列表的一种更紧凑的形式。）在 XML 中，每种类型都由特定的元素表示。属性列表的运行时表示则基于与这些抽象类型相对应的对象，这些对象既可以是 Cocoa 对象，也可以是 Core Foundation 对象。表 2-1 列出了各种类型及其对应的静态表示和运行时表示。

__表 2-1__  属性列表类型及其各种表示形式

| 抽象类型 | XML 元素 | Cocoa 类 | Core Foundation 类型 |
| --- | --- | --- | --- |
| 数组 | `<array>` | [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) | `CFArray` ([CFArrayRef](https://developer.apple.com/documentation/corefoundation/cfarray)) |
| 字典 | `<dict>` | [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) | `CFDictionary` ([CFDictionaryRef](https://developer.apple.com/documentation/corefoundation/cfdictionaryref)) |
| 字符串 | `<string>` | [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) | `CFString` ([CFStringRef](https://developer.apple.com/documentation/corefoundation/cfstringref)) |
| 数据 | `<data>` | [NSData](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDataClassCluster/Description.html#//apple_ref/occ/cl/NSData) | `CFData` ([CFDataRef](https://developer.apple.com/documentation/corefoundation/cfdata)) |
| 日期 | `<date>` | [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate) | `CFDate` ([CFDateRef](https://developer.apple.com/documentation/corefoundation/cfdateref)) |
| 数字 - 整数 | `<integer>` | [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber) ([intValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/intValue)) | `CFNumber` ([CFNumberRef](https://developer.apple.com/documentation/corefoundation/cfnumberref)，整数值) |
| 数字 - 浮点数 | `<real>` | [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber) ([floatValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/floatValue)) | `CFNumber` ([CFNumberRef](https://developer.apple.com/documentation/corefoundation/cfnumberref)，浮点值) |
| 布尔值 | `<true/>` 或 `<false/>` | [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber) ([boolValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/boolValue) == `YES` 或 [boolValue](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/instm/NSNumber/boolValue) == `NO`) | `CFBoolean` ([CFBooleanRef](https://developer.apple.com/documentation/corefoundation/cfbooleanref) ；[kCFBooleanTrue](https://developer.apple.com/documentation/corefoundation/kcfbooleantrue) 或 [kCFBooleanFalse](https://developer.apple.com/documentation/corefoundation/kcfbooleanfalse)) |

按照惯例，表 2-1 中列出的每一个 Cocoa 和 Core Foundation 对象都称为_属性列表对象_。从概念上讲，你可以把“属性列表”看作所有这些类的抽象超类。如果你从某个方法或函数拿到一个属性列表对象，你可以确定它一定是上述类型之一的实例，但_事先_你未必知道具体是哪一种。如果一个属性列表对象是容器（也就是数组或字典），那么它所包含的全部对象也必须是属性列表对象。如果某个数组或字典包含了不是属性列表对象的对象，你就无法用各种属性列表方法和函数来保存和恢复这个数据层次结构。另外，虽然 `NSDictionary` 和 CFDictionary 对象允许键是任意类型的对象，但只要键不是字符串对象，这些集合就不是属性列表对象。

由于所有这些类型都可以与对应的 Cocoa 类型自动相互转换，你可以对 Cocoa 对象使用 Core Foundation 的属性列表 API。不过在大多数情况下，[NSPropertyListSerialization](https://developer.apple.com/documentation/foundation/nspropertylistserialization) 类提供的方法已经足够灵活。

许多应用程序都需要某种机制来存储稍后要用到的信息。如果你需要存储的持久化数据量不大——比如小于几百 KB——属性列表就提供了一种统一而便捷的方式来组织、存储和访问这些数据。

在某些场景下，属性列表这套架构可能不够用。如果你需要存储大型、复杂的对象图，或者需要存储属性列表架构不支持的对象，又或者需要保留对象的可变性设置，那就应该使用[归档](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Archiving.html#//apple_ref/doc/uid/TP40008195-CH1)。更多信息请参阅 _[归档与序列化编程指南](../Archives%20and%20Serializations%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2do2i)_。

如果你想实现用户偏好设置或应用程序偏好设置，Cocoa 提供了专门为此设计的类。虽然用户默认设置系统确实用属性列表来存储信息，但你不必直接访问这些 plist。更多信息请参阅 _[偏好设置编程指南](../Preferences%20and%20Settings%20Programming%20Guide/About%20Preferences%20and%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2ts2i)_ 和 _[Core Foundation 偏好设置编程主题](../../Core%20Foundation/Preferences%20Programming%20Topics%20for%20Core%20Foundation/Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezds2i)_。

请注意，属性列表适合存放主要由字符串和数字构成的数据。用它存放大块二进制数据时效率非常低。

属性列表可以用三种方式存储：XML 表示、二进制格式，或者继承自 OpenStep 的“旧式”ASCII 格式。你可以把属性列表序列化为 XML 格式和二进制格式。对于旧式格式，序列化 API 只支持读取。

XML 属性列表比二进制形式更便于移植，而且可以手工编辑；但二进制属性列表要紧凑得多，因此占用内存更少，读写速度也比 XML 属性列表快得多。一般来说，如果你的属性列表规模不大，XML 属性列表带来的好处会超过二进制属性列表在 I/O 速度和紧凑性上的优势。如果数据集很大，那么二进制属性列表、[键控归档](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Archiving.html#//apple_ref/doc/uid/TP40008195-CH1)或自定义数据格式会是更好的选择。

[下一页](Creating%20Property%20Lists%20Programmatically.md)[上一页](Quick%20Start%20for%20Property%20Lists.md)

