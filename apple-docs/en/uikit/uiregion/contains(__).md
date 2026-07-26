---
title: 'contains(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiregion/contains(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiregion/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiregion/contains%28_%3A%29.json'
content_hash: 'sha256:268c91500c4d3d1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRegion](../uiregion.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean indicating whether the specified point is inside of the current region.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func contains(_ point: CGPoint) -> Bool
```

## Parameters

- `point` — The point to test. The specified point must be in the region’s coordinate system.

## Return Value

[true](../../swift/true.md) if the point is in the current region or [false](../../swift/false.md) if it is not.

## Discussion

UIKit Dynamics normally calls this method when it needs to determine the interactions between two objects. If you call this method yourself, remember that the origin of the region object itself is at the center of the region’s shape and you might need to adjust the value of `point` accordingly.
