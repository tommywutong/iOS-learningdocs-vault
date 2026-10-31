---
title: 'objc_registerClassPair(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_registerclasspair(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_registerclasspair(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_registerclasspair%28_%3A%29.json'
content_hash: 'sha256:13d8f12940a31823'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_registerClassPair(_:)

<sub>函数</sub>

注册使用 [objc_allocateClassPair](<objc_allocateclasspair(______).md>) 分配的类。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_registerClassPair(_ cls: AnyClass)
```

## 参数

- `cls` — 要注册的类。

## 另请参阅

### 添加类

- [objc_allocateClassPair](<objc_allocateclasspair(______).md>) — 创建一个新的类及其元类。
- [objc_disposeClassPair](<objc_disposeclasspair(__).md>) — 销毁一个类及其关联的元类。
- [objc_duplicateClass](<objc_duplicateclass(______).md>) — 由 Foundation 的键值观察使用。
