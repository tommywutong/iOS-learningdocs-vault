---
title: speed
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.2+, iPadOS 2.2+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocation/speed
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/speed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/speed.json'
content_hash: 'sha256:5b376914787b30cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# speed

<sub>Instance Property</sub>

The instantaneous speed of the device, measured in meters per second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var speed: CLLocationSpeed { get }
```

## Discussion

This value reflects the instantaneous speed of the device as it moves in the direction of its current heading. A negative value indicates an invalid speed. Because the actual speed can change many times between the delivery of location events, use this property for informational purposes only.

### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Getting speed and course information

- [speedAccuracy](speedaccuracy.md) — The accuracy of the speed value, measured in meters per second.
- [course](course.md) — The direction in which the device is traveling, measured in degrees and relative to due north.
- [courseAccuracy](courseaccuracy.md) — The accuracy of the course value, measured in degrees.
- [CLLocationSpeed](../cllocationspeed.md) — The velocity (measured in meters per second) at which the device is moving.
- [CLLocationDirection](../cllocationdirection.md) — An azimuth that is measured in degrees relative to true north.
- [CLLocationSpeedAccuracy](../cllocationspeedaccuracy.md) — The accuracy of a speed.
- [CLLocationDirectionAccuracy](../cllocationdirectionaccuracy.md) — The accuracy of a compass heading.
