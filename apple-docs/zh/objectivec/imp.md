---
title: IMP
framework: Objective-C Runtime
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/imp
source_url: 'https://developer.apple.com/documentation/objectivec/imp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/imp.json'
content_hash: 'sha256:55af95ef5e8a0cfd'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# IMP

<sub>类型别名</sub>

指向方法实现起始位置的指针。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias IMP = OpaquePointer
```

## 讨论

此数据类型是指向实现该方法的函数起始位置的指针。该函数使用当前 CPU 架构所实现的标准 C 调用约定。第一个参数是指向 `self` 的指针（即该类特定实例的内存，或者对于类方法，则是指向元类的指针）。第二个参数是方法选择器（selector）。其后是方法参数。

## 另请参阅

### 类定义数据结构

- [Method](method.md) — 一种不透明类型，表示类定义中的一个方法。
- [Ivar](ivar.md) — 一种不透明类型，表示一个实例变量。
- [Category](category.md) — 一种不透明类型，表示一个分类。
- [objc_property_t](objc_property_t.md) — 一种不透明类型，表示一个 Objective-C 声明的属性。
- [objc_method_description](objc_method_description.md) — 定义一个 Objective-C 方法。
- [objc_cache](objc_cache.md) — 方法调用的性能优化。包含指向最近使用的方法的指针。
- [objc_property_attribute_t](objc_property_attribute_t.md) — 定义一个属性特性。
