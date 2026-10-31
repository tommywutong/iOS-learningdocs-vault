---
title: 'perform(_:with:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 1.0+, iPadOS 1.0+, Mac Catalyst 1.0+, macOS 10.0+, tvOS 1.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobjectprotocol/perform(_:with:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobjectprotocol/perform(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobjectprotocol/perform%28_%3Awith%3A%29.json'
content_hash: 'sha256:c40989070eb12d20'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# perform(_:with:)

<sub>实例方法</sub>

向接收者发送带有一个对象作为参数的消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector!, with object: Any!) -> Unmanaged<AnyObject>!
```

## 参数

- `aSelector` — 标识要发送的消息的选择器。若 `aSelector` 为 `NULL`，则引发 [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md)。

- `object` — 作为消息唯一参数的对象。

## 返回值

作为消息结果的对象。

## 讨论

此方法与 [- performSelector:](<perform(__).md>) 相同，不同之处在于你可以为 `aSelector` 提供一个参数。`aSelector` 应标识接受单个类型为 id 的参数的方法。对于具有其他参数类型和返回值的方法，请使用 [NSInvocation](../../foundation/nsinvocation.md)。

## 另请参阅

### 相关文档

- [- methodForSelector:](<../nsobject-swift.class/method(for_).md>) — 定位并返回接收者某个方法实现的地址，以便可将其作为函数调用。

### 发送消息

- [- performSelector:](<perform(__).md>) — 向接收者发送指定消息并返回消息的结果。
- [- performSelector:withObject:withObject:](<perform(__with_with_).md>) — 向接收者发送带有两个对象作为参数的消息。
