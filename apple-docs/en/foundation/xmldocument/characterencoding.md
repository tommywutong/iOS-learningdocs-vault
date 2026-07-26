---
title: characterEncoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument/characterencoding
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/characterencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/characterencoding.json'
content_hash: 'sha256:930def16a5363e6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# characterEncoding

<sub>Instance Property</sub>

Sets the character encoding of the receiver to `encoding`,

<sub>Mac Catalyst, macOS</sub>

```swift
var characterEncoding: String? { get set }
```

## Parameters

- `encoding` — A string that specifies an encoding; it must match the name of an IANA character set. See [http://www.iana.org/assignments/character-sets](http://www.iana.org/assignments/character-sets) for a list of valid encoding specifiers.

## Discussion

Typically the encoding is specified in the XML declaration of a document that is processed, but it can be set at any time. If the specified encoding does not match the actual encoding, parsing of the document might fail.

## See Also

### Managing Document Attributes

- [documentContentKind](documentcontentkind.md) — Sets the kind of output content for the receiver.
- [DTD](dtd.md) — Returns an [XMLDTD](../xmldtd.md) object representing the internal DTD associated with the receiver.
- [standalone](isstandalone.md) — Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [MIMEType](mimetype.md) — Returns the MIME type for the receiver.
- [version](version.md) — Sets the version of the receiver’s XML.
