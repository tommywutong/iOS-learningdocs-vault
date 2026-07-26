---
title: 'url(at:effectiveRange:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsattributedstring/url(at:effectiverange:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/url(at:effectiverange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/url%28at%3Aeffectiverange%3A%29.json'
content_hash: 'sha256:3ba0b927a37f9f47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# url(at:effectiveRange:)

<sub>Instance Method</sub>

Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection.

> [!warning] Deprecated
> Use an [NSDataDetector](../nsdatadetector.md) object instead.

<sub>macOS</sub>

```swift
func url(at location: Int, effectiveRange: NSRangePointer) -> URL?
```

## Parameters

- `location` — The character index in the string at which the method checks for a link.

- `effectiveRange` — The actual range covered by the link attribute or URL string, or of non-URL text if no apparent URL is found.

## Return Value

The URL found at `location`.

## See Also

### Deprecated Instance Methods

- [- drawWithRect:options:](<draw(with_options_).md>) — Draws the attributed string with the specified options within the specified rectangle in the current graphics context. _(deprecated)_
- [- boundingRectWithSize:options:](<boundingrect(with_options_).md>) — Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context. _(deprecated)_
