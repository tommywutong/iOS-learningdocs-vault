---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/MetalKit.html
archived_at: '2026-07-18T02:57:09.553279Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# MetalKit Changes for Swift

### MetalKit

Modified [MTKMesh](https://developer.apple.com/documentation/metalkit/mtkmesh)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTKMeshBuffer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTKMeshBuffer : NSObject, MDLMeshBuffer, NSCopying {     init()     var length: Int { get }     var allocator: MTKMeshBufferAllocator { get }     var buffer: MTLBuffer { get }     var offset: Int { get }     var type: MDLMeshBufferType { get }     func zone() -> MDLMeshBufferZone? } ``` | AnyObject, MDLMeshBuffer, NSCopying, NSObjectProtocol |
| To | ``` class MTKMeshBuffer : NSObject, MDLMeshBuffer {     init()     var length: Int { get }     var allocator: MTKMeshBufferAllocator { get }     var buffer: MTLBuffer { get }     var offset: Int { get }     var type: MDLMeshBufferType { get }     func zone() -> MDLMeshBufferZone? } ``` | MDLMeshBuffer |

Modified [MTKMeshBufferAllocator](https://developer.apple.com/documentation/metalkit/mtkmeshbufferallocator)

|  | Protocols |
| --- | --- |
| From | AnyObject, MDLMeshBufferAllocator, NSObjectProtocol |
| To | MDLMeshBufferAllocator |

Modified [MTKSubmesh](https://developer.apple.com/documentation/metalkit/mtksubmesh)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTKTextureLoader](https://developer.apple.com/documentation/metalkit/mtktextureloader)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTKView](https://developer.apple.com/documentation/metalkit/mtkview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTKView : UIView {     init(frame frameRect: CGRect, device device: MTLDevice?)     init(coder coder: NSCoder)     weak var delegate: MTKViewDelegate?     var device: MTLDevice?     var currentDrawable: CAMetalDrawable? { get }     var framebufferOnly: Bool     var presentsWithTransaction: Bool     var colorPixelFormat: MTLPixelFormat     var depthStencilPixelFormat: MTLPixelFormat     var sampleCount: Int     var clearColor: MTLClearColor     var clearDepth: Double     var clearStencil: UInt32     var depthStencilTexture: MTLTexture? { get }     var multisampleColorTexture: MTLTexture? { get }     func releaseDrawables()     var currentRenderPassDescriptor: MTLRenderPassDescriptor? { get }     var preferredFramesPerSecond: Int     var enableSetNeedsDisplay: Bool     var autoResizeDrawable: Bool     var drawableSize: CGSize     var paused: Bool     func draw() } ``` | AnyObject, NSCoding |
| To | ``` class MTKView : UIView, NSCoding {     init(frame frameRect: CGRect, device device: MTLDevice?)     init(coder coder: NSCoder)     weak var delegate: MTKViewDelegate?     var device: MTLDevice?     var currentDrawable: CAMetalDrawable? { get }     var framebufferOnly: Bool     var presentsWithTransaction: Bool     var colorPixelFormat: MTLPixelFormat     var depthStencilPixelFormat: MTLPixelFormat     var sampleCount: Int     var clearColor: MTLClearColor     var clearDepth: Double     var clearStencil: UInt32     var depthStencilTexture: MTLTexture? { get }     var multisampleColorTexture: MTLTexture? { get }     func releaseDrawables()     var currentRenderPassDescriptor: MTLRenderPassDescriptor? { get }     var preferredFramesPerSecond: Int     var enableSetNeedsDisplay: Bool     var autoResizeDrawable: Bool     var drawableSize: CGSize     var paused: Bool     func draw() } ``` | NSCoding |

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
