---
title: isCameraAssistanceEnabled
framework: Nearby Interaction
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/nearbyinteraction/ninearbypeerconfiguration/iscameraassistanceenabled
source_url: 'https://developer.apple.com/documentation/nearbyinteraction/ninearbypeerconfiguration/iscameraassistanceenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/nearbyinteraction/ninearbypeerconfiguration/iscameraassistanceenabled.json'
content_hash: 'sha256:4d7ba2fb1b9d7c91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Nearby Interaction](../../nearbyinteraction.md) · [NINearbyPeerConfiguration](../ninearbypeerconfiguration.md)

# isCameraAssistanceEnabled

<sub>Instance Property</sub>

A Boolean value that combines the spatial awareness of ARKit with Nearby Interaction to improve the accuracy of a nearby object’s position.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isCameraAssistanceEnabled: Bool { get set }
```

## Discussion

The default value is `false`.

When `true`, this property leverages [ARKit](../../arkit.md) to provide a nearby object’s [distance](../ninearbyobject/distance-9atp7.md) and [direction](../ninearbyobject/direction-4qh5w.md) in a wider range of environmental conditions.

By studying image captures from the device’s camera, ARKit creates an accurate world model of the user’s physical space. As the user moves, ARKit tracks the device with 6 degrees of freedom, by noting the device’s:

- 3D position `(x, y, z)`
- 3D orientation `(roll, pitch, yaw)`

Nearby Interaction adds readings from the device’s Ultra Wideband Chip to attain a robust position for a nearby object. This also enables the interaction session to provide an object’s [horizontalAngle](../ninearbyobject/horizontalangle-hsg.md) and [verticalDirectionEstimate](../ninearbyobject/verticaldirectionestimate-swift.property.md).
