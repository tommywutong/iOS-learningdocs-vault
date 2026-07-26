---
title: IndexedIdentifierCollection
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/indexedidentifiercollection
source_url: 'https://developer.apple.com/documentation/swiftui/indexedidentifiercollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/indexedidentifiercollection.json'
content_hash: 'sha256:f47ea4c0d81b916e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# IndexedIdentifierCollection

<sub>Structure</sub>

A collection wrapper that iterates over the indices and identifiers of a collection together.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IndexedIdentifierCollection<Base, ID> where Base : Collection, ID : Hashable
```

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your behalf.

## Relationships

- **Conforms To**: [BidirectionalCollection](../swift/bidirectionalcollection.md), [Collection](../swift/collection.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [RandomAccessCollection](../swift/randomaccesscollection.md), [Sequence](../swift/sequence.md)

## See Also

### Editing a list

- [moveDisabled(_:)](<view/movedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is movable.
- [deleteDisabled(_:)](<view/deletedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is deletable.
- [editMode](environmentvalues/editmode.md) — An indication of whether the user can edit the contents of a view associated with this environment.
- [EditMode](editmode.md) — A mode that indicates whether the user can edit a view’s content.
- [EditActions](editactions.md) — A set of edit actions on a collection of data that a view can offer to a user.
- [EditableCollectionContent](editablecollectioncontent.md) — An opaque wrapper view that adds editing capabilities to a row in a list.
