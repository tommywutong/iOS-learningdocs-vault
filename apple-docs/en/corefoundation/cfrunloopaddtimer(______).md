---
title: 'CFRunLoopAddTimer(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopaddtimer(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopaddtimer(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopaddtimer%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:981ba48639b6c4e4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopAddTimer(_:_:_:)

<sub>Function</sub>

Adds a CFRunLoopTimer object to a run loop mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopAddTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFRunLoopMode!)
```

## Parameters

- `rl` — The run loop to modify.

- `timer` — The run loop timer to add.

- `mode` — The run loop mode of `rl` to which to add `timer`. Use the constant [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) to add `timer` to the set of objects monitored by all the common modes.

## Discussion

A run loop timer can be registered in only one run loop at a time, although it can be added to multiple run loop modes within that run loop.

If `rl` already contains `timer` in `mode`, this function does nothing.

## See Also

### Managing Timers

- [CFRunLoopGetNextTimerFireDate](<cfrunloopgetnexttimerfiredate(____).md>) — Returns the time at which the next timer will fire.
- [CFRunLoopRemoveTimer](<cfrunloopremovetimer(______).md>) — Removes a CFRunLoopTimer object from a run loop mode.
- [CFRunLoopContainsTimer](<cfrunloopcontainstimer(______).md>) — Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopTimer object.
