---
title: webPreferences
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentreadingoptionkey/webpreferences
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/webpreferences'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentreadingoptionkey/webpreferences.json'
content_hash: 'sha256:a98fcd5d5850fa37'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentReadingOptionKey](../documentreadingoptionkey.md)

# webPreferences

<sub>Type Property</sub>

A WebPreferences object.

<sub>macOS</sub>

```swift
static let webPreferences: NSAttributedString.DocumentReadingOptionKey
```

## Discussion

For HTML only. If not present, a default set of preferences is used. The previous string constant was `@"WebPreferences"`.

## See Also

### Getting the document options

- [baseURL](baseurl.md) — The base URL for HTML documents.
- [characterEncoding](characterencoding.md) — The string encoding.
- [defaultAttributes](defaultattributes.md) — The default attributes to apply to plain files.
- [documentType](documenttype.md) — The document type.
- [fileType](filetype.md) — The file type.
- [readAccessURL](readaccessurl.md) — The local files WebKit can access when loading content.
- [textEncodingName](textencodingname.md) — The text encoding to use.
- [textSizeMultiplier](textsizemultiplier.md) — The scale factor for font sizes.
- [timeout](timeout.md) — The time, in seconds, to wait for a document to finish loading.
- [webResourceLoadDelegate](webresourceloaddelegate.md) — An object to serve as the web resource loading delegate.
