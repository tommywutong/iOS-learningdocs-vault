---
title: 'NWEndpoint.hostPort(host:port:)'
framework: Network
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwendpoint/hostport(host:port:)'
source_url: 'https://developer.apple.com/documentation/network/nwendpoint/hostport(host:port:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwendpoint/hostport%28host%3Aport%3A%29.json'
content_hash: 'sha256:f7e897e07d19c7ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEndpoint](../nwendpoint.md)

# NWEndpoint.hostPort(host:port:)

<sub>Case</sub>

An endpoint represented as a host and port, with the host including both names and addresses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case hostPort(host: NWEndpoint.Host, port: NWEndpoint.Port)
```

## See Also

### Endpoint Types

- [NWEndpoint.service(name:type:domain:interface:)](<service(name_type_domain_interface_).md>) — An endpoint represented as a Bonjour service.
- [NWEndpoint.url(_:)](<url(__).md>) — An endpoint represented as a URL, with host and port values inferred from the URL.
- [NWEndpoint.unix(path:)](<unix(path_).md>) — An endpoint represented as a UNIX domain path.
