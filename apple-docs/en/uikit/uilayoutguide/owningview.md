---
title: owningView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutguide/owningview
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutguide/owningview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutguide/owningview.json'
content_hash: 'sha256:6f52893fc45e5f71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutGuide](../uilayoutguide.md)

# owningView

<sub>Instance Property</sub>

The view that owns this layout guide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var owningView: UIView? { get set }
```

## Discussion

By default, this property is `nil`. To participate in Auto Layout, the layout guide must be added to a view by calling its [- addLayoutGuide:](<../uiview/addlayoutguide(__).md>) method. Do not modify this property directly. Instead, use the view’s [- addLayoutGuide:](<../uiview/addlayoutguide(__).md>) and [- removeLayoutGuide:](<../uiview/removelayoutguide(__).md>) methods, which update this property as necessary.

## See Also

### Working with layout guides

- [identifier](identifier.md) — A string used to identify the layout guide.
- [layoutFrame](layoutframe.md) — The layout guide’s frame in its owning view’s coordinate system.
