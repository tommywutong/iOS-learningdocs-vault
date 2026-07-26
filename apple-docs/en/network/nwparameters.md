---
title: NWParameters
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters
source_url: 'https://developer.apple.com/documentation/network/nwparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters.json'
content_hash: 'sha256:b40a37adf2771308'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWParameters

<sub>Class</sub>

An object that stores the protocols to use for connections, options for sending data, and network path constraints.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class NWParameters
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Escapable](../swift/escapable.md), [NWParametersProvider](nwparametersprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Parameters

- [tls](nwparameters/tls.md) — A set of default parameters for connections and listeners that use TLS and TCP.
- [tcp](nwparameters/tcp.md) — A set of default parameters for connections and listeners that use TCP.
- [dtls](nwparameters/dtls.md) — A set of default parameters for connections and listeners that use DTLS and UDP.
- [udp](nwparameters/udp.md) — A set of default parameters for connections and listeners that use UDP.
- [quic(alpn:)](<nwparameters/quic(alpn_).md>) — Returns a set of default parameters for connections and listeners that use QUIC, with a set of supported Application-Layer Protocol Negotiation values.
- [quicDatagram(alpn:)](<nwparameters/quicdatagram(alpn_).md>) — Returns a set of default parameters for connections and listeners that use QUIC datagrams, with a set of supported Application-Layer Protocol Negotiation values.
- [init(tls:tcp:)](<nwparameters/init(tls_tcp_).md>) — Initializes parameters for TLS connections and listeners with custom TLS and TCP options.
- [init(dtls:udp:)](<nwparameters/init(dtls_udp_).md>) — Initializes parameters for DTLS connections and listeners with custom DTLS and UDP options.
- [init(quic:)](<nwparameters/init(quic_).md>) — Initializes parameters for QUIC connections and listeners with custom QUIC options.
- [init()](<nwparameters/init().md>) — Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [init(customIPProtocolNumber:)](<nwparameters/init(customipprotocolnumber_).md>) — Initializes parameters for connections and listeners using a custom IP protocol.
- [copy()](<nwparameters/copy().md>) — Performs a deep copy of a parameters object.

### Modifying Protocol Stacks

- [defaultProtocolStack](nwparameters/defaultprotocolstack.md) — The protocol stack used by connections and listeners.
- [ProtocolStack](nwparameters/protocolstack.md) — An ordered set of protocol options that define the protocols that connections and listeners use.
- [NWProtocol](nwprotocol.md) — The abstract superclass used by Network framework protocols and by custom network protocols that you define.

### Selecting Paths

- [requiredInterfaceType](nwparameters/requiredinterfacetype.md) — An interface type to require on connections and listeners.
- [requiredInterface](nwparameters/requiredinterface.md) — A specific interface to require on connections, listeners, and browsers.
- [requiredLocalEndpoint](nwparameters/requiredlocalendpoint.md) — A specific local IP address and port to use for connections and listeners.
- [prohibitConstrainedPaths](nwparameters/prohibitconstrainedpaths.md) — A Boolean that prevents connections, listeners, and browsers from using network paths marked as constrained by Low Data Mode.
- [prohibitExpensivePaths](nwparameters/prohibitexpensivepaths.md) — A Boolean that prevents connections, listeners, and browsers from using network paths marked as expensive.
- [prohibitedInterfaceTypes](nwparameters/prohibitedinterfacetypes.md) — A list of interface types that connections, listeners, and browsers will not use.
- [prohibitedInterfaces](nwparameters/prohibitedinterfaces.md) — A list of specific interfaces that connections and listeners will not use.

### Customizing Connection Options

- [multipathServiceType](nwparameters/multipathservicetype-swift.property.md) — An option to allow connections to use multipath protocols.
- [MultipathServiceType](nwparameters/multipathservicetype-swift.enum.md) — Modes in which a connection can support multipath protocols.
- [serviceClass](nwparameters/serviceclass-swift.property.md) — The traffic characteristics network connections send and receive.
- [ServiceClass](nwparameters/serviceclass-swift.enum.md) — Indicates how the system prioritizes transmitted traffic by your latency and throughput needs.
- [allowFastOpen](nwparameters/allowfastopen.md) — A Boolean that enables sending application data with protocol handshakes.
- [expiredDNSBehavior](nwparameters/expireddnsbehavior-swift.property.md) — A behavior that defines how expired DNS answers will be used.
- [ExpiredDNSBehavior](nwparameters/expireddnsbehavior-swift.enum.md) — Options for configuring how expired DNS answers should be used.
- [requiresDNSSECValidation](nwparameters/requiresdnssecvalidation.md) — A Boolean value that determines whether a connection requires DNSSEC validation when resolving endpoints.
- [preferNoProxies](nwparameters/prefernoproxies.md) — A Boolean that indicates that connections should ignore proxies when they are enabled on the system.
- [includePeerToPeer](nwparameters/includepeertopeer.md) — A Boolean that enables peer-to-peer link technologies for connections and listeners.
- [allowLocalEndpointReuse](nwparameters/allowlocalendpointreuse.md) — A Boolean that allows reusing local addresses and ports across connections.
- [acceptLocalOnly](nwparameters/acceptlocalonly.md) — A Boolean that restricts listeners to only accepting connections from the local link.

### Configuring Privacy Settings

- [setPrivacyContext(_:)](<nwparameters/setprivacycontext(__).md>) — Associates a privacy context with any connections or listeners that use the parameters.
- [PrivacyContext](nwparameters/privacycontext.md) — An object that defines the privacy requirements for a set of connections.

### Instance Properties

- [allowUltraConstrainedPaths](nwparameters/allowultraconstrainedpaths.md) — Allow connection to use interfaces considered ultra-constrained by the system
- [attribution](nwparameters/attribution-swift.property.md)
- [wifiAware](nwparameters/wifiaware.md) — Get and set Wi-Fi Aware specific connection parameters.

### Instance Methods

- [wifiAware(_:)](<nwparameters/wifiaware(__).md>) — Configure Wi-Fi Aware properties on an `NWParameters` object.

### Type Properties

- [applicationService](nwparameters/applicationservice.md) — The default parameters for connecting with other, local devices that are running your app.

### Enumerations

- [Attribution](nwparameters/attribution-swift.enum.md)

## See Also

### Essentials

- [NWEndpoint](nwendpoint.md) — A local or remote endpoint in a network connection.
