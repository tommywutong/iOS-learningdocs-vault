---
title: 'performTextSearchWithQueryString:usingOptions:resultAggregator:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-53wjq/performtextsearchwithquerystring:usingoptions:resultaggregator:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/performtextsearchwithquerystring:usingoptions:resultaggregator:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-53wjq/performtextsearchwithquerystring%3Ausingoptions%3Aresultaggregator%3A.json'
content_hash: 'sha256:60fd702bf8215a85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-53wjq.md)

# performTextSearchWithQueryString:usingOptions:resultAggregator:

<sub>Instance Method</sub>

Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) performTextSearchWithQueryString:(NSString *) string usingOptions:(UITextSearchOptions *) options resultAggregator:(id<UITextSearchAggregator>) aggregator;
```

## Parameters

- `string` — The string to search for.

- `options` — The configurable options to use for matching words and comparing strings.

- `aggregator` — An object you use to collect matching results. The aggregator is thread-safe, so you may send it messages on other threads.

## Discussion

The system calls this method during a find session to perform the search. Your implenentation should search for matching text ranges in your app’s documents and call [foundRange(_:searchString:document:)](<../uitextsearchaggregator-swift.struct/foundrange(__searchstring_document_).md>) on the aggregator object to add them to the set of matching ranges.

## See Also

### Handling searches

- [UITextSearchAggregator](../uitextsearchaggregator-c.protocol.md) — The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [compareFoundRange:toRange:inDocument:](comparefoundrange_torange_indocument_.md) — Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [compareOrderFromDocument:toDocument:](compareorderfromdocument_todocument_.md) — Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [UITextSearchDocumentIdentifier](../uitextsearchdocumentidentifier.md) — A string that uniquely identifies a specific document when searching for matching text across multiple documents.
