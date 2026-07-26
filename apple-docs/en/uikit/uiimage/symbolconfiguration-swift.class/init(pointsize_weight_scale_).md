---
title: 'init(pointSize:weight:scale:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(pointsize:weight:scale:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(pointsize:weight:scale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.class/init%28pointsize%3Aweight%3Ascale%3A%29.json'
content_hash: 'sha256:1ba6c1f8d6077bb4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [SymbolConfiguration](../symbolconfiguration-swift.class.md)

# init(pointSize:weight:scale:)

<sub>Initializer</sub>

Creates a configuration object with the specified point-size, weight, and scale information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight, scale: UIImage.SymbolScale)
```

## Parameters

- `pointSize` — The system font point size to use for the configuration.

- `weight` — The symbol image weight variant to select. Use this parameter to match the weight of the symbol image to your other content. For a list of possible values, see [SymbolWeight](../symbolweight.md).

- `scale` — The symbol image scale variant to select. Use this parameter to make the image appear bigger or smaller than text that uses the same point size. For a list of possible values, see [SymbolScale](../symbolscale.md).

## Return Value

A new symbol configuration object with the specified information.

## See Also

### Creating a symbol configuration

- [+ configurationWithPointSize:](<init(pointsize_).md>) — Creates a configuration object with the specified point-size information.
- [+ configurationWithPointSize:weight:](<init(pointsize_weight_).md>) — Creates a configuration object with the specified point-size and weight information.
- [+ configurationWithScale:](<init(scale_).md>) — Creates a configuration object with the specified scale information.
- [+ configurationWithTextStyle:](<init(textstyle_).md>) — Creates a configuration object with the specified font text style information.
- [+ configurationWithTextStyle:scale:](<init(textstyle_scale_).md>) — Creates a configuration object with the specified font text style and scale information.
- [+ configurationWithWeight:](<init(weight_).md>) — Creates a configuration object with the specified weight information.
- [+ configurationWithFont:](<init(font_).md>) — Creates a configuration object with the specified font information.
- [+ configurationWithFont:scale:](<init(font_scale_).md>) — Creates a configuration object with the specified font and scale information.
- [SymbolScale](../symbolscale.md) — Constants that indicate which scale variant of a symbol image to use.
- [SymbolWeight](../symbolweight.md) — Constants that indicate which weight variant of a symbol image to use.
- [SymbolColorRenderingMode](../symbolcolorrenderingmode.md)
- [SymbolVariableValueMode](../symbolvariablevaluemode.md)
