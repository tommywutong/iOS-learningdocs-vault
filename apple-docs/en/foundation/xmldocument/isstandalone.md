---
title: isStandalone
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument/isstandalone
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/isstandalone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/isstandalone.json'
content_hash: 'sha256:5ec530e569eaa4c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# isStandalone

<sub>Instance Property</sub>

Sets a Boolean value that specifies whether the receiver represents a standalone XML document.

<sub>Mac Catalyst, macOS</sub>

```swift
var isStandalone: Bool { get set }
```

## Parameters

- `standalone` — [true](../../swift/true.md) if the receiver represents a standalone XML document, [false](../../swift/false.md) otherwise.

## Discussion

A standalone document does not have an external DTD associated with it.

## See Also

### Managing Document Attributes

- [characterEncoding](characterencoding.md) — Sets the character encoding of the receiver to `encoding`,
- [documentContentKind](documentcontentkind.md) — Sets the kind of output content for the receiver.
- [DTD](dtd.md) — Returns an [XMLDTD](../xmldtd.md) object representing the internal DTD associated with the receiver.
- [MIMEType](mimetype.md) — Returns the MIME type for the receiver.
- [version](version.md) — Sets the version of the receiver’s XML.
