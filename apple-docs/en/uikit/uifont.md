---
title: UIFont
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifont
source_url: 'https://developer.apple.com/documentation/uikit/uifont'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont.json'
content_hash: 'sha256:85c7481fa61ec697'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFont

<sub>Class</sub>

An object that provides access to the font’s characteristics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class UIFont
```

## Overview

Use `UIFont` to access your font’s characteristics within your app. It also provides the system with access to the glyph information, used during layout. Font objects are immutable, so it’s safe to use them from multiple threads in your app.

In Objective-C, don’t create font objects using the `alloc` and `init` methods. Instead, use class methods of [UIFont](uifont.md), such as [+ preferredFontForTextStyle:](<uifont/preferredfont(fortextstyle_).md>), to look up and retrieve the desired font object. These methods check for an existing font object with the specified characteristics and return it if it exists. Otherwise, they create a new font object based on the desired font characteristics.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Fonts

- [Scaling fonts automatically](scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [+ preferredFontForTextStyle:](<uifont/preferredfont(fortextstyle_).md>) — Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [+ preferredFontForTextStyle:compatibleWithTraitCollection:](<uifont/preferredfont(fortextstyle_compatiblewith_).md>) — Returns an instance of the system font for the appropriate text style and traits.
- [TextStyle](uifont/textstyle.md) — Constants that describe the preferred styles for fonts.
- [+ fontWithName:size:](<uifont/init(name_size_).md>) — Creates and returns a font object for the specified font name and size.
- [+ fontWithDescriptor:size:](<uifont/init(descriptor_size_).md>) — Returns a font that matches the specified font descriptor.
- [- fontWithSize:](<uifont/withsize(__).md>) — Returns a font object that is the same as the font, but has the specified size.

### Creating System Fonts

- [+ systemFontOfSize:](<uifont/systemfont(ofsize_).md>) — Returns the font object for standard interface items in the specified size.
- [+ systemFontOfSize:weight:](<uifont/systemfont(ofsize_weight_).md>) — Returns the font object for standard interface items in the specified size and weight.
- [Weight](uifont/weight.md) — Constants that represent standard typeface styles.
- [+ systemFontOfSize:weight:width:](<uifont/systemfont(ofsize_weight_width_).md>)
- [Width](uifont/width.md)
- [+ boldSystemFontOfSize:](<uifont/boldsystemfont(ofsize_).md>) — Returns the font object for standard interface items in boldface type in the specified size.
- [+ italicSystemFontOfSize:](<uifont/italicsystemfont(ofsize_).md>) — Returns the font object for standard interface items in italic type in the specified size.
- [+ monospacedSystemFontOfSize:weight:](<uifont/monospacedsystemfont(ofsize_weight_).md>) — Returns the fixed-width font for standard interface text in the specified size.
- [+ monospacedDigitSystemFontOfSize:weight:](<uifont/monospaceddigitsystemfont(ofsize_weight_).md>) — Returns the standard system font with all digits of consistent width.

### Getting the Available Font Names

- [familyNames](uifont/familynames.md) — Returns an array of font family names available on the system.
- [+ fontNamesForFamilyName:](<uifont/fontnames(forfamilyname_).md>) — Returns an array of font names available in a particular font family.

### Getting Font Name Attributes

- [familyName](uifont/familyname.md) — The font family name.
- [fontName](uifont/fontname.md) — The font face name.

### Getting Font Metrics

- [pointSize](uifont/pointsize.md) — The font’s point size, or the effective vertical point size for a font with a nonstandard matrix.
- [ascender](uifont/ascender.md) — The top y-coordinate, offset from the baseline, of the font’s longest ascender.
- [descender](uifont/descender.md) — The bottom y-coordinate, offset from the baseline, of the font’s longest descender.
- [leading](uifont/leading.md) — The font’s leading information.
- [capHeight](uifont/capheight.md) — The font’s cap height information.
- [xHeight](uifont/xheight.md) — The x-height of the font.
- [lineHeight](uifont/lineheight.md) — The height, in points, of text lines.

### Getting System Font Information

- [labelFontSize](uifont/labelfontsize.md) — The standard font size, in points, for labels.
- [buttonFontSize](uifont/buttonfontsize.md) — The standard font size, in points, for buttons.
- [smallSystemFontSize](uifont/smallsystemfontsize.md) — The size, in points, of the standard small system font.
- [systemFontSize](uifont/systemfontsize.md) — The size, in points, of the standard system font.

### Getting Font Descriptors

- [fontDescriptor](uifont/fontdescriptor.md) — A font descriptor for the font.
- [UIFontDescriptor](uifontdescriptor.md) — A collection of attributes that describes a font.

### Initializers

- [init(coder:)](<uifont/init(coder_).md>)

## See Also

### Fonts

- [Scaling fonts automatically](scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Adding a custom font to your app](adding-a-custom-font-to-your-app.md) — Add a custom font to your app and use it in your app’s interface.
- [UIFontDescriptor](uifontdescriptor.md) — A collection of attributes that describes a font.
- [SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.
- [UIFontMetrics](uifontmetrics.md) — A utility object for obtaining custom fonts that scale to support Dynamic Type.
