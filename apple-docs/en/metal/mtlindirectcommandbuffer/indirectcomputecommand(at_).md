---
title: 'indirectComputeCommand(at:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（14.0 起废弃）, iPadOS 13.0+（14.0 起废弃）, Mac Catalyst 14.0+（14.0 起废弃）, tvOS 13.0+（14.0 起废弃）, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlindirectcommandbuffer/indirectcomputecommand(at:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbuffer/indirectcomputecommand(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbuffer/indirectcomputecommand%28at%3A%29.json'
content_hash: 'sha256:8f5e8389b8fda905'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md)

# indirectComputeCommand(at:)

<sub>Instance Method</sub>

Gets the compute command at the given index.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indirectComputeCommand(at Index: Int) -> any MTLIndirectComputeCommand
```

## Parameters

- `Index` — The index of the command to retrieve.

## Discussion

Call this method only if the indirect command buffer contains compute commands.

## See Also

### Retrieving commands

- [- indirectRenderCommandAtIndex:](<indirectrendercommandat(__).md>) — Gets the render command at the given index.
- [- indirectComputeCommandAtIndex:](<indirectcomputecommandat(__).md>) — Gets the compute command at the given index.
