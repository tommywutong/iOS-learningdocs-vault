---
title: 'throttle(for:scheduler:latest:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/throttle(for:scheduler:latest:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/throttle(for:scheduler:latest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/throttle%28for%3Ascheduler%3Alatest%3A%29.json'
content_hash: 'sha256:cf9d9f958eed3fab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# throttle(for:scheduler:latest:)

<sub>Instance Method</sub>

Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func throttle<S>(for interval: S.SchedulerTimeType.Stride, scheduler: S, latest: Bool) -> Publishers.Throttle<Self, S> where S : Scheduler
```

## Parameters

- `interval` — The interval at which to find and emit either the most recent or the first element, expressed in the time system of the scheduler.

- `scheduler` — The scheduler on which to publish elements.

- `latest` — A Boolean value that indicates whether to publish the most recent element. If `false`, the publisher emits the first element received during the interval.

## Return Value

A publisher that emits either the most-recent or first element received during the specified interval.

## Discussion

Use [throttle(for:scheduler:latest:)](<throttle(for_scheduler_latest_).md>) to selectively republish elements from an upstream publisher during an interval you specify. Other elements received from the upstream in the throttling interval aren’t republished.

In the example below, a [Timer.TimerPublisher](../../foundation/timer/timerpublisher.md) produces elements on one-second intervals; the [throttle(for:scheduler:latest:)](<throttle(for_scheduler_latest_).md>) operator delivers the first event, then republishes only the latest event in the following ten second intervals:

```swift
cancellable = Timer.publish(every: 3.0, on: .main, in: .default)
    .autoconnect()
    .print("\(Date().description)")
    .throttle(for: 10.0, scheduler: RunLoop.main, latest: true)
    .sink(
        receiveCompletion: { print ("Completion: \($0).") },
        receiveValue: { print("Received Timestamp \($0).") }
     )

// Prints:
 //    Publish at: 2020-03-19 18:26:54 +0000: receive value: (2020-03-19 18:26:57 +0000)
 //    Received Timestamp 2020-03-19 18:26:57 +0000.
 //    Publish at: 2020-03-19 18:26:54 +0000: receive value: (2020-03-19 18:27:00 +0000)
 //    Publish at: 2020-03-19 18:26:54 +0000: receive value: (2020-03-19 18:27:03 +0000)
 //    Publish at: 2020-03-19 18:26:54 +0000: receive value: (2020-03-19 18:27:06 +0000)
 //    Publish at: 2020-03-19 18:26:54 +0000: receive value: (2020-03-19 18:27:09 +0000)
 //    Received Timestamp 2020-03-19 18:27:09 +0000.
```

## See Also

### Controlling timing

- [measureInterval(using:options:)](<measureinterval(using_options_).md>) — Measures and emits the time interval between events received from an upstream publisher.
- [debounce(for:scheduler:options:)](<debounce(for_scheduler_options_).md>) — Publishes elements only after a specified time interval elapses between events.
- [delay(for:tolerance:scheduler:options:)](<delay(for_tolerance_scheduler_options_).md>) — Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [timeout(_:scheduler:options:customError:)](<timeout(__scheduler_options_customerror_).md>) — Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
