---
title: 'init(upstream:receiveSubscription:receiveOutput:receiveCompletion:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/breakpoint/init(upstream:receivesubscription:receiveoutput:receivecompletion:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/breakpoint/init(upstream:receivesubscription:receiveoutput:receivecompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/breakpoint/init%28upstream%3Areceivesubscription%3Areceiveoutput%3Areceivecompletion%3A%29.json'
content_hash: 'sha256:f833692ef6804c6e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Breakpoint](../breakpoint.md)

# init(upstream:receiveSubscription:receiveOutput:receiveCompletion:)

<sub>Initializer</sub>

Creates a breakpoint publisher with the provided upstream publisher and breakpoint-raising closures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, receiveSubscription: ((any Subscription) -> Bool)? = nil, receiveOutput: ((Upstream.Output) -> Bool)? = nil, receiveCompletion: ((Subscribers.Completion<Publishers.Breakpoint<Upstream>.Failure>) -> Bool)? = nil)
```

## Parameters

- `upstream` — The publisher from which this publisher receives elements.

- `receiveSubscription` — A closure that executes when the publisher receives a subscription, and can raise a debugger signal by returning a true Boolean value.

- `receiveOutput` — A closure that executes when the publisher receives output from the upstream publisher, and can raise a debugger signal by returning a true Boolean value.

- `receiveCompletion` — A closure that executes when the publisher receives completion, and can raise a debugger signal by returning a true Boolean value.
