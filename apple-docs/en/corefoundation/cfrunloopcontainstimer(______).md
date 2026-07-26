---
title: 'CFRunLoopContainsTimer(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopcontainstimer(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopcontainstimer(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopcontainstimer%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:bef24527697db56a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopContainsTimer(_:_:_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopTimer object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopContainsTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFRunLoopMode!) -> Bool
```

## Parameters

- `rl` — The run loop to examine.

- `timer` — The run loop timer for which to search.

- `mode` — The run loop mode of `rl` in which to search for `timer`. Use the constant [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) to search for `timer` in the set of objects monitored by all the common modes.

## Return Value

`true` if `timer` is in mode `mode` of the run loop `rl`, `false` otherwise.

## Discussion

If `timer` was added to [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md), this function returns `true` if `mode` is either [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) or any of the modes that has been added to the set of common modes.

## See Also

### Managing Timers

- [CFRunLoopAddTimer](<cfrunloopaddtimer(______).md>) — Adds a CFRunLoopTimer object to a run loop mode.
- [CFRunLoopGetNextTimerFireDate](<cfrunloopgetnexttimerfiredate(____).md>) — Returns the time at which the next timer will fire.
- [CFRunLoopRemoveTimer](<cfrunloopremovetimer(______).md>) — Removes a CFRunLoopTimer object from a run loop mode.
