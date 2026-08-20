---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/stringsClusters.html
archived_at: '2026-07-15T07:19:34.195719Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Character%20Sets.md)[上一页](Words%2C%20Paragraphs%2C%20and%20Line%20Breaks.md)

# 字符与字素簇

人们习惯把字符串看成一串字符，但在处理 `NSString` 对象，或者更一般地处理 Unicode 字符串时，多数情况下更好的做法是操作子串，而不是操作单个字符。原因在于：用户在文本中感知到的一个字符，在字符串里往往由多个字符表示。`NSString` 提供了大量方法来妥善处理 Unicode 字符串，总体上让符合 Unicode 规范变得很容易，但仍有几点需要留意。

`NSString` 对象在概念上是采用平台字节序的 UTF-16。这并不必然说明它内部采用何种存储机制；它的含义是：`NSString` 的长度、字符索引和范围都以 UTF-16 码元（code unit）为单位来表达，而 `NSString` 方法名中的“character”（字符）一词指的是 16 位、平台字节序的 UTF-16 码元。这是字符串对象常见的约定。多数情况下调用方不必过分在意这一点；只要你处理的是子串，范围索引的确切解释就未必重要。

用于书写现存语言的绝大多数 Unicode 码点（code point）都由单个 UTF-16 码元表示。不过，有些不太常用的 Unicode 码点在 UTF-16 中要用代理对（surrogate pair）表示。代理对是由两个 UTF-16 码元组成的序列，它们取自特定的保留区间，合起来表示单个 Unicode 码点。CFString 提供了在代理对与相应 Unicode 码点的 UTF-32 表示之间进行转换的函数。处理 `NSString` 对象时有一条约束：子串边界通常不应把代理对的两半分开。对于大多数 Cocoa 方法返回的范围，这一点一般会自动满足，但如果你自己构造子串范围，就应当记住这一点。然而，这并不是你需要考虑的唯一约束。

在许多书写系统中，单个字符可能由一个基字符加上重音符号或其他装饰性符号构成。字母与重音的可能组合数量庞大，Unicode 无法把每一种组合都表示为单个码点，因此这类组合通常表示为一个基字符后面跟着一个或多个组合标记（combining mark）。出于兼容性考虑，Unicode 确实为一些最常见的组合提供了单独的码点，它们被称为预组合形式（precomposed form）；Unicode 的规范化变换可以在预组合表示与分解表示之间进行转换。不过，即使一个字符串已经完全预组合，仍有许多组合必须用基字符加组合标记来表示。对于大多数文本处理而言，子串范围的安排应当保证其边界不会把基字符与它所关联的组合标记分开。

此外，还有一些书写系统，其中的字符所表示的部件组合比重音符号复杂得多。例如在韩文中，一个谚文音节可以由两到三个称为 jamo 的子部件组成。在南亚和东南亚广泛使用的印度系及受其影响的书写系统中，单个书写字符往往表示辅音、元音以及维拉摩（virama）之类符号的组合，而这些书写系统的 Unicode 表示常常为这些单独的部件各用一个码点，因此单个字符可能由多个码点组成。对于大多数文本处理而言，子串范围的安排还应保证其边界不会拆开单个谚文音节中的 jamo，也不会拆开印度系辅音丛的各个组成部分。

一般来说，这些组合——代理对、基字符加组合标记、谚文 jamo，以及印度系辅音丛——统称为字素簇（grapheme cluster）。为了把它们考虑在内，你可以使用 `NSString` 的 [rangeOfComposedCharacterSequencesForRange:](https://developer.apple.com/documentation/foundation/nsstring/1410993-rangeofcomposedcharactersequence) 或 [rangeOfComposedCharacterSequenceAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfComposedCharacterSequenceAtIndex:) 方法，也可以使用 [CFStringGetRangeOfComposedCharactersAtIndex](https://developer.apple.com/documentation/corefoundation/1541847-cfstringgetrangeofcomposedcharac)。它们可以用来调整字符串索引或子串范围，使其落在字素簇边界上，同时兼顾上面提到的所有约束。要以编程方式判定用户所感知的字符的边界，应当首选这些方法。:

在某些情况下，Unicode 算法处理多个字符的方式甚至超出了字素簇边界的范畴。Unicode 的大小写转换算法在把小写转为大写时，可能把单个字符变成多个字符；例如德语字符“ß”的标准大写形式是两个字母的序列“SS”。许多语言的本地化排序算法会把多字符序列当作单个单位处理；例如在某些欧洲语言中，排序时序列“ch”被视为单个字母。为了妥善处理这类情况，进行大小写转换、排序、搜索等操作时，务必使用标准的 `NSString` 方法，并且把它们作用于所要处理的整个字符串。请使用 `NSString` 的方法，例如 [lowercaseString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/lowercaseString)、[uppercaseString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/uppercaseString)、[capitalizedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/capitalizedString)、[compare:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/compare:) 及其各种变体、[rangeOfString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:) 及其各种变体、[rangeOfCharacterFromSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfCharacterFromSet:) 及其各种变体，或者 CFString 中的对应函数。它们都考虑到了 Unicode 字符串处理的复杂性，其中搜索和排序方法尤其提供了许多选项，用来控制它们应当识别哪些类型的等价关系。

在一些较少见的情况下，可能需要针对特定需求来定制字素簇的定义。判定和定制字素簇边界所涉及的问题，在 [Unicode Standard Annex #29](http://unicode.org/reports/tr29/) 中有详细讨论，其中给出了大量示例和一些算法。总体而言，Unicode 标准是了解 Unicode 算法以及处理 Unicode 字符串相关考量的最佳资料来源。

如果你关注的是光标移动和插入点定位角度上的字素簇边界，并且使用的是 Cocoa 文本系统，那么你应当知道：在 OS X v10.5 及更高版本中，[NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager) 提供了 API 支持，可以在一行文本完成布局后确定其中的插入点位置。注意，插入点边界与字形（glyph）边界并不相同；某些情况下的连字字形，例如拉丁文字中的“fi”连字，可能需要在用户所感知的字符边界上设置一个内部插入点。更多信息请参阅 _[Cocoa 文本架构指南](../../Cocoa%20Text%20Architecture%20Guide/About%20the%20Cocoa%20Text%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjz)_。

[下一页](Character%20Sets.md)[上一页](Words%2C%20Paragraphs%2C%20and%20Line%20Breaks.md)

