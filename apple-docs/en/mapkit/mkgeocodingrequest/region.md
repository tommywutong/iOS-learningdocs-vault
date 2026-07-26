---
title: region
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgeocodingrequest/region
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeocodingrequest/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeocodingrequest/region.json'
content_hash: 'sha256:c226561dcd39de12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGeocodingRequest](../mkgeocodingrequest.md)

# region

<sub>Instance Property</sub>

The geographic region for the framework to use as the bounds for the request; defaults to a region that covers the whole world.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var region: MKCoordinateRegion { get set }
```

## See Also

### Getting information about the geocoder

- [addressString](addressstring.md) — The string used to initialize the geocoder.
- [- getMapItemsWithCompletionHandler:](<getmapitems(completionhandler_).md>) — Returns the map items relevant to the geocoded location.
- [preferredLocale](preferredlocale.md) — A value that indicates the default locale the geocoder should use when processing requests.
