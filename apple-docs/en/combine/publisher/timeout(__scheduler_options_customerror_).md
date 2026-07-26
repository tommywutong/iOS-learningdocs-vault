---
title: 'timeout(_:scheduler:options:customError:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/timeout(_:scheduler:options:customerror:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/timeout(_:scheduler:options:customerror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/timeout%28_%3Ascheduler%3Aoptions%3Acustomerror%3A%29.json'
content_hash: 'sha256:16b54a5138af98f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# timeout(_:scheduler:options:customError:)

<sub>Instance Method</sub>

Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func timeout<S>(_ interval: S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions? = nil, customError: (() -> Self.Failure)? = nil) -> Publishers.Timeout<Self, S> where S : Scheduler
```

## Parameters

- `interval` — The maximum time interval the publisher can go without emitting an element, expressed in the time system of the scheduler.

- `scheduler` — The scheduler on which to deliver events.

- `options` — Scheduler options that customize the delivery of elements.

- `customError` — A closure that executes if the publisher times out. The publisher sends the failure returned by this closure to the subscriber as the reason for termination.

## Return Value

A publisher that terminates if the specified interval elapses with no events received from the upstream publisher.

## Discussion

Use [timeout(_:scheduler:options:customError:)](<timeout(__scheduler_options_customerror_).md>) to terminate a publisher if an element isn’t delivered within a timeout interval you specify.

In the example below, a [PassthroughSubject](../passthroughsubject.md) publishes [String](../../swift/string.md) elements and is configured to time out if no new elements are received within its `TIME_OUT` window of 5 seconds. A single value is published after the specified 2-second `WAIT_TIME`, after which no more elements are available; the publisher then times out and completes normally.

```swift
var WAIT_TIME : Int = 2
var TIMEOUT_TIME : Int = 5

let subject = PassthroughSubject<String, Never>()
let cancellable = subject
    .timeout(.seconds(TIMEOUT_TIME), scheduler: DispatchQueue.main, options: nil, customError:nil)
    .sink(
          receiveCompletion: { print ("completion: \($0) at \(Date())") },
          receiveValue: { print ("value: \($0) at \(Date())") }
     )

DispatchQueue.main.asyncAfter(deadline: .now() + .seconds(WAIT_TIME),
                              execute: { subject.send("Some data - sent after a delay of \(WAIT_TIME) seconds") } )

// Prints: value: Some data - sent after a delay of 2 seconds at 2020-03-10 23:47:59 +0000
//         completion: finished at 2020-03-10 23:48:04 +0000
```

If `customError` is `nil`, the publisher completes normally; if you provide a closure for the `customError` argument, the upstream publisher is instead terminated upon timeout, and the error is delivered to the downstream.

## See Also

### Controlling timing

- [measureInterval(using:options:)](<measureinterval(using_options_).md>) — Measures and emits the time interval between events received from an upstream publisher.
- [debounce(for:scheduler:options:)](<debounce(for_scheduler_options_).md>) — Publishes elements only after a specified time interval elapses between events.
- [delay(for:tolerance:scheduler:options:)](<delay(for_tolerance_scheduler_options_).md>) — Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [throttle(for:scheduler:latest:)](<throttle(for_scheduler_latest_).md>) — Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
