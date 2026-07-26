---
title: documentType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentattributekey/documenttype
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/documenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey/documenttype.json'
content_hash: 'sha256:2189950d7789ec66'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentAttributeKey](../documentattributekey.md)

# documentType

<sub>Type Property</sub>

The document type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let documentType: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is one of the document types declared in [DocumentType](../documenttype.md). For reader methods, this key in options can specify the document type for interpreting the contents. Upon return, the document attributes can contain this key for indicating the actual format used to read the contents. For write methods, this key specifies the format for generating the data.

The string constant in macOS 10.3 and earlier is `@"DocumentType"`.

## See Also

### Getting document type keys

- [fileType](filetype.md) — The document type for interpreting the document.
- [textEncodingName](textencodingname.md) — The name of the text encoding to use.
