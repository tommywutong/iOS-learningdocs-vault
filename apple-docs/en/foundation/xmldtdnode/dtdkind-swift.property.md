---
title: dtdKind
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldtdnode/dtdkind-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/xmldtdnode/dtdkind-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtdnode/dtdkind-swift.property.json'
content_hash: 'sha256:c7bc6ca2a0d59329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTDNode](../xmldtdnode.md)

# dtdKind

<sub>Instance Property</sub>

Returns the receiver’s DTD kind.

<sub>Mac Catalyst, macOS</sub>

```swift
var dtdKind: XMLDTDNode.DTDKind { get set }
```

## Return Value

The receiver’s DTD kind. See Constants for a list of valid NSXMLDTDNodeKind constants.

## Discussion

The DTD kind is distinct from a `NSXMLDTDNode` object’s node kind (returned by the `NSXMLNode` [kind](../xmlnode/kind-swift.property.md) method).
