---
title: UIImage.SymbolConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimage/symbolconfiguration-swift.class
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.class.json'
content_hash: 'sha256:b4aaba3419a28666'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# UIImage.SymbolConfiguration

<sub>Class</sub>

An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class SymbolConfiguration
```

## Overview

Symbol image configuration objects include details such as the point size, scale, text style, weight, and font to apply to your symbol image. The system uses these details to determine which variant of the image to use and how to scale or style the image.

[SymbolConfiguration](symbolconfiguration-swift.class.md) objects are immutable after you create them. If you use the [- configurationByApplyingConfiguration:](<configuration-swift.class/applying(__).md>) method on the object, the new image attributes replace any previous attributes you supplied. After creating a symbol configuration object, assign it to the [preferredSymbolConfiguration](../uiimageview/preferredsymbolconfiguration.md) property of the [UIImageView](../uiimageview.md) object you use to display the image. If you draw the image directly, use the [- imageWithConfiguration:](<withconfiguration(__).md>) method to create a new image that contains the new attributes.

## Relationships

- **Inherits From**: [Configuration](configuration-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSCoding](../../foundation/nscoding.md), [NSCopying](../../foundation/nscopying.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [NSSecureCoding](../../foundation/nssecurecoding.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a symbol configuration

- [+ configurationWithPointSize:](<symbolconfiguration-swift.class/init(pointsize_).md>) — Creates a configuration object with the specified point-size information.
- [+ configurationWithPointSize:weight:](<symbolconfiguration-swift.class/init(pointsize_weight_).md>) — Creates a configuration object with the specified point-size and weight information.
- [+ configurationWithPointSize:weight:scale:](<symbolconfiguration-swift.class/init(pointsize_weight_scale_).md>) — Creates a configuration object with the specified point-size, weight, and scale information.
- [+ configurationWithScale:](<symbolconfiguration-swift.class/init(scale_).md>) — Creates a configuration object with the specified scale information.
- [+ configurationWithTextStyle:](<symbolconfiguration-swift.class/init(textstyle_).md>) — Creates a configuration object with the specified font text style information.
- [+ configurationWithTextStyle:scale:](<symbolconfiguration-swift.class/init(textstyle_scale_).md>) — Creates a configuration object with the specified font text style and scale information.
- [+ configurationWithWeight:](<symbolconfiguration-swift.class/init(weight_).md>) — Creates a configuration object with the specified weight information.
- [+ configurationWithFont:](<symbolconfiguration-swift.class/init(font_).md>) — Creates a configuration object with the specified font information.
- [+ configurationWithFont:scale:](<symbolconfiguration-swift.class/init(font_scale_).md>) — Creates a configuration object with the specified font and scale information.
- [SymbolScale](symbolscale.md) — Constants that indicate which scale variant of a symbol image to use.
- [SymbolWeight](symbolweight.md) — Constants that indicate which weight variant of a symbol image to use.
- [SymbolColorRenderingMode](symbolcolorrenderingmode.md)
- [SymbolVariableValueMode](symbolvariablevaluemode.md)

### Creating a color configuration

- [+ configurationWithHierarchicalColor:](<symbolconfiguration-swift.class/init(hierarchicalcolor_).md>) — Creates a color configuration with a color scheme that originates from one color.
- [+ configurationWithPaletteColors:](<symbolconfiguration-swift.class/init(palettecolors_).md>) — Creates a color configuration with a color scheme from a palette of multiple colors.
- [+ configurationPreferringMulticolor](<symbolconfiguration-swift.class/preferringmulticolor().md>) — Creates a color configuration that specifies that the symbol image uses its multicolor variant, if one exists.
- [+ configurationPreferringMonochrome](<symbolconfiguration-swift.class/preferringmonochrome().md>) — Creates a color configuration that specifies that the symbol image uses its monochrome variant.

### Getting an unspecified configuration

- [unspecifiedConfiguration](symbolconfiguration-swift.class/unspecified.md) — A symbol configuration object that contains unspecified values for all attributes.

### Removing configuration attributes

- [- configurationWithoutPointSizeAndWeight](<symbolconfiguration-swift.class/configurationwithoutpointsizeandweight().md>) — Returns a copy of the current symbol configuration object without point-size and weight information.
- [- configurationWithoutScale](<symbolconfiguration-swift.class/configurationwithoutscale().md>) — Returns a copy of the current symbol configuration object without scale information.
- [- configurationWithoutTextStyle](<symbolconfiguration-swift.class/configurationwithouttextstyle().md>) — Returns a copy of the current symbol configuration object without font text style information.
- [- configurationWithoutWeight](<symbolconfiguration-swift.class/configurationwithoutweight().md>) — Returns a copy of the current symbol configuration object without weight information.

### Comparing symbol image configurations

- [- isEqualToConfiguration:](<symbolconfiguration-swift.class/isequal(to_).md>) — Returns a Boolean value that indicates whether the configuration objects are equivalent.

### Initializers

- [+ configurationWithColorRenderingMode:](<symbolconfiguration-swift.class/init(colorrenderingmode_).md>) — Initializes a symbol configuration with a preferred color rendering mode.
- [+ configurationWithVariableValueMode:](<symbolconfiguration-swift.class/init(variablevaluemode_).md>) — Initializes a symbol configuration with a preferred variable value mode.

## See Also

### Representations

- [UIImage](../uiimage.md) — An object that manages image data in your app.
- [Configuration](configuration-swift.class.md) — A configuration object that contains the traits that the system uses when selecting the current image variant.
