---
title: 'copyWithZone:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/copywithzone:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/copywithzone:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/copywithzone%3A.json'
content_hash: 'sha256:a8edc0b6bdea265f'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# copyWithZone:

<sub>类型方法</sub>

返回接收者。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (id) copyWithZone:(struct _NSZone *) zone;
```

## 参数

- `zone` — This argument is ignored.

## 返回值

The receiver.

## 讨论

存在此方法是为了使类对象可用于需要符合 [NSCopying](../../foundation/nscopying.md) 协议的对象的情况。例如，此方法允许你将类对象用作 `NSDictionary` 对象的键。你不应重写此方法。

## 另请参阅

### 创建、拷贝与释放对象

- [alloc](alloc.md) — 返回接收类的新实例。
- [allocWithZone:](allocwithzone_.md) — 返回接收类的新实例。
- [- init](<init().md>) — 由子类实现，以在为新对象（接收者）分配内存后立即对其进行初始化。
- [- copy](<copy().md>) — 返回 `copy(with:)` 返回的对象。
- [- mutableCopy](<mutablecopy().md>) — 返回 `mutableCopy(with:)`（其中 zone 为 `nil`）返回的对象。
- [mutableCopyWithZone:](mutablecopywithzone_.md) — 返回接收者。
- [dealloc](dealloc.md) — 释放接收者占用的内存。
- [new](new.md) — 分配接收类的新实例，向其发送 [- init](<init().md>) 消息，并返回已初始化的对象。
