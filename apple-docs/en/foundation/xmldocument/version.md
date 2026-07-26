---
title: version
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument/version
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/version.json'
content_hash: 'sha256:2cacbe664ca422ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# version

<sub>Instance Property</sub>

Sets the version of the receiver’s XML.

<sub>Mac Catalyst, macOS</sub>

```swift
var version: String? { get set }
```

## Parameters

- `version` — A string object identifying the version of the XML.

## Discussion

Currently, the version should be either “1.0 “or “1.1”.

## See Also

### Managing Document Attributes

- [characterEncoding](characterencoding.md) — Sets the character encoding of the receiver to `encoding`,
- [documentContentKind](documentcontentkind.md) — Sets the kind of output content for the receiver.
- [DTD](dtd.md) — Returns an [XMLDTD](../xmldtd.md) object representing the internal DTD associated with the receiver.
- [standalone](isstandalone.md) — Sets a Boolean value that specifies whether the receiver represents a standalone XML document.
- [MIMEType](mimetype.md) — Returns the MIME type for the receiver.
