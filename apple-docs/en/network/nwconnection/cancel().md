---
title: cancel()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/cancel()
source_url: 'https://developer.apple.com/documentation/network/nwconnection/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/cancel%28%29.json'
content_hash: 'sha256:df4a5d740cae5e98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# cancel()

<sub>Instance Method</sub>

Cancels the connection and gracefully disconnects any established network protocols.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func cancel()
```

## See Also

### Canceling Connections

- [forceCancel()](<forcecancel().md>) — Cancels the connection and immediately disconnects any established network protocols.
- [cancelCurrentEndpoint()](<cancelcurrentendpoint().md>) — Causes the current endpoint to be rejected, allowing the connection to try another resolved address.
