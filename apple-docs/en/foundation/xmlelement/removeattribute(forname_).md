---
title: 'removeAttribute(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/removeattribute(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/removeattribute(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/removeattribute%28forname%3A%29.json'
content_hash: 'sha256:b50066cc938c8b0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# removeAttribute(forName:)

<sub>Instance Method</sub>

Removes an attribute node identified by name.

<sub>Mac Catalyst, macOS</sub>

```swift
func removeAttribute(forName name: String)
```

## Parameters

- `name` — A string specifying the name of an attribute.

## See Also

### Handling Attributes

- [- addAttribute:](<addattribute(__).md>) — Adds an attribute node to the receiver.
- [- attributeForName:](<attribute(forname_).md>) — Returns the attribute node of the receiver with the specified name.
- [- attributeForLocalName:URI:](<attribute(forlocalname_uri_).md>) — Returns the attribute node of the receiver that is identified by a local name and URI.
- [attributes](attributes.md) — Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [- setAttributesWithDictionary:](<setattributeswith(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [- setAttributesAsDictionary:](<setattributesas(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary. _(deprecated)_
