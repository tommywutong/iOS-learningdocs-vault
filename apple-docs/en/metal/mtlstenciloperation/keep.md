---
title: MTLStencilOperation.keep
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstenciloperation/keep
source_url: 'https://developer.apple.com/documentation/metal/mtlstenciloperation/keep'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstenciloperation/keep.json'
content_hash: 'sha256:8fe757c8a13208c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStencilOperation](../mtlstenciloperation.md)

# MTLStencilOperation.keep

<sub>Case</sub>

A stencil operation that doesn’t modify a stencil value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case keep
```

## See Also

### Stencil operations

- [MTLStencilOperationZero](zero.md) — A stencil operation that sets a stencil value to zero.
- [MTLStencilOperationReplace](replace.md) — A stencil operation that replaces a stencil value with a reference value.
- [MTLStencilOperationIncrementClamp](incrementclamp.md) — A stencil operation that increases a stencil value by one, but only when the current value isn’t the maximum representable value.
- [MTLStencilOperationDecrementClamp](decrementclamp.md) — A stencil operation that decreases a nonzero stencil value by one.
- [MTLStencilOperationInvert](invert.md) — A stencil operation that applies a logical bitwise NOT to a stencil value.
- [MTLStencilOperationIncrementWrap](incrementwrap.md) — A stencil operation that decreases a nonzero stencil value by one, or when it’s the maximum representable value, resets it to zero.
- [MTLStencilOperationDecrementWrap](decrementwrap.md) — A stencil operation that decreases a nonzero stencil value by one, or when it’s zero, resets it to the maximum representable value.
