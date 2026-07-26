---
title: fileType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.6+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentreadingoptionkey/filetype
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/filetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentreadingoptionkey/filetype.json'
content_hash: 'sha256:07a877971afa8ef4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentReadingOptionKey](../documentreadingoptionkey.md)

# fileType

<sub>Type Property</sub>

The file type.

<sub>macOS</sub>

```swift
static let fileType: NSAttributedString.DocumentReadingOptionKey
```

## Discussion

The value of this attribute is an [NSString](../../nsstring.md) object indicating a document type to be forced when loading the document, specified as a UTI string; mutually exclusive with [documentType](documenttype.md).

## See Also

### Getting the document options

- [baseURL](baseurl.md) — The base URL for HTML documents.
- [characterEncoding](characterencoding.md) — The string encoding.
- [defaultAttributes](defaultattributes.md) — The default attributes to apply to plain files.
- [documentType](documenttype.md) — The document type.
- [readAccessURL](readaccessurl.md) — The local files WebKit can access when loading content.
- [textEncodingName](textencodingname.md) — The text encoding to use.
- [textSizeMultiplier](textsizemultiplier.md) — The scale factor for font sizes.
- [timeout](timeout.md) — The time, in seconds, to wait for a document to finish loading.
- [webPreferences](webpreferences.md) — A WebPreferences object.
- [webResourceLoadDelegate](webresourceloaddelegate.md) — An object to serve as the web resource loading delegate.
