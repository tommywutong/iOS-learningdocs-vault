---
title: 'isLike(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/islike(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/islike(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/islike%28_%3A%29.json'
content_hash: 'sha256:8ea81933793e423b'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isLike(_:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者是否“像”另一个给定对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func isLike(_ object: String) -> Bool
```

## 参数

- `object` — 用于与接收者比较的对象。

## 返回值

若认为接收者“像”`object` 则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

目前，Cocoa 自身从不向任何对象发送 [- isLike:](<islike(__).md>) 消息。

由 `NSObject` 提供的此方法默认实现返回 [NO](../no.md)。`NSString` 也提供了此方法的实现，若接收者匹配 `object` 描述的模式则返回 [YES](../yes.md)。
