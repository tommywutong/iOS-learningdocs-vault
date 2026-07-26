---
title: CLLocationDirection
framework: Core Location
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationdirection
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationdirection.json'
content_hash: 'sha256:6ef665425cdb78d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationDirection

<sub>Type Alias</sub>

An azimuth that is measured in degrees relative to true north.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CLLocationDirection = Double
```

## Discussion

Direction values are measured in degrees starting at due north and continue clockwise around the compass. Thus, north is 0 degrees, east is 90 degrees, south is 180 degrees, and so on. A negative value indicates an invalid direction.

## See Also

### Getting speed and course information

- [speed](cllocation/speed.md) — The instantaneous speed of the device, measured in meters per second.
- [speedAccuracy](cllocation/speedaccuracy.md) — The accuracy of the speed value, measured in meters per second.
- [course](cllocation/course.md) — The direction in which the device is traveling, measured in degrees and relative to due north.
- [courseAccuracy](cllocation/courseaccuracy.md) — The accuracy of the course value, measured in degrees.
- [CLLocationSpeed](cllocationspeed.md) — The velocity (measured in meters per second) at which the device is moving.
- [CLLocationSpeedAccuracy](cllocationspeedaccuracy.md) — The accuracy of a speed.
- [CLLocationDirectionAccuracy](cllocationdirectionaccuracy.md) — The accuracy of a compass heading.
