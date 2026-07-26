---
title: size
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcommandbuffer/size
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbuffer/size.json'
content_hash: 'sha256:ed0e0ce3844c4ea8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md)

# size

<sub>Instance Property</sub>

The number of commands contained in the indirect command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var size: Int { get }
```

## Discussion

You set the value of this property when you create the indirect command buffer, and afterwards it doesn’t change.
