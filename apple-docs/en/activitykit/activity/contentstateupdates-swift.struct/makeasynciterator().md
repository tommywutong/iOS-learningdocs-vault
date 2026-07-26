---
title: makeAsyncIterator()
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.1+（16.2 起废弃）, iPadOS 16.1+（16.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/activitykit/activity/contentstateupdates-swift.struct/makeasynciterator()
source_url: 'https://developer.apple.com/documentation/activitykit/activity/contentstateupdates-swift.struct/makeasynciterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/contentstateupdates-swift.struct/makeasynciterator%28%29.json'
content_hash: 'sha256:154da77d26a3992a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [ActivityKit](../../../activitykit.md) · [Activity](../../activity.md) · [ContentStateUpdates](../contentstateupdates-swift.struct.md)

# makeAsyncIterator()

<sub>Instance Method</sub>

Creates the asynchronous iterator that produces results from this asynchronous sequence.

> [!warning] Deprecated
> Use `ContentUpdates` instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func makeAsyncIterator() -> Activity<Attributes>.ContentStateUpdates.Iterator
```

## See Also

### Creating an iterator

- [Iterator](iterator.md) — An iterator for accessing individual data entries from the series. _(deprecated)_
- [Element](element.md) — The type of element this asynchronous sequence produces. _(deprecated)_
