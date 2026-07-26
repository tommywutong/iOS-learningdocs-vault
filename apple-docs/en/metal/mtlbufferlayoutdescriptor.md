---
title: MTLBufferLayoutDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbufferlayoutdescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbufferlayoutdescriptor.json'
content_hash: 'sha256:62120b8704c93d5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBufferLayoutDescriptor

<sub>Class</sub>

A description of how a compute function fetches input data for an attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLBufferLayoutDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Describing fetch behavior

- [stride](mtlbufferlayoutdescriptor/stride.md) — The number of bytes from one buffer entry to the next.
- [stepFunction](mtlbufferlayoutdescriptor/stepfunction.md) — Determines how and when compute functions fetch data.
- [stepRate](mtlbufferlayoutdescriptor/steprate.md) — How frequently the step function should load data.
- [MTLStepFunction](mtlstepfunction.md) — The frequency and locations at which a function fetches attribute data.

## See Also

### Configuring compute pass inputs

- [stageInputDescriptor](mtlcomputepipelinedescriptor/stageinputdescriptor.md) — The organization of input and output data for the next kernel call.
- [MTLAttributeDescriptor](mtlattributedescriptor.md) — A descriptor of an argument’s format and where its data is in memory.
- [MTLAttributeDescriptorArray](mtlattributedescriptorarray.md) — An array of attribute descriptor objects.
- [MTLBufferLayoutDescriptorArray](mtlbufferlayoutdescriptorarray.md) — An array of buffer layout descriptor objects.
