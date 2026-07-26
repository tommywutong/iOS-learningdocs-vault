---
title: name
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitem/name
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/name.json'
content_hash: 'sha256:61d469b48ae8cfc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# name

<sub>Instance Property</sub>

The descriptive name associated with the map item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var name: String? { get set }
```

## Discussion

Use this property to specify the name associated with the location. For example, if there’s a business at the specified location, use this property to specify the name of the business.

If this map item represents the user’s location, the value in this property is a localized version of _Current Location_.

## See Also

### Accessing the map item attributes

- [Identifier](identifier-swift.class.md) — A unique identifier for a place.
- [alternateIdentifiers](alternateidentifiers.md) — A set of alternative identifiers for a place.
- [identifier](identifier-swift.property.md) — A unique identifier for a place.
- [isCurrentLocation](iscurrentlocation.md) — A Boolean value that indicates whether the map item represents the user’s location.
- [placemark](placemark.md) — The placemark object containing the location information. _(deprecated)_
- [pointOfInterestCategory](pointofinterestcategory.md) — The point-of-interest category for the map item.
- [phoneNumber](phonenumber.md) — The phone number associated with a business at the specified location.
- [timeZone](timezone.md) — The time zone of the specified location.
- [url](url.md) — The URL associated with the specified location.
