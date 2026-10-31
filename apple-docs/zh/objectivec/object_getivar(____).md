---
title: 'object_getIvar(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/object_getivar(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/object_getivar(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/object_getivar%28_%3A_%3A%29.json'
content_hash: 'sha256:8f069ad76e9ed94f'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# object_getIvar(_:_:)

<sub>函数</sub>

读取对象中某个实例变量的值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object_getIvar(_ obj: Any?, _ ivar: Ivar) -> Any?
```

## 参数

- `obj` — 包含要读取其值的实例变量的对象。

- `ivar` — 描述要读取其值的实例变量的 Ivar。

## 返回值

由 `ivar` 指定的实例变量的值；若 `object` 为 `nil` 则为 `nil`。

## 讨论

若已知道实例变量的 Ivar，则 [object_getIvar](<object_getivar(____).md>) 比 [object_getInstanceVariable](object_getinstancevariable.md) 更快。

## 另请参阅

### 使用实例

- [object_getIndexedIvars](<object_getindexedivars(__).md>) — 返回一个指针，指向随给定实例对象分配的任何额外字节。
- [object_setIvar](<object_setivar(______).md>) — 设置对象中某个实例变量的值。
- [object_getClassName](<object_getclassname(__).md>) — 返回给定对象的类名。
- [object_getClass](<object_getclass(__).md>) — 返回一个对象的类。
- [object_setClass](<object_setclass(____).md>) — 设置一个对象的类。
