---
title: release
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-c.protocol/release
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-c.protocol/release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-c.protocol/release.json'
content_hash: 'sha256:b63c8624262e0877'
translated: true
---


> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# release

<sub>实例方法</sub>

递减接收者的引用计数。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) release;
```

## 讨论

当接收者的引用计数达到 `0` 时，会向其发送 [dealloc](../nsobject-swift.class/dealloc.md) 消息。

只有在定义自己的引用计数方案时，才应实现此方法。此类实现不应调用继承的方法；也就是说，它们不应向 `super` 发送 release 消息。

有关引用计数机制的更多信息，请参阅 [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i)。

### 特殊注意事项

你应采用 ARC，而不是使用手动引用计数——请参阅 [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226)。

## 另请参阅

### 过时方法

- [retain](retain.md) — 递增接收者的引用计数。
- [autorelease](autorelease.md) — 在当前自动释放池块结束时递减接收者的保留计数。
- [retainCount](retaincount.md) — 不要使用此方法。
- [zone](zone.md) — Zone 已废弃，大多数将其作为参数的类都会忽略它。
