---
title: Network
framework: Network
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network
source_url: 'https://developer.apple.com/documentation/network'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network.json'
content_hash: 'sha256:394ee903e429da62'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Network

<sub>Framework</sub>

Create network connections to send and receive data using transport and security protocols.

## Overview

Use this framework when you need direct access to protocols like TLS, TCP, and UDP for your custom application protocols. Continue to use [URLSession](foundation/urlsession.md), which is built upon this framework, for loading HTTP- and URL-based resources. For in-depth advice on where to start with networking, see [TN3151: Choosing the right networking API](technotes/tn3151-choosing-the-right-networking-api.md).

> [!note] Note
> watchOS supports Network framework for specific use cases. For more details, see [TN3135: Low-level networking on watchOS](technotes/tn3135-low-level-networking-on-watchos.md).

## Topics

### Essentials

- [NWEndpoint](network/nwendpoint.md) — A local or remote endpoint in a network connection.
- [NWParameters](network/nwparameters.md) — An object that stores the protocols to use for connections, options for sending data, and network path constraints.

### Connections and Listeners

- [NWConnection](network/nwconnection.md) — A bidirectional data connection between a local endpoint and a remote endpoint.
- [NWListener](network/nwlistener.md) — An object you use to listen for incoming network connections.
- [NWBrowser](network/nwbrowser.md) — An object you use to browse for available network services.
- [NWConnectionGroup](network/nwconnectiongroup.md) — An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [NWEthernetChannel](network/nwethernetchannel.md) — An object you use to send and receive custom Ethernet frames.

### Network Protocols

- [Building a custom peer-to-peer protocol](network/building-a-custom-peer-to-peer-protocol.md) — Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.
- [Connecting iPadOS and visionOS apps over the local network](visionos/connecting-ipados-and-visionos-apps-over-the-local-network.md) — Build an iPadOS companion app to control your visionOS app.
- [NWProtocolTCP](network/nwprotocoltcp.md) — A network protocol for connections that use the Transmission Control Protocol.
- [NWProtocolTLS](network/nwprotocoltls.md) — A network protocol for connections that use Transport Layer Security.
- [NWProtocolQUIC](network/nwprotocolquic.md) — A network protocol for connections that use the QUIC transport protocol.
- [NWProtocolUDP](network/nwprotocoludp.md) — A network protocol for connections that use the User Datagram Protocol.
- [NWProtocolIP](network/nwprotocolip.md) — A network protocol for configuring the Internet Protocol on connections.
- [NWProtocolWebSocket](network/nwprotocolwebsocket.md) — A network protocol for connections that use WebSocket.
- [NWProtocolFramer](network/nwprotocolframer.md) — A customizable network protocol for defining application message parsers.

### Network Security and Privacy

- [Security Options](network/security-options.md) — Configure security options for TLS handshakes.
- [Privacy Management](network/privacy-management.md) — Configure parameters related to user privacy.
- [Creating an Identity for Local Network TLS](network/creating-an-identity-for-local-network-tls.md) — Learn how to create and use a digital identity in your application for local network TLS.

### Paths and Interfaces

- [NWPath](network/nwpath.md) — An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [NWPathMonitor](network/nwpathmonitor.md) — An observer that you use to monitor and react to network changes.
- [NWInterface](network/nwinterface.md) — An interface that a network connection uses to send and receive data.

### Errors

- [NWError](network/nwerror.md) — The errors returned by objects in the Network framework.

### Network Debugging

