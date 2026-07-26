---
title: tapCount
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/tapcount
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/tapcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/tapcount.json'
content_hash: 'sha256:9dea4af9ae208a24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# tapCount

<sub>Instance Property</sub>

The number of times the finger was tapped for this given touch.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tapCount: Int { get }
```

## Discussion

The value of this property is an integer containing the number of taps that occurred for this touch within a predefined period of time. Use this property to evaluate whether the user single-tapped, double-tapped, or even triple-tapped a particular view or window.

## See Also

### Getting touch attributes

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
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
