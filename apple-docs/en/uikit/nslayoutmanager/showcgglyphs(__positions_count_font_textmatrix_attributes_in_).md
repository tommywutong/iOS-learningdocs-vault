---
title: 'showCGGlyphs(_:positions:count:font:textMatrix:attributes:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/showcgglyphs(_:positions:count:font:textmatrix:attributes:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/showcgglyphs(_:positions:count:font:textmatrix:attributes:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/showcgglyphs%28_%3Apositions%3Acount%3Afont%3Atextmatrix%3Aattributes%3Ain%3A%29.json'
content_hash: 'sha256:ba243aa21c48a215'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# showCGGlyphs(_:positions:count:font:textMatrix:attributes:in:)

<sub>Instance Method</sub>

Renders the glyphs at the specified positions, using the specified attributes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func showCGGlyphs(_ glyphs: UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count glyphCount: Int, font: UIFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any] = [:], in CGContext: CGContext)
```

## Parameters

- `glyphs` — The glyphs to draw, which may include embedded `NULL` bytes.

- `positions` — The positions at which to draw the glyphs in the user space coordinate system.

- `glyphCount` — The number of glyphs to draw.

- `font` — The font to apply to the graphics state. This value can be different from the [NSFontAttributeName](../nsfontattributename.md) value in the `attributes` argument because of various font substitutions that the system automatically executes.

- `textMatrix` — The affine transform mapping the text space coordinate system to the user space coordinate system. The `tx` and `ty` components of `textMatrix` are ignored because Quartz overrides them with the glyph positions.

- `attributes` — A dictionary of glyph attributes. For a list of possible keys and values, see [Glyph Attributes](../../appkit/glyph-attributes.md).

- `CGContext` — A graphics context object already configured with the information in the `font`, `textMatrix`, and `attributes` parameters

## Discussion

The layout manager calls this primitive method when it is time to lay out a set of glyphs in the specified graphics context.

## See Also

### Drawing

- [- drawBackgroundForGlyphRange:atPoint:](<drawbackground(forglyphrange_at_).md>) — Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [- drawGlyphsForGlyphRange:atPoint:](<drawglyphs(forglyphrange_at_).md>) — Draws the specified glyphs, which must lie completely within a single text container.
- [- drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawstrikethrough(forglyphrange_strikethroughtype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws a strikethrough for the specified glyphs.
- [- drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawunderline(forglyphrange_underlinetype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws underlining for the glyphs in a specified range.
- [- fillBackgroundRectArray:count:forCharacterRange:color:](<fillbackgroundrectarray(__count_forcharacterrange_color_).md>) — Fills background rectangles with a color.
- [- strikethroughGlyphRange:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<strikethroughglyphrange(__strikethroughtype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates and draws strikethrough for the specified glyphs.
- [- underlineGlyphRange:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<underlineglyphrange(__underlinetype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.
