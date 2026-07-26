---
title: NWConnection.DataTransferReport.PathReport
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/datatransferreport/pathreport
source_url: 'https://developer.apple.com/documentation/network/nwconnection/datatransferreport/pathreport'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/datatransferreport/pathreport.json'
content_hash: 'sha256:d8234e9de3b44293'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWConnection](../../nwconnection.md) · [DataTransferReport](../datatransferreport.md)

# NWConnection.DataTransferReport.PathReport

<sub>Structure</sub>

A report that contains details about data transfer over a single network path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PathReport
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Identifying Paths

- [interface](pathreport/interface.md) — The network interface this path used.

### Inspecting Application Metrics

- [receivedApplicationByteCount](pathreport/receivedapplicationbytecount.md) — The number of bytes the connection delivered.
- [sentApplicationByteCount](pathreport/sentapplicationbytecount.md) — The number of bytes sent on the connection.

### Inspecting Transport Metrics

- [receivedTransportByteCount](pathreport/receivedtransportbytecount.md) — The number of bytes the transport protocol delivered.
- [receivedTransportDuplicateByteCount](pathreport/receivedtransportduplicatebytecount.md) — The number of duplicated bytes the transport protocol detected.
- [receivedTransportOutOfOrderByteCount](pathreport/receivedtransportoutoforderbytecount.md) — The number of bytes the transport protocol received out of order.
- [sentTransportByteCount](pathreport/senttransportbytecount.md) — The number of bytes sent into the transport protocol.
- [retransmittedTransportByteCount](pathreport/retransmittedtransportbytecount.md) — The number of bytes the transport protocol retransmitted.
- [transportSmoothedRTT](pathreport/transportsmoothedrtt.md) — The smoothed round-trip time the transport protocol measured.
- [transportMinimumRTT](pathreport/transportminimumrtt.md) — The minimum round-trip time the transport protocol measured.
- [transportRTTVariance](pathreport/transportrttvariance.md) — The variance of the round-trip time the transport protocol measured.

### Inspecting Packet Metrics

- [receivedIPPacketCount](pathreport/receivedippacketcount.md) — The number of IP packets the connection received.
- [sentIPPacketCount](pathreport/sentippacketcount.md) — The number of IP packets the connection sent.

### Instance Properties

- [radioType](pathreport/radiotype.md)

## See Also

### Examining Data Transfer

- [aggregatePathReport](aggregatepathreport.md) — A report that sums counts across all network paths.
- [pathReports](pathreports.md) — An array of reports for each network path the connection used.
