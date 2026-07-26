---
title: reset()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 11.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectcomputecommand/reset()
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcomputecommand/reset()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcomputecommand/reset%28%29.json'
content_hash: 'sha256:6d8ea0e69b57cc8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectComputeCommand](../mtlindirectcomputecommand.md)

# reset()

<sub>Instance Method</sub>

Resets the command to its default state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func reset()
```

## Discussion

A command that has been reset loses any state that you previously set and does nothing when executed.
