---
title: rawValue
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ipaddress/rawvalue
source_url: 'https://developer.apple.com/documentation/network/ipaddress/rawvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ipaddress/rawvalue.json'
content_hash: 'sha256:2a7e6e01dcbca7c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [IPAddress](../ipaddress.md)

# rawValue

<sub>Instance Property</sub>

The raw data of an IP address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var rawValue: Data { get }
```

## See Also

### Inspecting Address Properties

- [interface](interface.md) — The interface associated with this address, such as the IPv6 scoped interface.
- [isLinkLocal](islinklocal.md) — A Boolean indicating whether this address is in a link-local range.
- [isLoopback](isloopback.md) — A Boolean indicating whether this address is a loopback address for the local device.
- [isMulticast](ismulticast.md) — A Boolean indicating whether this address is a multicast address.
