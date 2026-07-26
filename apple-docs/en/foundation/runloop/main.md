---
title: main
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/runloop/main
source_url: 'https://developer.apple.com/documentation/foundation/runloop/main'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/main.json'
content_hash: 'sha256:d380d5a63dfe4b51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# main

<sub>Type Property</sub>

Returns the run loop of the main thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var main: RunLoop { get }
```

## Return Value

An object representing the main thread’s run loop.

## See Also

### Accessing Run Loops and Modes

- [currentRunLoop](current.md) — Returns the run loop for the current thread.
- [currentMode](currentmode.md) — The receiver’s current input mode.
- [- limitDateForMode:](<limitdate(formode_).md>) — Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.
- [- getCFRunLoop](<getcfrunloop().md>) — Returns the receiver’s underlying run loop object.
- [Mode](mode.md) — Modes that a run loop operates in.
