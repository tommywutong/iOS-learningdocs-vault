---
title: 'withDesign(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 5.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontdescriptor/withdesign(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/withdesign(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/withdesign%28_%3A%29.json'
content_hash: 'sha256:be113f332aa987b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# withDesign(_:)

<sub>Instance Method</sub>

Returns a new font descriptor that’s the same as the existing descriptor, but with the specified design.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func withDesign(_ design: UIFontDescriptor.SystemDesign) -> UIFontDescriptor?
```

## Parameters

- `design` — The new system font design.

## Return Value

The new font descriptor, if the original font descriptor is from a system UI font; otherwise, `nil`.

## Discussion

This method changes the design of an existing font descriptor that describes a system UI font — for example, a font descriptor created by methods such as [+ systemFontOfSize:](<../uifont/systemfont(ofsize_).md>), [+ preferredFontForTextStyle:](<../uifont/preferredfont(fortextstyle_).md>), or [+ preferredFontDescriptorWithTextStyle:](<preferredfontdescriptor(withtextstyle_).md>). If the original font descriptor doesn’t describe a system font, this method returns `nil`.

## See Also

### Creating a font descriptor

- [+ preferredFontDescriptorWithTextStyle:](<preferredfontdescriptor(withtextstyle_).md>) — Returns a font descriptor that contains the specified text style and the user’s selected content size category.
- [+ preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:](<preferredfontdescriptor(withtextstyle_compatiblewith_).md>) — Returns a font descriptor that contains the text style and the content size category that the provided trait collection specifies.
- [+ fontDescriptorWithName:matrix:](<init(name_matrix_).md>) — Returns a font descriptor with the specified values for the name and matrix dictionary attributes.
- [+ fontDescriptorWithName:size:](<init(name_size_).md>) — Returns a font descriptor with the specified values for the name and size dictionary attributes.
- [- fontDescriptorByAddingAttributes:](<addingattributes(__).md>) — Returns a new font descriptor that’s the same as the existing descriptor, but with the specified attributes taking precedence over the existing ones.
- [- fontDescriptorWithFamily:](<withfamily(__).md>) — Returns a new font descriptor whose attributes are the same as the existing font descriptor, but from the specified family.
- [- fontDescriptorWithFace:](<withface(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified face.
- [- fontDescriptorWithMatrix:](<withmatrix(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified matrix.
- [- fontDescriptorWithSize:](<withsize(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified point size.
- [- fontDescriptorWithSymbolicTraits:](<withsymbolictraits(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified symbolic traits.
