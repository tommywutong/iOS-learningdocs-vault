---
title: 'init(_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwendpoint/port/init(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwendpoint/port/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwendpoint/port/init%28_%3A%29.json'
content_hash: 'sha256:a8861ef80af85bda'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWEndpoint](../../nwendpoint.md) · [Port](../port.md)

# init(_:)

<sub>Initializer</sub>

Initializes a port with a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ service: String)
```

## Discussion

Port strings are expected to be numeric values between 0 and 65535. Initializing with any other string will fail.
