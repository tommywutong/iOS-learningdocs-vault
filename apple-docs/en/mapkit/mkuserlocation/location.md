---
title: location
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkuserlocation/location
source_url: 'https://developer.apple.com/documentation/mapkit/mkuserlocation/location'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkuserlocation/location.json'
content_hash: 'sha256:424453d31b2a3811'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKUserLocation](../mkuserlocation.md)

# location

<sub>Instance Property</sub>

The location of the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var location: CLLocation? { get }
```

## Discussion

This property contains `nil` if the map view isn’t showing the user’s location, or if the map view is still determining the user’s location.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Determining the user’s location

- [updating](isupdating.md) — A Boolean value that indicates whether the map view is updating the user’s location.
- [heading](heading.md) — The heading of the user’s location.
