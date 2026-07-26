---
title: 'CFRunLoopContainsObserver(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopcontainsobserver(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopcontainsobserver(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopcontainsobserver%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7dc97ec221ab825f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopContainsObserver(_:_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopObserver object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopContainsObserver(_ rl: CFRunLoop!, _ observer: CFRunLoopObserver!, _ mode: CFRunLoopMode!) -> Bool
```

## Parameters

- `rl` — The run loop to examine.

- `observer` — The run loop observer for which to search.

- `mode` — The run loop mode in which to search for `observer`. Use the constant [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) to search for `observer` in the set of objects monitored by all the common modes.

## Return Value

`true` if `observer` is in mode `mode` of the run loop `rl`, otherwise `false`.

## Discussion

If `observer` was added to [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md), this function returns `true` if `mode` is either [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) or any of the modes that has been added to the set of common modes.

## See Also

### Managing Observers

- [CFRunLoopAddObserver](<cfrunloopaddobserver(______).md>) — Adds a CFRunLoopObserver object to a run loop mode.
- [CFRunLoopRemoveObserver](<cfrunloopremoveobserver(______).md>) — Removes a CFRunLoopObserver object from a run loop mode.
