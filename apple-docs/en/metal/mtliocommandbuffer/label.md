---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandbuffer/label
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/label.json'
content_hash: 'sha256:1ce2b497b15ef9d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# label

<sub>Instance Property</sub>

An optional name for the input/output command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## See Also

### Debugging a command buffer

- [- pushDebugGroup:](<pushdebuggroup(__).md>) — Sets the current name for this input/output command encoder by adding it to the top of the debug name stack.
- [- popDebugGroup](<popdebuggroup().md>) — Restores the previous name for this input/output command encoder by removing the top item of the debug name stack.
