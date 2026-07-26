---
title: receivedTransportOutOfOrderByteCount
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/datatransferreport/pathreport/receivedtransportoutoforderbytecount
source_url: 'https://developer.apple.com/documentation/network/nwconnection/datatransferreport/pathreport/receivedtransportoutoforderbytecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/datatransferreport/pathreport/receivedtransportoutoforderbytecount.json'
content_hash: 'sha256:92b20d699f9f120a'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Network](../../../../network.md) · [NWConnection](../../../nwconnection.md) · [DataTransferReport](../../datatransferreport.md) · [PathReport](../pathreport.md)

# receivedTransportOutOfOrderByteCount

<sub>Instance Property</sub>

The number of bytes the transport protocol received out of order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let receivedTransportOutOfOrderByteCount: UInt64
```

## See Also

### Inspecting Transport Metrics

- [receivedTransportByteCount](receivedtransportbytecount.md) — The number of bytes the transport protocol delivered.
- [receivedTransportDuplicateByteCount](receivedtransportduplicatebytecount.md) — The number of duplicated bytes the transport protocol detected.
- [sentTransportByteCount](senttransportbytecount.md) — The number of bytes sent into the transport protocol.
- [retransmittedTransportByteCount](retransmittedtransportbytecount.md) — The number of bytes the transport protocol retransmitted.
- [transportSmoothedRTT](transportsmoothedrtt.md) — The smoothed round-trip time the transport protocol measured.
- [transportMinimumRTT](transportminimumrtt.md) — The minimum round-trip time the transport protocol measured.
- [transportRTTVariance](transportrttvariance.md) — The variance of the round-trip time the transport protocol measured.
