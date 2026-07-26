---
title: type
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsattributedescription/type
source_url: 'https://developer.apple.com/documentation/coredata/nsattributedescription/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributedescription/type.json'
content_hash: 'sha256:8c856add7933ae01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAttributeDescription](../nsattributedescription.md)

# type

<sub>Instance Property</sub>

The attribute’s type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var type: NSAttributeDescription.AttributeType { get set }
```

## Discussion

Don’t change an attribute’s type after you add its containing managed object model to a persistent store coordinator; otherwise, Core Data throws an exception.

## See Also

### Managing the type

- [attributeValueClassName](attributevalueclassname.md) — The class name that represents the attribute’s value.
- [AttributeType](attributetype-swift.struct.md) — The types of attributes that Core Data supports.
- [attributeType](attributetype-swift.property.md) — The attribute’s type. _(deprecated)_
- [NSAttributeType](../nsattributetype.md) — The types of attribute that Core Data supports.
