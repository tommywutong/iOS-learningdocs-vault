---
title: preferringMulticolor()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/symbolconfiguration-swift.class/preferringmulticolor()
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/preferringmulticolor()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.class/preferringmulticolor%28%29.json'
content_hash: 'sha256:aaf43b09545e478a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [SymbolConfiguration](../symbolconfiguration-swift.class.md)

# preferringMulticolor()

<sub>Type Method</sub>

Creates a color configuration that specifies that the symbol image uses its multicolor variant, if one exists.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func preferringMulticolor() -> Self
```

## Return Value

A symbol configuration that acquires the multicolor variant of a symbol.

## Discussion

Use this method to acquire the multicolor variant of a symbol, if one exists. This method is the primary approach to retrieving multicolor symbols.

For this color configuration to have an effect, your symbol image must have the following:

- Its [renderingMode](../renderingmode-swift.property.md) set to [UIImageRenderingModeAlwaysTemplate](../renderingmode-swift.enum/alwaystemplate.md) or [UIImageRenderingModeAutomatic](../renderingmode-swift.enum/automatic.md).
- Multicolor annotations. If your symbol doesn’t have multicolor annotations, the resulting image is a monochrome (template) symbol image. If you combine this configuration with a hierarchical or palette color configuration using [- configurationByApplyingConfiguration:](<../configuration-swift.class/applying(__).md>), the resulting symbol uses the multicolor variant, if one exists, and defaults to the hierarchical or palette variant otherwise.

## See Also

### Creating a color configuration

- [+ configurationWithHierarchicalColor:](<init(hierarchicalcolor_).md>) — Creates a color configuration with a color scheme that originates from one color.
- [+ configurationWithPaletteColors:](<init(palettecolors_).md>) — Creates a color configuration with a color scheme from a palette of multiple colors.
- [+ configurationPreferringMonochrome](<preferringmonochrome().md>) — Creates a color configuration that specifies that the symbol image uses its monochrome variant.
