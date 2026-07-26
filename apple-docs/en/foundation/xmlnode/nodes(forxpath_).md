---
title: 'nodes(forXPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlnode/nodes(forxpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/nodes(forxpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/nodes%28forxpath%3A%29.json'
content_hash: 'sha256:5dfb3f03bf072c78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# nodes(forXPath:)

<sub>Instance Method</sub>

Returns the nodes resulting from executing an XPath query upon the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func nodes(forXPath xpath: String) throws -> [XMLNode]
```

## Parameters

- `xpath` — A string that expresses an XPath query.

## Return Value

An array of `NSXMLNode` objects that match the query, or an empty array if there are no matches.

## Discussion

The receiver acts as the context item for the query (”.”).  If you have explicitly added adjacent text nodes as children of an element, you should invoke the `NSXMLElement` method [- normalizeAdjacentTextNodesPreservingCDATA:](<../xmlelement/normalizeadjacenttextnodespreservingcdata(__).md>) (with an argument of [false](../../swift/false.md)) on the element before applying any XPath queries to it; this method coalesces these text nodes. The same precaution applies if you have processed a document preserving CDATA sections and these sections are adjacent to text nodes.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Executing Queries

- [- objectsForXQuery:error:](<objects(forxquery_).md>) — Returns the objects resulting from executing an XQuery query upon the receiver.
- [- objectsForXQuery:constants:error:](<objects(forxquery_constants_).md>) — Returns the objects resulting from executing an XQuery query upon the receiver.
- [XPath](xpath.md) — Returns the XPath expression identifying the receiver’s location in the document tree.
