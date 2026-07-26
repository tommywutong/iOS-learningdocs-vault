---
title: 'subscribe(on:options:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/subscribe(on:options:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/subscribe(on:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/subscribe%28on%3Aoptions%3A%29.json'
content_hash: 'sha256:072d0f764c9b06dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# subscribe(on:options:)

<sub>Instance Method</sub>

Specifies the scheduler on which to perform subscribe, cancel, and request operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subscribe<S>(on scheduler: S, options: S.SchedulerOptions? = nil) -> Publishers.SubscribeOn<Self, S> where S : Scheduler
```

## Parameters

- `scheduler` — The scheduler used to send messages to upstream publishers.

- `options` — Options that customize the delivery of elements.

## Return Value

A publisher which performs upstream operations on the specified scheduler.

## Discussion

In contrast with [receive(on:options:)](<receive(on_options_).md>), which affects downstream messages, [subscribe(on:options:)](<subscribe(on_options_).md>) changes the execution context of upstream messages.

In the following example, the [subscribe(on:options:)](<subscribe(on_options_).md>) operator causes `ioPerformingPublisher` to receive requests on `backgroundQueue`, while the [receive(on:options:)](<receive(on_options_).md>) causes `uiUpdatingSubscriber` to receive elements and completion on `RunLoop.main`.

```swift
let ioPerformingPublisher == // Some publisher.
let uiUpdatingSubscriber == // Some subscriber that updates the UI.

ioPerformingPublisher
    .subscribe(on: backgroundQueue)
    .receive(on: RunLoop.main)
    .subscribe(uiUpdatingSubscriber)
```

Using [subscribe(on:options:)](<subscribe(on_options_).md>) also causes the upstream publisher to perform [cancel()](<../cancellable/cancel().md>) using the specfied scheduler.

## See Also

### Specifying schedulers

- [receive(on:options:)](<receive(on_options_).md>) — Specifies the scheduler on which to receive elements from the publisher.
