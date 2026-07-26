---
title: 'indirectComputeCommandAt(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlindirectcommandbuffer/indirectcomputecommandat(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/indirectcomputecommandat(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbuffer/indirectcomputecommandat%28_%3A%29.json'
content_hash: 'sha256:835efed3a1c01ee3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md)

# indirectComputeCommandAt(_:)

<sub>Instance Method</sub>

Gets the compute command at the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func indirectComputeCommandAt(_ commandIndex: Int) -> any MTLIndirectComputeCommand
```

## Parameters

- `commandIndex` — The index of the command to retrieve.

## Discussion

Call this method only if the indirect command buffer contains compute commands.

## See Also

### Retrieving commands

- [- indirectRenderCommandAtIndex:](<indirectrendercommandat(__).md>) — Gets the render command at the given index.
- [indirectComputeCommand(at:)](<indirectcomputecommand(at_).md>) — Gets the compute command at the given index.
