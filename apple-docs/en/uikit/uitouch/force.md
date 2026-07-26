---
title: force
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/force
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/force'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/force.json'
content_hash: 'sha256:d417a87fe64043ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# force

<sub>Instance Property</sub>

The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var force: CGFloat { get }
```

## Discussion

This property is available on devices that support 3D Touch or Apple Pencil. To check at runtime if a device supports 3D Touch, read the value of the [forceTouchCapability](../uitraitcollection/forcetouchcapability.md) property on the trait collection for any object in your app with a trait environment.

The force reported by Apple Pencil is measured along the axis of the pencil. If you want a force perpendicular to the device, you need to calculate this value using the [altitudeAngle](altitudeangle.md) value.

The force reported by Apple Pencil is estimated at first, and may not always be updated. To determine if an update is expected, consult [estimatedPropertiesExpectingUpdates](estimatedpropertiesexpectingupdates.md) and look for a [UITouchPropertyForce](properties/force.md) flag. In this scenario, [estimationUpdateIndex](estimationupdateindex.md) contains a non-nil value, which you can correlate with the original touch when the update occurs. When there are no expected force updates, the entire touch sequence usually won’t have updates, so it may be appropriate to apply a custom, tool-specific force curve to the touch sequence.

## See Also

### Getting touch attributes

- [tapCount](tapcount.md) — The number of times the finger was tapped for this given touch.
- [timestamp](timestamp.md) — The time when the touch occurred or when it was last mutated.
- [type](type.md) — The type of the touch.
- [TouchType](touchtype.md) — The type of touch received.
- [phase](phase-swift.property.md) — The phase of the touch.
- [Phase](phase-swift.enum.md) — The phase of a touch event.
- [maximumPossibleForce](maximumpossibleforce.md) — The maximum possible force for a touch.
- [altitudeAngle](altitudeangle.md) — The altitude (in radians) of the stylus.
- [- azimuthAngleInView:](<azimuthangle(in_).md>) — Returns the azimuth angle (in radians) of the stylus.
- [- azimuthUnitVectorInView:](<azimuthunitvector(in_).md>) — Returns a unit vector that points in the direction of the azimuth of the stylus.
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
