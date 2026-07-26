---
title: 'withSize(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontdescriptor/withsize(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/withsize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/withsize%28_%3A%29.json'
content_hash: 'sha256:42286fbf82fada63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# withSize(_:)

<sub>Instance Method</sub>

Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified point size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func withSize(_ newPointSize: CGFloat) -> UIFontDescriptor
```

## Parameters

- `newPointSize` — The new point size.

## Return Value

The new font descriptor.

## See Also

### Creating a font descriptor

- [+ preferredFontDescriptorWithTextStyle:](<preferredfontdescriptor(withtextstyle_).md>) — Returns a font descriptor that contains the specified text style and the user’s selected content size category.
- [+ preferredFontDescriptorWithTextStyle:compatibleWithTraitCollection:](<preferredfontdescriptor(withtextstyle_compatiblewith_).md>) — Returns a font descriptor that contains the text style and the content size category that the provided trait collection specifies.
- [+ fontDescriptorWithName:matrix:](<init(name_matrix_).md>) — Returns a font descriptor with the specified values for the name and matrix dictionary attributes.
- [+ fontDescriptorWithName:size:](<init(name_size_).md>) — Returns a font descriptor with the specified values for the name and size dictionary attributes.
- [- fontDescriptorByAddingAttributes:](<addingattributes(__).md>) — Returns a new font descriptor that’s the same as the existing descriptor, but with the specified attributes taking precedence over the existing ones.
- [- fontDescriptorWithDesign:](<withdesign(__).md>) — Returns a new font descriptor that’s the same as the existing descriptor, but with the specified design.
- [- fontDescriptorWithFamily:](<withfamily(__).md>) — Returns a new font descriptor whose attributes are the same as the existing font descriptor, but from the specified family.
- [- fontDescriptorWithFace:](<withface(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified face.
- [- fontDescriptorWithMatrix:](<withmatrix(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified matrix.
- [- fontDescriptorWithSymbolicTraits:](<withsymbolictraits(__).md>) — Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified symbolic traits.
