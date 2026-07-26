---
title: 'bonjour(name:type:domain:txtRecord:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/listenerprovider/bonjour(name:type:domain:txtrecord:)'
source_url: 'https://developer.apple.com/documentation/network/listenerprovider/bonjour(name:type:domain:txtrecord:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/listenerprovider/bonjour%28name%3Atype%3Adomain%3Atxtrecord%3A%29.json'
content_hash: 'sha256:0d74158d200288a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [ListenerProvider](../listenerprovider.md)

# bonjour(name:type:domain:txtRecord:)

<sub>Type Method</sub>

Create a Bonjour service to advertise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func bonjour(name: String? = nil, type: String, domain: String? = nil, txtRecord: NWTXTRecord? = nil) -> BonjourListenerProvider
```

## Parameters

- `name` — The name to advertise. Defaults to `nil`, which allows the system to provide the name.

- `type` — The Bonjour service type to advertise.

- `domain` — The domain to advertise. Defaults to `nil`, which allows Bonjour to register in all default registration domains.

- `txtRecord` — An optional text record to advertise. If not provided, Bonjour will not register any text record associated with this service. Later, a text record can be advertised by setting `service` on `NetworkListener` with a TXT record.

## Discussion

Advertised services should be registered with IANA.
