---
title: 'CFRunLoopRemoveObserver(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopremoveobserver(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopremoveobserver(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopremoveobserver%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:4c83d48ee5c888ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopRemoveObserver(_:_:_:)

<sub>Function</sub>

Removes a CFRunLoopObserver object from a run loop mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopRemoveObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFRunLoopMode!)
```

## Parameters

- `rl` — The run loop to modify.

- `observer` — The run loop observer to remove.

- `mode` — The run loop mode of `rl` from which to remove `observer`. Use the constant [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) to remove `observer` from the set of objects monitored by all the common modes.

## Discussion

If `rl` does not contain `observer` in `mode`, this function does nothing.

## See Also

### Managing Observers

- [CFRunLoopAddObserver](<cfrunloopaddobserver(______).md>) — Adds a CFRunLoopObserver object to a run loop mode.
- [CFRunLoopContainsObserver](<cfrunloopcontainsobserver(______).md>) — Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopObserver object.
