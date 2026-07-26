---
title: 'init(data:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldtd/init(data:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldtd/init(data:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldtd/init%28data%3Aoptions%3A%29.json'
content_hash: 'sha256:67189466450dff25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDTD](../xmldtd.md)

# init(data:options:)

<sub>Initializer</sub>

Initializes and returns an `NSXMLDTD` object created from the DTD declarations encapsulated in an [NSData](../nsdata.md) object

<sub>Mac Catalyst, macOS</sub>

```swift
init(data: Data, options mask: XMLNode.Options = []) throws
```

## Parameters

- `data` — A data object containing DTD declarations.

- `mask` — A bit mask specifying input options; bit-OR multiple options. The current valid options are `NSXMLNodePreserveWhitespace` and `NSXMLNodePreserveEntities`; these constants are described in the “Constants” section of the [XMLNode](../xmlnode.md) reference.

## Return Value

An initialized `NSXMLDTD` object or `nil` if initialization fails because of parsing errors or other reasons.

## Discussion

This method is the designated initializer for the `NSXMLDTD` class. You use this method to create a stand-alone DTD which you can thereafter query and use for validation. You can associate the DTD created through this message with a document by setting the [DTD](../xmldocument/dtd.md) property on an [XMLDocument](../xmldocument.md) object.

> [!note] Handling Errors in Swift
> In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [- validateAndReturnError:](<../xmldocument/validate().md>) — Validates the document against the governing schema and returns whether the document conforms to the schema.

### Initializing an NSXMLDTD Object

- [- initWithContentsOfURL:options:error:](<init(contentsof_options_).md>) — Initializes and returns an `NSXMLDTD` object created from the DTD declarations in a URL-referenced source.
