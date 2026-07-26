---
title: receiveOutput
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/handleevents/receiveoutput
source_url: 'https://developer.apple.com/documentation/combine/publishers/handleevents/receiveoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/handleevents/receiveoutput.json'
content_hash: 'sha256:5f87f4c7cf7d03b3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [HandleEvents](../handleevents.md)

# receiveOutput

<sub>Instance Property</sub>

A closure that executes when the publisher receives a value from the upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var receiveOutput: ((Publishers.HandleEvents<Upstream>.Output) -> Void)?
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [receiveSubscription](receivesubscription.md) — A closure that executes when the publisher receives the subscription from the upstream publisher.
- [receiveCompletion](receivecompletion.md) — A closure that executes when the upstream publisher finishes normally or terminates with an error.
- [receiveCancel](receivecancel.md) — A closure that executes when the downstream receiver cancels publishing.
- [receiveRequest](receiverequest.md) — A closure that executes when the publisher receives a request for more elements.
