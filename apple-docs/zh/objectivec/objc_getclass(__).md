---
title: 'objc_getClass(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_getclass(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_getclass(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_getclass%28_%3A%29.json'
content_hash: 'sha256:059d95dfb57189a3'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_getClass(_:)

<sub>函数</sub>

返回指定类的类定义。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_getClass(_ name: UnsafePointer<CChar>) -> Any!
```

## 参数

- `name` — 要查找的类的名称。

## 返回值

具有该名称的类的 Class 对象；如果该类尚未向 Objective-C runtime 注册，则返回 `nil`。

## 讨论

此函数的实现与 [objc_lookUpClass](<objc_lookupclass(__).md>) 函数的实现相同。

## 另请参阅

### 获取类定义

- [objc_getClassList](<objc_getclasslist(____).md>) — 获取已注册的类定义列表。
- [objc_copyClassList](<objc_copyclasslist(__).md>) — 创建并返回一个指向所有已注册类定义的指针列表。
- [objc_lookUpClass](<objc_lookupclass(__).md>) — 返回指定类的类定义。
- [objc_getRequiredClass](<objc_getrequiredclass(__).md>) — 返回指定类的类定义。
- [objc_getMetaClass](<objc_getmetaclass(__).md>) — 返回指定类的元类定义。
