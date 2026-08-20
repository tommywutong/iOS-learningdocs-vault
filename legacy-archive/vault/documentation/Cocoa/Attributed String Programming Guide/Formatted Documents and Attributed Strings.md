---
title: 属性字符串编程指南
apple_id: 10000036i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/Articles/HTMLFilesandAttributedStrings.html
archived_at: '2026-07-15T05:25:48.730691Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [属性字符串编程指南](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)


[下一页](Word%20and%20Line%20Calculations%20in%20Attributed%20Strings.md)[上一页](RTF%20Files%20and%20Attributed%20Strings.md)

# 格式化文档与属性字符串

Application Kit 对 [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString) 的扩展增加了对多种常见标记语言的文本格式化命令和文档属性进行读写的支持，包括：

- HTML
- RTF 和 RTFD
- Microsoft Word
- Word XML
- WebKit WebArchive
- ECMA Office Open XML
- OASIS Open Document

在读写文本文档时，这些文档格式由文档属性字典中 [NSDocumentTypeDocumentAttribute](https://developer.apple.com/documentation/uikit/nsdocumenttypedocumentattribute) 键所返回的值来表示。对于所有这些语言，表示文档的文件都同时包含要显示的文本，以及穿插其中的格式化命令。显示这些文档的程序会解释这些命令来对文本进行格式化。格式化命令即"标签"（tag），用于表示段落、标题、换行、图片、超链接等格式化元素。此外，一些命令表示的是文档级别的属性，例如纸张大小、页边距、背景颜色等。

关于 RTF 和 RTFD 的更多具体信息，请参阅 [RTF Files and Attributed Strings](RTF%20Files%20and%20Attributed%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge3dilkcijbuessjijbq)。

Application Kit 对 `NSAttributedString` 的扩展包含两个通用方法，用于通过加载各种格式的文本文档来创建属性字符串。文档格式通过一个选项字典指定，该字典中的键在 _NSAttributedString AppKit Additions Reference_ 的"Option keys for importing documents"一节中有说明。如果指定了 [NSDocumentTypeDocumentOption](https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/1528001-documenttype) 键，并使用 [NSDocumentTypeDocumentAttribute](https://developer.apple.com/documentation/uikit/nsdocumenttypedocumentattribute) 所定义的某个值，文档就会按照指定的格式来解释。如果未指定 [NSDocumentTypeDocumentOption](https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/1528001-documenttype) 键，这些通用方法会检查该文档，并尽力尝试以合适的格式加载它。

用于读取格式化文档的两个通用方法是：

|  |  |
| --- | --- |
| [initWithURL:options:documentAttributes:error:](https://developer.apple.com/documentation/foundation/nsattributedstring/1530490-initwithurl) |  |
| [initWithData:options:documentAttributes:error:](https://developer.apple.com/documentation/foundation/nsattributedstring/1524613-initwithdata) |  |

Application Kit 对 `NSAttributedString` 的扩展还为多种常见文档类型分别定义了若干专用的便捷方法，用于创建属性字符串。此外，`NSMutableAttributedString` 定义了以下方法：

|  |  |
| --- | --- |
| [readFromURL:options:documentAttributes:](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1530903-read) |  |
| [readFromData:options:documentAttributes:](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1525145-read) |  |

属性字符串只为字符和段落存储属性信息，但大多数文档格式还支持更通用的文档级属性，例如纸张大小和页面布局。`NSAttributedString` 的读写方法会将这些指令存储在一个文档属性字典中。如果传递给文档读取方法的文档属性字典不为 `NULL`，该字典会被填充各种文档级属性。所支持的文档属性因文档类型而异。可能的文档属性键及其可取的值，在 _NSAttributedString AppKit Additions Reference_ 的"Document Attributes"一节中有说明。

Application Kit 对 `NSAttributedString` 的扩展还定义了用于生成数据、以将文本文档保存为各种格式的方法。这些方法接受一个文档属性字典，以便写出各种文档级属性；所支持的属性因文档类型而异，与文档读取方法的情况相同。

前两个方法是通用的，即适用于任何受支持的文档类型。它们要求提供一个文档属性字典，其中至少要指定 [NSDocumentTypeDocumentAttribute](https://developer.apple.com/documentation/uikit/nsdocumenttypedocumentattribute) 以确定要写出的格式。

用于写出格式化文档的两个通用方法是：

|  |  |
| --- | --- |
| [dataFromRange:documentAttributes:error:](https://developer.apple.com/documentation/foundation/nsattributedstring/1534090-datafromrange) |  |
| [fileWrapperFromRange:documentAttributes:error:](https://developer.apple.com/documentation/foundation/nsattributedstring/1530461-filewrapperfromrange) |  |

使用 [dataFromRange:documentAttributes:error:](https://developer.apple.com/documentation/foundation/nsattributedstring/1534090-datafromrange) 创建一个可写入磁盘上普通文件的数据对象。当你想在磁盘上创建一个目录结构（例如 RTFD）时，使用 [fileWrapperFromRange:documentAttributes:error:](https://developer.apple.com/documentation/foundation/nsattributedstring/1530461-filewrapperfromrange)。该文件包装器方法会针对适合使用目录结构的文档类型返回一个目录文件包装器；否则返回一个普通文件的文件包装器。

Application Kit 对 `NSAttributedString` 的扩展还为多种常见文档类型分别定义了若干专用的便捷方法，用于生成写出数据。

附件（例如内嵌的图片或文件）在属性字符串中由一个特殊字符和一个属性共同表示。该字符由全局名称 `NSAttachmentCharacter`（`U+FFFC`，Unicode 替换字符）标识，表示字符串中该位置存在一个附件。该属性在字符串中由属性名 `NSAttachmentAttributeName` 标识，其值是一个 `NSTextAttachment` 对象。`NSTextAttachment` 对象包含附件本身的数据，以及在该字符串被绘制时用于显示的图像。

你可以使用 `NSAttributedString` 的 [attributedStringWithAttachment:](https://developer.apple.com/documentation/foundation/nsattributedstring/1508376-init) 类方法构造一个附件字符串，然后使用 [appendAttributedString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/appendAttributedString:) 或 [insertAttributedString:atIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/insertAttributedString:atIndex:) 将其添加到一个可变属性字符串中。

[下一页](Word%20and%20Line%20Calculations%20in%20Attributed%20Strings.md)[上一页](RTF%20Files%20and%20Attributed%20Strings.md)
