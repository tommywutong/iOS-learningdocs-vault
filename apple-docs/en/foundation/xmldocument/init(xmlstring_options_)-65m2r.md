---
title: 'init(xmlString:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldocument/init(xmlstring:options:)-65m2r'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/init(xmlstring:options:)-65m2r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/init%28xmlstring%3Aoptions%3A%29-65m2r.json'
content_hash: 'sha256:5ddfe3fd4d8fd5e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# init(xmlString:options:)

<sub>Initializer</sub>

Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.

<sub>Mac Catalyst, macOS</sub>

```swift
convenience init(xmlString string: String, options mask: XMLNode.Options = []) throws
```

## Parameters

- `string` — A string object containing XML markup text.

- `mask` — A bit mask for input options. You can specify multiple options by bit-OR’ing them. See Constants for a list of valid input options.

## Return Value

An initialized `NSXMLDocument` object, or `nil` if initialization fails because of parsing errors or other reasons.

## Discussion

The encoding of the document is set to UTF-8.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Initializing NSXMLDocument Objects

- [- initWithContentsOfURL:options:error:](<init(contentsof_options_).md>) — Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source
- [- initWithData:options:error:](<init(data_options_).md>) — Initializes and returns an `NSXMLDocument` object created from an [NSData](../nsdata.md) object.
- [- initWithRootElement:](<init(rootelement_).md>) — Returns an `NSXMLDocument` object initialized with a single child, the root element.
- [+ replacementClassForClass:](<replacementclass(for_).md>) — Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.
