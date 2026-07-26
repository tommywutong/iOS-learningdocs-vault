---
title: EditActions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/editactions
source_url: 'https://developer.apple.com/documentation/swiftui/editactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/editactions.json'
content_hash: 'sha256:385ddeacf2053bfe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EditActions

<sub>Structure</sub>

A set of edit actions on a collection of data that a view can offer to a user.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct EditActions<Data>
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting edit operations

- [all](editactions/all-45m4m.md) — All the edit actions available on this collection.
- [all](editactions/all-4dctm.md) — All the edit actions available on this collection.
- [all](editactions/all-4uyun.md) — All the edit actions available on this collection.
- [all](editactions/all-6ryvk.md) — All the edit actions available on this collection.
- [delete](editactions/delete.md) — An edit action that allows the user to delete one or more elements of a collection.
- [move](editactions/move.md) — An edit action that allows the user to move elements of a collection.

### Creating an edit operation

- [init(rawValue:)](<editactions/init(rawvalue_).md>) — Creates a new set from a raw value.
- [rawValue](editactions/rawvalue.md) — The raw value.

## See Also

### Editing a list

- [moveDisabled(_:)](<view/movedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is movable.
- [deleteDisabled(_:)](<view/deletedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is deletable.
- [editMode](environmentvalues/editmode.md) — An indication of whether the user can edit the contents of a view associated with this environment.
- [EditMode](editmode.md) — A mode that indicates whether the user can edit a view’s content.
- [EditableCollectionContent](editablecollectioncontent.md) — An opaque wrapper view that adds editing capabilities to a row in a list.
- [IndexedIdentifierCollection](indexedidentifiercollection.md) — A collection wrapper that iterates over the indices and identifiers of a collection together.
