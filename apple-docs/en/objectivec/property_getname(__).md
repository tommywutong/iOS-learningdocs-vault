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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# property_getName(_:)

<sub>Function</sub>

Returns the name of a property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func property_getName(_ property: objc_property_t) -> UnsafePointer<CChar>
```

## Return Value

A C string containing the property’s name.

## See Also

### Working with Properties

- [property_getAttributes](<property_getattributes(__).md>) — Returns the attribute string of a property.
- [property_copyAttributeValue](<property_copyattributevalue(____).md>) — Returns the value of a property attribute given the attribute name.
- [property_copyAttributeList](<property_copyattributelist(____).md>) — Returns an array of property attributes for a given property.
