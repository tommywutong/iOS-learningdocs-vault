---
title: 'preferredFontDescriptor(withTextStyle:compatibleWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontdescriptor/preferredfontdescriptor(withtextstyle:compatiblewith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/preferredfontdescriptor(withtextstyle:compatiblewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/preferredfontdescriptor%28withtextstyle%3Acompatiblewith%3A%29.json'
content_hash: 'sha256:03d15a1362a99e73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# preferredFontDescriptor(withTextStyle:compatibleWith:)

<sub>Type Method</sub>

Returns a font descriptor that contains the text style and the content size category that the provided trait collection specifies.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func preferredFontDescriptor(withTextStyle style: UIFont.TextStyle, compatibleWith traitCollection: UITraitCollection?) -> UIFontDescriptor
```

## Parameters

- `style` — The text style for which to return a font descriptor.

- `traitCollection` — The trait collection containing the content size category information.

## Return Value

The new font descriptor.

## See Also

### Creating a font descriptor

- [+ preferredFontDescriptorWithTextStyle:](<preferredfontdescriptor(withtextstyle_).md>) — Returns a font descriptor that contains the specified text style and the user’s selected content size category.
- [+ fontDescriptorWithName:matrix:](<init(name_matrix_).md>) — Returns a font descriptor with the specified values for the name and matrix dictionary attributes.
- [+ fontDescriptorWithName:size:](<init(name_size_).md>) — Returns a font descriptor with the specified values for the name and size dictionary attributes.
- [- fontDescriptorByAddingAttributes:](<addingattributes(__).md>) — Returns a new font descriptor that’s the same as the existing descriptor, but with the specified attributes taking precedence over the existing ones.
- [- fontDescriptorWithDesign:](<withdesign(__).md>) — Returns a new font descriptor that’s the same as the existing descriptor, but with the specified design.
- [- fontDescriptorWithFamily:](<withfamily(__).md>) — Returns a new font descriptor whose attributes are the same as the existing font descriptor, but from the specified family.
- [- fontDescriptorWithFace:](<withface(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified face.
- [- fontDescriptorWithMatrix:](<withmatrix(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified matrix.
- [- fontDescriptorWithSize:](<withsize(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified point size.
- [- fontDescriptorWithSymbolicTraits:](<withsymbolictraits(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified symbolic traits.
