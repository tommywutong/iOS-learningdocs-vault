---
title: 'effectiveRadius(corner:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/effectiveradius(corner:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/effectiveradius(corner:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/effectiveradius%28corner%3A%29.json'
content_hash: 'sha256:8185510585fe153e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# effectiveRadius(corner:)

<sub>Instance Method</sub>

Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func effectiveRadius(corner: UIRectCorner) -> CGFloat
```

## Parameters

- `corner` — The corner whose effective radius you want to calculate.

## Return Value

A `CGFloat` value for the effective radius, expressed in points.

## Overview

When you call this method from [- layoutSubviews](<layoutsubviews().md>), [- updateProperties](<updateproperties().md>), or [- updateProperties](<../uiviewcontroller/updateproperties().md>), automatic invalidation occurs if the effective radius changes. If you provide more than one corner (for example, [UIRectCornerAllCorners](../uirectcorner/allcorners.md)), the returned radius represents the maximum effective radius of those corners.

## See Also

### Configuring a view’s corners

- [cornerConfiguration](cornerconfiguration-7l0ja.md) — A configuration that defines the corners of the view.
- [UICornerConfiguration](../uicornerconfiguration-swift.struct.md) — A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [UICornerRadius](../uicornerradius-swift.struct.md) — A type that represents the radius the system uses to round a corner.
