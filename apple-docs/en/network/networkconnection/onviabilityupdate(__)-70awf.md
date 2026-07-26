---
title: 'onViabilityUpdate(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkconnection/onviabilityupdate(_:)-70awf'
source_url: 'https://developer.apple.com/documentation/network/networkconnection/onviabilityupdate(_:)-70awf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/onviabilityupdate%28_%3A%29-70awf.json'
content_hash: 'sha256:7ac4bb37dede6aaa'
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
