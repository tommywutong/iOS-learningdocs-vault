---
title: alloc
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/alloc
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/alloc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/alloc.json'
content_hash: 'sha256:e3e6a3af7d7212b8'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# alloc

<sub>类型方法</sub>

返回接收类的新实例。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) alloc;
```

## 返回值

接收者的新实例。

## 讨论

这是新实例的一个实例变量，会被初始化为描述该类的数据结构；所有其他实例变量的内存都设为 `0`。

必须使用 `init...` 方法来完成初始化过程。例如：

```objc
TheClass *newObject = [[TheClass alloc] init];
```

不要重写 [alloc](alloc.md) 以包含初始化代码。相反，应实现特定于类的 `init...` 方法。

出于历史原因，[alloc](alloc.md) 会调用 [allocWithZone:](allocwithzone_.md)。

## 另请参阅

### 创建、拷贝与释放对象

- [allocWithZone:](allocwithzone_.md) — 返回接收类的新实例。
- [- init](<init().md>) — 由子类实现，在为新对象（接收者）分配内存后立即对其进行初始化。
- [- copy](<copy().md>) — Returns the object returned by `copy(with:)`.
- [copyWithZone:](copywithzone_.md) — 返回接收者。
- [- mutableCopy](<mutablecopy().md>) — 返回由 `mutableCopy(with:)` 返回的对象（其中 zone 为 `nil`）。
- [mutableCopyWithZone:](mutablecopywithzone_.md) — 返回接收者。
- [dealloc](dealloc.md) — 释放接收者占用的内存。
- [new](new.md) — 分配接收类的新实例，向其发送 [- init](<init().md>) 消息，并返回已初始化的对象。
