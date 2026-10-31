---
title: 'property_getAttributes(_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/property_getattributes(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/property_getattributes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/property_getattributes%28_%3A%29.json'
content_hash: 'sha256:c394780912a717f2'
translated: true
---

> 导航： [技术](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# property_getAttributes(_:)

<sub>函数</sub>

返回属性的特性字符串。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func property_getAttributes(_ property: objc_property_t) -> UnsafePointer<CChar>?
```

## 返回值

包含该属性特性的 C 字符串。

## 讨论

特性字符串的格式在 [Objective-C Runtime Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048) 的 [Declared Properties](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtPropertyIntrospection.html#//apple_ref/doc/uid/TP40008048-CH101) 中说明。

## 另请参阅

### 处理属性

- [property_getName](<property_getname(__).md>) — 返回属性的名称。
- [property_copyAttributeValue](<property_copyattributevalue(____).md>) — 返回给定特性名称对应的属性特性值。
- [property_copyAttributeList](<property_copyattributelist(____).md>) — 返回给定属性的属性特性数组。
