---
title: 'onBetterPathUpdate(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/networkchannel/onbetterpathupdate(_:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/onbetterpathupdate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/onbetterpathupdate%28_%3A%29.json'
content_hash: 'sha256:084ddfe418fff937'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# onBetterPathUpdate(_:)

<sub>Instance Method</sub>

A better path being available indicates that the system thinks there is a preferred path or interface to use, compared to the one this connection is actively using. As an example, the connection is established over an expensive cellular interface and an unmetered Wi-Fi interface is now available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func onBetterPathUpdate(_ handler: @escaping @isolated(any) @Sendable (Self, Bool) -> Void) -> Self
```

## Discussion

Set a closure to be called when a better path becomes available or unavailable, which may be called multiple times until the connection is cancelled.

When a better path is available, if it is possible to migrate work from this connection to a new connection, create a new connection to the endpoint. Continue doing work on this connection until the new connection is ready. Once ready, transition work to the new connection and cancel this one.

This closure will inherit the isolation domain of the caller.
