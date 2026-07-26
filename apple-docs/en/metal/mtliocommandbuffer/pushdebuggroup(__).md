---
title: 'pushDebugGroup(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtliocommandbuffer/pushdebuggroup(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/pushdebuggroup(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/pushdebuggroup%28_%3A%29.json'
content_hash: 'sha256:17705101c9285ebf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# pushDebugGroup(_:)

<sub>Instance Method</sub>

Sets the current name for this input/output command encoder by adding it to the top of the debug name stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pushDebugGroup(_ string: String)
```

## Parameters

- `string` — A new debugging name.

## See Also

### Debugging a command buffer

- [label](label.md) — An optional name for the input/output command buffer.
- [- popDebugGroup](<popdebuggroup().md>) — Restores the previous name for this input/output command encoder by removing the top item of the debug name stack.
