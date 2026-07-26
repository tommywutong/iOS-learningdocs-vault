---
title: options
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/framer/options
source_url: 'https://developer.apple.com/documentation/network/framer/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/framer/options.json'
content_hash: 'sha256:54d2e49c4646b966'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [Framer](../framer.md)

# options

<sub>Instance Property</sub>

The framer options to use with this framer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var options: NWProtocolFramer.Options
```

## Discussion

Framer implementations can provide extensions with chainable functions that internally set keys on this options object.
