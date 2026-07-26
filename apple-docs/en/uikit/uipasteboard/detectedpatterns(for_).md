---
title: 'detectedPatterns(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/detectedpatterns(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/detectedpatterns(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/detectedpatterns%28for%3A%29.json'
content_hash: 'sha256:487ea41431db83d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# detectedPatterns(for:)

<sub>Instance Method</sub>

Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func detectedPatterns(for keyPaths: Set<PartialKeyPath<UIPasteboard.DetectedValues>>) async throws -> Set<PartialKeyPath<UIPasteboard.DetectedValues>>
```

## Parameters

- `keyPaths` — A set of key paths you use to indicate which types of patterns you want the data detection system to match.

## Return Value

A set of key paths that represent the patterns the data detection system matches in the pasteboard.

## Discussion

Because this method only gives an indication of whether a pasteboard item matches a particular pattern and doesn’t allow the app to access the contents, the system doesn’t notify the user about reading the contents of the pasteboard.

## See Also

### Detecting patterns of content in pasteboard items

- [detectPatterns(for:completionHandler:)](<detectpatterns(for_completionhandler_)-23vwn.md>) — Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [detectPatterns(for:inItemSet:completionHandler:)](<detectpatterns(for_initemset_completionhandler_)-7ubl1.md>) — Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- [detectedPatterns(for:inItemSet:)](<detectedpatterns(for_initemset_).md>) — Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [detectValues(for:completionHandler:)](<detectvalues(for_completionhandler_)-6adre.md>) — Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.
- [detectedValues(for:)](<detectedvalues(for_).md>) — Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [detectValues(for:inItemSet:completionHandler:)](<detectvalues(for_initemset_completionhandler_)-pm9l.md>) — Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [detectedValues(for:inItemSet:)](<detectedvalues(for_initemset_).md>) — Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.
- [DetectedValues](detectedvalues.md) — An object that contains common types of data that the data detection system matches for a pasteboard.
- [DetectionPattern](detectionpattern.md) — An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.
