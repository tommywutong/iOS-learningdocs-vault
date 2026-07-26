---
title: 'detectValuesForPatterns:inItemSet:completionHandler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteboard/detectvaluesforpatterns:initemset:completionhandler:'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/detectvaluesforpatterns:initemset:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/detectvaluesforpatterns%3Ainitemset%3Acompletionhandler%3A.json'
content_hash: 'sha256:4e0c7f165cf1c7ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# detectValuesForPatterns:inItemSet:completionHandler:

<sub>Instance Method</sub>

Determines whether pasteboard items match the specified patterns, reading the contents if it finds a match.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) detectValuesForPatterns:(NSSet<NSString *> *) patterns inItemSet:(NSIndexSet *) itemSet completionHandler:(void (^)(NSArray<NSDictionary<NSString *,id> *> *, NSError *)) completionHandler;
```

## Parameters

- `patterns` — The patterns to detect on the pasteboard.

- `itemSet` — An index set with each integer value identifying a pasteboard item positionally in the pasteboard. Pass in nil to request all pasteboard items.

- `completionHandler` — A block that the system invokes after detecting patterns on the pasteboard. The block receives a `Result` instance that contains either an array of dictionaries with the patterns and the associated values found on the pasteboard or an error if detection failed. If `Result` contains an array, the index of each element in the array corresponds to the pasteboard item index specified in `itemSet`.

## Discussion

> [!important] Important
> Calling this method notifies the user that the app has read the contents of the pasteboard.

For details about the types returned for each pattern, see [DetectionPattern](detectionpattern.md).

## See Also

### Detecting patterns of content in pasteboard items

- [detectPatternsForPatterns:completionHandler:](detectpatternsforpatterns_completionhandler_.md) — Determines whether the first pasteboard item matches the specified patterns, without notifying the user.
- [detectPatternsForPatterns:inItemSet:completionHandler:](detectpatternsforpatterns_initemset_completionhandler_.md) — Determines whether pasteboard items match the specified patterns, without notifying the user.
- [detectValuesForPatterns:completionHandler:](detectvaluesforpatterns_completionhandler_.md) — Determines whether the first pasteboard item matches the specified patterns, reading the contents if it finds a match.
- [DetectionPattern](detectionpattern.md) — An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.
