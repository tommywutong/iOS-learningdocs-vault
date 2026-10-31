---
title: 'instancesRespond(to:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/instancesrespond(to:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/instancesrespond(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/instancesrespond%28to%3A%29.json'
content_hash: 'sha256:700452b88cc03305'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# instancesRespond(to:)

<sub>类型方法</sub>

返回一个布尔值，指示接收者的实例是否能够响应给定选择器。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func instancesRespond(to aSelector: Selector!) -> Bool
```

## 参数

- `aSelector` — 一个 [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。

## 返回值

若接收者的实例能够响应 `aSelector` 消息则为 [YES](../yes.md)，否则为 [NO](../no.md)。

## 讨论

若 `aSelector` 消息被转发给其他对象，即使此方法返回 [NO](../no.md)，该类的实例仍能无错误地接收这些消息。

若要询问类本身（而非其实例）能否响应特定消息，请改为向该类发送 `NSObject` 协议实例方法 [- respondsToSelector:](<../nsobjectprotocol/responds(to_).md>)。
