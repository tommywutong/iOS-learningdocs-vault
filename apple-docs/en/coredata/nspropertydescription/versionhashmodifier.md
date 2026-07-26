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
doc_path: /documentation/coredata/nspropertydescription/versionhashmodifier
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/versionhashmodifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/versionhashmodifier.json'
content_hash: 'sha256:d541765ec1aa89a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# versionHashModifier

<sub>Instance Property</sub>

The version hash modifier for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var versionHashModifier: String? { get set }
```

## Discussion

This value is included in the version hash for the property. You use it to mark or denote a property as being a different “version” than another even if all of the values which affect persistence are equal. (Such a difference is important in cases where the attributes of a property are unchanged but the format or content of its data are changed.)

## See Also

### Supporting Versioning

- [versionHash](versionhash.md) — The version hash for the receiver.
- [renamingIdentifier](renamingidentifier.md) — The renaming identifier for the receiver.
