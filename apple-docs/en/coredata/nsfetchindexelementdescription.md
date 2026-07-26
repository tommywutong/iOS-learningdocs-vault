---
title: NSFetchIndexElementDescription
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchindexelementdescription
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchindexelementdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchindexelementdescription.json'
content_hash: 'sha256:055bdcb750c28629'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSFetchIndexElementDescription

<sub>Class</sub>

Description of an Index Element

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSFetchIndexElementDescription
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an Index Element Description

- [- initWithProperty:collationType:](<nsfetchindexelementdescription/init(property_collationtype_).md>) — Creates an index element description using the specified property description and collation type.

### Inspecting an Index Element Description

- [collationType](nsfetchindexelementdescription/collationtype.md) — The type of collation that the index element uses, either binary or R-tree.
- [indexDescription](nsfetchindexelementdescription/indexdescription.md)
- [ascending](nsfetchindexelementdescription/isascending.md) — A Boolean value that controls whether an index that supports direction is an ascending or descending index.
- [property](nsfetchindexelementdescription/property.md) — A property description.
- [propertyName](nsfetchindexelementdescription/propertyname.md) — The specified name in the property description.

### Initializers

- [init(coder:)](<nsfetchindexelementdescription/init(coder_).md>)

## See Also

### Working with indexes

- [NSFetchIndexElementType](nsfetchindexelementtype.md) — Defines the possible types of index elements.
- [NSFetchIndexDescription](nsfetchindexdescription.md) — The description of the index.
