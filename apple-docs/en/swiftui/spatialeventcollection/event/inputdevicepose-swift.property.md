---
title: inputDevicePose
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.property.json'
content_hash: 'sha256:5e1a629f07e39158'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SpatialEventCollection](../../spatialeventcollection.md) · [Event](../event.md)

# inputDevicePose

<sub>Instance Property</sub>

The 3D position and orientation of the device controlling the touch, if one exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var inputDevicePose: SpatialEventCollection.Event.InputDevicePose? { get set }
```

## See Also

### Locating the event

- [location](location.md) — The 2D location of the event.
- [location3D](location3d.md) — The 3D location of the touch.
- [selectionRay](selectionray.md) — The 3D ray used to target the touch.
- [InputDevicePose](inputdevicepose-swift.struct.md) — A pose describing the input device like a hand controlling the event.
- [targetedEntity](targetedentity.md) — The entity target for this touch, if one exists.
