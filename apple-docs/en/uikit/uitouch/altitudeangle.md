---
title: altitudeAngle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/altitudeangle
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/altitudeangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/altitudeangle.json'
content_hash: 'sha256:f97758cd55b7fb88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# altitudeAngle

<sub>Instance Property</sub>

The altitude (in radians) of the stylus.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var altitudeAngle: CGFloat { get }
```

## Discussion

A value of `0` radians indicates that the stylus is parallel to the surface. The value of this property is `Pi/2` when the stylus is perpendicular to the surface.

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
- [- azimuthAngleInView:](<azimuthangle(in_).md>) — Returns the azimuth angle (in radians) of the stylus.
- [- azimuthUnitVectorInView:](<azimuthunitvector(in_).md>) — Returns a unit vector that points in the direction of the azimuth of the stylus.
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
