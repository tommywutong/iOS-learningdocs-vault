---
title: BonjourListenerProvider
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/bonjourlistenerprovider
source_url: 'https://developer.apple.com/documentation/network/bonjourlistenerprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/bonjourlistenerprovider.json'
content_hash: 'sha256:c0e42b5b787f9f25'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# BonjourListenerProvider

<sub>Structure</sub>

Advertise a Bonjour service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct BonjourListenerProvider
```

## Relationships

- **Conforms To**: [ListenerProvider](listenerprovider.md)

## Topics

### Initializers

- [init(name:type:domain:txtRecord:)](<bonjourlistenerprovider/init(name_type_domain_txtrecord_).md>) — Create a Bonjour service to advertise.

### Instance Properties

- [service](bonjourlistenerprovider/service.md) — The service advertised by the listener.
