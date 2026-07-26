---
title: backgroundColorTransformer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibackgroundconfiguration-swift.struct/backgroundcolortransformer
source_url: 'https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/backgroundcolortransformer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibackgroundconfiguration-swift.struct/backgroundcolortransformer.json'
content_hash: 'sha256:7cd959dda03a1e10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBackgroundConfiguration](../uibackgroundconfiguration-swift.struct.md)

# backgroundColorTransformer

<sub>Instance Property</sub>

The color transformer for resolving the background color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundColorTransformer: UIConfigurationColorTransformer? { get set }
```

## Discussion

If the value is `nil`, the configuration uses [backgroundColor](backgroundcolor.md) without any transformations.

## See Also

### Customizing the background

- [customView](customview.md) — A custom view for the background.
- [cornerRadius](cornerradius.md) — The preferred corner radius, using a continuous corner curve, for the background and stroke.
- [backgroundInsets](backgroundinsets.md) — The insets (or outsets, if negative) for the background and stroke, relative to the edges of the containing view.
- [edgesAddingLayoutMarginsToBackgroundInsets](edgesaddinglayoutmarginstobackgroundinsets.md) — The edges on which the configuration adds the containing view’s layout margins to the background insets.
- [backgroundColor](backgroundcolor.md) — The color of the background.
- [resolvedBackgroundColor(for:)](<resolvedbackgroundcolor(for_).md>) — Generates the resolved background color for the specified tint color, using the background color and color transformer.
- [visualEffect](visualeffect.md) — The visual effect that the configuration applies to the background.
- [shadowProperties](shadowproperties.md)
- [UIShadowProperties](../uishadowproperties-swift.struct.md)
- [strokeColor](strokecolor.md) — The color of the stroke.
- [strokeColorTransformer](strokecolortransformer.md) — The color transformer for resolving the stroke color.
- [resolvedStrokeColor(for:)](<resolvedstrokecolor(for_).md>) — Generates the resolved stroke color for the specified tint color, using the stroke color and color transformer.
- [strokeWidth](strokewidth.md) — The width of the stroke.
- [strokeOutset](strokeoutset.md) — The outset (or inset, if negative) for the stroke.
- [image](image.md) — The image displayed in the view’s background.
