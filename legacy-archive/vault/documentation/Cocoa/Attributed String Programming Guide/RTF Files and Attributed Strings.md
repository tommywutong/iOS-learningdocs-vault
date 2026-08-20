---
title: 属性字符串编程指南
apple_id: 10000036i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/Tasks/RTFAndAttrStrings.html
archived_at: '2026-07-15T05:25:53.823509Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [属性字符串编程指南](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)


[下一页](Formatted%20Documents%20and%20Attributed%20Strings.md)[上一页](Drawing%20Attributed%20Strings.md)

# RTF 文件与属性字符串

富文本格式（RTF）是由 Microsoft 公司设计的一种文本格式化语言。你可以使用穿插了 RTF 命令、分组和转义序列的纯文本，来表示字符、段落和文档格式属性。RTF 被广泛用作一种文档交换格式，用于在不同应用程序和计算平台之间传输带有格式信息的文档。Apple 使用自定义命令对 RTF 进行了扩展，本章将对此进行说明。

Application Kit 对 [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString) 的扩展增加了对多种常见文档格式（包括 RTF 和 RTFD）进行读写的支持，具体请参阅 [Formatted Documents and Attributed Strings](Formatted%20Documents%20and%20Attributed%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2danrsfvjvomi)。虽然 `NSAttributedString` 专门提供了用于读写 RTF 和 RTFD 数据的便捷方法，但这些方法相较于通用方法并无优势，而且它们缺少实用的 `error:` 参数。

Apple 对 RTF 语言进行了扩展，以支持 Cocoa 文本系统中可用、但标准 RTF 无法表示的文本属性和格式化结构。这些 Apple 扩展采用与标准 RTF 命令、分组和转义相同的形式。RTF 命令由一个反斜杠、后跟一串字母字符（区分大小写）、再后跟一个可选的整数参数值（可正可负）组成。RTF 分组以左花括号（{）开始，后跟 RTF 序列（其中可以嵌套其他分组），并以右花括号（}）结束。RTF 转义由一个反斜杠加一个特殊字符组成，例如 `\{`，表示一个字面上的左花括号，而不是分组的开始。

RTF 包含一个"目的地"（destination）的概念，它是一个包含 RTF 命令、以及可能要插入到文档其他位置（例如脚注）的文本的分组。转义序列 `\*` 表示：不理解其后命令的 RTF 阅读器应当忽略该目的地的内容。

RTF 中的尺寸以 _twip_ 为单位表示——1 twip 等于二十分之一点（point）。

表 1 列出了 Apple 针对字符属性的 RTF 扩展。

__表 1__  字符属性 RTF 扩展

