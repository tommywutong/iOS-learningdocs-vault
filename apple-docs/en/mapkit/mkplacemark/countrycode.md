---
title: countryCode
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（26.0 起废弃）, iPadOS 3.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, macOS 10.9+（26.0 起废弃）, tvOS 9.2+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）, watchOS 2.0+（26.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/mapkit/mkplacemark/countrycode
source_url: 'https://developer.apple.com/documentation/mapkit/mkplacemark/countrycode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkplacemark/countrycode.json'
content_hash: 'sha256:8d89a5f886b36ad7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPlacemark](../mkplacemark.md)

# countryCode

<sub>Instance Property</sub>

The abbreviated country or region name.

> [!warning] Deprecated
> Use MKMapItem's location, address and addressRepresentations properties instead. Use MKAddressRepresentations for formatted address strings for MapKit provided MKMapItems

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countryCode: String? { get }
```

## Discussion

This string is the standard abbreviation used to refer to the country or region. For example, if the placemark location was Apple’s headquarters, the value for this property would be the string “US”.
