---
title: NWPath
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpath
source_url: 'https://developer.apple.com/documentation/network/nwpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath.json'
content_hash: 'sha256:3c7b25d38b5bfba0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWPath

<sub>Structure</sub>

An object that contains information about the properties of the network that a connection uses, or that are available to your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NWPath
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Checking Path Availability

- [status](nwpath/status-swift.property.md) — A status indicating whether a path can be used by connections.
- [Status](nwpath/status-swift.enum.md) — Status values indicating whether a path can be used by connections.

### Inspecting Interfaces

- [usesInterfaceType(_:)](<nwpath/usesinterfacetype(__).md>) — Checks if connections using the path may send traffic over a specific interface type.
- [availableInterfaces](nwpath/availableinterfaces.md) — A list of all interfaces available to the path, in order of preference.
- [gateways](nwpath/gateways.md) — A list of gateways configured on the interfaces available to a path.

### Checking Path Capabilities

- [supportsIPv4](nwpath/supportsipv4.md) — A Boolean indicating whether the path can route IPv4 traffic.
- [supportsIPv6](nwpath/supportsipv6.md) — A Boolean indicating whether the path can route IPv6 traffic.
- [supportsDNS](nwpath/supportsdns.md) — A Boolean indicating whether the path has a DNS server configured.
- [isConstrained](nwpath/isconstrained.md) — A Boolean indicating whether the path uses an interface in Low Data Mode.
- [isExpensive](nwpath/isexpensive.md) — A Boolean indicating whether the path uses an interface that is considered expensive, such as Cellular or a Personal Hotspot.

### Inspecting Connected Paths

- [localEndpoint](nwpath/localendpoint.md) — The local endpoint in use by a connection’s network path.
- [remoteEndpoint](nwpath/remoteendpoint.md) — The remote endpoint in use by a connection’s network path.

### Instance Properties

- [isUltraConstrained](nwpath/isultraconstrained.md) — Checks if the path uses an NWInterface that is considered to be constrained by user preference
- [linkQuality](nwpath/linkquality-swift.property.md) — Represents the link quality measurement of the link layer network attachment
- [unsatisfiedReason](nwpath/unsatisfiedreason-swift.property.md)
- [wifiAware](nwpath/wifiaware.md) — Current status and performance information for Wi-Fi Aware, or `nil` if this path is not over Wi-Fi Aware.

### Enumerations

- [LinkQuality](nwpath/linkquality-swift.enum.md) — Represents the link quality measurement of the link layer network attachment
- [UnsatisfiedReason](nwpath/unsatisfiedreason-swift.enum.md)

## See Also

### Paths and Interfaces

- [NWPathMonitor](nwpathmonitor.md) — An observer that you use to monitor and react to network changes.
- [NWInterface](nwinterface.md) — An interface that a network connection uses to send and receive data.
