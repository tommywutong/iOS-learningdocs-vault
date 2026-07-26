---
title: invalidate
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchaggregator-c.protocol/invalidate
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol/invalidate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-c.protocol/invalidate.json'
content_hash: 'sha256:54e2a02b7f98bc7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchAggregator](../uitextsearchaggregator-c.protocol.md)

# invalidate

<sub>Instance Method</sub>

Invalidates all currently shown ranges.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) invalidate;
```

## Discussion

Calling this method causes the system find panel to update its current state, and might trigger a new search using [performTextSearchWithQueryString:usingOptions:resultAggregator:](../uitextsearching-53wjq/performtextsearchwithquerystring_usingoptions_resultaggregator_.md) immediately after.

## See Also

### Tracking search results

- [foundRange:forSearchString:inDocument:](foundrange_forsearchstring_indocument_.md) — Adds a text range to the set of matches.
- [invalidateFoundRange:inDocument:](invalidatefoundrange_indocument_.md) — Removes a text range from the set of matches.
- [finishedSearching](finishedsearching.md) — Finishes the search for text ranges.
- [allFoundRanges](allfoundranges.md) — An ordered set of all the text ranges that match the search.
