---
title: DropSession.Phase
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropsession/phase-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftui/dropsession/phase-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropsession/phase-swift.enum.json'
content_hash: 'sha256:cb9b1277985719e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropSession](../dropsession.md)

# DropSession.Phase

<sub>Enumeration</sub>

The phase of the current drop session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum Phase
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [DropSession.Phase.active](phase-swift.enum/active.md) — The drop session is active inside the drop destination.
- [DropSession.Phase.dataTransferCompleted](phase-swift.enum/datatransfercompleted.md) — Dragged items have been transferred. You can remove temporary items, perform any cleanup if needed.
- [DropSession.Phase.ended(_:)](<phase-swift.enum/ended(__).md>) — The drop has ended.
- [DropSession.Phase.entering](phase-swift.enum/entering.md) — The drop session is entering the drop destination.
- [DropSession.Phase.exiting](phase-swift.enum/exiting.md) — The drop session has exited the drop destination.

## See Also

### Getting drop session details

- [id](id-swift.property.md) — The unique identifier of the drop session.
- [ID](id-swift.struct.md) — The identifier of a drag session.
- [localSession](localsession-swift.property.md) — Provides additional information about a session if it originated within the app.
- [LocalSession](localsession-swift.struct.md) — Describes the session originated within the app.
- [phase](phase-swift.property.md) — The phase of the current drop session.
- [suggestedOperations](suggestedoperations.md) — Operations suggested by the drag source.
