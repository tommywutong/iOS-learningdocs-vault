---
title: upstream
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/breakpoint/upstream
source_url: 'https://developer.apple.com/documentation/combine/publishers/breakpoint/upstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/breakpoint/upstream.json'
content_hash: 'sha256:c12c3d9bebc710de'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Breakpoint](../breakpoint.md)

# upstream

<sub>Instance Property</sub>

The publisher from which this publisher receives elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let upstream: Upstream
```

## See Also

### Inspecting publisher properties

- [receiveSubscription](receivesubscription.md) — A closure that executes when the publisher receives a subscription, and can raise a debugger signal by returning a true Boolean value.
- [receiveOutput](receiveoutput.md) — A closure that executes when the publisher receives output from the upstream publisher, and can raise a debugger signal by returning a true Boolean value.
- [receiveCompletion](receivecompletion.md) — A closure that executes when the publisher receives completion, and can raise a debugger signal by returning a true Boolean value.
