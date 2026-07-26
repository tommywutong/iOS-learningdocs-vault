---
title: NWProtocolIP.Options
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwprotocolip/options
source_url: 'https://developer.apple.com/documentation/network/nwprotocolip/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolip/options.json'
content_hash: 'sha256:1aa4bbfc7de82945'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolIP](../nwprotocolip.md)

# NWProtocolIP.Options

<sub>Class</sub>

A container of options for configuring how IP is used on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Options
```

## Relationships

- **Inherits From**: [NWProtocolOptions](../nwprotocoloptions.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Selecting an IP Version

- [version](options/version-swift.property.md) — A required IP version that disables all other versions for a connection.
- [Version](options/version-swift.enum.md) — IP versions to require on connections and listeners.

### Customizing IP Behavior

- [shouldCalculateReceiveTime](options/shouldcalculatereceivetime.md) — A Boolean that indicates whether a connection delivers receive timestamps for IP packets.
- [hopLimit](options/hoplimit.md) — The default hop limit for packets a connection generates.
- [useMinimumMTU](options/useminimummtu.md) — A Boolean indicating that the connection uses the  minimum MTU value, which is 1280 bytes for IPv6.
- [disableFragmentation](options/disablefragmentation.md) — A Boolean that indicates whether fragmentation is disabled on outbound packets.

### Instance Properties

- [disableMulticastLoopback](options/disablemulticastloopback.md)
- [localAddressPreference](options/localaddresspreference.md)

### Enumerations

- [AddressPreference](options/addresspreference.md)

## See Also

### Configuring IP Connections

- [definition](definition.md) — The system definition of the Internet Protocol.
