---
title: DropSession.ID
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropsession/id-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftui/dropsession/id-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropsession/id-swift.struct.json'
content_hash: 'sha256:2256df35cf4e57f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropSession](../dropsession.md)

# DropSession.ID

<sub>Structure</sub>

The identifier of a drag session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct ID
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Methods

- [matches(_:)](<id-swift.struct/matches(__).md>) — Checks if the session value describes the same drag session as the object provided by AppKit.

## See Also

### Getting drop session details

- [id](id-swift.property.md) — The unique identifier of the drop session.
- [localSession](localsession-swift.property.md) — Provides additional information about a session if it originated within the app.
- [LocalSession](localsession-swift.struct.md) — Describes the session originated within the app.
- [phase](phase-swift.property.md) — The phase of the current drop session.
- [Phase](phase-swift.enum.md) — The phase of the current drop session.
- [suggestedOperations](suggestedoperations.md) — Operations suggested by the drag source.
