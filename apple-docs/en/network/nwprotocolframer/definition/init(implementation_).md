---
title: 'init(implementation:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/definition/init(implementation:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/definition/init(implementation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/definition/init%28implementation%3A%29.json'
content_hash: 'sha256:c28b1c38ec39e2e3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Definition](../definition.md)

# init(implementation:)

<sub>Initializer</sub>

Initializes a new protocol definition based on your protocol implementation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(implementation: any NWProtocolFramerImplementation.Type)
```

## Discussion

Each time you initialize a protocol definition with your implemention, a new definition is created that will not be considered equal to other definitions. If you need to associate messages with a protocol you have added to a connection’s protocol stack, make sure to use the same definition.
