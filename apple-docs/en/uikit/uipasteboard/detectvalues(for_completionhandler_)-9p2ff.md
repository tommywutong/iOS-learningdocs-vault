---
title: 'detectValues(for:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（15.0 起废弃）, iPadOS 14.0+（15.0 起废弃）, Mac Catalyst 14.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipasteboard/detectvalues(for:completionhandler:)-9p2ff'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/detectvalues(for:completionhandler:)-9p2ff'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/detectvalues%28for%3Acompletionhandler%3A%29-9p2ff.json'
content_hash: 'sha256:df4c8a461699eb98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# detectValues(for:completionHandler:)

<sub>Instance Method</sub>

Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.

> [!warning] Deprecated
> Use [detectValues(for:completionHandler:)](<detectvalues(for_completionhandler_)-6adre.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func detectValues(for patterns: Set<UIPasteboard.DetectionPattern>, completionHandler: @escaping (Result<[UIPasteboard.DetectionPattern : Any], any Error>) -> ())
```

## Parameters

- `patterns` — The patterns to detect on the pasteboard.

- `completionHandler` — A closure that the system invokes after detecting patterns on the pasteboard. The closure receives a `Result` instance that contains either a dictionary with the patterns found on the pasteboard or an error if detection failed. If the `Result` instance contains a dictionary, the keys specify the matched pattern, and the value specifies the content of the pasteboard.

## Discussion

> [!important] Important
> Calling this method notifies the user that the app has read the contents of the pasteboard.

For details about the types returned for each pattern, see [DetectionPattern](detectionpattern.md).

## See Also

### Deprecated

- [persistent](ispersistent.md) — A Boolean value that indicates whether the pasteboard is persistent. _(deprecated)_
- [- setPersistent:](<setpersistent(__).md>) — A Boolean value that indicates whether the pasteboard is persistent. _(deprecated)_
- [detectPatterns(for:completionHandler:)](<detectpatterns(for_completionhandler_)-5zlnd.md>) — Determines whether the first pasteboard item matches the specified patterns, without notifying the user. _(deprecated)_
- [detectPatterns(for:inItemSet:completionHandler:)](<detectpatterns(for_initemset_completionhandler_)-29iwn.md>) — Determines whether pasteboard items match the specified patterns, without notifying the user. _(deprecated)_
- [detectValues(for:inItemSet:completionHandler:)](<detectvalues(for_initemset_completionhandler_)-8y0iw.md>) — Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match. _(deprecated)_
