---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/Metal.html
archived_at: '2026-07-18T02:56:35.061005Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Metal Changes for Objective-C

### Metal

#### MTLArgument.h

Modified [MTLStructType.members](https://developer.apple.com/documentation/metal/mtlstructtype/1461975-members)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *members ``` |
| To | ``` @property(readonly, nonnull) NSArray<MTLStructMember *> *members ``` |

#### MTLBlitCommandEncoder.h

Added [-[MTLBlitCommandEncoder copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:]](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400771-copyfrombuffer)Added [-[MTLBlitCommandEncoder copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:]](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400756-copy)Added [MTLBlitOption](https://developer.apple.com/documentation/metal/mtlblitoption)Added [MTLBlitOptionDepthFromDepthStencil](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptiondepthfromdepthstencil)Added [MTLBlitOptionNone](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptionnone)Added [MTLBlitOptionRowLinearPVRTC](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptionrowlinearpvrtc)Added [MTLBlitOptionStencilFromDepthStencil](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptionstencilfromdepthstencil)

#### MTLComputeCommandEncoder.h

Added [-[MTLComputeCommandEncoder dispatchThreadgroupsWithIndirectBuffer:indirectBufferOffset:threadsPerThreadgroup:]](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443157-dispatchthreadgroups)Added [MTLDispatchThreadgroupsIndirectArguments](https://developer.apple.com/documentation/metal/mtldispatchthreadgroupsindirectarguments)Modified [-[MTLComputeCommandEncoder setBuffers:offsets:withRange:]](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443134-setbuffers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setBuffers:(const id<MTLBuffer> [])buffers offsets:(const NSUInteger [])offsets withRange:(NSRange)range ``` |
| To | ``` - (void)setBuffers:(id<MTLBuffer>  _Nullable const [])buffers offsets:(const NSUInteger [])offsets withRange:(NSRange)range ``` |

Modified [-[MTLComputeCommandEncoder setSamplerStates:lodMinClamps:lodMaxClamps:withRange:]](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443128-setsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setSamplerStates:(const id<MTLSamplerState> [])samplers lodMinClamps:(const float [])lodMinClamps lodMaxClamps:(const float [])lodMaxClamps withRange:(NSRange)range ``` |
| To | ``` - (void)setSamplerStates:(id<MTLSamplerState>  _Nullable const [])samplers lodMinClamps:(const float [])lodMinClamps lodMaxClamps:(const float [])lodMaxClamps withRange:(NSRange)range ``` |

Modified [-[MTLComputeCommandEncoder setSamplerStates:withRange:]](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443155-setsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setSamplerStates:(const id<MTLSamplerState> [])samplers withRange:(NSRange)range ``` |
| To | ``` - (void)setSamplerStates:(id<MTLSamplerState>  _Nullable const [])samplers withRange:(NSRange)range ``` |

Modified [-[MTLComputeCommandEncoder setTextures:withRange:]](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443148-settextures)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setTextures:(const id<MTLTexture> [])textures withRange:(NSRange)range ``` |
| To | ``` - (void)setTextures:(id<MTLTexture>  _Nullable const [])textures withRange:(NSRange)range ``` |

#### MTLComputePipeline.h

Added [MTLComputePipelineDescriptor](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor)Added [MTLComputePipelineDescriptor.computeFunction](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/1414917-computefunction)Added [MTLComputePipelineDescriptor.label](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/1414918-label)Added [-[MTLComputePipelineDescriptor reset]](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/1414923-reset)Added [MTLComputePipelineDescriptor.threadGroupSizeIsMultipleOfThreadExecutionWidth](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/1414915-threadgroupsizeismultipleofthrea)Modified [MTLComputePipelineReflection.arguments](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection/1414909-arguments)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *arguments ``` |
| To | ``` @property(readonly, nonnull) NSArray<MTLArgument *> *arguments ``` |

#### MTLDevice.h

Added [MTLDevice.maxThreadsPerThreadgroup](https://developer.apple.com/documentation/metal/mtldevice/1433393-maxthreadsperthreadgroup)Added [-[MTLDevice newComputePipelineStateWithDescriptor:options:completionHandler:]](https://developer.apple.com/documentation/metal/mtldevice/1433403-makecomputepipelinestate)Added [-[MTLDevice newComputePipelineStateWithDescriptor:options:reflection:error:]](https://developer.apple.com/documentation/metal/mtldevice/1433353-makecomputepipelinestate)Added [-[MTLDevice supportsTextureSampleCount:]](https://developer.apple.com/documentation/metal/mtldevice/1433355-supportstexturesamplecount)Added [MTLAutoreleasedComputePipelineReflection](https://developer.apple.com/documentation/metal/mtlautoreleasedcomputepipelinereflection)Added [MTLAutoreleasedRenderPipelineReflection](https://developer.apple.com/documentation/metal/mtlautoreleasedrenderpipelinereflection)Added [MTLFeatureSet_iOS_GPUFamily1_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_ios_gpufamily1_v2)Added [MTLFeatureSet_iOS_GPUFamily2_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/ios_gpufamily2_v2)Added [MTLFeatureSet_iOS_GPUFamily3_v1](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_ios_gpufamily3_v1)Added [MTLNewComputePipelineStateCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewcomputepipelinestatecompletionhandler)Added [MTLNewComputePipelineStateWithReflectionCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewcomputepipelinestatewithreflectioncompletionhandler)Added [MTLNewLibraryCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewlibrarycompletionhandler)Added [MTLNewRenderPipelineStateCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatecompletionhandler)Added [MTLNewRenderPipelineStateWithReflectionCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatewithreflectioncompletionhandler)Modified [-[MTLDevice newComputePipelineStateWithFunction:completionHandler:]](https://developer.apple.com/documentation/metal/mtldevice/1433427-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)newComputePipelineStateWithFunction:(id<MTLFunction>)computeFunction completionHandler:(void (^)(id<MTLComputePipelineState> computePipelineState, NSError *error))completionHandler ``` |
| To | ``` - (void)newComputePipelineStateWithFunction:(id<MTLFunction> _Nonnull)computeFunction completionHandler:(MTLNewComputePipelineStateCompletionHandler _Nonnull)completionHandler ``` |

Modified [-[MTLDevice newComputePipelineStateWithFunction:options:completionHandler:]](https://developer.apple.com/documentation/metal/mtldevice/1433410-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)newComputePipelineStateWithFunction:(id<MTLFunction>)computeFunction options:(MTLPipelineOption)options completionHandler:(void (^)(id<MTLComputePipelineState> computePipelineState, MTLComputePipelineReflection *reflection, NSError *error))completionHandler ``` |
| To | ``` - (void)newComputePipelineStateWithFunction:(id<MTLFunction> _Nonnull)computeFunction options:(MTLPipelineOption)options completionHandler:(MTLNewComputePipelineStateWithReflectionCompletionHandler _Nonnull)completionHandler ``` |

Modified [-[MTLDevice newComputePipelineStateWithFunction:options:reflection:error:]](https://developer.apple.com/documentation/metal/mtldevice/1433419-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` - (id<MTLComputePipelineState>)newComputePipelineStateWithFunction:(id<MTLFunction>)computeFunction options:(MTLPipelineOption)options reflection:(MTLComputePipelineReflection **)reflection error:(NSError **)error ``` |
| To | ``` - (id<MTLComputePipelineState> _Nullable)newComputePipelineStateWithFunction:(id<MTLFunction> _Nonnull)computeFunction options:(MTLPipelineOption)options reflection:(MTLAutoreleasedComputePipelineReflection * _Nullable)reflection error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[MTLDevice newLibraryWithSource:options:completionHandler:]](https://developer.apple.com/documentation/metal/mtldevice/1433351-newlibrarywithsource)

|  | Declaration |
| --- | --- |
| From | ``` - (void)newLibraryWithSource:(NSString *)source options:(MTLCompileOptions *)options completionHandler:(void (^)(id<MTLLibrary> library, NSError *error))completionHandler ``` |
| To | ``` - (void)newLibraryWithSource:(NSString * _Nonnull)source options:(MTLCompileOptions * _Nullable)options completionHandler:(MTLNewLibraryCompletionHandler _Nonnull)completionHandler ``` |

Modified [-[MTLDevice newRenderPipelineStateWithDescriptor:completionHandler:]](https://developer.apple.com/documentation/metal/mtldevice/1433363-makerenderpipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor *)descriptor completionHandler:(void (^)(id<MTLRenderPipelineState> renderPipelineState, NSError *error))completionHandler ``` |
| To | ``` - (void)newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor * _Nonnull)descriptor completionHandler:(MTLNewRenderPipelineStateCompletionHandler _Nonnull)completionHandler ``` |

Modified [-[MTLDevice newRenderPipelineStateWithDescriptor:options:completionHandler:]](https://developer.apple.com/documentation/metal/mtldevice/1433365-makerenderpipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor *)descriptor options:(MTLPipelineOption)options completionHandler:(void (^)(id<MTLRenderPipelineState> renderPipelineState, MTLRenderPipelineReflection *reflection, NSError *error))completionHandler ``` |
| To | ``` - (void)newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor * _Nonnull)descriptor options:(MTLPipelineOption)options completionHandler:(MTLNewRenderPipelineStateWithReflectionCompletionHandler _Nonnull)completionHandler ``` |

Modified [-[MTLDevice newRenderPipelineStateWithDescriptor:options:reflection:error:]](https://developer.apple.com/documentation/metal/mtldevice/1433361-newrenderpipelinestatewithdescri)

|  | Declaration |
| --- | --- |
| From | ``` - (id<MTLRenderPipelineState>)newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor *)descriptor options:(MTLPipelineOption)options reflection:(MTLRenderPipelineReflection **)reflection error:(NSError **)error ``` |
| To | ``` - (id<MTLRenderPipelineState> _Nullable)newRenderPipelineStateWithDescriptor:(MTLRenderPipelineDescriptor * _Nonnull)descriptor options:(MTLPipelineOption)options reflection:(MTLAutoreleasedRenderPipelineReflection * _Nullable)reflection error:(NSError * _Nullable * _Nullable)error ``` |

#### MTLLibrary.h

Added [MTLCompileOptions.languageVersion](https://developer.apple.com/documentation/metal/mtlcompileoptions/1515494-languageversion)Added [MTLLanguageVersion](https://developer.apple.com/documentation/metal/mtllanguageversion)Added [MTLLanguageVersion1_0](https://developer.apple.com/documentation/metal/mtllanguageversion/mtllanguageversion1_0)Added [MTLLanguageVersion1_1](https://developer.apple.com/documentation/metal/mtllanguageversion/version1_1)Modified [MTLCompileOptions.preprocessorMacros](https://developer.apple.com/documentation/metal/mtlcompileoptions/1516172-preprocessormacros)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy, nonatomic) NSDictionary *preprocessorMacros ``` |
| To | ``` @property(readwrite, copy, nonatomic, nullable) NSDictionary<NSString *,NSObject *> *preprocessorMacros ``` |

Modified [MTLFunction.vertexAttributes](https://developer.apple.com/documentation/metal/mtlfunction/1515944-vertexattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *vertexAttributes ``` |
| To | ``` @property(readonly, nullable) NSArray<MTLVertexAttribute *> *vertexAttributes ``` |

Modified [MTLLibrary.functionNames](https://developer.apple.com/documentation/metal/mtllibrary/1515651-functionnames)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *functionNames ``` |
| To | ``` @property(readonly, nonnull) NSArray<NSString *> *functionNames ``` |

#### MTLPixelFormat.h

Added [MTLPixelFormatBGR5A1Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr5a1unorm)Added [MTLPixelFormatDepth32Float_Stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatdepth32float_stencil8)

#### MTLRenderCommandEncoder.h

Added [-[MTLRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:instanceCount:baseVertex:baseInstance:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515520-drawindexedprimitives)Added [-[MTLRenderCommandEncoder drawIndexedPrimitives:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515392-drawindexedprimitives)Added [-[MTLRenderCommandEncoder drawPrimitives:indirectBuffer:indirectBufferOffset:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515467-drawprimitives)Added [-[MTLRenderCommandEncoder drawPrimitives:vertexStart:vertexCount:instanceCount:baseInstance:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515561-drawprimitives)Added [-[MTLRenderCommandEncoder setDepthClipMode:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516267-setdepthclipmode)Added [-[MTLRenderCommandEncoder setStencilFrontReferenceValue:backReferenceValue:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515522-setstencilreferencevalues)Added [MTLDepthClipMode](https://developer.apple.com/documentation/metal/mtldepthclipmode)Added [MTLDepthClipModeClamp](https://developer.apple.com/documentation/metal/mtldepthclipmode/mtldepthclipmodeclamp)Added [MTLDepthClipModeClip](https://developer.apple.com/documentation/metal/mtldepthclipmode/clip)Added [MTLDrawIndexedPrimitivesIndirectArguments](https://developer.apple.com/documentation/metal/mtldrawindexedprimitivesindirectarguments)Added [MTLDrawPrimitivesIndirectArguments](https://developer.apple.com/documentation/metal/mtldrawprimitivesindirectarguments)Added [MTLVisibilityResultModeCounting](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/mtlvisibilityresultmodecounting)Modified [-[MTLRenderCommandEncoder setFragmentBuffers:offsets:withRange:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515724-setfragmentbuffers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setFragmentBuffers:(const id<MTLBuffer> [])buffers offsets:(const NSUInteger [])offset withRange:(NSRange)range ``` |
| To | ``` - (void)setFragmentBuffers:(id<MTLBuffer>  _Nullable const [])buffers offsets:(const NSUInteger [])offset withRange:(NSRange)range ``` |

Modified [-[MTLRenderCommandEncoder setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515463-setfragmentsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setFragmentSamplerStates:(const id<MTLSamplerState> [])samplers lodMinClamps:(const float [])lodMinClamps lodMaxClamps:(const float [])lodMaxClamps withRange:(NSRange)range ``` |
| To | ``` - (void)setFragmentSamplerStates:(id<MTLSamplerState>  _Nullable const [])samplers lodMinClamps:(const float [])lodMinClamps lodMaxClamps:(const float [])lodMaxClamps withRange:(NSRange)range ``` |

Modified [-[MTLRenderCommandEncoder setFragmentSamplerStates:withRange:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515970-setfragmentsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setFragmentSamplerStates:(const id<MTLSamplerState> [])samplers withRange:(NSRange)range ``` |
| To | ``` - (void)setFragmentSamplerStates:(id<MTLSamplerState>  _Nullable const [])samplers withRange:(NSRange)range ``` |

Modified [-[MTLRenderCommandEncoder setFragmentTextures:withRange:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515878-setfragmenttextures)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setFragmentTextures:(const id<MTLTexture> [])textures withRange:(NSRange)range ``` |
| To | ``` - (void)setFragmentTextures:(id<MTLTexture>  _Nullable const [])textures withRange:(NSRange)range ``` |

Modified [-[MTLRenderCommandEncoder setVertexBuffers:offsets:withRange:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515987-setvertexbuffers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setVertexBuffers:(const id<MTLBuffer> [])buffers offsets:(const NSUInteger [])offsets withRange:(NSRange)range ``` |
| To | ``` - (void)setVertexBuffers:(id<MTLBuffer>  _Nullable const [])buffers offsets:(const NSUInteger [])offsets withRange:(NSRange)range ``` |

Modified [-[MTLRenderCommandEncoder setVertexSamplerStates:lodMinClamps:lodMaxClamps:withRange:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516322-setvertexsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setVertexSamplerStates:(const id<MTLSamplerState> [])samplers lodMinClamps:(const float [])lodMinClamps lodMaxClamps:(const float [])lodMaxClamps withRange:(NSRange)range ``` |
| To | ``` - (void)setVertexSamplerStates:(id<MTLSamplerState>  _Nullable const [])samplers lodMinClamps:(const float [])lodMinClamps lodMaxClamps:(const float [])lodMaxClamps withRange:(NSRange)range ``` |

Modified [-[MTLRenderCommandEncoder setVertexSamplerStates:withRange:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515400-setvertexsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setVertexSamplerStates:(const id<MTLSamplerState> [])samplers withRange:(NSRange)range ``` |
| To | ``` - (void)setVertexSamplerStates:(id<MTLSamplerState>  _Nullable const [])samplers withRange:(NSRange)range ``` |

Modified [-[MTLRenderCommandEncoder setVertexTextures:withRange:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516109-setvertextextures)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setVertexTextures:(const id<MTLTexture> [])textures withRange:(NSRange)range ``` |
| To | ``` - (void)setVertexTextures:(id<MTLTexture>  _Nullable const [])textures withRange:(NSRange)range ``` |

#### MTLRenderPass.h

Added [MTLRenderPassDepthAttachmentDescriptor.depthResolveFilter](https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor/1619184-depthresolvefilter)Added [MTLMultisampleDepthResolveFilter](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter)Added [MTLMultisampleDepthResolveFilterMax](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter/max)Added [MTLMultisampleDepthResolveFilterMin](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter/min)Added [MTLMultisampleDepthResolveFilterSample0](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter/mtlmultisampledepthresolvefiltersample0)

#### MTLRenderPipeline.h

Modified [MTLRenderPipelineReflection.fragmentArguments](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/1514701-fragmentarguments)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *fragmentArguments ``` |
| To | ``` @property(readonly, nullable) NSArray<MTLArgument *> *fragmentArguments ``` |

Modified [MTLRenderPipelineReflection.vertexArguments](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/1514686-vertexarguments)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *vertexArguments ``` |
| To | ``` @property(readonly, nullable) NSArray<MTLArgument *> *vertexArguments ``` |

#### MTLResource.h

Added [MTLResource.storageMode](https://developer.apple.com/documentation/metal/mtlresource/1515477-storagemode)Added [MTLResourceCPUCacheModeDefaultCache](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcecpucachemodedefaultcache)Added [MTLResourceCPUCacheModeWriteCombined](https://developer.apple.com/documentation/metal/mtlresourceoptions/1515730-cpucachemodewritecombined)Added [MTLResourceStorageModePrivate](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcestoragemodeprivate)Added [MTLResourceStorageModeShared](https://developer.apple.com/documentation/metal/mtlresourceoptions/1515613-storagemodeshared)Added [MTLStorageMode](https://developer.apple.com/documentation/metal/mtlstoragemode)Added [MTLStorageModePrivate](https://developer.apple.com/documentation/metal/mtlstoragemode/mtlstoragemodeprivate)Added [MTLStorageModeShared](https://developer.apple.com/documentation/metal/mtlstoragemode/shared)

#### MTLSampler.h

Added [MTLSamplerDescriptor.compareFunction](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/1516001-comparefunction)Added [MTLSamplerDescriptor.lodAverage](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor/1615844-lodaverage)

#### MTLTexture.h

Added [MTLTexture.buffer](https://developer.apple.com/documentation/metal/mtltexture/1619090-buffer)Added [MTLTexture.bufferBytesPerRow](https://developer.apple.com/documentation/metal/mtltexture/1619175-bufferbytesperrow)Added [MTLTexture.bufferOffset](https://developer.apple.com/documentation/metal/mtltexture/1619019-bufferoffset)Added [-[MTLTexture newTextureViewWithPixelFormat:textureType:levels:slices:]](https://developer.apple.com/documentation/metal/mtltexture/1515409-newtextureviewwithpixelformat)Added [MTLTexture.parentRelativeLevel](https://developer.apple.com/documentation/metal/mtltexture/1516265-parentrelativelevel)Added [MTLTexture.parentRelativeSlice](https://developer.apple.com/documentation/metal/mtltexture/1516221-parentrelativeslice)Added [MTLTexture.parentTexture](https://developer.apple.com/documentation/metal/mtltexture/1515372-parenttexture)Added [MTLTexture.usage](https://developer.apple.com/documentation/metal/mtltexture/1515763-usage)Added [MTLTextureDescriptor.cpuCacheMode](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515375-cpucachemode)Added [MTLTextureDescriptor.storageMode](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516262-storagemode)Added [MTLTextureDescriptor.usage](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515783-usage)Added [MTLTextureUsage](https://developer.apple.com/documentation/metal/mtltextureusage)Added [MTLTextureUsagePixelFormatView](https://developer.apple.com/documentation/metal/mtltextureusage/1516223-pixelformatview)Added [MTLTextureUsageRenderTarget](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusagerendertarget)Added [MTLTextureUsageShaderRead](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusageshaderread)Added [MTLTextureUsageShaderWrite](https://developer.apple.com/documentation/metal/mtltextureusage/1515854-shaderwrite)Added [MTLTextureUsageUnknown](https://developer.apple.com/documentation/metal/mtltextureusage/1515856-unknown)

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
