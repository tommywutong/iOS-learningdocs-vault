---
title: phoneNumber
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitem/phonenumber
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/phonenumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/phonenumber.json'
content_hash: 'sha256:458dcf930578b75a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# phoneNumber

<sub>Instance Property</sub>

The phone number associated with a business at the specified location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var phoneNumber: String? { get set }
```

## Discussion

If there’s a relevant phone number associated with the location, such as for a business at the location, use this property to specify that value.

## See Also

### Accessing the map item attributes

- [Identifier](identifier-swift.class.md) — A unique identifier for a place.
- [alternateIdentifiers](alternateidentifiers.md) — A set of alternative identifiers for a place.
- [identifier](identifier-swift.property.md) — A unique identifier for a place.
- [isCurrentLocation](iscurrentlocation.md) — A Boolean value that indicates whether the map item represents the user’s location.
- [name](name.md) — The descriptive name associated with the map item.
- [placemark](placemark.md) — The placemark object containing the location information. _(deprecated)_
- [pointOfInterestCategory](pointofinterestcategory.md) — The point-of-interest category for the map item.
- [timeZone](timezone.md) — The time zone of the specified location.
- [url](url.md) — The URL associated with the specified location.
