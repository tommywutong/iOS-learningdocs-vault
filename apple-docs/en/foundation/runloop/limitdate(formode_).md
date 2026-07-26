---
title: 'limitDate(forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/limitdate(formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/limitdate(formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/limitdate%28formode%3A%29.json'
content_hash: 'sha256:8978d00df673ee41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# limitDate(forMode:)

<sub>Instance Method</sub>

Performs one pass through the run loop in the specified mode and returns the date at which the next timer is scheduled to fire.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func limitDate(forMode mode: RunLoop.Mode) -> Date?
```

## Parameters

- `mode` — The run loop mode to search. You may specify custom modes or use one of the modes listed in `Run Loop Modes`.

## Return Value

The date at which the next timer is scheduled to fire, or `nil` if there are no input sources for this mode.

## Discussion

The run loop is entered with an immediate timeout, so the run loop does not block, waiting for input, if no input sources need processing.

## See Also

### Accessing Run Loops and Modes

- [currentRunLoop](current.md) — Returns the run loop for the current thread.
- [currentMode](currentmode.md) — The receiver’s current input mode.
- [mainRunLoop](main.md) — Returns the run loop of the main thread.
- [- getCFRunLoop](<getcfrunloop().md>) — Returns the receiver’s underlying run loop object.
- [Mode](mode.md) — Modes that a run loop operates in.
