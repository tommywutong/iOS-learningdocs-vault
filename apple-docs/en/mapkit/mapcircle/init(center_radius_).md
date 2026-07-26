---
title: 'init(center:radius:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcircle/init(center:radius:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcircle/init(center:radius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcircle/init%28center%3Aradius%3A%29.json'
content_hash: 'sha256:e8e8480b0d6b6726'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCircle](../mapcircle.md)

# init(center:radius:)

<sub>Initializer</sub>

Creates a circle with the center coordinate and radius you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(center coordinate: CLLocationCoordinate2D, radius: CLLocationDistance)
```

## Parameters

- `coordinate` — The location of the center of the circle.

- `radius` — The radius of the circle, in meters.

## See Also

### Creating a map circle

- [init(_:)](<init(__).md>) — Creates a circle overlay from an existing map circle object.
- [init(mapRect:)](<init(maprect_).md>) — Creates the largest possible circle centered within the given map rectangle.
