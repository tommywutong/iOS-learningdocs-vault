---
title: regionCode
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mkaddressrepresentations/regioncode
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/regioncode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressrepresentations/regioncode.json'
content_hash: 'sha256:e84bcbf3cc14d780'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAddressRepresentations](../mkaddressrepresentations.md)

# regionCode

<sub>Instance Property</sub>

The region’s ISO 3166-2 region code, such as “US”.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, readonly, nullable) NSString * regionCode;
```

## See Also

### Getting parts of an address

- [cityName](cityname.md) — The name of the city.
- [cityWithContext](citywithcontext.md) — The city name along with the country name, to provide additional disambiguating context.
- [regionName](regionname.md) — The region name, such as “United States”.
