---
title: 'attributeDeclaration(forName:elementName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/attributedeclaration(forname:elementname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/attributedeclaration(forname:elementname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/attributedeclaration%28forname%3Aelementname%3A%29.json'
content_hash: 'sha256:984a74918093ce97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# attributeDeclaration(forName:elementName:)

<sub>Instance Method</sub>

Returns the DTD node representing an attribute-list declaration for a given attribute and its element.

<sub>Mac Catalyst, macOS</sub>

```swift
func attributeDeclaration(forName name: String, elementName: String) -> XMLDTDNode?
```

## Parameters

- `name` — A string object identifying the name of an attribute.

- `elementName` — A string object identifying the name of an element.

## Return Value

An autoreleased [XMLDTDNode](../xmldtdnode.md) object, or `nil` if there is no matching attribute-list declaration.

## Discussion

For example, in the attribute-list declaration:

```objc
<!ATTLIST person idnum CDATA "0000">
```

“idnum” would correspond to `attrName` and “person” would correspond to `elementName`.

## See Also

### Getting DTD Nodes by Name

- [+ predefinedEntityDeclarationForName:](<predefinedentitydeclaration(forname_).md>) — Returns a DTD node representing the predefined entity declaration with the specified name.
- [- elementDeclarationForName:](<elementdeclaration(forname_).md>) — Returns the DTD node representing an element declaration for a specified element.
- [- entityDeclarationForName:](<entitydeclaration(forname_).md>) — Returns the DTD node representing the entity declaration for a specified entity.
- [- notationDeclarationForName:](<notationdeclaration(forname_).md>) — Returns the DTD node representing the notation declaration identified by the specified notation name.
