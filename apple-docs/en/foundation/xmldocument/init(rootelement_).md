---
title: 'init(rootElement:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldocument/init(rootelement:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/init(rootelement:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/init%28rootelement%3A%29.json'
content_hash: 'sha256:8762a020f0833cd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# init(rootElement:)

<sub>Initializer</sub>

Returns an `NSXMLDocument` object initialized with a single child, the root element.

<sub>Mac Catalyst, macOS</sub>

```swift
init(rootElement element: XMLElement?)
```

## Parameters

- `element` — An [XMLElement](../xmlelement.md) object representing an XML element.

## Return Value

An initialized `NSXMLDocument` object, or  `nil` if initialization fails for any reason.

## See Also

### Initializing NSXMLDocument Objects

- [- initWithContentsOfURL:options:error:](<init(contentsof_options_).md>) — Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source
- [- initWithData:options:error:](<init(data_options_).md>) — Initializes and returns an `NSXMLDocument` object created from an [NSData](../nsdata.md) object.
- [- initWithXMLString:options:error:](<init(xmlstring_options_)-65m2r.md>) — Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.
- [+ replacementClassForClass:](<replacementclass(for_).md>) — Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.
