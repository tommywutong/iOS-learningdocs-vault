---
title: 'ensureLayout(forBoundingRect:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/ensurelayout(forboundingrect:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/ensurelayout(forboundingrect:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/ensurelayout%28forboundingrect%3Ain%3A%29.json'
content_hash: 'sha256:0d97f69c4d695573'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# ensureLayout(forBoundingRect:in:)

<sub>Instance Method</sub>

Forces the layout manager to perform layout for the specified area in the specified text container if it hasn’t already.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func ensureLayout(forBoundingRect bounds: CGRect, in container: NSTextContainer)
```

## Parameters

- `bounds` — The area for which layout is performed.

- `container` — The text container containing the area for which layout is performed.

## Discussion

The layout manager reserves the right to perform layout for larger ranges. If noncontiguous layout is disabled, then the affected range is always effectively extended to start at the beginning of the text.

## See Also

### Causing glyph generation and layout

- [- ensureGlyphsForCharacterRange:](<ensureglyphs(forcharacterrange_).md>) — Forces the layout manager to generate glyphs for the specified character range if it hasn’t already.
- [- ensureGlyphsForGlyphRange:](<ensureglyphs(forglyphrange_).md>) — Forces the layout manager to generate glyphs for the specified glyph range if it hasn’t already.
- [- ensureLayoutForCharacterRange:](<ensurelayout(forcharacterrange_).md>) — Forces the layout manager to perform layout for the specified character range if it hasn’t already.
- [- ensureLayoutForGlyphRange:](<ensurelayout(forglyphrange_).md>) — Forces the layout manager to perform layout for the specified glyph range if it hasn’t already.
- [- ensureLayoutForTextContainer:](<ensurelayout(for_).md>) — Forces the layout manager to perform layout for the specified text container if it hasn’t already.
- [glyphGenerator](../../appkit/nslayoutmanager/glyphgenerator.md) — The glyph generator that the layout manager uses.
