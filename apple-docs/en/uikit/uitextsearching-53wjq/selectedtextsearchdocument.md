---
title: selectedTextSearchDocument
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearching-53wjq/selectedtextsearchdocument
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/selectedtextsearchdocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-53wjq/selectedtextsearchdocument.json'
content_hash: 'sha256:a27aa190fab608de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-53wjq.md)

# selectedTextSearchDocument

<sub>Instance Property</sub>

The object that uniquely identifies the specific document with selected text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly, nullable) UITextSearchDocumentIdentifier selectedTextSearchDocument;
```

## Discussion

When performing a search across multiple documents, this object returns the identifier for the document with the selected text. When performing a search on a single document, it returns `nil`.

## See Also

### Identifying selected text

- [selectedTextRange](selectedtextrange.md) — The range of selected text in a document.
