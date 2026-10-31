---
title: 'sel_isEqual(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/sel_isequal(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/sel_isequal(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/sel_isequal%28_%3A_%3A%29.json'
content_hash: 'sha256:16aaae7575d1331a'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# sel_isEqual(_:_:)

<sub>函数</sub>

返回一个布尔值，指示两个选择器是否相等。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sel_isEqual(_ lhs: Selector, _ rhs: Selector) -> Bool
```

## 参数

- `lhs` — The selector to compare with `rhs`.

- `rhs` — The selector to compare with `lhs`.

## 返回值

[YES](yes.md) if `rhs` and `rhs` are equal, otherwise [NO](no.md).

## 讨论

`sel_isEqual` is equivalent to `==`.

## 另请参阅

### 处理选择器

- [sel_getName](<sel_getname(__).md>) — 返回由给定选择器指定的方法的名称。
- [sel_registerName](<sel_registername(__).md>) — 向 Objective-C 运行时系统注册方法，将方法名映射到选择器，并返回选择器值。
- [sel_getUid](<sel_getuid(__).md>) — 向 Objective-C 运行时系统注册方法名。
