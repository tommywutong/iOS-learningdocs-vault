---
title: disableFragmentation
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolip/options/disablefragmentation
source_url: 'https://developer.apple.com/documentation/network/nwprotocolip/options/disablefragmentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolip/options/disablefragmentation.json'
content_hash: 'sha256:757dc88c471bf9ec'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolIP](../../nwprotocolip.md) · [Options](../options.md)

# disableFragmentation

<sub>Instance Property</sub>

A Boolean that indicates whether fragmentation is disabled on outbound packets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var disableFragmentation: Bool { get set }
```

## See Also

### Customizing IP Behavior

- [shouldCalculateReceiveTime](shouldcalculatereceivetime.md) — A Boolean that indicates whether a connection delivers receive timestamps for IP packets.
- [hopLimit](hoplimit.md) — The default hop limit for packets a connection generates.
- [useMinimumMTU](useminimummtu.md) — A Boolean indicating that the connection uses the  minimum MTU value, which is 1280 bytes for IPv6.
