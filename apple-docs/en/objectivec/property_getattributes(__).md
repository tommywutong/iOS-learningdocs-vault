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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# property_getAttributes(_:)

<sub>Function</sub>

Returns the attribute string of a property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func property_getAttributes(_ property: objc_property_t) -> UnsafePointer<CChar>?
```

## Return Value

A C string containing the property’s attributes.

## Discussion

The format of the attribute string is described in [Declared Properties](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtPropertyIntrospection.html#//apple_ref/doc/uid/TP40008048-CH101) in [Objective-C Runtime Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008048).

## See Also

### Working with Properties

- [property_getName](<property_getname(__).md>) — Returns the name of a property.
- [property_copyAttributeValue](<property_copyattributevalue(____).md>) — Returns the value of a property attribute given the attribute name.
- [property_copyAttributeList](<property_copyattributelist(____).md>) — Returns an array of property attributes for a given property.
