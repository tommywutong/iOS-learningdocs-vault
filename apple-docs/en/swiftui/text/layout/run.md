---
title: Text.Layout.Run
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/layout/run
source_url: 'https://developer.apple.com/documentation/swiftui/text/layout/run'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/layout/run.json'
content_hash: 'sha256:160da95ca3da118a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [Layout](../layout.md)

# Text.Layout.Run

<sub>Structure</sub>

A run of placed glyphs in a text layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Run
```

## Relationships

- **Conforms To**: [BidirectionalCollection](../../../swift/bidirectionalcollection.md), [Collection](../../../swift/collection.md), [Equatable](../../../swift/equatable.md), [RandomAccessCollection](../../../swift/randomaccesscollection.md), [Sequence](../../../swift/sequence.md)

## Topics

### Instance Properties

- [characterIndices](run/characterindices.md) — The array of character indices corresponding to the glyphs in `self`.
- [layoutDirection](run/layoutdirection.md) — The layout direction of the text run.
- [typographicBounds](run/typographicbounds.md) — The typographic bounds of the run of glyphs.

### Subscripts

- [subscript(_:)](<run/subscript(__).md>) — The custom attribute of type `T` associated with the run of glyphs, or nil. If no run contains the custom attribute we also check its attachment’s runs.
