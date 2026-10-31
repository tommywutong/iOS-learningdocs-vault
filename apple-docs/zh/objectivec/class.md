---
title: Class
framework: Objective-C Runtime
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/class
source_url: 'https://developer.apple.com/documentation/objectivec/class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class.json'
content_hash: 'sha256:7850071c794c50fe'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# Class

<sub>类型别名</sub>

一种不透明类型，表示一个 Objective-C 类。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct objc_class * Class;
```

## 另请参阅

### 类定义数据结构

- [Method](method.md) — 一种不透明类型，表示类定义中的一个方法。
- [Ivar](ivar.md) — 一种不透明类型，表示一个实例变量。
- [Category](category.md) — 一种不透明类型，表示一个分类。
- [objc_property_t](objc_property_t.md) — 一种不透明类型，表示一个 Objective-C 声明的属性。
- [IMP](imp.md) — 指向方法实现起始位置的指针。
- [SEL](sel.md) — 定义一种不透明类型，表示一个方法选择器（selector）。
- [objc_method_description](objc_method_description.md) — 定义一个 Objective-C 方法。
- [objc_cache](objc_cache.md) — 方法调用的性能优化。包含指向最近使用的方法的指针。
- [objc_property_attribute_t](objc_property_attribute_t.md) — 定义一个属性特性。
