---
title: 'publish(every:tolerance:on:in:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/timer/publish(every:tolerance:on:in:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/timer/publish(every:tolerance:on:in:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/timer/publish%28every%3Atolerance%3Aon%3Ain%3Aoptions%3A%29.json'
content_hash: 'sha256:964373b964de59e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Timer](../timer.md)

# publish(every:tolerance:on:in:options:)

<sub>Type Method</sub>

Returns a publisher that repeatedly emits the current date on the given interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func publish(every interval: TimeInterval, tolerance: TimeInterval? = nil, on runLoop: RunLoop, in mode: RunLoop.Mode, options: RunLoop.SchedulerOptions? = nil) -> Timer.TimerPublisher
```

## Parameters

- `interval` — The time interval on which to publish events. For example, a value of `0.5` publishes an event approximately every half-second.

- `tolerance` — The allowed timing variance when emitting events. Defaults to `nil`, which allows any variance.

- `runLoop` — The run loop on which the timer runs.

- `mode` — The run loop mode in which to run the timer.

- `options` — Scheduler options passed to the timer. Defaults to `nil`.

## Return Value

A publisher that repeatedly emits the current date on the given interval.

## Discussion

The return type, [TimerPublisher](timerpublisher.md), conforms to [ConnectablePublisher](../../combine/connectablepublisher.md), which means you must explicitly connect to the [Timer](../timer.md) publisher to begin publishing events. You can do this with a call to [connect()](<../../combine/connectablepublisher/connect().md>), or by using [autoconnect()](<../../combine/connectablepublisher/autoconnect().md>) to automatically connect when a subscriber attaches, as shown here:

```swift
cancellable = Timer.publish(every: 1, on: .main, in: .common)
    .autoconnect()
    .sink() {
        print ("timer fired: \($0)")
}

```

## Topics

### Creating a Timer Publisher

- [init(interval:tolerance:runLoop:mode:options:)](<timerpublisher/init(interval_tolerance_runloop_mode_options_).md>) — Creates a publisher that repeatedly emits the current date on the given interval.

## See Also

### Firing Messages as a Combine Publisher

- [TimerPublisher](timerpublisher.md) — A publisher that repeatedly emits the current date on a given interval.
