---
title: 'byDifference(from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiregion/bydifference(from:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiregion/bydifference(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiregion/bydifference%28from%3A%29.json'
content_hash: 'sha256:ee7d67122047628c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRegion](../uiregion.md)

# byDifference(from:)

<sub>Instance Method</sub>

Returns a new region created by subtracting the specified region from the current region.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func byDifference(from region: UIRegion) -> Self
```

## Parameters

- `region` — The region to be subtracted from the current region.

## Return Value

A new region that contains the points that are in the current region and not in the area defined by the `region` parameter.

## See Also

### Creating complex regions

- [- inverseRegion](<inverse().md>) — Returns a new region that’s the mathematical inverse of the current region.
- [- regionByIntersectionWithRegion:](<byintersection(with_).md>) — Returns a new region containing only the area occupied by both the specified region and current region.
- [- regionByUnionWithRegion:](<byunion(with_).md>) — Returns a new region containing the combined areas of the specified region and the current region.
