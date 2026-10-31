---
title: 'objc_getRequiredClass(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_getrequiredclass(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_getrequiredclass(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_getrequiredclass%28_%3A%29.json'
content_hash: 'sha256:17c4dad12acef49b'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_getRequiredClass(_:)

<sub>函数</sub>

返回指定类的类定义。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_getRequiredClass(_ name: UnsafePointer<CChar>) -> AnyClass
```

## 参数

- `name` — 要查找的类的名称。

## 返回值

指定类的 Class 对象。

## 讨论

此函数与 [objc_getClass](<objc_getclass(__).md>) 相同，但在找不到类时会终止进程。

此函数由 ZeroLink 使用；在没有 ZeroLink 的情况下，找不到类将是编译时链接错误。

## 另请参阅

### 获取类定义

- [objc_getClassList](<objc_getclasslist(____).md>) — 获取已注册的类定义列表。
- [objc_copyClassList](<objc_copyclasslist(__).md>) — 创建并返回一个指向所有已注册类定义的指针列表。
- [objc_lookUpClass](<objc_lookupclass(__).md>) — 返回指定类的类定义。
- [objc_getClass](<objc_getclass(__).md>) — 返回指定类的类定义。
- [objc_getMetaClass](<objc_getmetaclass(__).md>) — 返回指定类的元类定义。
