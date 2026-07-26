---
title: 'notationDeclaration(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/notationdeclaration(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/notationdeclaration(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/notationdeclaration%28forname%3A%29.json'
content_hash: 'sha256:93f6fab5ef02a929'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# notationDeclaration(forName:)

<sub>Instance Method</sub>

Returns the DTD node representing the notation declaration identified by the specified notation name.

<sub>Mac Catalyst, macOS</sub>

```swift
func notationDeclaration(forName name: String) -> XMLDTDNode?
```

## Parameters

- `name` — A string that is the name of a notation.

## Return Value

An autoreleased [XMLDTDNode](../xmldtdnode.md) object, or `nil` if there is no match.

## See Also

### Getting DTD Nodes by Name

- [+ predefinedEntityDeclarationForName:](<predefinedentitydeclaration(forname_).md>) — Returns a DTD node representing the predefined entity declaration with the specified name.
- [- elementDeclarationForName:](<elementdeclaration(forname_).md>) — Returns the DTD node representing an element declaration for a specified element.
- [- attributeDeclarationForName:elementName:](<attributedeclaration(forname_elementname_).md>) — Returns the DTD node representing an attribute-list declaration for a given attribute and its element.
- [- entityDeclarationForName:](<entitydeclaration(forname_).md>) — Returns the DTD node representing the entity declaration for a specified entity.
