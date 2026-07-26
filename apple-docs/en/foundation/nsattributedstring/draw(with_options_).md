---
title: 'draw(with:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsattributedstring/draw(with:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/draw(with:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/draw%28with%3Aoptions%3A%29.json'
content_hash: 'sha256:bd934ebca9644c35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# draw(with:options:)

<sub>Instance Method</sub>

Draws the attributed string with the specified options within the specified rectangle in the current graphics context.

> [!warning] Deprecated
> Use [- drawWithRect:options:context:](<draw(with_options_context_).md>) instead.

<sub>macOS</sub>

```swift
func draw(with rect: NSRect, options: NSString.DrawingOptions = [])
```

## Parameters

- `rect` — The rectangle specifies the rendering origin in the current graphics context.

- `options` — The string drawing options. See [NSStringDrawingOptions](../../uikit/nsstringdrawingoptions.md) for the available options.

## Discussion

The `rect` argument’s origin field specifies the rendering origin. The point is interpreted as the baseline origin by default. With `NSStringDrawingUsesLineFragmentOrigin`, it is interpreted as the upper left corner of the line fragment rect. The size field specifies the text container size. The width part of the size field specifies the maximum line fragment width if larger than `0.0`. The height defines the maximum size that can be occupied with text if larger than `0.0` and `NSStringDrawingUsesLineFragmentOrigin` is specified. If `NSStringDrawingUsesLineFragmentOrigin` is not specified, height is ignored and considered to be single-line rendering (`NSLineBreakByWordWrapping` and `NSLineBreakByCharWrapping` are treated as `NSLineBreakByClipping`).

You should only invoke this method when there is a current graphics context.

## See Also

### Deprecated Instance Methods

- [- URLAtIndex:effectiveRange:](<url(at_effectiverange_).md>) — Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection. _(deprecated)_
- [- boundingRectWithSize:options:](<boundingrect(with_options_).md>) — Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context. _(deprecated)_
