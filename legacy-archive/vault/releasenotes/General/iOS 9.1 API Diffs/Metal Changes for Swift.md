---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/Metal.html
archived_at: '2026-07-18T02:57:09.445146Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# Metal Changes for Swift

### Metal

Modified [MTLArgument](https://developer.apple.com/documentation/metal/mtlargument)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLArgumentAccess [enum]](https://developer.apple.com/documentation/metal/mtlargumentaccess)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLArgumentType [enum]](https://developer.apple.com/documentation/metal/mtlargumenttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLArrayType](https://developer.apple.com/documentation/metal/mtlarraytype)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLBlendFactor [enum]](https://developer.apple.com/documentation/metal/mtlblendfactor)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLBlendOperation [enum]](https://developer.apple.com/documentation/metal/mtlblendoperation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MTLBlitCommandEncoder : MTLCommandEncoder, NSObjectProtocol {     func synchronizeResource(_ resource: MTLResource)     func synchronizeTexture(_ texture: MTLTexture, slice slice: Int, level level: Int)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin, options options: MTLBlitOption)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int, options options: MTLBlitOption)     func generateMipmapsForTexture(_ texture: MTLTexture)     func fillBuffer(_ buffer: MTLBuffer, range range: NSRange, value value: UInt8)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, size size: Int) } ``` | MTLCommandEncoder, NSObjectProtocol |
| To | ``` protocol MTLBlitCommandEncoder : MTLCommandEncoder {     func synchronizeResource(_ resource: MTLResource)     func synchronizeTexture(_ texture: MTLTexture, slice slice: Int, level level: Int)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin, options options: MTLBlitOption)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int, options options: MTLBlitOption)     func generateMipmapsForTexture(_ texture: MTLTexture)     func fillBuffer(_ buffer: MTLBuffer, range range: NSRange, value value: UInt8)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, size size: Int) } ``` | MTLCommandEncoder |

Modified [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MTLBuffer : MTLResource, NSObjectProtocol {     var length: Int { get }     func contents() -> UnsafeMutablePointer<Void>     func didModifyRange(_ range: NSRange)     func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor, offset offset: Int, bytesPerRow bytesPerRow: Int) -> MTLTexture } ``` | MTLResource, NSObjectProtocol |
| To | ``` protocol MTLBuffer : MTLResource {     var length: Int { get }     func contents() -> UnsafeMutablePointer<Void>     func didModifyRange(_ range: NSRange)     func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor, offset offset: Int, bytesPerRow bytesPerRow: Int) -> MTLTexture } ``` | MTLResource |

Modified [MTLCommandBufferError [enum]](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/code)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLCommandBufferStatus [enum]](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLCompareFunction [enum]](https://developer.apple.com/documentation/metal/mtlcomparefunction)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLCompileOptions](https://developer.apple.com/documentation/metal/mtlcompileoptions)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MTLComputeCommandEncoder : MTLCommandEncoder, NSObjectProtocol {     func setComputePipelineState(_ state: MTLComputePipelineState)     func setBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setBufferOffset(_ offset: Int, atIndex index: Int)     func setBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange)     func setTexture(_ texture: MTLTexture?, atIndex index: Int)     func setTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setThreadgroupMemoryLength(_ length: Int, atIndex index: Int)     func dispatchThreadgroups(_ threadgroupsPerGrid: MTLSize, threadsPerThreadgroup threadsPerThreadgroup: MTLSize)     func dispatchThreadgroupsWithIndirectBuffer(_ indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int, threadsPerThreadgroup threadsPerThreadgroup: MTLSize) } ``` | MTLCommandEncoder, NSObjectProtocol |
| To | ``` protocol MTLComputeCommandEncoder : MTLCommandEncoder {     func setComputePipelineState(_ state: MTLComputePipelineState)     func setBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setBufferOffset(_ offset: Int, atIndex index: Int)     func setBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange)     func setTexture(_ texture: MTLTexture?, atIndex index: Int)     func setTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setThreadgroupMemoryLength(_ length: Int, atIndex index: Int)     func dispatchThreadgroups(_ threadgroupsPerGrid: MTLSize, threadsPerThreadgroup threadsPerThreadgroup: MTLSize)     func dispatchThreadgroupsWithIndirectBuffer(_ indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int, threadsPerThreadgroup threadsPerThreadgroup: MTLSize) } ``` | MTLCommandEncoder |

