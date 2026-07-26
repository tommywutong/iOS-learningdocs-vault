---
title: SpatialEventCollection.Event.Kind
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialeventcollection/event/kind-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/kind-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialeventcollection/event/kind-swift.enum.json'
content_hash: 'sha256:615bc5e9d3eb21bb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SpatialEventCollection](../../spatialeventcollection.md) · [Event](../event.md)

# SpatialEventCollection.Event.Kind

<sub>Enumeration</sub>

The possible input sources or modes of an event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
enum Kind
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md)

## Topics

### Getting the event type

- [SpatialEventCollection.Event.Kind.directPinch](kind-swift.enum/directpinch.md) — An event generated from a pinching hand in close proximity to content.
- [SpatialEventCollection.Event.Kind.indirectPinch](kind-swift.enum/indirectpinch.md) — An event generated from an indirectly targeted pinching hand.
- [SpatialEventCollection.Event.Kind.pointer](kind-swift.enum/pointer.md) — An event representing a click-based, indirect input device describing the input sequence from click to click release.
- [SpatialEventCollection.Event.Kind.touch](kind-swift.enum/touch.md) — An event generated from a touch directly targeting content.

### Enumeration Cases

- [SpatialEventCollection.Event.Kind.pencil](kind-swift.enum/pencil.md) — An event generated from a pencil making contact with content.

## See Also

### Identifying the event

- [timestamp](timestamp.md) — The time the event was processed.
- [id](id-swift.property.md) — An identifier that uniquely identifies the event over its lifetime.
- [ID](id-swift.struct.md) — A value that uniquely identifies an event over the course of its lifetime.
- [kind](kind-swift.property.md) — The event’s input source.
- [modifierKeys](modifierkeys.md) — The set of active modifier keys at the time of this event.
