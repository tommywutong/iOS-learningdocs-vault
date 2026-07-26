---
title: NetworkListener.ServiceRegistrationChange
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networklistener/serviceregistrationchange
source_url: 'https://developer.apple.com/documentation/network/networklistener/serviceregistrationchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networklistener/serviceregistrationchange.json'
content_hash: 'sha256:52645b56e4000c09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkListener](../networklistener.md)

# NetworkListener.ServiceRegistrationChange

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ServiceRegistrationChange
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [NetworkListener.ServiceRegistrationChange.add(_:)](<serviceregistrationchange/add(__).md>) — An event when a Bonjour service has been registered, with the endpoint being advertised
- [NetworkListener.ServiceRegistrationChange.remove(_:)](<serviceregistrationchange/remove(__).md>) — An event when a Bonjour service has been unregistered, with the endpoint being removed
