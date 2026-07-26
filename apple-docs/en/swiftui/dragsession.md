---
title: DragSession
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dragsession
source_url: 'https://developer.apple.com/documentation/swiftui/dragsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dragsession.json'
content_hash: 'sha256:a5e1700fb72c358e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DragSession

<sub>Structure</sub>

Describes the ongoing dragging session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DragSession
```

## Relationships

- **Conforms To**: [Identifiable](../swift/identifiable.md)

## Topics

### Structures

- [ID](dragsession/id-swift.struct.md) — The identifier of a drag session.

### Instance Properties

- [draggedItemIndex](dragsession/draggeditemindex.md) — The index of the dragged item under the cursor.
- [id](dragsession/id-swift.property.md) — The identifier of the drag session.
- [location](dragsession/location.md) — Location of the drag session in the local coordinate space.
- [phase](dragsession/phase-swift.property.md) — The current phase of the drag session.

### Instance Methods

- [draggedItemIDs(for:)](<dragsession/draggeditemids(for_).md>) — Provides an array of identifiers of the currently dragged items in a case when the items conform to the `Identifiable` protocol, or identifiers were provided to SwiftUI separately.

### Enumerations

- [Phase](dragsession/phase-swift.enum.md) — The phase of the current drag session

## See Also

### Moving items

- [DropSession](dropsession.md)
