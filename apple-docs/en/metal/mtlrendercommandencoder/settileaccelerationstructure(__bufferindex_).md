---
title: 'setTileAccelerationStructure(_:bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/settileaccelerationstructure(_:bufferindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settileaccelerationstructure(_:bufferindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/settileaccelerationstructure%28_%3Abufferindex%3A%29.json'
content_hash: 'sha256:b142a7f83e33c0b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setTileAccelerationStructure(_:bufferIndex:)

<sub>Instance Method</sub>

Assigns an acceleration structure to an entry in the tile shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setTileAccelerationStructure(_ accelerationStructure: (any MTLAccelerationStructure)?, bufferIndex: Int)
```

## Parameters

- `accelerationStructure` — An [MTLAccelerationStructure](../mtlaccelerationstructure.md) instance the command assigns to an entry in the tile shader argument table for acceleration structures.

- `bufferIndex` — An integer that represents the entry in the tile shader argument table for acceleration structures that stores a record of `accelerationStructure`.

## Discussion

By default, the acceleration structure at each index is `nil`.
