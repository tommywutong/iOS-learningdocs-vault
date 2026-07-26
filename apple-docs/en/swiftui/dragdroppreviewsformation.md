---
title: DragDropPreviewsFormation
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dragdroppreviewsformation
source_url: 'https://developer.apple.com/documentation/swiftui/dragdroppreviewsformation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dragdroppreviewsformation.json'
content_hash: 'sha256:534404fa86bfc777'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DragDropPreviewsFormation

<sub>Structure</sub>

On macOS, describes the way the dragged previews are visually composed. Both drag sources and drop destination can specify their desired preview formation.

<sub>macOS</sub>

```swift
struct DragDropPreviewsFormation
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [default](dragdroppreviewsformation/default.md) — System-determined composition.
- [list](dragdroppreviewsformation/list.md) — Drag images are laid out vertically, non-overlapping, and the left edges are aligned.
- [none](dragdroppreviewsformation/none.md) — Drag images maintain their set positions relative to each other.
- [pile](dragdroppreviewsformation/pile.md) — Drag images are placed on top of each other with random rotations.
- [stack](dragdroppreviewsformation/stack.md) — Drag images are laid out overlapping diagonally.

## See Also

### Describing preview formations

- [dragPreviewsFormation(_:)](<view/dragpreviewsformation(__).md>) — Describes the way dragged previews are visually composed.
- [dropPreviewsFormation(_:)](<view/droppreviewsformation(__).md>) — Describes the way previews for a drop are composed.
