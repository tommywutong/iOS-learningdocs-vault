---
title: 'byUnion(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiregion/byunion(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiregion/byunion(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiregion/byunion%28with%3A%29.json'
content_hash: 'sha256:b178aa54e901b14d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRegion](../uiregion.md)

# byUnion(with:)

<sub>Instance Method</sub>

Returns a new region containing the combined areas of the specified region and the current region.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func byUnion(with region: UIRegion) -> Self
```

## Parameters

- `region` — The region to be combined with the current region.

## Return Value

A new region that contains the points from both the current region and the shape specified by the `region` parameter.

## Discussion

Combining any region with the infinite region returns the infinite region.

## See Also

### Creating complex regions

- [- inverseRegion](<inverse().md>) — Returns a new region that’s the mathematical inverse of the current region.
- [- regionByDifferenceFromRegion:](<bydifference(from_).md>) — Returns a new region created by subtracting the specified region from the current region.
- [- regionByIntersectionWithRegion:](<byintersection(with_).md>) — Returns a new region containing only the area occupied by both the specified region and current region.
