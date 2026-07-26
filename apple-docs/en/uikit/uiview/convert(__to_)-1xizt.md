---
title: 'convert(_:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/convert(_:to:)-1xizt'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/convert(_:to:)-1xizt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/convert%28_%3Ato%3A%29-1xizt.json'
content_hash: 'sha256:67d9bf7222d1cd96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# convert(_:to:)

<sub>Instance Method</sub>

Converts a point from the receiver’s coordinate system to that of the specified view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ point: CGPoint, to view: UIView?) -> CGPoint
```

## Parameters

- `point` — A point specified in the local coordinate system (bounds) of the receiver.

- `view` — The view into whose coordinate system `point` is to be converted. If `view` is `nil`, this method instead converts to window base coordinates. Otherwise, both `view` and the receiver must belong to the same [UIWindow](../uiwindow.md) object.

## Return Value

The point converted to the coordinate system of `view`.

## See Also

### Converting between view coordinate systems

- [- convertPoint:fromView:](<convert(__from_)-8neo1.md>) — Converts a point from the coordinate system of a given view to that of the receiver.
- [- convertRect:toView:](<convert(__to_)-2kf3d.md>) — Converts a rectangle from the receiver’s coordinate system to that of another view.
- [- convertRect:fromView:](<convert(__from_)-7irzk.md>) — Converts a rectangle from the coordinate system of another view to that of the receiver.
