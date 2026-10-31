---
title: StringProtocol 实现
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/string/stringprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/string/stringprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/stringprotocol-implementations.json'
content_hash: 'sha256:82fa509bea6f6ccb'
translated: true
---

> 导航： [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# StringProtocol 实现

<sub>API 集合</sub>

## 主题

### 结构体

- [UTF16View](utf16view.md) — 一种把字符串内容表示为 UTF-16 代码单元集合的视图。
- [UTF8View](utf8view.md) — 一种把字符串内容表示为 UTF-8 代码单元集合的视图。
- [UnicodeScalarView](unicodescalarview.md) — 一种把字符串内容表示为 Unicode 标量值集合的视图。

### 运算符

- [!=(_:_:)](<!=(____)-frzf.md>)
- [==(_:_:)](<==(____)-8kzxf.md>)
- [\>(_:_:)](<_(____)-6o7qv.md>)
- [\<(_:_:)](<_(____)-8d1wy.md>)
- [\<=(_:_:)](<_=(____)-5y22v.md>)
- [\>=(_:_:)](<_=(____)-nd86.md>)

### 初始化方法

- [init(cString:)](<init(cstring_)-2p84k.md>) — 通过复制给定指针所引用的以 null 结尾的 UTF-8 数据，创建一个新字符串。
- [init(decoding:as:)](<init(decoding_as_).md>) — 以指定的编码从给定的 Unicode 代码单元创建一个字符串。
- [init(decodingCString:as:)](<init(decodingcstring_as_)-8yowf.md>) — 通过复制给定指针所引用的以 null 结尾的代码单元序列，创建一个新字符串。

### 实例属性

- [unicodeScalars](unicodescalars.md) — 此字符串的值表示为 Unicode 标量值的集合。
- [utf16](utf16.md) — `self` 的 UTF-16 编码。
- [utf8](utf8.md) — `self` 的 UTF-8 编码。

### 实例方法

- [hasPrefix(_:)](<hasprefix(__).md>)
- [hasSuffix(_:)](<hassuffix(__).md>)
- [lowercased()](<lowercased().md>) — 返回字符串的小写版本。
- [uppercased()](<uppercased().md>) — 返回字符串的大写版本。
- [withCString(_:)](<withcstring(__).md>) — 调用给定的闭包，并向其传递一个指向字符串内容的指针，内容表示为以 null 结尾的 UTF-8 代码单元序列。
- [withCString(encodedAs:_:)](<withcstring(encodedas___).md>) — 调用给定的闭包，并向其传递一个指向字符串内容的指针，内容表示为以 null 结尾的代码单元序列。
