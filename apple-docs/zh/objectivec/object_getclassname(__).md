---
title: 'object_getClassName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_getclassname(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_getclassname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_getclassname%28_%3A%29.json'
content_hash: 'sha256:a1951b234e25bda4'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_getClassName(_:)

<sub>函数</sub>

返回给定对象的类名。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_getClassName(_ obj: Any?) -> UnsafePointer<CChar>
```

## 参数

- `obj` — 一个 Objective-C 对象。

## 返回值

`obj` 所属类的名称。

## 另请参阅

### 使用实例

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — 返回一个指针，指向随给定实例对象分配的任何额外字节。
- [object_getIvar](<object_getivar(____).md>) — 读取对象中某个实例变量的值。
- [object_setIvar](<object_setivar(______).md>) — 设置对象中某个实例变量的值。
- [object_getClass](<object_getclass(__).md>) — 返回一个对象的类。
- [object_setClass](<object_setclass(____).md>) — 设置一个对象的类。
