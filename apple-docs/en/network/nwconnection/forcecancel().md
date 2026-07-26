---
title: forceCancel()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/forcecancel()
source_url: 'https://developer.apple.com/documentation/network/nwconnection/forcecancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/forcecancel%28%29.json'
content_hash: 'sha256:10dc5e29a2842586'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# forceCancel()

<sub>Instance Method</sub>

Cancels the connection and immediately disconnects any established network protocols.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func forceCancel()
```

## See Also

### Canceling Connections

- [cancel()](<cancel().md>) — Cancels the connection and gracefully disconnects any established network protocols.
- [cancelCurrentEndpoint()](<cancelcurrentendpoint().md>) — Causes the current endpoint to be rejected, allowing the connection to try another resolved address.
