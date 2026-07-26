---
title: SpatialEventCollection.Event.InputDevicePose
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.struct
source_url: 'https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.struct.json'
content_hash: 'sha256:55363be7c25aed65'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SpatialEventCollection](../../spatialeventcollection.md) · [Event](../event.md)

# SpatialEventCollection.Event.InputDevicePose

<sub>Structure</sub>

A pose describing the input device like a hand controlling the event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct InputDevicePose
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md)

## Topics

### Getting the event type

- [altitude](inputdevicepose-swift.struct/altitude.md) — The altitude angle.
- [azimuth](inputdevicepose-swift.struct/azimuth.md) — The azimuth angle.
- [pose3D](inputdevicepose-swift.struct/pose3d.md) — The 3D pose of the input device.

## See Also

### Locating the event

- [location](location.md) — The 2D location of the event.
- [location3D](location3d.md) — The 3D location of the touch.
- [selectionRay](selectionray.md) — The 3D ray used to target the touch.
- [inputDevicePose](inputdevicepose-swift.property.md) — The 3D position and orientation of the device controlling the touch, if one exists.
- [targetedEntity](targetedentity.md) — The entity target for this touch, if one exists.
