---
title: 'sel_registerName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/sel_registername(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/sel_registername(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/sel_registername%28_%3A%29.json'
content_hash: 'sha256:c4e1853e80c3bf09'
translated: true
---

> 导航：[技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# sel_registerName(_:)

<sub>函数</sub>

向 Objective-C runtime 系统注册一个方法，将方法名称映射为一个选择器（selector），并返回该选择器的值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sel_registerName(_ str: UnsafePointer<CChar>) -> Selector
```

## 参数

- `str` — 指向 C 字符串的指针。传入你希望注册的方法名称。

## 返回值

一个 [SEL](sel.md) 类型的指针，指定该命名方法的选择器。

## 讨论

你必须先向 Objective-C runtime 系统注册方法名称以获得该方法的选择器，然后才能将该方法添加到类定义中。如果该方法名称已经注册，此函数只是返回该选择器。

## 另请参阅

### 使用选择器

- [sel_getName](<sel_getname(__).md>) — 返回给定选择器（selector）所指定方法的名称。
- [sel_getUid](<sel_getuid(__).md>) — 向 Objective-C runtime 系统注册一个方法名称。
- [sel_isEqual](<sel_isequal(____).md>) — 返回一个布尔值，指示两个选择器是否相等。
