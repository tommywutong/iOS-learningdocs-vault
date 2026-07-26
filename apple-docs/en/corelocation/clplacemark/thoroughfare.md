---
title: thoroughfare
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clplacemark/thoroughfare
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark/thoroughfare'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark/thoroughfare.json'
content_hash: 'sha256:1281530245bf07f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLPlacemark](../clplacemark.md)

# thoroughfare

<sub>Instance Property</sub>

The street address associated with the placemark.

> [!warning] Deprecated
> Use either GeoToolbox.PlaceDescriptor or MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var thoroughfare: String? { get }
```

## Discussion

The street address contains the street name. For example, if the placemark location is Apple’s headquarters, the value for this property would be the string “Apple Park Way”.

## See Also

### Getting the placemark details

- [subThoroughfare](subthoroughfare.md) — Additional street-level information for the placemark. _(deprecated)_
- [locality](locality.md) — The city associated with the placemark. _(deprecated)_
- [subLocality](sublocality.md) — Additional city-level information for the placemark. _(deprecated)_
- [administrativeArea](administrativearea.md) — The state or province associated with the placemark. _(deprecated)_
- [subAdministrativeArea](subadministrativearea.md) — Additional administrative area information for the placemark. _(deprecated)_
- [postalCode](postalcode.md) — The postal code associated with the placemark. _(deprecated)_
