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
doc_path: /documentation/foundation/nsattributedstring/documentattributekey/filetype
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/documentattributekey/filetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/documentattributekey/filetype.json'
content_hash: 'sha256:665d361c76c1e94a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSAttributedString](../../nsattributedstring.md) · [DocumentAttributeKey](../documentattributekey.md)

# fileType

<sub>Type Property</sub>

The document type for interpreting the document.

<sub>macOS</sub>

```swift
static let fileType: NSAttributedString.DocumentAttributeKey
```

## Discussion

The value of this attribute is an [NSString](../../nsstring.md) object indicating which document type was used to interpret the document, specified as a UTI; for reading, this is available along with [documentType](documenttype.md), but for writing the two are mutually exclusive.

## See Also

### Getting document type keys

- [documentType](documenttype.md) — The document type.
- [textEncodingName](textencodingname.md) — The name of the text encoding to use.
