---
title: attributes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlelement/attributes
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/attributes.json'
content_hash: 'sha256:ce0e61f5b292da25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# attributes

<sub>Instance Property</sub>

Sets all attributes of the receiver at once, replacing any existing attribute nodes.

<sub>Mac Catalyst, macOS</sub>

```swift
var attributes: [XMLNode]? { get set }
```

## Parameters

- `attributes` — An array of [XMLNode](../xmlnode.md) objects of kind [NSXMLAttributeKind](../xmlnode/kind-swift.enum/attribute.md). If there are attribute nodes with the same name, the first attribute with that name is used. Send this message with `attributes` as `nil` to remove all attributes.

## Discussion

To set attributes in an element node using an [NSDictionary](../nsdictionary.md) object as the input parameter, see [- setAttributesWithDictionary:](<setattributeswith(__).md>).

## See Also

### Handling Attributes

- [- addAttribute:](<addattribute(__).md>) — Adds an attribute node to the receiver.
- [- attributeForName:](<attribute(forname_).md>) — Returns the attribute node of the receiver with the specified name.
- [- attributeForLocalName:URI:](<attribute(forlocalname_uri_).md>) — Returns the attribute node of the receiver that is identified by a local name and URI.
- [- removeAttributeForName:](<removeattribute(forname_).md>) — Removes an attribute node identified by name.
- [- setAttributesWithDictionary:](<setattributeswith(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [- setAttributesAsDictionary:](<setattributesas(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary. _(deprecated)_
