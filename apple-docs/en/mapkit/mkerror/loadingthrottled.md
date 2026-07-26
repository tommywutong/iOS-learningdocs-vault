---
title: loadingThrottled
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkerror/loadingthrottled
source_url: 'https://developer.apple.com/documentation/mapkit/mkerror/loadingthrottled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkerror/loadingthrottled.json'
content_hash: 'sha256:4e2b9fca403f2220'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKError](../mkerror.md)

# loadingThrottled

<sub>Type Property</sub>

The data didn’t load because data throttling is in effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var loadingThrottled: MKError.Code { get }
```

## Discussion

This error can occur if an app makes frequent requests for data over a short period of time.

## See Also

### Error codes

- [decodingFailed](decodingfailed.md) — GeoJSON decoding failed.
- [directionsNotFound](directionsnotfound.md) — Directions to the specified location aren’t available.
- [placemarkNotFound](placemarknotfound.md) — The framework couldn’t find the specified placemark.
- [serverFailure](serverfailure.md) — The map server was unable to return the desired information.
- [unknown](unknown.md) — An unknown error occurred.
- [Code](code.md) — Error constants for the MapKit framework.
