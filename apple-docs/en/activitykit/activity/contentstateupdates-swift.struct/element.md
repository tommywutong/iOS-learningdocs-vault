---
title: Activity.ContentStateUpdates.Element
framework: ActivityKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 16.1+（16.2 起废弃）, iPadOS 16.1+（16.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/activitykit/activity/contentstateupdates-swift.struct/element
source_url: 'https://developer.apple.com/documentation/activitykit/activity/contentstateupdates-swift.struct/element'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/contentstateupdates-swift.struct/element.json'
content_hash: 'sha256:8fd3003a3ea80be9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [ActivityKit](../../../activitykit.md) · [Activity](../../activity.md) · [ContentStateUpdates](../contentstateupdates-swift.struct.md)

# Activity.ContentStateUpdates.Element

<sub>Type Alias</sub>

The type of element this asynchronous sequence produces.

> [!warning] Deprecated
> Use `ContentUpdates` instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
typealias Element = Activity<Attributes>.ContentState
```

## See Also

### Creating an iterator

- [makeAsyncIterator()](<makeasynciterator().md>) — Creates the asynchronous iterator that produces results from this asynchronous sequence. _(deprecated)_
- [Iterator](iterator.md) — An iterator for accessing individual data entries from the series. _(deprecated)_
