---
title: UITouch.Phase
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitouch/phase-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uitouch/phase-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitouch/phase-swift.enum.json'
content_hash: 'sha256:892b89c797eab3d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITouch](../uitouch.md)

# UITouch.Phase

<sub>Enumeration</sub>

The phase of a touch event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum Phase
```

## Overview

The phase of a `UITouch` instance changes as the system receives updates during the course of an event. Access this value through the [phase](phase-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UITouchPhaseBegan](phase-swift.enum/began.md) — A touch for a given event has pressed down on the screen.
- [UITouchPhaseMoved](phase-swift.enum/moved.md) — A touch for a given event has moved over the screen.
- [UITouchPhaseStationary](phase-swift.enum/stationary.md) — A touch for a given event is pressed down on the screen, but hasn’t moved since the previous event.
- [UITouchPhaseEnded](phase-swift.enum/ended.md) — A touch for a given event has lifted from the screen.
- [UITouchPhaseCancelled](phase-swift.enum/cancelled.md) — The system canceled tracking for a touch, for example, when the user moves the device against their face.
- [UITouchPhaseRegionEntered](phase-swift.enum/regionentered.md) — A touch for a given event has entered a window on the screen.
- [UITouchPhaseRegionMoved](phase-swift.enum/regionmoved.md) — A touch for the given event is within a window on the screen, but has not yet pressed down.
- [UITouchPhaseRegionExited](phase-swift.enum/regionexited.md) — A touch for a given event has left a window on the screen.

### Initializers

- [init(rawValue:)](<phase-swift.enum/init(rawvalue_).md>)

## See Also

### Getting touch attributes

- [tapCount](tapcount.md) — The number of times the finger was tapped for this given touch.
- [timestamp](timestamp.md) — The time when the touch occurred or when it was last mutated.
- [type](type.md) — The type of the touch.
- [TouchType](touchtype.md) — The type of touch received.
- [phase](phase-swift.property.md) — The phase of the touch.
- [force](force.md) — The force of the touch, where a value of `1.0` represents the force of an average touch (predetermined by the system, not user-specific).
- [maximumPossibleForce](maximumpossibleforce.md) — The maximum possible force for a touch.
- [altitudeAngle](altitudeangle.md) — The altitude (in radians) of the stylus.
- [- azimuthAngleInView:](<azimuthangle(in_).md>) — Returns the azimuth angle (in radians) of the stylus.
- [- azimuthUnitVectorInView:](<azimuthunitvector(in_).md>) — Returns a unit vector that points in the direction of the azimuth of the stylus.
- [rollAngle](rollangle.md) — A value that represents the current barrel-roll angle of Apple Pencil.
