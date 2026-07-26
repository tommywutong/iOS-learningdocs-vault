---
title: 'debounce(for:scheduler:options:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/debounce(for:scheduler:options:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/debounce(for:scheduler:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/debounce%28for%3Ascheduler%3Aoptions%3A%29.json'
content_hash: 'sha256:cc56941e67fe5f66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# debounce(for:scheduler:options:)

<sub>Instance Method</sub>

Publishes elements only after a specified time interval elapses between events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func debounce<S>(for dueTime: S.SchedulerTimeType.Stride, scheduler: S, options: S.SchedulerOptions? = nil) -> Publishers.Debounce<Self, S> where S : Scheduler
```

## Parameters

- `dueTime` — The time the publisher should wait before publishing an element.

- `scheduler` — The scheduler on which this publisher delivers elements

- `options` — Scheduler options that customize this publisher’s delivery of elements.

## Return Value

A publisher that publishes events only after a specified time elapses.

## Discussion

Use the [debounce(for:scheduler:options:)](<debounce(for_scheduler_options_).md>) operator to control the number of values and time between delivery of values from the upstream publisher. This operator is useful to process bursty or high-volume event streams where you need to reduce the number of values delivered to the downstream to a rate you specify.

In this example, a [PassthroughSubject](../passthroughsubject.md) publishes elements on a schedule defined by the `bounces` array. The array is composed of tuples representing a value sent by the [PassthroughSubject](../passthroughsubject.md), and a [TimeInterval](../../foundation/timeinterval.md) ranging from one-quarter second up to 2 seconds that drives a delivery timer. As the queue builds, elements arriving faster than one-half second `debounceInterval` are discarded, while elements arriving at a rate slower than `debounceInterval` are passed through to the [sink(receiveValue:)](<sink(receivevalue_).md>) operator.

```swift
let bounces:[(Int,TimeInterval)] = [
    (0, 0),
    (1, 0.25),  // 0.25s interval since last index
    (2, 1),     // 0.75s interval since last index
    (3, 1.25),  // 0.25s interval since last index
    (4, 1.5),   // 0.25s interval since last index
    (5, 2)      // 0.5s interval since last index
]

let subject = PassthroughSubject<Int, Never>()
cancellable = subject
    .debounce(for: .seconds(0.5), scheduler: RunLoop.main)
    .sink { index in
        print ("Received index \(index)")
    }

for bounce in bounces {
    DispatchQueue.main.asyncAfter(deadline: .now() + bounce.1) {
        subject.send(bounce.0)
    }
}

// Prints:
//  Received index 1
//  Received index 4
//  Received index 5

//  Here is the event flow shown from the perspective of time, showing value delivery through the `debounce()` operator:

//  Time 0: Send index 0.
//  Time 0.25: Send index 1. Index 0 was waiting and is discarded.
//  Time 0.75: Debounce period ends, publish index 1.
//  Time 1: Send index 2.
//  Time 1.25: Send index 3. Index 2 was waiting and is discarded.
//  Time 1.5: Send index 4. Index 3 was waiting and is discarded.
//  Time 2: Debounce period ends, publish index 4. Also, send index 5.
//  Time 2.5: Debounce period ends, publish index 5.
```

## See Also

### Controlling timing

- [measureInterval(using:options:)](<measureinterval(using_options_).md>) — Measures and emits the time interval between events received from an upstream publisher.
- [delay(for:tolerance:scheduler:options:)](<delay(for_tolerance_scheduler_options_).md>) — Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [throttle(for:scheduler:latest:)](<throttle(for_scheduler_latest_).md>) — Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [timeout(_:scheduler:options:customError:)](<timeout(__scheduler_options_customerror_).md>) — Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.
