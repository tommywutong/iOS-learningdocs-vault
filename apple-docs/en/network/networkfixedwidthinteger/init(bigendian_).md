---
title: 'init(bigEndian:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/networkfixedwidthinteger/init(bigendian:)'
source_url: 'https://developer.apple.com/documentation/network/networkfixedwidthinteger/init(bigendian:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkfixedwidthinteger/init%28bigendian%3A%29.json'
content_hash: 'sha256:c4385f9d87ca722f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkFixedWidthInteger](../networkfixedwidthinteger.md)

# init(bigEndian:)

<sub>Initializer</sub>

Creates an integer from its big-endian representation, changing the byte order if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
override init(bigEndian: Self)
```

## Parameters

- `value` — A value to use as the big-endian representation of the new integer.
