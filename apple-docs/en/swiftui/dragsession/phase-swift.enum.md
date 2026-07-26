---
title: DragSession.Phase
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dragsession/phase-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftui/dragsession/phase-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dragsession/phase-swift.enum.json'
content_hash: 'sha256:c536c5cef6cfe1ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DragSession](../dragsession.md)

# DragSession.Phase

<sub>Enumeration</sub>

The phase of the current drag session

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum Phase
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [DragSession.Phase.active](phase-swift.enum/active.md) — The drag has moved to a new location.
- [DragSession.Phase.dataTransferCompleted](phase-swift.enum/datatransfercompleted.md) — Dragged items have been transferred. You can remove temporary items, perform any cleanup if needed.
- [DragSession.Phase.ended(_:)](<phase-swift.enum/ended(__).md>) — The drag has ended.
- [DragSession.Phase.ending(_:)](<phase-swift.enum/ending(__).md>) — The drag is about to finish.
- [DragSession.Phase.initial](phase-swift.enum/initial.md) — The drag session is about to begin
