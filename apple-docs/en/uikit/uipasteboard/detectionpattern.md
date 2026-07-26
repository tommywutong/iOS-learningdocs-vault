---
title: UIPasteboard.DetectionPattern
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/detectionpattern
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/detectionpattern'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/detectionpattern.json'
content_hash: 'sha256:7e2ab24363ca665e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# UIPasteboard.DetectionPattern

<sub>Structure</sub>

An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct DetectionPattern
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Detecting common patterns

- [UIPasteboardDetectionPatternNumber](detectionpattern/number.md) — A pattern that indicates the pasteboard contains a string that consists of a numeric value.
- [UIPasteboardDetectionPatternProbableWebSearch](detectionpattern/probablewebsearch.md) — A pattern that indicates the pasteboard contains a string suitable for use as a web search term.
- [UIPasteboardDetectionPatternProbableWebURL](detectionpattern/probableweburl.md) — A pattern that indicates the pasteboard contains a string that consists of a URL.

### Creating a detection pattern

- [init(rawValue:)](<detectionpattern/init(rawvalue_).md>) — Creates a detection pattern to detect different types of content on the pasteboard.

## See Also

### Detecting patterns of content in pasteboard items

- [detectPatterns(for:completionHandler:)](<detectpatterns(for_completionhandler_)-23vwn.md>) — Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [detectedPatterns(for:)](<detectedpatterns(for_).md>) — Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- [detectPatterns(for:inItemSet:completionHandler:)](<detectpatterns(for_initemset_completionhandler_)-7ubl1.md>) — Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- [detectedPatterns(for:inItemSet:)](<detectedpatterns(for_initemset_).md>) — Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [detectValues(for:completionHandler:)](<detectvalues(for_completionhandler_)-6adre.md>) — Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.
- [detectedValues(for:)](<detectedvalues(for_).md>) — Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [detectValues(for:inItemSet:completionHandler:)](<detectvalues(for_initemset_completionhandler_)-pm9l.md>) — Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [detectedValues(for:inItemSet:)](<detectedvalues(for_initemset_).md>) — Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.
- [DetectedValues](detectedvalues.md) — An object that contains common types of data that the data detection system matches for a pasteboard.
