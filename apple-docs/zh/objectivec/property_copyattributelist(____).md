---
title: 'property_copyAttributeList(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/property_copyattributelist(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/property_copyattributelist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/property_copyattributelist%28_%3A_%3A%29.json'
content_hash: 'sha256:1d9430616a3c297b'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# property_copyAttributeList(_:_:)

<sub>函数</sub>

返回给定属性的属性特性数组。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func property_copyAttributeList(_ property: objc_property_t, _ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_attribute_t>?
```

## 参数

- `property` — 要拷贝其特性的属性。

- `outCount` — 数组中返回的特性数量。

## 返回值

属性特性数组。必须使用 `free()` 释放该数组。

## 另请参阅

### 处理属性

- [property_getName](<property_getname(__).md>) — 返回属性的名称。
- [property_getAttributes](<property_getattributes(__).md>) — 返回属性的特性字符串。
- [property_copyAttributeValue](<property_copyattributevalue(____).md>) — 返回给定特性名称对应的属性特性值。
