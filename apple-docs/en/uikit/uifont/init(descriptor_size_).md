---
title: 'init(descriptor:size:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifont/init(descriptor:size:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifont/init(descriptor:size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/init%28descriptor%3Asize%3A%29.json'
content_hash: 'sha256:ceb7ee655ae0055c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# init(descriptor:size:)

<sub>Initializer</sub>

Returns a font that matches the specified font descriptor.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(descriptor: UIFontDescriptor, size pointSize: CGFloat)
```

## Parameters

- `descriptor` — The font descriptor to match.

- `pointSize` — The size in points to which the font is scaled. If greater than 0.0, it has precedence over `UIFontDescriptorSizeAttribute` in `descriptor`.

## Return Value

A font object for the specified descriptor and size.

## Discussion

In most cases, you can simply use [+ fontWithName:size:](<init(name_size_).md>) to create standard scaled fonts.

## See Also

### Creating Fonts

- [Scaling fonts automatically](../scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](../creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [+ preferredFontForTextStyle:](<preferredfont(fortextstyle_).md>) — Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [+ preferredFontForTextStyle:compatibleWithTraitCollection:](<preferredfont(fortextstyle_compatiblewith_).md>) — Returns an instance of the system font for the appropriate text style and traits.
- [TextStyle](textstyle.md) — Constants that describe the preferred styles for fonts.
- [+ fontWithName:size:](<init(name_size_).md>) — Creates and returns a font object for the specified font name and size.
- [- fontWithSize:](<withsize(__).md>) — Returns a font object that is the same as the font, but has the specified size.
