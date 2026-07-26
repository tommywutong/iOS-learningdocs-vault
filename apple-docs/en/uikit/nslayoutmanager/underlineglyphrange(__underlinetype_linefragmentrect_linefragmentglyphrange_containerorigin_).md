---
title: 'underlineGlyphRange(_:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/underlineglyphrange(_:underlinetype:linefragmentrect:linefragmentglyphrange:containerorigin:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/underlineglyphrange(_:underlinetype:linefragmentrect:linefragmentglyphrange:containerorigin:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/underlineglyphrange%28_%3Aunderlinetype%3Alinefragmentrect%3Alinefragmentglyphrange%3Acontainerorigin%3A%29.json'
content_hash: 'sha256:b29c9d8f395f6dcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# underlineGlyphRange(_:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:)

<sub>Instance Method</sub>

Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func underlineGlyphRange(_ glyphRange: NSRange, underlineType underlineVal: NSUnderlineStyle, lineFragmentRect lineRect: CGRect, lineFragmentGlyphRange lineGlyphRange: NSRange, containerOrigin: CGPoint)
```

## Parameters

- `glyphRange` — A range of glyphs, which must belong to a single line fragment rectangle (as returned by [- lineFragmentRectForGlyphAtIndex:effectiveRange:](<linefragmentrect(forglyphat_effectiverange_).md>)).

- `underlineVal` — The style of underlining to draw. This value is a mask derived from the value for [NSUnderlineStyleAttributeName](../nsunderlinestyleattributename.md)—for example, `(NSUnderlinePatternDash | NSUnderlineStyleThick | NSUnderlineByWordMask)`. Subclasses can define custom underlining styles.

- `lineRect` — The line fragment rectangle containing the glyphs to draw underlining for.

- `lineGlyphRange` — The range of all glyphs within that line fragment rectangle.

- `containerOrigin` — The origin of the line fragment rectangle’s `NSTextContainer` in its `NSTextView`.

## Discussion

This method determines which glyphs actually need to be underlined based on `underlineVal`. With `NSUnderlineStyleSingle`, for example, leading and trailing whitespace isn’t underlined, but whitespace between visible glyphs is. A potential word-underline style would omit underlining on any whitespace. After determining which glyphs to draw underlining on, this method invokes [- drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawunderline(forglyphrange_underlinetype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) for each contiguous range of glyphs that requires it.

## See Also

### Drawing

- [- drawBackgroundForGlyphRange:atPoint:](<drawbackground(forglyphrange_at_).md>) — Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [- drawGlyphsForGlyphRange:atPoint:](<drawglyphs(forglyphrange_at_).md>) — Draws the specified glyphs, which must lie completely within a single text container.
- [- drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawstrikethrough(forglyphrange_strikethroughtype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws a strikethrough for the specified glyphs.
- [- drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawunderline(forglyphrange_underlinetype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws underlining for the glyphs in a specified range.
- [- fillBackgroundRectArray:count:forCharacterRange:color:](<fillbackgroundrectarray(__count_forcharacterrange_color_).md>) — Fills background rectangles with a color.
- [- showCGGlyphs:positions:count:font:textMatrix:attributes:inContext:](<showcgglyphs(__positions_count_font_textmatrix_attributes_in_).md>) — Renders the glyphs at the specified positions, using the specified attributes.
- [- strikethroughGlyphRange:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<strikethroughglyphrange(__strikethroughtype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates and draws strikethrough for the specified glyphs.
