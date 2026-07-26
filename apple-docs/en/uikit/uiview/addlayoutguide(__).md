---
title: 'addLayoutGuide(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/addlayoutguide(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/addlayoutguide(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/addlayoutguide%28_%3A%29.json'
content_hash: 'sha256:205f2e42da86ee83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# addLayoutGuide(_:)

<sub>Instance Method</sub>

Adds the specified layout guide to the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addLayoutGuide(_ layoutGuide: UILayoutGuide)
```

## Parameters

- `layoutGuide` — The layout guide to be added.

## Discussion

This method adds the specified layout guide to the end of the view’s [layoutGuides](layoutguides.md) array. It also assigns the view to the guide’s [owningView](../uilayoutguide/owningview.md) property. Each guide can have only one owning view.

After the guide has been added to a view, it can participate in Auto Layout constraints with that view’s hierarchy.

## See Also

### Working with layout guides

- [layoutGuides](layoutguides.md) — The array of layout guide objects owned by this view.
- [layoutMarginsGuide](layoutmarginsguide.md) — A layout guide representing the view’s margins.
- [readableContentGuide](readablecontentguide.md) — A layout guide representing an area with a readable width within the view.
- [- removeLayoutGuide:](<removelayoutguide(__).md>) — Removes the specified layout guide from the view.
