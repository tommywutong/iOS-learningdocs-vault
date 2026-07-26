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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# property_copyAttributeValue(_:_:)

<sub>Function</sub>

Returns the value of a property attribute given the attribute name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func property_copyAttributeValue(_ property: objc_property_t, _ attributeName: UnsafePointer<CChar>) -> UnsafeMutablePointer<CChar>?
```

## Parameters

- `property` — The property whose value you are interested in.

- `attributeName` — A C string representing the name of the attribute.

## Return Value

The value string of the `attributeName` attribute, if one exists in `property`; otherwise, `nil`. You must free the returned value string with `free()`.

## See Also

### Working with Properties

- [property_getName](<property_getname(__).md>) — Returns the name of a property.
- [property_getAttributes](<property_getattributes(__).md>) — Returns the attribute string of a property.
- [property_copyAttributeList](<property_copyattributelist(____).md>) — Returns an array of property attributes for a given property.
