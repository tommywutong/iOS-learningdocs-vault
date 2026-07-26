---
title: 'withSize(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifont/withsize(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifont/withsize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/withsize%28_%3A%29.json'
content_hash: 'sha256:9d263d05d725f833'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# withSize(_:)

<sub>Instance Method</sub>

Returns a font object that is the same as the font, but has the specified size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func withSize(_ fontSize: CGFloat) -> UIFont
```

## Parameters

- `fontSize` — The desired size (in points) of the new font object. This value must be greater than 0.0.

## Return Value

A font object of the specified size.

## See Also

### Creating Fonts

- [Scaling fonts automatically](../scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](../creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [+ preferredFontForTextStyle:](<preferredfont(fortextstyle_).md>) — Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [+ preferredFontForTextStyle:compatibleWithTraitCollection:](<preferredfont(fortextstyle_compatiblewith_).md>) — Returns an instance of the system font for the appropriate text style and traits.
- [TextStyle](textstyle.md) — Constants that describe the preferred styles for fonts.
- [+ fontWithName:size:](<init(name_size_).md>) — Creates and returns a font object for the specified font name and size.
- [+ fontWithDescriptor:size:](<init(descriptor_size_).md>) — Returns a font that matches the specified font descriptor.
