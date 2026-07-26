---
title: 'invalidateFoundRange:inDocument:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearchaggregator-c.protocol/invalidatefoundrange:indocument:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol/invalidatefoundrange:indocument:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-c.protocol/invalidatefoundrange%3Aindocument%3A.json'
content_hash: 'sha256:77e6b3c759acb802'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchAggregator](../uitextsearchaggregator-c.protocol.md)

# invalidateFoundRange:inDocument:

<sub>Instance Method</sub>

Removes a text range from the set of matches.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) invalidateFoundRange:(UITextRange *) range inDocument:(UITextSearchDocumentIdentifier) document;
```

## Parameters

- `range` — The text range to remove from the set of matches.

- `document` — A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## Discussion

Call this method to invalidate a text range when removing or changing text in the document. This causes the system find panel to update its current state, and if the range is the highlighted range, the find panel advances to the next found result.

## See Also

### Tracking search results

- [foundRange:forSearchString:inDocument:](foundrange_forsearchstring_indocument_.md) — Adds a text range to the set of matches.
- [invalidate](invalidate.md) — Invalidates all currently shown ranges.
- [finishedSearching](finishedsearching.md) — Finishes the search for text ranges.
- [allFoundRanges](allfoundranges.md) — An ordered set of all the text ranges that match the search.
