---
title: 'property_copyAttributeValue(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/property_copyattributevalue(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/property_copyattributevalue(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/property_copyattributevalue%28_%3A_%3A%29.json'
content_hash: 'sha256:a51d0fad1eb1cd72'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# property_copyAttributeValue(_:_:)

<sub>函数</sub>

返回给定特性名称对应的属性特性值。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func property_copyAttributeValue(_ property: objc_property_t, _ attributeName: UnsafePointer<CChar>) -> UnsafeMutablePointer<CChar>?
```

## 参数

- `property` — 你感兴趣的属性。

- `attributeName` — 表示特性名称的 C 字符串。

## 返回值

若 `property` 中存在 `attributeName` 特性，则为其值字符串；否则为 `nil`。必须使用 `free()` 释放返回的值字符串。

## 另请参阅

### 处理属性

- [property_getName](<property_getname(__).md>) — 返回属性的名称。
- [property_getAttributes](<property_getattributes(__).md>) — 返回属性的特性字符串。
- [property_copyAttributeList](<property_copyattributelist(____).md>) — 返回给定属性的属性特性数组。
