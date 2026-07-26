---
title: notationName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldtdnode/notationname
source_url: 'https://developer.apple.com/documentation/foundation/xmldtdnode/notationname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtdnode/notationname.json'
content_hash: 'sha256:5da2ece0b03040e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTDNode](../xmldtdnode.md)

# notationName

<sub>Instance Property</sub>

Returns the name of the notation associated with the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var notationName: String? { get set }
```

## Return Value

The name of the notation associated with the receiver.

## Discussion

Notations are applicable to unparsed external entities, processing instructions, and some attribute values.

## See Also

### Managing DTD Identifiers

- [external](isexternal.md) — True if the system id is set. Valid for entities and notations.
- [publicID](publicid.md) — Returns the public identifier associated with the receiver.
- [systemID](systemid.md) — Returns the system identifier associated with the receiver.
