---
title: 'init(name:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/init(name:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/init(name:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/init%28name%3A%29.json'
content_hash: 'sha256:b4329b9500798885'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# init(name:)

<sub>Initializer</sub>

Returns an `NSXMLElement` object initialized with the specified name.

<sub>Mac Catalyst, macOS</sub>

```swift
convenience init(name: String)
```

## Parameters

- `name` — A string specifying the name of the element.

## Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

## Discussion

The XML string representation of this object is `<``name``></``name``>`. This method invokes [- initWithName:URI:](<init(name_uri_)-1r286.md>) with the URI parameter set to `nil`.

## See Also

### Related Documentation

- [Tree-Based XML Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html#//apple_ref/doc/uid/TP40001269)

### Initializing NSXMLElement Objects

- [- initWithName:stringValue:](<init(name_stringvalue_).md>) — Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [- initWithName:URI:](<init(name_uri_)-1r286.md>) — Returns an `NSXMLElement` object initialized with the specified name and URI.
- [- initWithXMLString:error:](<init(xmlstring_)-7vkg7.md>) — Returns an `NSXMLElement` object created from a specified string containing XML markup.
- [- initWithKind:options:](<init(kind_options_).md>)
