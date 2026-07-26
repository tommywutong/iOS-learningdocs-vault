---
title: alternateIdentifiers
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitem/alternateidentifiers
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/alternateidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/alternateidentifiers.json'
content_hash: 'sha256:4e93c6928781dd74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# alternateIdentifiers

<sub>Instance Property</sub>

A set of alternative identifiers for a place.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var alternateIdentifiers: Set<MKMapItem.Identifier> { get }
```

## Discussion

The identifier for a point of interest may change over time. This property provides a set of alternative identifiers for this map item.

## See Also

### Accessing the map item attributes

- [Identifier](identifier-swift.class.md) — A unique identifier for a place.
- [identifier](identifier-swift.property.md) — A unique identifier for a place.
- [isCurrentLocation](iscurrentlocation.md) — A Boolean value that indicates whether the map item represents the user’s location.
- [name](name.md) — The descriptive name associated with the map item.
- [placemark](placemark.md) — The placemark object containing the location information. _(deprecated)_
- [pointOfInterestCategory](pointofinterestcategory.md) — The point-of-interest category for the map item.
- [phoneNumber](phonenumber.md) — The phone number associated with a business at the specified location.
- [timeZone](timezone.md) — The time zone of the specified location.
- [url](url.md) — The URL associated with the specified location.
