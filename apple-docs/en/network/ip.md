---
title: IP
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/ip
source_url: 'https://developer.apple.com/documentation/network/ip'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/ip.json'
content_hash: 'sha256:7a785d112e01e3c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# IP

<sub>Structure</sub>

The system definition of the Internet Protocol (IP).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IP
```

## Overview

Can be used to insert IP into a protocol stack.

> [!note] Note
> Specifying IP is optional, and need only be included in a protocol stack when configuring IP options.

## Relationships

- **Conforms To**: [NetworkProtocolOptions](networkprotocoloptions.md)

## Topics

### Initializers

- [init()](<ip/init().md>)

### Instance Methods

- [fragmentationDisabled(_:)](<ip/fragmentationdisabled(__).md>) — Configure IP to disable fragmentation on outgoing packets.
- [hopLimit(_:)](<ip/hoplimit(__).md>) — Configure the IP hop limit.
- [localAddressPreference(_:)](<ip/localaddresspreference(__).md>)
- [minimumMTU(_:)](<ip/minimummtu(__).md>) — Configure IP to use the minimum MTU value.
- [multicastLoopbackDisabled(_:)](<ip/multicastloopbackdisabled(__).md>) — Specify if multicast packets should be looped back for local delivery.
- [receiveTimeCalculated(_:)](<ip/receivetimecalculated(__).md>) — Configure IP to calculate receive time for inbound packets.
- [version(_:)](<ip/version(__).md>)
