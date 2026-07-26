---
title: NSTextEncodingNameDocumentAttribute
framework: AppKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextencodingnamedocumentattribute
source_url: 'https://developer.apple.com/documentation/appkit/nstextencodingnamedocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextencodingnamedocumentattribute.json'
content_hash: 'sha256:9e26d895dff3b59d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSTextEncodingNameDocumentAttribute

<sub>Global Variable</sub>

The name of the text encoding to use.

<sub>macOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey NSTextEncodingNameDocumentAttribute;
```

## Discussion

An [NSString](../foundation/nsstring.md) object containing the name, IANA or otherwise, of a text encoding to be used. This attribute is mutually exclusive with [NSCharacterEncodingDocumentAttribute](nscharacterencodingdocumentattribute.md).

## See Also

### Getting document type keys

- [NSDocumentTypeDocumentAttribute](nsdocumenttypedocumentattribute.md) — The document type.
- [NSFileTypeDocumentAttribute](nsfiletypedocumentattribute.md) — The document type for interpreting the document.
