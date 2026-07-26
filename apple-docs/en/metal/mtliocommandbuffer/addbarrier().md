---
title: addBarrier()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandbuffer/addbarrier()
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/addbarrier()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/addbarrier%28%29.json'
content_hash: 'sha256:1eefb35ad682ad71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# addBarrier()

<sub>Instance Method</sub>

Encodes a barrier into the command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addBarrier()
```

## Discussion

The method encodes a barrier that starts any subsequent commands only after all the previously encoded commands have completed.
