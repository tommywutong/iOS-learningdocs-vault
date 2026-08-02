---
title: 事件驱动 XML 编程指南
apple_id: 10000186i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/XMLParsing/Articles/ValidatingXML.html
archived_at: '2026-07-15T07:21:28.081207Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [事件驱动 XML 编程指南](Introduction%20to%20Event-Driven%20XML%20Programming%20Guide%20for%20Cocoa.md)


[下一篇](XML%20Glossary.md) [上一篇](Constructing%20XML%20Tree%20Structures.md)

# 验证技巧与方法

验证是确保 XML 文档符合 DTD（Document Type Definition，文档类型定义）等语言模式所指定逻辑结构规则的过程。XML 文档可能格式良好（即遵守 XML 语法规则），但同时无效。例如，本应仅包含文本内容的元素可能包含子元素，或者元素可能缺少必需属性。

为了执行验证，可以构建 XML 文档模式的树，使其与表示文档实际内容的树结构相对应（请参阅[构建 XML 树结构](Constructing%20XML%20Tree%20Structures.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dqlkcineukqkcivcq)）。模式树以简洁、抽象的方式呈现文档_应有的_结构。模式树中的节点并不表示文档的实际元素和文本，而是表达文档各部分组合方式的规则。验证过程会依据模式规则检查文档的实际元素、属性及其他部分，确认文档是否符合要求。如果应用程序发现任何不符合要求之处，可以通知用户，并可要求用户修复错误。你既可以在首次读取和处理 XML 文档时验证它，也可以在用户之后尝试对其进行任何更改时再次验证。

由于 NSXMLParser 编程接口只用于报告 XML 结构和 DTD 声明，本文将重点讨论 DTD 这种语言模式。不过，如果使用 RELAX NG 等基于 XML 的语言模式，NSXMLParser 可以像处理其他 XML 文件一样处理该模式，并将所发现的内容报告给委托。你可以使用由此获取的数据执行验证。

有关构建规则的内容主要讨论元素声明和属性声明，因为它们是最常见也最重要的声明类型。[处理其他声明](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi3dsljrgaydembtgq)简要讨论了如何处理实体声明和记法声明等其他声明。

NSXMLParser 类会将它在文档中遇到的 DTD 声明报告给委托（前提是委托实现了必要的方法）。如果使用的语言模式是 DTD，NSXMLParser 可以帮助你获取验证所需的数据，也可将这些数据用于其他目的，例如在动态构建对象（如菜单模板）时强制保证正确性。

NSXMLParser 类定义了六个委托方法，解析器在内部或外部来源中遇到 DTD 声明时会调用这些方法。这些方法的形式如下：

`parser:found`_Type_`DeclarationWithName:`...

第三个参数及其后的参数取决于声明类型。以下列表简要说明了与 DTD 声明相关的 NSXMLParser 委托方法。

__`- parser:foundElementDeclarationWithName:model:`__：示例：`<!ELEMENT dictionary (documentation?, suite+)>`

__`- parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:`__：示例：`<!ATTLIST dictionary title CDATA #IMPLIED >`

__`- parser:foundInternalEntityDeclarationWithName:value:`__：示例：`<!ENTITY % OSType "CDATA">`

__`- parser:foundExternalEntityDeclarationWithName:publicID:systemID:`__：示例：`<!ENTITY name SYSTEM "name.xml">`

__`- parser:foundNotationDeclarationWithName:publicID:systemID:`__：示例：`<!NOTATION img PUBLIC "urn:mime:image/jpeg">`

__`- parser:foundUnparsedEntityDeclarationWithName:publicID:systemID: notationName:`__：示例：`<!ENTITY corplogo SYSTEM "logo.jpg" NDATA img>`

XML 文档通常会在靠近开头的 `DOCTYPE` 声明中标识一个外部 DTD 文件，该文件中的声明规定了文档的逻辑结构。例如，以下 `DOCTYPE` 声明表示，可以通过系统标识符“addresses.dtd”找到与根元素“addresses”相关的 DTD。

```xml
<!DOCTYPE addresses SYSTEM "addresses.dtd">
```

系统标识符通常假定 DTD 位于标准文件系统位置，例如 `/System/Library/DTDs`。处理开始时，NSXMLParser 委托有机会解析此外部实体，并向解析器提供要解析的 DTD 声明列表。

1. 准备 NSXMLParser 实例时，向其发送 `setShouldResolveExternalEntities:` 消息，并将参数设为 `YES`。
2. 实现委托方法 `parser:resolveExternalEntityName:systemID:`，将外部 DTD 文件中的声明作为 NSData 对象返回。

如果 DTD 声明位于 XML 文档内部，委托会自动收到 DTD 声明消息（当然，前提是它实现了相关方法）。

正如元素通常是 XML 文档中最常见的结构一样，元素声明也是 DTD 中最常见的声明。它们表达由子元素、文本及其他组成部分构成元素的规则。

元素声明由三部分组成：`!ELEMENT` 关键字、元素名称和内容模型。内容模型是名称之后直至右尖括号之前的所有内容。请看以下示例：

