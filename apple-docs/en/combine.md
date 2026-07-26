---
title: Combine
framework: Combine
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine
source_url: 'https://developer.apple.com/documentation/combine'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine.json'
content_hash: 'sha256:cad9cbb8fed7eeb0'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Combine

<sub>Framework</sub>

Customize handling of asynchronous events by combining event-processing operators.

## Overview

The Combine framework provides a declarative Swift API for processing values over time. These values can represent many kinds of asynchronous events. Combine declares _publishers_ to expose values that can change over time, and _subscribers_ to receive those values from the publishers.

- The [Publisher](combine/publisher.md) protocol declares a type that can deliver a sequence of values over time. Publishers have _operators_ to act on the values received from upstream publishers and republish them.
- At the end of a chain of publishers, a [Subscriber](combine/subscriber.md) acts on elements as it receives them. Publishers only emit values when explicitly requested to do so by subscribers. This puts your subscriber code in control of how fast it receives events from the publishers it’s connected to.

Several Foundation types expose their functionality through publishers, including [Timer](foundation/timer.md), [NotificationCenter](foundation/notificationcenter.md), and [URLSession](foundation/urlsession.md). Combine also provides a built-in publisher for any property that’s compliant with Key-Value Observing.

You can combine the output of multiple publishers and coordinate their interaction. For example, you can subscribe to updates from a text field’s publisher, and use the text to perform URL requests. You can then use another publisher to process the responses and use them to update your app.

By adopting Combine, you’ll make your code easier to read and maintain, by centralizing your event-processing code and eliminating troublesome techniques like nested closures and convention-based callbacks.

## Topics

### Essentials

- [Receiving and Handling Events with Combine](combine/receiving-and-handling-events-with-combine.md) — Customize and receive events from asynchronous sources.

### Publishers

- [Publisher](combine/publisher.md) — Declares that a type can transmit a sequence of values over time.
- [Publishers](combine/publishers.md) — A namespace for types that serve as publishers.
- [AnyPublisher](combine/anypublisher.md) — A publisher that performs type erasure by wrapping another publisher.
- [Published](combine/published.md) — A type that publishes a property marked with an attribute.
- [Cancellable](combine/cancellable.md) — A protocol indicating that an activity or action supports cancellation.
- [AnyCancellable](combine/anycancellable.md) — A type-erasing cancellable object that executes a provided closure when canceled.

### Convenience Publishers

- [Future](combine/future.md) — A publisher that eventually produces a single value and then finishes or fails.
- [Just](combine/just.md) — A publisher that emits an output to each subscriber just once, and then finishes.
- [Deferred](combine/deferred.md) — A publisher that awaits subscription before running the supplied closure to create a publisher for the new subscriber.
- [Empty](combine/empty.md) — A publisher that never publishes any values, and optionally finishes immediately.
- [Fail](combine/fail.md) — A publisher that immediately terminates with the specified error.
- [Record](combine/record.md) — A publisher that allows for recording a series of inputs and a completion, for later playback to each subscriber.

### Connectable Publishers

- [Controlling Publishing with Connectable Publishers](combine/controlling-publishing-with-connectable-publishers.md) — Coordinate when publishers start sending elements to subscribers.
- [ConnectablePublisher](combine/connectablepublisher.md) — A publisher that provides an explicit means of connecting and canceling publication.

### Subscribers

- [Processing Published Elements with Subscribers](combine/processing-published-elements-with-subscribers.md) — Apply back pressure to precisely control when publishers produce elements.
- [Subscriber](combine/subscriber.md) — A protocol that declares a type that can receive input from a publisher.
- [Subscribers](combine/subscribers.md) — A namespace for types that serve as subscribers.
- [AnySubscriber](combine/anysubscriber.md) — A type-erasing subscriber.
- [Subscription](combine/subscription.md) — A protocol representing the connection of a subscriber to a publisher.
- [Subscriptions](combine/subscriptions.md) — A namespace for symbols related to subscriptions.

### Subjects

- [Subject](combine/subject.md) — A publisher that exposes a method for outside callers to publish elements.
- [CurrentValueSubject](combine/currentvaluesubject.md) — A subject that wraps a single value and publishes a new element whenever the value changes.
- [PassthroughSubject](combine/passthroughsubject.md) — A subject that broadcasts elements to downstream subscribers.

### Schedulers

- [Scheduler](combine/scheduler.md) — A protocol that defines when and how to execute a closure.
- [ImmediateScheduler](combine/immediatescheduler.md) — A scheduler for performing synchronous actions.
- [SchedulerTimeIntervalConvertible](combine/schedulertimeintervalconvertible.md) — A protocol that provides a scheduler with an expression for relative time.

### Combine Migration

- [Routing Notifications to Combine Subscribers](combine/routing-notifications-to-combine-subscribers.md) — Deliver notifications to subscribers by using notification centers’ publishers.
- [Replacing Foundation Timers with Timer Publishers](combine/replacing-foundation-timers-with-timer-publishers.md) — Publish elements periodically by using a timer.
- [Performing Key-Value Observing with Combine](combine/performing-key-value-observing-with-combine.md) — Expose KVO changes with a Combine publisher.
- [Using Combine for Your App’s Asynchronous Code](combine/using-combine-for-your-app-s-asynchronous-code.md) — Apply common patterns to migrate your closure-based, event-handling code.

### Observable Objects

- [ObservableObject](combine/observableobject.md) — A type of object with a publisher that emits before the object has changed.
- [ObservableObjectPublisher](combine/observableobjectpublisher.md) — A publisher that publishes changes from observable objects.

### Asynchronous Publishers

- [AsyncPublisher](combine/asyncpublisher.md) — A publisher that exposes its elements as an asynchronous sequence.
- [AsyncThrowingPublisher](combine/asyncthrowingpublisher.md) — A publisher that exposes its elements as a throwing asynchronous sequence.

### Encoders and Decoders

- [TopLevelEncoder](combine/toplevelencoder.md) — A type that defines methods for encoding.
- [TopLevelDecoder](combine/topleveldecoder.md) — A type that defines methods for decoding.

### Debugging Identifiers

- [CustomCombineIdentifierConvertible](combine/customcombineidentifierconvertible.md) — A protocol for uniquely identifying publisher streams.
- [CombineIdentifier](combine/combineidentifier.md) — A unique identifier for identifying publisher streams.
