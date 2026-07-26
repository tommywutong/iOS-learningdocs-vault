---
title: current
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/current
source_url: 'https://developer.apple.com/documentation/foundation/runloop/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/current.json'
content_hash: 'sha256:4fd129458c1c0e76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# current

<sub>Type Property</sub>

Returns the run loop for the current thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var current: RunLoop { get }
```

## Return Value

The `NSRunLoop` object for the current thread.

## Discussion

If a run loop does not yet exist for the thread, one is created and returned.

## See Also

### Related Documentation

- [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)

### Accessing Run Loops and Modes

- [currentMode](currentmode.md) — The receiver’s current input mode.
- [- limitDateForMode:](<limitdate(formode_).md>) — Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [mainRunLoop](main.md) — Returns the run loop of the main thread.
- [- getCFRunLoop](<getcfrunloop().md>) — Returns the receiver’s underlying run loop object.
- [Mode](mode.md) — Modes that a run loop operates in.
