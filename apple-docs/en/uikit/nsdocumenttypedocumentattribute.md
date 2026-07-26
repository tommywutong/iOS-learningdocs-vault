---
title: NSDocumentTypeDocumentAttribute
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdocumenttypedocumentattribute
source_url: 'https://developer.apple.com/documentation/uikit/nsdocumenttypedocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdocumenttypedocumentattribute.json'
content_hash: 'sha256:20f5a641b889781f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDocumentTypeDocumentAttribute

<sub>Global Variable</sub>

The document type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey const NSDocumentTypeDocumentAttribute;
```

## Discussion

The value of this attribute is one of the document types declared in [NSAttributedStringDocumentType](nsattributedstringdocumenttype.md). For reader methods, this key in options can specify the document type for interpreting the contents. Upon return, the document attributes can contain this key for indicating the actual format used to read the contents. For write methods, this key specifies the format for generating the data.

The string constant in macOS 10.3 and earlier is `@"DocumentType"`.

## See Also

### Getting document type keys

- [NSFileTypeDocumentAttribute](../appkit/nsfiletypedocumentattribute.md) — The document type for interpreting the document.
- [NSTextEncodingNameDocumentAttribute](../appkit/nstextencodingnamedocumentattribute.md) — The name of the text encoding to use.
