---
title: 'delay(for:tolerance:scheduler:options:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/delay(for:tolerance:scheduler:options:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/delay(for:tolerance:scheduler:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/delay%28for%3Atolerance%3Ascheduler%3Aoptions%3A%29.json'
content_hash: 'sha256:63a9db7727fbb756'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# delay(for:tolerance:scheduler:options:)

<sub>Instance Method</sub>

Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func delay<S>(for interval: S.SchedulerTimeType.Stride, tolerance: S.SchedulerTimeType.Stride? = nil, scheduler: S, options: S.SchedulerOptions? = nil) -> Publishers.Delay<Self, S> where S : Scheduler
```

## Parameters

- `interval` — The amount of time to delay.

- `tolerance` — The allowed tolerance in delivering delayed events. The `Delay` publisher may deliver elements this much sooner or later than the interval specifies.

- `scheduler` — The scheduler to deliver the delayed events.

- `options` — Options relevant to the scheduler’s behavior.

## Return Value

A publisher that delays delivery of elements and completion to the downstream receiver.

## Discussion

Use [delay(for:tolerance:scheduler:options:)](<delay(for_tolerance_scheduler_options_).md>) when you need to delay the delivery of elements to a downstream by a specified amount of time.

In this example, a [Timer](../../foundation/timer.md) publishes an event every second. The [delay(for:tolerance:scheduler:options:)](<delay(for_tolerance_scheduler_options_).md>) operator holds the delivery of the initial element for 3 seconds (±0.5 seconds), after which each element is delivered to the downstream on the main run loop after the specified delay:

```swift
let df = DateFormatter()
df.dateStyle = .none
df.timeStyle = .long
cancellable = Timer.publish(every: 1.0, on: .main, in: .default)
    .autoconnect()
    .handleEvents(receiveOutput: { date in
        print ("Sending Timestamp \'\(df.string(from: date))\' to delay()")
    })
    .delay(for: .seconds(3), scheduler: RunLoop.main, options: .none)
    .sink(
        receiveCompletion: { print ("completion: \($0)", terminator: "\n") },
        receiveValue: { value in
            let now = Date()
            print ("At \(df.string(from: now)) received  Timestamp \'\(df.string(from: value))\' sent: \(String(format: "%.2f", now.timeIntervalSince(value))) secs ago", terminator: "\n")
        }
    )

// Prints:
//    Sending Timestamp '5:02:33 PM PDT' to delay()
//    Sending Timestamp '5:02:34 PM PDT' to delay()
//    Sending Timestamp '5:02:35 PM PDT' to delay()
//    Sending Timestamp '5:02:36 PM PDT' to delay()
//    At 5:02:36 PM PDT received  Timestamp '5:02:33 PM PDT' sent: 3.00 secs ago
//    Sending Timestamp '5:02:37 PM PDT' to delay()
//    At 5:02:37 PM PDT received  Timestamp '5:02:34 PM PDT' sent: 3.00 secs ago
//    Sending Timestamp '5:02:38 PM PDT' to delay()
//    At 5:02:38 PM PDT received  Timestamp '5:02:35 PM PDT' sent: 3.00 secs ago
```

The delay affects the delivery of elements and completion, but not of the original subscription.

## See Also

### Controlling timing

- [measureInterval(using:options:)](<measureinterval(using_options_).md>) — Measures and emits the time interval between events received from an upstream publisher.
- [debounce(for:scheduler:options:)](<debounce(for_scheduler_options_).md>) — Publishes elements only after a specified time interval elapses between events.
- [throttle(for:scheduler:latest:)](<throttle(for_scheduler_latest_).md>) — Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [timeout(_:scheduler:options:customError:)](<timeout(__scheduler_options_customerror_).md>) — Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
