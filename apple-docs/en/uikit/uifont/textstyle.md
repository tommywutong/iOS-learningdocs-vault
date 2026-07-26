---
title: UIFont.TextStyle
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 3.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifont/textstyle
source_url: 'https://developer.apple.com/documentation/uikit/uifont/textstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifont/textstyle.json'
content_hash: 'sha256:e99f9e564671da42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFont](../uifont.md)

# UIFont.TextStyle

<sub>Structure</sub>

Constants that describe the preferred styles for fonts.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct TextStyle
```

## Overview

Pass these constants to the [+ preferredFontForTextStyle:](<preferredfont(fortextstyle_).md>) method of [UIFont](../uifont.md) or the [+ preferredFontDescriptorWithTextStyle:](<../uifontdescriptor/preferredfontdescriptor(withtextstyle_).md>) method of [UIFontDescriptor](../uifontdescriptor.md) to retrieve the corresponding font information.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIFontTextStyleBody](textstyle/body.md) — The font for body text.
- [UIFontTextStyleCallout](textstyle/callout.md) — The font for callouts.
- [UIFontTextStyleCaption1](textstyle/caption1.md) — The font for standard captions.
- [UIFontTextStyleCaption2](textstyle/caption2.md) — The font for alternate captions.
- [UIFontTextStyleFootnote](textstyle/footnote.md) — The font for footnotes.
- [UIFontTextStyleHeadline](textstyle/headline.md) — The font for headings.
- [UIFontTextStyleSubheadline](textstyle/subheadline.md) — The font for subheadings.
- [UIFontTextStyleLargeTitle](textstyle/largetitle.md) — The font style for large titles.
- [UIFontTextStyleExtraLargeTitle](textstyle/extralargetitle.md) — The font style for extra large titles.
- [UIFontTextStyleExtraLargeTitle2](textstyle/extralargetitle2.md) — The font style for extra extra large titles.
- [UIFontTextStyleTitle1](textstyle/title1.md) — The font for first-level hierarchical headings.
- [UIFontTextStyleTitle2](textstyle/title2.md) — The font for second-level hierarchical headings.
- [UIFontTextStyleTitle3](textstyle/title3.md) — The font for third-level hierarchical headings.

### Metrics

- [metrics](textstyle/metrics.md) — The corresponding font metrics object for the text style.

### Initializers

- [init(rawValue:)](<textstyle/init(rawvalue_).md>) — Creates a text style with the specified raw value.

## See Also

### Creating Fonts

- [Scaling fonts automatically](../scaling-fonts-automatically.md) — Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](../creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [+ preferredFontForTextStyle:](<preferredfont(fortextstyle_).md>) — Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [+ preferredFontForTextStyle:compatibleWithTraitCollection:](<preferredfont(fortextstyle_compatiblewith_).md>) — Returns an instance of the system font for the appropriate text style and traits.
- [+ fontWithName:size:](<init(name_size_).md>) — Creates and returns a font object for the specified font name and size.
- [+ fontWithDescriptor:size:](<init(descriptor_size_).md>) — Returns a font that matches the specified font descriptor.
- [- fontWithSize:](<withsize(__).md>) — Returns a font object that is the same as the font, but has the specified size.
