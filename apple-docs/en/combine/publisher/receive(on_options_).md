---
title: 'receive(on:options:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/receive(on:options:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/receive(on:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/receive%28on%3Aoptions%3A%29.json'
content_hash: 'sha256:e694a293a43b9d34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# receive(on:options:)

<sub>Instance Method</sub>

Specifies the scheduler on which to receive elements from the publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive<S>(on scheduler: S, options: S.SchedulerOptions? = nil) -> Publishers.ReceiveOn<Self, S> where S : Scheduler
```

## Parameters

- `scheduler` — The scheduler the publisher uses for element delivery.

- `options` — Scheduler options used to customize element delivery.

## Return Value

A publisher that delivers elements using the specified scheduler.

## Discussion

You use the [receive(on:options:)](<receive(on_options_).md>) operator to receive results and completion on a specific scheduler, such as performing UI work on the main run loop. In contrast with [subscribe(on:options:)](<subscribe(on_options_).md>), which affects upstream messages, [receive(on:options:)](<receive(on_options_).md>) changes the execution context of downstream messages.

In the following example, the [subscribe(on:options:)](<subscribe(on_options_).md>) operator causes `jsonPublisher` to receive requests on `backgroundQueue`, while the [receive(on:options:)](<receive(on_options_).md>) causes `labelUpdater` to receive elements and completion on `RunLoop.main`.

```swift
let jsonPublisher = MyJSONLoaderPublisher() // Some publisher.
let labelUpdater = MyLabelUpdateSubscriber() // Some subscriber that updates the UI.

jsonPublisher
    .subscribe(on: backgroundQueue)
    .receive(on: RunLoop.main)
    .subscribe(labelUpdater)
```

Prefer [receive(on:options:)](<receive(on_options_).md>) over explicit use of dispatch queues when performing work in subscribers. For example, instead of the following pattern:

```swift
pub.sink {
    DispatchQueue.main.async {
        // Do something.
    }
}
```

Use this pattern instead:

```swift
pub.receive(on: DispatchQueue.main).sink {
    // Do something.
}
```

> [!note] Note
> [receive(on:options:)](<receive(on_options_).md>) doesn’t affect the scheduler used to call the subscriber’s [receive(subscription:)](<../subscriber/receive(subscription_).md>) method.

## See Also

### Specifying schedulers

- [subscribe(on:options:)](<subscribe(on_options_).md>) — Specifies the scheduler on which to perform subscribe, cancel, and request operations.
