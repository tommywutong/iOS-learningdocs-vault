---
title: 'setMaximumPacingRateBytesPerSecond(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/network/nwprotocoltcp/metadata/setmaximumpacingratebytespersecond(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocoltcp/metadata/setmaximumpacingratebytespersecond(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocoltcp/metadata/setmaximumpacingratebytespersecond%28_%3A%29.json'
content_hash: 'sha256:d07865af7fa1ce37'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolTCP](../../nwprotocoltcp.md) · [Metadata](../metadata.md)

# setMaximumPacingRateBytesPerSecond(_:)

<sub>Instance Method</sub>

Set the maximum pacing rate for this TCP connection, in bytes per second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setMaximumPacingRateBytesPerSecond(_ maximumPacingRateBytesPerSecond: UInt64?)
```

## Parameters

- `maximumPacingRateBytesPerSecond` — Maximum pacing rate in bytes per second, or `nil` to disable pacing.

## Discussion

TCP pacing spreads out packet transmission to avoid bursts and reduce network congestion. The actual on-wire rate is the minimum of this cap and the rate computed from the congestion window and RTT, so this value never increases throughput above what congestion control allows.

Pass `nil` to disable pacing on this connection — the connection will send without pacing (subject only to congestion control).
