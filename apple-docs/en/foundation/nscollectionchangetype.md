---
title: NSCollectionChangeType
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscollectionchangetype
source_url: 'https://developer.apple.com/documentation/foundation/nscollectionchangetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscollectionchangetype.json'
content_hash: 'sha256:ad880430af8d78c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSCollectionChangeType

<sub>Enumeration</sub>

The type of change represented in computing the difference of an ordered collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSCollectionChangeType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Types of Ordered Collection Changes

- [NSCollectionChangeInsert](nscollectionchangetype/insert.md) — A change type that represents the insertion of an object into an ordered collection.
- [NSCollectionChangeRemove](nscollectionchangetype/remove.md) — A change type that represents the removal of an object from an ordered collection.

### Initializers

- [init(rawValue:)](<nscollectionchangetype/init(rawvalue_).md>)

## See Also

### Accessing Changes

- [hasChanges](nsorderedcollectiondifference/haschanges.md) — A Boolean value that indicates if the difference has changes.
- [insertions](nsorderedcollectiondifference/insertions.md) — A collection of insertion change objects.
- [removals](nsorderedcollectiondifference/removals.md) — A collection of removal change objects.
- [NSOrderedCollectionChange](nsorderedcollectionchange.md) — An object that represents an indexed change within an ordered collection.
