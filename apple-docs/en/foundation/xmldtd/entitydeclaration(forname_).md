---
title: 'entityDeclaration(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/entitydeclaration(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/entitydeclaration(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/entitydeclaration%28forname%3A%29.json'
content_hash: 'sha256:dd9970c027727865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# entityDeclaration(forName:)

<sub>Instance Method</sub>

Returns the DTD node representing the entity declaration for a specified entity.

<sub>Mac Catalyst, macOS</sub>

```swift
func entityDeclaration(forName name: String) -> XMLDTDNode?
```

## Parameters

- `name` — A string that is the name of an entity.

## Return Value

An autoreleased [XMLDTDNode](../xmldtdnode.md) object, or `nil` if there is no match.

## See Also

### Getting DTD Nodes by Name

- [+ predefinedEntityDeclarationForName:](<predefinedentitydeclaration(forname_).md>) — Returns a DTD node representing the predefined entity declaration with the specified name.
- [- elementDeclarationForName:](<elementdeclaration(forname_).md>) — Returns the DTD node representing an element declaration for a specified element.
- [- attributeDeclarationForName:elementName:](<attributedeclaration(forname_elementname_).md>) — Returns the DTD node representing an attribute-list declaration for a given attribute and its element.
- [- notationDeclarationForName:](<notationdeclaration(forname_).md>) — Returns the DTD node representing the notation declaration identified by the specified notation name.
