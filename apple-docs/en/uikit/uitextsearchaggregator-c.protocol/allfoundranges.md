---
title: allFoundRanges
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchaggregator-c.protocol/allfoundranges
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchaggregator-c.protocol/allfoundranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchaggregator-c.protocol/allfoundranges.json'
content_hash: 'sha256:7aaa2349a98aaf60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchAggregator](../uitextsearchaggregator-c.protocol.md)

# allFoundRanges

<sub>Instance Property</sub>

An ordered set of all the text ranges that match the search.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) NSOrderedSet<UITextRange *> * allFoundRanges;
```

## See Also

### Tracking search results

- [foundRange:forSearchString:inDocument:](foundrange_forsearchstring_indocument_.md) — Adds a text range to the set of matches.
- [invalidateFoundRange:inDocument:](invalidatefoundrange_indocument_.md) — Removes a text range from the set of matches.
- [invalidate](invalidate.md) — Invalidates all currently shown ranges.
- [finishedSearching](finishedsearching.md) — Finishes the search for text ranges.