- [Choosing a Network Debugging Tool](network/choosing-a-network-debugging-tool.md) — Decide which tool works best for your network debugging problem.
- [Debugging HTTP Server-Side Errors](network/debugging-http-server-side-errors.md) — Understand HTTP server-side errors and how to debug them.
- [Debugging HTTPS Problems with CFNetwork Diagnostic Logging](network/debugging-https-problems-with-cfnetwork-diagnostic-logging.md) — Use CFNetwork diagnostic logging to investigate HTTP and HTTPS problems.
- [Recording a Packet Trace](network/recording-a-packet-trace.md) — Learn how to record a low-level trace of network traffic.
- [Taking Advantage of Third-Party Network Debugging Tools](network/taking-advantage-of-third-party-network-debugging-tools.md) — Learn about the available third-party network debugging tools.
- [Testing and Debugging L4S in Your App](network/testing-and-debugging-l4s-in-your-app.md) — Learn how to verify your app on an L4S-capable host and network to improve your app’s responsiveness.

### C-Language Symbols

- [C-Language Symbols](network/c-language-symbols.md)

### Structures

- [nw_interface_radio_type_t](network/nw_interface_radio_type_t.md)
- [nw_multipath_version_t](network/nw_multipath_version_t.md)
- [nw_path_unsatisfied_reason_t](network/nw_path_unsatisfied_reason_t.md)
- [nw_quic_stream_type_t](network/nw_quic_stream_type_t.md)
- [Bonjour](network/bonjour.md) — A browser that discovers Bonjour services.
- [BonjourListenerProvider](network/bonjourlistenerprovider.md) — Advertise a Bonjour service.
- [Coder](network/coder.md) — A protocol that frames and encodes/decodes Codable types.
- [DTLS](network/dtls.md) — The system definition of the Datagram Transport Layer Security (DTLS) protocol. _(beta)_
- [DefaultProtocolStorage](network/defaultprotocolstorage.md)
- [Framer](network/framer.md) — An instance of a Framer protocol to load into a protocol stack.
- [IP](network/ip.md) — The system definition of the Internet Protocol (IP).
- [NWParametersBuilder](network/nwparametersbuilder.md) — An opaque class that is responsible for creating and configuring NWParameters based on the parameterized protocol stack.
- [NWTXTRecord](network/nwtxtrecord.md) — A dictionary representing a TXT record in a DNS packet.
- [NetworkJSONCoder](network/networkjsoncoder.md)
- [NetworkPropertyListCoder](network/networkpropertylistcoder.md)
- [ProtocolMetadataBuilder](network/protocolmetadatabuilder.md) — A resultBuilder for configuring metadata in send methods in a declarative way.
- [ProtocolStackBuilder](network/protocolstackbuilder.md) — A resultBuilder for specifying and configuring protocol stacks in a declarative way
- [ProxyConfiguration](network/proxyconfiguration.md) — A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.
- [QUIC](network/quic.md) — The system definition of the QUIC protocol.
- [QUICDatagram](network/quicdatagram.md) — Send and receive unreliable datagrams over QUIC via RFC 9221
- [QUICStream](network/quicstream.md) — A QUIC stream that runs over a QUIC connection.
- [TCP](network/tcp.md) — The system definition of the Transmission Control Protocol (TCP).
- [TLS](network/tls.md) — The system definition of the Transport Layer Security (TLS) protocol.
- [TLV](network/tlv.md) — A Type-Length-Value (TLV) framing protocol.
- [TXTRecordDecoder](network/txtrecorddecoder.md)
- [UDP](network/udp.md) — The system definition of the User Datagram Protocol (UDP).
- [UnexpectedEndpointType](network/unexpectedendpointtype.md) — An error generated when an unexpected endpoint type is supplied.
- [WebSocket](network/websocket.md) — The system definition of the WebSocket protocol.
- [nw_link_quality_t](network/nw_link_quality_t.md)

### Classes

- [NWMultiplexGroup](network/nwmultiplexgroup.md)
- [NetworkBrowser](network/networkbrowser.md) — Discover advertised services and devices on the network.
- [NetworkChannel](network/networkchannel.md) — A base class supporting sending and recieving data through an arbitrary network channel.
- [NetworkConnection](network/networkconnection.md) — Connect to an endpoint on the network to send and receive data.
- [NetworkListener](network/networklistener.md) — Listen for incoming network connections.

### Reference

