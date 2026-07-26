---
title: 'anchorWithOffset(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutyaxisanchor/anchorwithoffset(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutyaxisanchor/anchorwithoffset(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutyaxisanchor/anchorwithoffset%28to%3A%29.json'
content_hash: 'sha256:4395ceafd4beb350'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutYAxisAnchor](../nslayoutyaxisanchor.md)

# anchorWithOffset(to:)

<sub>Instance Method</sub>

Creates a layout dimension object from two anchors.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func anchorWithOffset(to otherAnchor: NSLayoutYAxisAnchor) -> NSLayoutDimension
```

## Parameters

- `otherAnchor` — The second anchor to use when creating the layout dimension.

## Return Value

The [NSLayoutDimension](../nslayoutdimension.md) object represented by the two anchors.

## Discussion

Use the returned object to define constraints relative to the space between the current anchor and the object in the `otherAnchor` parameter.
