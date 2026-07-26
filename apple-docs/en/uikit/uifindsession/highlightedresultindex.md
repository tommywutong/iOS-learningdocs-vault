---
title: highlightedResultIndex
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifindsession/highlightedresultindex
source_url: 'https://developer.apple.com/documentation/uikit/uifindsession/highlightedresultindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindsession/highlightedresultindex.json'
content_hash: 'sha256:faf5cfff0283495a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindSession](../uifindsession.md)

# highlightedResultIndex

<sub>Instance Property</sub>

The index of the result the find panel highlights.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var highlightedResultIndex: Int { get }
```

## Discussion

To indicate no highlighted result, return `nil` (Swift) or [NSNotFound](../../foundation/nsnotfound-9t5v2.md) (Objective-C).

## See Also

### Getting session information

- [resultCount](resultcount.md) — The total number of results the search matches.
- [supportsReplacement](supportsreplacement.md) — A Boolean value that indicates whether to allow replacing find panel results.
- [allowsReplacementForCurrentlyHighlightedResult](allowsreplacementforcurrentlyhighlightedresult.md) — A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.
- [searchResultDisplayStyle](searchresultdisplaystyle-swift.property.md) — The information the find panel includes in the summary of found results.
- [SearchResultDisplayStyle](searchresultdisplaystyle-swift.enum.md) — Constants that describe the results summary the find panel UI includes.
