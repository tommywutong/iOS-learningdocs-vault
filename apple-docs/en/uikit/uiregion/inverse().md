---
title: inverse()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiregion/inverse()
source_url: 'https://developer.apple.com/documentation/uikit/uiregion/inverse()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiregion/inverse%28%29.json'
content_hash: 'sha256:4b590987cde8c942'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRegion](../uiregion.md)

# inverse()

<sub>Instance Method</sub>

Returns a new region that’s the mathematical inverse of the current region.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func inverse() -> Self
```

## Return Value

A new region whose contents include all points that are not in the current region.

## Discussion

The inverse of the infinite region is an empty region.

## See Also

### Creating complex regions

- [- regionByDifferenceFromRegion:](<bydifference(from_).md>) — Returns a new region created by subtracting the specified region from the current region.
- [- regionByIntersectionWithRegion:](<byintersection(with_).md>) — Returns a new region containing only the area occupied by both the specified region and current region.
- [- regionByUnionWithRegion:](<byunion(with_).md>) — Returns a new region containing the combined areas of the specified region and the current region.
