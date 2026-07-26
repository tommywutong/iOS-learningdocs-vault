---
title: NSFetchIndexDescription
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsfetchindexdescription
source_url: 'https://developer.apple.com/documentation/coredata/nsfetchindexdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsfetchindexdescription.json'
content_hash: 'sha256:08cca2702ce07ad1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSFetchIndexDescription

<sub>Class</sub>

The description of the index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSFetchIndexDescription
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an Index Description

- [- initWithName:elements:](<nsfetchindexdescription/init(name_elements_).md>) — Creates a fetch index description using the specified name and element descriptions.

### Inspecting an Index Description

- [elements](nsfetchindexdescription/elements.md) — An array of fetch index element descriptions.
- [entity](nsfetchindexdescription/entity.md) — The entity description for the fetch index description.
- [name](nsfetchindexdescription/name.md) — The name of the fetch index description.
- [partialIndexPredicate](nsfetchindexdescription/partialindexpredicate.md) — A predicate that selects rows for indexing, if the index is a partial index.

### Initializers

- [init(coder:)](<nsfetchindexdescription/init(coder_).md>)

## See Also

### Working with indexes

- [NSFetchIndexElementType](nsfetchindexelementtype.md) — Defines the possible types of index elements.
- [NSFetchIndexElementDescription](nsfetchindexelementdescription.md) — Description of an Index Element
