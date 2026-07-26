---
title: ocean
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.8+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/clplacemark/ocean
source_url: 'https://developer.apple.com/documentation/corelocation/clplacemark/ocean'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clplacemark/ocean.json'
content_hash: 'sha256:7e81377d53fcb053'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLPlacemark](../clplacemark.md)

# ocean

<sub>Instance Property</sub>

The name of the ocean associated with the placemark.

> [!warning] Deprecated
> Use either GeoToolbox.PlaceDescriptor or MapKit

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var ocean: String? { get }
```

## Discussion

For coordinates that lie over an ocean, this property contains the name of the ocean.

## See Also

### Getting landscape information

- [inlandWater](inlandwater.md) — The name of the inland water body associated with the placemark. _(deprecated)_
