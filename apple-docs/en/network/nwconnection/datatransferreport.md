---
title: NWConnection.DataTransferReport
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/datatransferreport
source_url: 'https://developer.apple.com/documentation/network/nwconnection/datatransferreport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/datatransferreport.json'
content_hash: 'sha256:113d63722e9579ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# NWConnection.DataTransferReport

<sub>Structure</sub>

A report that provides metrics about data being sent and received on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DataTransferReport
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Examining Data Transfer

- [aggregatePathReport](datatransferreport/aggregatepathreport.md) — A report that sums counts across all network paths.
- [pathReports](datatransferreport/pathreports.md) — An array of reports for each network path the connection used.
- [PathReport](datatransferreport/pathreport.md) — A report that contains details about data transfer over a single network path.

### Summarizing Reports

- [duration](datatransferreport/duration.md) — The duration of the data transfer report, from when it was started to when it was collected.

## See Also

### Collecting Connection Metrics

- [Collecting Network Connection Metrics](../collecting-network-connection-metrics.md) — Use reports to understand how DNS and protocol handshakes impact connection establishment.
- [requestEstablishmentReport(queue:completion:)](<requestestablishmentreport(queue_completion_).md>) — Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [EstablishmentReport](establishmentreport.md) — A report that provides metrics about the establishment of a connection.
- [startDataTransferReport()](<startdatatransferreport().md>) — Begins a new data transfer report, which can later be collected.
- [PendingDataTransferReport](pendingdatatransferreport.md) — An outstanding data transfer report that has yet to be collected.
