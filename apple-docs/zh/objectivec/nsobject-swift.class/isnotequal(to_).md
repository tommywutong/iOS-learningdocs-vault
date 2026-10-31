---
title: 'isNotEqual(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/isnotequal(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isnotequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/isnotequal%28to%3A%29.json'
content_hash: 'sha256:125f6bbb61921388'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isNotEqual(to:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者是否不等于另一个给定对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func isNotEqual(to object: Any?) -> Bool
```

## 参数

- `object` — 用于与接收者比较的对象。

## 返回值

若接收者不等于 `object` 则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

目前，Cocoa 自身从不向任何对象发送 [- isNotEqualTo:](<isnotequal(to_).md>) 消息。

由 `NSObject` 提供的此方法默认实现会在向同一对象发送 `isEqual:` 消息将返回 [NO](../no.md) 时返回 [YES](../yes.md)。
