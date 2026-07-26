---
title: maximumPossibleForce
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/maximumpossibleforce
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/maximumpossibleforce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/maximumpossibleforce.json'
content_hash: 'sha256:5191b77b5405accb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# maximumPossibleForce

<sub>Instance Property</sub>

The maximum possible force for a touch.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var maximumPossibleForce: CGFloat { get }
```

## Discussion

The value of this property is sufficiently high to provide a wide dynamic range for values of the [force](force.md) property.

This property is available on devices that support 3D Touch or Apple Pencil. To check at runtime if a device supports 3D Touch, read the value of the [forceTouchCapability](../uitraitcollection/forcetouchcapability.md) property on the trait collection for any object in your app with a trait environment.

## See Also

### Getting touch attributes

- [tapCount](tapcount.md) — The number of times the finger was tapped for this given touch.
- [timestamp](timestamp.md) — The time when the touch occurred or when it was last mutated.
- [type](type.md) — The type of the touch.
- [TouchType](touchtype.md) — The type of touch received.
- [phase](phase-swift.property.md) — The phase of the touch.
- [Phase](phase-swift.enum.md) — The phase of a touch event.
- [force](force.md) — The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).
- [altitudeAngle](altitudeangle.md) — The altitude (in radians) of the stylus.
- [- azimuthAngleInView:](<azimuthangle(in_).md>) — Returns the azimuth angle (in radians) of the stylus.
- [- azimuthUnitVectorInView:](<azimuthunitvector(in_).md>) — Returns a unit vector that points in the direction of the azimuth of the stylus.
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
