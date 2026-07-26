---
title: 'removeLayoutGuide(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/removelayoutguide(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/removelayoutguide(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/removelayoutguide%28_%3A%29.json'
content_hash: 'sha256:f6d563bb56b35c7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# removeLayoutGuide(_:)

<sub>Instance Method</sub>

Removes the specified layout guide from the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeLayoutGuide(_ layoutGuide: UILayoutGuide)
```

## Parameters

- `layoutGuide` — The layout guide to be removed.

## Discussion

This method removes the layout guide from the view’s [layoutGuides](layoutguides.md) array and sets the guide’s [owningView](../uilayoutguide/owningview.md) property to `nil`. It also removes any constraints to the layout guide.

Layout guides cannot participate in Auto Layout constraints unless they are added to a view in the view hierarchy.

## See Also

### Working with layout guides

- [- addLayoutGuide:](<addlayoutguide(__).md>) — Adds the specified layout guide to the view.
- [layoutGuides](layoutguides.md) — The array of layout guide objects owned by this view.
- [layoutMarginsGuide](layoutmarginsguide.md) — A layout guide representing the view’s margins.
- [readableContentGuide](readablecontentguide.md) — A layout guide representing an area with a readable width within the view.
