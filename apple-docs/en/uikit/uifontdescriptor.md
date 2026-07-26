---
title: UIFontDescriptor
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor.json'
content_hash: 'sha256:03a104273dccedcb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFontDescriptor

<sub>Class</sub>

A collection of attributes that describes a font.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class UIFontDescriptor
```

## Overview

A font descriptor can be used to create or modify a [UIFont](uifont.md) object. Font descriptors have a font matching capability, so that you can partially describe a font by creating a font descriptor with, for example, just a family name. You can use [- matchingFontDescriptorsWithMandatoryKeys:](<uifontdescriptor/matchingfontdescriptors(withmandatorykeys_).md>) to find all the available fonts in the system with a matching family name. Font descriptors can also be archived and unarchived.

There are several ways to create a new [UIFontDescriptor](uifontdescriptor.md) object. To take advantage of text styles and respect the user’s current content size category, use [+ preferredFontDescriptorWithTextStyle:](<uifontdescriptor/preferredfontdescriptor(withtextstyle_).md>). You can also use `alloc` and [- initWithFontAttributes:](<uifontdescriptor/init(fontattributes_).md>), [fontDescriptorWithFontAttributes:](uifontdescriptor/fontdescriptorwithfontattributes_.md), [+ fontDescriptorWithName:matrix:](<uifontdescriptor/init(name_matrix_).md>), or [+ fontDescriptorWithName:size:](<uifontdescriptor/init(name_size_).md>) to create a font descriptor based on your custom attributes dictionary or on a specific font’s name and size. Alternatively you can use one of the `fontDescriptor…` instance methods (such as [- fontDescriptorWithFace:](<uifontdescriptor/withface(__).md>)) to create a modified version of an existing descriptor. The latter methods are useful if you have an existing descriptor and simply want to change one aspect.

All attributes in the attributes dictionary are optional.

For design guidance, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/typography/).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a font descriptor

- [+ preferredFontDescriptorWithTextStyle:](<uifontdescriptor/preferredfontdescriptor(withtextstyle_).md>) — Returns a font descriptor that contains the specified text style and the user’s selected content size category.
- [+ preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:](<uifontdescriptor/preferredfontdescriptor(withtextstyle_compatiblewith_).md>) — Returns a font descriptor that contains the text style and the content size category that the provided trait collection specifies.
- [+ fontDescriptorWithName:matrix:](<uifontdescriptor/init(name_matrix_).md>) — Returns a font descriptor with the specified values for the name and matrix dictionary attributes.
- [+ fontDescriptorWithName:size:](<uifontdescriptor/init(name_size_).md>) — Returns a font descriptor with the specified values for the name and size dictionary attributes.
- [- fontDescriptorByAddingAttributes:](<uifontdescriptor/addingattributes(__).md>) — Returns a new font descriptor that’s the same as the existing descriptor, but with the specified attributes taking precedence over the existing ones.
- [- fontDescriptorWithDesign:](<uifontdescriptor/withdesign(__).md>) — Returns a new font descriptor that’s the same as the existing descriptor, but with the specified design.
- [- fontDescriptorWithFamily:](<uifontdescriptor/withfamily(__).md>) — Returns a new font descriptor whose attributes are the same as the existing font descriptor, but from the specified family.
- [- fontDescriptorWithFace:](<uifontdescriptor/withface(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified face.
- [- fontDescriptorWithMatrix:](<uifontdescriptor/withmatrix(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified matrix.
- [- fontDescriptorWithSize:](<uifontdescriptor/withsize(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified point size.
- [- fontDescriptorWithSymbolicTraits:](<uifontdescriptor/withsymbolictraits(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified symbolic traits.

### Initializing a font descriptor

- [- initWithFontAttributes:](<uifontdescriptor/init(fontattributes_).md>) — Creates a font descriptor with the specified attributes.
- [- init](<uifontdescriptor/init().md>) — Creates a font descriptor.
- [- initWithCoder:](<uifontdescriptor/init(coder_).md>) — Creates a font descriptor from data in an unarchiver.

### Finding fonts

- [- matchingFontDescriptorsWithMandatoryKeys:](<uifontdescriptor/matchingfontdescriptors(withmandatorykeys_).md>) — Returns all the fonts available in the system with specified attributes that match those of the font.

### Querying a font descriptor

- [fontAttributes](uifontdescriptor/fontattributes.md) — The font descriptor’s dictionary of attributes.
- [matrix](uifontdescriptor/matrix.md) — The current transform matrix of the font descriptor.
- [- objectForKey:](<uifontdescriptor/object(forkey_).md>) — Returns the font attribute that the corresponding key specifies.
- [pointSize](uifontdescriptor/pointsize.md) — The point size of the font descriptor.
- [postscriptName](uifontdescriptor/postscriptname.md) — The PostScript name of the font descriptor.
- [symbolicTraits](uifontdescriptor/symbolictraits-swift.property.md) — The traits of the font descriptor.
- [SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.

### Constants

- [TextStyle](uifont/textstyle.md) — Constants that describe the preferred styles for fonts.
- [SystemDesign](uifontdescriptor/systemdesign.md) — Constants that describe the system-defined typeface designs.
- [SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.
- [Class](uifontdescriptor/class.md) — Constants that classify certain stylistic qualities of the font.
- [AttributeName](uifontdescriptor/attributename.md) — Constants that describe font attributes.
- [FeatureKey](uifontdescriptor/featurekey.md) — Keys for retrieving feature settings.
- [TraitKey](uifontdescriptor/traitkey.md) — Keys for retrieving the font descriptor’s trait information.
- [Weight](uifont/weight.md) — Constants that represent standard typeface styles.
- [Width](uifont/width.md)

## See Also

### Fonts

- [Scaling fonts automatically](scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Adding a custom font to your app](adding-a-custom-font-to-your-app.md) — Add a custom font to your app and use it in your app’s interface.
- [UIFont](uifont.md) — An object that provides access to the font’s characteristics.
- [SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md) — Constants that describe the stylistic aspects of a font.
- [UIFontMetrics](uifontmetrics.md) — A utility object for obtaining custom fonts that scale to support Dynamic Type.
