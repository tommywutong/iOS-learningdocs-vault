---
title: 'init(xmlString:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlelement/init(xmlstring:)-7vkg7'
source_url: 'https://developer.apple.com/documentation/foundation/xmlelement/init(xmlstring:)-7vkg7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlelement/init%28xmlstring%3A%29-7vkg7.json'
content_hash: 'sha256:0efbe48222b601e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLElement](../xmlelement.md)

# init(xmlString:)

<sub>Initializer</sub>

Returns an `NSXMLElement` object created from a specified string containing XML markup.

<sub>Mac Catalyst, macOS</sub>

```swift
init(xmlString string: String) throws
```

## Parameters

- `string` — A string containing XML markup for an element.

## Return Value

The initialized `NSXMLElement` object or `nil` if initialization did not succeed.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Initializing NSXMLElement Objects

- [- initWithName:](<init(name_).md>) — Returns an `NSXMLElement` object initialized with the specified name.
- [- initWithName:stringValue:](<init(name_stringvalue_).md>) — Returns an `NSXMLElement` object initialized with a specified name and a single text-node child containing a specified value.
- [- initWithName:URI:](<init(name_uri_)-1r286.md>) — Returns an `NSXMLElement` object initialized with the specified name and URI.
- [- initWithKind:options:](<init(kind_options_).md>)
