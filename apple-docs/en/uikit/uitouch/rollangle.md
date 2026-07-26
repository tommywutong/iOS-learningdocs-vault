---
title: rollAngle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, visionOS 1.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/rollangle
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/rollangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/rollangle.json'
content_hash: 'sha256:b4185c6666bafc61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# rollAngle

<sub>Instance Property</sub>

A value that represents the current barrel-roll angle of Apple Pencil.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var rollAngle: CGFloat { get }
```

## Discussion

For models of Apple Pencil that don’t support barrel-roll angle data, the value of this property is `0`.

## See Also

### Getting touch attributes

- [tapCount](tapcount.md) — The number of times the finger was tapped for this given touch.
- [timestamp](timestamp.md) — The time when the touch occurred or when it was last mutated.
- [type](type.md) — The type of the touch.
- [TouchType](touchtype.md) — The type of touch received.
- [phase](phase-swift.property.md) — The phase of the touch.
- [Phase](phase-swift.enum.md) — The phase of a touch event.
- [force](force.md) — The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).
- [maximumPossibleForce](maximumpossibleforce.md) — The maximum possible force for a touch.
- [altitudeAngle](altitudeangle.md) — The altitude (in radians) of the stylus.
- [- azimuthAngleInView:](<azimuthangle(in_).md>) — Returns the azimuth angle (in radians) of the stylus.
- [- azimuthUnitVectorInView:](<azimuthunitvector(in_).md>) — Returns a unit vector that points in the direction of the azimuth of the stylus.
