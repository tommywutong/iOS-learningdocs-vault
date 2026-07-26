---
title: 'NWEndpoint.url(_:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwendpoint/url(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwendpoint/url(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwendpoint/url%28_%3A%29.json'
content_hash: 'sha256:0e2c5772d82f3d96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEndpoint](../nwendpoint.md)

# NWEndpoint.url(_:)

<sub>Case</sub>

An endpoint represented as a URL, with host and port values inferred from the URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case url(URL)
```

## See Also

### Endpoint Types

- [NWEndpoint.hostPort(host:port:)](<hostport(host_port_).md>) — An endpoint represented as a host and port, with the host including both names and addresses.
- [NWEndpoint.service(name:type:domain:interface:)](<service(name_type_domain_interface_).md>) — An endpoint represented as a Bonjour service.
- [NWEndpoint.unix(path:)](<unix(path_).md>) — An endpoint represented as a UNIX domain path.
