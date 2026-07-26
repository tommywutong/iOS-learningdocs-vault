---
title: 'resolvedStrokeColor(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibackgroundconfiguration-swift.struct/resolvedstrokecolor(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/resolvedstrokecolor(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-swift.struct/resolvedstrokecolor%28for%3A%29.json'
content_hash: 'sha256:eec947fdae81ae0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md)

# resolvedStrokeColor(for:)

<sub>Instance Method</sub>

Generates the resolved stroke color for the specified tint color, using the stroke color and color transformer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func resolvedStrokeColor(for tintColor: UIColor) -> UIColor
```

## Discussion

The resulting color depends on [strokeColor](strokecolor.md) and [strokeColorTransformer](strokecolortransformer.md).

## See Also

### Customizing the background

- [customView](customview.md) — A custom view for the background.
- [cornerRadius](cornerradius.md) — The preferred corner radius, using a continuous corner curve, for the background and stroke.
- [backgroundInsets](backgroundinsets.md) — The insets (or outsets, if negative) for the background and stroke, relative to the edges of the containing view.
- [edgesAddingLayoutMarginsToBackgroundInsets](edgesaddinglayoutmarginstobackgroundinsets.md) — The edges on which the configuration adds the containing view’s layout margins to the background insets.
- [backgroundColor](backgroundcolor.md) — The color of the background.
- [backgroundColorTransformer](backgroundcolortransformer.md) — The color transformer for resolving the background color.
- [resolvedBackgroundColor(for:)](<resolvedbackgroundcolor(for_).md>) — Generates the resolved background color for the specified tint color, using the background color and color transformer.
- [visualEffect](visualeffect.md) — The visual effect that the configuration applies to the background.
- [shadowProperties](shadowproperties.md)
- [UIShadowProperties](../uishadowproperties-swift.struct.md)
- [strokeColor](strokecolor.md) — The color of the stroke.
- [strokeColorTransformer](strokecolortransformer.md) — The color transformer for resolving the stroke color.
- [strokeWidth](strokewidth.md) — The width of the stroke.
- [strokeOutset](strokeoutset.md) — The outset (or inset, if negative) for the stroke.
- [image](image.md) — The image displayed in the view’s background.
