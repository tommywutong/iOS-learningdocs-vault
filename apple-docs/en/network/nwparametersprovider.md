---
title: NWParametersProvider
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparametersprovider
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider.json'
content_hash: 'sha256:e294340c2e683afe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWParametersProvider

<sub>Protocol</sub>

Types that conform to the NWParametersProvider protocol can be used to generate an NWParameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NWParametersProvider
```

## Relationships

- **Conforming Types**: [NWParameters](nwparameters.md), [NWParametersBuilder](nwparametersbuilder.md)

## Topics

### Instance Properties

- [parameters](nwparametersprovider/parameters.md) — The generated NWParameters.

### Instance Methods

- [constrainedPathsProhibited(_:)](<nwparametersprovider/constrainedpathsprohibited(__).md>) — Prohibit using constrained paths.
- [dnssecValidationRequired(_:)](<nwparametersprovider/dnssecvalidationrequired(__).md>) — Require DNSSEC validation when resolving an endpoint before making a connection.
- [expensivePathsProhibited(_:)](<nwparametersprovider/expensivepathsprohibited(__).md>) — Prohibit using expensive paths.
- [expiredDNSBehavior(_:)](<nwparametersprovider/expireddnsbehavior(__).md>) — Allow or prohibit the use of expired DNS answers during connection establishment.
- [fastOpenAllowed(_:)](<nwparametersprovider/fastopenallowed(__).md>) — Allow fast open to be used on a connection.
- [localEndpoint(_:)](<nwparametersprovider/localendpoint(__).md>) — Specify a specific endpoint to use as the local endpoint.
- [localEndpointReuseAllowed(_:)](<nwparametersprovider/localendpointreuseallowed(__).md>) — Allow local endpoint reuse.
- [localOnly(_:)](<nwparametersprovider/localonly(__).md>) — Limit inbound connections to peers attached to the local link.
- [localPort(_:)](<nwparametersprovider/localport(__).md>) — Specify a specific port to use as the local endpoint, letting the system select the address.
- [multipathServiceType(_:)](<nwparametersprovider/multipathservicetype(__).md>) — Set the multipath service to use for connections.
- [noProxiesPreferred(_:)](<nwparametersprovider/noproxiespreferred(__).md>) — Prefer not using proxies when making connections.
- [peerToPeerIncluded(_:)](<nwparametersprovider/peertopeerincluded(__).md>) — Include peer-to-peer interfaces when connecting, listening, and browsing.
- [prohibitedInterfaceTypes(_:)](<nwparametersprovider/prohibitedinterfacetypes(__).md>) — Prohibit certain interface types from being used to connect, listen, and browse.
- [prohibitedInterfaces(_:)](<nwparametersprovider/prohibitedinterfaces(__).md>) — Prohibit certain interfaces from being used to connect, listen, and browse.
- [requiredInterface(_:)](<nwparametersprovider/requiredinterface(__).md>) — Require an interface when connecting, listening, and browsing.
- [requiredInterfaceType(_:)](<nwparametersprovider/requiredinterfacetype(__).md>) — Require an interface type when connecting, listening, and browsing.
- [serviceClass(_:)](<nwparametersprovider/serviceclass(__).md>) — Set the data service class to use for connections.
- [ultraConstrainedPathsAllowed(_:)](<nwparametersprovider/ultraconstrainedpathsallowed(__).md>) — Allow connection to use interfaces considered ultra-constrained by the system
