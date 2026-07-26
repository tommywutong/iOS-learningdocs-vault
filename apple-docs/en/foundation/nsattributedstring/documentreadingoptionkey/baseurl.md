---
title: baseURL
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentreadingoptionkey/baseurl
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/baseurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentreadingoptionkey/baseurl.json'
content_hash: 'sha256:446f3be3b5d94d0d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentReadingOptionKey](../documentreadingoptionkey.md)

# baseURL

<sub>Type Property</sub>

The base URL for HTML documents.

<sub>macOS</sub>

```swift
static let baseURL: NSAttributedString.DocumentReadingOptionKey
```

## Discussion

For HTML documents; [NSURL](../../nsurl.md) containing base URL. The previous string constant was `@"BaseURL".`

## See Also

### Getting the document options

- [characterEncoding](characterencoding.md) — The string encoding.
- [defaultAttributes](defaultattributes.md) — The default attributes to apply to plain files.
- [documentType](documenttype.md) — The document type.
- [fileType](filetype.md) — The file type.
- [readAccessURL](readaccessurl.md) — The local files WebKit can access when loading content.
- [textEncodingName](textencodingname.md) — The text encoding to use.
- [textSizeMultiplier](textsizemultiplier.md) — The scale factor for font sizes.
- [timeout](timeout.md) — The time, in seconds, to wait for a document to finish loading.
- [webPreferences](webpreferences.md) — A WebPreferences object.
- [webResourceLoadDelegate](webresourceloaddelegate.md) — An object to serve as the web resource loading delegate.
