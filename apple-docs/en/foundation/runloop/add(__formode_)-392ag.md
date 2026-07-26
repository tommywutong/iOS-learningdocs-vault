---
title: 'add(_:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/add(_:formode:)-392ag'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/add(_:formode:)-392ag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/add%28_%3Aformode%3A%29-392ag.json'
content_hash: 'sha256:94557dc4b2388003'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [RunLoop](../runloop.md)

# add(_:forMode:)

<sub>Instance Method</sub>

Registers a given timer with a given input mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func add(_ timer: Timer, forMode mode: RunLoop.Mode)
```

## Parameters

- `timer` — The timer to register with the receiver.

- `mode` — The mode in which to add `aTimer`. You may specify a custom mode or use one of the modes listed in `Run Loop Modes`.

## Discussion

You can add a timer to multiple input modes. While running in the designated mode, the receiver causes the timer to fire on or after its scheduled fire date. Upon firing, the timer invokes its associated handler routine, which is a selector on a designated object.

The receiver retains `aTimer`. To remove a timer from all run loop modes on which it is installed, send an [- invalidate](<../timer/invalidate().md>) message to the timer.
