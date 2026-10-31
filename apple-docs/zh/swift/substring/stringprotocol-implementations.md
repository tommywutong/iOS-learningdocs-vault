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
doc_path: /documentation/swift/substring/stringprotocol-implementations
source_url: 'https://developer.apple.com/documentation/swift/substring/stringprotocol-implementations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/stringprotocol-implementations.json'
content_hash: 'sha256:0e01f850b265875b'
translated: true
---

> 导航：[技术](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md) · [Substring](../substring.md)

# StringProtocol 实现

<sub>API 集合</sub>

## 主题

### 结构体

- [UTF16View](utf16view.md)
- [UTF8View](utf8view.md)
- [UnicodeScalarView](unicodescalarview.md)

### 运算符

- [!=(_:_:)](<!=(____)-fryj.md>)
- [==(_:_:)](<==(____).md>)
- [\>(_:_:)](<_(____)-6o7pz.md>)
- [\<(_:_:)](<_(____)-8d1w2.md>)
- [\<=(_:_:)](<_=(____)-5y23r.md>)
- [\>=(_:_:)](<_=(____)-nd7a.md>)

### 初始化方法

- [init(cString:)](<init(cstring_).md>) — 根据给定指针处空终止、UTF-8 编码的字节序列创建字符串。
- [init(decoding:as:)](<init(decoding_as_).md>) — 根据给定的 Unicode 码元按指定编码创建字符串。
- [init(decodingCString:as:)](<init(decodingcstring_as_).md>) — 根据给定指针处空终止的字节序列创建字符串。

### 实例属性

- [unicodeScalars](unicodescalars.md)
- [utf16](utf16.md)
- [utf8](utf8.md)

### 实例方法

- [hasPrefix(_:)](<hasprefix(__).md>) — 返回一个布尔值，指示字符串是否以指定的前缀开头。
- [hasSuffix(_:)](<hassuffix(__).md>) — 返回一个布尔值，指示字符串是否以指定的后缀结尾。
- [hash(into:)](<hash(into_).md>) — 将此值的基本组成部分提供给给定的哈希器（hasher）来进行哈希。
- [lowercased()](<lowercased().md>)
- [uppercased()](<uppercased().md>)
- [withCString(_:)](<withcstring(__).md>) — 使用指向字符串内容的指针调用给定闭包，该内容表示为空终止的 UTF-8 码元序列。
- [withCString(encodedAs:_:)](<withcstring(encodedas___).md>) — 使用指向字符串内容的指针调用给定闭包，该内容表示为空终止的码元序列。
