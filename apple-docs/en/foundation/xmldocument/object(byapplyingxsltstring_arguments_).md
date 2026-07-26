---
title: 'object(byApplyingXSLTString:arguments:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldocument/object(byapplyingxsltstring:arguments:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/object(byapplyingxsltstring:arguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/object%28byapplyingxsltstring%3Aarguments%3A%29.json'
content_hash: 'sha256:8e60651642ff1ca9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# object(byApplyingXSLTString:arguments:)

<sub>Instance Method</sub>

Applies the XSLT pattern rules and templates (specified as a string) to the receiver and returns a document object containing transformed XML or HTML markup.

<sub>Mac Catalyst, macOS</sub>

```swift
func object(byApplyingXSLTString xslt: String, arguments: [String : String]?) throws -> Any
```

## Parameters

- `xslt` — A string object containing the XSLT pattern rules and templates.

- `arguments` — A dictionary containing [NSString](../nsstring.md) key-value pairs that are passed as runtime parameters to the XSLT processor. Pass in `nil` if you have no parameters to pass. > [!note] Note > Several XML websites discuss XSLT parameters, including O’Reilly Media’s [http://www.xml.com](http://www.xml.com).

## Return Value

Depending on intended output, the method returns an `NSXMLDocument` object _or_ an [NSData](../nsdata.md) data containing transformed XML or HTML markup. If the message is supposed to create plain text or RTF, then an `NSData` object is returned, otherwise an XML document object. The method returns  `nil` if XSLT processing did not succeed.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Transforming a Document Using XSLT

- [- objectByApplyingXSLT:arguments:error:](<object(byapplyingxslt_arguments_).md>) — Applies the XSLT pattern rules and templates (specified as a data object) to the receiver and returns a document object containing transformed XML or HTML markup.
- [- objectByApplyingXSLTAtURL:arguments:error:](<objectbyapplyingxslt(at_arguments_).md>) — Applies the XSLT pattern rules and templates located at a specified URL to the receiver and returns a document object containing transformed XML markup or an [NSData](../nsdata.md) object containing plain text, RTF text, and so on.
