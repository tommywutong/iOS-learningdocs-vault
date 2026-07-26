---
title: 'setLayoutRect(_:for:glyphRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/setlayoutrect(_:for:glyphrange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/setlayoutrect(_:for:glyphrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/setlayoutrect%28_%3Afor%3Aglyphrange%3A%29.json'
content_hash: 'sha256:b5915f2fe5c694cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setLayoutRect(_:for:glyphRange:)

<sub>Instance Method</sub>

Sets the layout rectangle that encloses the specified text block and glyph range.

<sub>macOS</sub>

```swift
func setLayoutRect(_ rect: NSRect, for block: NSTextBlock, glyphRange: NSRange)
```

## Parameters

- `rect` — The layout rectangle to set.

- `block` — The text block whose layout rectangle is set.

- `glyphRange` — The range of glyphs in the text block.

## Discussion

This method causes glyph generation but not layout. Block layout rectangles and bounds rectangles are always in container coordinates.

## See Also

### Handling layout for text blocks

- [- layoutRectForTextBlock:glyphRange:](<layoutrect(for_glyphrange_).md>) — Returns the rectangle for the layout of the specified text block and glyph range.
- [- setBoundsRect:forTextBlock:glyphRange:](<setboundsrect(__for_glyphrange_).md>) — Sets the bounding rectangle that encloses the specified text block and glyph range.
- [- boundsRectForTextBlock:glyphRange:](<boundsrect(for_glyphrange_).md>) — Returns the bounding rectangle that encloses the specified text block and glyph range.
- [- layoutRectForTextBlock:atIndex:effectiveRange:](<layoutrect(for_at_effectiverange_).md>) — Returns the rectangle for the layout of the specified text block and glyph.
- [- boundsRectForTextBlock:atIndex:effectiveRange:](<boundsrect(for_at_effectiverange_).md>) — Returns the bounding rectangle for the specified text block and glyph.
