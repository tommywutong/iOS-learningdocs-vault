---
title: 'attribute(forLocalName:uri:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/attribute(forlocalname:uri:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/attribute(forlocalname:uri:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/attribute%28forlocalname%3Auri%3A%29.json'
content_hash: 'sha256:d5187cf667e0ead4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# attribute(forLocalName:uri:)

<sub>Instance Method</sub>

Returns the attribute node of the receiver that is identified by a local name and URI.

<sub>Mac Catalyst, macOS</sub>

```swift
func attribute(forLocalName localName: String, uri URI: String?) -> XMLNode?
```

## Parameters

- `localName` — A string specifying the local name of an attribute.

- `URI` — A sting identifying the URI associated with an attribute.

## Return Value

An XML node object representing a matching attribute or `nil` if no such node was found.

## See Also

### Handling Attributes

- [- addAttribute:](<addattribute(__).md>) — Adds an attribute node to the receiver.
- [- attributeForName:](<attribute(forname_).md>) — Returns the attribute node of the receiver with the specified name.
- [attributes](attributes.md) — Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [- removeAttributeForName:](<removeattribute(forname_).md>) — Removes an attribute node identified by name.
- [- setAttributesWithDictionary:](<setattributeswith(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [- setAttributesAsDictionary:](<setattributesas(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary. _(deprecated)_
