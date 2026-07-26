---
title: region
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clplacemark/region
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark/region'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark/region.json'
content_hash: 'sha256:c91c9fd56e6515a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLPlacemark](../clplacemark.md)

# region

<sub>Instance Property</sub>

The geographic region associated with the placemark.

> [!warning] Deprecated
> Use either GeoToolbox.PlaceDescriptor or MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@NSCopying var region: CLRegion? { get }
```

## See Also

### Getting the placemark’s location

- [location](location.md) — The location object containing latitude and longitude information. _(deprecated)_
