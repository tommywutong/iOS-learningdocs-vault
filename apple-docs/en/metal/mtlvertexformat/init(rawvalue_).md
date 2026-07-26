---
title: 'init(rawValue:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlvertexformat/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexformat/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexformat/init%28rawvalue%3A%29.json'
content_hash: 'sha256:8545fcaf1a855252'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexFormat](../mtlvertexformat.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a vertex format from a raw integer value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(rawValue: UInt)
```

## Parameters

- `rawValue` — The underlying integer value that represents a vertex format.

## Discussion

Use the [MTLVertexFormat](../mtlvertexformat.md) structure’s type properties, such as [MTLVertexFormatUChar4Normalized_BGRA](uchar4normalized_bgra.md), instead of this initializer.
