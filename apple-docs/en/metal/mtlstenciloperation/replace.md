---
title: MTLStencilOperation.replace
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstenciloperation/replace
source_url: 'https://developer.apple.com/documentation/metal/mtlstenciloperation/replace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstenciloperation/replace.json'
content_hash: 'sha256:59f4dcaa54a1b9a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStencilOperation](../mtlstenciloperation.md)

# MTLStencilOperation.replace

<sub>Case</sub>

A stencil operation that replaces a stencil value with a reference value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case replace
```

## Discussion

You can set by the reference value by calling the [- setStencilReferenceValue:](<../mtlrendercommandencoder/setstencilreferencevalue(__).md>) method of an [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) instance.

## See Also

### Stencil operations

- [MTLStencilOperationKeep](keep.md) — A stencil operation that doesn’t modify a stencil value.
- [MTLStencilOperationZero](zero.md) — A stencil operation that sets a stencil value to zero.
- [MTLStencilOperationIncrementClamp](incrementclamp.md) — A stencil operation that increases a stencil value by one, but only when the current value isn’t the maximum representable value.
- [MTLStencilOperationDecrementClamp](decrementclamp.md) — A stencil operation that decreases a nonzero stencil value by one.
- [MTLStencilOperationInvert](invert.md) — A stencil operation that applies a logical bitwise NOT to a stencil value.
- [MTLStencilOperationIncrementWrap](incrementwrap.md) — A stencil operation that decreases a nonzero stencil value by one, or when it’s the maximum representable value, resets it to zero.
- [MTLStencilOperationDecrementWrap](decrementwrap.md) — A stencil operation that decreases a nonzero stencil value by one, or when it’s zero, resets it to the maximum representable value.
