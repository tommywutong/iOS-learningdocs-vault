---
title: mimeType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument/mimetype
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/mimetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/mimetype.json'
content_hash: 'sha256:c07d705cd7987943'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# mimeType

<sub>Instance Property</sub>

Returns the MIME type for the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var mimeType: String? { get set }
```

## Return Value

The MIME type for the receiver (for example, “text/xml”).

## Discussion

MIME types are assigned by IANA (see [http://www.iana.org/assignments/media-types/index.html](http://www.iana.org/assignments/media-types/index.html)).

## See Also

### Managing Document Attributes

- [characterEncoding](characterencoding.md) — Sets the character encoding of the receiver to `encoding`,
- [documentContentKind](documentcontentkind.md) — Sets the kind of output content for the receiver.
- [DTD](dtd.md) — Returns an [XMLDTD](../xmldtd.md) object representing the internal DTD associated with the receiver.
- [standalone](isstandalone.md) — Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [version](version.md) — Sets the version of the receiver’s XML.
