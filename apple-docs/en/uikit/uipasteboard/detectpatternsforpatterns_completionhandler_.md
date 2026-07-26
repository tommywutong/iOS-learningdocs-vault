---
title: 'detectPatternsForPatterns:completionHandler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/detectpatternsforpatterns:completionhandler:'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/detectpatternsforpatterns:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/detectpatternsforpatterns%3Acompletionhandler%3A.json'
content_hash: 'sha256:2a674b45bffc1db0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# detectPatternsForPatterns:completionHandler:

<sub>Instance Method</sub>

Determines whether the first pasteboard item matches the specified patterns, without notifying the user.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) detectPatternsForPatterns:(NSSet<NSString *> *) patterns completionHandler:(void (^)(NSSet<NSString *> *, NSError *)) completionHandler;
```

## Parameters

- `patterns` — The patterns to detect on the pasteboard.

- `completionHandler` — A block that the system invokes after detecting patterns on the pasteboard. The block receives a `Result` instance that contains either a set with the patterns found on the pasteboard or an error if detection failed.

## Discussion

Because this method only gives an indication of whether a pasteboard item matches a particular pattern and doesn’t allow the app to access the contents, the system doesn’t notify the user about reading the contents of the pasteboard.

## See Also

### Detecting patterns of content in pasteboard items

- [detectPatternsForPatterns:inItemSet:completionHandler:](detectpatternsforpatterns_initemset_completionhandler_.md) — Determines whether pasteboard items match the specified patterns, without notifying the user.
- [detectValuesForPatterns:completionHandler:](detectvaluesforpatterns_completionhandler_.md) — Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [detectValuesForPatterns:inItemSet:completionHandler:](detectvaluesforpatterns_initemset_completionhandler_.md) — Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match.
- [DetectionPattern](detectionpattern.md) — An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.
