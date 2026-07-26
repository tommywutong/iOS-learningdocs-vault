---
title: placemark
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（26.0 起废弃）, iPadOS 6.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.9+（26.0 起废弃）, tvOS 9.2+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkmapitem/placemark
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitem/placemark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitem/placemark.json'
content_hash: 'sha256:11919be426a63d1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItem](../mkmapitem.md)

# placemark

<sub>Instance Property</sub>

The placemark object containing the location information.

> [!warning] Deprecated
> Use location, address and addressRepresentations instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var placemark: MKPlacemark { get }
```

## Discussion

If you create the map item using the [+ mapItemForCurrentLocation](<forcurrentlocation().md>) method, the value of this property is `nil` and the [isCurrentLocation](iscurrentlocation.md) property is [true](../../swift/true.md).

## See Also

### Accessing the map item attributes

- [Identifier](identifier-swift.class.md) — A unique identifier for a place.
- [alternateIdentifiers](alternateidentifiers.md) — A set of alternative identifiers for a place.
- [identifier](identifier-swift.property.md) — A unique identifier for a place.
- [isCurrentLocation](iscurrentlocation.md) — A Boolean value that indicates whether the map item represents the user’s location.
- [name](name.md) — The descriptive name associated with the map item.
- [pointOfInterestCategory](pointofinterestcategory.md) — The point-of-interest category for the map item.
- [phoneNumber](phonenumber.md) — The phone number associated with a business at the specified location.
- [timeZone](timezone.md) — The time zone of the specified location.
- [url](url.md) — The URL associated with the specified location.
