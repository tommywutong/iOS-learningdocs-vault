---
title: 'init(center:radius:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkcircle/init(center:radius:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkcircle/init(center:radius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkcircle/init%28center%3Aradius%3A%29.json'
content_hash: 'sha256:b8aec90ca96b8f5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKCircle](../mkcircle.md)

# init(center:radius:)

<sub>Initializer</sub>

Creates and returns a circle object using the specified coordinate and radius.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(center coord: CLLocationCoordinate2D, radius: CLLocationDistance)
```

## Parameters

- `coord` — The center point of the circle, specified as a latitude and longitude value.

- `radius` — The radius of the circle, measured in meters from the center point.

## Return Value

A circle overlay object.

## See Also

### Related Documentation

- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)

### Creating a circle overlay

- [+ circleWithMapRect:](<init(maprect_).md>) — Creates and returns a circle object that derives the circular area from the specified rectangle.
