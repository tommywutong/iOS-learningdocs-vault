---
title: 'ensureGlyphs(forGlyphRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/ensureglyphs(forglyphrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/ensureglyphs(forglyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/ensureglyphs%28forglyphrange%3A%29.json'
content_hash: 'sha256:b93ca242bdeaf748'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# ensureGlyphs(forGlyphRange:)

<sub>Instance Method</sub>

Forces the layout manager to generate glyphs for the specified glyph range if it hasn’t already.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func ensureGlyphs(forGlyphRange glyphRange: NSRange)
```

## Parameters

- `glyphRange` — The glyph range for which glyphs are generated.

## Discussion

The layout manager reserves the right to perform glyph generation for larger ranges. If noncontiguous layout is disabled, then the affected range is always effectively extended to start at the beginning of the text.

## See Also

### Causing glyph generation and layout

- [- ensureGlyphsForCharacterRange:](<ensureglyphs(forcharacterrange_).md>) — Forces the layout manager to generate glyphs for the specified character range if it hasn’t already.
- [- ensureLayoutForBoundingRect:inTextContainer:](<ensurelayout(forboundingrect_in_).md>) — Forces the layout manager to perform layout for the specified area in the specified text container if it hasn’t already.
- [- ensureLayoutForCharacterRange:](<ensurelayout(forcharacterrange_).md>) — Forces the layout manager to perform layout for the specified character range if it hasn’t already.
- [- ensureLayoutForGlyphRange:](<ensurelayout(forglyphrange_).md>) — Forces the layout manager to perform layout for the specified glyph range if it hasn’t already.
- [- ensureLayoutForTextContainer:](<ensurelayout(for_).md>) — Forces the layout manager to perform layout for the specified text container if it hasn’t already.
- [glyphGenerator](../../appkit/nslayoutmanager/glyphgenerator.md) — The glyph generator that the layout manager uses.
