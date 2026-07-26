---
title: 'NWConnection.SendCompletion.contentProcessed(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/sendcompletion/contentprocessed(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/sendcompletion/contentprocessed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/sendcompletion/contentprocessed%28_%3A%29.json'
content_hash: 'sha256:43dfd935876a51d6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [SendCompletion](../sendcompletion.md)

# NWConnection.SendCompletion.contentProcessed(_:)

<sub>Case</sub>

Provide a completion handler that’s invoked when the sent data is processed by the stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency case contentProcessed(@Sendable (NWError?) -> Void)
```

## See Also

### Completions

- [NWConnection.SendCompletion.idempotent](idempotent.md) — Mark the sent data as idempotent—data that can be sent multiple times.
