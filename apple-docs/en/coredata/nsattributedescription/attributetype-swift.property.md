---
title: attributeType
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nsattributedescription/attributetype-swift.property
source_url: 'https://developer.apple.com/documentation/coredata/nsattributedescription/attributetype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsattributedescription/attributetype-swift.property.json'
content_hash: 'sha256:2e94a20576901368'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAttributeDescription](../nsattributedescription.md)

# attributeType

<sub>Instance Property</sub>

The attribute’s type.

> [!warning] Deprecated
> Use [type](type.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attributeType: NSAttributeType { get set }
```

## Discussion

Don’t change an attribute’s type after you add its containing managed object model to a persistent store coordinator; otherwise, Core Data throws an exception.

## See Also

### Managing the type

- [attributeValueClassName](attributevalueclassname.md) — The class name that represents the attribute’s value.
- [type](type.md) — The attribute’s type.
- [AttributeType](attributetype-swift.struct.md) — The types of attributes that Core Data supports.
- [NSAttributeType](../nsattributetype.md) — The types of attribute that Core Data supports.
