---
title: DropSession
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropsession
source_url: 'https://developer.apple.com/documentation/swiftui/dropsession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropsession.json'
content_hash: 'sha256:9ee6de529b0572fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DropSession

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct DropSession
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Escapable](../swift/escapable.md), [Identifiable](../swift/identifiable.md)

## Topics

### Getting drop session details

- [id](dropsession/id-swift.property.md) — The unique identifier of the drop session.
- [ID](dropsession/id-swift.struct.md) — The identifier of a drag session.
- [localSession](dropsession/localsession-swift.property.md) — Provides additional information about a session if it originated within the app.
- [LocalSession](dropsession/localsession-swift.struct.md) — Describes the session originated within the app.
- [phase](dropsession/phase-swift.property.md) — The phase of the current drop session.
- [Phase](dropsession/phase-swift.enum.md) — The phase of the current drop session.
- [suggestedOperations](dropsession/suggestedoperations.md) — Operations suggested by the drag source.

### Getting drop details

- [itemsCount](dropsession/itemscount.md) — Number of items for the drop.
- [location](dropsession/location.md) — Location of drop in the local coordinate space
- [size](dropsession/size.md) — Size of the drop destination view.

### Supporting reordering

- [reorderDestination(for:in:)](<dropsession/reorderdestination(for_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_
- [reorderDestination(for:itemID:in:)](<dropsession/reorderdestination(for_itemid_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_

## See Also

### Moving items

- [DragSession](dragsession.md) — Describes the ongoing dragging session.
