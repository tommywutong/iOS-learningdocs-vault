---
title: autorelease
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-c.protocol/autorelease
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-c.protocol/autorelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-c.protocol/autorelease.json'
content_hash: 'sha256:edb5c69ee7ec6613'
translated: true
---


> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# autorelease

<sub>实例方法</sub>

在当前自动释放池块结束时递减接收者的保留计数。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) autorelease;
```

## 返回值

`self`。

## 讨论

有关自动释放池块的更多信息，请参阅 [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i)。

### 特殊注意事项

你应采用 ARC，而不是使用手动引用计数——请参阅 [Transitioning to ARC Release Notes](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226)。

## 另请参阅

### 过时方法

- [retain](retain.md) — 递增接收者的引用计数。
- [release](release.md) — 递减接收者的引用计数。
- [retainCount](retaincount.md) — 不要使用此方法。
- [zone](zone.md) — Zone 已废弃，大多数将其作为参数的类都会忽略它。
