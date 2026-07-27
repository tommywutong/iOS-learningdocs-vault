---
title: NSString 处理异常名称
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring-handling-exception-names
source_url: 'https://developer.apple.com/documentation/foundation/nsstring-handling-exception-names'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring-handling-exception-names.json'
content_hash: 'sha256:cc8069a45b3df9db'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [字符串与文本](strings-and-text.md) · [NSString](nsstring.md)

# NSString 处理异常名称

<sub>API 集合</sub>

这些常量定义了 `NSString` 无法以给定编码表示字符串或无法将字符串解析为属性列表时所引发异常的名称。

## 主题

### 常量

- [NSCharacterConversionException](nsexceptionname/characterconversionexception.md) — 如果字符串无法以文件系统编码或字符串编码表示，`NSString` 会引发 `NSCharacterConversionException`。
- [NSParseErrorException](nsexceptionname/parseerrorexception.md) — 如果字符串无法解析为属性列表，`NSString` 会引发 `NSParseErrorException`。

## 另请参阅

### 使用编码

- [availableStringEncodings](nsstring/availablestringencodings.md) — 返回 App 环境中字符串对象支持的、以零终止的编码列表。
- [defaultCStringEncoding](nsstring/defaultcstringencoding.md) — 返回任何接受 C 字符串作为实参的方法所假定使用的 C 字符串编码。
- [+ stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:](<nsstring/stringencoding(for_encodingoptions_convertedstring_usedlossyconversion_).md>) — 通过尝试依据指定编码选项创建字符串，返回检测出的给定数据的字符串编码。
- [+ localizedNameOfStringEncoding:](<nsstring/localizedname(of_).md>) — 返回一个易于阅读的字符串，给出指定编码的名称。
- [- canBeConvertedToEncoding:](<nsstring/canbeconverted(to_).md>) — 返回一个布尔值，指示接收者能否在不丢失信息的情况下转换为指定编码。
- [- dataUsingEncoding:](<nsstring/data(using_).md>) — 返回一个 `NSData` 对象，其中包含使用给定编码进行编码后的接收者表示。
- [- dataUsingEncoding:allowLossyConversion:](<nsstring/data(using_allowlossyconversion_).md>) — 返回一个 `NSData` 对象，其中包含使用给定编码进行编码后的接收者表示。
- [description](nsstring/description.md)
- [fastestEncoding](nsstring/fastestencoding.md) — 接收者可在不丢失信息的情况下转换到的最快编码。
- [smallestEncoding](nsstring/smallestencoding.md) — 接收者可在不丢失信息的情况下转换到的最小编码。
- [StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey.md)
