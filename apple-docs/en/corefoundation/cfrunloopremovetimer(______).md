---
title: 'CFRunLoopRemoveTimer(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopremovetimer(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopremovetimer(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopremovetimer%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ecfa72cc5806c703'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopRemoveTimer(_:_:_:)

<sub>Function</sub>

Removes a CFRunLoopTimer object from a run loop mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopRemoveTimer(_ rl: CFRunLoop!, _ timer: CFRunLoopTimer!, _ mode: CFRunLoopMode!)
```

## Parameters

- `rl` — The run loop to modify.

- `timer` — The run loop timer to remove.

- `mode` — The run loop mode of `rl` from which to remove `timer`. Use the constant [kCFRunLoopCommonModes](cfrunloopmode/commonmodes.md) to remove `timer` from the set of objects monitored by all the common modes.

## Discussion

If `rl` does not contain `timer` in `mode`, this function does nothing.

## See Also

### Managing Timers

- [CFRunLoopAddTimer](<cfrunloopaddtimer(______).md>) — Adds a CFRunLoopTimer object to a run loop mode.
- [CFRunLoopGetNextTimerFireDate](<cfrunloopgetnexttimerfiredate(____).md>) — Returns the time at which the next timer will fire.
- [CFRunLoopContainsTimer](<cfrunloopcontainstimer(______).md>) — Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopTimer object.
