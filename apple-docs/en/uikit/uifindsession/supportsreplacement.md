---
title: supportsReplacement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifindsession/supportsreplacement
source_url: 'https://developer.apple.com/documentation/uikit/uifindsession/supportsreplacement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifindsession/supportsreplacement.json'
content_hash: 'sha256:8825d8a7079e5cd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFindSession](../uifindsession.md)

# supportsReplacement

<sub>Instance Property</sub>

A Boolean value that indicates whether to allow replacing find panel results.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var supportsReplacement: Bool { get }
```

## Discussion

This property determines whether the find panel shows the replacement UI.

The default value is [false](../../swift/false.md).

## See Also

### Getting session information

- [resultCount](resultcount.md) — The total number of results the search matches.
- [highlightedResultIndex](highlightedresultindex.md) — The index of the result the find panel highlights.
- [allowsReplacementForCurrentlyHighlightedResult](allowsreplacementforcurrentlyhighlightedresult.md) — A Boolean value that indicates whether to allow replacing the result the find panel is highlighting.
- [searchResultDisplayStyle](searchresultdisplaystyle-swift.property.md) — The information the find panel includes in the summary of found results.
- [SearchResultDisplayStyle](searchresultdisplaystyle-swift.enum.md) — Constants that describe the results summary the find panel UI includes.
