---
title: 'property_getName(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/property_getname(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/property_getname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/property_getname%28_%3A%29.json'
content_hash: 'sha256:111111f6bbed6154'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# property_getName(_:)

<sub>函数</sub>

返回属性的名称。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func property_getName(_ property: objc_property_t) -> UnsafePointer<CChar>
```

## 返回值

包含属性名称的 C 字符串。

## 另请参阅

### 使用属性

- [property_getAttributes](<property_getattributes(__).md>) — 返回一个属性的特性字符串。
- [property_copyAttributeValue](<property_copyattributevalue(____).md>) — 根据给定的特性名称返回属性特性的值。
- [property_copyAttributeList](<property_copyattributelist(____).md>) — 返回给定属性的属性特性数组。
