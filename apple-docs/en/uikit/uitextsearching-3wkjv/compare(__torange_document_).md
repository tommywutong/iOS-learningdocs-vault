---
title: 'compare(_:toRange:document:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-3wkjv/compare(_:torange:document:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/compare(_:torange:document:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/compare%28_%3Atorange%3Adocument%3A%29.json'
content_hash: 'sha256:aa4d4dc01a7e33b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# compare(_:toRange:document:)

<sub>Instance Method</sub>

Compares ranges from the set of matches the aggregator provides to determine navigation order.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func compare(_ foundRange: UITextRange, toRange: UITextRange, document: Self.DocumentIdentifier?) -> ComparisonResult
```

## Parameters

- `foundRange` — The range of characters in a text container to compare from.

- `toRange` — The range of characters in a text container to compare to.

- `document` — A string that uniquely identifies the document containing the text ranges. `Nil` when searching a single document.

## Return Value

Returns the result of comparing the two text ranges.

## Discussion

The system calls this method during a find session to determine which [UITextRange](../uitextrange.md) to highlight next when a user taps the “next” or “previous” button.

## See Also

### Handling searches

- [performTextSearch(queryString:options:resultAggregator:)](<performtextsearch(querystring_options_resultaggregator_).md>) — Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md) — The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [compare(document:toDocument:)](<compare(document_todocument_).md>) — Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [DocumentIdentifier](documentidentifier.md) — An object that uniquely identifies a specific document when searching for matching text across multiple documents.
