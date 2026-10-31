---
title: retain
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-c.protocol/retain
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-c.protocol/retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-c.protocol/retain.json'
content_hash: 'sha256:0d8a327d14b64ea3'
translated: true
---


> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# retain

<sub>实例方法</sub>

递增接收者的引用计数。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) retain;
```

## 返回值

`self`。

## 讨论

当你希望在使用完对象之前防止其被释放时，应向该对象发送 [retain](retain.md) 消息。

当对象的引用计数达到 `0` 时，它会自动被释放。[retain](retain.md) 消息会递增引用计数，而 [release](release.md) 消息会递减引用计数。有关此机制的更多信息，请参阅 [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i)。

为方便起见，[retain](retain.md) 返回 `self`，因为它可能用在嵌套表达式中。

只有在定义自己的引用计数方案时，才应实现此方法。此类实现必须返回 `self`，并且不应通过向 `super` 发送 [retain](retain.md) 消息来调用继承的方法。

### 特殊注意事项

你应采用 ARC，而不是使用手动引用计数——请参阅 [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226)。

## 另请参阅

### 过时方法

- [release](release.md) — 递减接收者的引用计数。
- [autorelease](autorelease.md) — 在当前自动释放池块结束时递减接收者的保留计数。
- [retainCount](retaincount.md) — 不要使用此方法。
- [zone](zone.md) — Zone 已废弃，大多数将其作为参数的类都会忽略它。
