---
title: NSWritingDirectionAttributeName
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nswritingdirectionattributename
source_url: 'https://developer.apple.com/documentation/uikit/nswritingdirectionattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nswritingdirectionattributename.json'
content_hash: 'sha256:c82b21dcff942732'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSWritingDirectionAttributeName

<sub>Global Variable</sub>

The writing direction of the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringKey const NSWritingDirectionAttributeName;
```

## Overview

The value of this attribute is an [NSArray](../foundation/nsarray.md) object containing [NSNumber](../foundation/nsnumber.md) objects representing the nested levels of writing direction overrides, in order from outermost to innermost.

This attribute provides a means to override the default bidirectional text algorithm, equivalent to using the Unicode bidi control characters `LRE`, `RLE`, `LRO`, or `RLO` paired with `PDF`, but as a higher-level attribute. (See [Unicode Standard Annex #9](http://unicode.org/reports/tr9/) for information about the Unicode bidi formatting codes.) The `NSWritingDirectionAttributeName` constant is a character-level attribute that provides a higher-level alternative to the inclusion of explicit bidirectional control characters in text. It is the `NSAttributedString` equivalent of the HTML markup using the `bdo` element with the `dir` attribute.

The values of the `NSNumber` objects should be `0`, `1`, `2`, or `3`, for `LRE`, `RLE`, `LRO`, or `RLO` respectively, and combinations of [NSWritingDirectionLeftToRight](nswritingdirection/lefttoright.md) and [NSWritingDirectionRightToLeft](nswritingdirection/righttoleft.md) with [NSTextWritingDirectionEmbedding](nstextwritingdirection/embedding.md) or [NSTextWritingDirectionOverride](nstextwritingdirection/override.md), as shown in the following table.

| Array `NSNumber` Values | Unicode Control Characters | Writing Direction Constants |
|---|---|---|
| `0` | `LRE` | `NSWritingDirectionLeftToRight \| NSTextWritingDirectionEmbedding` |
| `1` | `RLE` | `NSWritingDirectionRightToLeft \| NSTextWritingDirectionEmbedding` |
| `2` | `LRO` | `NSWritingDirectionLeftToRight \| NSTextWritingDirectionOverride` |
| `3` | `RLO` | `NSWritingDirectionRightToLeft \| NSTextWritingDirectionOverride` |

## See Also

### Getting rendering attribute keys

- [NSBackgroundColorAttributeName](nsbackgroundcolorattributename.md) — The color of the background behind the text.
- [NSBaselineOffsetAttributeName](nsbaselineoffsetattributename.md) — The vertical offset for the position of the text.
- [NSFontAttributeName](nsfontattributename.md) — The font of the text.
- [NSForegroundColorAttributeName](nsforegroundcolorattributename.md) — The color of the text.
- [NSKernAttributeName](nskernattributename.md) — The kerning of the text.
- [NSLigatureAttributeName](nsligatureattributename.md) — The ligature of the text.
- [NSParagraphStyleAttributeName](nsparagraphstyleattributename.md) — The paragraph style of the text.
- [NSStrikethroughColorAttributeName](nsstrikethroughcolorattributename.md) — The color of the strikethrough.
- [NSStrikethroughStyleAttributeName](nsstrikethroughstyleattributename.md) — The strikethrough style of the text.
- [NSStrokeColorAttributeName](nsstrokecolorattributename.md) — The color of the stroke.
- [NSStrokeWidthAttributeName](nsstrokewidthattributename.md) — The width of the stroke.
- [NSTrackingAttributeName](nstrackingattributename.md) — The amount to modify the default tracking.
- [NSUnderlineColorAttributeName](nsunderlinecolorattributename.md) — The color of the underline.
- [NSUnderlineStyleAttributeName](nsunderlinestyleattributename.md) — The underline style of the text.
