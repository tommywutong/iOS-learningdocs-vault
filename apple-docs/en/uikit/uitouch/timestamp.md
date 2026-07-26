---
title: timestamp
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/timestamp
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/timestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/timestamp.json'
content_hash: 'sha256:7013c568696a0640'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# timestamp

<sub>Instance Property</sub>

The time when the touch occurred or when it was last mutated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var timestamp: TimeInterval { get }
```

## Discussion

The value of this property is the time, in seconds since system startup, that the touch originated or was last changed. You can store the value of this property and compare it to the timestamp in subsequent [UITouch](../uitouch.md) objects to determine the duration of the touch and, if it is being swiped, the speed of movement. For a definition of the time since system startup, see the description of the [systemUptime](../../foundation/processinfo/systemuptime.md) method of the [ProcessInfo](../../foundation/processinfo.md) class.

## See Also

### Getting touch attributes

- [tapCount](tapcount.md) — The number of times the finger was tapped for this given touch.
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
