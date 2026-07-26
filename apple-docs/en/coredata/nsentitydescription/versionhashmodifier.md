---
title: versionHashModifier
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription/versionhashmodifier
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription/versionhashmodifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription/versionhashmodifier.json'
content_hash: 'sha256:c79653c13b017e23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSEntityDescription](../nsentitydescription.md)

# versionHashModifier

<sub>Instance Property</sub>

The version hash modifier for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var versionHashModifier: String? { get set }
```

## Discussion

This value is included in the version hash for the entity. You use it to mark or denote an entity as being a different “version” than another even if all of the values which affect persistence are equal. (Such a difference is important in cases where, for example, the structure of an entity is unchanged but the format or content of data has changed.)

## See Also

### Managing versioning

- [versionHash](versionhash.md) — The version hash for the receiver.
