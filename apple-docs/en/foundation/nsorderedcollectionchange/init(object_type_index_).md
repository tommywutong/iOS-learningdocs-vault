---
title: 'init(object:type:index:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedcollectionchange/init(object:type:index:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/init(object:type:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectionchange/init%28object%3Atype%3Aindex%3A%29.json'
content_hash: 'sha256:ac867f6528f77a7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionChange](../nsorderedcollectionchange.md)

# init(object:type:index:)

<sub>Initializer</sub>

Creates a change object that represents inserting or removing an object from an ordered collection at a specific index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(object anObject: Any?, type: NSCollectionChangeType, index: Int)
```

## Parameters

- `anObject` — An optional object the change will remove or insert.

- `type` — The type of change.

- `index` — The index location within an ordered collection where the change applies.

## See Also

### Creating a Change

- [- initWithObject:type:index:associatedIndex:](<init(object_type_index_associatedindex_).md>) — Creates a change object that represents inserting, removing, or moving an object from an ordered collection at a specific index.
