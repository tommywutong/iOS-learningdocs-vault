---
title: allowsReplacementForCurrentlyHighlightedResult
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifindsession/allowsreplacementforcurrentlyhighlightedresult
source_url: 'https://developer.apple.com/documentation/uikit/uifindsession/allowsreplacementforcurrentlyhighlightedresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindsession/allowsreplacementforcurrentlyhighlightedresult.json'
content_hash: 'sha256:00a2c1eaa00895d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindSession](../uifindsession.md)

# allowsReplacementForCurrentlyHighlightedResult

<sub>Instance Property</sub>

A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsReplacementForCurrentlyHighlightedResult: Bool { get }
```

## Discussion

This property determines whether the find panel supports replacement for the currently highlighted item. If [true](../../swift/true.md), the system enables the Replace button in the find panel and the hardware keyboard shortcuts for replacement.

The default value is [true](../../swift/true.md) if [supportsReplacement](supportsreplacement.md) is [true](../../swift/true.md).

## See Also

### Getting session information

- [resultCount](resultcount.md) — The total number of results the search matches.
- [highlightedResultIndex](highlightedresultindex.md) — The index of the result the find panel highlights.
- [supportsReplacement](supportsreplacement.md) — A Boolean value that indicates whether to allow replacing find panel results.
- [searchResultDisplayStyle](searchresultdisplaystyle-swift.property.md) — The information the find panel includes in the summary of found results.
- [SearchResultDisplayStyle](searchresultdisplaystyle-swift.enum.md) — Constants that describe the results summary the find panel UI includes.
