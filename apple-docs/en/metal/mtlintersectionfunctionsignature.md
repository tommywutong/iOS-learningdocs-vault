---
title: MTLIntersectionFunctionSignature
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlintersectionfunctionsignature
source_url: 'https://developer.apple.com/documentation/metal/mtlintersectionfunctionsignature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlintersectionfunctionsignature.json'
content_hash: 'sha256:0cc90ef75dca8d3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIntersectionFunctionSignature

<sub>Structure</sub>

Constants for specifying different types of custom intersection functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLIntersectionFunctionSignature
```

## Overview

For more information on declaring intersection functions in MSL, see [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializing the intersection function signature

- [init(rawValue:)](<mtlintersectionfunctionsignature/init(rawvalue_).md>) — Returns a new signature description from a specified raw value.

### Specifying the intersection function signature

- [MTLIntersectionFunctionSignatureInstancing](mtlintersectionfunctionsignature/instancing.md) — A flag indicating that function signature uses instancing.
- [MTLIntersectionFunctionSignatureTriangleData](mtlintersectionfunctionsignature/triangledata.md) — A flag indicating that function signature uses triangle data.
- [MTLIntersectionFunctionSignatureWorldSpaceData](mtlintersectionfunctionsignature/worldspacedata.md) — A flag indicating that function signature uses world space data.

### Type Properties

- [MTLIntersectionFunctionSignatureCurveData](mtlintersectionfunctionsignature/curvedata.md)
- [MTLIntersectionFunctionSignatureExtendedLimits](mtlintersectionfunctionsignature/extendedlimits.md)
- [MTLIntersectionFunctionSignatureInstanceMotion](mtlintersectionfunctionsignature/instancemotion.md)
- [MTLIntersectionFunctionSignatureIntersectionFunctionBuffer](mtlintersectionfunctionsignature/intersectionfunctionbuffer.md)
- [MTLIntersectionFunctionSignatureMaxLevels](mtlintersectionfunctionsignature/maxlevels.md)
- [MTLIntersectionFunctionSignaturePrimitiveMotion](mtlintersectionfunctionsignature/primitivemotion.md)
- [MTLIntersectionFunctionSignatureUserData](mtlintersectionfunctionsignature/userdata.md)

## See Also

### Intersection function tables

- [MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md) — A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
- [MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md) — A specification of how to create an intersection function table.
- [MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md) — A description of an intersection function that performs an intersection test.
- [MTLIntersectionFunctionBufferArguments](mtlintersectionfunctionbufferarguments.md)
