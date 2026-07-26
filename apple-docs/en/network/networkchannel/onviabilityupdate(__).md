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
doc_path: '/documentation/network/networkchannel/onviabilityupdate(_:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/onviabilityupdate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/onviabilityupdate%28_%3A%29.json'
content_hash: 'sha256:15e8a44167de8d7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# onViabilityUpdate(_:)

<sub>Instance Method</sub>

Set a closure to be called when the connection’s viability changes, which may be called multiple times until the connection is cancelled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func onViabilityUpdate(_ handler: @escaping @isolated(any) @Sendable (Self, Bool) -> Void) -> Self
```

## Discussion

Connections that are not currently viable do not have a route, and packets will not be sent or received. There is a possibility that the connection will become viable again when network connectivity changes.

This closure will inherit the isolation domain of the caller.
