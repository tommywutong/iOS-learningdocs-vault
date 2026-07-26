---
title: ActivityAuthorizationInfo.FrequentPushEnablementUpdates
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activityauthorizationinfo/frequentpushenablementupdates-swift.struct
source_url: 'https://developer.apple.com/documentation/activitykit/activityauthorizationinfo/frequentpushenablementupdates-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityauthorizationinfo/frequentpushenablementupdates-swift.struct.json'
content_hash: 'sha256:0e354b09f1cbb986'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityAuthorizationInfo](../activityauthorizationinfo.md)

# ActivityAuthorizationInfo.FrequentPushEnablementUpdates

<sub>Structure</sub>

A structure that can observe whether you can update Live Activities with frequent ActivityKit push notifications.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct FrequentPushEnablementUpdates
```

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md)

## Topics

### Creating an iterator

- [makeAsyncIterator()](<frequentpushenablementupdates-swift.struct/makeasynciterator().md>) — Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Iterator](frequentpushenablementupdates-swift.struct/iterator.md) — An iterator for accessing individual data entries from the series.
- [Element](frequentpushenablementupdates-swift.struct/element.md) — The type of element this asynchronous sequence produces.

## See Also

### Observing availability of frequent ActivityKit push notifications

- [frequentPushesEnabled](frequentpushesenabled.md) — A Boolean value that indicates whether a person permitted you to update Live Activities with frequent ActivityKit push notifications.
- [frequentPushEnablementUpdates](frequentpushenablementupdates-swift.property.md) — An asynchronous sequence you use to observe whether a person permitted you to update Live Activities with frequent ActivityKit push notifications.
