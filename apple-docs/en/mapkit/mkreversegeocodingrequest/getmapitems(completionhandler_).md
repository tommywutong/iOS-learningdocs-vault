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
doc_path: '/documentation/mapkit/mkreversegeocodingrequest/getmapitems(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocodingrequest/getmapitems(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocodingrequest/getmapitems%28completionhandler%3A%29.json'
content_hash: 'sha256:6d8405fec0f2c1ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocodingRequest](../mkreversegeocodingrequest.md)

# getMapItems(completionHandler:)

<sub>Instance Method</sub>

Returns the map items relevant to the reverse geocoded location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getMapItems(completionHandler: @escaping @MainActor @Sendable ([MKMapItem]?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mapItems: [MKMapItem] { get async throws }
```

## See Also

### Getting information about map items and the reverse geocoder’s locale’

- [preferredLocale](preferredlocale.md) — A value that indicates the preferred locale for the addresses the request returns, or `nil` if the framework should use the device locale.
