---
title: layoutFrame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutguide/layoutframe
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutguide/layoutframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutguide/layoutframe.json'
content_hash: 'sha256:8ee0484b7d87cc0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILayoutGuide](../uilayoutguide.md)

# layoutFrame

<sub>Instance Property</sub>

The layout guide’s frame in its owning view’s coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var layoutFrame: CGRect { get }
```

## Discussion

The layout guide defines a rectangular space in its owning view’s coordinate system. This property contains a valid [CGRect](../../corefoundation/cgrect.md) value by the time its owning view’s [- layoutSubviews](<../uiview/layoutsubviews().md>) method is called.

## See Also

### Related Documentation

- [- layoutSubviews](<../uiview/layoutsubviews().md>) — Lays out subviews.

### Working with layout guides

- [identifier](identifier.md) — A string used to identify the layout guide.
- [owningView](owningview.md) — The view that owns this layout guide.
