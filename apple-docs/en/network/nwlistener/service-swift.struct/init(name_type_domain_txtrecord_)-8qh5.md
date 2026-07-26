---
title: 'init(name:type:domain:txtRecord:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwlistener/service-swift.struct/init(name:type:domain:txtrecord:)-8qh5'
source_url: 'https://developer.apple.com/documentation/network/nwlistener/service-swift.struct/init(name:type:domain:txtrecord:)-8qh5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwlistener/service-swift.struct/init%28name%3Atype%3Adomain%3Atxtrecord%3A%29-8qh5.json'
content_hash: 'sha256:b3f3cc58dc675964'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWListener](../../nwlistener.md) · [Service](../service-swift.struct.md)

# init(name:type:domain:txtRecord:)

<sub>Initializer</sub>

Initializes a Bonjour service to advertise with a TXT record.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(name: String? = nil, type: String, domain: String? = nil, txtRecord: NWTXTRecord)
```

## Discussion

Advertised services are primarily defined by their types. If you do not specify a service name, the device name will be chosen. You should not specify a Bonjour domain unless you know you need to advertise only on a particular domain.

## See Also

### Defining Services

- [init(name:type:domain:txtRecord:)](<init(name_type_domain_txtrecord_)-1lb30.md>) — Initializes a Bonjour service to advertise.
- [noAutoRename](noautorename.md) — A Boolean that indicates whether the service prohibits automatic renaming in the event of a name conflict.
