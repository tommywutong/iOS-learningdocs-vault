---
title: finishedSearching
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchaggregator-c.protocol/finishedsearching
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol/finishedsearching'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-c.protocol/finishedsearching.json'
content_hash: 'sha256:2a44b0c09af45391'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchAggregator](../uitextsearchaggregator-c.protocol.md)

# finishedSearching

<sub>Instance Method</sub>

Finishes the search for text ranges.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) finishedSearching;
```

## Discussion

Call this method after searching all documents.

## See Also

### Tracking search results

- [foundRange:forSearchString:inDocument:](foundrange_forsearchstring_indocument_.md) — Adds a text range to the set of matches.
- [invalidateFoundRange:inDocument:](invalidatefoundrange_indocument_.md) — Removes a text range from the set of matches.
- [invalidate](invalidate.md) — Invalidates all currently shown ranges.
- [allFoundRanges](allfoundranges.md) — An ordered set of all the text ranges that match the search.
