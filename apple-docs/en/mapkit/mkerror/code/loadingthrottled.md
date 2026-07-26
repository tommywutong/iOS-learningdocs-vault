---
title: MKError.Code.loadingThrottled
framework: MapKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkerror/code/loadingthrottled
source_url: 'https://developer.apple.com/documentation/mapkit/mkerror/code/loadingthrottled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkerror/code/loadingthrottled.json'
content_hash: 'sha256:12c2b6cf0c73c620'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [MapKit](../../../mapkit.md) · [MKError](../../mkerror.md) · [Code](../code.md)

# MKError.Code.loadingThrottled

<sub>Case</sub>

The data didn’t load because data throttling is in effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case loadingThrottled
```

## Discussion

This error can occur if an app makes frequent requests for data over a short period of time.

## See Also

### Constants

- [MKErrorDecodingFailed](decodingfailed.md) — GeoJSON decoding failed.
- [MKErrorDirectionsNotFound](directionsnotfound.md) — The framework couldn’t find the specified directions.
- [MKErrorPlacemarkNotFound](placemarknotfound.md) — The specified placemark could not be found.
- [MKErrorServerFailure](serverfailure.md) — The map server was unable to return the desired information.
- [MKErrorUnknown](unknown.md) — An unknown error occurred.
