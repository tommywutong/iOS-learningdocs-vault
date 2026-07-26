---
title: 'cityWithContext(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkaddressrepresentations/citywithcontext(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressrepresentations/citywithcontext(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressrepresentations/citywithcontext%28_%3A%29.json'
content_hash: 'sha256:0fde8b34ad1b3600'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAddressRepresentations](../mkaddressrepresentations.md)

# cityWithContext(_:)

<sub>Instance Method</sub>

The city name and, optionally and if applicable, state and region to provide additional disambiguating context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cityWithContext(_ style: MKAddressRepresentations.ContextStyle) -> String?
```

## Parameters

- `style` — The [ContextStyle](contextstyle.md) to apply.

## See Also

### Getting a full address and city name

- [- fullAddressIncludingRegion:singleLine:](<fulladdress(includingregion_singleline_).md>) — Returns the the location’s full address, optionally including the country or on a single link without line breaks.
