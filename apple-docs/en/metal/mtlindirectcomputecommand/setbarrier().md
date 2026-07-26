---
title: setBarrier()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcomputecommand/setbarrier()
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/setbarrier()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcomputecommand/setbarrier%28%29.json'
content_hash: 'sha256:bf807ddf0bde4ded'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectComputeCommand](../mtlindirectcomputecommand.md)

# setBarrier()

<sub>Instance Method</sub>

Adds a barrier to ensure that commands executed prior to this command are complete before this command executes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setBarrier()
```

## Discussion

Set or clear barriers (as needed) before encoding the command.

## See Also

### Synchronizing command execution

- [- clearBarrier](<clearbarrier().md>) — Removes any barrier set on the command.
