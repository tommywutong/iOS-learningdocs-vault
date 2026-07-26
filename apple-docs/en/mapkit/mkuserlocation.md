---
title: MKUserLocation
framework: MapKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkuserlocation
source_url: 'https://developer.apple.com/documentation/mapkit/mkuserlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkuserlocation.json'
content_hash: 'sha256:1f3f0247d5eff3d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# MKUserLocation

<sub>Class</sub>

An annotation that reflects the user’s location on the map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MKUserLocation
```

## Overview

You don’t create instances of this class directly. Instead, you retrieve an existing `MKUserLocation` object from the [userLocation](mkmapview/userlocation.md) property of the map view that displays in your app.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [MKAnnotation](mkannotation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Determining the user’s location

- [location](mkuserlocation/location.md) — The location of the device.
- [updating](mkuserlocation/isupdating.md) — A Boolean value that indicates whether the map view is updating the user’s location.
- [heading](mkuserlocation/heading.md) — The heading of the user’s location.

### Accessing the user’s location annotation

- [title](mkuserlocation/title.md) — The title to display for the user’s location annotation.
- [subtitle](mkuserlocation/subtitle.md) — The subtitle to display for the user’s location annotation.

## See Also

### User location

- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md) — Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [MKUserLocationView](mkuserlocationview.md) — A configurable annotation that shows the user’s location using the default MapKit style.
