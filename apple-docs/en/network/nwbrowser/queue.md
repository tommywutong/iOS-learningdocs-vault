---
title: queue
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwbrowser/queue
source_url: 'https://developer.apple.com/documentation/network/nwbrowser/queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwbrowser/queue.json'
content_hash: 'sha256:b81fcc1621829c35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWBrowser](../nwbrowser.md)

# queue

<sub>Instance Property</sub>

The queue on which browser events are delivered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var queue: DispatchQueue? { get }
```

## See Also

### Inspecting Browsers

- [descriptor](descriptor-swift.property.md) — The service descriptor with which the browser was initialized.
- [parameters](parameters.md) — The parameters with which the browser was initialized.
