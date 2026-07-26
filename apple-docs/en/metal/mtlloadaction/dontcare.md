---
title: MTLLoadAction.dontCare
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlloadaction/dontcare
source_url: 'https://developer.apple.com/documentation/metal/mtlloadaction/dontcare'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlloadaction/dontcare.json'
content_hash: 'sha256:6931673a3dadcd4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLoadAction](../mtlloadaction.md)

# MTLLoadAction.dontCare

<sub>Case</sub>

The GPU has permission to discard the existing contents of the attachment at the start of the render pass, replacing them with arbitrary data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case dontCare
```

## See Also

### Load actions

- [MTLLoadActionLoad](load.md) — The GPU preserves the existing contents of the attachment at the start of the render pass.
- [MTLLoadActionClear](clear.md) — The GPU writes a value to every pixel in the attachment at the start of the render pass.
