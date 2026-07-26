---
title: 'boundingRect(with:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsattributedstring/boundingrect(with:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/boundingrect(with:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/boundingrect%28with%3Aoptions%3A%29.json'
content_hash: 'sha256:93809aa2b4832954'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# boundingRect(with:options:)

<sub>Instance Method</sub>

Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context.

> [!warning] Deprecated
> Use [- boundingRectWithSize:options:context:](<boundingrect(with_options_context_).md>) instead.

<sub>macOS</sub>

```swift
func boundingRect(with size: NSSize, options: NSString.DrawingOptions = []) -> NSRect
```

## Parameters

- `size` — The size of the rectangle to draw in.

- `options` — The string drawing options. See [NSStringDrawingOptions](../../uikit/nsstringdrawingoptions.md) for the possible values.

## Return Value

The bounding rectangle in the current graphics context.

## Discussion

The origin of the rectangle returned from this method is the first glyph origin.

## See Also

### Deprecated Instance Methods

- [- URLAtIndex:effectiveRange:](<url(at_effectiverange_).md>) — Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection. _(deprecated)_
- [- drawWithRect:options:](<draw(with_options_).md>) — Draws the attributed string with the specified options within the specified rectangle in the current graphics context. _(deprecated)_
