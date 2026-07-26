---
title: Building a custom peer-to-peer protocol
framework: Network
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, watchOS 9.0+, Xcode 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/building-a-custom-peer-to-peer-protocol
source_url: 'https://developer.apple.com/documentation/network/building-a-custom-peer-to-peer-protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/building-a-custom-peer-to-peer-protocol.json'
content_hash: 'sha256:2c5971b293ab9d14'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# Building a custom peer-to-peer protocol

<sub>Sample Code</sub>

Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.

## Overview

This TicTacToe sample code project creates a networked game that you can play between different devices, communicating with a custom protocol. The game offers two ways to play:

- On Apple TV, the game uses [DeviceDiscoveryUI](../devicediscoveryui.md) to discover nearby iOS, iPadOS, and watchOS devices. After connecting, you can use your device to play against an AI opponent on Apple TV.
- On iOS and iPadOS devices, the game uses Bonjour and TLS to establish secure connections between nearby devices. You can use this mode to play a peer-to-peer two-player game.

> [!note] Note
> This sample code project is associated with WWDC22 session [110339: Build device-to-device interactions with the Network framework](https://developer.apple.com/wwdc22/110339/). It’s also associated with WWDC 2020 session [10110: Support local network privacy in your app](https://developer.apple.com/wwdc20/10110/) and with WWDC 2019 session [713: Advances in Networking, Part 2](https://developer.apple.com/wwdc19/713/).

## See Also

### Network Protocols

- [Connecting iPadOS and visionOS apps over the local network](../visionos/connecting-ipados-and-visionos-apps-over-the-local-network.md) — Build an iPadOS companion app to control your visionOS app.
- [NWProtocolTCP](nwprotocoltcp.md) — A network protocol for connections that use the Transmission Control Protocol.
- [NWProtocolTLS](nwprotocoltls.md) — A network protocol for connections that use Transport Layer Security.
- [NWProtocolQUIC](nwprotocolquic.md) — A network protocol for connections that use the QUIC transport protocol.
- [NWProtocolUDP](nwprotocoludp.md) — A network protocol for connections that use the User Datagram Protocol.
- [NWProtocolIP](nwprotocolip.md) — A network protocol for configuring the Internet Protocol on connections.
- [NWProtocolWebSocket](nwprotocolwebsocket.md) — A network protocol for connections that use WebSocket.
- [NWProtocolFramer](nwprotocolframer.md) — A customizable network protocol for defining application message parsers.

## Download

- [BuildingACustomPeerToPeerProtocol.zip](https://docs-assets.developer.apple.com/published/b9d884834905/BuildingACustomPeerToPeerProtocol.zip)
