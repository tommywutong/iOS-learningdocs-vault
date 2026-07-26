---
title: 'collect(queue:completion:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/pendingdatatransferreport/collect(queue:completion:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/pendingdatatransferreport/collect(queue:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/pendingdatatransferreport/collect%28queue%3Acompletion%3A%29.json'
content_hash: 'sha256:e4506899cfa9d423'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [PendingDataTransferReport](../pendingdatatransferreport.md)

# collect(queue:completion:)

<sub>Instance Method</sub>

Stops an outstanding data transfer report and delivers the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func collect(queue: DispatchQueue, completion: @escaping @Sendable (NWConnection.DataTransferReport) -> Void)
```
