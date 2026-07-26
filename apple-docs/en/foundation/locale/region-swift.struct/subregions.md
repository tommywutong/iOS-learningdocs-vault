---
title: subRegions
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/region-swift.struct/subregions
source_url: 'https://developer.apple.com/documentation/foundation/locale/region-swift.struct/subregions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/region-swift.struct/subregions.json'
content_hash: 'sha256:715f6e932b2d0470'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Region](../region-swift.struct.md)

# subRegions

<sub>Instance Property</sub>

An array of all the sub-regions of the region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var subRegions: [Locale.Region] { get }
```

## Discussion

The following example looks up the sub-regions of region `021`, which represents North America.

```swift
let northAmericaRegion = Locale.Region("021")
let subRegions = northAmericaRegion.subRegions //BM, CA, GL, PM, US
```

The returned `subRegions` have the following identifiers:

| Identifier | Country |
|---|---|
| BM | Bermuda |
| CA | Canada |
| GL | Greenland |
| PM | Saint Pierre and Miquelon |
| US | United States |

## See Also

### Examining region properties

- [identifier](identifier.md) — The BCP 47 identifier of the region.
- [containingRegion](containingregion.md) — The region that contains this region, if any.
- [continent](continent.md) — The continent that contains this region, if any.
- [isISORegion](isisoregion.md) — A Boolean value that indicates whether the region is an ISO-defined region.
