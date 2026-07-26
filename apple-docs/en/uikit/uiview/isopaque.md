---
title: isOpaque
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/isopaque
source_url: 'https://developer.apple.com/documentation/uikit/uiview/isopaque'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/isopaque.json'
content_hash: 'sha256:90b2632061700294'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# isOpaque

<sub>Instance Property</sub>

A Boolean value that determines whether the view is opaque.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isOpaque: Bool { get set }
```

## Discussion

This property provides a hint to the drawing system as to how it should treat the view. If set to [true](../../swift/true.md), the drawing system treats the view as fully opaque, which allows the drawing system to optimize some drawing operations and improve performance. If set to [false](../../swift/false.md), the drawing system composites the view normally with other content. The default value of this property is [true](../../swift/true.md).

An opaque view is expected to fill its bounds with entirely opaque content—that is, the content should have an alpha value of `1.0`. If the view is opaque and either does not fill its bounds or contains wholly or partially transparent content, the results are unpredictable. You should always set the value of this property to [false](../../swift/false.md) if the view is fully or partially transparent.

You only need to set a value for the opaque property in subclasses of [UIView](../uiview.md) that draw their own content using the [- drawRect:](<draw(__).md>) method. The opaque property has no effect in system-provided classes such as [UIButton](../uibutton.md), [UILabel](../uilabel.md), [UITableViewCell](../uitableviewcell.md), and so on.

## See Also

### Configuring a view’s visual appearance

- [backgroundColor](backgroundcolor.md) — The view’s background color.
- [hidden](ishidden.md) — A Boolean value that determines whether the view is hidden.
- [alpha](alpha.md) — The view’s alpha value.
- [tintColor](tintcolor.md) — The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [tintAdjustmentMode](tintadjustmentmode-swift.property.md) — The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [clipsToBounds](clipstobounds.md) — A Boolean value that determines whether subviews are confined to the bounds of the view.
- [clearsContextBeforeDrawing](clearscontextbeforedrawing.md) — A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [maskView](mask.md) — An optional view whose alpha channel is used to mask a view’s content.
- [layerClass](layerclass.md) — Returns the class used to create the layer for instances of this class.
- [layer](layer.md) — The view’s Core Animation layer to use for rendering.
