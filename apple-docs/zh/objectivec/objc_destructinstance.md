---
title: objc_destructInstance
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_destructinstance
source_url: 'https://developer.apple.com/documentation/objectivec/objc_destructinstance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_destructinstance.json'
content_hash: 'sha256:095f3515960f4596'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_destructInstance

<sub>函数</sub>

销毁一个类的实例但不释放内存，并移除其任何关联引用。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void *objc_destructInstance(id obj);
```

## 讨论

如果 `obj` 为 `nil`，此方法不做任何事。

> [!important] 重要
> 垃圾回收器不会调用此函数。因此，如果你编辑此函数，也应一并编辑 finalize。尽管如此，Core Foundation 及其他客户端在垃圾回收下确实会调用此函数。

## 另请参阅

### 实例化类

- [class_createInstance](<class_createinstance(____).md>) — 创建一个类的实例，在默认的 malloc 内存区中为该类分配内存。
- [objc_constructInstance](objc_constructinstance.md) — 在指定位置创建一个类的实例。
