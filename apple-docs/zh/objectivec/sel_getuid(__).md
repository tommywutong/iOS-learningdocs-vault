---
title: 'sel_getUid(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/sel_getuid(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/sel_getuid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/sel_getuid%28_%3A%29.json'
content_hash: 'sha256:efa5752d8338b768'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# sel_getUid(_:)

<sub>函数</sub>

向 Objective-C 运行时系统注册方法名称。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sel_getUid(_ str: UnsafePointer<CChar>) -> Selector
```

## 参数

- `str` — 指向 C 字符串的指针。传入要注册的方法名称。

## 返回值

类型为 [SEL](sel.md) 的指针，指定命名方法的选择器。

## 讨论

此方法的实现与 [sel_registerName](<sel_registername(__).md>) 的实现相同。

### Version-Notes

在 OS X 10.0 版之前，此方法尝试查找映射到给定名称的选择器，若未找到则返回 `NULL`。出于安全考虑已更改此行为，因为观察到许多调用者在没有检查返回值的情况下将选择器传递给 `objc_msgSend` 系列函数，而这在选择器为 `NULL` 时不安全。

## 另请参阅

### 处理选择器

- [sel_getName](<sel_getname(__).md>) — 返回由给定选择器指定的方法的名称。
- [sel_registerName](<sel_registername(__).md>) — 向 Objective-C 运行时系统注册方法，将方法名映射到选择器，并返回选择器值。
- [sel_isEqual](<sel_isequal(____).md>) — 返回一个布尔值，指示两个选择器是否相等。
