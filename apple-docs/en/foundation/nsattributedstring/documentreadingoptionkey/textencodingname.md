---
title: textEncodingName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentreadingoptionkey/textencodingname
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/textencodingname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentreadingoptionkey/textencodingname.json'
content_hash: 'sha256:267dfa05bf671e45'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentReadingOptionKey](../documentreadingoptionkey.md)

# textEncodingName

<sub>Type Property</sub>

The text encoding to use.

<sub>macOS</sub>

```swift
static let textEncodingName: NSAttributedString.DocumentReadingOptionKey
```

## Discussion

[NSString](../../nsstring.md) containing the name, IANA or otherwise, of a text encoding to override any encoding specified in an HTML document. Mutually exclusive with [characterEncoding](characterencoding.md). The previous string constant was `@"TextEncodingName"`.

## See Also

### Getting the document options

- [baseURL](baseurl.md) — The base URL for HTML documents.
- [characterEncoding](characterencoding.md) — The string encoding.
- [defaultAttributes](defaultattributes.md) — The default attributes to apply to plain files.
- [documentType](documenttype.md) — The document type.
- [fileType](filetype.md) — The file type.
- [readAccessURL](readaccessurl.md) — The local files WebKit can access when loading content.
- [textSizeMultiplier](textsizemultiplier.md) — The scale factor for font sizes.
- [timeout](timeout.md) — The time, in seconds, to wait for a document to finish loading.
- [webPreferences](webpreferences.md) — A WebPreferences object.
- [webResourceLoadDelegate](webresourceloaddelegate.md) — An object to serve as the web resource loading delegate.
