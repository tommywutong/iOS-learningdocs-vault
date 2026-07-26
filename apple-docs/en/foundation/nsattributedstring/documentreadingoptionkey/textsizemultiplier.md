---
title: textSizeMultiplier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentreadingoptionkey/textsizemultiplier
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/textsizemultiplier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentreadingoptionkey/textsizemultiplier.json'
content_hash: 'sha256:d682b611177b249f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentReadingOptionKey](../documentreadingoptionkey.md)

# textSizeMultiplier

<sub>Type Property</sub>

The scale factor for font sizes.

<sub>macOS</sub>

```swift
static let textSizeMultiplier: NSAttributedString.DocumentReadingOptionKey
```

## Discussion

[NSNumber](../../nsnumber.md) containing float, default 1.0; for HTML only, corresponding to WebView’s `textSizeMultiplier`.

## See Also

### Getting the document options

- [baseURL](baseurl.md) — The base URL for HTML documents.
- [characterEncoding](characterencoding.md) — The string encoding.
- [defaultAttributes](defaultattributes.md) — The default attributes to apply to plain files.
- [documentType](documenttype.md) — The document type.
- [fileType](filetype.md) — The file type.
- [readAccessURL](readaccessurl.md) — The local files WebKit can access when loading content.
- [textEncodingName](textencodingname.md) — The text encoding to use.
- [timeout](timeout.md) — The time, in seconds, to wait for a document to finish loading.
- [webPreferences](webpreferences.md) — A WebPreferences object.
- [webResourceLoadDelegate](webresourceloaddelegate.md) — An object to serve as the web resource loading delegate.
