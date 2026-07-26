---
title: 'init(path:documentAttributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsattributedstring/init(path:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(path:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28path%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:e794a267dc722c85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(path:documentAttributes:)

<sub>Initializer</sub>

Initializes a new attribute string object from RTF or RTFD data in the file at the specified path.

> [!warning] Deprecated
> Use [- initWithURL:options:documentAttributes:error:](<init(url_options_documentattributes_).md>) instead.

<sub>macOS</sub>

```swift
init?(path: String, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

## Parameters

- `path` — The path to an RTF or RTFD file.

- `dict` — An in-out dictionary containing document-level attributes described in `Document Attributes`. May be `NULL`, in which case no document attributes are returned.

## Return Value

Returns an initialized object, or `nil` if the data can’t be decoded.

## Discussion

The contents of `path` will be examined to best load the file in whatever format it’s in. Filter services can be used to convert the file into a format recognized by Cocoa. Also returns by reference in `docAttributes` a dictionary containing document-level attributes described in `Document Attributes`. `docAttributes` may be `NULL`, in which case no document attributes are returned. Returns an initialized object, or `nil` if the file at `path` can’t be decoded.

## See Also

### Deprecated Initializers

- [- initWithURL:documentAttributes:](<init(url_documentattributes_).md>) — Initializes a new attributed string object from the data at the specified URL. _(deprecated)_
- [- initWithFileURL:options:documentAttributes:error:](<init(fileurl_options_documentattributes_).md>) — Initializes a new attributed string object from the data at the specified URL. _(deprecated)_
