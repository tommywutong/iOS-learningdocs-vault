---
title: 'objc_duplicateClass(_:_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_duplicateclass(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_duplicateclass(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_duplicateclass%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5041e076c1d7cbe5'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_duplicateClass(_:_:_:)

<sub>函数</sub>

由 Foundation 的键值观察使用。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_duplicateClass(_ original: AnyClass, _ name: UnsafePointer<CChar>, _ extraBytes: Int) -> AnyClass
```

## 讨论

请勿自行调用此函数。

## 另请参阅

### 添加类

- [objc_allocateClassPair](<objc_allocateclasspair(______).md>) — 创建一个新的类及其元类。
- [objc_disposeClassPair](<objc_disposeclasspair(__).md>) — 销毁一个类及其关联的元类。
- [objc_registerClassPair](<objc_registerclasspair(__).md>) — 注册使用 [objc_allocateClassPair](<objc_allocateclasspair(______).md>) 分配的类。
