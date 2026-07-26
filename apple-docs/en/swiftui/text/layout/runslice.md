---
title: Text.Layout.RunSlice
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/layout/runslice
source_url: 'https://developer.apple.com/documentation/swiftui/text/layout/runslice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/layout/runslice.json'
content_hash: 'sha256:c57ffaf9034fff42'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [Layout](../layout.md)

# Text.Layout.RunSlice

<sub>Structure</sub>

A slice of a run of placed glyphs in a text layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RunSlice
```

## Relationships

- **Conforms To**: [BidirectionalCollection](../../../swift/bidirectionalcollection.md), [Collection](../../../swift/collection.md), [Equatable](../../../swift/equatable.md), [RandomAccessCollection](../../../swift/randomaccesscollection.md), [Sequence](../../../swift/sequence.md)

## Topics

### Initializers

- [init(run:indices:)](<runslice/init(run_indices_).md>)

### Instance Properties

- [characterIndices](runslice/characterindices.md) — The array of character indices corresponding to the glyphs in `self`.
- [run](runslice/run.md)
- [typographicBounds](runslice/typographicbounds.md) — The typographic bounds of the partial run of glyphs.

### Subscripts

- [subscript(_:)](<runslice/subscript(__).md>) — The custom attribute of type `T` associated with the run of glyphs, or nil.
