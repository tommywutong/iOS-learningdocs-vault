---
title: 'drawGlyphs(forGlyphRange:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanager/drawglyphs(forglyphrange:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanager/drawglyphs(forglyphrange:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanager/drawglyphs%28forglyphrange%3Aat%3A%29.json'
content_hash: 'sha256:57cbfda4f8c15880'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManager](../nslayoutmanager.md)

# drawGlyphs(forGlyphRange:at:)

<sub>Instance Method</sub>

Draws the specified glyphs, which must lie completely within a single text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func drawGlyphs(forGlyphRange glyphsToShow: NSRange, at origin: CGPoint)
```

## Parameters

- `glyphsToShow` — The range of glyphs that are drawn.

- `origin` — The position of the text container in the coordinate system of the currently focused view.

## Discussion

This method is called by `NSTextView` for drawing. You can override it to perform additional drawing, or to replace text drawing entirely, but not to change layout. You can call this method directly, but focus must already be locked on the destination view or image. This method expects the coordinate system of the view to be flipped.

This method draws the actual glyphs, including attachments, as well as any underlines or strikethoughs.

Performs glyph generation and layout if needed.

## See Also

### Related Documentation

- [textContainerOrigin](../../appkit/nstextview/textcontainerorigin.md) — The origin of the receiver’s text container.
- [- glyphRangeForTextContainer:](<glyphrange(for_).md>) — Returns the range of glyphs lying within the specified text container.

### Drawing

- [- drawBackgroundForGlyphRange:atPoint:](<drawbackground(forglyphrange_at_).md>) — Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [- drawStrikethroughForGlyphRange:strikethroughType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawstrikethrough(forglyphrange_strikethroughtype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws a strikethrough for the specified glyphs.
- [- drawUnderlineForGlyphRange:underlineType:baselineOffset:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<drawunderline(forglyphrange_underlinetype_baselineoffset_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Draws underlining for the glyphs in a specified range.
- [- fillBackgroundRectArray:count:forCharacterRange:color:](<fillbackgroundrectarray(__count_forcharacterrange_color_).md>) — Fills background rectangles with a color.
- [- showCGGlyphs:positions:count:font:textMatrix:attributes:inContext:](<showcgglyphs(__positions_count_font_textmatrix_attributes_in_).md>) — Renders the glyphs at the specified positions, using the specified attributes.
- [- strikethroughGlyphRange:strikethroughType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<strikethroughglyphrange(__strikethroughtype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates and draws strikethrough for the specified glyphs.
- [- underlineGlyphRange:underlineType:lineFragmentRect:lineFragmentGlyphRange:containerOrigin:](<underlineglyphrange(__underlinetype_linefragmentrect_linefragmentglyphrange_containerorigin_).md>) — Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.