- [Network Constants](network/network-constants.md) — Access Network framework constants used in C.
- [Network Functions](network/network-functions.md) — Access Network framework functions used in C.
- [Network Data Types](network/network-data-types.md)

### Protocols

- [BrowserProvider](network/browserprovider.md) — BrowserProviders can be used when creating NetworkBrowsers.
- [Connectable](network/connectable.md) — Describes types that can be used to make NetworkConnections.
- [ConnectionStorage](network/connectionstorage.md) — Types that conform to ConnectionStorage can be used as additional storage within a connection.
- [DatagramProtocol](network/datagramprotocol.md) — Types that conform to DatagramProtocol send and receive messages with minimal or no metadata, usually constrained to a fixed maximum size.
- [FramerProtocol](network/framerprotocol.md) — Framer protocols allow custom framing and serialization of messages on a connection.
- [ListenerProvider](network/listenerprovider.md) — Extensible support for configuring advertise descriptors to define the service a listener should advertise.
- [MessageProtocol](network/messageprotocol.md) — Types that conform to MessageProtocol send and receive messages. The conforming type is responsible for specifying its message-specific metadata.
- [MultiplexProtocol](network/multiplexprotocol.md) — Types that conform to MultiplexProtocol are allowed to be the top protocol in a network protocol stack for multiplexing network connection objects.
- [NWParametersProvider](network/nwparametersprovider.md) — Types that conform to the NWParametersProvider protocol can be used to generate an NWParameters.
- [NetworkCoder](network/networkcoder.md)
- [NetworkDecoder](network/networkdecoder.md) — A type that conforms to the NetworkEncoder protocol can decode data to an Encodable object
- [NetworkEncoder](network/networkencoder.md) — A type that conforms to the NetworkEncoder protocol can encode a Encodable object to Data
- [NetworkFixedWidthInteger](network/networkfixedwidthinteger.md)
- [NetworkMetadataProtocol](network/networkmetadataprotocol.md) — Types that conform to NetworkProtocolOptions can be used when configuring protocol stacks.
- [NetworkProtocolOptions](network/networkprotocoloptions.md)
- [OneToOneProtocol](network/onetooneprotocol.md) — Types that conform to OneToOneProtocol are allowed to be the top protocol in a network protocol stack for non-multiplexed connections.
- [StreamProtocol](network/streamprotocol.md) — Types that conform to the StreamProtocol protocol expose methods for sending and receiving byte streams.

### Variables

- [kNWErrorDomainWiFiAware](network/knwerrordomainwifiaware.md)
- [nw_error_domain_wifi_aware](network/nw_error_domain_wifi_aware.md)
- [nw_link_quality_good](network/nw_link_quality_good.md)
- [nw_link_quality_minimal](network/nw_link_quality_minimal.md)
- [nw_link_quality_moderate](network/nw_link_quality_moderate.md)
- [nw_link_quality_unknown](network/nw_link_quality_unknown.md)

### Functions

- [nw_parameters_get_allow_ultra_constrained](<network/nw_parameters_get_allow_ultra_constrained(__).md>)
- [nw_parameters_set_allow_ultra_constrained](<network/nw_parameters_set_allow_ultra_constrained(____).md>)
- [nw_path_get_link_quality](<network/nw_path_get_link_quality(__).md>)
- [nw_path_is_ultra_constrained](<network/nw_path_is_ultra_constrained(__).md>)
- [nw_tcp_set_max_pacing_rate](<network/nw_tcp_set_max_pacing_rate(____).md>) _(beta)_
- [withNetworkConnection(to:using:_:)](<network/withnetworkconnection(to_using___)-1sik8.md>)
- [withNetworkConnection(to:using:_:)](<network/withnetworkconnection(to_using___)-4wpc9.md>)
- [withNetworkConnection(to:using:_:)](<network/withnetworkconnection(to_using___)-7skhi.md>)
- [withNetworkConnection(to:using:_:)](<network/withnetworkconnection(to_using___)-887ho.md>)
