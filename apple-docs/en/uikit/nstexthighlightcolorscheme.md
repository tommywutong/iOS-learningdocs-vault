---
title: NSTextHighlightColorScheme
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstexthighlightcolorscheme
source_url: 'https://developer.apple.com/documentation/uikit/nstexthighlightcolorscheme'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstexthighlightcolorscheme.json'
content_hash: 'sha256:2c7658c8489901c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextHighlightColorScheme

<sub>Type Alias</sub>

Constants that specify the highlight color to use with the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef NSString * NSTextHighlightColorScheme;
```

## Overview

Use an [NSTextHighlightColorScheme](nstexthighlightcolorscheme.md) structure as the value of the [NSTextHighlightColorSchemeAttributeName](nstexthighlightcolorschemeattributename.md) attribute. That attribute specifies which color to use when drawing the highlight on the text. This attribute specifies only the color option. To display the highlight itself, add the [NSTextHighlightStyleAttributeName](nstexthighlightstyleattributename.md) attribute to the text.

## Topics

### Getting the color schemes

- [NSTextHighlightColorSchemeDefault](nstexthighlightcolorschemedefault.md) — The default system highlight color.
- [NSTextHighlightColorSchemeBlue](nstexthighlightcolorschemeblue.md) — A blue highlight color.
- [NSTextHighlightColorSchemeMint](nstexthighlightcolorschememint.md) — A mint green highlight color.
- [NSTextHighlightColorSchemeOrange](nstexthighlightcolorschemeorange.md) — An orange highlight color.
- [NSTextHighlightColorSchemePink](nstexthighlightcolorschemepink.md) — A pink highlight color.
- [NSTextHighlightColorSchemePurple](nstexthighlightcolorschemepurple.md) — A purple highlight color.

## See Also

### Getting text content attributes

- [TextKit string attribute keys](textkit-string-attribute-keys.md) — UIKit-specific keys you use to apply attributes to ranges of characters in an attributed string.
- [NSTextHighlightStyle](nstexthighlightstyle.md) — Constants that specify the type of highlight to apply to text.
- [NSTextEffectStyle](nstexteffectstyle.md) — Constants for the type of effect to apply to the text.
- [NSUnderlineStyle](nsunderlinestyle.md) — Constants for the underline style and strikethrough style attribute keys.
- [NSWritingDirectionFormatType](nswritingdirectionformattype.md) — Constants for the writing direction attribute key.
