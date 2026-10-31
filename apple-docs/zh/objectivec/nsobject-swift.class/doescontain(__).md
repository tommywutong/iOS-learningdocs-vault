---
title: 'doesContain(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/doescontain(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/doescontain(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/doescontain%28_%3A%29.json'
content_hash: 'sha256:806f0de3aaf54b80'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# doesContain(_:)

<sub>实例方法</sub>

返回一个布尔值，指示接收者是否包含给定对象。

<sub>Mac Catalyst, macOS</sub>

```swift
func doesContain(_ object: Any) -> Bool
```

## 参数

- `object` — 要在接收者中搜索的对象。

## 返回值

若接收者包含 `object` 则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

目前，Cocoa 自身从不向任何对象发送 [- doesContain:](<doescontain(__).md>) 消息。

由 `NSObject` 提供的此方法默认实现会在接收者实际上是 `NSArray` 对象、且向同一对象发送 [indexOfObjectIdentical(to:)](<../../foundation/nsarray/indexofobjectidentical(to_).md>) 消息将返回非 `NSNotFound` 的值时返回 [YES](../yes.md)。
