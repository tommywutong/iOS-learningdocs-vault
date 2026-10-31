---
title: objc_method_description
framework: Objective-C Runtime
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/objc_method_description
source_url: 'https://developer.apple.com/documentation/objectivec/objc_method_description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/objc_method_description.json'
content_hash: 'sha256:4d6ab1f4738b600f'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# objc_method_description

<sub>结构体</sub>

Defines an Objective-C method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct objc_method_description
```

## 关系

- **符合**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## 主题

### 字段

- [name](objc_method_description/name.md) — 运行时方法的名称。
- [types](objc_method_description/types.md) — 方法参数的类型。

### 初始化方法

- [init()](<objc_method_description/init().md>)
- [init(name:types:)](<objc_method_description/init(name_types_).md>)

## 另请参阅

### 类定义数据结构

- [Method](method.md) — 一个不透明类型，表示类定义中的一个方法。
- [Ivar](ivar.md) — 一个不透明类型，表示一个实例变量。
- [Category](category.md) — 一个不透明类型，表示一个分类。
- [objc_property_t](objc_property_t.md) — 表示 Objective-C 声明属性的不透明类型。
- [IMP](imp.md) — 一个指向方法实现起始位置的指针。
- [objc_cache](objc_cache.md) — 针对方法调用的性能优化。包含指向最近使用过的方法的指针。
- [objc_property_attribute_t](objc_property_attribute_t.md) — 定义一个属性特性。
