---
title: 'setAttributesWith(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/setattributeswith(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/setattributeswith(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/setattributeswith%28_%3A%29.json'
content_hash: 'sha256:81772e922af952d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# setAttributesWith(_:)

<sub>Instance Method</sub>

Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.

<sub>Mac Catalyst, macOS</sub>

```swift
func setAttributesWith(_ attributes: [String : String])
```

## Parameters

- `attributes` — A dictionary of key-value pairs where the attribute name is the key and the object value of the attribute is the dictionary value.

## Discussion

The method uses these names and object values to create [XMLNode](../xmlnode.md) objects of kind [NSXMLAttributeKind](../xmlnode/kind-swift.enum/attribute.md). Existing attributes are removed.

## See Also

### Handling Attributes

- [- addAttribute:](<addattribute(__).md>) — Adds an attribute node to the receiver.
- [- attributeForName:](<attribute(forname_).md>) — Returns the attribute node of the receiver with the specified name.
- [- attributeForLocalName:URI:](<attribute(forlocalname_uri_).md>) — Returns the attribute node of the receiver that is identified by a local name and URI.
- [attributes](attributes.md) — Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [- removeAttributeForName:](<removeattribute(forname_).md>) — Removes an attribute node identified by name.
- [- setAttributesAsDictionary:](<setattributesas(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary. _(deprecated)_
