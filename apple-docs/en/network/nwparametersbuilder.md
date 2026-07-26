---
title: NWParametersBuilder
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwparametersbuilder
source_url: 'https://developer.apple.com/documentation/network/nwparametersbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersbuilder.json'
content_hash: 'sha256:3d01bf4dce69a3a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWParametersBuilder

<sub>Structure</sub>

An opaque class that is responsible for creating and configuring NWParameters based on the parameterized protocol stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NWParametersBuilder<Top, each P> where Top : NetworkProtocolOptions, repeat each P : NetworkProtocolOptions
```

## Relationships

- **Conforms To**: [NWParametersProvider](nwparametersprovider.md)

## Topics

### Initializers

- [init(_:)](<nwparametersbuilder/init(__).md>)
- [init(auto:)](<nwparametersbuilder/init(auto_).md>)

### Instance Methods

- [wifiAware(_:)](<nwparametersbuilder/wifiaware(__).md>) — Configure Wi-Fi Aware properties on an `NetworkConnection`

### Type Methods

- [parameters(_:)](<nwparametersbuilder/parameters(__).md>)
- [parameters(initialParameters:_:)](<nwparametersbuilder/parameters(initialparameters___).md>)
