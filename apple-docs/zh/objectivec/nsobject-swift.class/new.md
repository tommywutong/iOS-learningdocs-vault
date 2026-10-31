---
title: new
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/new
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/new'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/new.json'
content_hash: 'sha256:c4ebb069ee75ad3f'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# new

<sub>类型方法</sub>

分配接收类的新实例，向其发送 [- init](<init().md>) 消息，并返回初始化后的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) new;
```

## 返回值

接收者的新实例。

## 讨论

此方法是 [alloc](alloc.md) 与 [- init](<init().md>) 的组合。与 [alloc](alloc.md) 一样，它会初始化新对象的 `isa` 实例变量，使其指向类数据结构，然后调用 [- init](<init().md>) 方法以完成初始化过程。

## 另请参阅

### 创建、拷贝与释放对象

- [alloc](alloc.md) — 返回接收类的新实例。
- [allocWithZone:](allocwithzone_.md) — 返回接收类的新实例。
- [- init](<init().md>) — 由子类实现，以在为新对象（接收者）分配内存后立即对其进行初始化。
- [- copy](<copy().md>) — 返回 `copy(with:)` 返回的对象。
- [copyWithZone:](copywithzone_.md) — 返回接收者。
- [- mutableCopy](<mutablecopy().md>) — 返回 `mutableCopy(with:)`（其中 zone 为 `nil`）返回的对象。
- [mutableCopyWithZone:](mutablecopywithzone_.md) — 返回接收者。
- [dealloc](dealloc.md) — 释放接收者占用的内存。
