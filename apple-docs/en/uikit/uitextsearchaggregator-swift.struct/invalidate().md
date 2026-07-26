---
title: invalidate()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchaggregator-swift.struct/invalidate()
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/invalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-swift.struct/invalidate%28%29.json'
content_hash: 'sha256:d86e882581b69f9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md)

# invalidate()

<sub>Instance Method</sub>

Invalidates all currently shown ranges.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func invalidate()
```

## Discussion

Calling this method causes the system find panel to update its current state, and might trigger a new search using [performTextSearch(queryString:options:resultAggregator:)](<../uitextsearching-3wkjv/performtextsearch(querystring_options_resultaggregator_).md>) (Swift) or [performTextSearchWithQueryString:usingOptions:resultAggregator:](../uitextsearching-53wjq/performtextsearchwithquerystring_usingoptions_resultaggregator_.md) (Objective-C) immediately after.

## See Also

### Tracking search results

- [foundRange(_:searchString:document:)](<foundrange(__searchstring_document_).md>) — Adds a text range to the set of matches.
- [invalidateFoundRange(_:document:)](<invalidatefoundrange(__document_).md>) — Removes a text range from the set of matches.
- [finishedSearching()](<finishedsearching().md>) — Finishes the search for text ranges.
- [allFoundRanges](allfoundranges.md) — An ordered set of all the text ranges that match the search.
