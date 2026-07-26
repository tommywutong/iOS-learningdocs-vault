---
title: 'init(name:type:domain:txtRecord:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwlistener/service-swift.struct/init(name:type:domain:txtrecord:)-1lb30'
source_url: 'https://developer.apple.com/documentation/network/nwlistener/service-swift.struct/init(name:type:domain:txtrecord:)-1lb30'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/service-swift.struct/init%28name%3Atype%3Adomain%3Atxtrecord%3A%29-1lb30.json'
content_hash: 'sha256:60c5fe62cd52cef9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWListener](../../nwlistener.md) · [Service](../service-swift.struct.md)

# init(name:type:domain:txtRecord:)

<sub>Initializer</sub>

Initializes a Bonjour service to advertise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(name: String? = nil, type: String, domain: String? = nil, txtRecord: Data? = nil)
```

## Discussion

Advertised services are primarily defined by their types. If you do not specify a service name, the device name will be chosen. You should not specify a Bonjour domain unless you know you need to advertise only on a particular domain.

## See Also

### Defining Services

- [init(name:type:domain:txtRecord:)](<init(name_type_domain_txtrecord_)-8qh5.md>) — Initializes a Bonjour service to advertise with a TXT record.
- [noAutoRename](noautorename.md) — A Boolean that indicates whether the service prohibits automatic renaming in the event of a name conflict.
