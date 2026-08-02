---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/MetalKit.html
archived_at: '2026-07-18T02:53:10.366902Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# MetalKit Changes for Objective-C

### MetalKit (Added)

#### MTKModel.h (Added)

Added [MTKMesh](https://developer.apple.com/documentation/metalkit/mtkmesh)Added [-[MTKMesh initWithMesh:device:error:]](https://developer.apple.com/documentation/metalkit/mtkmesh/1535933-initwithmesh)Added [MTKMesh.name](https://developer.apple.com/documentation/metalkit/mtkmesh/1536038-name)Added [+[MTKMesh newMeshesFromAsset:device:sourceMeshes:error:]](https://developer.apple.com/documentation/metalkit/mtkmesh/1535934-newmeshesfromasset)Added [MTKMesh.submeshes](https://developer.apple.com/documentation/metalkit/mtkmesh/1535989-submeshes)Added [MTKMesh.vertexBuffers](https://developer.apple.com/documentation/metalkit/mtkmesh/1536021-vertexbuffers)Added [MTKMesh.vertexCount](https://developer.apple.com/documentation/metalkit/mtkmesh/1536023-vertexcount)Added [MTKMesh.vertexDescriptor](https://developer.apple.com/documentation/metalkit/mtkmesh/1535961-vertexdescriptor)Added [MTKMeshBuffer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer)Added [MTKMeshBuffer.allocator](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/1536029-allocator)Added [MTKMeshBuffer.buffer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/1535985-buffer)Added [MTKMeshBuffer.length](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/1535957-length)Added [MTKMeshBuffer.offset](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/1536040-offset)Added [MTKMeshBuffer.type](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/1535955-type)Added [MTKMeshBuffer.zone](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/1581386-zone)Added [MTKMeshBufferAllocator](https://developer.apple.com/documentation/metalkit/mtkmeshbufferallocator)Added [MTKMeshBufferAllocator.device](https://developer.apple.com/documentation/metalkit/mtkmeshbufferallocator/1535944-device)Added [-[MTKMeshBufferAllocator initWithDevice:]](https://developer.apple.com/documentation/metalkit/mtkmeshbufferallocator/1535959-init)Added [MTKSubmesh](https://developer.apple.com/documentation/metalkit/mtksubmesh)Added [MTKSubmesh.indexBuffer](https://developer.apple.com/documentation/metalkit/mtksubmesh/1535975-indexbuffer)Added [MTKSubmesh.indexCount](https://developer.apple.com/documentation/metalkit/mtksubmesh/1536009-indexcount)Added [MTKSubmesh.indexType](https://developer.apple.com/documentation/metalkit/mtksubmesh/1536033-indextype)Added [MTKSubmesh.mesh](https://developer.apple.com/documentation/metalkit/mtksubmesh/1535952-mesh)Added [MTKSubmesh.name](https://developer.apple.com/documentation/metalkit/mtksubmesh/1535953-name)Added [MTKSubmesh.primitiveType](https://developer.apple.com/documentation/metalkit/mtksubmesh/1535949-primitivetype)Added [MTKMetalVertexDescriptorFromModelIO()](https://developer.apple.com/documentation/metalkit/1535983-mtkmetalvertexdescriptorfrommode)Added [MTKMetalVertexFormatFromModelIO()](https://developer.apple.com/documentation/metalkit/1536013-mtkmetalvertexformatfrommodelio)Added [MTKModelErrorDomain](https://developer.apple.com/documentation/metalkit/mtkmodelerrordomain)Added [MTKModelErrorKey](https://developer.apple.com/documentation/metalkit/mtkmodelerrorkey)Added [MTKModelIOVertexDescriptorFromMetal()](https://developer.apple.com/documentation/metalkit/1535946-mtkmodeliovertexdescriptorfromme)Added [MTKModelIOVertexFormatFromMetal()](https://developer.apple.com/documentation/metalkit/1535945-mtkmodeliovertexformatfrommetal)

#### MTKTextureLoader.h (Added)

Added [MTKTextureLoader](https://developer.apple.com/documentation/metalkit/mtktextureloader)Added [MTKTextureLoader.device](https://developer.apple.com/documentation/metalkit/mtktextureloader/1536030-device)Added [-[MTKTextureLoader initWithDevice:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1536035-init)Added [-[MTKTextureLoader newTextureWithCGImage:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1536039-newtexture)Added [-[MTKTextureLoader newTextureWithCGImage:options:error:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1536028-newtexture)Added [-[MTKTextureLoader newTextureWithContentsOfURL:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1535939-newtexturewithcontentsofurl)Added [-[MTKTextureLoader newTextureWithContentsOfURL:options:error:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1535963-newtexturewithcontentsofurl)Added [-[MTKTextureLoader newTextureWithData:options:completionHandler:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1536031-newtexturewithdata)Added [-[MTKTextureLoader newTextureWithData:options:error:]](https://developer.apple.com/documentation/metalkit/mtktextureloader/1535951-newtexturewithdata)Added [MTKTextureLoaderCallback](https://developer.apple.com/documentation/metalkit/mtktextureloadercallback)Added [MTKTextureLoaderErrorDomain](https://developer.apple.com/documentation/metalkit/mtktextureloader/error/1535979-domain)Added [MTKTextureLoaderErrorKey](https://developer.apple.com/documentation/metalkit/mtktextureloadererrorkey)Added [MTKTextureLoaderOptionAllocateMipmaps](https://developer.apple.com/documentation/metalkit/mtktextureloaderoptionallocatemipmaps)Added [MTKTextureLoaderOptionSRGB](https://developer.apple.com/documentation/metalkit/mtktextureloaderoptionsrgb)Added [MTKTextureLoaderOptionTextureCPUCacheMode](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/1536022-texturecpucachemode)Added [MTKTextureLoaderOptionTextureUsage](https://developer.apple.com/documentation/metalkit/mtktextureloader/option/1536026-textureusage)

#### MTKView.h (Added)

Added [MTKView](https://developer.apple.com/documentation/metalkit/mtkview)Added [MTKView.autoResizeDrawable](https://developer.apple.com/documentation/metalkit/mtkview/1535938-autoresizedrawable)Added [MTKView.clearColor](https://developer.apple.com/documentation/metalkit/mtkview/1536036-clearcolor)Added [MTKView.clearDepth](https://developer.apple.com/documentation/metalkit/mtkview/1535987-cleardepth)Added [MTKView.clearStencil](https://developer.apple.com/documentation/metalkit/mtkview/1536042-clearstencil)Added [MTKView.colorPixelFormat](https://developer.apple.com/documentation/metalkit/mtkview/1535940-colorpixelformat)Added [MTKView.currentDrawable](https://developer.apple.com/documentation/metalkit/mtkview/1535971-currentdrawable)Added [MTKView.currentRenderPassDescriptor](https://developer.apple.com/documentation/metalkit/mtkview/1536024-currentrenderpassdescriptor)Added [MTKView.delegate](https://developer.apple.com/documentation/metalkit/mtkview/1535937-delegate)Added [MTKView.depthStencilPixelFormat](https://developer.apple.com/documentation/metalkit/mtkview/1536041-depthstencilpixelformat)Added [MTKView.depthStencilTexture](https://developer.apple.com/documentation/metalkit/mtkview/1535950-depthstenciltexture)Added [MTKView.device](https://developer.apple.com/documentation/metalkit/mtkview/1536011-device)Added [-[MTKView draw]](https://developer.apple.com/documentation/metalkit/mtkview/1535943-draw)Added [MTKView.drawableSize](https://developer.apple.com/documentation/metalkit/mtkview/1535969-drawablesize)Added [MTKView.enableSetNeedsDisplay](https://developer.apple.com/documentation/metalkit/mtkview/1535993-enablesetneedsdisplay)Added [MTKView.framebufferOnly](https://developer.apple.com/documentation/metalkit/mtkview/1535998-framebufferonly)Added [-[MTKView initWithCoder:]](https://developer.apple.com/documentation/metalkit/mtkview/1536037-init)Added [-[MTKView initWithFrame:device:]](https://developer.apple.com/documentation/metalkit/mtkview/1536018-initwithframe)Added [MTKView.multisampleColorTexture](https://developer.apple.com/documentation/metalkit/mtkview/1536020-multisamplecolortexture)Added [MTKView.paused](https://developer.apple.com/documentation/metalkit/mtkview/1535973-paused)Added [MTKView.preferredFramesPerSecond](https://developer.apple.com/documentation/metalkit/mtkview/1536027-preferredframespersecond)Added [MTKView.presentsWithTransaction](https://developer.apple.com/documentation/metalkit/mtkview/1535947-presentswithtransaction)Added [-[MTKView releaseDrawables]](https://developer.apple.com/documentation/metalkit/mtkview/1535948-releasedrawables)Added [MTKView.sampleCount](https://developer.apple.com/documentation/metalkit/mtkview/1535991-samplecount)Added [MTKViewDelegate](https://developer.apple.com/documentation/metalkit/mtkviewdelegate)Added [-[MTKViewDelegate drawInMTKView:]](https://developer.apple.com/documentation/metalkit/mtkviewdelegate/1535942-drawinmtkview)Added [-[MTKViewDelegate mtkView:drawableSizeWillChange:]](https://developer.apple.com/documentation/metalkit/mtkviewdelegate/1536015-mtkview)

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
