---
title: allFoundRanges
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchaggregator-swift.struct/allfoundranges
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/allfoundranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-swift.struct/allfoundranges.json'
content_hash: 'sha256:a0d06c2e547e5e14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md)

# allFoundRanges

<sub>Instance Property</sub>

An ordered set of all the text ranges that match the search.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allFoundRanges: [UITextRange] { get }
```

## See Also

### Tracking search results

- [foundRange(_:searchString:document:)](<foundrange(__searchstring_document_).md>) — Adds a text range to the set of matches.
- [invalidateFoundRange(_:document:)](<invalidatefoundrange(__document_).md>) — Removes a text range from the set of matches.
- [invalidate()](<invalidate().md>) — Invalidates all currently shown ranges.
- [finishedSearching()](<finishedsearching().md>) — Finishes the search for text ranges.
