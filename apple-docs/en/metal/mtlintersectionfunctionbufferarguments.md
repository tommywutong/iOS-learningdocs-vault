---
title: MTLIntersectionFunctionBufferArguments
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlintersectionfunctionbufferarguments
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctionbufferarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctionbufferarguments.json'
content_hash: 'sha256:db33c507ee13196b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIntersectionFunctionBufferArguments

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLIntersectionFunctionBufferArguments
```

## Overview

Struct containing arguments for intersection function buffers.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<mtlintersectionfunctionbufferarguments/init().md>)
- [init(intersectionFunctionBuffer:intersectionFunctionBufferSize:intersectionFunctionStride:)](<mtlintersectionfunctionbufferarguments/init(intersectionfunctionbuffer_intersectionfunctionbuffersize_intersectionfunctionstride_).md>)

### Instance Properties

- [intersectionFunctionBuffer](mtlintersectionfunctionbufferarguments/intersectionfunctionbuffer.md)
- [intersectionFunctionBufferSize](mtlintersectionfunctionbufferarguments/intersectionfunctionbuffersize.md)
- [intersectionFunctionStride](mtlintersectionfunctionbufferarguments/intersectionfunctionstride.md)

## See Also

### Intersection function tables

- [MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md) — A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
- [MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md) — A specification of how to create an intersection function table.
- [MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md) — A description of an intersection function that performs an intersection test.
- [MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature.md) — Constants for specifying different types of custom intersection functions.
