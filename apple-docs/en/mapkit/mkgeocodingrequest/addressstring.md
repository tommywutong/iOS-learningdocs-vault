---
title: addressString
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkgeocodingrequest/addressstring
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeocodingrequest/addressstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeocodingrequest/addressstring.json'
content_hash: 'sha256:5c67e768a2ef3cf0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGeocodingRequest](../mkgeocodingrequest.md)

# addressString

<sub>Instance Property</sub>

The string used to initialize the geocoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var addressString: String { get }
```

## See Also

### Getting information about the geocoder

- [- getMapItemsWithCompletionHandler:](<getmapitems(completionhandler_).md>) — Returns the map items relevant to the geocoded location.
- [preferredLocale](preferredlocale.md) — A value that indicates the default locale the geocoder should use when processing requests.
- [region](region.md) — The geographic region for the framework to use as the bounds for the request; defaults to a region that covers the whole world.
