---
title: maximumDatagramSize
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkchannel/maximumdatagramsize
source_url: 'https://developer.apple.com/documentation/network/networkchannel/maximumdatagramsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel/maximumdatagramsize.json'
content_hash: 'sha256:e02106dece5f8e10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkChannel](../networkchannel.md)

# maximumDatagramSize

<sub>Instance Property</sub>

Retrieve the maximum datagram size that can be sent on the channel. Any datagrams sent should be less than or equal to this size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var maximumDatagramSize: Int { get }
```
