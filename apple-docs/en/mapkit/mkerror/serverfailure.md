---
title: serverFailure
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkerror/serverfailure
source_url: 'https://developer.apple.com/documentation/mapkit/mkerror/serverfailure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkerror/serverfailure.json'
content_hash: 'sha256:7f6597e83babe27c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKError](../mkerror.md)

# serverFailure

<sub>Type Property</sub>

The map server was unable to return the desired information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var serverFailure: MKError.Code { get }
```

## See Also

### Error codes

- [decodingFailed](decodingfailed.md) — GeoJSON decoding failed.
- [directionsNotFound](directionsnotfound.md) — Directions to the specified location aren’t available.
- [loadingThrottled](loadingthrottled.md) — The data didn’t load because data throttling is in effect.
- [placemarkNotFound](placemarknotfound.md) — The framework couldn’t find the specified placemark.
- [unknown](unknown.md) — An unknown error occurred.
- [Code](code.md) — Error constants for the MapKit framework.
