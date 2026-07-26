---
title: NetServiceDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/netservicedelegate
source_url: 'https://developer.apple.com/documentation/foundation/netservicedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservicedelegate.json'
content_hash: 'sha256:4d25504c441c78f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NetServiceDelegate

<sub>Protocol</sub>

The interface a net service uses to inform its delegate about the state of the service it offers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol NetServiceDelegate : NSObjectProtocol
```

## Overview

The [NetServiceDelegate](netservicedelegate.md) protocol defines the optional methods implemented by delegates of [NetService](netservice.md) objects.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Using Network Services

- [- netServiceWillPublish:](<netservicedelegate/netservicewillpublish(__).md>) — Notifies the delegate that the network is ready to publish the service.
- [- netService:didNotPublish:](<netservicedelegate/netservice(__didnotpublish_).md>) — Notifies the delegate that a service could not be published.
- [- netServiceDidPublish:](<netservicedelegate/netservicedidpublish(__).md>) — Notifies the delegate that a service was successfully published.
- [- netServiceWillResolve:](<netservicedelegate/netservicewillresolve(__).md>) — Notifies the delegate that the network is ready to resolve the service.
- [- netService:didNotResolve:](<netservicedelegate/netservice(__didnotresolve_).md>) — Informs the delegate that an error occurred during resolution of a given service.
- [- netServiceDidResolveAddress:](<netservicedelegate/netservicedidresolveaddress(__).md>) — Informs the delegate that the address for a given service was resolved.
- [- netService:didUpdateTXTRecordData:](<netservicedelegate/netservice(__didupdatetxtrecord_).md>) — Notifies the delegate that the TXT record for a given service has been updated.
- [- netServiceDidStop:](<netservicedelegate/netservicedidstop(__).md>) — Informs the delegate that a [- publish](<netservice/publish().md>) or [- resolveWithTimeout:](<netservice/resolve(withtimeout_).md>) request was stopped.

### Accepting Connections

- [- netService:didAcceptConnectionWithInputStream:outputStream:](<netservicedelegate/netservice(__didacceptconnectionwith_outputstream_).md>) — Called when a client connects to a service managed by Bonjour.

## See Also

### Local Network Services

- [NetService](netservice.md) — A network service that broadcasts its availability using multicast DNS. _(deprecated)_
- [NSBonjourServices](../bundleresources/information-property-list/nsbonjourservices.md) — Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../bundleresources/information-property-list/nslocalnetworkusagedescription.md) — A message that tells people why the app is requesting access to the local network.
