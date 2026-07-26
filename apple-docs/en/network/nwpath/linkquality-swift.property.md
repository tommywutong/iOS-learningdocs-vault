---
title: linkQuality
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpath/linkquality-swift.property
source_url: 'https://developer.apple.com/documentation/network/nwpath/linkquality-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath/linkquality-swift.property.json'
content_hash: 'sha256:8d6614fc6b523b14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPath](../nwpath.md)

# linkQuality

<sub>Instance Property</sub>

Represents the link quality measurement of the link layer network attachment

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var linkQuality: NWPath.LinkQuality { get }
```

## Discussion

Use this value to tune initial values for algorithms that can scale with the capabilities of the network. Do not use this value to gate connection attempts or to override adjustments that would be made based on actual network performance.
