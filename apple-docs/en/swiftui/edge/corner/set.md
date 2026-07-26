---
title: Edge.Corner.Set
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/edge/corner/set
source_url: 'https://developer.apple.com/documentation/swiftui/edge/corner/set'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/edge/corner/set.json'
content_hash: 'sha256:b0cd497188a6b4ca'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Edge](../../edge.md) · [Corner](../corner.md)

# Edge.Corner.Set

<sub>Structure</sub>

An efficient set of corners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Set
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [ExpressibleByArrayLiteral](../../../swift/expressiblebyarrayliteral.md), [Hashable](../../../swift/hashable.md), [OptionSet](../../../swift/optionset.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md), [SetAlgebra](../../../swift/setalgebra.md)

## Topics

### Initializers

- [init(_:)](<set/init(__).md>) — Creates set of corners containing only the specified corner.
- [init(rawValue:)](<set/init(rawvalue_).md>) — Creates a corner set given a raw value.

### Instance Methods

- [contains(_:)](<set/contains(__).md>) — Returns true only if `corner` is a member of the calling set.

### Type Properties

- [all](set/all.md) — All corners.
- [bottom](set/bottom.md) — The bottom leading and trailing corners.
- [bottomLeading](set/bottomleading.md) — The bottom leading corner.
- [bottomTrailing](set/bottomtrailing.md) — The bottom trailing corner.
- [leading](set/leading.md) — The top and bottom leading corners.
- [none](set/none.md) — No corners.
- [top](set/top.md) — The top leading and trailing corners.
- [topLeading](set/topleading.md) — The top leading corner.
- [topTrailing](set/toptrailing.md) — The top trailing corner.
- [trailing](set/trailing.md) — The top and bottom trailing corners.
