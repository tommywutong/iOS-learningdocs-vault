---
title: 'preferredFont(forTextStyle:compatibleWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifont/preferredfont(fortextstyle:compatiblewith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifont/preferredfont(fortextstyle:compatiblewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/preferredfont%28fortextstyle%3Acompatiblewith%3A%29.json'
content_hash: 'sha256:91d40d274e028b93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# preferredFont(forTextStyle:compatibleWith:)

<sub>Type Method</sub>

Returns an instance of the system font for the appropriate text style and traits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func preferredFont(forTextStyle style: UIFont.TextStyle, compatibleWith traitCollection: UITraitCollection?) -> UIFont
```

## Parameters

- `style` — The text style for which to return a font. See [TextStyle](textstyle.md) for recognized values.

- `traitCollection` — The traits to use when determining which font to return.

## Return Value

The system font associated with the specified text style and traits.

## Discussion

To create a styled font based on a custom font, use a [UIFontMetrics](../uifontmetrics.md) object.

Because fonts are immutable, any element that adjusts for an updated content size category does not modify the font itself. Instead, the element replaces the assigned font with a new instance based on the original settings.

## See Also

### Creating Fonts

- [Scaling fonts automatically](../scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](../creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [+ preferredFontForTextStyle:](<preferredfont(fortextstyle_).md>) — Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [TextStyle](textstyle.md) — Constants that describe the preferred styles for fonts.
- [+ fontWithName:size:](<init(name_size_).md>) — Creates and returns a font object for the specified font name and size.
- [+ fontWithDescriptor:size:](<init(descriptor_size_).md>) — Returns a font that matches the specified font descriptor.
- [- fontWithSize:](<withsize(__).md>) — Returns a font object that is the same as the font, but has the specified size.
