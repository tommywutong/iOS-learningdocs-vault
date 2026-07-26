---
title: 'preferredFont(forTextStyle:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifont/preferredfont(fortextstyle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifont/preferredfont(fortextstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/preferredfont%28fortextstyle%3A%29.json'
content_hash: 'sha256:d42547121d32f6a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# preferredFont(forTextStyle:)

<sub>Type Method</sub>

Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func preferredFont(forTextStyle style: UIFont.TextStyle) -> UIFont
```

## Parameters

- `style` — The text style for which to return a font. See [TextStyle](textstyle.md) for recognized values.

## Return Value

The system font associated with the specified text style.

## Discussion

To create a styled font based on a custom font, use a [UIFontMetrics](../uifontmetrics.md) object.

Because fonts are immutable, any element that adjusts for an updated content size category does not modify the font itself. Instead, the element replaces the assigned font with a new instance based on the original settings.

## See Also

### Creating Fonts

- [Scaling fonts automatically](../scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](../creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [+ preferredFontForTextStyle:compatibleWithTraitCollection:](<preferredfont(fortextstyle_compatiblewith_).md>) — Returns an instance of the system font for the appropriate text style and traits.
- [TextStyle](textstyle.md) — Constants that describe the preferred styles for fonts.
- [+ fontWithName:size:](<init(name_size_).md>) — Creates and returns a font object for the specified font name and size.
- [+ fontWithDescriptor:size:](<init(descriptor_size_).md>) — Returns a font that matches the specified font descriptor.
- [- fontWithSize:](<withsize(__).md>) — Returns a font object that is the same as the font, but has the specified size.
