---
title: versionHash
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspropertydescription/versionhash
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/versionhash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/versionhash.json'
content_hash: 'sha256:62ac6453e7a2e3a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# versionHash

<sub>Instance Property</sub>

The version hash for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var versionHash: Data { get }
```

## Discussion

The version hash is used to uniquely identify a property based on its configuration. The version hash uses only values which affect the persistence of data and the user-defined [versionHashModifier](versionhashmodifier.md) value. (The values which affect persistence are the name of the property, and the flags for `isOptional`, `isTransient`, and `isReadOnly`.) This value is stored as part of the version information in the metadata for stores, as well as a definition of a property involved in an `NSPropertyMapping` object.

## See Also

### Supporting Versioning

- [versionHashModifier](versionhashmodifier.md) — The version hash modifier for the receiver.
- [renamingIdentifier](renamingidentifier.md) — The renaming identifier for the receiver.
