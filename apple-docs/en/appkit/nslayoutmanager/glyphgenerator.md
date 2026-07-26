---
title: glyphGenerator
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutmanager/glyphgenerator
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/glyphgenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/glyphgenerator.json'
content_hash: 'sha256:3722d534b4e1d843'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# glyphGenerator

<sub>Instance Property</sub>

The glyph generator that the layout manager uses.

<sub>macOS</sub>

```swift
var glyphGenerator: NSGlyphGenerator { get set }
```

## Discussion

Setting the glyph generator invalidates all glyphs and layout in the layout manager.

## See Also

### Causing glyph generation and layout

- [- ensureGlyphsForCharacterRange:](<ensureglyphs(forcharacterrange_).md>) — Forces the layout manager to generate glyphs for the specified character range if it hasn’t already.
- [- ensureGlyphsForGlyphRange:](<ensureglyphs(forglyphrange_).md>) — Forces the layout manager to generate glyphs for the specified glyph range if it hasn’t already.
- [- ensureLayoutForBoundingRect:inTextContainer:](<ensurelayout(forboundingrect_in_).md>) — Forces the layout manager to perform layout for the specified area in the specified text container if it hasn’t already.
- [- ensureLayoutForCharacterRange:](<ensurelayout(forcharacterrange_).md>) — Forces the layout manager to perform layout for the specified character range if it hasn’t already.
- [- ensureLayoutForGlyphRange:](<ensurelayout(forglyphrange_).md>) — Forces the layout manager to perform layout for the specified glyph range if it hasn’t already.
- [- ensureLayoutForTextContainer:](<ensurelayout(for_).md>) — Forces the layout manager to perform layout for the specified text container if it hasn’t already.
