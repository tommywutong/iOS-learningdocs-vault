---
title: UITextSearchAggregator
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchaggregator-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-swift.struct.json'
content_hash: 'sha256:d7a32044dbf87807'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSearchAggregator

<sub>Structure</sub>

The methods you use on a find session’s aggregator to collect matching text ranges for a search.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct UITextSearchAggregator<DocumentIdentifier> where DocumentIdentifier : Hashable
```

## Overview

To track text ranges that match the search, call these methods on the aggregator for the searchable object implementing the [UITextSearching](uitextsearching-53wjq.md) protocol for a [UITextSearchingFindSession](uitextsearchingfindsession.md).

## Topics

### Tracking search results

- [foundRange(_:searchString:document:)](<uitextsearchaggregator-swift.struct/foundrange(__searchstring_document_).md>) — Adds a text range to the set of matches.
- [invalidateFoundRange(_:document:)](<uitextsearchaggregator-swift.struct/invalidatefoundrange(__document_).md>) — Removes a text range from the set of matches.
- [invalidate()](<uitextsearchaggregator-swift.struct/invalidate().md>) — Invalidates all currently shown ranges.
- [finishedSearching()](<uitextsearchaggregator-swift.struct/finishedsearching().md>) — Finishes the search for text ranges.
- [allFoundRanges](uitextsearchaggregator-swift.struct/allfoundranges.md) — An ordered set of all the text ranges that match the search.

## See Also

### Handling searches

- [performTextSearch(queryString:options:resultAggregator:)](<uitextsearching-3wkjv/performtextsearch(querystring_options_resultaggregator_).md>) — Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [compare(_:toRange:document:)](<uitextsearching-3wkjv/compare(__torange_document_).md>) — Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [compare(document:toDocument:)](<uitextsearching-3wkjv/compare(document_todocument_).md>) — Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [DocumentIdentifier](uitextsearching-3wkjv/documentidentifier.md) — An object that uniquely identifies a specific document when searching for matching text across multiple documents.
