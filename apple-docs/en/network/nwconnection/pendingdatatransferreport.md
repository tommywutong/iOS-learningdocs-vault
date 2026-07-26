---
title: NWConnection.PendingDataTransferReport
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/pendingdatatransferreport
source_url: 'https://developer.apple.com/documentation/network/nwconnection/pendingdatatransferreport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/pendingdatatransferreport.json'
content_hash: 'sha256:d0ebfdce31d7938d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# NWConnection.PendingDataTransferReport

<sub>Class</sub>

An outstanding data transfer report that has yet to be collected.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class PendingDataTransferReport
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Collecting Reports

- [collect(queue:completion:)](<pendingdatatransferreport/collect(queue_completion_).md>) — Stops an outstanding data transfer report and delivers the result.

## See Also

### Collecting Connection Metrics

- [Collecting Network Connection Metrics](../collecting-network-connection-metrics.md) — Use reports to understand how DNS and protocol handshakes impact connection establishment.
- [requestEstablishmentReport(queue:completion:)](<requestestablishmentreport(queue_completion_).md>) — Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [EstablishmentReport](establishmentreport.md) — A report that provides metrics about the establishment of a connection.
- [startDataTransferReport()](<startdatatransferreport().md>) — Begins a new data transfer report, which can later be collected.
- [DataTransferReport](datatransferreport.md) — A report that provides metrics about data being sent and received on a connection.
