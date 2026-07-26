---
title: textEncodingName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/documentattributekey/textencodingname
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/textencodingname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey/textencodingname.json'
content_hash: 'sha256:14d4e1c4aca3bc35'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentAttributeKey](../documentattributekey.md)

# textEncodingName

<sub>Type Property</sub>

The name of the text encoding to use.

<sub>macOS</sub>

```swift
static let textEncodingName: NSAttributedString.DocumentAttributeKey
```

## Discussion

An [NSString](../../nsstring.md) object containing the name, IANA or otherwise, of a text encoding to be used. This attribute is mutually exclusive with [characterEncoding](characterencoding.md).

## See Also

### Getting document type keys

- [documentType](documenttype.md) — The document type.
- [fileType](filetype.md) — The document type for interpreting the document.
