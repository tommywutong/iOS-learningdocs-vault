---
title: popDebugGroup()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandbuffer/popdebuggroup()
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/popdebuggroup()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/popdebuggroup%28%29.json'
content_hash: 'sha256:4adf60a1712203dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# popDebugGroup()

<sub>Instance Method</sub>

Restores the previous name for this input/output command encoder by removing the top item of the debug name stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func popDebugGroup()
```

## See Also

### Debugging a command buffer

- [label](label.md) — An optional name for the input/output command buffer.
- [- pushDebugGroup:](<pushdebuggroup(__).md>) — Sets the current name for this input/output command encoder by adding it to the top of the debug name stack.
