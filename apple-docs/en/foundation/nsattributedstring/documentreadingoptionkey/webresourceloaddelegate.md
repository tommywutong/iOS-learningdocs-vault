---
title: webResourceLoadDelegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentreadingoptionkey/webresourceloaddelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/webresourceloaddelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentreadingoptionkey/webresourceloaddelegate.json'
content_hash: 'sha256:63bbddb9597356f8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentReadingOptionKey](../documentreadingoptionkey.md)

# webResourceLoadDelegate

<sub>Type Property</sub>

An object to serve as the web resource loading delegate.

<sub>macOS</sub>

```swift
static let webResourceLoadDelegate: NSAttributedString.DocumentReadingOptionKey
```

## Discussion

For HTML only. The value is an [NSObject](../../../objectivec/nsobject-swift.class.md).

If not present, a default delegate is used that permits the loading of subsidiary resources but does not respond to authentication challenges. The previous string constant was `@"WebResourceLoadDelegate"`.

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
- [webPreferences](webpreferences.md) — A WebPreferences object.
