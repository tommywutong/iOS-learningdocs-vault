---
title: 'onViabilityUpdate(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/networkconnection/onviabilityupdate(_:)-13jwf'
source_url: 'https://developer.apple.com/documentation/network/networkconnection/onviabilityupdate(_:)-13jwf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/onviabilityupdate%28_%3A%29-13jwf.json'
content_hash: 'sha256:e0cad6f7cdbd751c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkConnection](../networkconnection.md)

# onViabilityUpdate(_:)

<sub>Instance Method</sub>

Set a closure to be called when the connection’s viability changes, which may be called multiple times until the connection is cancelled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult final func onViabilityUpdate(_ handler: @escaping @isolated(any) @Sendable (NetworkConnection<ApplicationProtocol>, Bool) -> Void) -> Self
```

## Discussion

Connections that are not currently viable do not have a route, and packets will not be sent or received. There is a possibility that the connection will become viable again when network connectivity changes.

This closure will inherit the isolation domain of the caller.
