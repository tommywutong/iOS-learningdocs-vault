---
title: 'foundRange:forSearchString:inDocument:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearchaggregator-c.protocol/foundrange:forsearchstring:indocument:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol/foundrange:forsearchstring:indocument:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-c.protocol/foundrange%3Aforsearchstring%3Aindocument%3A.json'
content_hash: 'sha256:56af010822e92483'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchAggregator](../uitextsearchaggregator-c.protocol.md)

# foundRange:forSearchString:inDocument:

<sub>Instance Method</sub>

Adds a text range to the set of matches.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) foundRange:(UITextRange *) range forSearchString:(NSString *) string inDocument:(UITextSearchDocumentIdentifier) document;
```

## Parameters

- `range` — The text range to add to the set of matches.

- `string` — The query string the search used to locate this range of text.

- `document` — A string that uniquely identifies the document containing the text range. `Nil` when searching a single document.

## Discussion

Call this method to add a text range found in your document to the set of matches.

## See Also

### Tracking search results

- [invalidateFoundRange:inDocument:](invalidatefoundrange_indocument_.md) — Removes a text range from the set of matches.
- [invalidate](invalidate.md) — Invalidates all currently shown ranges.
- [finishedSearching](finishedsearching.md) — Finishes the search for text ranges.
- [allFoundRanges](allfoundranges.md) — An ordered set of all the text ranges that match the search.
