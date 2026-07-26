---
title: 'init(contentsOf:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldocument/init(contentsof:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/init(contentsof:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/init%28contentsof%3Aoptions%3A%29.json'
content_hash: 'sha256:eacefc826b57dbc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# init(contentsOf:options:)

<sub>Initializer</sub>

Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source

<sub>Mac Catalyst, macOS</sub>

```swift
convenience init(contentsOf url: URL, options mask: XMLNode.Options = []) throws
```

## Parameters

- `url` — An [NSURL](../nsurl.md) object specifying a URL source.

- `mask` — A bit mask for input options. You can specify multiple options by bit-OR’ing them. See Constants for a list of valid input options.

## Return Value

An initialized `NSXMLDocument` object, or  `nil` if initialization fails because of parsing errors or other reasons.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [Tree-Based XML Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSXML_Concepts/NSXML.html#//apple_ref/doc/uid/TP40001269)

### Initializing NSXMLDocument Objects

- [- initWithData:options:error:](<init(data_options_).md>) — Initializes and returns an `NSXMLDocument` object created from an [NSData](../nsdata.md) object.
- [- initWithRootElement:](<init(rootelement_).md>) — Returns an `NSXMLDocument` object initialized with a single child, the root element.
- [- initWithXMLString:options:error:](<init(xmlstring_options_)-65m2r.md>) — Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.
- [+ replacementClassForClass:](<replacementclass(for_).md>) — Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.
