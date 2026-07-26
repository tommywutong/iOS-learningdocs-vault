---
title: courseAccuracy
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 13.4+, visionOS 1.0+, watchOS 6.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocation/courseaccuracy
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/courseaccuracy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/courseaccuracy.json'
content_hash: 'sha256:fab123f49b511d7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# courseAccuracy

<sub>Instance Property</sub>

The accuracy of the course value, measured in degrees.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var courseAccuracy: CLLocationDirectionAccuracy { get }
```

## Discussion

When this property contains `0` or a positive number, the value in the course property is plus or minus the specified number degrees, modulo 360. When this property contains a negative number, the value in the course property is invalid.

## See Also

### Getting speed and course information

- [speed](speed.md) — The instantaneous speed of the device, measured in meters per second.
- [speedAccuracy](speedaccuracy.md) — The accuracy of the speed value, measured in meters per second.
- [course](course.md) — The direction in which the device is traveling, measured in degrees and relative to due north.
- [CLLocationSpeed](../cllocationspeed.md) — The velocity (measured in meters per second) at which the device is moving.
- [CLLocationDirection](../cllocationdirection.md) — An azimuth that is measured in degrees relative to true north.
- [CLLocationSpeedAccuracy](../cllocationspeedaccuracy.md) — The accuracy of a speed.
- [CLLocationDirectionAccuracy](../cllocationdirectionaccuracy.md) — The accuracy of a compass heading.
