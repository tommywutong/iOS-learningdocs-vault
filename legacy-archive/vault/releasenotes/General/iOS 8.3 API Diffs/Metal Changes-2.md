---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/Metal.html
archived_at: '2026-07-18T02:56:26.933614Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# Metal Changes

## Metal

Added MTLClearColor.init()Added MTLClearColor.init(red: Double, green: Double, blue: Double, alpha: Double)Added MTLComputeCommandEncoder.setBufferOffset(Int, atIndex: Int)Added MTLComputeCommandEncoder.setBytes(UnsafePointer<Void>, length: Int, atIndex: Int)Added MTLOrigin.init()Added MTLOrigin.init(x: Int, y: Int, z: Int)Added MTLRegion.init()Added MTLRegion.init(origin: MTLOrigin, size: MTLSize)Added MTLRenderCommandEncoder.setFragmentBufferOffset(Int, atIndex: Int)Added MTLRenderCommandEncoder.setFragmentBytes(UnsafePointer<Void>, length: Int, atIndex: Int)Added MTLRenderCommandEncoder.setVertexBufferOffset(Int, atIndex: Int)Added MTLRenderCommandEncoder.setVertexBytes(UnsafePointer<Void>, length: Int, atIndex: Int)Added MTLScissorRect.init()Added MTLScissorRect.init(x: Int, y: Int, width: Int, height: Int)Added MTLSize.init()Added MTLSize.init(width: Int, height: Int, depth: Int)Added MTLVertexAttribute.attributeTypeAdded MTLViewport.init()Added MTLViewport.init(originX: Double, originY: Double, width: Double, height: Double, znear: Double, zfar: Double)Modified MTLClearColor [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTLClearColor {     var red: Double     var green: Double     var blue: Double     var alpha: Double } ``` |
| To | ``` struct MTLClearColor {     var red: Double     var green: Double     var blue: Double     var alpha: Double     init()     init(red red: Double, green green: Double, blue blue: Double, alpha alpha: Double) } ``` |

Modified MTLOrigin [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTLOrigin {     var x: Int     var y: Int     var z: Int } ``` |
| To | ``` struct MTLOrigin {     var x: Int     var y: Int     var z: Int     init()     init(x x: Int, y y: Int, z z: Int) } ``` |

Modified MTLRegion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTLRegion {     var origin: MTLOrigin     var size: MTLSize } ``` |
| To | ``` struct MTLRegion {     var origin: MTLOrigin     var size: MTLSize     init()     init(origin origin: MTLOrigin, size size: MTLSize) } ``` |

Modified MTLScissorRect [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTLScissorRect {     var x: Int     var y: Int     var width: Int     var height: Int } ``` |
| To | ``` struct MTLScissorRect {     var x: Int     var y: Int     var width: Int     var height: Int     init()     init(x x: Int, y y: Int, width width: Int, height height: Int) } ``` |

Modified MTLSize [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTLSize {     var width: Int     var height: Int     var depth: Int } ``` |
| To | ``` struct MTLSize {     var width: Int     var height: Int     var depth: Int     init()     init(width width: Int, height height: Int, depth depth: Int) } ``` |

Modified MTLViewport [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MTLViewport {     var originX: Double     var originY: Double     var width: Double     var height: Double     var znear: Double     var zfar: Double } ``` |
| To | ``` struct MTLViewport {     var originX: Double     var originY: Double     var width: Double     var height: Double     var znear: Double     var zfar: Double     init()     init(originX originX: Double, originY originY: Double, width width: Double, height height: Double, znear znear: Double, zfar zfar: Double) } ``` |

Modified MTLCommandBufferErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let MTLCommandBufferErrorDomain: NSString! ``` |
| To | ``` let MTLCommandBufferErrorDomain: String ``` |

Modified MTLLibraryErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let MTLLibraryErrorDomain: NSString! ``` |
| To | ``` let MTLLibraryErrorDomain: String ``` |

Modified MTLRenderPipelineErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let MTLRenderPipelineErrorDomain: NSString! ``` |
| To | ``` let MTLRenderPipelineErrorDomain: String ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