| RTF 序列 | 说明 | 参数 |
| --- | --- | --- |
| \CocoaLigature_N_ | 连字控制 | [NSLigatureAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1524592-ligature) 的值。0 = 无连字，1 = 默认连字，2 = 所有连字。默认值为 1。 |
| \expansion_N_ | 应用于字形的扩展系数 | 2000 \* [NSExpansionAttributeName](https://developer.apple.com/documentation/appkit/nsexpansionattributename) 的值（扩展系数的对数）。默认值为 0。 |
| \obliqueness_N_ | 应用于字形的倾斜 | 2000 \* [NSObliquenessAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1535353-obliqueness) 的值。0 = 无倾斜。默认值为 0。 |
| \fsmilli_N_ | 更精细的字号规格 | 1000 \* 字号。当 \fs 不是整数或半点值时，会在 \fs 之外额外写出；该值会被 \fs 覆盖，因此应紧跟在 \fs 之后写出。默认值由 \fs 决定。 |
| \shadx_N_ \shady_N_ | 阴影偏移，与 \shad 一起写出 | X 和 Y 偏移量，单位为 twip（0 = 无偏移）。默认值分别为 \shadx3 和 \shady-3。 |
| \shadr_N_ | 阴影模糊，与 \shad 一起写出 | 模糊半径，单位为 twip。0 = 无模糊。默认值为 0。 |
| \strikec_N_ | 删除线颜色 | 颜色编号。默认与前景文本颜色相同。 |
| \strikestyle_N_ | 删除线样式，在 \strike、\striked、\strikew 不足以表达时写出 | 样式和图案掩码，[NSObliquenessAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1535353-obliqueness) 的值。0 = 无；0x8000 = 按单词；样式：1 = 单线，2 = 粗线，9 = 双线；图案：0x100 = 点状，0x200 = 短划线，0x300 = 点划线，0x400 = 双点划线。默认值为 0。 |
| \strokec_N_ | 描边颜色 | 颜色编号。默认与前景文本颜色相同。 |
| \strokewidth_N_ | 字形描边宽度，与 \outl 一起写出。 | 20 \* 以字号百分比表示的描边宽度。0 = 无描边。默认值为 0。负值表示字形既有描边又有填充；描边宽度取该参数的绝对值。 |
| \ulstyle_N_ | 下划线样式，在标准 \ul 命令不足以表达时写出 | 样式和图案掩码，[NSUnderlineStyleAttributeName](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1524865-underlinestyle) 的值。0 = 无；0x8000 = 按单词；样式：1 = 单线，2 = 粗线，9 = 双线；图案：0x100 = 点状，0x200 = 短划线，0x300 = 点划线，0x400 = 双点划线。默认值为 0。 |
| {{\NeXTGraphic _attachment_ \width_N_ \height_N_} _string_} | 与 RTF 文件位于同一文件夹中（通常打包在 RTFD 文档内）的附件文件名 | _attachment_ 是附件文件名，以 UTF-8 编码并经过适当的 RTF 转义。width 和 height 参数可选地以 twip 为单位指定附件大小。_string_ 始终为 0xAC。 |
| {{}{\\*\glid_N_ _basestring_}_string_} | 显式指定字形的字形 ID。（额外的 {} 用于绕开 OS X 10.2 及更早版本中一个 RTF 阅读器的 bug。） | 字形标识符（\glid 的参数）。_basestring_ 是该字形 ID 打算覆盖的字符串；该属性随后会应用到指定的 _string_ 上。通常 _string_ 与 _basestring_ 相同，不过 _string_ 中也可能包含 _basestring_ 的多个实例。 |
| {{}{\\*\glid_N_ _basestring_\glcol_N_} _string_} | 显式指定字形的字形 ID | 字符标识符（\glid 的参数）和字符集合（\glcol 的参数）。集合 ID：0 = identity，1 = Adobe-CNS1，2 = Adobe-GB1，3 = Adobe-Japan1，4 = Adobe-Japan2，5 = Adobe-Korea。 |
| {{}{\\*\glid _basestring_\glnam _glyphname_}_string_} | 显式指定字形的字形 ID | _glyphname_ 是以 UTF-8 编码的字形名称。 |
| \AppleTypeServicesU_N_ | 字符外形控制 | [NSCharacterShapeAttributeName](https://developer.apple.com/documentation/appkit/nscharactershapeattributename) 的值。该值被解释为 Apple Type Services 的 kCharacterShapeType 选择器 + 1。值为 0 时禁用该属性。默认值为 0。 |

表 2 列出了 Apple 针对段落属性的 RTF 扩展。

__表 2__  段落属性 RTF 扩展

| RTF 序列 | 说明 | 参数 |
| --- | --- | --- |
| \pardeftab_N_ | 段落的默认制表符间隔 | 制表符间隔值，单位为 twip。0 = 除显式指定的制表符外没有其他制表符。默认值为 0。 |
| \qnatural | 段落的自然文本对齐方式（基于文字系统），与 \ql 一起写出 | 无 |
| \slleading_N_ | 段落行距（NSParagraphStyle 的 lineSpacing 方法） | 行距值，单位为 twip。默认值为 0。 |
| \slmaximum_N_ | 最大行高（NSParagraphStyle 的 maximumLineHeight 方法），与 \sl 一起写出，必要时还需 \slmult | 最大行高值，单位为 twip。默认值为 0，表示无最大限制。 |
| \slminimum_N_ | 最小行高（NSParagraphStyle 的 minimumLineHeight 方法），与 \sl 一起写出，必要时还需 \slmult | 最小行高值，单位为 twip。默认值为 0。 |

表 3 列出了 Apple 针对文档属性的 RTF 扩展。

__表 3__  文档属性 RTF 扩展

| RTF 序列 | 说明 | 参数 |
| --- | --- | --- |
| \readonlydoc_N_ | 只读文档。这与文件系统的权限或文件所有权无关；它只是一个提示，表示如果查看器或编辑器支持，该文档应以只读方式呈现给用户。 | 0 = 非只读，1 = 只读。默认值为 0。 |
| \cocoartf_N_ | Cocoa RTF 写入器版本号。这是 Apple 用来标识写出该文档所用 RTF 写入器版本号的数字。 | 递增的版本号。0 = 非 Cocoa 写入器，1 = NextStep，40 = OpenStep，100 = OS X v10.0，102 = 10.2。（除了未来版本会递增这个数字之外，不应对该数字未来的变化方式做任何其他假设。）默认值为 0，不过会使用一些启发式方法来识别 OS X 之前的文档。 |
| \viewh_N_ \vieww_N_ | 用于显示该文档的显示区域大小（不是窗口或视图大小） | 显示区域尺寸，单位为 twip。默认值未指定。 |

[下一页](Formatted%20Documents%20and%20Attributed%20Strings.md)[上一页](Drawing%20Attributed%20Strings.md)
