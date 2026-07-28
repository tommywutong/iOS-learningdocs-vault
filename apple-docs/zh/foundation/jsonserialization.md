---
title: JSONSerialization
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonserialization
source_url: 'https://developer.apple.com/documentation/foundation/jsonserialization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonserialization.json'
content_hash: 'sha256:3f3c144ce7520729'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# JSONSerialization

<sub>类</sub>

一个在 JSON 与等效 Foundation 对象之间进行转换的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class JSONSerialization
```

## 概述

你可以使用 [JSONSerialization](jsonserialization.md) 类将 JSON 转换为 Foundation 对象，或将 Foundation 对象转换为 JSON。

要将 Foundation 对象转换为 JSON，该对象必须满足以下属性：

- 顶层对象是 [NSArray](nsarray.md) 或 [NSDictionary](nsdictionary.md)，除非你设置了 [NSJSONWritingFragmentsAllowed](jsonserialization/writingoptions/fragmentsallowed.md) 选项。
- 所有对象都是 [NSString](nsstring.md)、[NSNumber](nsnumber.md)、[NSArray](nsarray.md)、[NSDictionary](nsdictionary.md) 或 [NSNull](nsnull.md) 的实例。
- 所有字典的键都是 [NSString](nsstring.md) 的实例。
- 数字既非 `NaN` 也非无穷大。

还可能有其他规则。调用 [+ isValidJSONObject:](<jsonserialization/isvalidjsonobject(__).md>) 或尝试进行转换是判断 [JSONSerialization](jsonserialization.md) 类能否将给定对象转换为 JSON 数据的确定方法。

> [!note] 注意
> 在 iOS 7 及更高版本和 macOS 10.9 及更高版本中，[JSONSerialization](jsonserialization.md) 是线程安全的。

## 关系

- **继承自**：[NSObject](../objectivec/nsobject-swift.class.md)

- **遵循**：[CVarArg](../swift/cvararg.md)、[CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)、[CustomStringConvertible](../swift/customstringconvertible.md)、[Equatable](../swift/equatable.md)、[Hashable](../swift/hashable.md)、[NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## 主题

### 创建 JSON 对象

- [+ JSONObjectWithData:options:error:](<jsonserialization/jsonobject(with_options_)-8demi.md>) — 从给定的 JSON 数据返回一个 Foundation 对象。
- [+ JSONObjectWithStream:options:error:](<jsonserialization/jsonobject(with_options_)-3afap.md>) — 从给定流中的 JSON 数据返回一个 Foundation 对象。
- [ReadingOptions](jsonserialization/readingoptions.md) — 从 JSON 数据创建 Foundation 对象时使用的选项。

### 创建 JSON 数据

- [+ dataWithJSONObject:options:error:](<jsonserialization/data(withjsonobject_options_).md>) — 从 Foundation 对象返回 JSON 数据。
- [+ writeJSONObject:toStream:options:error:](<jsonserialization/writejsonobject(__to_options_error_).md>) — 将给定的 JSON 对象写入一个流。
- [WritingOptions](jsonserialization/writingoptions.md) — 用于写入 JSON 数据的选项。
- [+ isValidJSONObject:](<jsonserialization/isvalidjsonobject(__).md>) — 返回一个布尔值，指示序列化器是否可以将给定对象转换为 JSON 数据。

## 另请参阅

### JSON

- [使用 JSON 与自定义类型](using-json-with-custom-types.md) — 使用 Swift 的 JSON 支持编码和解码 JSON 数据，无论其结构如何。
- [JSONEncoder](jsonencoder.md) — 一个将数据类型的实例编码为 JSON 对象的对象。
- [JSONDecoder](jsondecoder.md) — 一个从 JSON 对象解码数据类型的实例的对象。
