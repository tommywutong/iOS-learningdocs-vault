---
title: 'object_setClass(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_setclass(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_setclass(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_setclass%28_%3A_%3A%29.json'
content_hash: 'sha256:60a48a9a2c0d943b'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_setClass(_:_:)

<sub>函数</sub>

设置对象的类。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_setClass(_ obj: Any?, _ cls: AnyClass) -> AnyClass?
```

## 参数

- `obj` — 要修改的对象。

- `cls` — 一个类对象。

## 返回值

`object` 先前的类值；若 `object` 为 `nil` 则为 `Nil`。

## 另请参阅

### 使用实例

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — 返回一个指针，指向随给定实例对象分配的任何额外字节。
- [object_getIvar](<object_getivar(____).md>) — 读取对象中某个实例变量的值。
- [object_setIvar](<object_setivar(______).md>) — 设置对象中某个实例变量的值。
- [object_getClassName](<object_getclassname(__).md>) — 返回给定对象的类名。
- [object_getClass](<object_getclass(__).md>) — 返回一个对象的类。
