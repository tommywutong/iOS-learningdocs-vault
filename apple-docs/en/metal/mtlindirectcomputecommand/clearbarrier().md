---
title: clearBarrier()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcomputecommand/clearbarrier()
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/clearbarrier()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcomputecommand/clearbarrier%28%29.json'
content_hash: 'sha256:f12c2f5820c9f70c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectComputeCommand](../mtlindirectcomputecommand.md)

# clearBarrier()

<sub>Instance Method</sub>

Removes any barrier set on the command.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func clearBarrier()
```

## Discussion

You need to set or clear barriers (as needed) before executing any of the commands in the indirect command buffer.

## See Also

### Synchronizing command execution

- [- setBarrier](<setbarrier().md>) — Adds a barrier to ensure that commands executed prior to this command are complete before this command executes.
