---
title: Text.Layout
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/layout
source_url: 'https://developer.apple.com/documentation/swiftui/text/layout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/layout.json'
content_hash: 'sha256:7384628c828ae1f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# Text.Layout

<sub>Structure</sub>

A value describing the layout and custom attributes of a tree of `Text` views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Layout
```

## Relationships

- **Conforms To**: [BidirectionalCollection](../../swift/bidirectionalcollection.md), [Collection](../../swift/collection.md), [Equatable](../../swift/equatable.md), [RandomAccessCollection](../../swift/randomaccesscollection.md), [Sequence](../../swift/sequence.md)

## Topics

### Structures

- [CharacterIndex](layout/characterindex.md) — The index of a character in the source text. An opaque type, this is intended to be used to determine relative locations of elements in the layout, rather than how they map to the source strings.
- [DrawingOptions](layout/drawingoptions.md) — Option flags used when drawing `Text.Layout` lines or runs into a graphics context.
- [Line](layout/line.md) — A single line in a text layout: a collection of runs of placed glyphs.
- [Run](layout/run.md) — A run of placed glyphs in a text layout.
- [RunSlice](layout/runslice.md) — A slice of a run of placed glyphs in a text layout.
- [TypographicBounds](layout/typographicbounds.md) — The typographic bounds of an element in a text layout.

### Instance Properties

- [isTruncated](layout/istruncated.md) — Indicates if this text is truncated.
