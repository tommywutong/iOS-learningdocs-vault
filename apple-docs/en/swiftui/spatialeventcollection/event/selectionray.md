---
title: selectionRay
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialeventcollection/event/selectionray
source_url: 'https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/selectionray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialeventcollection/event/selectionray.json'
content_hash: 'sha256:9b7f5105f3a8b483'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SpatialEventCollection](../../spatialeventcollection.md) · [Event](../event.md)

# selectionRay

<sub>Instance Property</sub>

The 3D ray used to target the touch.

<sub>macOS, visionOS</sub>

```swift
var selectionRay: Ray3D?
```

## See Also

### Locating the event

- [location](location.md) — The 2D location of the event.
- [location3D](location3d.md) — The 3D location of the touch.
- [inputDevicePose](inputdevicepose-swift.property.md) — The 3D position and orientation of the device controlling the touch, if one exists.
- [InputDevicePose](inputdevicepose-swift.struct.md) — A pose describing the input device like a hand controlling the event.
- [targetedEntity](targetedentity.md) — The entity target for this touch, if one exists.
