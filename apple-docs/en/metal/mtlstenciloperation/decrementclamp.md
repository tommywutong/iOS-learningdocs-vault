---
title: MTLStencilOperation.decrementClamp
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstenciloperation/decrementclamp
source_url: 'https://developer.apple.com/documentation/metal/mtlstenciloperation/decrementclamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstenciloperation/decrementclamp.json'
content_hash: 'sha256:c8ff71e5e618710f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStencilOperation](../mtlstenciloperation.md)

# MTLStencilOperation.decrementClamp

<sub>Case</sub>

A stencil operation that decreases a nonzero stencil value by one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case decrementClamp
```

## Discussion

The operation doesn’t modify a stencil value if it’s currently equal to `0`.

## See Also

### Stencil operations

- [MTLStencilOperationKeep](keep.md) — A stencil operation that doesn’t modify a stencil value.
- [MTLStencilOperationZero](zero.md) — A stencil operation that sets a stencil value to zero.
- [MTLStencilOperationReplace](replace.md) — A stencil operation that replaces a stencil value with a reference value.
- [MTLStencilOperationIncrementClamp](incrementclamp.md) — A stencil operation that increases a stencil value by one, but only when the current value isn’t the maximum representable value.
- [MTLStencilOperationInvert](invert.md) — A stencil operation that applies a logical bitwise NOT to a stencil value.
- [MTLStencilOperationIncrementWrap](incrementwrap.md) — A stencil operation that decreases a nonzero stencil value by one, or when it’s the maximum representable value, resets it to zero.
- [MTLStencilOperationDecrementWrap](decrementwrap.md) — A stencil operation that decreases a nonzero stencil value by one, or when it’s zero, resets it to the maximum representable value.
