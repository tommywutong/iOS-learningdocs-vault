---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/Metal.html
archived_at: '2026-07-18T02:56:55.073634Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Metal Changes for Swift

### Metal

Removed MTLColorWriteMask.init(_: UInt)Removed MTLPipelineOption.init(_: UInt)Removed MTLResourceOptions.init(_: UInt)Added [MTLBlitCommandEncoder.copyFromBuffer(_: MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, toTexture: MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin, options: MTLBlitOption)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400771-copyfrombuffer)Added [MTLBlitCommandEncoder.copyFromTexture(_: MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, toBuffer: MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int, options: MTLBlitOption)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400756-copy)Added [MTLBlitOption [struct]](https://developer.apple.com/documentation/metal/mtlblitoption)Added [MTLBlitOption.DepthFromDepthStencil](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptiondepthfromdepthstencil)Added MTLBlitOption.init(rawValue: UInt)Added [MTLBlitOption.None](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptionnone)Added [MTLBlitOption.RowLinearPVRTC](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptionrowlinearpvrtc)Added [MTLBlitOption.StencilFromDepthStencil](https://developer.apple.com/documentation/metal/mtlblitoption/1400759-stencilfromdepthstencil)Added [MTLCompileOptions.languageVersion](https://developer.apple.com/documentation/metal/mtlcompileoptions/1515494-languageversion)Added [MTLComputeCommandEncoder.dispatchThreadgroupsWithIndirectBuffer(_: MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443157-dispatchthreadgroupswithindirect)Added [MTLComputePipelineDescriptor](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor)Added [MTLComputePipelineDescriptor.computeFunction](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/1414917-computefunction)Added [MTLComputePipelineDescriptor.label](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/1414918-label)Added [MTLComputePipelineDescriptor.reset()](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/1414923-reset)Added [MTLComputePipelineDescriptor.threadGroupSizeIsMultipleOfThreadExecutionWidth](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/1414915-threadgroupsizeismultipleofthrea)Added [MTLDepthClipMode [enum]](https://developer.apple.com/documentation/metal/mtldepthclipmode)Added [MTLDepthClipMode.Clamp](https://developer.apple.com/documentation/metal/mtldepthclipmode/clamp)Added [MTLDepthClipMode.Clip](https://developer.apple.com/documentation/metal/mtldepthclipmode/mtldepthclipmodeclip)Added [MTLDevice.maxThreadsPerThreadgroup](https://developer.apple.com/documentation/metal/mtldevice/1433393-maxthreadsperthreadgroup)Added [MTLDevice.newComputePipelineStateWithDescriptor(_: MTLComputePipelineDescriptor, options: MTLPipelineOption, completionHandler: MTLNewComputePipelineStateWithReflectionCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433403-makecomputepipelinestate)Added [MTLDevice.newComputePipelineStateWithDescriptor(_: MTLComputePipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>) throws -> MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtldevice/1433353-newcomputepipelinestatewithdescr)Added [MTLDevice.supportsTextureSampleCount(_: Int) -> Bool](https://developer.apple.com/documentation/metal/mtldevice/1433355-supportstexturesamplecount)Added [MTLDispatchThreadgroupsIndirectArguments [struct]](https://developer.apple.com/documentation/metal/mtldispatchthreadgroupsindirectarguments)Added MTLDispatchThreadgroupsIndirectArguments.init()Added MTLDispatchThreadgroupsIndirectArguments.init(threadgroupsPerGrid: (UInt32, UInt32, UInt32))Added [MTLDispatchThreadgroupsIndirectArguments.threadgroupsPerGrid](https://developer.apple.com/documentation/metal/mtldispatchthreadgroupsindirectarguments/1443132-threadgroupspergrid)Added [MTLDrawIndexedPrimitivesIndirectArguments [struct]](https://developer.apple.com/documentation/metal/mtldrawindexedprimitivesindirectarguments)Added [MTLDrawIndexedPrimitivesIndirectArguments.baseInstance](https://developer.apple.com/documentation/metal/mtldrawindexedprimitivesindirectarguments/1516255-baseinstance)Added [MTLDrawIndexedPrimitivesIndirectArguments.baseVertex](https://developer.apple.com/documentation/metal/mtldrawindexedprimitivesindirectarguments/1515837-basevertex)Added [MTLDrawIndexedPrimitivesIndirectArguments.indexCount](https://developer.apple.com/documentation/metal/mtldrawindexedprimitivesindirectarguments/1515431-indexcount)Added [MTLDrawIndexedPrimitivesIndirectArguments.indexStart](https://developer.apple.com/documentation/metal/mtldrawindexedprimitivesindirectarguments/1515492-indexstart)Added MTLDrawIndexedPrimitivesIndirectArguments.init()Added MTLDrawIndexedPrimitivesIndirectArguments.init(indexCount: UInt32, instanceCount: UInt32, indexStart: UInt32, baseVertex: Int32, baseInstance: UInt32)Added [MTLDrawIndexedPrimitivesIndirectArguments.instanceCount](https://developer.apple.com/documentation/metal/mtldrawindexedprimitivesindirectarguments/1515432-instancecount)Added [MTLDrawPrimitivesIndirectArguments [struct]](https://developer.apple.com/documentation/metal/mtldrawprimitivesindirectarguments)Added [MTLDrawPrimitivesIndirectArguments.baseInstance](https://developer.apple.com/documentation/metal/mtldrawprimitivesindirectarguments/1515718-baseinstance)Added MTLDrawPrimitivesIndirectArguments.init()Added MTLDrawPrimitivesIndirectArguments.init(vertexCount: UInt32, instanceCount: UInt32, vertexStart: UInt32, baseInstance: UInt32)Added [MTLDrawPrimitivesIndirectArguments.instanceCount](https://developer.apple.com/documentation/metal/mtldrawprimitivesindirectarguments/1515739-instancecount)Added [MTLDrawPrimitivesIndirectArguments.vertexCount](https://developer.apple.com/documentation/metal/mtldrawprimitivesindirectarguments/1515487-vertexcount)Added [MTLDrawPrimitivesIndirectArguments.vertexStart](https://developer.apple.com/documentation/metal/mtldrawprimitivesindirectarguments/1515992-vertexstart)Added [MTLFeatureSet.iOS_GPUFamily1_v1](https://developer.apple.com/documentation/metal/mtlfeatureset/ios_gpufamily1_v1)Added [MTLFeatureSet.iOS_GPUFamily1_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/ios_gpufamily1_v2)Added [MTLFeatureSet.iOS_GPUFamily2_v1](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_ios_gpufamily2_v1)Added [MTLFeatureSet.iOS_GPUFamily2_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_ios_gpufamily2_v2)Added [MTLFeatureSet.iOS_GPUFamily3_v1](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_ios_gpufamily3_v1)Added [MTLLanguageVersion [enum]](https://developer.apple.com/documentation/metal/mtllanguageversion)Added [MTLLanguageVersion.Version1_0](https://developer.apple.com/documentation/metal/mtllanguageversion/version1_0)Added [MTLLanguageVersion.Version1_1](https://developer.apple.com/documentation/metal/mtllanguageversion/version1_1)Added [MTLMultisampleDepthResolveFilter [enum]](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter)Added [MTLMultisampleDepthResolveFilter.Max](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter/mtlmultisampledepthresolvefiltermax)Added [MTLMultisampleDepthResolveFilter.Min](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter/mtlmultisampledepthresolvefiltermin)Added [MTLMultisampleDepthResolveFilter.Sample0](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter/mtlmultisampledepthresolvefiltersample0)Added [MTLPixelFormat.BGR5A1Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr5a1unorm)Added [MTLPixelFormat.Depth32Float_Stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/depth32float_stencil8)Added [MTLRenderCommandEncoder.drawIndexedPrimitives(_: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLBuffer, indexBufferOffset: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515520-drawindexedprimitives)Added [MTLRenderCommandEncoder.drawIndexedPrimitives(_: MTLPrimitiveType, indexType: MTLIndexType, indexBuffer: MTLBuffer, indexBufferOffset: Int, indirectBuffer: MTLBuffer, indirectBufferOffset: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515392-drawindexedprimitives)Added [MTLRenderCommandEncoder.drawPrimitives(_: MTLPrimitiveType, indirectBuffer: MTLBuffer, indirectBufferOffset: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515467-drawprimitives)Added [MTLRenderCommandEncoder.drawPrimitives(_: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515561-drawprimitives)Added [MTLRenderCommandEncoder.setDepthClipMode(_: MTLDepthClipMode)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516267-setdepthclipmode)Added [MTLRenderCommandEncoder.setStencilFrontReferenceValue(_: UInt32, backReferenceValue: UInt32)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515522-setstencilreferencevalues)Added [MTLRenderPassDepthAttachmentDescriptor.depthResolveFilter](https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor/1619184-depthresolvefilter)Added [MTLResource.storageMode](https://developer.apple.com/documentation/metal/mtlresource/1515477-storagemode)Added [MTLResourceOptions.CPUCacheModeDefaultCache](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcecpucachemodedefaultcache)Added [MTLResourceOptions.CPUCacheModeWriteCombined](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcecpucachemodewritecombined)Added [MTLResourceOptions.StorageModePrivate](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcestoragemodeprivate)Added [MTLResourceOptions.StorageModeShared](https://developer.apple.com/documentation/metal/mtlresourceoptions/1515613-storagemodeshared)Added [MTLSamplerDescriptor.compareFunction](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/1516001-comparefunction)Added [MTLSamplerDescriptor.lodAverage](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/1615844-lodaverage)Added [MTLStorageMode [enum]](https://developer.apple.com/documentation/metal/mtlstoragemode)Added [MTLStorageMode.Private](https://developer.apple.com/documentation/metal/mtlstoragemode/private)Added [MTLStorageMode.Shared](https://developer.apple.com/documentation/metal/mtlstoragemode/mtlstoragemodeshared)Added [MTLTexture.buffer](https://developer.apple.com/documentation/metal/mtltexture/1619090-buffer)Added [MTLTexture.bufferBytesPerRow](https://developer.apple.com/documentation/metal/mtltexture/1619175-bufferbytesperrow)Added [MTLTexture.bufferOffset](https://developer.apple.com/documentation/metal/mtltexture/1619019-bufferoffset)Added [MTLTexture.newTextureViewWithPixelFormat(_: MTLPixelFormat, textureType: MTLTextureType, levels: NSRange, slices: NSRange) -> MTLTexture](https://developer.apple.com/documentation/metal/mtltexture/1515409-newtextureviewwithpixelformat)Added [MTLTexture.parentRelativeLevel](https://developer.apple.com/documentation/metal/mtltexture/1516265-parentrelativelevel)Added [MTLTexture.parentRelativeSlice](https://developer.apple.com/documentation/metal/mtltexture/1516221-parentrelativeslice)Added [MTLTexture.parentTexture](https://developer.apple.com/documentation/metal/mtltexture/1515372-parenttexture)Added [MTLTexture.usage](https://developer.apple.com/documentation/metal/mtltexture/1515763-usage)Added [MTLTextureDescriptor.cpuCacheMode](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515375-cpucachemode)Added [MTLTextureDescriptor.storageMode](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516262-storagemode)Added [MTLTextureDescriptor.usage](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515783-usage)Added [MTLTextureUsage [struct]](https://developer.apple.com/documentation/metal/mtltextureusage)Added MTLTextureUsage.init(rawValue: UInt)Added [MTLTextureUsage.PixelFormatView](https://developer.apple.com/documentation/metal/mtltextureusage/1516223-pixelformatview)Added [MTLTextureUsage.RenderTarget](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusagerendertarget)Added [MTLTextureUsage.ShaderRead](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusageshaderread)Added [MTLTextureUsage.ShaderWrite](https://developer.apple.com/documentation/metal/mtltextureusage/1515854-shaderwrite)Added [MTLTextureUsage.Unknown](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusageunknown)Added [MTLVisibilityResultMode.Counting](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/counting)Added [MTLAutoreleasedComputePipelineReflection](https://developer.apple.com/documentation/metal/mtlautoreleasedcomputepipelinereflection)Added [MTLAutoreleasedRenderPipelineReflection](https://developer.apple.com/documentation/metal/mtlautoreleasedrenderpipelinereflection)Added [MTLNewComputePipelineStateCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewcomputepipelinestatecompletionhandler)Added [MTLNewComputePipelineStateWithReflectionCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewcomputepipelinestatewithreflectioncompletionhandler)Added [MTLNewLibraryCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewlibrarycompletionhandler)Added [MTLNewRenderPipelineStateCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatecompletionhandler)Added [MTLNewRenderPipelineStateWithReflectionCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatewithreflectioncompletionhandler)Added MTLResourceCPUCacheModeShiftAdded MTLResourceStorageModeShiftModified [MTLArgument](https://developer.apple.com/documentation/metal/mtlargument)

|  | Declaration |
| --- | --- |
| From | ``` class MTLArgument : NSObject {     var name: String { get }     var type: MTLArgumentType { get }     var access: MTLArgumentAccess { get }     var index: Int { get }     var active: Bool { get }     var bufferAlignment: Int { get }     var bufferDataSize: Int { get }     var bufferDataType: MTLDataType { get }     var bufferStructType: MTLStructType? { get }     var threadgroupMemoryAlignment: Int { get }     var threadgroupMemoryDataSize: Int { get }     var textureType: MTLTextureType { get }     var textureDataType: MTLDataType { get } } ``` |
| To | ``` class MTLArgument : NSObject {     var name: String { get }     var type: MTLArgumentType { get }     var access: MTLArgumentAccess { get }     var index: Int { get }     var active: Bool { get }     var bufferAlignment: Int { get }     var bufferDataSize: Int { get }     var bufferDataType: MTLDataType { get }     var bufferStructType: MTLStructType { get }     var threadgroupMemoryAlignment: Int { get }     var threadgroupMemoryDataSize: Int { get }     var textureType: MTLTextureType { get }     var textureDataType: MTLDataType { get } } ``` |

Modified [MTLArgument.bufferStructType](https://developer.apple.com/documentation/metal/mtlargument/1462041-bufferstructtype)

|  | Declaration |
| --- | --- |
| From | ``` var bufferStructType: MTLStructType? { get } ``` |
| To | ``` var bufferStructType: MTLStructType { get } ``` |

Modified [MTLArgumentAccess [enum]](https://developer.apple.com/documentation/metal/mtlargumentaccess)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLArgumentType [enum]](https://developer.apple.com/documentation/metal/mtlargumenttype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLBlendFactor [enum]](https://developer.apple.com/documentation/metal/mtlblendfactor)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLBlendOperation [enum]](https://developer.apple.com/documentation/metal/mtlblendoperation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLBlitCommandEncoder : MTLCommandEncoder, NSObjectProtocol {     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int)     func generateMipmapsForTexture(_ texture: MTLTexture)     func fillBuffer(_ buffer: MTLBuffer, range range: NSRange, value value: UInt8)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, size size: Int) } ``` |
| To | ``` protocol MTLBlitCommandEncoder : MTLCommandEncoder, NSObjectProtocol {     func synchronizeResource(_ resource: MTLResource)     func synchronizeTexture(_ texture: MTLTexture, slice slice: Int, level level: Int)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin, options options: MTLBlitOption)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int, options options: MTLBlitOption)     func generateMipmapsForTexture(_ texture: MTLTexture)     func fillBuffer(_ buffer: MTLBuffer, range range: NSRange, value value: UInt8)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, size size: Int) } ``` |

Modified [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLBuffer : MTLResource, NSObjectProtocol {     var length: Int { get }     func contents() -> UnsafeMutablePointer<Void>     func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor, offset offset: Int, bytesPerRow bytesPerRow: Int) -> MTLTexture? } ``` |
| To | ``` protocol MTLBuffer : MTLResource, NSObjectProtocol {     var length: Int { get }     func contents() -> UnsafeMutablePointer<Void>     func didModifyRange(_ range: NSRange)     func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor, offset offset: Int, bytesPerRow bytesPerRow: Int) -> MTLTexture } ``` |

Modified [MTLBuffer.newTextureWithDescriptor(_: MTLTextureDescriptor, offset: Int, bytesPerRow: Int) -> MTLTexture](https://developer.apple.com/documentation/metal/mtlbuffer/1613852-newtexturewithdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor, offset offset: Int, bytesPerRow bytesPerRow: Int) -> MTLTexture? ``` |
| To | ``` func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor, offset offset: Int, bytesPerRow bytesPerRow: Int) -> MTLTexture ``` |

Modified [MTLColorWriteMask [struct]](https://developer.apple.com/documentation/metal/mtlcolorwritemask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MTLColorWriteMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: MTLColorWriteMask { get }     static var Red: MTLColorWriteMask { get }     static var Green: MTLColorWriteMask { get }     static var Blue: MTLColorWriteMask { get }     static var Alpha: MTLColorWriteMask { get }     static var All: MTLColorWriteMask { get } } ``` | RawOptionSetType |
| To | ``` struct MTLColorWriteMask : OptionSetType {     init(rawValue rawValue: UInt)     static var None: MTLColorWriteMask { get }     static var Red: MTLColorWriteMask { get }     static var Green: MTLColorWriteMask { get }     static var Blue: MTLColorWriteMask { get }     static var Alpha: MTLColorWriteMask { get }     static var All: MTLColorWriteMask { get } } ``` | OptionSetType |

Modified [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLCommandBuffer : NSObjectProtocol {     var device: MTLDevice { get }     var commandQueue: MTLCommandQueue { get }     var retainedReferences: Bool { get }     var label: String? { get set }     func enqueue()     func commit()     func addScheduledHandler(_ block: MTLCommandBufferHandler)     func presentDrawable(_ drawable: MTLDrawable)     func presentDrawable(_ drawable: MTLDrawable, atTime presentationTime: CFTimeInterval)     func waitUntilScheduled()     func addCompletedHandler(_ block: MTLCommandBufferHandler)     func waitUntilCompleted()     var status: MTLCommandBufferStatus { get }     var error: NSError? { get }     func blitCommandEncoder() -> MTLBlitCommandEncoder     func renderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder?     func computeCommandEncoder() -> MTLComputeCommandEncoder     func parallelRenderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder? } ``` |
| To | ``` protocol MTLCommandBuffer : NSObjectProtocol {     var device: MTLDevice { get }     var commandQueue: MTLCommandQueue { get }     var retainedReferences: Bool { get }     var label: String? { get set }     func enqueue()     func commit()     func addScheduledHandler(_ block: MTLCommandBufferHandler)     func presentDrawable(_ drawable: MTLDrawable)     func presentDrawable(_ drawable: MTLDrawable, atTime presentationTime: CFTimeInterval)     func waitUntilScheduled()     func addCompletedHandler(_ block: MTLCommandBufferHandler)     func waitUntilCompleted()     var status: MTLCommandBufferStatus { get }     var error: NSError? { get }     func blitCommandEncoder() -> MTLBlitCommandEncoder     func renderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder     func computeCommandEncoder() -> MTLComputeCommandEncoder     func parallelRenderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder } ``` |

Modified [MTLCommandBuffer.parallelRenderCommandEncoderWithDescriptor(_: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443009-parallelrendercommandencoderwith)

|  | Declaration |
| --- | --- |
| From | ``` func parallelRenderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder? ``` |
| To | ``` func parallelRenderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder ``` |

Modified [MTLCommandBuffer.renderCommandEncoderWithDescriptor(_: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442999-makerendercommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` func renderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder? ``` |
| To | ``` func renderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder ``` |

Modified [MTLCommandBufferError [enum]](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/code)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLCommandBufferStatus [enum]](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLCommandQueue](https://developer.apple.com/documentation/metal/mtlcommandqueue)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLCommandQueue : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     func commandBuffer() -> MTLCommandBuffer!     func commandBufferWithUnretainedReferences() -> MTLCommandBuffer     func insertDebugCaptureBoundary() } ``` |
| To | ``` protocol MTLCommandQueue : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     func commandBuffer() -> MTLCommandBuffer     func commandBufferWithUnretainedReferences() -> MTLCommandBuffer     func insertDebugCaptureBoundary() } ``` |

Modified [MTLCommandQueue.commandBuffer() -> MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandqueue/1508686-commandbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func commandBuffer() -> MTLCommandBuffer! ``` |
| To | ``` func commandBuffer() -> MTLCommandBuffer ``` |

Modified [MTLCompareFunction [enum]](https://developer.apple.com/documentation/metal/mtlcomparefunction)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLCompileOptions](https://developer.apple.com/documentation/metal/mtlcompileoptions)

|  | Declaration |
| --- | --- |
| From | ``` class MTLCompileOptions : NSObject, NSCopying {     var preprocessorMacros: [NSObject : AnyObject]!     var fastMathEnabled: Bool } ``` |
| To | ``` class MTLCompileOptions : NSObject, NSCopying {     var preprocessorMacros: [String : NSObject]?     var fastMathEnabled: Bool     var languageVersion: MTLLanguageVersion } ``` |

Modified [MTLCompileOptions.preprocessorMacros](https://developer.apple.com/documentation/metal/mtlcompileoptions/1516172-preprocessormacros)

|  | Declaration |
| --- | --- |
| From | ``` var preprocessorMacros: [NSObject : AnyObject]! ``` |
| To | ``` var preprocessorMacros: [String : NSObject]? ``` |

Modified [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLComputeCommandEncoder : MTLCommandEncoder, NSObjectProtocol {     func setComputePipelineState(_ state: MTLComputePipelineState)     func setBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setBufferOffset(_ offset: Int, atIndex index: Int)     func setBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange)     func setTexture(_ texture: MTLTexture?, atIndex index: Int)     func setTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState!, atIndex index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState!, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setThreadgroupMemoryLength(_ length: Int, atIndex index: Int)     func dispatchThreadgroups(_ threadgroupsPerGrid: MTLSize, threadsPerThreadgroup threadsPerThreadgroup: MTLSize) } ``` |
| To | ``` protocol MTLComputeCommandEncoder : MTLCommandEncoder, NSObjectProtocol {     func setComputePipelineState(_ state: MTLComputePipelineState)     func setBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setBufferOffset(_ offset: Int, atIndex index: Int)     func setBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange)     func setTexture(_ texture: MTLTexture?, atIndex index: Int)     func setTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setThreadgroupMemoryLength(_ length: Int, atIndex index: Int)     func dispatchThreadgroups(_ threadgroupsPerGrid: MTLSize, threadsPerThreadgroup threadsPerThreadgroup: MTLSize)     func dispatchThreadgroupsWithIndirectBuffer(_ indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int, threadsPerThreadgroup threadsPerThreadgroup: MTLSize) } ``` |

Modified [MTLComputeCommandEncoder.setSamplerState(_: MTLSamplerState?, atIndex: Int)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443144-setsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setSamplerState(_ sampler: MTLSamplerState!, atIndex index: Int) ``` |
| To | ``` func setSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int) ``` |

Modified [MTLComputeCommandEncoder.setSamplerState(_: MTLSamplerState?, lodMinClamp: Float, lodMaxClamp: Float, atIndex: Int)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443153-setsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setSamplerState(_ sampler: MTLSamplerState!, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int) ``` |
| To | ``` func setSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int) ``` |

Modified [MTLComputePipelineReflection](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection)

|  | Declaration |
| --- | --- |
| From | ``` class MTLComputePipelineReflection : NSObject {     var arguments: [AnyObject]! { get } } ``` |
| To | ``` class MTLComputePipelineReflection : NSObject {     var arguments: [MTLArgument] { get } } ``` |

Modified [MTLComputePipelineReflection.arguments](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection/1414909-arguments)

|  | Declaration |
| --- | --- |
| From | ``` var arguments: [AnyObject]! { get } ``` |
| To | ``` var arguments: [MTLArgument] { get } ``` |

Modified [MTLCPUCacheMode [enum]](https://developer.apple.com/documentation/metal/mtlcpucachemode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLCullMode [enum]](https://developer.apple.com/documentation/metal/mtlcullmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLDataType [enum]](https://developer.apple.com/documentation/metal/mtldatatype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLDevice : NSObjectProtocol {     var name: String { get }     func newCommandQueue() -> MTLCommandQueue     func newCommandQueueWithMaxCommandBufferCount(_ maxCommandBufferCount: Int) -> MTLCommandQueue     func newBufferWithLength(_ length: Int, options options: MTLResourceOptions) -> MTLBuffer!     func newBufferWithBytes(_ pointer: UnsafePointer<Void>, length length: Int, options options: MTLResourceOptions) -> MTLBuffer!     func newBufferWithBytesNoCopy(_ pointer: UnsafeMutablePointer<Void>, length length: Int, options options: MTLResourceOptions, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?) -> MTLBuffer!     func newDepthStencilStateWithDescriptor(_ descriptor: MTLDepthStencilDescriptor) -> MTLDepthStencilState     func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor) -> MTLTexture!     func newSamplerStateWithDescriptor(_ descriptor: MTLSamplerDescriptor) -> MTLSamplerState     func newDefaultLibrary() -> MTLLibrary?     func newLibraryWithFile(_ filepath: String, error error: NSErrorPointer) -> MTLLibrary?     func newLibraryWithData(_ data: dispatch_data_t, error error: NSErrorPointer) -> MTLLibrary?     func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?, error error: NSErrorPointer) -> MTLLibrary?     func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?, completionHandler completionHandler: ((MTLLibrary!, NSError!) -> Void)!)     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, error error: NSErrorPointer) -> MTLRenderPipelineState?     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLRenderPipelineReflection?>, error error: NSErrorPointer) -> MTLRenderPipelineState?     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: ((MTLRenderPipelineState!, NSError!) -> Void)!)     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: ((MTLRenderPipelineState!, MTLRenderPipelineReflection!, NSError!) -> Void)!)     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, error error: NSErrorPointer) -> MTLComputePipelineState?     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLComputePipelineReflection?>, error error: NSErrorPointer) -> MTLComputePipelineState?     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, completionHandler completionHandler: ((MTLComputePipelineState!, NSError!) -> Void)!)     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: ((MTLComputePipelineState!, MTLComputePipelineReflection!, NSError!) -> Void)!)     func supportsFeatureSet(_ featureSet: MTLFeatureSet) -> Bool } ``` |
| To | ``` protocol MTLDevice : NSObjectProtocol {     var name: String? { get }     var maxThreadsPerThreadgroup: MTLSize { get }     var lowPower: Bool { get }     var headless: Bool { get }     var depth24Stencil8PixelFormatSupported: Bool { get }     func newCommandQueue() -> MTLCommandQueue     func newCommandQueueWithMaxCommandBufferCount(_ maxCommandBufferCount: Int) -> MTLCommandQueue     func newBufferWithLength(_ length: Int, options options: MTLResourceOptions) -> MTLBuffer     func newBufferWithBytes(_ pointer: UnsafePointer<Void>, length length: Int, options options: MTLResourceOptions) -> MTLBuffer     func newBufferWithBytesNoCopy(_ pointer: UnsafeMutablePointer<Void>, length length: Int, options options: MTLResourceOptions, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?) -> MTLBuffer     func newDepthStencilStateWithDescriptor(_ descriptor: MTLDepthStencilDescriptor) -> MTLDepthStencilState     func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor) -> MTLTexture     func newSamplerStateWithDescriptor(_ descriptor: MTLSamplerDescriptor) -> MTLSamplerState     func newDefaultLibrary() -> MTLLibrary?     func newLibraryWithFile(_ filepath: String) throws -> MTLLibrary     func newLibraryWithData(_ data: dispatch_data_t) throws -> MTLLibrary     func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?) throws -> MTLLibrary     func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?, completionHandler completionHandler: MTLNewLibraryCompletionHandler)     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor) throws -> MTLRenderPipelineState     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>) throws -> MTLRenderPipelineState     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: MTLNewRenderPipelineStateCompletionHandler)     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewRenderPipelineStateWithReflectionCompletionHandler)     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction) throws -> MTLComputePipelineState     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>) throws -> MTLComputePipelineState     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, completionHandler completionHandler: MTLNewComputePipelineStateCompletionHandler)     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewComputePipelineStateWithReflectionCompletionHandler)     func newComputePipelineStateWithDescriptor(_ descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>) throws -> MTLComputePipelineState     func newComputePipelineStateWithDescriptor(_ descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewComputePipelineStateWithReflectionCompletionHandler)     func supportsFeatureSet(_ featureSet: MTLFeatureSet) -> Bool     func supportsTextureSampleCount(_ sampleCount: Int) -> Bool } ``` |

Modified [MTLDevice.name](https://developer.apple.com/documentation/metal/mtldevice/1433359-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified [MTLDevice.newBufferWithBytes(_: UnsafePointer<Void>, length: Int, options: MTLResourceOptions) -> MTLBuffer](https://developer.apple.com/documentation/metal/mtldevice/1433429-newbufferwithbytes)

|  | Declaration |
| --- | --- |
| From | ``` func newBufferWithBytes(_ pointer: UnsafePointer<Void>, length length: Int, options options: MTLResourceOptions) -> MTLBuffer! ``` |
| To | ``` func newBufferWithBytes(_ pointer: UnsafePointer<Void>, length length: Int, options options: MTLResourceOptions) -> MTLBuffer ``` |

Modified [MTLDevice.newBufferWithBytesNoCopy(_: UnsafeMutablePointer<Void>, length: Int, options: MTLResourceOptions, deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?) -> MTLBuffer](https://developer.apple.com/documentation/metal/mtldevice/1433382-newbufferwithbytesnocopy)

|  | Declaration |
| --- | --- |
| From | ``` func newBufferWithBytesNoCopy(_ pointer: UnsafeMutablePointer<Void>, length length: Int, options options: MTLResourceOptions, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?) -> MTLBuffer! ``` |
| To | ``` func newBufferWithBytesNoCopy(_ pointer: UnsafeMutablePointer<Void>, length length: Int, options options: MTLResourceOptions, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?) -> MTLBuffer ``` |

Modified [MTLDevice.newBufferWithLength(_: Int, options: MTLResourceOptions) -> MTLBuffer](https://developer.apple.com/documentation/metal/mtldevice/1433375-makebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func newBufferWithLength(_ length: Int, options options: MTLResourceOptions) -> MTLBuffer! ``` |
| To | ``` func newBufferWithLength(_ length: Int, options options: MTLResourceOptions) -> MTLBuffer ``` |

Modified [MTLDevice.newComputePipelineStateWithFunction(_: MTLFunction) throws -> MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtldevice/1433395-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, error error: NSErrorPointer) -> MTLComputePipelineState? ``` |
| To | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction) throws -> MTLComputePipelineState ``` |

Modified [MTLDevice.newComputePipelineStateWithFunction(_: MTLFunction, completionHandler: MTLNewComputePipelineStateCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433427-newcomputepipelinestatewithfunct)

|  | Declaration |
| --- | --- |
| From | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, completionHandler completionHandler: ((MTLComputePipelineState!, NSError!) -> Void)!) ``` |
| To | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, completionHandler completionHandler: MTLNewComputePipelineStateCompletionHandler) ``` |

Modified [MTLDevice.newComputePipelineStateWithFunction(_: MTLFunction, options: MTLPipelineOption, completionHandler: MTLNewComputePipelineStateWithReflectionCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433410-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: ((MTLComputePipelineState!, MTLComputePipelineReflection!, NSError!) -> Void)!) ``` |
| To | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewComputePipelineStateWithReflectionCompletionHandler) ``` |

Modified [MTLDevice.newComputePipelineStateWithFunction(_: MTLFunction, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>) throws -> MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtldevice/1433419-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLComputePipelineReflection?>, error error: NSErrorPointer) -> MTLComputePipelineState? ``` |
| To | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>) throws -> MTLComputePipelineState ``` |

Modified [MTLDevice.newLibraryWithData(_: dispatch_data_t) throws -> MTLLibrary](https://developer.apple.com/documentation/metal/mtldevice/1433391-newlibrarywithdata)

|  | Declaration |
| --- | --- |
| From | ``` func newLibraryWithData(_ data: dispatch_data_t, error error: NSErrorPointer) -> MTLLibrary? ``` |
| To | ``` func newLibraryWithData(_ data: dispatch_data_t) throws -> MTLLibrary ``` |

Modified [MTLDevice.newLibraryWithFile(_: String) throws -> MTLLibrary](https://developer.apple.com/documentation/metal/mtldevice/1433416-newlibrarywithfile)

|  | Declaration |
| --- | --- |
| From | ``` func newLibraryWithFile(_ filepath: String, error error: NSErrorPointer) -> MTLLibrary? ``` |
| To | ``` func newLibraryWithFile(_ filepath: String) throws -> MTLLibrary ``` |

Modified [MTLDevice.newLibraryWithSource(_: String, options: MTLCompileOptions?) throws -> MTLLibrary](https://developer.apple.com/documentation/metal/mtldevice/1433431-newlibrarywithsource)

|  | Declaration |
| --- | --- |
| From | ``` func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?, error error: NSErrorPointer) -> MTLLibrary? ``` |
| To | ``` func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?) throws -> MTLLibrary ``` |

Modified [MTLDevice.newLibraryWithSource(_: String, options: MTLCompileOptions?, completionHandler: MTLNewLibraryCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433351-newlibrarywithsource)

|  | Declaration |
| --- | --- |
| From | ``` func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?, completionHandler completionHandler: ((MTLLibrary!, NSError!) -> Void)!) ``` |
| To | ``` func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?, completionHandler completionHandler: MTLNewLibraryCompletionHandler) ``` |

Modified [MTLDevice.newRenderPipelineStateWithDescriptor(_: MTLRenderPipelineDescriptor) throws -> MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtldevice/1433369-newrenderpipelinestatewithdescri)

|  | Declaration |
| --- | --- |
| From | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, error error: NSErrorPointer) -> MTLRenderPipelineState? ``` |
| To | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor) throws -> MTLRenderPipelineState ``` |

Modified [MTLDevice.newRenderPipelineStateWithDescriptor(_: MTLRenderPipelineDescriptor, completionHandler: MTLNewRenderPipelineStateCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433363-makerenderpipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: ((MTLRenderPipelineState!, NSError!) -> Void)!) ``` |
| To | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: MTLNewRenderPipelineStateCompletionHandler) ``` |

Modified [MTLDevice.newRenderPipelineStateWithDescriptor(_: MTLRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: MTLNewRenderPipelineStateWithReflectionCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433365-newrenderpipelinestatewithdescri)

|  | Declaration |
| --- | --- |
| From | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: ((MTLRenderPipelineState!, MTLRenderPipelineReflection!, NSError!) -> Void)!) ``` |
| To | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewRenderPipelineStateWithReflectionCompletionHandler) ``` |

Modified [MTLDevice.newRenderPipelineStateWithDescriptor(_: MTLRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>) throws -> MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtldevice/1433361-makerenderpipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLRenderPipelineReflection?>, error error: NSErrorPointer) -> MTLRenderPipelineState? ``` |
| To | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>) throws -> MTLRenderPipelineState ``` |

Modified [MTLDevice.newTextureWithDescriptor(_: MTLTextureDescriptor) -> MTLTexture](https://developer.apple.com/documentation/metal/mtldevice/1433425-newtexturewithdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor) -> MTLTexture! ``` |
| To | ``` func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor) -> MTLTexture ``` |

Modified [MTLFeatureSet [enum]](https://developer.apple.com/documentation/metal/mtlfeatureset)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum MTLFeatureSet : UInt {     case _iOS_GPUFamily1_v1     case _iOS_GPUFamily2_v1 } ``` | -- |
| To | ``` enum MTLFeatureSet : UInt {     case iOS_GPUFamily1_v1     case iOS_GPUFamily2_v1     case iOS_GPUFamily1_v2     case iOS_GPUFamily2_v2     case iOS_GPUFamily3_v1     case OSX_GPUFamily1_v1 } ``` | UInt |

Modified [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLFunction : NSObjectProtocol {     var device: MTLDevice { get }     var functionType: MTLFunctionType { get }     var vertexAttributes: [AnyObject]! { get }     var name: String { get } } ``` |
| To | ``` protocol MTLFunction : NSObjectProtocol {     var device: MTLDevice { get }     var functionType: MTLFunctionType { get }     var vertexAttributes: [MTLVertexAttribute]? { get }     var name: String { get } } ``` |

Modified [MTLFunction.vertexAttributes](https://developer.apple.com/documentation/metal/mtlfunction/1515944-vertexattributes)

|  | Declaration |
| --- | --- |
| From | ``` var vertexAttributes: [AnyObject]! { get } ``` |
| To | ``` var vertexAttributes: [MTLVertexAttribute]? { get } ``` |

Modified [MTLFunctionType [enum]](https://developer.apple.com/documentation/metal/mtlfunctiontype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLIndexType [enum]](https://developer.apple.com/documentation/metal/mtlindextype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLLibrary : NSObjectProtocol {     var label: String! { get set }     var device: MTLDevice! { get }     func newFunctionWithName(_ functionName: String!) -> MTLFunction?     var functionNames: [AnyObject]! { get } } ``` |
| To | ``` protocol MTLLibrary : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     func newFunctionWithName(_ functionName: String) -> MTLFunction?     var functionNames: [String] { get } } ``` |

Modified [MTLLibrary.device](https://developer.apple.com/documentation/metal/mtllibrary/1515661-device)

|  | Declaration |
| --- | --- |
| From | ``` var device: MTLDevice! { get } ``` |
| To | ``` var device: MTLDevice { get } ``` |

Modified [MTLLibrary.functionNames](https://developer.apple.com/documentation/metal/mtllibrary/1515651-functionnames)

|  | Declaration |
| --- | --- |
| From | ``` var functionNames: [AnyObject]! { get } ``` |
| To | ``` var functionNames: [String] { get } ``` |

Modified [MTLLibrary.label](https://developer.apple.com/documentation/metal/mtllibrary/1516253-label)

|  | Declaration |
| --- | --- |
| From | ``` var label: String! { get set } ``` |
| To | ``` var label: String? { get set } ``` |

Modified [MTLLibrary.newFunctionWithName(_: String) -> MTLFunction?](https://developer.apple.com/documentation/metal/mtllibrary/1515524-newfunctionwithname)

|  | Declaration |
| --- | --- |
| From | ``` func newFunctionWithName(_ functionName: String!) -> MTLFunction? ``` |
| To | ``` func newFunctionWithName(_ functionName: String) -> MTLFunction? ``` |

Modified [MTLLibraryError [enum]](https://developer.apple.com/documentation/metal/mtllibraryerror/code)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLLoadAction [enum]](https://developer.apple.com/documentation/metal/mtlloadaction)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLPipelineOption [struct]](https://developer.apple.com/documentation/metal/mtlpipelineoption)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MTLPipelineOption : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: MTLPipelineOption { get }     static var ArgumentInfo: MTLPipelineOption { get }     static var BufferTypeInfo: MTLPipelineOption { get } } ``` | RawOptionSetType |
| To | ``` struct MTLPipelineOption : OptionSetType {     init(rawValue rawValue: UInt)     static var None: MTLPipelineOption { get }     static var ArgumentInfo: MTLPipelineOption { get }     static var BufferTypeInfo: MTLPipelineOption { get } } ``` | OptionSetType |

Modified [MTLPixelFormat [enum]](https://developer.apple.com/documentation/metal/mtlpixelformat)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum MTLPixelFormat : UInt {     case Invalid     case A8Unorm     case R8Unorm     case R8Unorm_sRGB     case R8Snorm     case R8Uint     case R8Sint     case R16Unorm     case R16Snorm     case R16Uint     case R16Sint     case R16Float     case RG8Unorm     case RG8Unorm_sRGB     case RG8Snorm     case RG8Uint     case RG8Sint     case B5G6R5Unorm     case A1BGR5Unorm     case ABGR4Unorm     case R32Uint     case R32Sint     case R32Float     case RG16Unorm     case RG16Snorm     case RG16Uint     case RG16Sint     case RG16Float     case RGBA8Unorm     case RGBA8Unorm_sRGB     case RGBA8Snorm     case RGBA8Uint     case RGBA8Sint     case BGRA8Unorm     case BGRA8Unorm_sRGB     case RGB10A2Unorm     case RGB10A2Uint     case RG11B10Float     case RGB9E5Float     case RG32Uint     case RG32Sint     case RG32Float     case RGBA16Unorm     case RGBA16Snorm     case RGBA16Uint     case RGBA16Sint     case RGBA16Float     case RGBA32Uint     case RGBA32Sint     case RGBA32Float     case PVRTC_RGB_2BPP     case PVRTC_RGB_2BPP_sRGB     case PVRTC_RGB_4BPP     case PVRTC_RGB_4BPP_sRGB     case PVRTC_RGBA_2BPP     case PVRTC_RGBA_2BPP_sRGB     case PVRTC_RGBA_4BPP     case PVRTC_RGBA_4BPP_sRGB     case EAC_R11Unorm     case EAC_R11Snorm     case EAC_RG11Unorm     case EAC_RG11Snorm     case EAC_RGBA8     case EAC_RGBA8_sRGB     case ETC2_RGB8     case ETC2_RGB8_sRGB     case ETC2_RGB8A1     case ETC2_RGB8A1_sRGB     case ASTC_4x4_sRGB     case ASTC_5x4_sRGB     case ASTC_5x5_sRGB     case ASTC_6x5_sRGB     case ASTC_6x6_sRGB     case ASTC_8x5_sRGB     case ASTC_8x6_sRGB     case ASTC_8x8_sRGB     case ASTC_10x5_sRGB     case ASTC_10x6_sRGB     case ASTC_10x8_sRGB     case ASTC_10x10_sRGB     case ASTC_12x10_sRGB     case ASTC_12x12_sRGB     case ASTC_4x4_LDR     case ASTC_5x4_LDR     case ASTC_5x5_LDR     case ASTC_6x5_LDR     case ASTC_6x6_LDR     case ASTC_8x5_LDR     case ASTC_8x6_LDR     case ASTC_8x8_LDR     case ASTC_10x5_LDR     case ASTC_10x6_LDR     case ASTC_10x8_LDR     case ASTC_10x10_LDR     case ASTC_12x10_LDR     case ASTC_12x12_LDR     case GBGR422     case BGRG422     case Depth32Float     case Stencil8 } ``` | -- |
| To | ``` enum MTLPixelFormat : UInt {     case Invalid     case A8Unorm     case R8Unorm     case R8Unorm_sRGB     case R8Snorm     case R8Uint     case R8Sint     case R16Unorm     case R16Snorm     case R16Uint     case R16Sint     case R16Float     case RG8Unorm     case RG8Unorm_sRGB     case RG8Snorm     case RG8Uint     case RG8Sint     case B5G6R5Unorm     case A1BGR5Unorm     case ABGR4Unorm     case BGR5A1Unorm     case R32Uint     case R32Sint     case R32Float     case RG16Unorm     case RG16Snorm     case RG16Uint     case RG16Sint     case RG16Float     case RGBA8Unorm     case RGBA8Unorm_sRGB     case RGBA8Snorm     case RGBA8Uint     case RGBA8Sint     case BGRA8Unorm     case BGRA8Unorm_sRGB     case RGB10A2Unorm     case RGB10A2Uint     case RG11B10Float     case RGB9E5Float     case RG32Uint     case RG32Sint     case RG32Float     case RGBA16Unorm     case RGBA16Snorm     case RGBA16Uint     case RGBA16Sint     case RGBA16Float     case RGBA32Uint     case RGBA32Sint     case RGBA32Float     case BC1_RGBA     case BC1_RGBA_sRGB     case BC2_RGBA     case BC2_RGBA_sRGB     case BC3_RGBA     case BC3_RGBA_sRGB     case BC4_RUnorm     case BC4_RSnorm     case BC5_RGUnorm     case BC5_RGSnorm     case BC6H_RGBFloat     case BC6H_RGBUfloat     case BC7_RGBAUnorm     case BC7_RGBAUnorm_sRGB     case PVRTC_RGB_2BPP     case PVRTC_RGB_2BPP_sRGB     case PVRTC_RGB_4BPP     case PVRTC_RGB_4BPP_sRGB     case PVRTC_RGBA_2BPP     case PVRTC_RGBA_2BPP_sRGB     case PVRTC_RGBA_4BPP     case PVRTC_RGBA_4BPP_sRGB     case EAC_R11Unorm     case EAC_R11Snorm     case EAC_RG11Unorm     case EAC_RG11Snorm     case EAC_RGBA8     case EAC_RGBA8_sRGB     case ETC2_RGB8     case ETC2_RGB8_sRGB     case ETC2_RGB8A1     case ETC2_RGB8A1_sRGB     case ASTC_4x4_sRGB     case ASTC_5x4_sRGB     case ASTC_5x5_sRGB     case ASTC_6x5_sRGB     case ASTC_6x6_sRGB     case ASTC_8x5_sRGB     case ASTC_8x6_sRGB     case ASTC_8x8_sRGB     case ASTC_10x5_sRGB     case ASTC_10x6_sRGB     case ASTC_10x8_sRGB     case ASTC_10x10_sRGB     case ASTC_12x10_sRGB     case ASTC_12x12_sRGB     case ASTC_4x4_LDR     case ASTC_5x4_LDR     case ASTC_5x5_LDR     case ASTC_6x5_LDR     case ASTC_6x6_LDR     case ASTC_8x5_LDR     case ASTC_8x6_LDR     case ASTC_8x8_LDR     case ASTC_10x5_LDR     case ASTC_10x6_LDR     case ASTC_10x8_LDR     case ASTC_10x10_LDR     case ASTC_12x10_LDR     case ASTC_12x12_LDR     case GBGR422     case BGRG422     case Depth32Float     case Stencil8     case Depth24Unorm_Stencil8     case Depth32Float_Stencil8 } ``` | UInt |

Modified [MTLPrimitiveType [enum]](https://developer.apple.com/documentation/metal/mtlprimitivetype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLPurgeableState [enum]](https://developer.apple.com/documentation/metal/mtlpurgeablestate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLRenderCommandEncoder : MTLCommandEncoder, NSObjectProtocol {     func setRenderPipelineState(_ pipelineState: MTLRenderPipelineState)     func setVertexBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setVertexBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setVertexBufferOffset(_ offset: Int, atIndex index: Int)     func setVertexBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange)     func setVertexTexture(_ texture: MTLTexture?, atIndex index: Int)     func setVertexTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState, atIndex index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setViewport(_ viewport: MTLViewport)     func setFrontFacingWinding(_ frontFacingWinding: MTLWinding)     func setCullMode(_ cullMode: MTLCullMode)     func setDepthBias(_ depthBias: Float, slopeScale slopeScale: Float, clamp clamp: Float)     func setScissorRect(_ rect: MTLScissorRect)     func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)     func setFragmentBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setFragmentBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setFragmentBufferOffset(_ offset: Int, atIndex index: Int)     func setFragmentBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offset: UnsafePointer<Int>, withRange range: NSRange)     func setFragmentTexture(_ texture: MTLTexture?, atIndex index: Int)     func setFragmentTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState, atIndex index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setBlendColorRed(_ red: Float, green green: Float, blue blue: Float, alpha alpha: Float)     func setDepthStencilState(_ depthStencilState: MTLDepthStencilState)     func setStencilReferenceValue(_ referenceValue: UInt32)     func setVisibilityResultMode(_ mode: MTLVisibilityResultMode, offset offset: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int) } ``` |
| To | ``` protocol MTLRenderCommandEncoder : MTLCommandEncoder, NSObjectProtocol {     func setRenderPipelineState(_ pipelineState: MTLRenderPipelineState)     func setVertexBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setVertexBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setVertexBufferOffset(_ offset: Int, atIndex index: Int)     func setVertexBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange)     func setVertexTexture(_ texture: MTLTexture?, atIndex index: Int)     func setVertexTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setViewport(_ viewport: MTLViewport)     func setFrontFacingWinding(_ frontFacingWinding: MTLWinding)     func setCullMode(_ cullMode: MTLCullMode)     func setDepthClipMode(_ depthClipMode: MTLDepthClipMode)     func setDepthBias(_ depthBias: Float, slopeScale slopeScale: Float, clamp clamp: Float)     func setScissorRect(_ rect: MTLScissorRect)     func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)     func setFragmentBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setFragmentBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setFragmentBufferOffset(_ offset: Int, atIndex index: Int)     func setFragmentBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offset: UnsafePointer<Int>, withRange range: NSRange)     func setFragmentTexture(_ texture: MTLTexture?, atIndex index: Int)     func setFragmentTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setBlendColorRed(_ red: Float, green green: Float, blue blue: Float, alpha alpha: Float)     func setDepthStencilState(_ depthStencilState: MTLDepthStencilState?)     func setStencilReferenceValue(_ referenceValue: UInt32)     func setStencilFrontReferenceValue(_ frontReferenceValue: UInt32, backReferenceValue backReferenceValue: UInt32)     func setVisibilityResultMode(_ mode: MTLVisibilityResultMode, offset offset: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int, baseInstance baseInstance: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int, baseVertex baseVertex: Int, baseInstance baseInstance: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int) } ``` |

Modified [MTLRenderCommandEncoder.setDepthStencilState(_: MTLDepthStencilState?)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516119-setdepthstencilstate)

|  | Declaration |
| --- | --- |
| From | ``` func setDepthStencilState(_ depthStencilState: MTLDepthStencilState) ``` |
| To | ``` func setDepthStencilState(_ depthStencilState: MTLDepthStencilState?) ``` |

Modified [MTLRenderCommandEncoder.setFragmentSamplerState(_: MTLSamplerState?, atIndex: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515577-setfragmentsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentSamplerState(_ sampler: MTLSamplerState, atIndex index: Int) ``` |
| To | ``` func setFragmentSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int) ``` |

Modified [MTLRenderCommandEncoder.setFragmentSamplerState(_: MTLSamplerState?, lodMinClamp: Float, lodMaxClamp: Float, atIndex: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515485-setfragmentsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentSamplerState(_ sampler: MTLSamplerState, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int) ``` |
| To | ``` func setFragmentSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int) ``` |

Modified [MTLRenderCommandEncoder.setVertexSamplerState(_: MTLSamplerState?, atIndex: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515537-setvertexsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexSamplerState(_ sampler: MTLSamplerState, atIndex index: Int) ``` |
| To | ``` func setVertexSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int) ``` |

Modified [MTLRenderCommandEncoder.setVertexSamplerState(_: MTLSamplerState?, lodMinClamp: Float, lodMaxClamp: Float, atIndex: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515864-setvertexsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexSamplerState(_ sampler: MTLSamplerState, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int) ``` |
| To | ``` func setVertexSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int) ``` |

Modified [MTLRenderPassColorAttachmentDescriptorArray](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray)

|  | Declaration |
| --- | --- |
| From | ``` class MTLRenderPassColorAttachmentDescriptorArray : NSObject {     subscript (attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor!     func objectAtIndexedSubscript(_ attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor!     func setObject(_ attachment: MTLRenderPassColorAttachmentDescriptor!, atIndexedSubscript attachmentIndex: Int) } ``` |
| To | ``` class MTLRenderPassColorAttachmentDescriptorArray : NSObject {     subscript (_ attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor!     func objectAtIndexedSubscript(_ attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor     func setObject(_ attachment: MTLRenderPassColorAttachmentDescriptor?, atIndexedSubscript attachmentIndex: Int) } ``` |

Modified [MTLRenderPassColorAttachmentDescriptorArray.subscript(_: Int) -> MTLRenderPassColorAttachmentDescriptor!](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray/1437977-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor! ``` |
| To | ``` subscript (_ attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor! ``` |

Modified [MTLRenderPassDepthAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class MTLRenderPassDepthAttachmentDescriptor : MTLRenderPassAttachmentDescriptor {     var clearDepth: Double } ``` |
| To | ``` class MTLRenderPassDepthAttachmentDescriptor : MTLRenderPassAttachmentDescriptor {     var clearDepth: Double     var depthResolveFilter: MTLMultisampleDepthResolveFilter } ``` |

Modified [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class MTLRenderPassDescriptor : NSObject, NSCopying {     init!() -> MTLRenderPassDescriptor     class func renderPassDescriptor() -> MTLRenderPassDescriptor!     var colorAttachments: MTLRenderPassColorAttachmentDescriptorArray { get }     @NSCopying var depthAttachment: MTLRenderPassDepthAttachmentDescriptor!     @NSCopying var stencilAttachment: MTLRenderPassStencilAttachmentDescriptor!     var visibilityResultBuffer: MTLBuffer? } ``` |
| To | ``` class MTLRenderPassDescriptor : NSObject, NSCopying {      init()     class func renderPassDescriptor() -> MTLRenderPassDescriptor     var colorAttachments: MTLRenderPassColorAttachmentDescriptorArray { get }     @NSCopying var depthAttachment: MTLRenderPassDepthAttachmentDescriptor!     @NSCopying var stencilAttachment: MTLRenderPassStencilAttachmentDescriptor!     var visibilityResultBuffer: MTLBuffer? } ``` |

Modified [MTLRenderPipelineColorAttachmentDescriptorArray](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray)

|  | Declaration |
| --- | --- |
| From | ``` class MTLRenderPipelineColorAttachmentDescriptorArray : NSObject {     subscript (attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor!     func objectAtIndexedSubscript(_ attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor!     func setObject(_ attachment: MTLRenderPipelineColorAttachmentDescriptor!, atIndexedSubscript attachmentIndex: Int) } ``` |
| To | ``` class MTLRenderPipelineColorAttachmentDescriptorArray : NSObject {     subscript (_ attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor!     func objectAtIndexedSubscript(_ attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor     func setObject(_ attachment: MTLRenderPipelineColorAttachmentDescriptor?, atIndexedSubscript attachmentIndex: Int) } ``` |

Modified [MTLRenderPipelineColorAttachmentDescriptorArray.subscript(_: Int) -> MTLRenderPipelineColorAttachmentDescriptor!](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray/1514673-objectatindexedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor! ``` |
| To | ``` subscript (_ attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor! ``` |

Modified MTLRenderPipelineError [enum]

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLRenderPipelineReflection](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection)

|  | Declaration |
| --- | --- |
| From | ``` class MTLRenderPipelineReflection : NSObject {     var vertexArguments: [AnyObject]! { get }     var fragmentArguments: [AnyObject]! { get } } ``` |
| To | ``` class MTLRenderPipelineReflection : NSObject {     var vertexArguments: [MTLArgument]? { get }     var fragmentArguments: [MTLArgument]? { get } } ``` |

Modified [MTLRenderPipelineReflection.fragmentArguments](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/1514701-fragmentarguments)

|  | Declaration |
| --- | --- |
| From | ``` var fragmentArguments: [AnyObject]! { get } ``` |
| To | ``` var fragmentArguments: [MTLArgument]? { get } ``` |

Modified [MTLRenderPipelineReflection.vertexArguments](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/1514686-vertexarguments)

|  | Declaration |
| --- | --- |
| From | ``` var vertexArguments: [AnyObject]! { get } ``` |
| To | ``` var vertexArguments: [MTLArgument]? { get } ``` |

Modified [MTLResource](https://developer.apple.com/documentation/metal/mtlresource)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLResource : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     var cpuCacheMode: MTLCPUCacheMode { get }     func setPurgeableState(_ state: MTLPurgeableState) -> MTLPurgeableState } ``` |
| To | ``` protocol MTLResource : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     var cpuCacheMode: MTLCPUCacheMode { get }     var storageMode: MTLStorageMode { get }     func setPurgeableState(_ state: MTLPurgeableState) -> MTLPurgeableState } ``` |

Modified [MTLResourceOptions [struct]](https://developer.apple.com/documentation/metal/mtlresourceoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MTLResourceOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var OptionCPUCacheModeDefault: MTLResourceOptions { get }     static var OptionCPUCacheModeWriteCombined: MTLResourceOptions { get } } ``` | RawOptionSetType |
| To | ``` struct MTLResourceOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var CPUCacheModeDefaultCache: MTLResourceOptions { get }     static var CPUCacheModeWriteCombined: MTLResourceOptions { get }     static var StorageModeShared: MTLResourceOptions { get }     static var StorageModeManaged: MTLResourceOptions { get }     static var StorageModePrivate: MTLResourceOptions { get }     static var OptionCPUCacheModeDefault: MTLResourceOptions { get }     static var OptionCPUCacheModeWriteCombined: MTLResourceOptions { get } } ``` | OptionSetType |

Modified [MTLSamplerAddressMode [enum]](https://developer.apple.com/documentation/metal/mtlsampleraddressmode)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum MTLSamplerAddressMode : UInt {     case ClampToEdge     case Repeat     case MirrorRepeat     case ClampToZero } ``` | -- |
| To | ``` enum MTLSamplerAddressMode : UInt {     case ClampToEdge     case MirrorClampToEdge     case Repeat     case MirrorRepeat     case ClampToZero } ``` | UInt |

Modified [MTLSamplerDescriptor](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class MTLSamplerDescriptor : NSObject, NSCopying {     var minFilter: MTLSamplerMinMagFilter     var magFilter: MTLSamplerMinMagFilter     var mipFilter: MTLSamplerMipFilter     var maxAnisotropy: Int     var sAddressMode: MTLSamplerAddressMode     var tAddressMode: MTLSamplerAddressMode     var rAddressMode: MTLSamplerAddressMode     var normalizedCoordinates: Bool     var lodMinClamp: Float     var lodMaxClamp: Float     var label: String! } ``` |
| To | ``` class MTLSamplerDescriptor : NSObject, NSCopying {     var minFilter: MTLSamplerMinMagFilter     var magFilter: MTLSamplerMinMagFilter     var mipFilter: MTLSamplerMipFilter     var maxAnisotropy: Int     var sAddressMode: MTLSamplerAddressMode     var tAddressMode: MTLSamplerAddressMode     var rAddressMode: MTLSamplerAddressMode     var normalizedCoordinates: Bool     var lodMinClamp: Float     var lodMaxClamp: Float     var lodAverage: Bool     var compareFunction: MTLCompareFunction     var label: String? } ``` |

Modified [MTLSamplerDescriptor.label](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/1515771-label)

|  | Declaration |
| --- | --- |
| From | ``` var label: String! ``` |
| To | ``` var label: String? ``` |

Modified [MTLSamplerMinMagFilter [enum]](https://developer.apple.com/documentation/metal/mtlsamplerminmagfilter)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLSamplerMipFilter [enum]](https://developer.apple.com/documentation/metal/mtlsamplermipfilter)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLSamplerState](https://developer.apple.com/documentation/metal/mtlsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLSamplerState : NSObjectProtocol {     var label: String! { get }     var device: MTLDevice! { get } } ``` |
| To | ``` protocol MTLSamplerState : NSObjectProtocol {     var label: String? { get }     var device: MTLDevice { get } } ``` |

Modified [MTLSamplerState.device](https://developer.apple.com/documentation/metal/mtlsamplerstate/1515871-device)

|  | Declaration |
| --- | --- |
| From | ``` var device: MTLDevice! { get } ``` |
| To | ``` var device: MTLDevice { get } ``` |

Modified [MTLSamplerState.label](https://developer.apple.com/documentation/metal/mtlsamplerstate/1516329-label)

|  | Declaration |
| --- | --- |
| From | ``` var label: String! { get } ``` |
| To | ``` var label: String? { get } ``` |

Modified [MTLStencilOperation [enum]](https://developer.apple.com/documentation/metal/mtlstenciloperation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLStoreAction [enum]](https://developer.apple.com/documentation/metal/mtlstoreaction)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLStructMember](https://developer.apple.com/documentation/metal/mtlstructmember)

|  | Declaration |
| --- | --- |
| From | ``` class MTLStructMember : NSObject {     var name: String! { get }     var offset: Int { get }     var dataType: MTLDataType { get }     func structType() -> MTLStructType!     func arrayType() -> MTLArrayType! } ``` |
| To | ``` class MTLStructMember : NSObject {     var name: String { get }     var offset: Int { get }     var dataType: MTLDataType { get }     func structType() -> MTLStructType?     func arrayType() -> MTLArrayType? } ``` |

Modified [MTLStructMember.arrayType() -> MTLArrayType?](https://developer.apple.com/documentation/metal/mtlstructmember/1461887-arraytype)

|  | Declaration |
| --- | --- |
| From | ``` func arrayType() -> MTLArrayType! ``` |
| To | ``` func arrayType() -> MTLArrayType? ``` |

Modified [MTLStructMember.name](https://developer.apple.com/documentation/metal/mtlstructmember/1461944-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [MTLStructMember.structType() -> MTLStructType?](https://developer.apple.com/documentation/metal/mtlstructmember/1462011-structtype)

|  | Declaration |
| --- | --- |
| From | ``` func structType() -> MTLStructType! ``` |
| To | ``` func structType() -> MTLStructType? ``` |

Modified [MTLStructType](https://developer.apple.com/documentation/metal/mtlstructtype)

|  | Declaration |
| --- | --- |
| From | ``` class MTLStructType : NSObject {     var members: [AnyObject]! { get }     func memberByName(_ name: String!) -> MTLStructMember! } ``` |
| To | ``` class MTLStructType : NSObject {     var members: [MTLStructMember] { get }     func memberByName(_ name: String) -> MTLStructMember? } ``` |

Modified [MTLStructType.memberByName(_: String) -> MTLStructMember?](https://developer.apple.com/documentation/metal/mtlstructtype/1462001-memberbyname)

|  | Declaration |
| --- | --- |
| From | ``` func memberByName(_ name: String!) -> MTLStructMember! ``` |
| To | ``` func memberByName(_ name: String) -> MTLStructMember? ``` |

Modified [MTLStructType.members](https://developer.apple.com/documentation/metal/mtlstructtype/1461975-members)

|  | Declaration |
| --- | --- |
| From | ``` var members: [AnyObject]! { get } ``` |
| To | ``` var members: [MTLStructMember] { get } ``` |

Modified [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLTexture : MTLResource, NSObjectProtocol {     var rootResource: MTLResource? { get }     var textureType: MTLTextureType { get }     var pixelFormat: MTLPixelFormat { get }     var width: Int { get }     var height: Int { get }     var depth: Int { get }     var mipmapLevelCount: Int { get }     var sampleCount: Int { get }     var arrayLength: Int { get }     var framebufferOnly: Bool { get }     func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int, fromRegion region: MTLRegion, mipmapLevel level: Int, slice slice: Int)     func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, slice slice: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int)     func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, fromRegion region: MTLRegion, mipmapLevel level: Int)     func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int)     func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat) -> MTLTexture? } ``` |
| To | ``` protocol MTLTexture : MTLResource, NSObjectProtocol {     var rootResource: MTLResource? { get }     var parentTexture: MTLTexture? { get }     var parentRelativeLevel: Int { get }     var parentRelativeSlice: Int { get }     var buffer: MTLBuffer? { get }     var bufferOffset: Int { get }     var bufferBytesPerRow: Int { get }     var textureType: MTLTextureType { get }     var pixelFormat: MTLPixelFormat { get }     var width: Int { get }     var height: Int { get }     var depth: Int { get }     var mipmapLevelCount: Int { get }     var sampleCount: Int { get }     var arrayLength: Int { get }     var usage: MTLTextureUsage { get }     var framebufferOnly: Bool { get }     func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int, fromRegion region: MTLRegion, mipmapLevel level: Int, slice slice: Int)     func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, slice slice: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int)     func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, fromRegion region: MTLRegion, mipmapLevel level: Int)     func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int)     func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat) -> MTLTexture     func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat, textureType textureType: MTLTextureType, levels levelRange: NSRange, slices sliceRange: NSRange) -> MTLTexture } ``` |

Modified [MTLTexture.newTextureViewWithPixelFormat(_: MTLPixelFormat) -> MTLTexture](https://developer.apple.com/documentation/metal/mtltexture/1515598-maketextureview)

|  | Declaration |
| --- | --- |
| From | ``` func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat) -> MTLTexture? ``` |
| To | ``` func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat) -> MTLTexture ``` |

Modified [MTLTextureDescriptor](https://developer.apple.com/documentation/metal/mtltexturedescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class MTLTextureDescriptor : NSObject, NSCopying {     class func texture2DDescriptorWithPixelFormat(_ pixelFormat: MTLPixelFormat, width width: Int, height height: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor     class func textureCubeDescriptorWithPixelFormat(_ pixelFormat: MTLPixelFormat, size size: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor     var textureType: MTLTextureType     var pixelFormat: MTLPixelFormat     var width: Int     var height: Int     var depth: Int     var mipmapLevelCount: Int     var sampleCount: Int     var arrayLength: Int     var resourceOptions: MTLResourceOptions } ``` |
| To | ``` class MTLTextureDescriptor : NSObject, NSCopying {     class func texture2DDescriptorWithPixelFormat(_ pixelFormat: MTLPixelFormat, width width: Int, height height: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor     class func textureCubeDescriptorWithPixelFormat(_ pixelFormat: MTLPixelFormat, size size: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor     var textureType: MTLTextureType     var pixelFormat: MTLPixelFormat     var width: Int     var height: Int     var depth: Int     var mipmapLevelCount: Int     var sampleCount: Int     var arrayLength: Int     var resourceOptions: MTLResourceOptions     var cpuCacheMode: MTLCPUCacheMode     var storageMode: MTLStorageMode     var usage: MTLTextureUsage } ``` |

Modified [MTLTextureType [enum]](https://developer.apple.com/documentation/metal/mtltexturetype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum MTLTextureType : UInt {     case Type1D     case Type1DArray     case Type2D     case Type2DArray     case Type2DMultisample     case TypeCube     case Type3D } ``` | -- |
| To | ``` enum MTLTextureType : UInt {     case Type1D     case Type1DArray     case Type2D     case Type2DArray     case Type2DMultisample     case TypeCube     case TypeCubeArray     case Type3D } ``` | UInt |

Modified [MTLTriangleFillMode [enum]](https://developer.apple.com/documentation/metal/mtltrianglefillmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLVertexAttribute](https://developer.apple.com/documentation/metal/mtlvertexattribute)

|  | Declaration |
| --- | --- |
| From | ``` class MTLVertexAttribute : NSObject {     var name: String! { get }     var attributeIndex: Int { get }     var attributeType: MTLDataType { get }     var active: Bool { get } } ``` |
| To | ``` class MTLVertexAttribute : NSObject {     var name: String? { get }     var attributeIndex: Int { get }     var attributeType: MTLDataType { get }     var active: Bool { get } } ``` |

Modified [MTLVertexAttribute.name](https://developer.apple.com/documentation/metal/mtlvertexattribute/1515447-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified [MTLVertexAttributeDescriptorArray](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray)

|  | Declaration |
| --- | --- |
| From | ``` class MTLVertexAttributeDescriptorArray : NSObject {     subscript (index: Int) -> MTLVertexAttributeDescriptor!     func objectAtIndexedSubscript(_ index: Int) -> MTLVertexAttributeDescriptor!     func setObject(_ attributeDesc: MTLVertexAttributeDescriptor!, atIndexedSubscript index: Int) } ``` |
| To | ``` class MTLVertexAttributeDescriptorArray : NSObject {     subscript (_ index: Int) -> MTLVertexAttributeDescriptor!     func objectAtIndexedSubscript(_ index: Int) -> MTLVertexAttributeDescriptor     func setObject(_ attributeDesc: MTLVertexAttributeDescriptor?, atIndexedSubscript index: Int) } ``` |

Modified [MTLVertexAttributeDescriptorArray.subscript(_: Int) -> MTLVertexAttributeDescriptor!](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray/1516138-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (index: Int) -> MTLVertexAttributeDescriptor! ``` |
| To | ``` subscript (_ index: Int) -> MTLVertexAttributeDescriptor! ``` |

Modified [MTLVertexBufferLayoutDescriptorArray](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray)

|  | Declaration |
| --- | --- |
| From | ``` class MTLVertexBufferLayoutDescriptorArray : NSObject {     subscript (index: Int) -> MTLVertexBufferLayoutDescriptor!     func objectAtIndexedSubscript(_ index: Int) -> MTLVertexBufferLayoutDescriptor!     func setObject(_ bufferDesc: MTLVertexBufferLayoutDescriptor!, atIndexedSubscript index: Int) } ``` |
| To | ``` class MTLVertexBufferLayoutDescriptorArray : NSObject {     subscript (_ index: Int) -> MTLVertexBufferLayoutDescriptor!     func objectAtIndexedSubscript(_ index: Int) -> MTLVertexBufferLayoutDescriptor     func setObject(_ bufferDesc: MTLVertexBufferLayoutDescriptor?, atIndexedSubscript index: Int) } ``` |

Modified [MTLVertexBufferLayoutDescriptorArray.subscript(_: Int) -> MTLVertexBufferLayoutDescriptor!](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray/1516230-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (index: Int) -> MTLVertexBufferLayoutDescriptor! ``` |
| To | ``` subscript (_ index: Int) -> MTLVertexBufferLayoutDescriptor! ``` |

Modified [MTLVertexDescriptor](https://developer.apple.com/documentation/metal/mtlvertexdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class MTLVertexDescriptor : NSObject, NSCopying {     init!() -> MTLVertexDescriptor     class func vertexDescriptor() -> MTLVertexDescriptor!     var layouts: MTLVertexBufferLayoutDescriptorArray { get }     var attributes: MTLVertexAttributeDescriptorArray { get }     func reset() } ``` |
| To | ``` class MTLVertexDescriptor : NSObject, NSCopying {      init()     class func vertexDescriptor() -> MTLVertexDescriptor     var layouts: MTLVertexBufferLayoutDescriptorArray { get }     var attributes: MTLVertexAttributeDescriptorArray { get }     func reset() } ``` |

Modified [MTLVertexFormat [enum]](https://developer.apple.com/documentation/metal/mtlvertexformat)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLVertexStepFunction [enum]](https://developer.apple.com/documentation/metal/mtlvertexstepfunction)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLVisibilityResultMode [enum]](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum MTLVisibilityResultMode : UInt {     case Disabled     case Boolean } ``` | -- |
| To | ``` enum MTLVisibilityResultMode : UInt {     case Disabled     case Boolean     case Counting } ``` | UInt |

Modified [MTLWinding [enum]](https://developer.apple.com/documentation/metal/mtlwinding)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MTLCommandBufferHandler](https://developer.apple.com/documentation/metal/mtlcommandbufferhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MTLCommandBufferHandler = (MTLCommandBuffer!) -> Void ``` |
| To | ``` typealias MTLCommandBufferHandler = (MTLCommandBuffer) -> Void ``` |

Modified [MTLCreateSystemDefaultDevice() -> MTLDevice?](https://developer.apple.com/documentation/metal/1433401-mtlcreatesystemdefaultdevice)

|  | Declaration |
| --- | --- |
| From | ``` func MTLCreateSystemDefaultDevice() -> MTLDevice! ``` |
| To | ``` func MTLCreateSystemDefaultDevice() -> MTLDevice? ``` |

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
