---
title: 'init(name:matrix:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontdescriptor/init(name:matrix:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/init(name:matrix:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/init%28name%3Amatrix%3A%29.json'
content_hash: 'sha256:ab9fcc520a3a0864'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# init(name:matrix:)

<sub>Initializer</sub>

Returns a font descriptor with the specified values for the name and matrix dictionary attributes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(name fontName: String, matrix: CGAffineTransform)
```

## Parameters

- `fontName` — The value for [UIFontDescriptorNameAttribute](attributename/name.md).

- `matrix` — The value for [UIFontDescriptorMatrixAttribute](attributename/matrix.md).

## Return Value

The new font descriptor.

## See Also

### Creating a font descriptor

- [+ preferredFontDescriptorWithTextStyle:](<preferredfontdescriptor(withtextstyle_).md>) — Returns a font descriptor that contains the specified text style and the user’s selected content size category.
- [+ preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:](<preferredfontdescriptor(withtextstyle_compatiblewith_).md>) — Returns a font descriptor that contains the text style and the content size category that the provided trait collection specifies.
- [+ fontDescriptorWithName:size:](<init(name_size_).md>) — Returns a font descriptor with the specified values for the name and size dictionary attributes.
- [- fontDescriptorByAddingAttributes:](<addingattributes(__).md>) — Returns a new font descriptor that’s the same as the existing descriptor, but with the specified attributes taking precedence over the existing ones.
- [- fontDescriptorWithDesign:](<withdesign(__).md>) — Returns a new font descriptor that’s the same as the existing descriptor, but with the specified design.
- [- fontDescriptorWithFamily:](<withfamily(__).md>) — Returns a new font descriptor whose attributes are the same as the existing font descriptor, but from the specified family.
- [- fontDescriptorWithFace:](<withface(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified face.
- [- fontDescriptorWithMatrix:](<withmatrix(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified matrix.
- [- fontDescriptorWithSize:](<withsize(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified point size.
- [- fontDescriptorWithSymbolicTraits:](<withsymbolictraits(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified symbolic traits.
