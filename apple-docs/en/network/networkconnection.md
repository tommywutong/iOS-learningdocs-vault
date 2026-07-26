---
title: NetworkConnection
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkconnection
source_url: 'https://developer.apple.com/documentation/network/networkconnection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkconnection.json'
content_hash: 'sha256:b5882c6aa15364ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NetworkConnection

<sub>Class</sub>

Connect to an endpoint on the network to send and receive data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class NetworkConnection<ApplicationProtocol> where ApplicationProtocol : NetworkProtocolOptions
```

## Overview

A connection handles establishment of any transport, security, and application-level protocols required to transmit and receive user data. Connections may make multiple establishment attempts before the connection is ready.

## Relationships

- **Inherits From**: [NetworkChannel](networkchannel.md)

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(to:using:)](<networkconnection/init(to_using_)-182om.md>)
- [init(to:using:)](<networkconnection/init(to_using_)-51aq2.md>) — Create a new connection to an endpoint, with protocol stack.
- [init(to:using:)](<networkconnection/init(to_using_)-5e864.md>)
- [init(to:using:)](<networkconnection/init(to_using_)-69glf.md>)
- [init(to:using:)](<networkconnection/init(to_using_)-6yzx9.md>) — Create a new outbound connection to an endpoint, with parameters. The parameters determine the protocols to be used for the connection, and their options.
- [init(to:using:)](<networkconnection/init(to_using_)-7gprx.md>)
- [init(to:using:)](<networkconnection/init(to_using_)-907m0.md>)
- [init(to:using:)](<networkconnection/init(to_using_)-9kq3t.md>)

### Instance Properties

- [applicationError](networkconnection/applicationerror.md) — The QUIC application error code to send for the connection, or received from the peer.
- [currentPath](networkconnection/currentpath.md) — Current path for the connection, which can be used to extract interface and effective endpoint information
- [datagrams](networkconnection/datagrams.md) — Access connection-wide unreliable datagrams over QUIC. Subsequent accesses to this object will return the same reference. All incoming datagrams for the entire QUIC connection will be received on this `SubConnection` once invoked.
- [keepalive](networkconnection/keepalive.md) — Set the QUIC connection keepalive interval.
- [localEndpoint](networkconnection/localendpoint.md)
- [negotiatedALPN](networkconnection/negotiatedalpn.md) — Return the negotiated application protocol used when establishing the connection
- [remoteEndpoint](networkconnection/remoteendpoint.md)
- [remoteIdleTimeout](networkconnection/remoteidletimeout.md) — Access the idle_timeout value in milliseconds received from the peer in the transport parameters.
- [remoteMaxStreamsBidirectional](networkconnection/remotemaxstreamsbidirectional.md) — Get the maximum number of bidirectional streams advertised by peer that an application is allowed to create.
- [remoteMaxStreamsUnidirectional](networkconnection/remotemaxstreamsunidirectional.md) — Get the maximum number of unidirectional streams advertised by peer that an application is allowed to create.
- [securityProtocolMetadata](networkconnection/securityprotocolmetadata.md) — Access the sec_protocol_metadata_t for the QUIC Connection. See \<Security/SecProtocolMetadata.h\> for functions to further access security metadata.
- [usableDatagramFrameSize](networkconnection/usabledatagramframesize.md) — Get the usable size of a datagram frame from a QUIC datagram flow.
- [wifiAware](networkconnection/wifiaware.md) — Get the current connection information for Wi-Fi Aware if the connection is over Wi-Fi Aware, `nil` if it’s not over Wi-Fi Aware.

### Instance Methods

- [inboundStreams(_:)](<networkconnection/inboundstreams(__).md>) — Handle inbound streams and provide a closure on which callback handlers will be executed. When the `NetworkConnection<QUIC>` state moves to `ready`, the internal listener is registered with the system and can receive incoming streams on the multiplexing instance. `inboundStreams` should only be called once on a `NetworkConnection<QUIC>`, and multiple calls to run will throw an exception.
- [inboundStreams(prepending:_:)](<networkconnection/inboundstreams(prepending___).md>) — Handle inbound streams and provide a closure on which callback handlers will be executed. When the `NetworkConnection<QUIC>` state moves to `ready`, the internal listener is registered with the system and can receive incoming streams on the multiplexing instance. `inboundStreams` should only be called once on a `NetworkConnection<QUIC>`, and multiple calls to run will throw an exception.
- [onBetterPathUpdate(_:)](<networkconnection/onbetterpathupdate(__)-2h2wu.md>) — A better path being available indicates that the system thinks there is a preferred path or interface to use, compared to the one this connection is actively using. As an example, the connection is established over an expensive cellular interface and an unmetered Wi-Fi interface is now available. _(beta)_
- [onBetterPathUpdate(_:)](<networkconnection/onbetterpathupdate(__)-7b4ue.md>) — A better path being available indicates that the system thinks there is a preferred path or interface to use, compared to the one this connection is actively using. As an example, the connection is established over an expensive cellular interface and an unmetered Wi-Fi interface is now available.
- [onPathUpdate(_:)](<networkconnection/onpathupdate(__)-2uoc8.md>) — Set a closure to be called when the connection’s path has changed, which may be called multiple times until the connection is cancelled. _(beta)_
- [onPathUpdate(_:)](<networkconnection/onpathupdate(__)-6sn1s.md>) — Set a closure to be called when the connection’s path has changed, which may be called multiple times until the connection is cancelled.
- [onStateUpdate(_:)](<networkconnection/onstateupdate(__).md>) — Set a closure to be called when the connection’s state changes, which may be called multiple times until the connection is cancelled.
- [onViabilityUpdate(_:)](<networkconnection/onviabilityupdate(__)-13jwf.md>) — Set a closure to be called when the connection’s viability changes, which may be called multiple times until the connection is cancelled. _(beta)_
- [onViabilityUpdate(_:)](<networkconnection/onviabilityupdate(__)-70awf.md>) — Set a closure to be called when the connection’s viability changes, which may be called multiple times until the connection is cancelled.
- [openStream(directionality:)](<networkconnection/openstream(directionality_).md>) — Initiate a new data stream over QUIC. When invoked with no parameters, the default stream type will be bidirectional. Unidirectional streams can be initiated by setting the optional `bidirectional` parameter to false.
- [openStream(directionality:_:)](<networkconnection/openstream(directionality___).md>) — Initiate a new data stream over QUIC. When invoked with no parameters, the default stream type will be bidirectional. Unidirectional streams can be initiated by setting the optional `bidirectional` parameter to false.
- [start()](<networkconnection/start().md>) — Initiate some action to open the connection on the network like making a handshake, initiating a multiplexing session, etc. Starts the connection, which will cause the connection to evaluate its path, do resolution, and try to become ready (connected). `NetworkConnection` establishment is asynchronous. `onStateUpdate` will be called when the state changes. If the connection cannot be established, the state will transition to `waiting` with an associated error describing the reason. If an unrecoverable error is encountered, the state will transition to `failed` with an associated error value. If the connection is established, the state will transition to `ready`.
- [tryNextEndpoint()](<networkconnection/trynextendpoint().md>) — Cancel the currently connected endpoint, causing the connection to fall through to the next endpoint if available, or to go to the waiting state if no more endpoints are available.
