---
title: retainCount
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-c.protocol/retaincount
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-c.protocol/retaincount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-c.protocol/retaincount.json'
content_hash: 'sha256:b832f75f65dd70e0'
translated: true
---


> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObjectProtocol](../nsobjectprotocol.md)

# retainCount

<sub>实例方法</sub>

不要使用此方法。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (NSUInteger) retainCount;
```

## 返回值

接收者的引用计数。

## 讨论

此方法对于调试内存管理问题没有价值。因为任意数量的框架对象都可能已保留某个对象以持有对它的引用，与此同时自动释放池也可能对该对象持有任意数量的延迟释放，所以你几乎不可能从此方法获得有用信息。

要了解你必须遵守的内存管理基本规则，请阅读 [Memory Management Policy](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmRules.html#//apple_ref/doc/uid/20000994)。要诊断内存管理问题，请使用合适的工具：

- [Clang Static analyzer](http://clang-analyzer.llvm.org) 通常甚至能在你运行程序之前就找到内存管理问题。
- Instruments 应用程序中的 Object Alloc 工具（参见 [Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)）可以跟踪对象的分配与销毁。

## 另请参阅

### 过时方法

- [retain](retain.md) — 递增接收者的引用计数。
- [release](release.md) — 递减接收者的引用计数。
- [autorelease](autorelease.md) — 在当前自动释放池块结束时递减接收者的保留计数。
- [zone](zone.md) — Zone 已废弃，大多数将其作为参数的类都会忽略它。
