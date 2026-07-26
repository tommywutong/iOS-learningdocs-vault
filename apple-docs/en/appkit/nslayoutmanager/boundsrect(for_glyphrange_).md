---
title: 'boundsRect(for:glyphRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/boundsrect(for:glyphrange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/boundsrect(for:glyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/boundsrect%28for%3Aglyphrange%3A%29.json'
content_hash: 'sha256:b40a7f5ac99ddb80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# boundsRect(for:glyphRange:)

<sub>Instance Method</sub>

Returns the bounding rectangle that encloses the specified text block and glyph range.

<sub>macOS</sub>

```swift
func boundsRect(for block: NSTextBlock, glyphRange: NSRange) -> NSRect
```

## Parameters

- `block` — The text block whose bounds rectangle is returned.

- `glyphRange` — The range of glyphs in the text block.

## Return Value

The bounding rectangle, or `NSZeroRect` if no rectangle has been set for the specified block since the last invalidation

## Discussion

This method causes glyph generation but not layout. Block layout rectangles and bounds rectangles are always in container coordinates.

## See Also

### Handling layout for text blocks

- [- setLayoutRect:forTextBlock:glyphRange:](<setlayoutrect(__for_glyphrange_).md>) — Sets the layout rectangle that encloses the specified text block and glyph range.
- [- layoutRectForTextBlock:glyphRange:](<layoutrect(for_glyphrange_).md>) — Returns the rectangle for the layout of the specified text block and glyph range.
- [- setBoundsRect:forTextBlock:glyphRange:](<setboundsrect(__for_glyphrange_).md>) — Sets the bounding rectangle that encloses the specified text block and glyph range.
- [- layoutRectForTextBlock:atIndex:effectiveRange:](<layoutrect(for_at_effectiverange_).md>) — Returns the rectangle for the layout of the specified text block and glyph.
- [- boundsRectForTextBlock:atIndex:effectiveRange:](<boundsrect(for_at_effectiverange_).md>) — Returns the bounding rectangle for the specified text block and glyph.