Modified [MTLComputePipelineDescriptor](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLComputePipelineReflection](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLCPUCacheMode [enum]](https://developer.apple.com/documentation/metal/mtlcpucachemode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLCullMode [enum]](https://developer.apple.com/documentation/metal/mtlcullmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLDataType [enum]](https://developer.apple.com/documentation/metal/mtldatatype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLDepthClipMode [enum]](https://developer.apple.com/documentation/metal/mtldepthclipmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLDepthStencilDescriptor](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLFeatureSet [enum]](https://developer.apple.com/documentation/metal/mtlfeatureset)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLFunctionType [enum]](https://developer.apple.com/documentation/metal/mtlfunctiontype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLIndexType [enum]](https://developer.apple.com/documentation/metal/mtlindextype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLLanguageVersion [enum]](https://developer.apple.com/documentation/metal/mtllanguageversion)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLLibraryError [enum]](https://developer.apple.com/documentation/metal/mtllibraryerror/code)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLLoadAction [enum]](https://developer.apple.com/documentation/metal/mtlloadaction)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLMultisampleDepthResolveFilter [enum]](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MTLParallelRenderCommandEncoder : MTLCommandEncoder, NSObjectProtocol {     func renderCommandEncoder() -> MTLRenderCommandEncoder } ``` | MTLCommandEncoder, NSObjectProtocol |
| To | ``` protocol MTLParallelRenderCommandEncoder : MTLCommandEncoder {     func renderCommandEncoder() -> MTLRenderCommandEncoder } ``` | MTLCommandEncoder |

Modified [MTLPixelFormat [enum]](https://developer.apple.com/documentation/metal/mtlpixelformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLPrimitiveType [enum]](https://developer.apple.com/documentation/metal/mtlprimitivetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLPurgeableState [enum]](https://developer.apple.com/documentation/metal/mtlpurgeablestate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MTLRenderCommandEncoder : MTLCommandEncoder, NSObjectProtocol {     func setRenderPipelineState(_ pipelineState: MTLRenderPipelineState)     func setVertexBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setVertexBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setVertexBufferOffset(_ offset: Int, atIndex index: Int)     func setVertexBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange)     func setVertexTexture(_ texture: MTLTexture?, atIndex index: Int)     func setVertexTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setViewport(_ viewport: MTLViewport)     func setFrontFacingWinding(_ frontFacingWinding: MTLWinding)     func setCullMode(_ cullMode: MTLCullMode)     func setDepthClipMode(_ depthClipMode: MTLDepthClipMode)     func setDepthBias(_ depthBias: Float, slopeScale slopeScale: Float, clamp clamp: Float)     func setScissorRect(_ rect: MTLScissorRect)     func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)     func setFragmentBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setFragmentBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setFragmentBufferOffset(_ offset: Int, atIndex index: Int)     func setFragmentBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offset: UnsafePointer<Int>, withRange range: NSRange)     func setFragmentTexture(_ texture: MTLTexture?, atIndex index: Int)     func setFragmentTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setBlendColorRed(_ red: Float, green green: Float, blue blue: Float, alpha alpha: Float)     func setDepthStencilState(_ depthStencilState: MTLDepthStencilState?)     func setStencilReferenceValue(_ referenceValue: UInt32)     func setStencilFrontReferenceValue(_ frontReferenceValue: UInt32, backReferenceValue backReferenceValue: UInt32)     func setVisibilityResultMode(_ mode: MTLVisibilityResultMode, offset offset: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int, baseInstance baseInstance: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int, baseVertex baseVertex: Int, baseInstance baseInstance: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int) } ``` | MTLCommandEncoder, NSObjectProtocol |
| To | ``` protocol MTLRenderCommandEncoder : MTLCommandEncoder {     func setRenderPipelineState(_ pipelineState: MTLRenderPipelineState)     func setVertexBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setVertexBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setVertexBufferOffset(_ offset: Int, atIndex index: Int)     func setVertexBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange)     func setVertexTexture(_ texture: MTLTexture?, atIndex index: Int)     func setVertexTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setViewport(_ viewport: MTLViewport)     func setFrontFacingWinding(_ frontFacingWinding: MTLWinding)     func setCullMode(_ cullMode: MTLCullMode)     func setDepthClipMode(_ depthClipMode: MTLDepthClipMode)     func setDepthBias(_ depthBias: Float, slopeScale slopeScale: Float, clamp clamp: Float)     func setScissorRect(_ rect: MTLScissorRect)     func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)     func setFragmentBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setFragmentBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setFragmentBufferOffset(_ offset: Int, atIndex index: Int)     func setFragmentBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offset: UnsafePointer<Int>, withRange range: NSRange)     func setFragmentTexture(_ texture: MTLTexture?, atIndex index: Int)     func setFragmentTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setBlendColorRed(_ red: Float, green green: Float, blue blue: Float, alpha alpha: Float)     func setDepthStencilState(_ depthStencilState: MTLDepthStencilState?)     func setStencilReferenceValue(_ referenceValue: UInt32)     func setStencilFrontReferenceValue(_ frontReferenceValue: UInt32, backReferenceValue backReferenceValue: UInt32)     func setVisibilityResultMode(_ mode: MTLVisibilityResultMode, offset offset: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int, baseInstance baseInstance: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int, baseVertex baseVertex: Int, baseInstance baseInstance: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int) } ``` | MTLCommandEncoder |

Modified [MTLRenderPassAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLRenderPassColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLRenderPassColorAttachmentDescriptorArray](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLRenderPassDepthAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLRenderPassStencilAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassstencilattachmentdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLRenderPipelineColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLRenderPipelineColorAttachmentDescriptorArray](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified MTLRenderPipelineError [enum]

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLRenderPipelineReflection](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLSamplerAddressMode [enum]](https://developer.apple.com/documentation/metal/mtlsampleraddressmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLSamplerDescriptor](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLSamplerMinMagFilter [enum]](https://developer.apple.com/documentation/metal/mtlsamplerminmagfilter)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLSamplerMipFilter [enum]](https://developer.apple.com/documentation/metal/mtlsamplermipfilter)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLStencilDescriptor](https://developer.apple.com/documentation/metal/mtlstencildescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLStencilOperation [enum]](https://developer.apple.com/documentation/metal/mtlstenciloperation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLStorageMode [enum]](https://developer.apple.com/documentation/metal/mtlstoragemode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLStoreAction [enum]](https://developer.apple.com/documentation/metal/mtlstoreaction)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLStructMember](https://developer.apple.com/documentation/metal/mtlstructmember)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLStructType](https://developer.apple.com/documentation/metal/mtlstructtype)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MTLTexture : MTLResource, NSObjectProtocol {     var rootResource: MTLResource? { get }     var parentTexture: MTLTexture? { get }     var parentRelativeLevel: Int { get }     var parentRelativeSlice: Int { get }     var buffer: MTLBuffer? { get }     var bufferOffset: Int { get }     var bufferBytesPerRow: Int { get }     var textureType: MTLTextureType { get }     var pixelFormat: MTLPixelFormat { get }     var width: Int { get }     var height: Int { get }     var depth: Int { get }     var mipmapLevelCount: Int { get }     var sampleCount: Int { get }     var arrayLength: Int { get }     var usage: MTLTextureUsage { get }     var framebufferOnly: Bool { get }     func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int, fromRegion region: MTLRegion, mipmapLevel level: Int, slice slice: Int)     func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, slice slice: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int)     func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, fromRegion region: MTLRegion, mipmapLevel level: Int)     func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int)     func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat) -> MTLTexture     func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat, textureType textureType: MTLTextureType, levels levelRange: NSRange, slices sliceRange: NSRange) -> MTLTexture } ``` | MTLResource, NSObjectProtocol |
| To | ``` protocol MTLTexture : MTLResource {     var rootResource: MTLResource? { get }     var parentTexture: MTLTexture? { get }     var parentRelativeLevel: Int { get }     var parentRelativeSlice: Int { get }     var buffer: MTLBuffer? { get }     var bufferOffset: Int { get }     var bufferBytesPerRow: Int { get }     var textureType: MTLTextureType { get }     var pixelFormat: MTLPixelFormat { get }     var width: Int { get }     var height: Int { get }     var depth: Int { get }     var mipmapLevelCount: Int { get }     var sampleCount: Int { get }     var arrayLength: Int { get }     var usage: MTLTextureUsage { get }     var framebufferOnly: Bool { get }     func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int, fromRegion region: MTLRegion, mipmapLevel level: Int, slice slice: Int)     func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, slice slice: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int)     func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, fromRegion region: MTLRegion, mipmapLevel level: Int)     func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int)     func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat) -> MTLTexture     func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat, textureType textureType: MTLTextureType, levels levelRange: NSRange, slices sliceRange: NSRange) -> MTLTexture } ``` | MTLResource |

Modified [MTLTextureDescriptor](https://developer.apple.com/documentation/metal/mtltexturedescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLTextureType [enum]](https://developer.apple.com/documentation/metal/mtltexturetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLTriangleFillMode [enum]](https://developer.apple.com/documentation/metal/mtltrianglefillmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLVertexAttribute](https://developer.apple.com/documentation/metal/mtlvertexattribute)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLVertexAttributeDescriptor](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLVertexAttributeDescriptorArray](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLVertexBufferLayoutDescriptor](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLVertexBufferLayoutDescriptorArray](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MTLVertexDescriptor](https://developer.apple.com/documentation/metal/mtlvertexdescriptor)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MTLVertexFormat [enum]](https://developer.apple.com/documentation/metal/mtlvertexformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLVertexStepFunction [enum]](https://developer.apple.com/documentation/metal/mtlvertexstepfunction)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLVisibilityResultMode [enum]](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MTLWinding [enum]](https://developer.apple.com/documentation/metal/mtlwinding)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

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
