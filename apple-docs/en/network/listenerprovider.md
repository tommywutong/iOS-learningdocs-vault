---
title: ListenerProvider
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/listenerprovider
source_url: 'https://developer.apple.com/documentation/network/listenerprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/listenerprovider.json'
content_hash: 'sha256:e13c3dd9a05efc60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# ListenerProvider

<sub>Protocol</sub>

Extensible support for configuring advertise descriptors to define the service a listener should advertise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ListenerProvider
```

## Overview

Listeners use advertise descriptors to advertise services that can subsequently be discovered by browsers.

## Relationships

- **Conforming Types**: [BonjourListenerProvider](bonjourlistenerprovider.md)

## Topics

### Instance Properties

- [service](listenerprovider/service.md)

### Type Methods

- [bonjour(name:type:domain:txtRecord:)](<listenerprovider/bonjour(name_type_domain_txtrecord_).md>) — Create a Bonjour service to advertise.
- [wifiAware(_:active:)](<listenerprovider/wifiaware(__active_).md>) — Sets a network listener to publish Wi-Fi Aware services to the selected paired devices.
