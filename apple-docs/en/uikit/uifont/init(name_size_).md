---
title: 'init(name:size:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifont/init(name:size:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifont/init(name:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/init%28name%3Asize%3A%29.json'
content_hash: 'sha256:ee79db7d5bd86fc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# init(name:size:)

<sub>Initializer</sub>

Creates and returns a font object for the specified font name and size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init?(name fontName: String, size fontSize: CGFloat)
```

## Parameters

- `fontName` — The fully specified name of the font. This name incorporates both the font family name and the specific style information for the font.

- `fontSize` — The size (in points) to which the font is scaled. This value must be greater than 0.0.

## Return Value

A font object of the specified name and size.

## Discussion

You can use the [+ fontNamesForFamilyName:](<fontnames(forfamilyname_).md>) method to retrieve the specific font names for a given font family.

## See Also

### Related Documentation

- [familyNames](familynames.md) — Returns an array of font family names available on the system.
- [+ fontNamesForFamilyName:](<fontnames(forfamilyname_).md>) — Returns an array of font names available in a particular font family.

### Creating Fonts

- [Scaling fonts automatically](../scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](../creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [+ preferredFontForTextStyle:](<preferredfont(fortextstyle_).md>) — Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [+ preferredFontForTextStyle:compatibleWithTraitCollection:](<preferredfont(fortextstyle_compatiblewith_).md>) — Returns an instance of the system font for the appropriate text style and traits.
- [TextStyle](textstyle.md) — Constants that describe the preferred styles for fonts.
- [+ fontWithDescriptor:size:](<init(descriptor_size_).md>) — Returns a font that matches the specified font descriptor.
- [- fontWithSize:](<withsize(__).md>) — Returns a font object that is the same as the font, but has the specified size.
