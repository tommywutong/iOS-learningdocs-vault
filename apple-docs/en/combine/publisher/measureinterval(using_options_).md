---
title: 'measureInterval(using:options:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/measureinterval(using:options:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/measureinterval(using:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/measureinterval%28using%3Aoptions%3A%29.json'
content_hash: 'sha256:4d150a1444884bc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# measureInterval(using:options:)

<sub>Instance Method</sub>

Measures and emits the time interval between events received from an upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func measureInterval<S>(using scheduler: S, options: S.SchedulerOptions? = nil) -> Publishers.MeasureInterval<Self, S> where S : Scheduler
```

## Parameters

- `scheduler` — A scheduler to use for tracking the timing of events.

- `options` — Options that customize the delivery of elements.

## Return Value

A publisher that emits elements representing the time interval between the elements it receives.

## Discussion

Use [measureInterval(using:options:)](<measureinterval(using_options_).md>) to measure the time between events delivered from an upstream publisher.

In the example below, a 1-second [Timer](../../foundation/timer.md) is used as the data source for an event publisher; the [measureInterval(using:options:)](<measureinterval(using_options_).md>) operator reports the elapsed time between the reception of events on the main run loop:

```swift
cancellable = Timer.publish(every: 1, on: .main, in: .default)
    .autoconnect()
    .measureInterval(using: RunLoop.main)
    .sink { print("\($0)", terminator: "\n") }

// Prints:
//      Stride(magnitude: 1.0013610124588013)
//      Stride(magnitude: 0.9992760419845581)
```

The output type of the returned publisher is the time interval of the provided scheduler.

This operator uses the provided scheduler’s [now](../scheduler/now.md) property to measure intervals between events.

## See Also

### Controlling timing

- [debounce(for:scheduler:options:)](<debounce(for_scheduler_options_).md>) — Publishes elements only after a specified time interval elapses between events.
- [delay(for:tolerance:scheduler:options:)](<delay(for_tolerance_scheduler_options_).md>) — Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [throttle(for:scheduler:latest:)](<throttle(for_scheduler_latest_).md>) — Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [timeout(_:scheduler:options:customError:)](<timeout(__scheduler_options_customerror_).md>) — Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
