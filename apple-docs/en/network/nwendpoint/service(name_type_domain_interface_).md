---
title: 'NWEndpoint.service(name:type:domain:interface:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwendpoint/service(name:type:domain:interface:)'
source_url: 'https://developer.apple.com/documentation/network/nwendpoint/service(name:type:domain:interface:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwendpoint/service%28name%3Atype%3Adomain%3Ainterface%3A%29.json'
content_hash: 'sha256:d3ef3957dc71f743'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEndpoint](../nwendpoint.md)

# NWEndpoint.service(name:type:domain:interface:)

<sub>Case</sub>

An endpoint represented as a Bonjour service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case service(name: String, type: String, domain: String, interface: NWInterface?)
```

## See Also

### Endpoint Types

- [NWEndpoint.hostPort(host:port:)](<hostport(host_port_).md>) — An endpoint represented as a host and port, with the host including both names and addresses.
- [NWEndpoint.url(_:)](<url(__).md>) — An endpoint represented as a URL, with host and port values inferred from the URL.
- [NWEndpoint.unix(path:)](<unix(path_).md>) — An endpoint represented as a UNIX domain path.
