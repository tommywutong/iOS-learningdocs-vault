---
title: pointOfInterestCategory
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkmapitem/pointofinterestcategory
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/pointofinterestcategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/pointofinterestcategory.json'
content_hash: 'sha256:9f2e0a9fe072cbb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# pointOfInterestCategory

<sub>Instance Property</sub>

The point-of-interest category for the map item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pointOfInterestCategory: MKPointOfInterestCategory? { get set }
```

## Discussion

If the map item doesn’t correspond to a point of interest, or if the point of interest isn’t one of the known values in [MKPointOfInterestCategory](../mkpointofinterestcategory.md), [pointOfInterestCategory](pointofinterestcategory.md) is `nil`.

## See Also

### Accessing the map item attributes

- [Identifier](identifier-swift.class.md) — A unique identifier for a place.
- [alternateIdentifiers](alternateidentifiers.md) — A set of alternative identifiers for a place.
- [identifier](identifier-swift.property.md) — A unique identifier for a place.
- [isCurrentLocation](iscurrentlocation.md) — A Boolean value that indicates whether the map item represents the user’s location.
- [name](name.md) — The descriptive name associated with the map item.
- [placemark](placemark.md) — The placemark object containing the location information. _(deprecated)_
- [phoneNumber](phonenumber.md) — The phone number associated with a business at the specified location.
- [timeZone](timezone.md) — The time zone of the specified location.
- [url](url.md) — The URL associated with the specified location.
