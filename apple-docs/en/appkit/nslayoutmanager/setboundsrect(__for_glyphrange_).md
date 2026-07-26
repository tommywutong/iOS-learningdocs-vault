---
title: 'setBoundsRect(_:for:glyphRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/setboundsrect(_:for:glyphrange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/setboundsrect(_:for:glyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/setboundsrect%28_%3Afor%3Aglyphrange%3A%29.json'
content_hash: 'sha256:376c7330ea0882df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setBoundsRect(_:for:glyphRange:)

<sub>Instance Method</sub>

Sets the bounding rectangle that encloses the specified text block and glyph range.

<sub>macOS</sub>

```swift
func setBoundsRect(_ rect: NSRect, for block: NSTextBlock, glyphRange: NSRange)
```

## Parameters

- `rect` — The bounding rectangle to set.

- `block` — The text block whose bounding rectangle is set.

- `glyphRange` — The range of glyphs in the text block.

## Discussion

This method causes glyph generation but not layout. Block layout rectangles and bounds rectangles are always in container coordinates.

## See Also

### Handling layout for text blocks

- [- setLayoutRect:forTextBlock:glyphRange:](<setlayoutrect(__for_glyphrange_).md>) — Sets the layout rectangle that encloses the specified text block and glyph range.
- [- layoutRectForTextBlock:glyphRange:](<layoutrect(for_glyphrange_).md>) — Returns the rectangle for the layout of the specified text block and glyph range.
- [- boundsRectForTextBlock:glyphRange:](<boundsrect(for_glyphrange_).md>) — Returns the bounding rectangle that encloses the specified text block and glyph range.
- [- layoutRectForTextBlock:atIndex:effectiveRange:](<layoutrect(for_at_effectiverange_).md>) — Returns the rectangle for the layout of the specified text block and glyph.
- [- boundsRectForTextBlock:atIndex:effectiveRange:](<boundsrect(for_at_effectiverange_).md>) — Returns the bounding rectangle for the specified text block and glyph.
