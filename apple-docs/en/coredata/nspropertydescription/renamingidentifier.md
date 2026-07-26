---
title: renamingIdentifier
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspropertydescription/renamingidentifier
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription/renamingidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription/renamingidentifier.json'
content_hash: 'sha256:a1f6366ffae81c59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPropertyDescription](../nspropertydescription.md)

# renamingIdentifier

<sub>Instance Property</sub>

The renaming identifier for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var renamingIdentifier: String? { get set }
```

## Discussion

This is used to resolve naming conflicts between models. When creating an entity mapping between entities in two managed object models, a source entity property and a destination entity property that share the same identifier indicate that a property mapping should be configured to migrate from the source to the destination. If unset, the identifier will return the property’s name.

## See Also

### Supporting Versioning

- [versionHash](versionhash.md) — The version hash for the receiver.
- [versionHashModifier](versionhashmodifier.md) — The version hash modifier for the receiver.
