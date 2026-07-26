---
title: 'compare(document:toDocument:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-3wkjv/compare(document:todocument:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/compare(document:todocument:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/compare%28document%3Atodocument%3A%29.json'
content_hash: 'sha256:9792ed190d5c718a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# compare(document:toDocument:)

<sub>Instance Method</sub>

Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func compare(document: Self.DocumentIdentifier, toDocument: Self.DocumentIdentifier) -> ComparisonResult
```

## Parameters

- `document` — A string that uniquely identifies the document to compare from.

- `toDocument` — A string that uniquely identifies the document to compare to.

## Return Value

Returns the result of comparing the two documents.

## Discussion

The system calls this method during a find session to determine which document’s ranges to highlight next when a user taps the “next” or “previous” button. Return [ComparisonResult.orderedAscending](../../foundation/comparisonresult/orderedascending.md) if the text ranges found in the `fromDocument` come before those found in the `toDocument` in your view. Otherwise, return [ComparisonResult.orderedDescending](../../foundation/comparisonresult/ordereddescending.md).

The system only calls this method if you provide document identifiers to the session’s result aggregator.

## Default Implementations

### UITextSearching Implementations

- [compare(document:toDocument:)](<compare(document_todocument_)-8h4x9.md>)

## See Also

### Handling searches

- [performTextSearch(queryString:options:resultAggregator:)](<performtextsearch(querystring_options_resultaggregator_).md>) — Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md) — The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [compare(_:toRange:document:)](<compare(__torange_document_).md>) — Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [DocumentIdentifier](documentidentifier.md) — An object that uniquely identifies a specific document when searching for matching text across multiple documents.
