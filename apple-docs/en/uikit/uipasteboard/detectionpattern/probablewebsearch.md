---
title: probableWebSearch
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/detectionpattern/probablewebsearch
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/detectionpattern/probablewebsearch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/detectionpattern/probablewebsearch.json'
content_hash: 'sha256:5e96cf52a3954ff7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPasteboard](../../uipasteboard.md) · [DetectionPattern](../detectionpattern.md)

# probableWebSearch

<sub>Type Property</sub>

A pattern that indicates the pasteboard contains a string suitable for use as a web search term.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let probableWebSearch: UIPasteboard.DetectionPattern
```

## Discussion

When you include this pattern in calls to [detectValues(for:inItemSet:completionHandler:)](<../detectvalues(for_initemset_completionhandler_)-pm9l.md>) or [detectValues(for:completionHandler:)](<../detectvalues(for_completionhandler_)-6adre.md>) — [detectValuesForPatterns:inItemSet:completionHandler:](../detectvaluesforpatterns_initemset_completionhandler_.md) or [detectValuesForPatterns:completionHandler:](../detectvaluesforpatterns_completionhandler_.md) in Objective-C — and the pasteboard detects a string suitable for use as a web search term, it reports the value as an [NSString](../../../foundation/nsstring.md).

## See Also

### Detecting common patterns

- [UIPasteboardDetectionPatternNumber](number.md) — A pattern that indicates the pasteboard contains a string that consists of a numeric value.
- [UIPasteboardDetectionPatternProbableWebURL](probableweburl.md) — A pattern that indicates the pasteboard contains a string that consists of a URL.
