---
title: 'detectPatterns(for:inItemSet:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（15.0 起废弃）, iPadOS 14.0+（15.0 起废弃）, Mac Catalyst 14.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipasteboard/detectpatterns(for:initemset:completionhandler:)-29iwn'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/detectpatterns(for:initemset:completionhandler:)-29iwn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/detectpatterns%28for%3Ainitemset%3Acompletionhandler%3A%29-29iwn.json'
content_hash: 'sha256:521a5f9aca710f2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# detectPatterns(for:inItemSet:completionHandler:)

<sub>Instance Method</sub>

Determines whether pasteboard items match the specified patterns, without notifying the user.

> [!warning] Deprecated
> Use [detectPatterns(for:inItemSet:completionHandler:)](<detectpatterns(for_initemset_completionhandler_)-7ubl1.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func detectPatterns(for patterns: Set<UIPasteboard.DetectionPattern>, inItemSet itemSet: IndexSet?, completionHandler: @escaping (Result<[Set<UIPasteboard.DetectionPattern>], any Error>) -> ())
```

## Parameters

- `patterns` — The patterns to detect on the pasteboard.

- `itemSet` — An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass `nil` to detect patterns in all pasteboard items.

- `completionHandler` — A closure that the system invokes after detecting patterns on the pasteboard. The closure receives a `Result` instance that contains either an array with the patterns found on the pasteboard or an error if detection failed. If the `Result` instance contains an array, the index of each element in the array corresponds to the pasteboard item index specified in `itemSet`.

## Discussion

Because this method only detects for the presence of patterns and does not read the contents of the pasteboard, the system doesn’t notify the user about reading the contents of the pasteboard.

## See Also

### Deprecated

- [persistent](ispersistent.md) — A Boolean value that indicates whether the pasteboard is persistent. _(deprecated)_
- [- setPersistent:](<setpersistent(__).md>) — A Boolean value that indicates whether the pasteboard is persistent. _(deprecated)_
- [detectPatterns(for:completionHandler:)](<detectpatterns(for_completionhandler_)-5zlnd.md>) — Determines whether the first pasteboard item matches the specified patterns, without notifying the user. _(deprecated)_
- [detectValues(for:completionHandler:)](<detectvalues(for_completionhandler_)-9p2ff.md>) — Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match. _(deprecated)_
- [detectValues(for:inItemSet:completionHandler:)](<detectvalues(for_initemset_completionhandler_)-8y0iw.md>) — Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match. _(deprecated)_
