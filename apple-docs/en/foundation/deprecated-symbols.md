---
title: Deprecated Symbols
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/deprecated-symbols
source_url: 'https://developer.apple.com/documentation/foundation/deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/deprecated-symbols.json'
content_hash: 'sha256:eb3174ad799c8b12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [NSAttributedString](nsattributedstring.md)

# Deprecated Symbols

<sub>API Collection</sub>

Migrate your code away from using these symbols.

## Topics

### Deprecated Initializers

- [- initWithPath:documentAttributes:](<nsattributedstring/init(path_documentattributes_).md>) — Initializes a new attribute string object from RTF or RTFD data in the file at the specified path. _(deprecated)_
- [- initWithURL:documentAttributes:](<nsattributedstring/init(url_documentattributes_).md>) — Initializes a new attributed string object from the data at the specified URL. _(deprecated)_
- [- initWithFileURL:options:documentAttributes:error:](<nsattributedstring/init(fileurl_options_documentattributes_).md>) — Initializes a new attributed string object from the data at the specified URL. _(deprecated)_

### Deprecated Properties

- [containsAttachments](nsattributedstring/containsattachments.md) — A Boolean value that indicates whether the attribute string contains any attachment attributes. _(deprecated)_

### Deprecated Enumerations

- [NSTextWritingDirection](../uikit/nstextwritingdirection.md) — Options for specifying text-writing direction. _(deprecated)_

### Deprecated Instance Methods

- [- URLAtIndex:effectiveRange:](<nsattributedstring/url(at_effectiverange_).md>) — Returns a URL, either from a link attribute or from text at the specified location that appears to be a URL string, for use in automatic link detection. _(deprecated)_
- [- drawWithRect:options:](<nsattributedstring/draw(with_options_).md>) — Draws the attributed string with the specified options within the specified rectangle in the current graphics context. _(deprecated)_
- [- boundingRectWithSize:options:](<nsattributedstring/boundingrect(with_options_).md>) — Calculates and returns a bounding rectangle for the attributed string using the options specified within the specified rectangle in the current graphics context. _(deprecated)_
