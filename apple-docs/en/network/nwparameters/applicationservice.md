---
title: applicationService
framework: Network
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparameters/applicationservice
source_url: 'https://developer.apple.com/documentation/network/nwparameters/applicationservice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparameters/applicationservice.json'
content_hash: 'sha256:3cd59c6b9eb8968d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParameters](../nwparameters.md)

# applicationService

<sub>Type Property</sub>

The default parameters for connecting with other, local devices that are running your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class var applicationService: NWParameters { get }
```

## Discussion

The default parameters set up an encrypted connection with another device on the local network. You can use these parameters as-is, or you can add a [NWProtocolFramer](../nwprotocolframer.md) to provide application-level messaging support.
