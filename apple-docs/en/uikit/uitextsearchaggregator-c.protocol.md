---
title: UITextSearchAggregator
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchaggregator-c.protocol
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-c.protocol.json'
content_hash: 'sha256:06a7c90a5f5c5bf7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSearchAggregator

<sub>Protocol</sub>

The methods you use on a find session’s aggregator to collect matching text ranges for a search.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@protocol UITextSearchAggregator <NSObject>
```

## Overview

To track text ranges that match the search, call these methods on the aggregator for the searchable object implementing the [UITextSearching](uitextsearching-53wjq.md) protocol for a [UITextSearchingFindSession](uitextsearchingfindsession.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Tracking search results

- [foundRange:forSearchString:inDocument:](uitextsearchaggregator-c.protocol/foundrange_forsearchstring_indocument_.md) — Adds a text range to the set of matches.
- [invalidateFoundRange:inDocument:](uitextsearchaggregator-c.protocol/invalidatefoundrange_indocument_.md) — Removes a text range from the set of matches.
- [invalidate](uitextsearchaggregator-c.protocol/invalidate.md) — Invalidates all currently shown ranges.
- [finishedSearching](uitextsearchaggregator-c.protocol/finishedsearching.md) — Finishes the search for text ranges.
- [allFoundRanges](uitextsearchaggregator-c.protocol/allfoundranges.md) — An ordered set of all the text ranges that match the search.

## See Also

### Handling searches

- [performTextSearchWithQueryString:usingOptions:resultAggregator:](uitextsearching-53wjq/performtextsearchwithquerystring_usingoptions_resultaggregator_.md) — Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [compareFoundRange:toRange:inDocument:](uitextsearching-53wjq/comparefoundrange_torange_indocument_.md) — Compares ranges from the set of matches the aggregator provides to determine navigation order.
- [compareOrderFromDocument:toDocument:](uitextsearching-53wjq/compareorderfromdocument_todocument_.md) — Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [UITextSearchDocumentIdentifier](uitextsearchdocumentidentifier.md) — A string that uniquely identifies a specific document when searching for matching text across multiple documents.
