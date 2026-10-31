---
title: 'perform(_:with:with:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/perform(_:with:with:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/perform(_:with:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/perform%28_%3Awith%3Awith%3A%29.json'
content_hash: 'sha256:b0c617f5ba46e3da'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# perform(_:with:with:)

<sub>实例方法</sub>

向接收者发送带有两个对象作为参数的消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector!, with object1: Any!, with object2: Any!) -> Unmanaged<AnyObject>!
```

## 参数

- `aSelector` — 标识要发送的消息的选择器。若 `aSelector` 为 `NULL`，则引发 [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md)。

- `object1` — 作为消息第一个参数的对象。

- `object2` — 作为消息第二个参数的对象

## 返回值

作为消息结果的对象。

## 讨论

此方法与 [- performSelector:](<perform(__).md>) 相同，不同之处在于你可以为 `aSelector` 提供两个参数。`aSelector` 应标识可以接受两个类型为 id 的参数的方法。对于具有其他参数类型和返回值的方法，请使用 [NSInvocation](../../foundation/nsinvocation.md)。

## 另请参阅

### 相关文档

- [- methodForSelector:](<../nsobject-swift.class/method(for_).md>) — 定位并返回接收者某个方法实现的地址，以便可将其作为函数调用。

### 发送消息

- [- performSelector:](<perform(__).md>) — 向接收者发送指定消息并返回消息的结果。
- [- performSelector:withObject:](<perform(__with_).md>) — 向接收者发送带有一个对象作为参数的消息。
