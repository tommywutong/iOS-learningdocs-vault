---
title: 'attribute(forName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/attribute(forname:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/attribute(forname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/attribute%28forname%3A%29.json'
content_hash: 'sha256:9cfd29bbbfca76eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# attribute(forName:)

<sub>Instance Method</sub>

Returns the attribute node of the receiver with the specified name.

<sub>Mac Catalyst, macOS</sub>

```swift
func attribute(forName name: String) -> XMLNode?
```

## Parameters

- `name` — A string specifying the name of an attribute.

## Return Value

An XML node object representing a matching attribute or `nil` if no such node was found.

## Discussion

If `name` is a qualified name, then this method invokes [- attributeForLocalName:URI:](<attribute(forlocalname_uri_).md>) with the URI parameter set to the URI associated with the prefix. Otherwise comparison is based on string equality of the qualified or non-qualified name.

## See Also

### Handling Attributes

- [- addAttribute:](<addattribute(__).md>) — Adds an attribute node to the receiver.
- [- attributeForLocalName:URI:](<attribute(forlocalname_uri_).md>) — Returns the attribute node of the receiver that is identified by a local name and URI.
- [attributes](attributes.md) — Sets all attributes of the receiver at once, replacing any existing attribute nodes.
- [- removeAttributeForName:](<removeattribute(forname_).md>) — Removes an attribute node identified by name.
- [- setAttributesWithDictionary:](<setattributeswith(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed dictionary.
- [- setAttributesAsDictionary:](<setattributesas(__).md>) — Sets the attributes of the receiver based on the key-value pairs specified in the passed-in dictionary. _(deprecated)_
