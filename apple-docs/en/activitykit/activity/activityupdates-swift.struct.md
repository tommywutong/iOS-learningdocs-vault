---
title: Activity.ActivityUpdates
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/activityupdates-swift.struct
source_url: 'https://developer.apple.com/documentation/activitykit/activity/activityupdates-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/activityupdates-swift.struct.json'
content_hash: 'sha256:02288a148f8ca9d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# Activity.ActivityUpdates

<sub>Structure</sub>

A structure that offers functionality to observe changes to a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct ActivityUpdates
```

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md)

## Topics

### Creating an iterator

- [makeAsyncIterator()](<activityupdates-swift.struct/makeasynciterator().md>) — Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [Iterator](activityupdates-swift.struct/iterator.md) — An iterator for accessing individual data entries from the series.
- [Element](activityupdates-swift.struct/element.md) — The type of element this asynchronous sequence produces.

## See Also

### Accessing Live Activities

- [activities](activities.md) — An array of your app’s current Live Activities.
- [activityUpdates](activityupdates-swift.type.property.md) — An asynchronous sequence you use to observe changes to ongoing Live Activities and to asynchronously access a Live Activity when you start it.
