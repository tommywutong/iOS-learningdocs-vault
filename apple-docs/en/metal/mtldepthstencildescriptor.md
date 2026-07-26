---
title: MTLDepthStencilDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldepthstencildescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtldepthstencildescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldepthstencildescriptor.json'
content_hash: 'sha256:46050e8bf7a5b74f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDepthStencilDescriptor

<sub>Class</sub>

An instance that configures new [MTLDepthStencilState](mtldepthstencilstate.md) instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLDepthStencilDescriptor
```

## Overview

An [MTLDepthStencilDescriptor](mtldepthstencildescriptor.md) instance is used to define a specific configuration of the depth and stencil stages of a rendering pipeline. To create an [MTLDepthStencilDescriptor](mtldepthstencildescriptor.md) instance, use standard allocation and initialization techniques.

To enable writing the depth value to a depth attachment, set the depthWriteEnabled property to [true](../swift/true.md).

The depthCompareFunction property specifies how the depth test is performed. If a fragment’s depth value fails the depth test, the fragment is discarded. [MTLCompareFunctionLess](mtlcomparefunction/less.md) is a commonly used value for [depthCompareFunction](mtldepthstencildescriptor/depthcomparefunction.md), because fragment values that are farther away from the viewer than the pixel depth value (a previously written fragment) fail the depth test and are considered occluded by the earlier depth value.

The [frontFaceStencil](mtldepthstencildescriptor/frontfacestencil.md) and [backFaceStencil](mtldepthstencildescriptor/backfacestencil.md) properties define two independent stencil descriptors: one for front-facing primitives and the other for back-facing primitives, respectively. Both properties can be set to the same MTLStencilDescriptor instance.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying depth operations

- [depthCompareFunction](mtldepthstencildescriptor/depthcomparefunction.md) — The comparison that is performed between a fragment’s depth value and the depth value in the attachment, which determines whether to discard the fragment.
- [depthWriteEnabled](mtldepthstencildescriptor/isdepthwriteenabled.md) — A Boolean value that indicates whether depth values can be written to the depth attachment.

### Specifying stencil descriptors for primitives

- [backFaceStencil](mtldepthstencildescriptor/backfacestencil.md) — The stencil descriptor for back-facing primitives.
- [frontFaceStencil](mtldepthstencildescriptor/frontfacestencil.md) — The stencil descriptor for front-facing primitives.

### Identifying properties

- [label](mtldepthstencildescriptor/label.md) — A string that identifies this object.

## See Also

### Depth testing

- [Calculating primitive visibility using depth testing](calculating-primitive-visibility-using-depth-testing.md) — Determine which pixels are visible in a scene by using a depth texture.
- [MTLDepthStencilState](mtldepthstencilstate.md) — A depth and stencil state instance that specifies the depth and stencil configuration and operations used in a render pass.
- [MTLStencilDescriptor](mtlstencildescriptor.md) — An object that defines the front-facing or back-facing stencil operations of a depth and stencil state object.
