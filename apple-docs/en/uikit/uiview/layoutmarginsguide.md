---
title: layoutMarginsGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/layoutmarginsguide
source_url: 'https://developer.apple.com/documentation/uikit/uiview/layoutmarginsguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/layoutmarginsguide.json'
content_hash: 'sha256:5b5dcb96acb2d69d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# layoutMarginsGuide

<sub>Instance Property</sub>

A layout guide representing the view’s margins.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var layoutMarginsGuide: UILayoutGuide { get }
```

## Discussion

Use this layout guide’s anchors to create constraints with the view’s margin.

## See Also

### Related Documentation

- [layoutMargins](layoutmargins.md) — The default spacing to use when laying out content in the view.

### Working with layout guides

- [- addLayoutGuide:](<addlayoutguide(__).md>) — Adds the specified layout guide to the view.
- [layoutGuides](layoutguides.md) — The array of layout guide objects owned by this view.
- [readableContentGuide](readablecontentguide.md) — A layout guide representing an area with a readable width within the view.
- [- removeLayoutGuide:](<removelayoutguide(__).md>) — Removes the specified layout guide from the view.
