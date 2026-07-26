---
title: 'setAttributesAs(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/xmlelement/setattributesas(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/setattributesas(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/setattributesas%28_%3A%29.json'
content_hash: 'sha256:64350cbb82dbc7be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# setAttributesAs(_:)

<sub>Instance Method</sub>

Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary.

> [!warning] Deprecated
> This method is deprecated because it does not function properly. Instead use [- setAttributesWithDictionary:](<setattributeswith(__).md>).

<sub>Mac Catalyst, macOS</sub>

```swift
func setAttributesAs(_ attributes: [AnyHashable : Any])
```

## Parameters

- `attributes` — A dictionary of key-value pairs where the attribute name is the key and the object value of the attribute is the dictionary value.

## Discussion

The method uses these names and object values to create [XMLNode](../xmlnode.md) objects of kind [NSXMLAttributeKind](../xmlnode/kind-swift.enum/attribute.md). Existing attributes are not removed.

## See Also

### Handling Attributes

- [- addAttribute:](<addattribute(__).md>) — Adds an attribute node to the receiver.
- [- attributeForName:](<attribute(forname_).md>) — Returns the attribute node of the receiver with the specified name.
- [- attributeForLocalName:URI:](<attribute(forlocalname_uri_).md>) — Returns the attribute node of the receiver that is identified by a local name and URI.
- [attributes](attributes.md) — Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [- removeAttributeForName:](<removeattribute(forname_).md>) — Removes an attribute node identified by name.
- [- setAttributesWithDictionary:](<setattributeswith(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
