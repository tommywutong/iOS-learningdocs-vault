---
title: 'ensureLayout(forGlyphRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/ensurelayout(forglyphrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/ensurelayout(forglyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/ensurelayout%28forglyphrange%3A%29.json'
content_hash: 'sha256:e5520f38b8bc2ddb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# ensureLayout(forGlyphRange:)

<sub>Instance Method</sub>

Forces the layout manager to perform layout for the specified glyph range if it hasn’t already.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func ensureLayout(forGlyphRange glyphRange: NSRange)
```

## Parameters

- `glyphRange` — The glyph range for which layout is performed.

## Discussion

The layout manager reserves the right to perform layout for larger ranges. If noncontiguous layout is disabled, then the affected range is always effectively extended to start at the beginning of the text.

## See Also

### Causing glyph generation and layout

- [- ensureGlyphsForCharacterRange:](<ensureglyphs(forcharacterrange_).md>) — Forces the layout manager to generate glyphs for the specified character range if it hasn’t already.
- [- ensureGlyphsForGlyphRange:](<ensureglyphs(forglyphrange_).md>) — Forces the layout manager to generate glyphs for the specified glyph range if it hasn’t already.
- [- ensureLayoutForBoundingRect:inTextContainer:](<ensurelayout(forboundingrect_in_).md>) — Forces the layout manager to perform layout for the specified area in the specified text container if it hasn’t already.
- [- ensureLayoutForCharacterRange:](<ensurelayout(forcharacterrange_).md>) — Forces the layout manager to perform layout for the specified character range if it hasn’t already.
- [- ensureLayoutForTextContainer:](<ensurelayout(for_).md>) — Forces the layout manager to perform layout for the specified text container if it hasn’t already.
- [glyphGenerator](../../appkit/nslayoutmanager/glyphgenerator.md) — The glyph generator that the layout manager uses.
