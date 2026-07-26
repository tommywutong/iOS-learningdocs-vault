---
title: 'init(mapRect:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcircle/init(maprect:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcircle/init(maprect:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcircle/init%28maprect%3A%29.json'
content_hash: 'sha256:62355be26f8a3f4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapCircle](../mapcircle.md)

# init(mapRect:)

<sub>Initializer</sub>

Creates the largest possible circle centered within the given map rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(mapRect: MKMapRect)
```

## Parameters

- `mapRect` — The rectangle to center the circle within.

## See Also

### Creating a map circle

- [init(_:)](<init(__).md>) — Creates a circle overlay from an existing map circle object.
- [init(center:radius:)](<init(center_radius_).md>) — Creates a circle with the center coordinate and radius you specify.
