---
title: CFRunLoopTimerCallBack
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunlooptimercallback
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooptimercallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooptimercallback.json'
content_hash: 'sha256:e37de6a1f34dbdd7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopTimerCallBack

<sub>Type Alias</sub>

Callback invoked when a CFRunLoopTimer object fires.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFRunLoopTimerCallBack = (CFRunLoopTimer?, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `timer` — The run loop timer that is firing.

- `info` — The `info` member of the [CFRunLoopTimerContext](cfrunlooptimercontext.md) structure that was used when creating the run loop timer.

## Discussion

If `timer` repeats, the run loop automatically schedules the next firing time after calling this function, unless you manually update the firing time within this callback by calling [CFRunLoopTimerSetNextFireDate](<cfrunlooptimersetnextfiredate(____).md>). If `timer` does not repeat, the run loop invalidates `timer`.

You specify this callback when you create the timer with [CFRunLoopTimerCreate](<cfrunlooptimercreate(______________).md>).
