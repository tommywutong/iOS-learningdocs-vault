---
title: 'init(name:uri:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/init(name:uri:)-1r286'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/init(name:uri:)-1r286'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/init%28name%3Auri%3A%29-1r286.json'
content_hash: 'sha256:8b6f9f78b9e15f35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# init(name:uri:)

<sub>Initializer</sub>

Returns an `NSXMLElement` object initialized with the specified name and URI.

<sub>Mac Catalyst, macOS</sub>

```swift
init(name: String, uri URI: String?)
```

## Parameters

- `name` — A string that specifies the qualified name of the element.

- `URI` — A string that specifies the namespace URI associated with the element.

## Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

## Discussion

You can look up the namespace prefix for this element node based on its URI using [- resolvePrefixForNamespaceURI:](<resolveprefix(fornamespaceuri_).md>).  This method is the primary initializer for the `NSXMLElement` class.

## See Also

### Initializing NSXMLElement Objects

- [- initWithName:](<init(name_).md>) — Returns an `NSXMLElement` object initialized with the specified name.
- [- initWithName:stringValue:](<init(name_stringvalue_).md>) — Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [- initWithXMLString:error:](<init(xmlstring_)-7vkg7.md>) — Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [- initWithKind:options:](<init(kind_options_).md>)
