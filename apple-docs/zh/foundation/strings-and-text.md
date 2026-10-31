---
title: 字符串与文本
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/strings-and-text
source_url: 'https://developer.apple.com/documentation/foundation/strings-and-text'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/strings-and-text.json'
content_hash: 'sha256:29ba24613ebaf4a6'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 字符串与文本

<sub>API 集合</sub>

创建和处理 Unicode 字符组成的字符串，使用正则表达式查找模式，并对文本执行自然语言分析。

## 主题

### 字符串

- [String](../swift/string.md) — 一个 Unicode 字符串值，是字符的集合。
- [String Encodings](1497293-string-encodings.md) — 用于在原始数据与字符串表示之间转换的编码标准常量。

### 带元数据的字符串

- [AttributedString](attributedstring.md) — 一种字符串值类型（value type），可为文本的各个部分关联属性。
- [AttributedSubstring](attributedsubstring.md) — 属性字符串的一部分。
- [Attributed String Supporting Types](attributed-string-supporting-types.md) — 带属性字符串、带属性子字符串及辅助类型扩展或遵循的类型，用于共享通用功能。
- [NSAttributedString](nsattributedstring.md) — 管理字符范围的数据、布局和样式信息以支持渲染的文本字符串。
- [NSMutableAttributedString](nsmutableattributedstring.md) — 一种可变字符串，可为文本的各个部分关联属性，例如视觉样式、超链接或辅助功能数据。

### 字符

- [CharacterSet](characterset.md) — 一组用于搜索操作的 Unicode 字符值。
- [UnicodeScalar](../swift/unicodescalar.md)

### 模式匹配

- [Scanner](scanner.md) — 一种字符串解析器，扫描字符集中的子字符串或字符，以及十进制、十六进制和浮点表示的数值。
- [NSRegularExpression](nsregularexpression.md) — 已编译正则表达式的一种不可变表示，可应用到 Unicode 字符串。
- [NSDataDetector](nsdatadetector.md) — 一种专用的正则表达式对象，按预定义的数据模式匹配自然语言文本。
- [NSTextCheckingResult](nstextcheckingresult.md) — 在分析文本块期间（例如匹配正则表达式时）发现的文本内容出现位置。
- [NSNotFound](nsnotfound-4qp9h.md) — 一个值，表示找不到或不存在请求的项目。

### 拼写与语法

- [NSSpellServer](nsspellserver.md) — 一种服务器，你的 App 用它向系统中运行的其他 App 提供拼写检查服务。
- [NSSpellServerDelegate](nsspellserverdelegate.md) — 拼写服务器的委托所实现的可选方法。

### 本地化

- [Locale](locale.md) — 用于格式化待呈现数据的语言、文化和技术惯例信息。
- [NSOrthography](nsorthography.md) — 对自然语言文本语言内容的描述，通常用于拼写和语法检查。
- [NSLocalizedString(_:tableName:bundle:value:comment:)](<nslocalizedstring(__tablename_bundle_value_comment_).md>) — 从 Xcode 在导出本地化时为你生成的表格中返回一个本地化字符串。
- [LocalizedStringResource](localizedstringresource.md) — 对可本地化字符串的引用，可从另一个进程访问。
- [CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md) — 一种提供进程外可本地化描述的类型。
- [URLResource](urlresource.md) — 位于 bundle 内特定文件 URL 处的一种资源。

### 已废弃

- [NSLinguisticTagger](nslinguistictagger.md) — 分析自然语言文本以标注词性和词法类别，识别名称，执行词形还原，并确定语言和文字系统。_(已废弃)_
- [Deprecated String Encodings](1497268-deprecated-string-encodings.md)

## 另请参阅

### 基本原理

- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md) — 使用 Cocoa 中普遍采用的原始值和其他基础类型。
- [Collections](collections.md) — 使用数组、字典、集合和专用集合来存储和迭代对象组或值组。
- [Dates and Times](dates-and-times.md) — 比较日期与时间，并执行日历和时区计算。
- [Units and Measurement](units-and-measurement.md) — 为数值标注物理维度，以便进行区域设置感知的格式化和相关单位间转换。
- [Data Formatting](data-formatting.md) — 在数值、日期、测量结果及其他值与适应区域设置的字符串表示形式之间进行转换。
- [Filters and Sorting](filters-and-sorting.md) — 使用谓词、表达式和排序描述符检查集合及其他服务中的元素。
