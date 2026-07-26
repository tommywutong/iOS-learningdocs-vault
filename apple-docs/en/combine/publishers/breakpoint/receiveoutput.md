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
doc_path: /documentation/combine/publishers/breakpoint/receiveoutput
source_url: 'https://developer.apple.com/documentation/combine/publishers/breakpoint/receiveoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/breakpoint/receiveoutput.json'
content_hash: 'sha256:8f7b45c963c5f841'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Breakpoint](../breakpoint.md)

# receiveOutput

<sub>Instance Property</sub>

A closure that executes when the publisher receives output from the upstream publisher, and can raise a debugger signal by returning a true Boolean value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let receiveOutput: ((Upstream.Output) -> Bool)?
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [receiveSubscription](receivesubscription.md) — A closure that executes when the publisher receives a subscription, and can raise a debugger signal by returning a true Boolean value.
- [receiveCompletion](receivecompletion.md) — A closure that executes when the publisher receives completion, and can raise a debugger signal by returning a true Boolean value.
