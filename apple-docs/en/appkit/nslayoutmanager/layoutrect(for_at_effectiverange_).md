---
title: 'layoutRect(for:at:effectiveRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/layoutrect(for:at:effectiverange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/layoutrect(for:at:effectiverange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/layoutrect%28for%3Aat%3Aeffectiverange%3A%29.json'
content_hash: 'sha256:14f0846055c71168'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# layoutRect(for:at:effectiveRange:)

<sub>Instance Method</sub>

Returns the rectangle for the layout of the specified text block and glyph.

<sub>macOS</sub>

```swift
func layoutRect(for block: NSTextBlock, at glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?) -> NSRect
```

## Parameters

- `block` — The text block whose layout rectangle is returned.

- `glyphIndex` — Index of the glyph.

- `effectiveGlyphRange` — If not `NULL`, on output, the range for all glyphs in the text block.

## Return Value

The layout rectangle of the text block, or `NSZeroRect` if no rectangle has been set for the specified block since the last invalidation.

## Discussion

This method causes glyph generation but not layout. Block layout rectangles and bounds rectangles are always in container coordinates.

## See Also

### Handling layout for text blocks

- [- setLayoutRect:forTextBlock:glyphRange:](<setlayoutrect(__for_glyphrange_).md>) — Sets the layout rectangle that encloses the specified text block and glyph range.
- [- layoutRectForTextBlock:glyphRange:](<layoutrect(for_glyphrange_).md>) — Returns the rectangle for the layout of the specified text block and glyph range.
- [- setBoundsRect:forTextBlock:glyphRange:](<setboundsrect(__for_glyphrange_).md>) — Sets the bounding rectangle that encloses the specified text block and glyph range.
- [- boundsRectForTextBlock:glyphRange:](<boundsrect(for_glyphrange_).md>) — Returns the bounding rectangle that encloses the specified text block and glyph range.
- [- boundsRectForTextBlock:atIndex:effectiveRange:](<boundsrect(for_at_effectiverange_).md>) — Returns the bounding rectangle for the specified text block and glyph.
