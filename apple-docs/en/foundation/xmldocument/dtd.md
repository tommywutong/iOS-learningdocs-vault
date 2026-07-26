---
title: dtd
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument/dtd
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/dtd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/dtd.json'
content_hash: 'sha256:51c5f741a1d9e93a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# dtd

<sub>Instance Property</sub>

Returns an [XMLDTD](../xmldtd.md) object representing the internal DTD associated with the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
@NSCopying var dtd: XMLDTD? { get set }
```

## Return Value

An [XMLDTD](../xmldtd.md) object representing the internal DTD associated with the receiver or `nil` if no DTD has been associated.

## See Also

### Managing Document Attributes

- [characterEncoding](characterencoding.md) — Sets the character encoding of the receiver to `encoding`,
- [documentContentKind](documentcontentkind.md) — Sets the kind of output content for the receiver.
- [standalone](isstandalone.md) — Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [MIMEType](mimetype.md) — Returns the MIME type for the receiver.
- [version](version.md) — Sets the version of the receiver’s XML.
