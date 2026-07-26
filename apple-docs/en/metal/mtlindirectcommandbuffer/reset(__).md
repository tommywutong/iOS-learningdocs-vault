---
title: 'reset(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlindirectcommandbuffer/reset(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/reset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbuffer/reset%28_%3A%29.json'
content_hash: 'sha256:3cc83c545e75c1d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md)

# reset(_:)

<sub>Instance Method</sub>

Resets a range of commands to their default state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func reset(_ range: Range<Int>)
```

## Parameters

- `range` — The range of commands to reset. The range needs to fit inside the indirect command buffer’s extents.
