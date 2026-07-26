---
title: 'requestEstablishmentReport(queue:completion:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/requestestablishmentreport(queue:completion:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/requestestablishmentreport(queue:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/requestestablishmentreport%28queue%3Acompletion%3A%29.json'
content_hash: 'sha256:37a72536b449b58b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# requestEstablishmentReport(queue:completion:)

<sub>Instance Method</sub>

Requests a copy of the connection’s establishment report once the connection is in the ready state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final func requestEstablishmentReport(queue: DispatchQueue, completion: @escaping @Sendable (NWConnection.EstablishmentReport?) -> Void)
```

## See Also

### Collecting Connection Metrics

- [Collecting Network Connection Metrics](../collecting-network-connection-metrics.md) — Use reports to understand how DNS and protocol handshakes impact connection establishment.
- [EstablishmentReport](establishmentreport.md) — A report that provides metrics about the establishment of a connection.
- [startDataTransferReport()](<startdatatransferreport().md>) — Begins a new data transfer report, which can later be collected.
- [PendingDataTransferReport](pendingdatatransferreport.md) — An outstanding data transfer report that has yet to be collected.
- [DataTransferReport](datatransferreport.md) — A report that provides metrics about data being sent and received on a connection.
