---
title: objc_property_attribute_t
framework: Objective-C Runtime
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_property_attribute_t
source_url: 'https://developer.apple.com/documentation/objectivec/objc_property_attribute_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_property_attribute_t.json'
content_hash: 'sha256:62c8447209c63e6c'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_property_attribute_t

<sub>结构体</sub>

Defines a property attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct objc_property_attribute_t
```

## 关系

- **符合**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## 主题

### 初始化方法

- [init(name:value:)](<objc_property_attribute_t/init(name_value_).md>)

### 实例属性

- [name](objc_property_attribute_t/name.md) — 属性的名称。
- [value](objc_property_attribute_t/value.md) — 属性的值（通常为空）。

## 另请参阅

### 类定义数据结构

- [Method](method.md) — 一个不透明类型，表示类定义中的一个方法。
- [Ivar](ivar.md) — 一个不透明类型，表示一个实例变量。
- [Category](category.md) — 一个不透明类型，表示一个分类。
- [objc_property_t](objc_property_t.md) — 表示 Objective-C 声明属性的不透明类型。
- [IMP](imp.md) — 一个指向方法实现起始位置的指针。
- [objc_method_description](objc_method_description.md) — 定义一个 Objective-C 方法。
- [objc_cache](objc_cache.md) — 针对方法调用的性能优化。包含指向最近使用过的方法的指针。
