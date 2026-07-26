---
title: 'peerToPeerIncluded(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/peertopeerincluded(_:)-60331'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/peertopeerincluded(_:)-60331'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/peertopeerincluded%28_%3A%29-60331.json'
content_hash: 'sha256:b98764c264cf473c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# peerToPeerIncluded(_:)

<sub>Instance Method</sub>

Include peer-to-peer interfaces when connecting, listening, and browsing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func peerToPeerIncluded(_ included: Bool) -> Self
```

## Parameters

- `included` — True if peer-to-peer interfaces should be included, false otherwise.

## Discussion

> [!important] Important
> Connections, Listeners, and Browsers using peer-to-peer interfaces can consume significantly more power and should not be kept running for longer than necessary.
>
> Peer-to-peer link technologies can be power-intensive. If a connection or listener with this flag enabled remains idle for an extended period, the system may return a `kDNSServiceErr_AWDLTimeout` error, transitioning it to a failed state that yields no further results. Any retry mechanism should implement exponential backoff or similar rate-limiting to avoid prolonged power drain.

This will not take effect if a specific interface is required. Applicable when advertising a Bonjour service on a listener, or connecting to a Bonjour service.
