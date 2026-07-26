---
title: 'compareFoundRange:toRange:inDocument:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearching-53wjq/comparefoundrange:torange:indocument:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearching-53wjq/comparefoundrange:torange:indocument:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearching-53wjq/comparefoundrange%3Atorange%3Aindocument%3A.json'
content_hash: 'sha256:9486438eb66f40e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearching](../uitextsearching-53wjq.md)

# compareFoundRange:toRange:inDocument:

<sub>Instance Method</sub>

Compares ranges from the set of matches the aggregator provides to determine navigation order.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (NSComparisonResult) compareFoundRange:(UITextRange *) foundRange toRange:(UITextRange *) toRange inDocument:(UITextSearchDocumentIdentifier) document;
```

## Parameters

- `foundRange` — The range of characters in a text container to compare from.

- `toRange` — The range of characters in a text container to compare to.

- `document` — A string that uniquely identifies the document containing the text ranges. `Nil` when searching a single document.

## Return Value

Returns the result of comparing the two text ranges.

## Discussion

The system calls this method during a find session to determine which [UITextRange](../uitextrange.md) to highlight next when a user taps the “next” or “previous” button.

## See Also

### Handling searches

- [performTextSearchWithQueryString:usingOptions:resultAggregator:](performtextsearchwithquerystring_usingoptions_resultaggregator_.md) — Searches for ranges of text matching the string across all searchable documents and collects results in the aggregator.
- [UITextSearchAggregator](../uitextsearchaggregator-c.protocol.md) — The methods you use on a find session’s aggregator to collect matching text ranges for a search.
- [compareOrderFromDocument:toDocument:](compareorderfromdocument_todocument_.md) — Compares documents containing matching ranges from the set the aggregator provides to determine navigation order.
- [UITextSearchDocumentIdentifier](../uitextsearchdocumentidentifier.md) — A string that uniquely identifies a specific document when searching for matching text across multiple documents.
