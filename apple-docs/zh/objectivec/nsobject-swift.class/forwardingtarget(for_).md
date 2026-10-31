---
title: 'forwardingTarget(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/forwardingtarget(for:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/forwardingtarget(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/forwardingtarget%28for%3A%29.json'
content_hash: 'sha256:565bc33ec121237c'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# forwardingTarget(for:)

<sub>实例方法</sub>

返回应首先将无法识别的消息定向到的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func forwardingTarget(for aSelector: Selector!) -> Any?
```

## 参数

- `aSelector` — 接收者未实现的方法的 [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。

## 返回值

应首先将无法识别的消息定向到的对象。

## 讨论

若对象实现（或继承）此方法，并返回非 `nil`（且非 `self`）的结果，则将该返回对象用作新的接收对象，消息分发会继续到该新对象。（显然，若从此方法返回 `self`，代码会陷入无限循环。）

若你在非根类中实现此方法，当你的类对给定选择器没有可返回的内容时，应返回调用 super 实现的结果。

此方法使对象有机会在开销大得多的 [forwardInvocation:](forwardinvocation_.md) 机制接管之前，重定向发送给它的未知消息。当你只想将消息重定向到另一个对象时，这很有用，并且可比常规转发快一个数量级。若转发的目标是捕获 NSInvocation，或在转发期间操控参数或返回值，则此方法并不适用。
