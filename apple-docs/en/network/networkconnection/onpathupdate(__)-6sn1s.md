---
title: 'onPathUpdate(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkconnection/onpathupdate(_:)-6sn1s'
source_url: 'https://developer.apple.com/documentation/network/networkconnection/onpathupdate(_:)-6sn1s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection/onpathupdate%28_%3A%29-6sn1s.json'
content_hash: 'sha256:5b4f1a3266ecd5ad'
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
