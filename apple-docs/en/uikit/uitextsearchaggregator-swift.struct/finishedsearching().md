---
title: finishedSearching()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchaggregator-swift.struct/finishedsearching()
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/finishedsearching()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-swift.struct/finishedsearching%28%29.json'
content_hash: 'sha256:fc6414e70a7b49dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md)

# finishedSearching()

<sub>Instance Method</sub>

Finishes the search for text ranges.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func finishedSearching()
```

## Discussion

Call this method after searching all documents.

## See Also

### Tracking search results

- [foundRange(_:searchString:document:)](<foundrange(__searchstring_document_).md>) — Adds a text range to the set of matches.
- [invalidateFoundRange(_:document:)](<invalidatefoundrange(__document_).md>) — Removes a text range from the set of matches.
- [invalidate()](<invalidate().md>) — Invalidates all currently shown ranges.
- [allFoundRanges](allfoundranges.md) — An ordered set of all the text ranges that match the search.
