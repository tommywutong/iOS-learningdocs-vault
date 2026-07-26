---
title: subThoroughfare
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clplacemark/subthoroughfare
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark/subthoroughfare'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark/subthoroughfare.json'
content_hash: 'sha256:4a014027c8cf8ad3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLPlacemark](../clplacemark.md)

# subThoroughfare

<sub>Instance Property</sub>

Additional street-level information for the placemark.

> [!warning] Deprecated
> Use either GeoToolbox.PlaceDescriptor or MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var subThoroughfare: String? { get }
```

## Discussion

Subthroughfares provide information such as the street number for the location. For example, if the placemark location is Apple’s headquarters (1 Apple Park Way), the value for this property would be the string “1”.

## See Also

### Getting the placemark details

- [thoroughfare](thoroughfare.md) — The street address associated with the placemark. _(deprecated)_
- [locality](locality.md) — The city associated with the placemark. _(deprecated)_
- [subLocality](sublocality.md) — Additional city-level information for the placemark. _(deprecated)_
- [administrativeArea](administrativearea.md) — The state or province associated with the placemark. _(deprecated)_
- [subAdministrativeArea](subadministrativearea.md) — Additional administrative area information for the placemark. _(deprecated)_
- [postalCode](postalcode.md) — The postal code associated with the placemark. _(deprecated)_
