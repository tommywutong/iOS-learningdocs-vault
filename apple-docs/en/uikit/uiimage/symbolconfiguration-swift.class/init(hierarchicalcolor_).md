---
title: 'init(hierarchicalColor:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(hierarchicalcolor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(hierarchicalcolor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.class/init%28hierarchicalcolor%3A%29.json'
content_hash: 'sha256:ddf9bab4a6822aac'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [SymbolConfiguration](../symbolconfiguration-swift.class.md)

# init(hierarchicalColor:)

<sub>Initializer</sub>

Creates a color configuration with a color scheme that originates from one color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init(hierarchicalColor: UIColor)
```

## Parameters

- `hierarchicalColor` — The colors to apply to the symbol.

## Discussion

When you create an image with this configuration, the system generates a color scheme according to the color you specify, creating secondary and tertiary colors by reducing the intensity of the base color. Typically, the system generates the secondary and tertiary colors by reducing the opacity of the primary color, but it may perform additional color adjustments.

The system renders all layers in your symbol with the primary, secondary, and tertiary colors according to the symbol layer hierarchy.

For this color configuration to have an effect, your symbol image must have the following:

- Its [renderingMode](../renderingmode-swift.property.md) set to [UIImageRenderingModeAlwaysTemplate](../renderingmode-swift.enum/alwaystemplate.md) or [UIImageRenderingModeAutomatic](../renderingmode-swift.enum/automatic.md).
- Hierarchical layer annotations. If your symbol doesn’t have hierarchical layer annotations, the resulting image is a monochrome (template) symbol image.

This color configuration can’t combine with palette color configurations that you create with [+ configurationWithPaletteColors:](<init(palettecolors_).md>). If you attempt to combine this configuration with a palette color configuration, the last configuration that you specify takes precedence, overwriting the previous color configuration.

## See Also

### Creating a color configuration

- [+ configurationWithPaletteColors:](<init(palettecolors_).md>) — Creates a color configuration with a color scheme from a palette of multiple colors.
- [+ configurationPreferringMulticolor](<preferringmulticolor().md>) — Creates a color configuration that specifies that the symbol image uses its multicolor variant, if one exists.
- [+ configurationPreferringMonochrome](<preferringmonochrome().md>) — Creates a color configuration that specifies that the symbol image uses its monochrome variant.
