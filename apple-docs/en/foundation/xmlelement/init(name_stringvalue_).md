---
title: 'init(name:stringValue:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/init(name:stringvalue:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/init(name:stringvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/init%28name%3Astringvalue%3A%29.json'
content_hash: 'sha256:953b2ca12d18cc73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# init(name:stringValue:)

<sub>Initializer</sub>

Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.

<sub>Mac Catalyst, macOS</sub>

```swift
convenience init(name: String, stringValue string: String?)
```

## Parameters

- `name` — A string specifying the name of the element.

- `string` — The string value of the receiver’s text node.

## Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

## Discussion

The string representation of this object is `<``name``>``string``</``name``>`.

## See Also

### Initializing NSXMLElement Objects

- [- initWithName:](<init(name_).md>) — Returns an `NSXMLElement` object initialized with the specified name.
- [- initWithName:URI:](<init(name_uri_)-1r286.md>) — Returns an `NSXMLElement` object initialized with the specified name and URI.
- [- initWithXMLString:error:](<init(xmlstring_)-7vkg7.md>) — Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [- initWithKind:options:](<init(kind_options_).md>)
