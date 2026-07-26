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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# property_copyAttributeList(_:_:)

<sub>Function</sub>

Returns an array of property attributes for a given property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func property_copyAttributeList(_ property: objc_property_t, _ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<objc_property_attribute_t>?
```

## Parameters

- `property` — The property whose attributes you want to copy.

- `outCount` — The number of attributes returned in the array.

## Return Value

An array of property attributes. You must free the array with `free()`.

## See Also

### Working with Properties

- [property_getName](<property_getname(__).md>) — Returns the name of a property.
- [property_getAttributes](<property_getattributes(__).md>) — Returns the attribute string of a property.
- [property_copyAttributeValue](<property_copyattributevalue(____).md>) — Returns the value of a property attribute given the attribute name.
