---
title: 'objc_getMetaClass(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_getmetaclass(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_getmetaclass(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_getmetaclass%28_%3A%29.json'
content_hash: 'sha256:695afbd0603f0a8b'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_getMetaClass(_:)

<sub>函数</sub>

返回指定类的元类定义。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_getMetaClass(_ name: UnsafePointer<CChar>) -> Any!
```

## 参数

- `name` — 要查找的类的名称。

## 返回值

指定类的元类的 `Class` 对象；若该类未在 Objective-C 运行时中注册，则为 `nil`。

## 讨论

若指定类的定义未注册，此函数会调用类处理程序回调，然后再次检查该类是否已注册。不过，每个类定义都必须有一个有效的元类定义，你可以安全地假定所有类定义（以及因此所有元类定义）都是与其超类一起加载的。

## 另请参阅

### 获取类定义

- [objc_getClassList](<objc_getclasslist(____).md>) — 获取已注册的类定义列表。
- [objc_copyClassList](<objc_copyclasslist(__).md>) — 创建并返回一个指向所有已注册类定义的指针列表。
- [objc_lookUpClass](<objc_lookupclass(__).md>) — 返回指定类的类定义。
- [objc_getClass](<objc_getclass(__).md>) — 返回指定类的类定义。
- [objc_getRequiredClass](<objc_getrequiredclass(__).md>) — 返回指定类的类定义。
