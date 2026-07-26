---
title: MTLStencilOperation.incrementWrap
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstenciloperation/incrementwrap
source_url: 'https://developer.apple.com/documentation/metal/mtlstenciloperation/incrementwrap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstenciloperation/incrementwrap.json'
content_hash: 'sha256:1cacec301579a2bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStencilOperation](../mtlstenciloperation.md)

# MTLStencilOperation.incrementWrap

<sub>Case</sub>

A stencil operation that decreases a nonzero stencil value by one, or when it’s the maximum representable value, resets it to zero.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case incrementWrap
```

## Discussion

The operation sets a stencil value to `0` if it’s currently equal to the maximum representable value.

## See Also

### Stencil operations

- [MTLStencilOperationKeep](keep.md) — A stencil operation that doesn’t modify a stencil value.
- [MTLStencilOperationZero](zero.md) — A stencil operation that sets a stencil value to zero.
- [MTLStencilOperationReplace](replace.md) — A stencil operation that replaces a stencil value with a reference value.
- [MTLStencilOperationIncrementClamp](incrementclamp.md) — A stencil operation that increases a stencil value by one, but only when the current value isn’t the maximum representable value.
- [MTLStencilOperationDecrementClamp](decrementclamp.md) — A stencil operation that decreases a nonzero stencil value by one.
- [MTLStencilOperationInvert](invert.md) — A stencil operation that applies a logical bitwise NOT to a stencil value.
- [MTLStencilOperationDecrementWrap](decrementwrap.md) — A stencil operation that decreases a nonzero stencil value by one, or when it’s zero, resets it to the maximum representable value.
