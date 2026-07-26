---
title: documentContentKind
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument/documentcontentkind
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/documentcontentkind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/documentcontentkind.json'
content_hash: 'sha256:9a61c43efc73421f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# documentContentKind

<sub>Instance Property</sub>

Sets the kind of output content for the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var documentContentKind: XMLDocument.ContentKind { get set }
```

## Parameters

- `kind` — An `enum` constant identifying a kind of document content. The valid NSXMLDocumentContentKind constants are `NSXMLDocumentXMLKind`, `NSXMLDocumentXHTMLKind`, `NSXMLDocumentHTMLKind`, and `NSXMLDocumentTextKind`.

## Discussion

Most of the differences among document-content kind have to do with the handling of content-less tags such as `<br>`.

## See Also

### Managing Document Attributes

- [characterEncoding](characterencoding.md) — Sets the character encoding of the receiver to `encoding`,
- [DTD](dtd.md) — Returns an [XMLDTD](../xmldtd.md) object representing the internal DTD associated with the receiver.
- [standalone](isstandalone.md) — Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [MIMEType](mimetype.md) — Returns the MIME type for the receiver.
- [version](version.md) — Sets the version of the receiver’s XML.
