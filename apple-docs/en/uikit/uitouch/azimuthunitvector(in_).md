---
title: 'azimuthUnitVector(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitouch/azimuthunitvector(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/azimuthunitvector(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/azimuthunitvector%28in%3A%29.json'
content_hash: 'sha256:27bcaf0a5203b747'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# azimuthUnitVector(in:)

<sub>Instance Method</sub>

Returns a unit vector that points in the direction of the azimuth of the stylus.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func azimuthUnitVector(in view: UIView?) -> CGVector
```

## Parameters

- `view` — The view that contains the stylus’s touch. Pass `nil` to get the unit vector for the azimuth that is relative to the touch’s window.

## Return Value

The unit vector that points in the direction of the azimuth of the stylus.

## Discussion

It is less expensive to get the azimuth unit vector than the azimuth angle. If you’re creating transform matrices, the unit vector can also be more useful.

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
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
