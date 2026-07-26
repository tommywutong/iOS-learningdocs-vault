---
title: 'init(xmlString:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtdnode/init(xmlstring:)-1dyhd'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtdnode/init(xmlstring:)-1dyhd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtdnode/init%28xmlstring%3A%29-1dyhd.json'
content_hash: 'sha256:209966d58fb75aa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTDNode](../xmldtdnode.md)

# init(xmlString:)

<sub>Initializer</sub>

Returns an `NSXMLDTDNode` object initialized with the DTD declaration in a given string.

<sub>Mac Catalyst, macOS</sub>

```swift
init?(xmlString string: String)
```

## Parameters

- `string` — The DTD declaration.

## Return Value

An `NSXMLDTDNode` object initialized with the DTD declaration in `string`. Returns `nil` if initialization did not succeed, as might occur if the passed-in declaration is malformed.

## Discussion

The node kind (NSXMLNode) assigned to the returned object—element, attribute, entity, or notation declaration— is based on the full XML string that is parsed. To assign a subkind, set the [DTDKind](dtdkind-swift.property.md) property.

You may also use the [+ DTDNodeWithXMLString:](<../xmlnode/dtdnode(withxmlstring_).md>) or [- initWithKind:](<../xmlnode/init(kind_).md>) methods to create `NSXMLDTDNode` instances. However, you cannot use the latter method to create `NSXMLDTDNode` instances for attribute-list declarations.

## See Also

### Related Documentation

- [Tree-Based XML Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html#//apple_ref/doc/uid/TP40001269)
