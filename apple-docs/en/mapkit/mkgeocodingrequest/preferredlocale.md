---
title: preferredLocale
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgeocodingrequest/preferredlocale
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeocodingrequest/preferredlocale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeocodingrequest/preferredlocale.json'
content_hash: 'sha256:274a5b8adc79b395'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGeocodingRequest](../mkgeocodingrequest.md)

# preferredLocale

<sub>Instance Property</sub>

A value that indicates the default locale the geocoder should use when processing requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredLocale: Locale? { get set }
```

## See Also

### Getting information about the geocoder

- [addressString](addressstring.md) — The string used to initialize the geocoder.
- [- getMapItemsWithCompletionHandler:](<getmapitems(completionhandler_).md>) — Returns the map items relevant to the geocoded location.
- [region](region.md) — The geographic region for the framework to use as the bounds for the request; defaults to a region that covers the whole world.
