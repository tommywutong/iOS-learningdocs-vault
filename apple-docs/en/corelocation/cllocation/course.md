---
title: course
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.2+, iPadOS 2.2+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocation/course
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/course'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/course.json'
content_hash: 'sha256:dd98e5cd228befea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# course

<sub>Instance Property</sub>

The direction in which the device is traveling, measured in degrees and relative to due north.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var course: CLLocationDirection { get }
```

## Discussion

Course values are measured in degrees starting at due north and continue clockwise around the compass. Thus, north is 0 degrees, east is 90 degrees, south is 180 degrees, and so on. Course values may not be available on all devices. A negative value indicates that the course information is invalid.

### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Getting speed and course information

- [speed](speed.md) — The instantaneous speed of the device, measured in meters per second.
- [speedAccuracy](speedaccuracy.md) — The accuracy of the speed value, measured in meters per second.
- [courseAccuracy](courseaccuracy.md) — The accuracy of the course value, measured in degrees.
- [CLLocationSpeed](../cllocationspeed.md) — The velocity (measured in meters per second) at which the device is moving.
- [CLLocationDirection](../cllocationdirection.md) — An azimuth that is measured in degrees relative to true north.
- [CLLocationSpeedAccuracy](../cllocationspeedaccuracy.md) — The accuracy of a speed.
- [CLLocationDirectionAccuracy](../cllocationdirectionaccuracy.md) — The accuracy of a compass heading.
