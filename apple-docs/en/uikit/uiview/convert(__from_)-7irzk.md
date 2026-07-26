---
title: 'convert(_:from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/convert(_:from:)-7irzk'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/convert(_:from:)-7irzk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/convert%28_%3Afrom%3A%29-7irzk.json'
content_hash: 'sha256:a8026768700860c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# convert(_:from:)

<sub>Instance Method</sub>

Converts a rectangle from the coordinate system of another view to that of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func convert(_ rect: CGRect, from view: UIView?) -> CGRect
```

## Parameters

- `rect` — A rectangle specified in the local coordinate system (bounds) of `view`.

- `view` — The view with `rect` in its coordinate system. If `view` is `nil`, this method instead converts from window base coordinates. Otherwise, both `view` and the receiver must belong to the same [UIWindow](../uiwindow.md) object.

## Return Value

The converted rectangle.

## See Also

### Converting between view coordinate systems

- [- convertPoint:toView:](<convert(__to_)-1xizt.md>) — Converts a point from the receiver’s coordinate system to that of the specified view.
- [- convertPoint:fromView:](<convert(__from_)-8neo1.md>) — Converts a point from the coordinate system of a given view to that of the receiver.
- [- convertRect:toView:](<convert(__to_)-2kf3d.md>) — Converts a rectangle from the receiver’s coordinate system to that of another view.
