---
title: listenForConnections
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/netservice/options/listenforconnections
source_url: 'https://developer.apple.com/documentation/foundation/netservice/options/listenforconnections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/netservice/options/listenforconnections.json'
content_hash: 'sha256:d6087c43bebadd04'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NetService](../../netservice.md) · [Options](../options.md)

# listenForConnections

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var listenForConnections: NetService.Options { get }
```

## Discussion

Specifies that a TCP listener should be started for both IPv4 and IPv6 on the port specified by this service. If the listening port can’t be opened, the service calls its delegate’s [- netService:didNotPublish:](<../../netservicedelegate/netservice(__didnotpublish_).md>) method to report the error.

The listener supports only TCP connections. If the service’s type does not end with `_tcp`, publication fails with [NSNetServicesBadArgumentError](../errorcode-swift.enum/badargumenterror.md).

Whenever a client connects to the listening socket, the service calls its delegate’s [- netService:didAcceptConnectionWithInputStream:outputStream:](<../../netservicedelegate/netservice(__didacceptconnectionwith_outputstream_).md>) method with a pair of `NSStream` objects.

## See Also

### Constants

- [NSNetServiceNoAutoRename](noautorename.md) — Specifies that the network service should not rename itself in the event of a name collision.
