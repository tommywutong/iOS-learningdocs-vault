---
title: Method
framework: Objective-C Runtime
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/method
source_url: 'https://developer.apple.com/documentation/objectivec/method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/method.json'
content_hash: 'sha256:ded944b7126dd20b'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# Method

<sub>类型别名</sub>

一种不透明类型，表示类定义中的一个方法。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Method = OpaquePointer
```

## 另请参阅

### 类定义数据结构

- [Ivar](ivar.md) — 一种不透明类型，表示一个实例变量。
- [Category](category.md) — 一种不透明类型，表示一个分类。
- [objc_property_t](objc_property_t.md) — 一种不透明类型，表示一个 Objective-C 声明的属性。
- [IMP](imp.md) — 指向方法实现起始位置的指针。
- [objc_method_description](objc_method_description.md) — 定义一个 Objective-C 方法。
- [objc_cache](objc_cache.md) — 方法调用的性能优化。包含指向最近使用的方法的指针。
- [objc_property_attribute_t](objc_property_attribute_t.md) — 定义一个属性特性。
