---
title: 'init(textStyle:scale:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(textstyle:scale:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(textstyle:scale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.class/init%28textstyle%3Ascale%3A%29.json'
content_hash: 'sha256:a94e2889bafef620'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [SymbolConfiguration](../symbolconfiguration-swift.class.md)

# init(textStyle:scale:)

<sub>Initializer</sub>

Creates a configuration object with the specified font text style and scale information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init(textStyle: UIFont.TextStyle, scale: UIImage.SymbolScale)
```

## Parameters

- `textStyle` — The system text styles that support Dynamic Type. For a list of possible values, see [TextStyle](../../uifont/textstyle.md).

- `scale` — The symbol image scale variant to select. Use this parameter to make the image appear bigger or smaller than text that uses the same text style. For a list of possible values, see [SymbolScale](../symbolscale.md).

## Return Value

A new symbol configuration object with the specified information.

## Discussion

Symbol images pick up the font styling information associated with the specified text style, causing them to match any text that uses the same style. Like it does for the text, UIKit scales the image to match the current Dynamic Type setting.

## See Also

### Creating a symbol configuration

- [+ configurationWithPointSize:](<init(pointsize_).md>) — Creates a configuration object with the specified point-size information.
- [+ configurationWithPointSize:weight:](<init(pointsize_weight_).md>) — Creates a configuration object with the specified point-size and weight information.
- [+ configurationWithPointSize:weight:scale:](<init(pointsize_weight_scale_).md>) — Creates a configuration object with the specified point-size, weight, and scale information.
- [+ configurationWithScale:](<init(scale_).md>) — Creates a configuration object with the specified scale information.
- [+ configurationWithTextStyle:](<init(textstyle_).md>) — Creates a configuration object with the specified font text style information.
- [+ configurationWithWeight:](<init(weight_).md>) — Creates a configuration object with the specified weight information.
- [+ configurationWithFont:](<init(font_).md>) — Creates a configuration object with the specified font information.
- [+ configurationWithFont:scale:](<init(font_scale_).md>) — Creates a configuration object with the specified font and scale information.
- [SymbolScale](../symbolscale.md) — Constants that indicate which scale variant of a symbol image to use.
- [SymbolWeight](../symbolweight.md) — Constants that indicate which weight variant of a symbol image to use.
- [SymbolColorRenderingMode](../symbolcolorrenderingmode.md)
- [SymbolVariableValueMode](../symbolvariablevaluemode.md)
