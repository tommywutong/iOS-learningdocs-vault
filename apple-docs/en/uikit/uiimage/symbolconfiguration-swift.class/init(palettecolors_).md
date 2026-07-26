---
title: 'init(paletteColors:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(palettecolors:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(palettecolors:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.class/init%28palettecolors%3A%29.json'
content_hash: 'sha256:3407569cbb2e29ff'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [SymbolConfiguration](../symbolconfiguration-swift.class.md)

# init(paletteColors:)

<sub>Initializer</sub>

Creates a color configuration with a color scheme from a palette of multiple colors.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init(paletteColors: [UIColor])
```

## Parameters

- `paletteColors` — The colors to apply to the symbol.

## Discussion

When you create an image with this configuration, the system applies each color to the corresponding layer in the symbol layer hierarchy.

If the symbol has only two nonconsecutive layers (primary and tertiary), specifying two colors applies the second color to the tertiary layer. Specifying three colors ignores the second color and applies the third color to the tertiary layer.

For this color configuration to have an effect, your symbol image must have the following:

- Its [renderingMode](../renderingmode-swift.property.md) set to [UIImageRenderingModeAlwaysTemplate](../renderingmode-swift.enum/alwaystemplate.md) or [UIImageRenderingModeAutomatic](../renderingmode-swift.enum/automatic.md).
- Hierarchical layer annotations. If your symbol doesn’t have hierarchical layer annotations, the resulting image is a monochrome (template) symbol image.

This color configuration can’t combine with hierarchical color configurations that you create with [+ configurationWithHierarchicalColor:](<init(hierarchicalcolor_).md>). If you attempt to combine this configuration with a hierarchical color configuration, the last configuration that you specify takes precedence, overwriting the previous color configuration.

## See Also

### Creating a color configuration

- [+ configurationWithHierarchicalColor:](<init(hierarchicalcolor_).md>) — Creates a color configuration with a color scheme that originates from one color.
- [+ configurationPreferringMulticolor](<preferringmulticolor().md>) — Creates a color configuration that specifies that the symbol image uses its multicolor variant, if one exists.
- [+ configurationPreferringMonochrome](<preferringmonochrome().md>) — Creates a color configuration that specifies that the symbol image uses its monochrome variant.
