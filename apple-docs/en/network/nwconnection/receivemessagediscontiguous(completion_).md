---
title: 'receiveMessageDiscontiguous(completion:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/receivemessagediscontiguous(completion:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/receivemessagediscontiguous(completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/receivemessagediscontiguous%28completion%3A%29.json'
content_hash: 'sha256:2650c72199801078'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# receiveMessageDiscontiguous(completion:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final func receiveMessageDiscontiguous(completion: @escaping @Sendable (DispatchData?, NWConnection.ContentContext?, Bool, NWError?) -> Void)
```
