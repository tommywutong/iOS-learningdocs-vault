---
title: retransmittedTransportByteCount
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/datatransferreport/pathreport/retransmittedtransportbytecount
source_url: 'https://developer.apple.com/documentation/network/nwconnection/datatransferreport/pathreport/retransmittedtransportbytecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/datatransferreport/pathreport/retransmittedtransportbytecount.json'
content_hash: 'sha256:adfb5b389d3de518'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWConnection](../../../nwconnection.md) · [DataTransferReport](../../datatransferreport.md) · [PathReport](../pathreport.md)

# retransmittedTransportByteCount

<sub>Instance Property</sub>

The number of bytes the transport protocol retransmitted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let retransmittedTransportByteCount: UInt64
```

## See Also

### Inspecting Transport Metrics

- [receivedTransportByteCount](receivedtransportbytecount.md) — The number of bytes the transport protocol delivered.
- [receivedTransportDuplicateByteCount](receivedtransportduplicatebytecount.md) — The number of duplicated bytes the transport protocol detected.
- [receivedTransportOutOfOrderByteCount](receivedtransportoutoforderbytecount.md) — The number of bytes the transport protocol received out of order.
- [sentTransportByteCount](senttransportbytecount.md) — The number of bytes sent into the transport protocol.
- [transportSmoothedRTT](transportsmoothedrtt.md) — The smoothed round-trip time the transport protocol measured.
- [transportMinimumRTT](transportminimumrtt.md) — The minimum round-trip time the transport protocol measured.
- [transportRTTVariance](transportrttvariance.md) — The variance of the round-trip time the transport protocol measured.
