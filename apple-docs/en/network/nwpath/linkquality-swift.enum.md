---
title: NWPath.LinkQuality
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwpath/linkquality-swift.enum
source_url: 'https://developer.apple.com/documentation/network/nwpath/linkquality-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwpath/linkquality-swift.enum.json'
content_hash: 'sha256:e071f5ba181facd7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWPath](../nwpath.md)

# NWPath.LinkQuality

<sub>Enumeration</sub>

Represents the link quality measurement of the link layer network attachment

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum LinkQuality
```

## Overview

Use this value to tune initial values for algorithms that can scale with the capabilities of the network. Do not use this value to gate connection attempts or to override adjustments that would be made based on actual network performance.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [NWPath.LinkQuality.good](linkquality-swift.enum/good.md) — Link quality is good
- [NWPath.LinkQuality.minimal](linkquality-swift.enum/minimal.md) — Link quality is minimal
- [NWPath.LinkQuality.moderate](linkquality-swift.enum/moderate.md) — Link quality is moderate
- [NWPath.LinkQuality.unknown](linkquality-swift.enum/unknown.md) — No link quality measurement is available
