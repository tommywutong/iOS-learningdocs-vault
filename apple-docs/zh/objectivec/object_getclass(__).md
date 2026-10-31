---
title: 'object_getClass(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_getclass(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_getclass(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_getclass%28_%3A%29.json'
content_hash: 'sha256:2903f98ee29bf2c4'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_getClass(_:)

<sub>函数</sub>

返回一个对象的类。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_getClass(_ obj: Any?) -> AnyClass?
```

## 参数

- `obj` — 你想要检查的对象。

## 返回值

`object` 所属实例的类对象；如果 `object` 为 `nil`，则返回 `Nil`。

## 另请参阅

### 使用实例

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — 返回一个指针，指向随给定实例对象分配的任何额外字节。
- [object_getIvar](<object_getivar(____).md>) — 读取对象中某个实例变量的值。
- [object_setIvar](<object_setivar(______).md>) — 设置对象中某个实例变量的值。
- [object_getClassName](<object_getclassname(__).md>) — 返回给定对象的类名。
- [object_setClass](<object_setclass(____).md>) — 设置一个对象的类。
