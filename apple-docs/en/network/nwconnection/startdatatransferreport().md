---
title: startDataTransferReport()
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/startdatatransferreport()
source_url: 'https://developer.apple.com/documentation/network/nwconnection/startdatatransferreport()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/startdatatransferreport%28%29.json'
content_hash: 'sha256:dea37069c927a09f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# startDataTransferReport()

<sub>Instance Method</sub>

Begins a new data transfer report, which can later be collected.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func startDataTransferReport() -> NWConnection.PendingDataTransferReport
```

## See Also

### Collecting Connection Metrics

- [Collecting Network Connection Metrics](../collecting-network-connection-metrics.md) — Use reports to understand how DNS and protocol handshakes impact connection establishment.
- [requestEstablishmentReport(queue:completion:)](<requestestablishmentreport(queue_completion_).md>) — Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [EstablishmentReport](establishmentreport.md) — A report that provides metrics about the establishment of a connection.
- [PendingDataTransferReport](pendingdatatransferreport.md) — An outstanding data transfer report that has yet to be collected.
- [DataTransferReport](datatransferreport.md) — A report that provides metrics about data being sent and received on a connection.
