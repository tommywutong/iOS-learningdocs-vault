---
title: 'CFRunLoopGetNextTimerFireDate(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopgetnexttimerfiredate(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopgetnexttimerfiredate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopgetnexttimerfiredate%28_%3A_%3A%29.json'
content_hash: 'sha256:86fa2d407151c5cf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopGetNextTimerFireDate(_:_:)

<sub>Function</sub>

Returns the time at which the next timer will fire.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopGetNextTimerFireDate(_ rl: CFRunLoop!, _ mode: CFRunLoopMode!) -> CFAbsoluteTime
```

## Parameters

- `rl` — The run loop to examine.

- `mode` — The run loop mode within `rl` to test.

## Return Value

The earliest firing time of the run loop timers registered in `mode` for the run loop `rl`.

## See Also

### Managing Timers

- [CFRunLoopAddTimer](<cfrunloopaddtimer(______).md>) — Adds a CFRunLoopTimer object to a run loop mode.
- [CFRunLoopRemoveTimer](<cfrunloopremovetimer(______).md>) — Removes a CFRunLoopTimer object from a run loop mode.
- [CFRunLoopContainsTimer](<cfrunloopcontainstimer(______).md>) — Returns a Boolean value that indicates whether a run loop mode contains a particular CFRunLoopTimer object.
