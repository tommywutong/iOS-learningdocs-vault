---
title: 'isCaseInsensitiveLike(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/iscaseinsensitivelike(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/iscaseinsensitivelike(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/iscaseinsensitivelike%28_%3A%29.json'
content_hash: 'sha256:ec00c2d8b0a34d5b'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isCaseInsensitiveLike(_:)

<sub>实例方法</sub>

返回一个布尔值，指示在忽略接收者中字符大小写时，是否认为接收者“像”给定字符串。

<sub>Mac Catalyst, macOS</sub>

```swift
func isCaseInsensitiveLike(_ object: String) -> Bool
```

## 参数

- `object` — 用于与接收者比较的字符串。

## 返回值

若在忽略接收者中字符大小写时认为接收者“像”`aString` 则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

目前，Cocoa 自身从不向任何对象发送 [- isCaseInsensitiveLike:](<iscaseinsensitivelike(__).md>) 消息。

由 `NSObject` 提供的此方法默认实现返回 [NO](../no.md)。`NSString` 也提供了此方法的实现，若接收者在忽略大小写的情况下匹配 `aString` 描述的模式则返回 [YES](../yes.md)。
