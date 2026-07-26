---
title: 'performTextSearch(queryString:options:resultAggregator:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-3wkjv/performtextsearch(querystring:options:resultaggregator:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-3wkjv/performtextsearch(querystring:options:resultaggregator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-3wkjv/performtextsearch%28querystring%3Aoptions%3Aresultaggregator%3A%29.json'
content_hash: 'sha256:b4474970f356a66f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-3wkjv.md)

# performTextSearch(queryString:options:resultAggregator:)

<sub>Instance Method</sub>

Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func performTextSearch(queryString: String, options: UITextSearchOptions, resultAggregator: UITextSearchAggregator<Self.DocumentIdentifier>)
```

## Parameters

- `queryString` — The string to search for.

- `options` — The configurable options to use for matching words and comparing strings.

- `resultAggregator` — An object you use to collect matching results. The aggregator is thread-safe, so you may send it messages on other threads.

## Discussion

The system calls this method during a find session to perform the search. Your implenentation should search for matching text ranges in your app’s documents and call [foundRange(_:searchString:document:)](<../uitextsearchaggregator-swift.struct/foundrange(__searchstring_document_).md>) on the aggregator object to add them to the set of matching ranges.

## See Also

### Handling searches

- [UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md) — The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [compare(_:toRange:document:)](<compare(__torange_document_).md>) — Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [compare(document:toDocument:)](<compare(document_todocument_).md>) — Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [DocumentIdentifier](documentidentifier.md) — An object that uniquely identifies a specific document when searching for matching text across multiple documents.
