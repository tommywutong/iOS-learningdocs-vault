---
title: MTLLoadAction.load
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlloadaction/load
source_url: 'https://developer.apple.com/documentation/metal/mtlloadaction/load'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlloadaction/load.json'
content_hash: 'sha256:3157a3ef130aa0a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLoadAction](../mtlloadaction.md)

# MTLLoadAction.load

<sub>Case</sub>

The GPU preserves the existing contents of the attachment at the start of the render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case load
```

## See Also

### Load actions

- [MTLLoadActionDontCare](dontcare.md) — The GPU has permission to discard the existing contents of the attachment at the start of the render pass, replacing them with arbitrary data.
- [MTLLoadActionClear](clear.md) — The GPU writes a value to every pixel in the attachment at the start of the render pass.
