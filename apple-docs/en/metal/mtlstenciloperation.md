---
title: MTLStencilOperation
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstenciloperation
source_url: 'https://developer.apple.com/documentation/metal/mtlstenciloperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstenciloperation.json'
content_hash: 'sha256:968c391889849330'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStencilOperation

<sub>Enumeration</sub>

The operation performed on a currently stored stencil value when a comparison test passes or fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLStencilOperation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Stencil operations

- [MTLStencilOperationKeep](mtlstenciloperation/keep.md) — A stencil operation that doesn’t modify a stencil value.
- [MTLStencilOperationZero](mtlstenciloperation/zero.md) — A stencil operation that sets a stencil value to zero.
- [MTLStencilOperationReplace](mtlstenciloperation/replace.md) — A stencil operation that replaces a stencil value with a reference value.
- [MTLStencilOperationIncrementClamp](mtlstenciloperation/incrementclamp.md) — A stencil operation that increases a stencil value by one, but only when the current value isn’t the maximum representable value.
- [MTLStencilOperationDecrementClamp](mtlstenciloperation/decrementclamp.md) — A stencil operation that decreases a nonzero stencil value by one.
- [MTLStencilOperationInvert](mtlstenciloperation/invert.md) — A stencil operation that applies a logical bitwise NOT to a stencil value.
- [MTLStencilOperationIncrementWrap](mtlstenciloperation/incrementwrap.md) — A stencil operation that decreases a nonzero stencil value by one, or when it’s the maximum representable value, resets it to zero.
- [MTLStencilOperationDecrementWrap](mtlstenciloperation/decrementwrap.md) — A stencil operation that decreases a nonzero stencil value by one, or when it’s zero, resets it to the maximum representable value.

### Initializers

- [init(rawValue:)](<mtlstenciloperation/init(rawvalue_).md>)

## See Also

### Configuring stencil functions and operations

- [stencilFailureOperation](mtlstencildescriptor/stencilfailureoperation.md) — The operation that is performed to update the values in the stencil attachment when the stencil test fails.
- [depthFailureOperation](mtlstencildescriptor/depthfailureoperation.md) — The operation that is performed to update the values in the stencil attachment when the stencil test passes, but the depth test fails.
- [depthStencilPassOperation](mtlstencildescriptor/depthstencilpassoperation.md) — The operation that is performed to update the values in the stencil attachment when both the stencil test and the depth test pass.
- [stencilCompareFunction](mtlstencildescriptor/stencilcomparefunction.md) — The comparison that is performed between the masked reference value and a masked value in the stencil attachment.
