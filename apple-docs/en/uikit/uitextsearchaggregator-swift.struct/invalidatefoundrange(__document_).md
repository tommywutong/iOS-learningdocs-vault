---
title: 'invalidateFoundRange(_:document:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearchaggregator-swift.struct/invalidatefoundrange(_:document:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/invalidatefoundrange(_:document:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-swift.struct/invalidatefoundrange%28_%3Adocument%3A%29.json'
content_hash: 'sha256:132a5670d2165480'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md)

# invalidateFoundRange(_:document:)

<sub>Instance Method</sub>

Removes a text range from the set of matches.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func invalidateFoundRange(_ range: UITextRange, document: DocumentIdentifier)
```

## Parameters

- `range` — The text range to remove from the set of matches.

- `document` — A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## Discussion

Call this method to invalidate a text range when removing or changing text in the document. This causes the system find panel to update it’s current state, and if the range is the highlighted range, the find panel advances to the next found result.

## See Also

### Tracking search results

- [foundRange(_:searchString:document:)](<foundrange(__searchstring_document_).md>) — Adds a text range to the set of matches.
- [invalidate()](<invalidate().md>) — Invalidates all currently shown ranges.
- [finishedSearching()](<finishedsearching().md>) — Finishes the search for text ranges.
- [allFoundRanges](allfoundranges.md) — An ordered set of all the text ranges that match the search.
