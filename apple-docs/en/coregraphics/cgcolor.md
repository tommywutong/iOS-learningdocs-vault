---
title: CGColor
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolor
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolor.json'
content_hash: 'sha256:09d0ec2b22a630d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColor

<sub>Class</sub>

A set of components that define a color, with a color space specifying how to interpret them.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGColor
```

## Overview

`CGColor` is the fundamental data type used internally by Core Graphics to represent colors. `CGColor` objects, and the functions that operate on them, provide a fast and convenient way of managing and setting colors directly, especially colors that are reused (such as black for text).

A color object contains a set of components (such as red, green, and blue) that uniquely define a color, and a color space that specifies how those components should be interpreted.

Color objects provide a fast and convenient way to manage and set colors, especially colors that are used repeatedly. Drawing operations use color objects for setting fill and stroke colors, managing alpha, and setting color with a pattern.

[CGColor](cgcolor.md) is derived from [CFTypeRef](../corefoundation/cftyperef.md) and inherits the properties that all Core Foundation types have in common.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Colors

- [CGColorCreateCopy](<cgcolor/copy().md>) — Creates a copy of an existing color.
- [CGColorCreateCopyWithAlpha](<cgcolor/copy(alpha_).md>) — Creates a copy of an existing color, substituting a new alpha value.
- [CGColorCreateGenericCMYK](<cgcolor/init(genericcmykcyan_magenta_yellow_black_alpha_).md>) — Creates a color in the Generic CMYK color space.
- [CGColorCreateGenericGray](<cgcolor/init(gray_alpha_).md>) — Creates a color in the Generic gray color space.
- [CGColorCreateGenericGrayGamma2_2](<cgcolor/init(genericgraygamma2_2gray_alpha_).md>) — Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [CGColorCreateGenericRGB](<cgcolor/init(red_green_blue_alpha_).md>) — Creates a color in the Generic RGB color space.
- [CGColorCreateSRGB](<cgcolor/init(srgbred_green_blue_alpha_).md>) — Creates a color in the sRGB color space.
- [CGColorCreate](<cgcolor/init(colorspace_components_).md>) — Creates a color using a list of intensity values (including alpha) and an associated color space.
- [CGColorCreateWithPattern](<cgcolor/init(patternspace_pattern_components_).md>) — Creates a color using a list of intensity values (including alpha), a pattern color space, and a pattern.

### Getting System Colors

- [black](cgcolor/black.md) — The black color in the Generic gray color space.
- [white](cgcolor/white.md) — The white color in the Generic gray color space.
- [clear](cgcolor/clear.md) — The clear color in the Generic gray color space.

### Examining a Color

- [CGColorGetAlpha](cgcolor/alpha.md) — Returns the value of the alpha component associated with a color.
- [CGColorGetColorSpace](cgcolor/colorspace.md) — Returns the color space associated with a color.
- [components](cgcolor/components.md) — Returns the values of the color components (including alpha) associated with a color.
- [CGColorGetNumberOfComponents](cgcolor/numberofcomponents.md) — Returns the number of color components (including alpha) associated with a color.
- [CGColorGetPattern](cgcolor/pattern.md) — Returns the pattern associated with a color in a pattern color space.

### Converting Between Color Spaces

- [kCGColorConversionTRCSize](cgcolor/conversiontrcsize.md)
- [CGColorCreateCopyByMatchingToColorSpace](<cgcolor/converted(to_intent_options_).md>) — Creates a new color in a different color space that matches the provided color.

### Working with Core Foundation Types

- [CGColorGetTypeID](cgcolor/typeid.md) — Returns the Core Foundation type identifier for a color data type.

### Type Properties

- [kCGColorConversionBlackPointCompensation](cgcolor/conversionblackpointcompensation.md) — An option for whether to apply black point compensation when converting between color profiles.

### Initializers

- [CGColorCreateWithContentHeadroom](<cgcolor/init(headroom_colorspace_red_green_blue_alpha_).md>)

### Instance Properties

- [CGColorGetContentHeadroom](cgcolor/contentheadroom.md)

## See Also

### Related Documentation

- [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)

### Colors and Fonts

- [CGColorConversionInfo](cgcolorconversioninfo.md) — An object that describes how to convert between color spaces for use by other system services.
- [CGColorSpace](cgcolorspace.md) — A profile that specifies how to interpret a color value for display.
- [CGFont](cgfont.md) — A set of character glyphs and layout information for drawing text.
