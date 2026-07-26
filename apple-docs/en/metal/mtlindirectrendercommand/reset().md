---
title: reset()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlindirectrendercommand/reset()
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectrendercommand/reset()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectrendercommand/reset%28%29.json'
content_hash: 'sha256:4d63fe9da2b03664'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectRenderCommand](../mtlindirectrendercommand.md)

# reset()

<sub>Instance Method</sub>

Resets the command to its default state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func reset()
```

## Discussion

A command that has been reset loses any state that you previously set and does nothing when executed.
