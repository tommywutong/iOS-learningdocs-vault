---
title: 'object_getIndexedIvars(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_getindexedivars(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_getindexedivars(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_getindexedivars%28_%3A%29.json'
content_hash: 'sha256:1899b7587dbc2f92'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_getIndexedIvars(_:)

<sub>函数</sub>

返回与给定对象实例一并分配的任何额外字节的指针。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_getIndexedIvars(_ obj: Any?) -> UnsafeMutableRawPointer?
```

## 参数

- `obj` — 一个 Objective-C 对象。

## 返回值

指向随 `obj` 一并分配的任何额外字节的指针。若 `obj` 未分配任何额外字节，则解引用返回的指针是未定义行为。

## 讨论

此函数返回指向随实例一并分配的任何额外字节的指针（由带 extraBytes\>0 的 [class_createInstance](<class_createinstance(____).md>) 指定）。该内存在对象的普通实例变量之后，但不一定紧邻最后一个实例变量。

返回的指针保证按指针大小对齐，即使对象最后一个实例变量之后的区域对齐要求更低。从不保证大于指针大小的对齐，即使该区域对齐要求更高。

在垃圾回收环境中，会对该内存进行保守扫描。

## 另请参阅

### 使用实例

- [object_getIvar](<object_getivar(____).md>) — 读取对象中某个实例变量的值。
- [object_setIvar](<object_setivar(______).md>) — 设置对象中某个实例变量的值。
- [object_getClassName](<object_getclassname(__).md>) — 返回给定对象的类名。
- [object_getClass](<object_getclass(__).md>) — 返回一个对象的类。
- [object_setClass](<object_setclass(____).md>) — 设置一个对象的类。
