---
title: customError
framework: Combine
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/timeout/customerror
source_url: 'https://developer.apple.com/documentation/combine/publishers/timeout/customerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/timeout/customerror.json'
content_hash: 'sha256:8cb9016f8108175b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Timeout](../timeout.md)

# customError

<sub>Instance Property</sub>

A closure that executes if the publisher times out. The publisher sends the failure returned by this closure to the subscriber as the reason for termination.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let customError: (() -> Publishers.Timeout<Upstream, Context>.Failure)?
```

## See Also

### Inspecting publisher properties

- [upstream](upstream.md) — The publisher from which this publisher receives elements.
- [interval](interval.md) — The maximum time interval the publisher can go without emitting an element, expressed in the time system of the scheduler.
- [scheduler](scheduler.md) — The scheduler on which to deliver events.
- [options](options.md) — Scheduler options that customize the delivery of elements.
