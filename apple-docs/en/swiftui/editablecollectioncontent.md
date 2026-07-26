---
title: EditableCollectionContent
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/editablecollectioncontent
source_url: 'https://developer.apple.com/documentation/swiftui/editablecollectioncontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/editablecollectioncontent.json'
content_hash: 'sha256:3b2c942ab1deaf6d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EditableCollectionContent

<sub>Structure</sub>

An opaque wrapper view that adds editing capabilities to a row in a list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct EditableCollectionContent<Content, Data>
```

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your behalf.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [View](view.md)

## See Also

### Editing a list

- [moveDisabled(_:)](<view/movedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is movable.
- [deleteDisabled(_:)](<view/deletedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is deletable.
- [editMode](environmentvalues/editmode.md) — An indication of whether the user can edit the contents of a view associated with this environment.
- [EditMode](editmode.md) — A mode that indicates whether the user can edit a view’s content.
- [EditActions](editactions.md) — A set of edit actions on a collection of data that a view can offer to a user.
- [IndexedIdentifierCollection](indexedidentifiercollection.md) — A collection wrapper that iterates over the indices and identifiers of a collection together.
