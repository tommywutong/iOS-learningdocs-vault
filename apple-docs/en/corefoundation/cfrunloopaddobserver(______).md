---
title: 'CFRunLoopAddObserver(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopaddobserver(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopaddobserver(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopaddobserver%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7ed908ff975177f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopAddObserver(_:_:_:)

<sub>Function</sub>

Adds a CFRunLoopObserver object to a run loop mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopAddObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFRunLoopMode!)
```

## Parameters

- `rl` — The run loop to modify.

- `observer` — The run loop observer to add.

- `mode` — The run loop mode to which to add `observer`. Use the constant [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) to add `observer` to the set of objects monitored by all the common modes.

## Discussion

A run loop observer can be registered in only one run loop at a time, although it can be added to multiple run loop modes within that run loop.

If `rl` already contains `observer` in `mode`, this function does nothing.

## See Also

### Managing Observers

- [CFRunLoopContainsObserver](<cfrunloopcontainsobserver(______).md>) — Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopObserver object.
- [CFRunLoopRemoveObserver](<cfrunloopremoveobserver(______).md>) — Removes a CFRunLoopObserver object from a run loop mode.
