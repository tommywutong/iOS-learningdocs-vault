---
title: bigEndian
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkfixedwidthinteger/bigendian
source_url: 'https://developer.apple.com/documentation/network/networkfixedwidthinteger/bigendian'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkfixedwidthinteger/bigendian.json'
content_hash: 'sha256:286b8e79ac751c38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NetworkFixedWidthInteger](../networkfixedwidthinteger.md)

# bigEndian

<sub>Instance Property</sub>

The big-endian representation of this integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
override var bigEndian: Self { get }
```

## Discussion

If necessary, the byte order of this value is reversed from the typical byte order of this integer type. On a big-endian platform, for any integer `x`, `x == x.bigEndian`.
