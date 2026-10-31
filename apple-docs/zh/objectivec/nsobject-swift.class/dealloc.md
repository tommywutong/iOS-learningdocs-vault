---
title: dealloc
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/dealloc
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/dealloc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/dealloc.json'
content_hash: 'sha256:2a245632c7dad82d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# dealloc

<sub>实例方法</sub>

Deallocates the memory occupied by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) dealloc;
```

## 讨论

随后向接收者发送的消息可能会生成错误，指示消息已发送给已释放的对象（前提是已释放的内存尚未被重用）。

你重写此方法以处置除对象实例变量以外的资源，例如：

```objc
- (void)dealloc {
    free(myBigBlockOfMemory);
}
```

在 `dealloc` 的实现中，不要调用超类的实现。应尽量避免使用 `dealloc` 管理文件描述符等有限资源的生命周期。

你从不直接发送 [dealloc](dealloc.md) 消息。相反，对象的 `dealloc` 方法由运行时调用。有关更多详细信息，请参阅 [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i)。

### 特殊注意事项

在不使用 ARC 时，你的 `dealloc` 实现必须作为最后一条指令调用超类的实现。

## 另请参阅

### 创建、拷贝与释放对象

- [alloc](alloc.md) — 返回接收类的新实例。
- [allocWithZone:](allocwithzone_.md) — 返回接收类的新实例。
- [- init](<init().md>) — 由子类实现，以在为新对象（接收者）分配内存后立即对其进行初始化。
- [- copy](<copy().md>) — 返回 `copy(with:)` 返回的对象。
- [copyWithZone:](copywithzone_.md) — 返回接收者。
- [- mutableCopy](<mutablecopy().md>) — 返回 `mutableCopy(with:)`（其中 zone 为 `nil`）返回的对象。
- [mutableCopyWithZone:](mutablecopywithzone_.md) — 返回接收者。
- [new](new.md) — 分配接收类的新实例，向其发送 [- init](<init().md>) 消息，并返回已初始化的对象。
