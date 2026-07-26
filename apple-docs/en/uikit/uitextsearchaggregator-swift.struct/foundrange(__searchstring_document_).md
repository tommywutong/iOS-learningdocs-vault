---
title: 'foundRange(_:searchString:document:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearchaggregator-swift.struct/foundrange(_:searchstring:document:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-swift.struct/foundrange(_:searchstring:document:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-swift.struct/foundrange%28_%3Asearchstring%3Adocument%3A%29.json'
content_hash: 'sha256:ea52a778c190f0de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchAggregator](../uitextsearchaggregator-swift.struct.md)

# foundRange(_:searchString:document:)

<sub>Instance Method</sub>

Adds a text range to the set of matches.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func foundRange(_ range: UITextRange, searchString: String, document: DocumentIdentifier)
```

## Parameters

- `range` — The text range to add to the set of matches.

- `searchString` — The query string the search used to locate this range of text.

- `document` — A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## Discussion

Call this method to add a text range found in your document to the set of matches.

## See Also

### Tracking search results

- [invalidateFoundRange(_:document:)](<invalidatefoundrange(__document_).md>) — Removes a text range from the set of matches.
- [invalidate()](<invalidate().md>) — Invalidates all currently shown ranges.
- [finishedSearching()](<finishedsearching().md>) — Finishes the search for text ranges.
- [allFoundRanges](allfoundranges.md) — An ordered set of all the text ranges that match the search.
