---
title: characterEncoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentreadingoptionkey/characterencoding
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentreadingoptionkey/characterencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentreadingoptionkey/characterencoding.json'
content_hash: 'sha256:6a109e27d1d35fce'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentReadingOptionKey](../documentreadingoptionkey.md)

# characterEncoding

<sub>Type Property</sub>

The string encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let characterEncoding: NSAttributedString.DocumentReadingOptionKey
```

## Discussion

For plain text documents; [NSNumber](../../nsnumber.md) containing the unsigned int [NSStringEncoding](../../nsstringencoding.md) to override any encoding specified in an HTML document. The previous string constant was `@"CharacterEncoding"`.

## See Also

### Getting the document options

- [baseURL](baseurl.md) — The base URL for HTML documents.
- [defaultAttributes](defaultattributes.md) — The default attributes to apply to plain files.
- [documentType](documenttype.md) — The document type.
- [fileType](filetype.md) — The file type.
- [readAccessURL](readaccessurl.md) — The local files WebKit can access when loading content.
- [textEncodingName](textencodingname.md) — The text encoding to use.
- [textSizeMultiplier](textsizemultiplier.md) — The scale factor for font sizes.
- [timeout](timeout.md) — The time, in seconds, to wait for a document to finish loading.
- [webPreferences](webpreferences.md) — A WebPreferences object.
- [webResourceLoadDelegate](webresourceloaddelegate.md) — An object to serve as the web resource loading delegate.
