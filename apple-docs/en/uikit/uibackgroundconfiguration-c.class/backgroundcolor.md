---
title: backgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundconfiguration-c.class/backgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-c.class/backgroundcolor.json'
content_hash: 'sha256:89b41bb5eeb20b3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-c.class.md)

# backgroundColor

<sub>Instance Property</sub>

The color of the background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, strong, nullable) UIColor * backgroundColor;
```

## Discussion

If the value is `nil`, the background color is the view’s tint color. Use [clearColor](../uicolor/clear.md) for a transparent background with no color.

## See Also

### Customizing the background

- [customView](customview.md) — A custom view for the background.
- [cornerRadius](cornerradius.md) — The preferred corner radius, using a continuous corner curve, for the background and stroke.
- [backgroundInsets](backgroundinsets.md) — The insets (or outsets, if negative) for the background and stroke, relative to the edges of the containing view.
- [edgesAddingLayoutMarginsToBackgroundInsets](edgesaddinglayoutmarginstobackgroundinsets.md) — The edges on which the configuration adds the containing view’s layout margins to the background insets.
- [backgroundColorTransformer](backgroundcolortransformer.md) — The color transformer for resolving the background color.
- [resolvedBackgroundColorForTintColor:](resolvedbackgroundcolorfortintcolor_.md) — Generates the resolved background color for the specified tint color, using the background color and color transformer.
- [visualEffect](visualeffect.md) — The visual effect that the configuration applies to the background.
- [shadowProperties](shadowproperties.md) — Describes a shadow applied by the background. Defaults to no shadow (i.e. a shadow with an opacity of 0.0).
- [UIShadowProperties](../uishadowproperties-c.class.md)
- [strokeColor](strokecolor.md) — The color of the stroke.
- [strokeColorTransformer](strokecolortransformer.md) — The color transformer for resolving the stroke color.
- [resolvedStrokeColorForTintColor:](resolvedstrokecolorfortintcolor_.md) — Generates the resolved stroke color for the specified tint color, using the stroke color and color transformer.
- [strokeWidth](strokewidth.md) — The width of the stroke.
- [strokeOutset](strokeoutset.md) — The outset (or inset, if negative) for the stroke.
- [image](image.md) — The image displayed in the view’s background.
