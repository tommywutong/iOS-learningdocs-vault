---
title: 'indirectRenderCommandAt(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlindirectcommandbuffer/indirectrendercommandat(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/indirectrendercommandat(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbuffer/indirectrendercommandat%28_%3A%29.json'
content_hash: 'sha256:8617ff13c5c7bd5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md)

# indirectRenderCommandAt(_:)

<sub>Instance Method</sub>

Gets the render command at the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func indirectRenderCommandAt(_ commandIndex: Int) -> any MTLIndirectRenderCommand
```

## Parameters

- `commandIndex` — The index of the command to retrieve.

## Discussion

Call this method only if the indirect command buffer contains rendering commands.

## See Also

### Retrieving commands

- [- indirectComputeCommandAtIndex:](<indirectcomputecommandat(__).md>) — Gets the compute command at the given index.
- [indirectComputeCommand(at:)](<indirectcomputecommand(at_).md>) — Gets the compute command at the given index.
