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
doc_path: /documentation/mapkit/mkreversegeocodingrequest/preferredlocale
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocodingrequest/preferredlocale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocodingrequest/preferredlocale.json'
content_hash: 'sha256:c6b5e677af26d472'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocodingRequest](../mkreversegeocodingrequest.md)

# preferredLocale

<sub>Instance Property</sub>

A value that indicates the preferred locale for the addresses the request returns, or `nil` if the framework should use the device locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredLocale: Locale? { get set }
```

## See Also

### Getting information about map items and the reverse geocoder’s locale’

- [- getMapItemsWithCompletionHandler:](<getmapitems(completionhandler_).md>) — Returns the map items relevant to the reverse geocoded location.
