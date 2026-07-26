---
title: SpatialEventCollection.Event.Phase.ended
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialeventcollection/event/phase-swift.enum/ended
source_url: 'https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/phase-swift.enum/ended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialeventcollection/event/phase-swift.enum/ended.json'
content_hash: 'sha256:e17a91f74439ce22'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftUI](../../../../swiftui.md) · [SpatialEventCollection](../../../spatialeventcollection.md) · [Event](../../event.md) · [Phase](../phase-swift.enum.md)

# SpatialEventCollection.Event.Phase.ended

<sub>Case</sub>

The state associated with this phase ended normally and won’t produce any more updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
case ended
```

## See Also

### Getting the phase

- [SpatialEventCollection.Event.Phase.active](active.md) — The phase is active and the state associated with it is guaranteed to produce at least one more update.
- [SpatialEventCollection.Event.Phase.cancelled](cancelled.md) — The state associated with this phase was canceled and won’t produce any more updates.
