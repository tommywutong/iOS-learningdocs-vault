---
title: 'sel_getName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/sel_getname(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/sel_getname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/sel_getname%28_%3A%29.json'
content_hash: 'sha256:3a3c7aa8309be1ac'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# sel_getName(_:)

<sub>函数</sub>

返回由给定选择器指定的方法的名称。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sel_getName(_ sel: Selector) -> UnsafePointer<CChar>
```

## 参数

- `sel` — 类型为 [SEL](sel.md) 的指针。传入你希望确定其名称的选择器。

## 返回值

指示选择器名称的 C 字符串。

## 另请参阅

### 处理选择器

- [sel_registerName](<sel_registername(__).md>) — 向 Objective-C 运行时系统注册方法，将方法名映射到选择器，并返回选择器值。
- [sel_getUid](<sel_getuid(__).md>) — 向 Objective-C 运行时系统注册方法名。
- [sel_isEqual](<sel_isequal(____).md>) — 返回一个布尔值，指示两个选择器是否相等。
