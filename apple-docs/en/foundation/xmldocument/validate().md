---
title: validate()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmldocument/validate()
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/validate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/validate%28%29.json'
content_hash: 'sha256:86b0d876104d36c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# validate()

<sub>Instance Method</sub>

Validates the document against the governing schema and returns whether the document conforms to the schema.

<sub>Mac Catalyst, macOS</sub>

```swift
func validate() throws
```

## Discussion

The constants indicating the kind of validation errors are emitted by the underlying parser; see `NSXMLParser.h` for most of these constants. If the schema is defined with a DTD, this method uses the [XMLDTD](../xmldtd.md) object set for the receiver for validation. If the schema is based on XML Schema, the method uses the URL specified as the value of the `xsi:schemaLocation` attribute of the root element.

You can validate an XML document when it is first processed by specifying the `NSXMLDocumentValidate` option when you initialize an `NSXMLDocument` object with the [- initWithContentsOfURL:options:error:](<init(contentsof_options_).md>), [- initWithData:options:error:](<init(data_options_).md>), or [- initWithXMLString:options:error:](<init(xmlstring_options_)-65m2r.md>) methods.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.
