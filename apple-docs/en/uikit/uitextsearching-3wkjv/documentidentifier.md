---
title: DocumentIdentifier
framework: UIKit
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearching-3wkjv/documentidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/documentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/documentidentifier.json'
content_hash: 'sha256:9b774656aaa504b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# DocumentIdentifier

<sub>Associated Type</sub>

An object that uniquely identifies a specific document when searching for matching text across multiple documents.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
associatedtype DocumentIdentifier : Hashable = AnyHashable?
```

## Discussion

The [UITextSearching](../uitextsearching-53wjq.md) and [UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md) protocols use this type to distinguish matches in a specific document from text in other documents with the same range.

## See Also

### Handling searches

- [performTextSearch(queryString:options:resultAggregator:)](<performtextsearch(querystring_options_resultaggregator_).md>) — Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md) — The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [compare(_:toRange:document:)](<compare(__torange_document_).md>) — Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [compare(document:toDocument:)](<compare(document_todocument_).md>) — Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