```xml
<!ELEMENT cocoa EMPTY>
<!ELEMENT keyboard (layouts+, modifierMap+, keyMapSet+, actions*, terminators*)>
<!ELEMENT dict (key, %plistObject;)*>
<!ELEMENT string (#PCDATA)>
```

内容模型可以指定无内容（`EMPTY`）、任意内容（`ANY`，较为少见）、文本内容（`#PCDATA`）以及子元素。它可以按名称标识子元素，也可以通过实体引用标识（例如上面第三个示例中的 `%plistObject;`）。模型还可以指定混合内容，即元素可以按任意顺序包含文本和子元素。通过出现次数修饰符（`*`、`+`、`?`）和其他语法约定，内容模型还可以指定子元素的顺序、元素是必需还是可选、元素可出现的次数，以及元素之间可接受的选择。出现次数修饰符既可以应用于元素组（括号内），也可以应用于单个元素。

验证所需的工作是检查元素声明的内容模型，并推导出该元素的组成规则。一种方法是为每种规则类型及规则作用范围（单个元素或元素组）设计相应的类。随后，可通过元素名称将该规则类的实例与元素关联。验证期间，会针对元素的当前成员或可能的成员查询这些实例。

表 1 列出了可从元素声明的内容模型推导出的最重要规则。

__表 1__　可能的元素验证规则

| 规则 | 内容模型示例 | 说明 |
| --- | --- | --- |
| 仅文本内容 | `(#PCDATA)` |  |
| 混合内容 | `(#PCDATA \| bold \| italic)` | 此处竖线的含义与“选择”不同；存在 `#PCDATA` 时，竖线表示文本和子元素可以混合出现。 |
| 无内容 | `EMPTY` | 用于标志类型的值。 |
| 必需顺序 | `(name, address, phone)` | 逗号表示规定的顺序。 |
| 选择 | `(read \| write \| readwrite)` | 如果成员中没有 `#PCDATA`（请参阅“混合内容”），竖线表示必须使用所列元素之一。 |
| 恰好出现一次 | `(name, address, phone)` | 无修饰标点。可应用于单个元素或元素组。 |
| 出现零次或多次 | `(%plistObject;)*` | 出现次数修饰符为星号（“\*”）。可应用于单个元素或元素组。 |
| 出现一次或多次 | `(property+)` | 出现次数修饰符为加号（“+”）。可应用于单个元素或元素组。 |
| 出现零次或一次 | `(%implementation;?)` | 出现次数修饰符为问号（“?”）。可应用于单个元素或元素组。 |

元素通常带有与之关联的属性，因此在 DTD 中经常会遇到属性列表声明。属性列表声明使用与元素声明不同的语法指定属性规则。它们依次指定关联的元素、属性名称、属性类型和默认值。例如，声明

```xml
<!ATTLIST modifierMap defaultIndex NMTOKEN #REQUIRED >
```

表示与 `modifierMap` 元素关联的 `defaultIndex` 属性属于 `NMTOKEN` 类型（即它必须是有效的 XML 名称）；作为默认值提供的 `#REQUIRED` 关键字表示必须为该属性提供值。

当 NSXMLParser 实例遇到属性列表声明时，会向其委托发送 `parser:foundAttributeDeclarationWithName:forElement:type:defaultValue:`。传入的参数包括属性名称、关联元素、属性类型及其默认值。属性规则由最后两个参数（类型和默认值）的组合推导而来。表 2 列出了可从属性列表声明构建的一些规则。

__表 2__　可能的属性验证规则

| 规则 | 关键字或示例 | 类型或默认值 | 说明 |
| --- | --- | --- | --- |
| 唯一值 | `ID` | 类型 | 属性值在 XML 文档中必须唯一。 |
| 必需值 | `#REQUIRED` | 默认值 | 必须在文档中指定属性值。 |
| 引用唯一属性值 | `IDREF`、`IDREFS` | 类型 | 值必须引用文档其他位置的有效 `ID` 类型值。`IDREFS` 指定一组 `ID` 引用（位于括号内）。 |
| 有效的 XML 名称 | `NMTOKEN`、`NMTOKENS` | 类型 | 值必须是有效的 XML 名称（包括实体引用）。`NMTOKENS` 指定一组 XML 名称（位于括号内）。 |
| 固定值 | `#FIXED "value"` | 默认值 | 值必须为“value”。 |
| 列表中的有效 XML 名称 | `(name \| address \| phone)` | 类型 | 属性枚举：值必须是括号内的 XML 名称之一。 |
| 列表中的有效已定义类型 | `NOTATION (tiff \| gif \| jpg)` | 类型 | 属性枚举：值必须是括号内已定义的类型之一。 |

实体声明和记法声明等其他 DTD 声明不如元素声明和属性列表声明常见。查阅一些 DTD 文档后，你可以很容易地为这些其他声明推导出规则结构。不过，需要注意以下几点：

- 需要记录实体声明，以防它们被用作元素声明内容模型的一部分。
- 由于记法可以用作属性类型，因此也应对其进行跟踪。

[下一篇](XML%20Glossary.md) [上一篇](Constructing%20XML%20Tree%20Structures.md)
