---
title: 'onPathUpdate(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/networkconnection/onpathupdate(_:)-2uoc8'
source_url: 'https://developer.apple.com/documentation/network/networkconnection/onpathupdate(_:)-2uoc8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/onpathupdate%28_%3A%29-2uoc8.json'
content_hash: 'sha256:dfc3250e91c2dfd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkConnection](../networkconnection.md)

# onPathUpdate(_:)

<sub>Instance Method</sub>

Set a closure to be called when the connection’s path has changed, which may be called multiple times until the connection is cancelled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult final func onPathUpdate(_ handler: @escaping @isolated(any) @Sendable (NetworkConnection<ApplicationProtocol>, NWPath) -> Void) -> Self
```

## Discussion

This closure will inherit the isolation domain of the caller.
