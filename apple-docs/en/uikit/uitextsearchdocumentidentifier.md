---
title: UITextSearchDocumentIdentifier
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchdocumentidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchdocumentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchdocumentidentifier.json'
content_hash: 'sha256:f4dd668604781445'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSearchDocumentIdentifier

<sub>Type Alias</sub>

A string that uniquely identifies a specific document when searching for matching text across multiple documents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef id<NSCopying,NSObject> UITextSearchDocumentIdentifier;
```

## Discussion

The [UITextSearching](uitextsearching-53wjq.md) and [UITextSearchAggregator](uitextsearchaggregator-swift.struct.md) protocols use this type to distinguish matches in a specific document from text in other documents with the same range.

## See Also

### Handling searches

- [performTextSearchWithQueryString:usingOptions:resultAggregator:](uitextsearching-53wjq/performtextsearchwithquerystring_usingoptions_resultaggregator_.md) — Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [UITextSearchAggregator](uitextsearchaggregator-c.protocol.md) — The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [compareFoundRange:toRange:inDocument:](uitextsearching-53wjq/comparefoundrange_torange_indocument_.md) — Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [compareOrderFromDocument:toDocument:](uitextsearching-53wjq/compareorderfromdocument_todocument_.md) — Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
