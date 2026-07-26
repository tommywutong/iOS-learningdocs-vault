---
title: NetworkCoder
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkcoder
source_url: 'https://developer.apple.com/documentation/network/networkcoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkcoder.json'
content_hash: 'sha256:686613380162e711'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NetworkCoder

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NetworkCoder : Sendable
```

## Relationships

- **Inherits From**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [NetworkJSONCoder](networkjsoncoder.md), [NetworkPropertyListCoder](networkpropertylistcoder.md)

## Topics

### Associated Types

- [Decoder](networkcoder/decoder.md)
- [Encoder](networkcoder/encoder.md)

### Initializers

- [init()](<networkcoder/init().md>)

### Instance Methods

- [makeDecoder()](<networkcoder/makedecoder().md>) — Returns an instance of NetworkDecoder
- [makeEncoder()](<networkcoder/makeencoder().md>) — Returns an instance of NetworkEncoder

### Type Properties

- [json](networkcoder/json.md)
- [propertyList](networkcoder/propertylist.md)
