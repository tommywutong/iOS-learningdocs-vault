---
title: 'getMapItems(completionHandler:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkgeocodingrequest/getmapitems(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkgeocodingrequest/getmapitems(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkgeocodingrequest/getmapitems%28completionhandler%3A%29.json'
content_hash: 'sha256:371fda9b3798bcfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKGeocodingRequest](../mkgeocodingrequest.md)

# getMapItems(completionHandler:)

<sub>Instance Method</sub>

Returns the map items relevant to the geocoded location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getMapItems(completionHandler: @escaping @MainActor @Sendable ([MKMapItem]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mapItems: [MKMapItem] { get async throws }
```

## See Also

### Getting information about the geocoder

- [addressString](addressstring.md) — The string used to initialize the geocoder.
- [preferredLocale](preferredlocale.md) — A value that indicates the default locale the geocoder should use when processing requests.
- [region](region.md) — The geographic region for the framework to use as the bounds for the request; defaults to a region that covers the whole world.
