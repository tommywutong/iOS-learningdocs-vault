---
title: xPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/xpath
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/xpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/xpath.json'
content_hash: 'sha256:1bf7f4372bfe122e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# xPath

<sub>Instance Property</sub>

Returns the XPath expression identifying the receiver’s location in the document tree.

<sub>Mac Catalyst, macOS</sub>

```swift
var xPath: String? { get }
```

## Discussion

For example, this method might return a string such as “foo/bar[2]/baz”. The result of this method can be used directly in the [- nodesForXPath:error:](<nodes(forxpath_).md>) and [- objectsForXQuery:constants:error:](<objects(forxquery_constants_).md>) methods.

## See Also

### Executing Queries

- [- nodesForXPath:error:](<nodes(forxpath_).md>) — Returns the nodes resulting from executing an XPath query upon the receiver.
- [- objectsForXQuery:error:](<objects(forxquery_).md>) — Returns the objects resulting from executing an XQuery query upon the receiver.
- [- objectsForXQuery:constants:error:](<objects(forxquery_constants_).md>) — Returns the objects resulting from executing an XQuery query upon the receiver.
