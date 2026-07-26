---
title: 'objects(forXQuery:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmlnode/objects(forxquery:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/objects(forxquery:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/objects%28forxquery%3A%29.json'
content_hash: 'sha256:00eb225d39957ac6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# objects(forXQuery:)

<sub>Instance Method</sub>

Returns the objects resulting from executing an XQuery query upon the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func objects(forXQuery xquery: String) throws -> [Any]
```

## Parameters

- `xquery` — A string that expresses an XQuery query.

## Discussion

The receiver acts as the context item for the query (”.”).  If the receiver has been changed after parsing to have multiple adjacent text nodes, you should invoke the `NSXMLElement` method [- normalizeAdjacentTextNodesPreservingCDATA:](<../xmlelement/normalizeadjacenttextnodespreservingcdata(__).md>) (with an argument of [false](../../swift/false.md)) to coalesce the text nodes before querying .This convenience method invokes [- objectsForXQuery:constants:error:](<objects(forxquery_constants_).md>) with `nil` for the `constants` dictionary.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Executing Queries

- [- nodesForXPath:error:](<nodes(forxpath_).md>) — Returns the nodes resulting from executing an XPath query upon the receiver.
- [- objectsForXQuery:constants:error:](<objects(forxquery_constants_).md>) — Returns the objects resulting from executing an XQuery query upon the receiver.
- [XPath](xpath.md) — Returns the XPath expression identifying the receiver’s location in the document tree.
