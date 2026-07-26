---
title: 'byIntersection(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiregion/byintersection(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiregion/byintersection(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiregion/byintersection%28with%3A%29.json'
content_hash: 'sha256:db393f99a79425b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRegion](../uiregion.md)

# byIntersection(with:)

<sub>Instance Method</sub>

Returns a new region containing only the area occupied by both the specified region and current region.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func byIntersection(with region: UIRegion) -> Self
```

## Parameters

- `region` — The region to be intersected with the current region.

## Return Value

A new region that contains only the points that are in both the current region and the shape specified by the `region` parameter.

## See Also

### Creating complex regions

- [- inverseRegion](<inverse().md>) — Returns a new region that’s the mathematical inverse of the current region.
- [- regionByDifferenceFromRegion:](<bydifference(from_).md>) — Returns a new region created by subtracting the specified region from the current region.
- [- regionByUnionWithRegion:](<byunion(with_).md>) — Returns a new region containing the combined areas of the specified region and the current region.
