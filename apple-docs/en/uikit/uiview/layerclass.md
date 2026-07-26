---
title: layerClass
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/layerclass
source_url: 'https://developer.apple.com/documentation/uikit/uiview/layerclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/layerclass.json'
content_hash: 'sha256:d449ae143d014da8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# layerClass

<sub>Type Property</sub>

Returns the class used to create the layer for instances of this class.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var layerClass: AnyClass { get }
```

## Return Value

The class used to create the view’s Core Animation layer.

## Discussion

This method returns the [CALayer](../../quartzcore/calayer.md) class object by default. Subclasses can override this method and return a different layer class as needed. For example, if your view uses tiling to display a large scrollable area, you might want to override this property and return the [CATiledLayer](../../quartzcore/catiledlayer.md) class, as shown in the following code.

```swift
override class var layerClass : AnyClass {
   return CATiledLayer.self
}
```

This method is called only once early in the creation of the view in order to create the corresponding layer object.

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
- [maskView](mask.md) — An optional view whose alpha channel is used to mask a view’s content.
- [layer](layer.md) — The view’s Core Animation layer to use for rendering.
