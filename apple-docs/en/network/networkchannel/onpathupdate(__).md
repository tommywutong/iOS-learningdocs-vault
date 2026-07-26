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
doc_path: '/documentation/network/networkchannel/onpathupdate(_:)'
source_url: 'https://developer.apple.com/documentation/network/networkchannel/onpathupdate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/onpathupdate%28_%3A%29.json'
content_hash: 'sha256:116220ba78abf29f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# onPathUpdate(_:)

<sub>Instance Method</sub>

Set a closure to be called when the connection’s path has changed, which may be called multiple times until the connection is cancelled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func onPathUpdate(_ handler: @escaping @isolated(any) @Sendable (Self, NWPath) -> Void) -> Self
```

## Discussion

This closure will inherit the isolation domain of the caller.
