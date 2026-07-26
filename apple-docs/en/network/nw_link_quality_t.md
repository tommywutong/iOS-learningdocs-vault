---
title: nw_link_quality_t
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_link_quality_t
source_url: 'https://developer.apple.com/documentation/network/nw_link_quality_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_link_quality_t.json'
content_hash: 'sha256:2cce9927ddb9550e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_link_quality_t

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct nw_link_quality_t
```

## Overview

Link quality measurement is a representation of the expected capabilities of the link layer network attachment. Use this value to tune initial values for algorithms that can scale with the capabilities of the network. Do not use this value to gate connection attempts or to override adjustments that would be made based on actual network performance.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init(_:)](<nw_link_quality_t/init(__).md>)
- [init(rawValue:)](<nw_link_quality_t/init(rawvalue_).md>)

### Instance Properties

- [rawValue](nw_link_quality_t/rawvalue.md)
