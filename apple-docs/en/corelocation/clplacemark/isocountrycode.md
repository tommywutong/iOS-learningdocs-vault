---
title: isoCountryCode
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clplacemark/isocountrycode
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark/isocountrycode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark/isocountrycode.json'
content_hash: 'sha256:b2e4fab1f1ade9cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLPlacemark](../clplacemark.md)

# isoCountryCode

<sub>Instance Property</sub>

The abbreviated country or region name.

> [!warning] Deprecated
> Use either GeoToolbox.PlaceDescriptor or MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isoCountryCode: String? { get }
```

## Discussion

This string is the standard abbreviation used to refer to the country or region. For example, if the placemark location is Apple’s headquarters, the value for this property would be the string “US”.

## See Also

### Getting the placemark’s country

- [country](country.md) — The name of the country or region associated with the placemark. _(deprecated)_
