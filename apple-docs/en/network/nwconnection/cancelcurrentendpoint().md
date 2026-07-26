---
title: cancelCurrentEndpoint()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/cancelcurrentendpoint()
source_url: 'https://developer.apple.com/documentation/network/nwconnection/cancelcurrentendpoint()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/cancelcurrentendpoint%28%29.json'
content_hash: 'sha256:005447c5f227474a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# cancelCurrentEndpoint()

<sub>Instance Method</sub>

Causes the current endpoint to be rejected, allowing the connection to try another resolved address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func cancelCurrentEndpoint()
```

## Discussion

Protocols that do not have handshakes, such as UDP, do not allow connections to validate connectivity on their own. Cancelling an endpoint allows you to indicate that a certain endpoint should be rejected due to a lack of valid response. If other addresses were resolved for the remote endpoint, those will be attempted next.

## See Also

### Canceling Connections

- [cancel()](<cancel().md>) — Cancels the connection and gracefully disconnects any established network protocols.
- [forceCancel()](<forcecancel().md>) — Cancels the connection and immediately disconnects any established network protocols.
