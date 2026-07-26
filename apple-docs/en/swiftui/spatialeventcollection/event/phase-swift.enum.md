---
title: SpatialEventCollection.Event.Phase
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialeventcollection/event/phase-swift.enum
source_url: 'https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/phase-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialeventcollection/event/phase-swift.enum.json'
content_hash: 'sha256:da4b8cd93660f0b7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SpatialEventCollection](../../spatialeventcollection.md) · [Event](../event.md)

# SpatialEventCollection.Event.Phase

<sub>Enumeration</sub>

The states that an event can have.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
enum Phase
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md)

## Topics

### Getting the phase

- [SpatialEventCollection.Event.Phase.active](phase-swift.enum/active.md) — The phase is active and the state associated with it is guaranteed to produce at least one more update.
- [SpatialEventCollection.Event.Phase.cancelled](phase-swift.enum/cancelled.md) — The state associated with this phase was canceled and won’t produce any more updates.
- [SpatialEventCollection.Event.Phase.ended](phase-swift.enum/ended.md) — The state associated with this phase ended normally and won’t produce any more updates.

## See Also

### Getting the event’s current phase

- [phase](phase-swift.property.md) — The phase of the event.
