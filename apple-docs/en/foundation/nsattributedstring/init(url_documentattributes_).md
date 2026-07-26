---
title: 'init(URL:documentAttributes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsattributedstring/init(url:documentattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/init(url:documentattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/init%28url%3Adocumentattributes%3A%29.json'
content_hash: 'sha256:9fc730b14d160d53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# init(URL:documentAttributes:)

<sub>Initializer</sub>

Initializes a new attributed string object from the data at the specified URL.

> [!warning] Deprecated
> Use [- initWithURL:options:documentAttributes:error:](<init(url_options_documentattributes_).md>) instead.

<sub>macOS</sub>

```swift
init?(URL url: URL, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

<sub>macOS</sub>

```swift
init?(url: URL, documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?)
```

## Parameters

- `url` — An `NSURL` object specifying the document to load.

- `dict` — An in-out dictionary containing document-level attributes described in `Document Attributes`. May be `NULL`, in which case no document attributes are returned.

## Return Value

Returns an initialized object, or `nil` if the data can’t be decoded.

## Discussion

The contents of `aURL` are examined to best load the file in whatever format it’s in. Filter services can be used to convert the file into a format recognized by Cocoa. Also returns by reference in `docAttributes` a dictionary containing document-level attributes described in `Document Attributes`. `docAttributes` may be `NULL`, in which case no document attributes are returned. Returns an initialized object, or `nil` if the file at `path` can’t be decoded.

## See Also

### Deprecated Initializers

- [- initWithPath:documentAttributes:](<init(path_documentattributes_).md>) — Initializes a new attribute string object from RTF or RTFD data in the file at the specified path. _(deprecated)_
- [- initWithFileURL:options:documentAttributes:error:](<init(fileurl_options_documentattributes_).md>) — Initializes a new attributed string object from the data at the specified URL. _(deprecated)_
