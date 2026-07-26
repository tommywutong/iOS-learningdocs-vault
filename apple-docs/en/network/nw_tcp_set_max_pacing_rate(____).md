---
title: 'nw_tcp_set_max_pacing_rate(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/network/nw_tcp_set_max_pacing_rate(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_tcp_set_max_pacing_rate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_tcp_set_max_pacing_rate%28_%3A_%3A%29.json'
content_hash: 'sha256:073448b00ead6ba4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_tcp_set_max_pacing_rate(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_tcp_set_max_pacing_rate(_ metadata: nw_protocol_metadata_t, _ max_pacing_rate: UInt64) -> Int32
```

## Parameters

- `metadata` — A TCP protocol metadata object from an established connection (e.g. obtained via nw_connection_access_established_protocol_metadata).

- `max_pacing_rate` — Maximum pacing rate in bytes per second. 0 or UINT64_MAX disables pacing on this connection.

## Return Value

Returns 0 on success, or a POSIX errno value on failure (e.g. EINVAL if metadata is not a TCP metadata object, or the underlying socket error).

## Discussion

Set a maximum pacing rate for a TCP connection, in bytes per second.

TCP pacing spreads outgoing packet transmission across time to avoid bursts and reduce queueing in the network. With a cap in place, the on-wire rate is the minimum of (a) this cap, and (b) the rate computed from the congestion window divided by smoothed RTT. The cap therefore never raises throughput above what congestion control would otherwise allow.

```
A value of 0 or UINT64_MAX disables pacing on this connection — the
connection sends without pacing (subject only to congestion control).

Rates in the open interval (0, 12500) are silently clamped up to
12500 bytes/second (100 Kbps). Callers needing genuinely sub-100-Kbps
pacing must shape at the application layer.

The cap may be updated at any time during the lifetime of an
established connection. Each call replaces the prior value.
```
