---
title: selectedTextSearchDocument
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearching-3wkjv/selectedtextsearchdocument
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/selectedtextsearchdocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/selectedtextsearchdocument.json'
content_hash: 'sha256:371ff5be6c735039'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# selectedTextSearchDocument

<sub>Instance Property</sub>

The object that uniquely identifies the specific document with selected text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var selectedTextSearchDocument: Self.DocumentIdentifier? { get }
```

## Discussion

When performing a search across multiple documents, this object returns the identifier for the document with the selected text. When performing a search on a single document, it returns `nil`.

## Default Implementations

### UITextSearching Implementations

- [selectedTextSearchDocument](selectedtextsearchdocument-72uzm.md)

## See Also

### Identifying selected text

- [selectedTextRange](selectedtextrange.md) — The range of selected text in a document.
