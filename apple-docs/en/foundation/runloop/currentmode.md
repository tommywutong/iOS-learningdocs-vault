---
title: currentMode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/currentmode
source_url: 'https://developer.apple.com/documentation/foundation/runloop/currentmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/currentmode.json'
content_hash: 'sha256:e0a49b01b892344e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# currentMode

<sub>Instance Property</sub>

The receiver’s current input mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentMode: RunLoop.Mode? { get }
```

## Discussion

The receiver’s current input mode. This method returns the current input mode _only_ while the receiver is running; otherwise, it returns `nil`.

The current mode is set by the methods that run the run loop, such as [- acceptInputForMode:beforeDate:](<acceptinput(formode_before_).md>) and [- runMode:beforeDate:](<run(mode_before_).md>).

## See Also

### Related Documentation

- [- runUntilDate:](<run(until_).md>) — Runs the loop until the specified date, during which time it processes data from all attached input sources.
- [- run](<run().md>) — Puts the receiver into a permanent loop, during which time it processes data from all attached input sources.

### Accessing Run Loops and Modes

- [currentRunLoop](current.md) — Returns the run loop for the current thread.
- [- limitDateForMode:](<limitdate(formode_).md>) — Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [mainRunLoop](main.md) — Returns the run loop of the main thread.
- [- getCFRunLoop](<getcfrunloop().md>) — Returns the receiver’s underlying run loop object.
- [Mode](mode.md) — Modes that a run loop operates in.
