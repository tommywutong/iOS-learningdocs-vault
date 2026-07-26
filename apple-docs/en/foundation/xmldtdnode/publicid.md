---
title: publicID
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldtdnode/publicid
source_url: 'https://developer.apple.com/documentation/foundation/xmldtdnode/publicid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtdnode/publicid.json'
content_hash: 'sha256:099a1a789b50fc9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTDNode](../xmldtdnode.md)

# publicID

<sub>Instance Property</sub>

Returns the public identifier associated with the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var publicID: String? { get set }
```

## Return Value

The public identifier associated with the receiver.

## Discussion

The public ID is applicable to entities and notations.

## See Also

### Managing DTD Identifiers

- [external](isexternal.md) — True if the system id is set. Valid for entities and notations.
- [notationName](notationname.md) — Returns the name of the notation associated with the receiver.
- [systemID](systemid.md) — Returns the system identifier associated with the receiver.
