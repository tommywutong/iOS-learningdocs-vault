---
title: location
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkreversegeocodingrequest/location
source_url: 'https://developer.apple.com/documentation/mapkit/mkreversegeocodingrequest/location'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkreversegeocodingrequest/location.json'
content_hash: 'sha256:ac5cabaa89774fbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKReverseGeocodingRequest](../mkreversegeocodingrequest.md)

# location

<sub>Instance Property</sub>

The location provided to the initializer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var location: CLLocation { get }
```

## See Also

### Getting the reverse geocoder’s state

- [loading](isloading.md) — A Boolean value that indicates whether the current reverse geocoding request is in a loading state.
- [cancelled](iscancelled.md) — A Boolean value that indicates whether the current reverse geocoding request is in a cancelled state.
