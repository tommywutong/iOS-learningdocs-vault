---
title: containingRegion
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/region-swift.struct/containingregion
source_url: 'https://developer.apple.com/documentation/foundation/locale/region-swift.struct/containingregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/region-swift.struct/containingregion.json'
content_hash: 'sha256:bbd18837e073966c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Locale](../../locale.md) · [Region](../region-swift.struct.md)

# containingRegion

<sub>Instance Property</sub>

The region that contains this region, if any.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var containingRegion: Locale.Region? { get }
```

## Discussion

The following example shows how to look up the containing region for the `US` region.

```swift
let usRegion = Locale.Region("US")
let containingRegion = usRegion.containingRegion //Identifier "021": Northern America

```

## See Also

### Examining region properties

- [identifier](identifier.md) — The BCP 47 identifier of the region.
- [continent](continent.md) — The continent that contains this region, if any.
- [isISORegion](isisoregion.md) — A Boolean value that indicates whether the region is an ISO-defined region.
- [subRegions](subregions.md) — An array of all the sub-regions of the region.
