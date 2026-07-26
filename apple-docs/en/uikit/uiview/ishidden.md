---
title: isHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/ishidden
source_url: 'https://developer.apple.com/documentation/uikit/uiview/ishidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/ishidden.json'
content_hash: 'sha256:cf8c611fbb709a65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# isHidden

<sub>Instance Property</sub>

A Boolean value that determines whether the view is hidden.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHidden: Bool { get set }
```

## Discussion

Setting the value of this property to [true](../../swift/true.md) hides the receiver and setting it to [false](../../swift/false.md) shows the receiver. The default value is [false](../../swift/false.md).

A hidden view disappears from its window and does not receive input events. It remains in its superview’s list of subviews, however, and participates in autoresizing as usual. Hiding a view with subviews has the effect of hiding those subviews and any view descendants they might have. This effect is implicit and does not alter the hidden state of the receiver’s descendants.

Hiding the view that is the window’s current first responder causes the view’s next valid key view to become the new first responder.

The value of this property reflects the state of the receiver only and does not account for the state of the receiver’s ancestors in the view hierarchy. Thus this property can be [false](../../swift/false.md) but the receiver may still be hidden if an ancestor is hidden.

## See Also

### Configuring a view’s visual appearance

- [backgroundColor](backgroundcolor.md) — The view’s background color.
- [alpha](alpha.md) — The view’s alpha value.
- [opaque](isopaque.md) — A Boolean value that determines whether the view is opaque.
- [tintColor](tintcolor.md) — The first nondefault tint color value in the view’s hierarchy, ascending from and starting with the view itself.
- [tintAdjustmentMode](tintadjustmentmode-swift.property.md) — The first non-default tint adjustment mode value in the view’s hierarchy, ascending from and starting with the view itself.
- [clipsToBounds](clipstobounds.md) — A Boolean value that determines whether subviews are confined to the bounds of the view.
- [clearsContextBeforeDrawing](clearscontextbeforedrawing.md) — A Boolean value that determines whether the view’s bounds should be automatically cleared before drawing.
- [maskView](mask.md) — An optional view whose alpha channel is used to mask a view’s content.
- [layerClass](layerclass.md) — Returns the class used to create the layer for instances of this class.
- [layer](layer.md) — The view’s Core Animation layer to use for rendering.
