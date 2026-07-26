---
title: UITouch.TouchType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/touchtype
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/touchtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/touchtype.json'
content_hash: 'sha256:bb4fcdf5ccbf6a20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# UITouch.TouchType

<sub>Enumeration</sub>

The type of touch received.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum TouchType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Touch types

- [UITouchTypeDirect](touchtype/direct.md) — A touch resulting from direct contact with the screen.
- [UITouchTypeIndirect](touchtype/indirect.md) — A touch that doesn’t result from contact with the screen.
- [UITouchTypePencil](touchtype/pencil.md) — A touch from Apple Pencil.
- [UITouchTypeIndirectPointer](touchtype/indirectpointer.md) — A touch resulting from a button-based, indirect input device that describes the input sequence from button press to button release.

### Deprecated

- [UITouchTypeStylus](touchtype/stylus.md) — A touch from a stylus. _(deprecated)_

### Initializers

- [init(rawValue:)](<touchtype/init(rawvalue_).md>)

## See Also

### Getting touch attributes

- [tapCount](tapcount.md) — The number of times the finger was tapped for this given touch.
- [timestamp](timestamp.md) — The time when the touch occurred or when it was last mutated.
- [type](type.md) — The type of the touch.
- [phase](phase-swift.property.md) — The phase of the touch.
- [Phase](phase-swift.enum.md) — The phase of a touch event.
- [force](force.md) — The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).
- [maximumPossibleForce](maximumpossibleforce.md) — The maximum possible force for a touch.
- [altitudeAngle](altitudeangle.md) — The altitude (in radians) of the stylus.
- [- azimuthAngleInView:](<azimuthangle(in_).md>) — Returns the azimuth angle (in radians) of the stylus.
- [- azimuthUnitVectorInView:](<azimuthunitvector(in_).md>) — Returns a unit vector that points in the direction of the azimuth of the stylus.
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
