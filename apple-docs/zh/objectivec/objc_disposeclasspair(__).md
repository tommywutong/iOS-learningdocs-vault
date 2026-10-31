---
title: 'objc_disposeClassPair(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/objc_disposeclasspair(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/objc_disposeclasspair(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_disposeclasspair%28_%3A%29.json'
content_hash: 'sha256:74f3b278eebd3330'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_disposeClassPair(_:)

<sub>函数</sub>

销毁类及其关联的元类。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objc_disposeClassPair(_ cls: AnyClass)
```

## 参数

- `cls` — 要销毁的类。此类必须已使用 [objc_allocateClassPair](<objc_allocateclasspair(______).md>) 分配。

## 讨论

若存在 `cls` 类或其任何子类的实例，请勿调用此函数。

## 另请参阅

### 添加类

- [objc_allocateClassPair](<objc_allocateclasspair(______).md>) — 创建新的类和元类。
- [objc_registerClassPair](<objc_registerclasspair(__).md>) — 注册使用 [objc_allocateClassPair](<objc_allocateclasspair(______).md>) 分配的类。
- [objc_duplicateClass](<objc_duplicateclass(______).md>) — 供 Foundation 的键值观察使用。
