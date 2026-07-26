---
title: continent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/region-swift.struct/continent
source_url: 'https://developer.apple.com/documentation/foundation/locale/region-swift.struct/continent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/region-swift.struct/continent.json'
content_hash: 'sha256:d22e9cd4dff3bac5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Region](../region-swift.struct.md)

# continent

<sub>Instance Property</sub>

The continent that contains this region, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var continent: Locale.Region? { get }
```

## Discussion

This value can be `nil` when the system can’t determine the appropriate continent, such as when the region isn’t an ISO region.

## See Also

### Examining region properties

- [identifier](identifier.md) — The BCP 47 identifier of the region.
- [containingRegion](containingregion.md) — The region that contains this region, if any.
- [isISORegion](isisoregion.md) — A Boolean value that indicates whether the region is an ISO-defined region.
- [subRegions](subregions.md) — An array of all the sub-regions of the region.
