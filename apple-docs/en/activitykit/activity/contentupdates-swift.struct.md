---
title: Activity.ContentUpdates
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/contentupdates-swift.struct
source_url: 'https://developer.apple.com/documentation/activitykit/activity/contentupdates-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/contentupdates-swift.struct.json'
content_hash: 'sha256:56d1f5fe810d2a7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# Activity.ContentUpdates

<sub>Structure</sub>

A structure that offers functionality to observe changes to the dynamic content of a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct ContentUpdates
```

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md)

## Topics

### Structures

- [Iterator](contentupdates-swift.struct/iterator.md) — An iterator for accessing individual data entries from the series.

### Instance Methods

- [makeAsyncIterator()](<contentupdates-swift.struct/makeasynciterator().md>) — Creates the asynchronous iterator that produces results from this asynchronous sequence.

### Type Aliases

- [Element](contentupdates-swift.struct/element.md) — The type of element this asynchronous sequence produces.

## See Also

### Observing Live Activity content changes

- [contentUpdates](contentupdates-swift.property.md) — An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.
