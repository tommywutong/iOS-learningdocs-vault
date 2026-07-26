---
title: altitude
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.struct/altitude
source_url: 'https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.struct/altitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialeventcollection/event/inputdevicepose-swift.struct/altitude.json'
content_hash: 'sha256:efb0f437df4846e8'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftUI](../../../../swiftui.md) · [SpatialEventCollection](../../../spatialeventcollection.md) · [Event](../../event.md) · [InputDevicePose](../inputdevicepose-swift.struct.md)

# altitude

<sub>Instance Property</sub>

The altitude angle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var altitude: Angle
```

## Discussion

An angle of zero indicates that the device is parallel to the content, while 90 degrees indicates that it is normal to the content surface.

## See Also

### Getting the event type

- [azimuth](azimuth.md) — The azimuth angle.
- [pose3D](pose3d.md) — The 3D pose of the input device.
