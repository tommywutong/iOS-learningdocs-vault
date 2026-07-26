---
title: 'init(upstream:receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/handleevents/init(upstream:receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/handleevents/init(upstream:receivesubscription:receiveoutput:receivecompletion:receivecancel:receiverequest:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/handleevents/init%28upstream%3Areceivesubscription%3Areceiveoutput%3Areceivecompletion%3Areceivecancel%3Areceiverequest%3A%29.json'
content_hash: 'sha256:985527bf4b84acb2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [HandleEvents](../handleevents.md)

# init(upstream:receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)

<sub>Initializer</sub>

Creates a publisher that performs the specified closures when publisher events occur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, receiveSubscription: ((any Subscription) -> Void)? = nil, receiveOutput: ((Publishers.HandleEvents<Upstream>.Output) -> Void)? = nil, receiveCompletion: ((Subscribers.Completion<Publishers.HandleEvents<Upstream>.Failure>) -> Void)? = nil, receiveCancel: (() -> Void)? = nil, receiveRequest: ((Subscribers.Demand) -> Void)?)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `receiveSubscription` — A closure that executes when the publisher receives the subscription from the upstream publisher.

- `receiveOutput` — A closure that executes when the publisher receives a value from the upstream publisher.

- `receiveCompletion` — A closure that executes when the publisher receives the completion from the upstream publisher.

- `receiveCancel` — A closure that executes when the downstream receiver cancels publishing.

- `receiveRequest` — A closure that executes when the publisher receives a request for more elements.
