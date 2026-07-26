---
title: systemID
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldtdnode/systemid
source_url: 'https://developer.apple.com/documentation/foundation/xmldtdnode/systemid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtdnode/systemid.json'
content_hash: 'sha256:00a956c73410ef12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTDNode](../xmldtdnode.md)

# systemID

<sub>Instance Property</sub>

Returns the system identifier associated with the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var systemID: String? { get set }
```

## Return Value

The system identifier associated with the receiver.

## See Also

### Managing DTD Identifiers

- [external](isexternal.md) — True if the system id is set. Valid for entities and notations.
- [notationName](notationname.md) — Returns the name of the notation associated with the receiver.
- [publicID](publicid.md) — Returns the public identifier associated with the receiver.
