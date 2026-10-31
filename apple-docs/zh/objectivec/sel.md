---
title: SEL
framework: Objective-C Runtime
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/sel
source_url: 'https://developer.apple.com/documentation/objectivec/sel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/sel.json'
content_hash: 'sha256:7416575cfa884cf0'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# SEL

<sub>类型别名</sub>

定义表示方法选择器的不透明类型。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef struct objc_selector * SEL;
```

## 讨论

方法选择器用于在运行时表示方法的名称。方法选择器是已在 Objective-C 运行时中注册（或“映射”）的 C 字符串。编译器生成的选择器会自动映射。

你可以在运行时使用函数 [sel_registerName](<sel_registername(__).md>) 添加新选择器并检索现有选择器。

使用选择器时，必须使用 [sel_registerName](<sel_registername(__).md>) 返回的值或 Objective-C 编译器指令 `@selector()`。不能简单地将 C 字符串强制转换为 `SEL`。

## 另请参阅

### 类定义数据结构

- [Class](class.md) — 一种不透明类型，表示一个 Objective-C 类。
- [Method](method.md) — 一个不透明类型，表示类定义中的一个方法。
- [Ivar](ivar.md) — 一个不透明类型，表示一个实例变量。
- [Category](category.md) — 一个不透明类型，表示一个分类。
- [objc_property_t](objc_property_t.md) — 表示 Objective-C 声明属性的不透明类型。
- [IMP](imp.md) — 一个指向方法实现起始位置的指针。
- [objc_method_description](objc_method_description.md) — 定义一个 Objective-C 方法。
- [objc_cache](objc_cache.md) — 针对方法调用的性能优化。包含指向最近使用过的方法的指针。
- [objc_property_attribute_t](objc_property_attribute_t.md) — 定义一个属性特性。
