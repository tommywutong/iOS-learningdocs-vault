---
title: receiveCompletion
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/handleevents/receivecompletion
source_url: 'https://developer.apple.com/documentation/combine/publishers/handleevents/receivecompletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/handleevents/receivecompletion.json'
content_hash: 'sha256:d60d2dd6b2b15561'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [HandleEvents](../handleevents.md)

# receiveCompletion

<sub>Instance Property</sub>

A closure that executes when the upstream publisher finishes normally or terminates with an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var receiveCompletion: ((Subscribers.Completion<Publishers.HandleEvents<Upstream>.Failure>) -> Void)?
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [receiveSubscription](receivesubscription.md) — A closure that executes when the publisher receives the subscription from the upstream publisher.
- [receiveOutput](receiveoutput.md) — A closure that executes when the publisher receives a value from the upstream publisher.
- [receiveCancel](receivecancel.md) — A closure that executes when the downstream receiver cancels publishing.
- [receiveRequest](receiverequest.md) — A closure that executes when the publisher receives a request for more elements.
