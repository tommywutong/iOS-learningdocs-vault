---
title: 'fullAddress(includingRegion:singleLine:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkaddressrepresentations/fulladdress(includingregion:singleline:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/fulladdress(includingregion:singleline:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressrepresentations/fulladdress%28includingregion%3Asingleline%3A%29.json'
content_hash: 'sha256:2a0e438391347106'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAddressRepresentations](../mkaddressrepresentations.md)

# fullAddress(includingRegion:singleLine:)

<sub>Instance Method</sub>

Returns the the location’s full address, optionally including the country or on a single link without line breaks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fullAddress(includingRegion: Bool, singleLine: Bool) -> String?
```

## Parameters

- `includingRegion` — A Boolean value that indicates whether the address should include the region name.

- `singleLine` — A Boolean value that indicates whether the framework should format the address as a single line.

## See Also

### Getting a full address and city name

- [- cityWithContextUsingStyle:](<citywithcontext(__).md>) — The city name and, optionally and if applicable, state and region to provide additional disambiguating context.
