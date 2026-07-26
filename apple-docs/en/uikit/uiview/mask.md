---
title: mask
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/mask
source_url: 'https://developer.apple.com/documentation/uikit/uiview/mask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/mask.json'
content_hash: 'sha256:d6246d7aea074637'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# mask

<sub>Instance Property</sub>

An optional view whose alpha channel is used to mask a view’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var mask: UIView? { get set }
```

## Discussion

The view’s alpha channel determines how much of the view’s content and background shows through. Fully or partially opaque pixels allow the underlying content to show through but fully transparent pixels block that content.

## See Also

### Configuring a view’s visual appearance

- [backgroundColor](backgroundcolor.md) — The view’s background color.
- [hidden](ishidden.md) — A Boolean value that determines whether the view is hidden.
- [alpha](alpha.md) — The view’s alpha value.
- [opaque](isopaque.md) — A Boolean value that determines whether the view is opaque.
- [tintColor](tintcolor.md) — The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [tintAdjustmentMode](tintadjustmentmode-swift.property.md) — The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [clipsToBounds](clipstobounds.md) — A Boolean value that determines whether subviews are confined to the bounds of the view.
- [clearsContextBeforeDrawing](clearscontextbeforedrawing.md) — A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [layerClass](layerclass.md) — Returns the class used to create the layer for instances of this class.
- [layer](layer.md) — The view’s Core Animation layer to use for rendering.
