---
title: makeAsyncIterator()
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/activitystateupdates-swift.struct/makeasynciterator()
source_url: 'https://developer.apple.com/documentation/activitykit/activity/activitystateupdates-swift.struct/makeasynciterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/activitystateupdates-swift.struct/makeasynciterator%28%29.json'
content_hash: 'sha256:22bedaa2aed1f2f9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [ActivityKit](../../../activitykit.md) · [Activity](../../activity.md) · [ActivityStateUpdates](../activitystateupdates-swift.struct.md)

# makeAsyncIterator()

<sub>Instance Method</sub>

Creates the asynchronous iterator that produces results from this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func makeAsyncIterator() -> Activity<Attributes>.ActivityStateUpdates.Iterator
```

## See Also

### Creating an iterator

- [Iterator](iterator.md) — An iterator for accessing individual data entries from the series.
- [Element](element.md) — The type of element this asynchronous sequence produces.
