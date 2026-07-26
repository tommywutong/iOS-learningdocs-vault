---
title: 'addAttribute(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/addattribute(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/addattribute(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/addattribute%28_%3A%29.json'
content_hash: 'sha256:eb14cf734fa39334'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# addAttribute(_:)

<sub>Instance Method</sub>

Adds an attribute node to the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func addAttribute(_ attribute: XMLNode)
```

## Parameters

- `attribute` — An XML node object representing an attribute. If the receiver already has an attribute with the same name, `anAttribute` replaces the old attribute.

## Discussion

The order of multiple attributes is preserved if the `NSXMLPreserveAttributeOrder` option is specified when the element is created.

## See Also

### Handling Attributes

- [- attributeForName:](<attribute(forname_).md>) — Returns the attribute node of the receiver with the specified name.
- [- attributeForLocalName:URI:](<attribute(forlocalname_uri_).md>) — Returns the attribute node of the receiver that is identified by a local name and URI.
- [attributes](attributes.md) — Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [- removeAttributeForName:](<removeattribute(forname_).md>) — Removes an attribute node identified by name.
- [- setAttributesWithDictionary:](<setattributeswith(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [- setAttributesAsDictionary:](<setattributesas(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary. _(deprecated)_
