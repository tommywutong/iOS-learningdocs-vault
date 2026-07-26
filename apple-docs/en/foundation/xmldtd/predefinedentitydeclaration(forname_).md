---
title: 'predefinedEntityDeclaration(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/predefinedentitydeclaration(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/predefinedentitydeclaration(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/predefinedentitydeclaration%28forname%3A%29.json'
content_hash: 'sha256:9840d08d5445375e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# predefinedEntityDeclaration(forName:)

<sub>Type Method</sub>

Returns a DTD node representing the predefined entity declaration with the specified name.

<sub>Mac Catalyst, macOS</sub>

```swift
class func predefinedEntityDeclaration(forName name: String) -> XMLDTDNode?
```

## Parameters

- `name` — A string identifying a predefined entity declaration.

## Return Value

An autoreleased [XMLDTDNode](../xmldtdnode.md) object, or `nil` if there is no match for `name`.

## Discussion

The five predefined entity references (or character references) are “\<” (less-than sign), “\>” (greater-than sign), “&” (ampersand), “"” (quotation mark), and “'” (apostrophe).

## See Also

### Getting DTD Nodes by Name

- [- elementDeclarationForName:](<elementdeclaration(forname_).md>) — Returns the DTD node representing an element declaration for a specified element.
- [- attributeDeclarationForName:elementName:](<attributedeclaration(forname_elementname_).md>) — Returns the DTD node representing an attribute-list declaration for a given attribute and its element.
- [- entityDeclarationForName:](<entitydeclaration(forname_).md>) — Returns the DTD node representing the entity declaration for a specified entity.
- [- notationDeclarationForName:](<notationdeclaration(forname_).md>) — Returns the DTD node representing the notation declaration identified by the specified notation name.
