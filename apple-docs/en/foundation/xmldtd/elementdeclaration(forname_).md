---
title: 'elementDeclaration(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/elementdeclaration(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/elementdeclaration(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/elementdeclaration%28forname%3A%29.json'
content_hash: 'sha256:5487fb7570ebdf98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# elementDeclaration(forName:)

<sub>Instance Method</sub>

Returns the DTD node representing an element declaration for a specified element.

<sub>Mac Catalyst, macOS</sub>

```swift
func elementDeclaration(forName name: String) -> XMLDTDNode?
```

## Parameters

- `name` — A string that is the name of an element.

## Return Value

An autoreleased [XMLDTDNode](../xmldtdnode.md) object, or `nil` if there is no match.

## See Also

### Getting DTD Nodes by Name

- [+ predefinedEntityDeclarationForName:](<predefinedentitydeclaration(forname_).md>) — Returns a DTD node representing the predefined entity declaration with the specified name.
- [- attributeDeclarationForName:elementName:](<attributedeclaration(forname_elementname_).md>) — Returns the DTD node representing an attribute-list declaration for a given attribute and its element.
- [- entityDeclarationForName:](<entitydeclaration(forname_).md>) — Returns the DTD node representing the entity declaration for a specified entity.
- [- notationDeclarationForName:](<notationdeclaration(forname_).md>) — Returns the DTD node representing the notation declaration identified by the specified notation name.
