---
title: NSFileTypeDocumentAttribute
framework: AppKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.6+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsfiletypedocumentattribute
source_url: 'https://developer.apple.com/documentation/appkit/nsfiletypedocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsfiletypedocumentattribute.json'
content_hash: 'sha256:38249faaafcb30af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSFileTypeDocumentAttribute

<sub>Global Variable</sub>

The document type for interpreting the document.

<sub>macOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey NSFileTypeDocumentAttribute;
```

## Discussion

The value of this attribute is an [NSString](../foundation/nsstring.md) object indicating which document type was used to interpret the document, specified as a UTI; for reading, this is available along with [NSDocumentTypeDocumentAttribute](nsdocumenttypedocumentattribute.md), but for writing the two are mutually exclusive.

## See Also

### Getting document type keys

- [NSDocumentTypeDocumentAttribute](nsdocumenttypedocumentattribute.md) — The document type.
- [NSTextEncodingNameDocumentAttribute](nstextencodingnamedocumentattribute.md) — The name of the text encoding to use.
