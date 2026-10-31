---
title: 'object_setIvar(_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_setivar(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_setivar(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_setivar%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:327eab2b5fddb0b5'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_setIvar(_:_:_:)

<sub>函数</sub>

设置对象中某个实例变量的值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_setIvar(_ obj: Any?, _ ivar: Ivar, _ value: Any?)
```

## 参数

- `obj` — 包含要设置其值的实例变量的对象。

- `ivar` — 描述要设置其值的实例变量的 Ivar。

- `value` — 实例变量的新值。

## 讨论

若已知道实例变量的 Ivar，则 [object_setIvar](<object_setivar(______).md>) 比 [object_setInstanceVariable](object_setinstancevariable.md) 更快。

## 另请参阅

### 使用实例

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — 返回一个指针，指向随给定实例对象分配的任何额外字节。
- [object_getIvar](<object_getivar(____).md>) — 读取对象中某个实例变量的值。
- [object_getClassName](<object_getclassname(__).md>) — 返回给定对象的类名。
- [object_getClass](<object_getclass(__).md>) — 返回一个对象的类。
- [object_setClass](<object_setclass(____).md>) — 设置一个对象的类。
