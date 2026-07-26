---
title: cityWithContext
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkaddressrepresentations/citywithcontext
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/citywithcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressrepresentations/citywithcontext.json'
content_hash: 'sha256:fa683786bb338a9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAddressRepresentations](../mkaddressrepresentations.md)

# cityWithContext

<sub>Instance Property</sub>

The city name along with the country name, to provide additional disambiguating context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var cityWithContext: String? { get }
```

## Discussion

This returns the same value as `cityWithContext(.automatic)`.

## See Also

### Getting parts of an address

- [cityName](cityname.md) — The name of the city.
- [regionName](regionname.md) — The region name, such as “United States”.
- [region](region.md)
