---
title: 'init(interval:tolerance:runLoop:mode:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timer/timerpublisher/init(interval:tolerance:runloop:mode:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/timer/timerpublisher/init(interval:tolerance:runloop:mode:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/timerpublisher/init%28interval%3Atolerance%3Arunloop%3Amode%3Aoptions%3A%29.json'
content_hash: 'sha256:c7826cbe9926c659'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Timer](../../timer.md) · [TimerPublisher](../timerpublisher.md)

# init(interval:tolerance:runLoop:mode:options:)

<sub>Initializer</sub>

Creates a publisher that repeatedly emits the current date on the given interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(interval: TimeInterval, tolerance: TimeInterval? = nil, runLoop: RunLoop, mode: RunLoop.Mode, options: RunLoop.SchedulerOptions? = nil)
```

## Parameters

- `interval` — The interval on which to publish events.

- `tolerance` — The allowed timing variance when emitting events. Defaults to `nil`, which allows any variance.

- `runLoop` — The run loop on which the timer runs.

- `mode` — The run loop mode in which to run the timer.

- `options` — Scheduler options passed to the timer. Defaults to `nil`.
