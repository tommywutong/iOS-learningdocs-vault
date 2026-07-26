---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtllogicaltophysicalcolorattachmentmap/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtllogicaltophysicalcolorattachmentmap/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllogicaltophysicalcolorattachmentmap/subscript%28_%3A%29.json'
content_hash: 'sha256:66a75a4b2cf553a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLogicalToPhysicalColorAttachmentMap](../mtllogicaltophysicalcolorattachmentmap.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Maps a physical color attachment index to a logical index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(logicalIndex: Int) -> Int { get set }
```

## Overview

To set the physical index, which represents the render pass color attachment index `P`, for a logical index, which represents the pipeline state’s configuration for a color attachment `L`, assign: `myMapping[L] = P`. To retrieve a stored physical index use `let P = myMapping[L]`.
