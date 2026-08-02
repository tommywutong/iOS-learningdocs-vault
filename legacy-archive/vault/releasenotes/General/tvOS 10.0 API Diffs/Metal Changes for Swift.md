---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/Metal.html
archived_at: '2026-07-18T02:57:51.342158Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# Metal Changes for Swift

### Metal

Removed [MTLBlitOption.None](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptionnone)Removed [MTLColorWriteMask.None](https://developer.apple.com/documentation/metal/mtlcolorwritemask/mtlcolorwritemasknone)Removed MTLFeatureSet.TVOS_GPUFamily1_v1Removed [MTLPipelineOption.None](https://developer.apple.com/documentation/metal/mtlpipelineoption/mtlpipelineoptionnone)Removed [MTLRenderCommandEncoder.setDepthClipMode(_: MTLDepthClipMode)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516267-setdepthclipmode)Removed [MTLResourceOptions.CPUCacheModeDefaultCache](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcecpucachemodedefaultcache)Removed [MTLResourceOptions.OptionCPUCacheModeDefault](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourceoptioncpucachemodedefault)Added [MTLArgument.arrayLength](https://developer.apple.com/documentation/metal/mtlargument/1649746-arraylength)Added [MTLArgument.isDepthTexture](https://developer.apple.com/documentation/metal/mtlargument/1639934-isdepthtexture)Added [MTLAttribute](https://developer.apple.com/documentation/metal/mtlattribute)Added [MTLAttribute.attributeIndex](https://developer.apple.com/documentation/metal/mtlattribute/2097158-attributeindex)Added [MTLAttribute.attributeType](https://developer.apple.com/documentation/metal/mtlattribute/2097155-attributetype)Added [MTLAttribute.isActive](https://developer.apple.com/documentation/metal/mtlattribute/2097160-active)Added [MTLAttribute.isPatchControlPointData](https://developer.apple.com/documentation/metal/mtlattribute/2097156-patchcontrolpointdata)Added [MTLAttribute.isPatchData](https://developer.apple.com/documentation/metal/mtlattribute/2097157-patchdata)Added [MTLAttribute.name](https://developer.apple.com/documentation/metal/mtlattribute/2097161-name)Added [MTLAttributeDescriptor](https://developer.apple.com/documentation/metal/mtlattributedescriptor)Added [MTLAttributeDescriptor.bufferIndex](https://developer.apple.com/documentation/metal/mtlattributedescriptor/2097218-bufferindex)Added [MTLAttributeDescriptor.format](https://developer.apple.com/documentation/metal/mtlattributedescriptor/2097194-format)Added [MTLAttributeDescriptor.offset](https://developer.apple.com/documentation/metal/mtlattributedescriptor/2097220-offset)Added [MTLAttributeDescriptorArray](https://developer.apple.com/documentation/metal/mtlattributedescriptorarray)Added [MTLAttributeDescriptorArray.subscript(_: Int) -> MTLAttributeDescriptor](https://developer.apple.com/documentation/metal/mtlattributedescriptorarray/2097215-objectatindexedsubscript)Added [MTLAttributeFormat [enum]](https://developer.apple.com/documentation/metal/mtlattributeformat)Added [MTLAttributeFormat.char2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatchar2)Added [MTLAttributeFormat.char2Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatchar2normalized)Added [MTLAttributeFormat.char3](https://developer.apple.com/documentation/metal/mtlattributeformat/char3)Added [MTLAttributeFormat.char3Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/char3normalized)Added [MTLAttributeFormat.char4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatchar4)Added [MTLAttributeFormat.char4Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/char4normalized)Added [MTLAttributeFormat.float](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatfloat)Added [MTLAttributeFormat.float2](https://developer.apple.com/documentation/metal/mtlattributeformat/float2)Added [MTLAttributeFormat.float3](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatfloat3)Added [MTLAttributeFormat.float4](https://developer.apple.com/documentation/metal/mtlattributeformat/float4)Added [MTLAttributeFormat.half2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformathalf2)Added [MTLAttributeFormat.half3](https://developer.apple.com/documentation/metal/mtlattributeformat/half3)Added [MTLAttributeFormat.half4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformathalf4)Added [MTLAttributeFormat.int](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatint)Added [MTLAttributeFormat.int1010102Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatint1010102normalized)Added [MTLAttributeFormat.int2](https://developer.apple.com/documentation/metal/mtlattributeformat/int2)Added [MTLAttributeFormat.int3](https://developer.apple.com/documentation/metal/mtlattributeformat/int3)Added [MTLAttributeFormat.int4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatint4)Added [MTLAttributeFormat.invalid](https://developer.apple.com/documentation/metal/mtlattributeformat/invalid)Added [MTLAttributeFormat.short2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatshort2)Added [MTLAttributeFormat.short2Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/short2normalized)Added [MTLAttributeFormat.short3](https://developer.apple.com/documentation/metal/mtlattributeformat/short3)Added [MTLAttributeFormat.short3Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatshort3normalized)Added [MTLAttributeFormat.short4](https://developer.apple.com/documentation/metal/mtlattributeformat/short4)Added [MTLAttributeFormat.short4Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatshort4normalized)Added [MTLAttributeFormat.uchar2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuchar2)Added [MTLAttributeFormat.uchar2Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuchar2normalized)Added [MTLAttributeFormat.uchar3](https://developer.apple.com/documentation/metal/mtlattributeformat/uchar3)Added [MTLAttributeFormat.uchar3Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuchar3normalized)Added [MTLAttributeFormat.uchar4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuchar4)Added [MTLAttributeFormat.uchar4Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuchar4normalized)Added [MTLAttributeFormat.uint](https://developer.apple.com/documentation/metal/mtlattributeformat/uint)Added [MTLAttributeFormat.uInt1010102Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/uint1010102normalized)Added [MTLAttributeFormat.uint2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuint2)Added [MTLAttributeFormat.uint3](https://developer.apple.com/documentation/metal/mtlattributeformat/uint3)Added [MTLAttributeFormat.uint4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuint4)Added [MTLAttributeFormat.ushort2](https://developer.apple.com/documentation/metal/mtlattributeformat/ushort2)Added [MTLAttributeFormat.ushort2Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatushort2normalized)Added [MTLAttributeFormat.ushort3](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatushort3)Added [MTLAttributeFormat.ushort3Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/ushort3normalized)Added [MTLAttributeFormat.ushort4](https://developer.apple.com/documentation/metal/mtlattributeformat/ushort4)Added [MTLAttributeFormat.ushort4Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/ushort4normalized)Added [MTLBlitCommandEncoder.updateFence(_: MTLFence)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1649359-updatefence)Added [MTLBlitCommandEncoder.waitForFence(_: MTLFence)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1649358-waitforfence)Added [MTLBuffer.addDebugMarker(_: String, range: NSRange)](https://developer.apple.com/documentation/metal/mtlbuffer/1779576-adddebugmarker)Added [MTLBuffer.removeAllDebugMarkers()](https://developer.apple.com/documentation/metal/mtlbuffer/1779577-removealldebugmarkers)Added [MTLBufferLayoutDescriptor](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor)Added [MTLBufferLayoutDescriptor.stepFunction](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/2097182-stepfunction)Added [MTLBufferLayoutDescriptor.stepRate](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/2097164-steprate)Added [MTLBufferLayoutDescriptor.stride](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/2097190-stride)Added [MTLBufferLayoutDescriptorArray](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptorarray)Added [MTLBufferLayoutDescriptorArray.subscript(_: Int) -> MTLBufferLayoutDescriptor](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptorarray/2097228-subscript)Added [MTLCommandBufferErrorDomain.memoryless](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/code/memoryless)Added [MTLComputeCommandEncoder.setStageInRegion(_: MTLRegion)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/2097047-setstageinregion)Added [MTLComputeCommandEncoder.updateFence(_: MTLFence)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1649789-updatefence)Added [MTLComputeCommandEncoder.waitForFence(_: MTLFence)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1649790-waitforfence)Added [MTLComputePipelineDescriptor.stageInputDescriptor](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/2092373-stageinputdescriptor)Added [MTLDevice.heapBufferSizeAndAlign() -> MTLSizeAndAlign](https://developer.apple.com/documentation/metal/mtldevice/1649922-heapbuffersizeandalign)Added [MTLDevice.heapTextureSizeAndAlign(descriptor: MTLTextureDescriptor) -> MTLSizeAndAlign](https://developer.apple.com/documentation/metal/mtldevice/1649927-heaptexturesizeandalignwithdescr)Added [MTLDevice.makeDefaultLibrary(bundle: Bundle) throws -> MTLLibrary](https://developer.apple.com/documentation/metal/mtldevice/2177054-newdefaultlibrarywithbundle)Added [MTLDevice.makeFence() -> MTLFence](https://developer.apple.com/documentation/metal/mtldevice/1649923-newfence)Added [MTLDevice.makeHeap(descriptor: MTLHeapDescriptor) -> MTLHeap](https://developer.apple.com/documentation/metal/mtldevice/1649928-makeheap)Added [MTLDrawPatchIndirectArguments [struct]](https://developer.apple.com/documentation/metal/mtldrawpatchindirectarguments)Added [MTLDrawPatchIndirectArguments.baseInstance](https://developer.apple.com/documentation/metal/mtldrawpatchindirectarguments/1639938-baseinstance)Added [MTLDrawPatchIndirectArguments.init()](https://developer.apple.com/documentation/metal/mtldrawpatchindirectarguments/1639941-init)Added [MTLDrawPatchIndirectArguments.init(patchCount: UInt32, instanceCount: UInt32, patchStart: UInt32, baseInstance: UInt32)](https://developer.apple.com/documentation/metal/mtldrawpatchindirectarguments/1640032-init)Added [MTLDrawPatchIndirectArguments.instanceCount](https://developer.apple.com/documentation/metal/mtldrawpatchindirectarguments/1640058-instancecount)Added [MTLDrawPatchIndirectArguments.patchCount](https://developer.apple.com/documentation/metal/mtldrawpatchindirectarguments/1639945-patchcount)Added [MTLDrawPatchIndirectArguments.patchStart](https://developer.apple.com/documentation/metal/mtldrawpatchindirectarguments/1639980-patchstart)Added [MTLFeatureSet.tvOS_GPUFamily1_v1](https://developer.apple.com/documentation/metal/mtlfeatureset/mtlfeatureset_tvos_gpufamily1_v1)Added [MTLFeatureSet.tvOS_GPUFamily1_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/tvos_gpufamily1_v2)Added [MTLFence](https://developer.apple.com/documentation/metal/mtlfence)Added [MTLFence.device](https://developer.apple.com/documentation/metal/mtlfence/1648532-device)Added [MTLFence.label](https://developer.apple.com/documentation/metal/mtlfence/1648531-label)Added [MTLFunction.functionConstantsDictionary](https://developer.apple.com/documentation/metal/mtlfunction/2314777-functionconstantsdictionary)Added [MTLFunction.label](https://developer.apple.com/documentation/metal/mtlfunction/1640034-label)Added [MTLFunction.patchControlPointCount](https://developer.apple.com/documentation/metal/mtlfunction/1639890-patchcontrolpointcount)Added [MTLFunction.patchType](https://developer.apple.com/documentation/metal/mtlfunction/1639909-patchtype)Added [MTLFunction.stageInputAttributes](https://developer.apple.com/documentation/metal/mtlfunction/2097159-stageinputattributes)Added [MTLFunctionConstant](https://developer.apple.com/documentation/metal/mtlfunctionconstant)Added [MTLFunctionConstant.index](https://developer.apple.com/documentation/metal/mtlfunctionconstant/1639905-index)Added [MTLFunctionConstant.name](https://developer.apple.com/documentation/metal/mtlfunctionconstant/1639955-name)Added [MTLFunctionConstant.required](https://developer.apple.com/documentation/metal/mtlfunctionconstant/1639988-required)Added [MTLFunctionConstant.type](https://developer.apple.com/documentation/metal/mtlfunctionconstant/1639950-type)Added [MTLFunctionConstantValues](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues)Added [MTLFunctionConstantValues.reset()](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/1639526-reset)Added [MTLFunctionConstantValues.setConstantValue(_: UnsafeRawPointer, type: MTLDataType, at: Int)](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/1639531-setconstantvalue)Added [MTLFunctionConstantValues.setConstantValue(_: UnsafeRawPointer, type: MTLDataType, withName: String)](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/1639530-setconstantvalue)Added [MTLFunctionConstantValues.setConstantValues(_: UnsafeRawPointer, type: MTLDataType, with: NSRange)](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/1639527-setconstantvalues)Added [MTLHeap](https://developer.apple.com/documentation/metal/mtlheap)Added [MTLHeap.cpuCacheMode](https://developer.apple.com/documentation/metal/mtlheap/1771280-cpucachemode)Added [MTLHeap.device](https://developer.apple.com/documentation/metal/mtlheap/1771285-device)Added [MTLHeap.label](https://developer.apple.com/documentation/metal/mtlheap/1771279-label)Added [MTLHeap.makeBuffer() -> MTLBuffer](https://developer.apple.com/documentation/metal/mtlheap/1649571-makebuffer)Added [MTLHeap.makeTexture(descriptor: MTLTextureDescriptor) -> MTLTexture](https://developer.apple.com/documentation/metal/mtlheap/1649574-newtexturewithdescriptor)Added [MTLHeap.maxAvailableSize(alignment: Int) -> Int](https://developer.apple.com/documentation/metal/mtlheap/1771284-maxavailablesizewithalignment)Added [MTLHeap.setPurgeableState(_: MTLPurgeableState) -> MTLPurgeableState](https://developer.apple.com/documentation/metal/mtlheap/1771281-setpurgeablestate)Added [MTLHeap.size](https://developer.apple.com/documentation/metal/mtlheap/1649569-size)Added [MTLHeap.storageMode](https://developer.apple.com/documentation/metal/mtlheap/1771282-storagemode)Added [MTLHeap.usedSize](https://developer.apple.com/documentation/metal/mtlheap/2097557-usedsize)Added [MTLHeapDescriptor](https://developer.apple.com/documentation/metal/mtlheapdescriptor)Added [MTLHeapDescriptor.cpuCacheMode](https://developer.apple.com/documentation/metal/mtlheapdescriptor/1649573-cpucachemode)Added [MTLHeapDescriptor.size](https://developer.apple.com/documentation/metal/mtlheapdescriptor/1649568-size)Added [MTLHeapDescriptor.storageMode](https://developer.apple.com/documentation/metal/mtlheapdescriptor/1649567-storagemode)Added [MTLLanguageVersion.version1_2](https://developer.apple.com/documentation/metal/mtllanguageversion/mtllanguageversion1_2)Added [MTLLibrary.makeFunction(name: String, constantValues: MTLFunctionConstantValues) throws -> MTLFunction](https://developer.apple.com/documentation/metal/mtllibrary/1640020-makefunction)Added [MTLLibrary.makeFunction(name: String, constantValues: MTLFunctionConstantValues, completionHandler: (MTLFunction?, Error) -> Swift.Void)](https://developer.apple.com/documentation/metal/mtllibrary/1640053-newfunctionwithname)Added [MTLLibraryErrorDomain.fileNotFound](https://developer.apple.com/documentation/metal/mtllibraryerror/code/filenotfound)Added [MTLLibraryErrorDomain.functionNotFound](https://developer.apple.com/documentation/metal/mtllibraryerror/mtllibraryerrorfunctionnotfound)Added [MTLParallelRenderCommandEncoder.setColorStoreAction(_: MTLStoreAction, at: Int)](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/1639891-setcolorstoreaction)Added [MTLParallelRenderCommandEncoder.setDepthStoreAction(_: MTLStoreAction)](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/1639937-setdepthstoreaction)Added [MTLParallelRenderCommandEncoder.setStencilStoreAction(_: MTLStoreAction)](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/1640016-setstencilstoreaction)Added [MTLPatchType [enum]](https://developer.apple.com/documentation/metal/mtlpatchtype)Added [MTLPatchType.none](https://developer.apple.com/documentation/metal/mtlpatchtype/mtlpatchtypenone)Added [MTLPatchType.quad](https://developer.apple.com/documentation/metal/mtlpatchtype/quad)Added [MTLPatchType.triangle](https://developer.apple.com/documentation/metal/mtlpatchtype/mtlpatchtypetriangle)Added [MTLPixelFormat.bgr10_xr](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10_xr)Added [MTLPixelFormat.bgr10_xr_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatbgr10_xr_srgb)Added [MTLPixelFormat.BGRA10_XR](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra10_xr)Added [MTLPixelFormat.bgra10_XR_sRGB](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra10_xr_srgb)Added [MTLPixelFormat.x32_stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/x32_stencil8)Added [MTLQuadTessellationFactorsHalf [struct]](https://developer.apple.com/documentation/metal/mtlquadtessellationfactorshalf)Added [MTLQuadTessellationFactorsHalf.edgeTessellationFactor](https://developer.apple.com/documentation/metal/mtlquadtessellationfactorshalf/1639974-edgetessellationfactor)Added [MTLQuadTessellationFactorsHalf.init()](https://developer.apple.com/documentation/metal/mtlquadtessellationfactorshalf/1639906-init)Added [MTLQuadTessellationFactorsHalf.init(edgeTessellationFactor: (UInt16, UInt16, UInt16, UInt16), insideTessellationFactor: (UInt16, UInt16))](https://developer.apple.com/documentation/metal/mtlquadtessellationfactorshalf/1640001-init)Added [MTLQuadTessellationFactorsHalf.insideTessellationFactor](https://developer.apple.com/documentation/metal/mtlquadtessellationfactorshalf/1639968-insidetessellationfactor)Added [MTLRenderCommandEncoder.drawIndexedPatches(numberOfPatchControlPoints: Int, patchStart: Int, patchCount: Int, patchIndexBuffer: MTLBuffer?, patchIndexBufferOffset: Int, controlPointIndexBuffer: MTLBuffer, controlPointIndexBufferOffset: Int, instanceCount: Int, baseInstance: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1640031-drawindexedpatches)Added [MTLRenderCommandEncoder.drawPatches(numberOfPatchControlPoints: Int, patchStart: Int, patchCount: Int, patchIndexBuffer: MTLBuffer?, patchIndexBufferOffset: Int, instanceCount: Int, baseInstance: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1639984-drawpatches)Added [MTLRenderCommandEncoder.setColorStoreAction(_: MTLStoreAction, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1640054-setcolorstoreaction)Added [MTLRenderCommandEncoder.setDepthStoreAction(_: MTLStoreAction)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1640036-setdepthstoreaction)Added [MTLRenderCommandEncoder.setStencilStoreAction(_: MTLStoreAction)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1639936-setstencilstoreaction)Added [MTLRenderCommandEncoder.setTessellationFactorBuffer(_: MTLBuffer?, offset: Int, instanceStride: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1640035-settessellationfactorbuffer)Added [MTLRenderCommandEncoder.setTessellationFactorScale(_: Float)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1639992-settessellationfactorscale)Added [MTLRenderCommandEncoder.update(_: MTLFence, after: MTLRenderStages)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1648377-updatefence)Added [MTLRenderCommandEncoder.wait(for: MTLFence, before: MTLRenderStages)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1648378-waitforfence)Added [MTLRenderPipelineDescriptor.isTessellationFactorScaleEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1640045-istessellationfactorscaleenabled)Added [MTLRenderPipelineDescriptor.maxTessellationFactor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1640060-maxtessellationfactor)Added [MTLRenderPipelineDescriptor.tessellationControlPointIndexType](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1640059-tessellationcontrolpointindextyp)Added [MTLRenderPipelineDescriptor.tessellationFactorFormat](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1639951-tessellationfactorformat)Added [MTLRenderPipelineDescriptor.tessellationFactorStepFunction](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1640062-tessellationfactorstepfunction)Added [MTLRenderPipelineDescriptor.tessellationOutputWindingOrder](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1639911-tessellationoutputwindingorder)Added [MTLRenderPipelineDescriptor.tessellationPartitionMode](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1639979-tessellationpartitionmode)Added [MTLRenderStages [struct]](https://developer.apple.com/documentation/metal/mtlrenderstages)Added [MTLRenderStages.fragment](https://developer.apple.com/documentation/metal/mtlrenderstages/1648376-fragment)Added [MTLRenderStages.init(rawValue: UInt)](https://developer.apple.com/documentation/metal/mtlrenderstages/1650064-init)Added [MTLRenderStages.vertex](https://developer.apple.com/documentation/metal/mtlrenderstages/1648380-vertex)Added [MTLResource.heap](https://developer.apple.com/documentation/metal/mtlresource/1682333-heap)Added [MTLResource.isAliasable() -> Bool](https://developer.apple.com/documentation/metal/mtlresource/1771702-isaliasable)Added [MTLResource.makeAliasable()](https://developer.apple.com/documentation/metal/mtlresource/1771705-makealiasable)Added [MTLResourceOptions.hazardTrackingModeUntracked](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcehazardtrackingmodeuntracked)Added [MTLResourceOptions.storageModeMemoryless](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcestoragemodememoryless)Added [MTLSamplerBorderColor [enum]](https://developer.apple.com/documentation/metal/mtlsamplerbordercolor)Added [MTLSamplerBorderColor.opaqueBlack](https://developer.apple.com/documentation/metal/mtlsamplerbordercolor/mtlsamplerbordercoloropaqueblack)Added [MTLSamplerBorderColor.opaqueWhite](https://developer.apple.com/documentation/metal/mtlsamplerbordercolor/mtlsamplerbordercoloropaquewhite)Added [MTLSamplerBorderColor.transparentBlack](https://developer.apple.com/documentation/metal/mtlsamplerbordercolor/mtlsamplerbordercolortransparentblack)Added [MTLSizeAndAlign [struct]](https://developer.apple.com/documentation/metal/mtlsizeandalign)Added [MTLSizeAndAlign.align](https://developer.apple.com/documentation/metal/mtlsizeandalign/1649926-align)Added [MTLSizeAndAlign.init()](https://developer.apple.com/documentation/metal/mtlsizeandalign/1650063-init)Added [MTLSizeAndAlign.init(size: Int, align: Int)](https://developer.apple.com/documentation/metal/mtlsizeandalign/1650062-init)Added [MTLSizeAndAlign.size](https://developer.apple.com/documentation/metal/mtlsizeandalign/1649924-size)Added [MTLStageInputOutputDescriptor](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor)Added [MTLStageInputOutputDescriptor.attributes](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097206-attributes)Added [MTLStageInputOutputDescriptor.indexBufferIndex](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097237-indexbufferindex)Added [MTLStageInputOutputDescriptor.indexType](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097184-indextype)Added [MTLStageInputOutputDescriptor.layouts](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097202-layouts)Added [MTLStageInputOutputDescriptor.reset()](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097185-reset)Added [MTLStepFunction [enum]](https://developer.apple.com/documentation/metal/mtlstepfunction)Added [MTLStepFunction.constant](https://developer.apple.com/documentation/metal/mtlstepfunction/mtlstepfunctionconstant)Added [MTLStepFunction.perInstance](https://developer.apple.com/documentation/metal/mtlstepfunction/perinstance)Added [MTLStepFunction.perPatch](https://developer.apple.com/documentation/metal/mtlstepfunction/mtlstepfunctionperpatch)Added [MTLStepFunction.perPatchControlPoint](https://developer.apple.com/documentation/metal/mtlstepfunction/perpatchcontrolpoint)Added [MTLStepFunction.perVertex](https://developer.apple.com/documentation/metal/mtlstepfunction/pervertex)Added [MTLStepFunction.threadPositionInGridX](https://developer.apple.com/documentation/metal/mtlstepfunction/mtlstepfunctionthreadpositioningridx)Added [MTLStepFunction.threadPositionInGridXIndexed](https://developer.apple.com/documentation/metal/mtlstepfunction/threadpositioningridxindexed)Added [MTLStepFunction.threadPositionInGridY](https://developer.apple.com/documentation/metal/mtlstepfunction/threadpositioningridy)Added [MTLStepFunction.threadPositionInGridYIndexed](https://developer.apple.com/documentation/metal/mtlstepfunction/threadpositioningridyindexed)Added [MTLStorageMode.memoryless](https://developer.apple.com/documentation/metal/mtlstoragemode/mtlstoragemodememoryless)Added [MTLStoreAction.storeAndMultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/storeandmultisampleresolve)Added [MTLStoreAction.unknown](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionunknown)Added [MTLTessellationControlPointIndexType [enum]](https://developer.apple.com/documentation/metal/mtltessellationcontrolpointindextype)Added [MTLTessellationControlPointIndexType.none](https://developer.apple.com/documentation/metal/mtltessellationcontrolpointindextype/mtltessellationcontrolpointindextypenone)Added [MTLTessellationControlPointIndexType.uint16](https://developer.apple.com/documentation/metal/mtltessellationcontrolpointindextype/mtltessellationcontrolpointindextypeuint16)Added [MTLTessellationControlPointIndexType.uint32](https://developer.apple.com/documentation/metal/mtltessellationcontrolpointindextype/mtltessellationcontrolpointindextypeuint32)Added [MTLTessellationFactorFormat [enum]](https://developer.apple.com/documentation/metal/mtltessellationfactorformat)Added [MTLTessellationFactorFormat.half](https://developer.apple.com/documentation/metal/mtltessellationfactorformat/mtltessellationfactorformathalf)Added [MTLTessellationFactorStepFunction [enum]](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction)Added [MTLTessellationFactorStepFunction.constant](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/constant)Added [MTLTessellationFactorStepFunction.perInstance](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/perinstance)Added [MTLTessellationFactorStepFunction.perPatch](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/perpatch)Added [MTLTessellationFactorStepFunction.perPatchAndPerInstance](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/mtltessellationfactorstepfunctionperpatchandperinstance)Added [MTLTessellationPartitionMode [enum]](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode)Added [MTLTessellationPartitionMode.fractionalEven](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode/fractionaleven)Added [MTLTessellationPartitionMode.fractionalOdd](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode/fractionalodd)Added [MTLTessellationPartitionMode.integer](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode/mtltessellationpartitionmodeinteger)Added [MTLTessellationPartitionMode.pow2](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode/pow2)Added [MTLTriangleTessellationFactorsHalf [struct]](https://developer.apple.com/documentation/metal/mtltriangletessellationfactorshalf)Added [MTLTriangleTessellationFactorsHalf.edgeTessellationFactor](https://developer.apple.com/documentation/metal/mtltriangletessellationfactorshalf/1640010-edgetessellationfactor)Added [MTLTriangleTessellationFactorsHalf.init()](https://developer.apple.com/documentation/metal/mtltriangletessellationfactorshalf/1640040-init)Added [MTLTriangleTessellationFactorsHalf.init(edgeTessellationFactor: (UInt16, UInt16, UInt16), insideTessellationFactor: UInt16)](https://developer.apple.com/documentation/metal/mtltriangletessellationfactorshalf/1639990-init)Added [MTLTriangleTessellationFactorsHalf.insideTessellationFactor](https://developer.apple.com/documentation/metal/mtltriangletessellationfactorshalf/1639953-insidetessellationfactor)Added [MTLVertexAttribute.isPatchControlPointData](https://developer.apple.com/documentation/metal/mtlvertexattribute/1640013-patchcontrolpointdata)Added [MTLVertexAttribute.isPatchData](https://developer.apple.com/documentation/metal/mtlvertexattribute/1640002-patchdata)Added [MTLVertexStepFunction.perPatch](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/perpatch)Added [MTLVertexStepFunction.perPatchControlPoint](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/perpatchcontrolpoint)Added MTLResourceHazardTrackingModeShiftModified [MTLArgument](https://developer.apple.com/documentation/metal/mtlargument)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLArgument : NSObject {     var name: String { get }     var type: MTLArgumentType { get }     var access: MTLArgumentAccess { get }     var index: Int { get }     var active: Bool { get }     var bufferAlignment: Int { get }     var bufferDataSize: Int { get }     var bufferDataType: MTLDataType { get }     var bufferStructType: MTLStructType { get }     var threadgroupMemoryAlignment: Int { get }     var threadgroupMemoryDataSize: Int { get }     var textureType: MTLTextureType { get }     var textureDataType: MTLDataType { get } } ``` | -- |
| To | ``` class MTLArgument : NSObject {     var name: String { get }     var type: MTLArgumentType { get }     var access: MTLArgumentAccess { get }     var index: Int { get }     var isActive: Bool { get }     var bufferAlignment: Int { get }     var bufferDataSize: Int { get }     var bufferDataType: MTLDataType { get }     var bufferStructType: MTLStructType { get }     var threadgroupMemoryAlignment: Int { get }     var threadgroupMemoryDataSize: Int { get }     var textureType: MTLTextureType { get }     var textureDataType: MTLDataType { get }     var isDepthTexture: Bool { get }     var arrayLength: Int { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLArgument : CVarArg { } extension MTLArgument : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLArgument.isActive](https://developer.apple.com/documentation/metal/mtlargument/1461891-isactive)

|  | Declaration |
| --- | --- |
| From | ``` var active: Bool { get } ``` |
| To | ``` var isActive: Bool { get } ``` |

Modified [MTLArgumentAccess [enum]](https://developer.apple.com/documentation/metal/mtlargumentaccess)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLArgumentAccess : UInt {     case ReadOnly     case ReadWrite     case WriteOnly } ``` |
| To | ``` enum MTLArgumentAccess : UInt {     case readOnly     case readWrite     case writeOnly } ``` |

Modified [MTLArgumentAccess.readOnly](https://developer.apple.com/documentation/metal/mtlargumentaccess/readonly)

|  | Declaration |
| --- | --- |
| From | ``` case ReadOnly ``` |
| To | ``` case readOnly ``` |

Modified [MTLArgumentAccess.readWrite](https://developer.apple.com/documentation/metal/mtlargumentaccess/mtlargumentaccessreadwrite)

|  | Declaration |
| --- | --- |
| From | ``` case ReadWrite ``` |
| To | ``` case readWrite ``` |

Modified [MTLArgumentAccess.writeOnly](https://developer.apple.com/documentation/metal/mtlargumentaccess/mtlargumentaccesswriteonly)

|  | Declaration |
| --- | --- |
| From | ``` case WriteOnly ``` |
| To | ``` case writeOnly ``` |

Modified [MTLArgumentType [enum]](https://developer.apple.com/documentation/metal/mtlargumenttype)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLArgumentType : UInt {     case Buffer     case ThreadgroupMemory     case Texture     case Sampler } ``` |
| To | ``` enum MTLArgumentType : UInt {     case buffer     case threadgroupMemory     case texture     case sampler } ``` |

Modified [MTLArgumentType.buffer](https://developer.apple.com/documentation/metal/mtlargumenttype/buffer)

|  | Declaration |
| --- | --- |
| From | ``` case Buffer ``` |
| To | ``` case buffer ``` |

Modified [MTLArgumentType.sampler](https://developer.apple.com/documentation/metal/mtlargumenttype/sampler)

|  | Declaration |
| --- | --- |
| From | ``` case Sampler ``` |
| To | ``` case sampler ``` |

Modified [MTLArgumentType.texture](https://developer.apple.com/documentation/metal/mtlargumenttype/mtlargumenttypetexture)

|  | Declaration |
| --- | --- |
| From | ``` case Texture ``` |
| To | ``` case texture ``` |

Modified [MTLArgumentType.threadgroupMemory](https://developer.apple.com/documentation/metal/mtlargumenttype/threadgroupmemory)

|  | Declaration |
| --- | --- |
| From | ``` case ThreadgroupMemory ``` |
| To | ``` case threadgroupMemory ``` |

Modified [MTLArrayType](https://developer.apple.com/documentation/metal/mtlarraytype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLArrayType : NSObject {     var arrayLength: Int { get }     var elementType: MTLDataType { get }     var stride: Int { get }     func elementStructType() -> MTLStructType?     func elementArrayType() -> MTLArrayType? } ``` | -- |
| To | ``` class MTLArrayType : NSObject {     var arrayLength: Int { get }     var elementType: MTLDataType { get }     var stride: Int { get }     func elementStructType() -> MTLStructType?     func element() -> MTLArrayType?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLArrayType : CVarArg { } extension MTLArrayType : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLArrayType.element() -> MTLArrayType?](https://developer.apple.com/documentation/metal/mtlarraytype/1461963-element)

|  | Declaration |
| --- | --- |
| From | ``` func elementArrayType() -> MTLArrayType? ``` |
| To | ``` func element() -> MTLArrayType? ``` |

Modified [MTLBlendFactor [enum]](https://developer.apple.com/documentation/metal/mtlblendfactor)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLBlendFactor : UInt {     case Zero     case One     case SourceColor     case OneMinusSourceColor     case SourceAlpha     case OneMinusSourceAlpha     case DestinationColor     case OneMinusDestinationColor     case DestinationAlpha     case OneMinusDestinationAlpha     case SourceAlphaSaturated     case BlendColor     case OneMinusBlendColor     case BlendAlpha     case OneMinusBlendAlpha } ``` |
| To | ``` enum MTLBlendFactor : UInt {     case zero     case one     case sourceColor     case oneMinusSourceColor     case sourceAlpha     case oneMinusSourceAlpha     case destinationColor     case oneMinusDestinationColor     case destinationAlpha     case oneMinusDestinationAlpha     case sourceAlphaSaturated     case blendColor     case oneMinusBlendColor     case blendAlpha     case oneMinusBlendAlpha } ``` |

Modified [MTLBlendFactor.blendAlpha](https://developer.apple.com/documentation/metal/mtlblendfactor/mtlblendfactorblendalpha)

|  | Declaration |
| --- | --- |
| From | ``` case BlendAlpha ``` |
| To | ``` case blendAlpha ``` |

Modified [MTLBlendFactor.blendColor](https://developer.apple.com/documentation/metal/mtlblendfactor/mtlblendfactorblendcolor)

|  | Declaration |
| --- | --- |
| From | ``` case BlendColor ``` |
| To | ``` case blendColor ``` |

Modified [MTLBlendFactor.destinationAlpha](https://developer.apple.com/documentation/metal/mtlblendfactor/destinationalpha)

|  | Declaration |
| --- | --- |
| From | ``` case DestinationAlpha ``` |
| To | ``` case destinationAlpha ``` |

Modified [MTLBlendFactor.destinationColor](https://developer.apple.com/documentation/metal/mtlblendfactor/destinationcolor)

|  | Declaration |
| --- | --- |
| From | ``` case DestinationColor ``` |
| To | ``` case destinationColor ``` |

Modified [MTLBlendFactor.one](https://developer.apple.com/documentation/metal/mtlblendfactor/mtlblendfactorone)

|  | Declaration |
| --- | --- |
| From | ``` case One ``` |
| To | ``` case one ``` |

Modified [MTLBlendFactor.oneMinusBlendAlpha](https://developer.apple.com/documentation/metal/mtlblendfactor/mtlblendfactoroneminusblendalpha)

|  | Declaration |
| --- | --- |
| From | ``` case OneMinusBlendAlpha ``` |
| To | ``` case oneMinusBlendAlpha ``` |

Modified [MTLBlendFactor.oneMinusBlendColor](https://developer.apple.com/documentation/metal/mtlblendfactor/oneminusblendcolor)

|  | Declaration |
| --- | --- |
| From | ``` case OneMinusBlendColor ``` |
| To | ``` case oneMinusBlendColor ``` |

Modified [MTLBlendFactor.oneMinusDestinationAlpha](https://developer.apple.com/documentation/metal/mtlblendfactor/oneminusdestinationalpha)

|  | Declaration |
| --- | --- |
| From | ``` case OneMinusDestinationAlpha ``` |
| To | ``` case oneMinusDestinationAlpha ``` |

Modified [MTLBlendFactor.oneMinusDestinationColor](https://developer.apple.com/documentation/metal/mtlblendfactor/oneminusdestinationcolor)

|  | Declaration |
| --- | --- |
| From | ``` case OneMinusDestinationColor ``` |
| To | ``` case oneMinusDestinationColor ``` |

Modified [MTLBlendFactor.oneMinusSourceAlpha](https://developer.apple.com/documentation/metal/mtlblendfactor/mtlblendfactoroneminussourcealpha)

|  | Declaration |
| --- | --- |
| From | ``` case OneMinusSourceAlpha ``` |
| To | ``` case oneMinusSourceAlpha ``` |

Modified [MTLBlendFactor.oneMinusSourceColor](https://developer.apple.com/documentation/metal/mtlblendfactor/oneminussourcecolor)

|  | Declaration |
| --- | --- |
| From | ``` case OneMinusSourceColor ``` |
| To | ``` case oneMinusSourceColor ``` |

Modified [MTLBlendFactor.sourceAlpha](https://developer.apple.com/documentation/metal/mtlblendfactor/mtlblendfactorsourcealpha)

|  | Declaration |
| --- | --- |
| From | ``` case SourceAlpha ``` |
| To | ``` case sourceAlpha ``` |

Modified [MTLBlendFactor.sourceAlphaSaturated](https://developer.apple.com/documentation/metal/mtlblendfactor/mtlblendfactorsourcealphasaturated)

|  | Declaration |
| --- | --- |
| From | ``` case SourceAlphaSaturated ``` |
| To | ``` case sourceAlphaSaturated ``` |

Modified [MTLBlendFactor.sourceColor](https://developer.apple.com/documentation/metal/mtlblendfactor/sourcecolor)

|  | Declaration |
| --- | --- |
| From | ``` case SourceColor ``` |
| To | ``` case sourceColor ``` |

Modified [MTLBlendFactor.zero](https://developer.apple.com/documentation/metal/mtlblendfactor/zero)

|  | Declaration |
| --- | --- |
| From | ``` case Zero ``` |
| To | ``` case zero ``` |

Modified [MTLBlendOperation [enum]](https://developer.apple.com/documentation/metal/mtlblendoperation)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLBlendOperation : UInt {     case Add     case Subtract     case ReverseSubtract     case Min     case Max } ``` |
| To | ``` enum MTLBlendOperation : UInt {     case add     case subtract     case reverseSubtract     case min     case max } ``` |

Modified [MTLBlendOperation.add](https://developer.apple.com/documentation/metal/mtlblendoperation/mtlblendoperationadd)

|  | Declaration |
| --- | --- |
| From | ``` case Add ``` |
| To | ``` case add ``` |

Modified [MTLBlendOperation.max](https://developer.apple.com/documentation/metal/mtlblendoperation/mtlblendoperationmax)

|  | Declaration |
| --- | --- |
| From | ``` case Max ``` |
| To | ``` case max ``` |

Modified [MTLBlendOperation.min](https://developer.apple.com/documentation/metal/mtlblendoperation/mtlblendoperationmin)

|  | Declaration |
| --- | --- |
| From | ``` case Min ``` |
| To | ``` case min ``` |

Modified [MTLBlendOperation.reverseSubtract](https://developer.apple.com/documentation/metal/mtlblendoperation/mtlblendoperationreversesubtract)

|  | Declaration |
| --- | --- |
| From | ``` case ReverseSubtract ``` |
| To | ``` case reverseSubtract ``` |

Modified [MTLBlendOperation.subtract](https://developer.apple.com/documentation/metal/mtlblendoperation/mtlblendoperationsubtract)

|  | Declaration |
| --- | --- |
| From | ``` case Subtract ``` |
| To | ``` case subtract ``` |

Modified [MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlblitcommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLBlitCommandEncoder : MTLCommandEncoder {     func synchronizeResource(_ resource: MTLResource)     func synchronizeTexture(_ texture: MTLTexture, slice slice: Int, level level: Int)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin, options options: MTLBlitOption)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int)     func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int, options options: MTLBlitOption)     func generateMipmapsForTexture(_ texture: MTLTexture)     func fillBuffer(_ buffer: MTLBuffer, range range: NSRange, value value: UInt8)     func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, size size: Int) } ``` |
| To | ``` protocol MTLBlitCommandEncoder : MTLCommandEncoder {     func synchronize(resource resource: MTLResource)     func synchronize(texture texture: MTLTexture, slice slice: Int, level level: Int)     func copy(from sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, to destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copy(from sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, to destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin)     func copy(from sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, to destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin, options options: MTLBlitOption)     func copy(from sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, to destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int)     func copy(from sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, to destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int, options options: MTLBlitOption)     func generateMipmaps(for texture: MTLTexture)     func fill(buffer buffer: MTLBuffer, range range: NSRange, value value: UInt8)     func copy(from sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, to destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, size size: Int)     func updateFence(_ fence: MTLFence)     func waitForFence(_ fence: MTLFence) } ``` |

Modified [MTLBlitCommandEncoder.copy(from: MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to: MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400752-copyfrombuffer)

|  | Declaration |
| --- | --- |
| From | ``` func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin) ``` |
| To | ``` func copy(from sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, to destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin) ``` |

Modified [MTLBlitCommandEncoder.copy(from: MTLBuffer, sourceOffset: Int, sourceBytesPerRow: Int, sourceBytesPerImage: Int, sourceSize: MTLSize, to: MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin, options: MTLBlitOption)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400771-copyfrombuffer)

|  | Declaration |
| --- | --- |
| From | ``` func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin, options options: MTLBlitOption) ``` |
| To | ``` func copy(from sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, sourceBytesPerRow sourceBytesPerRow: Int, sourceBytesPerImage sourceBytesPerImage: Int, sourceSize sourceSize: MTLSize, to destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin, options options: MTLBlitOption) ``` |

Modified [MTLBlitCommandEncoder.copy(from: MTLBuffer, sourceOffset: Int, to: MTLBuffer, destinationOffset: Int, size: Int)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400767-copyfrombuffer)

|  | Declaration |
| --- | --- |
| From | ``` func copyFromBuffer(_ sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, size size: Int) ``` |
| To | ``` func copy(from sourceBuffer: MTLBuffer, sourceOffset sourceOffset: Int, to destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, size size: Int) ``` |

Modified [MTLBlitCommandEncoder.copy(from: MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400773-copyfromtexture)

|  | Declaration |
| --- | --- |
| From | ``` func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int) ``` |
| To | ``` func copy(from sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, to destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int) ``` |

Modified [MTLBlitCommandEncoder.copy(from: MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: MTLBuffer, destinationOffset: Int, destinationBytesPerRow: Int, destinationBytesPerImage: Int, options: MTLBlitOption)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400756-copy)

|  | Declaration |
| --- | --- |
| From | ``` func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toBuffer destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int, options options: MTLBlitOption) ``` |
| To | ``` func copy(from sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, to destinationBuffer: MTLBuffer, destinationOffset destinationOffset: Int, destinationBytesPerRow destinationBytesPerRow: Int, destinationBytesPerImage destinationBytesPerImage: Int, options options: MTLBlitOption) ``` |

Modified [MTLBlitCommandEncoder.copy(from: MTLTexture, sourceSlice: Int, sourceLevel: Int, sourceOrigin: MTLOrigin, sourceSize: MTLSize, to: MTLTexture, destinationSlice: Int, destinationLevel: Int, destinationOrigin: MTLOrigin)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400754-copy)

|  | Declaration |
| --- | --- |
| From | ``` func copyFromTexture(_ sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, toTexture destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin) ``` |
| To | ``` func copy(from sourceTexture: MTLTexture, sourceSlice sourceSlice: Int, sourceLevel sourceLevel: Int, sourceOrigin sourceOrigin: MTLOrigin, sourceSize sourceSize: MTLSize, to destinationTexture: MTLTexture, destinationSlice destinationSlice: Int, destinationLevel destinationLevel: Int, destinationOrigin destinationOrigin: MTLOrigin) ``` |

Modified [MTLBlitCommandEncoder.fill(buffer: MTLBuffer, range: NSRange, value: UInt8)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400761-fillbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func fillBuffer(_ buffer: MTLBuffer, range range: NSRange, value value: UInt8) ``` |
| To | ``` func fill(buffer buffer: MTLBuffer, range range: NSRange, value value: UInt8) ``` |

Modified [MTLBlitCommandEncoder.generateMipmaps(for: MTLTexture)](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1400748-generatemipmapsfortexture)

|  | Declaration |
| --- | --- |
| From | ``` func generateMipmapsForTexture(_ texture: MTLTexture) ``` |
| To | ``` func generateMipmaps(for texture: MTLTexture) ``` |

Modified [MTLBlitOption [struct]](https://developer.apple.com/documentation/metal/mtlblitoption)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MTLBlitOption : OptionSetType {     init(rawValue rawValue: UInt)     static var None: MTLBlitOption { get }     static var DepthFromDepthStencil: MTLBlitOption { get }     static var StencilFromDepthStencil: MTLBlitOption { get }     static var RowLinearPVRTC: MTLBlitOption { get } } ``` | OptionSetType |
| To | ``` struct MTLBlitOption : OptionSet {     init(rawValue rawValue: UInt)     static var none: MTLBlitOption { get }     static var depthFromDepthStencil: MTLBlitOption { get }     static var stencilFromDepthStencil: MTLBlitOption { get }     static var rowLinearPVRTC: MTLBlitOption { get }     func intersect(_ other: MTLBlitOption) -> MTLBlitOption     func exclusiveOr(_ other: MTLBlitOption) -> MTLBlitOption     mutating func unionInPlace(_ other: MTLBlitOption)     mutating func intersectInPlace(_ other: MTLBlitOption)     mutating func exclusiveOrInPlace(_ other: MTLBlitOption)     func isSubsetOf(_ other: MTLBlitOption) -> Bool     func isDisjointWith(_ other: MTLBlitOption) -> Bool     func isSupersetOf(_ other: MTLBlitOption) -> Bool     mutating func subtractInPlace(_ other: MTLBlitOption)     func isStrictSupersetOf(_ other: MTLBlitOption) -> Bool     func isStrictSubsetOf(_ other: MTLBlitOption) -> Bool } extension MTLBlitOption {     func union(_ other: MTLBlitOption) -> MTLBlitOption     func intersection(_ other: MTLBlitOption) -> MTLBlitOption     func symmetricDifference(_ other: MTLBlitOption) -> MTLBlitOption } extension MTLBlitOption {     func contains(_ member: MTLBlitOption) -> Bool     mutating func insert(_ newMember: MTLBlitOption) -> (inserted: Bool, memberAfterInsert: MTLBlitOption)     mutating func remove(_ member: MTLBlitOption) -> MTLBlitOption?     mutating func update(with newMember: MTLBlitOption) -> MTLBlitOption? } extension MTLBlitOption {     convenience init()     mutating func formUnion(_ other: MTLBlitOption)     mutating func formIntersection(_ other: MTLBlitOption)     mutating func formSymmetricDifference(_ other: MTLBlitOption) } extension MTLBlitOption {     convenience init<S : Sequence where S.Iterator.Element == MTLBlitOption>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MTLBlitOption...)     mutating func subtract(_ other: MTLBlitOption)     func isSubset(of other: MTLBlitOption) -> Bool     func isSuperset(of other: MTLBlitOption) -> Bool     func isDisjoint(with other: MTLBlitOption) -> Bool     func subtracting(_ other: MTLBlitOption) -> MTLBlitOption     var isEmpty: Bool { get }     func isStrictSuperset(of other: MTLBlitOption) -> Bool     func isStrictSubset(of other: MTLBlitOption) -> Bool } ``` | OptionSet |

Modified [MTLBlitOption.depthFromDepthStencil](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptiondepthfromdepthstencil)

|  | Declaration |
| --- | --- |
| From | ``` static var DepthFromDepthStencil: MTLBlitOption { get } ``` |
| To | ``` static var depthFromDepthStencil: MTLBlitOption { get } ``` |

Modified [MTLBlitOption.rowLinearPVRTC](https://developer.apple.com/documentation/metal/mtlblitoption/mtlblitoptionrowlinearpvrtc)

|  | Declaration |
| --- | --- |
| From | ``` static var RowLinearPVRTC: MTLBlitOption { get } ``` |
| To | ``` static var rowLinearPVRTC: MTLBlitOption { get } ``` |

Modified [MTLBlitOption.stencilFromDepthStencil](https://developer.apple.com/documentation/metal/mtlblitoption/1400759-stencilfromdepthstencil)

|  | Declaration |
| --- | --- |
| From | ``` static var StencilFromDepthStencil: MTLBlitOption { get } ``` |
| To | ``` static var stencilFromDepthStencil: MTLBlitOption { get } ``` |

Modified [MTLBuffer](https://developer.apple.com/documentation/metal/mtlbuffer)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLBuffer : MTLResource {     var length: Int { get }     func contents() -> UnsafeMutablePointer<Void>     func didModifyRange(_ range: NSRange)     func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor, offset offset: Int, bytesPerRow bytesPerRow: Int) -> MTLTexture } ``` |
| To | ``` protocol MTLBuffer : MTLResource {     var length: Int { get }     func contents() -> UnsafeMutableRawPointer     func didModifyRange(_ range: NSRange)     func makeTexture(descriptor descriptor: MTLTextureDescriptor, offset offset: Int, bytesPerRow bytesPerRow: Int) -> MTLTexture     func addDebugMarker(_ marker: String, range range: NSRange)     func removeAllDebugMarkers() } ``` |

Modified [MTLBuffer.contents() -> UnsafeMutableRawPointer](https://developer.apple.com/documentation/metal/mtlbuffer/1515716-contents)

|  | Declaration |
| --- | --- |
| From | ``` func contents() -> UnsafeMutablePointer<Void> ``` |
| To | ``` func contents() -> UnsafeMutableRawPointer ``` |

Modified [MTLBuffer.makeTexture(descriptor: MTLTextureDescriptor, offset: Int, bytesPerRow: Int) -> MTLTexture](https://developer.apple.com/documentation/metal/mtlbuffer/1613852-newtexturewithdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor, offset offset: Int, bytesPerRow bytesPerRow: Int) -> MTLTexture ``` |
| To | ``` func makeTexture(descriptor descriptor: MTLTextureDescriptor, offset offset: Int, bytesPerRow bytesPerRow: Int) -> MTLTexture ``` |

Modified [MTLColorWriteMask [struct]](https://developer.apple.com/documentation/metal/mtlcolorwritemask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MTLColorWriteMask : OptionSetType {     init(rawValue rawValue: UInt)     static var None: MTLColorWriteMask { get }     static var Red: MTLColorWriteMask { get }     static var Green: MTLColorWriteMask { get }     static var Blue: MTLColorWriteMask { get }     static var Alpha: MTLColorWriteMask { get }     static var All: MTLColorWriteMask { get } } ``` | OptionSetType |
| To | ``` struct MTLColorWriteMask : OptionSet {     init(rawValue rawValue: UInt)     static var none: MTLColorWriteMask { get }     static var red: MTLColorWriteMask { get }     static var green: MTLColorWriteMask { get }     static var blue: MTLColorWriteMask { get }     static var alpha: MTLColorWriteMask { get }     static var all: MTLColorWriteMask { get }     func intersect(_ other: MTLColorWriteMask) -> MTLColorWriteMask     func exclusiveOr(_ other: MTLColorWriteMask) -> MTLColorWriteMask     mutating func unionInPlace(_ other: MTLColorWriteMask)     mutating func intersectInPlace(_ other: MTLColorWriteMask)     mutating func exclusiveOrInPlace(_ other: MTLColorWriteMask)     func isSubsetOf(_ other: MTLColorWriteMask) -> Bool     func isDisjointWith(_ other: MTLColorWriteMask) -> Bool     func isSupersetOf(_ other: MTLColorWriteMask) -> Bool     mutating func subtractInPlace(_ other: MTLColorWriteMask)     func isStrictSupersetOf(_ other: MTLColorWriteMask) -> Bool     func isStrictSubsetOf(_ other: MTLColorWriteMask) -> Bool } extension MTLColorWriteMask {     func union(_ other: MTLColorWriteMask) -> MTLColorWriteMask     func intersection(_ other: MTLColorWriteMask) -> MTLColorWriteMask     func symmetricDifference(_ other: MTLColorWriteMask) -> MTLColorWriteMask } extension MTLColorWriteMask {     func contains(_ member: MTLColorWriteMask) -> Bool     mutating func insert(_ newMember: MTLColorWriteMask) -> (inserted: Bool, memberAfterInsert: MTLColorWriteMask)     mutating func remove(_ member: MTLColorWriteMask) -> MTLColorWriteMask?     mutating func update(with newMember: MTLColorWriteMask) -> MTLColorWriteMask? } extension MTLColorWriteMask {     convenience init()     mutating func formUnion(_ other: MTLColorWriteMask)     mutating func formIntersection(_ other: MTLColorWriteMask)     mutating func formSymmetricDifference(_ other: MTLColorWriteMask) } extension MTLColorWriteMask {     convenience init<S : Sequence where S.Iterator.Element == MTLColorWriteMask>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MTLColorWriteMask...)     mutating func subtract(_ other: MTLColorWriteMask)     func isSubset(of other: MTLColorWriteMask) -> Bool     func isSuperset(of other: MTLColorWriteMask) -> Bool     func isDisjoint(with other: MTLColorWriteMask) -> Bool     func subtracting(_ other: MTLColorWriteMask) -> MTLColorWriteMask     var isEmpty: Bool { get }     func isStrictSuperset(of other: MTLColorWriteMask) -> Bool     func isStrictSubset(of other: MTLColorWriteMask) -> Bool } ``` | OptionSet |

Modified [MTLColorWriteMask.all](https://developer.apple.com/documentation/metal/mtlcolorwritemask/1514695-all)

|  | Declaration |
| --- | --- |
| From | ``` static var All: MTLColorWriteMask { get } ``` |
| To | ``` static var all: MTLColorWriteMask { get } ``` |

Modified [MTLColorWriteMask.alpha](https://developer.apple.com/documentation/metal/mtlcolorwritemask/1514664-alpha)

|  | Declaration |
| --- | --- |
| From | ``` static var Alpha: MTLColorWriteMask { get } ``` |
| To | ``` static var alpha: MTLColorWriteMask { get } ``` |

Modified [MTLColorWriteMask.blue](https://developer.apple.com/documentation/metal/mtlcolorwritemask/mtlcolorwritemaskblue)

|  | Declaration |
| --- | --- |
| From | ``` static var Blue: MTLColorWriteMask { get } ``` |
| To | ``` static var blue: MTLColorWriteMask { get } ``` |

Modified [MTLColorWriteMask.green](https://developer.apple.com/documentation/metal/mtlcolorwritemask/mtlcolorwritemaskgreen)

|  | Declaration |
| --- | --- |
| From | ``` static var Green: MTLColorWriteMask { get } ``` |
| To | ``` static var green: MTLColorWriteMask { get } ``` |

Modified [MTLColorWriteMask.red](https://developer.apple.com/documentation/metal/mtlcolorwritemask/1514653-red)

|  | Declaration |
| --- | --- |
| From | ``` static var Red: MTLColorWriteMask { get } ``` |
| To | ``` static var red: MTLColorWriteMask { get } ``` |

Modified [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLCommandBuffer : NSObjectProtocol {     var device: MTLDevice { get }     var commandQueue: MTLCommandQueue { get }     var retainedReferences: Bool { get }     var label: String? { get set }     func enqueue()     func commit()     func addScheduledHandler(_ block: MTLCommandBufferHandler)     func presentDrawable(_ drawable: MTLDrawable)     func presentDrawable(_ drawable: MTLDrawable, atTime presentationTime: CFTimeInterval)     func waitUntilScheduled()     func addCompletedHandler(_ block: MTLCommandBufferHandler)     func waitUntilCompleted()     var status: MTLCommandBufferStatus { get }     var error: NSError? { get }     func blitCommandEncoder() -> MTLBlitCommandEncoder     func renderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder     func computeCommandEncoder() -> MTLComputeCommandEncoder     func parallelRenderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder } ``` |
| To | ``` protocol MTLCommandBuffer : NSObjectProtocol {     var device: MTLDevice { get }     var commandQueue: MTLCommandQueue { get }     var retainedReferences: Bool { get }     var label: String? { get set }     func enqueue()     func commit()     func addScheduledHandler(_ block: Metal.MTLCommandBufferHandler)     func present(_ drawable: MTLDrawable)     func present(_ drawable: MTLDrawable, atTime presentationTime: CFTimeInterval)     func waitUntilScheduled()     func addCompletedHandler(_ block: Metal.MTLCommandBufferHandler)     func waitUntilCompleted()     var status: MTLCommandBufferStatus { get }     var error: Error? { get }     func makeBlitCommandEncoder() -> MTLBlitCommandEncoder     func makeRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder     func makeComputeCommandEncoder() -> MTLComputeCommandEncoder     func makeParallelRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder } ``` |

Modified [MTLCommandBuffer.addCompletedHandler(_: Metal.MTLCommandBufferHandler)](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442997-addcompletedhandler)

|  | Declaration |
| --- | --- |
| From | ``` func addCompletedHandler(_ block: MTLCommandBufferHandler) ``` |
| To | ``` func addCompletedHandler(_ block: Metal.MTLCommandBufferHandler) ``` |

Modified [MTLCommandBuffer.addScheduledHandler(_: Metal.MTLCommandBufferHandler)](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442991-addscheduledhandler)

|  | Declaration |
| --- | --- |
| From | ``` func addScheduledHandler(_ block: MTLCommandBufferHandler) ``` |
| To | ``` func addScheduledHandler(_ block: Metal.MTLCommandBufferHandler) ``` |

Modified [MTLCommandBuffer.error](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443040-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [MTLCommandBuffer.makeBlitCommandEncoder() -> MTLBlitCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443001-makeblitcommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` func blitCommandEncoder() -> MTLBlitCommandEncoder ``` |
| To | ``` func makeBlitCommandEncoder() -> MTLBlitCommandEncoder ``` |

Modified [MTLCommandBuffer.makeComputeCommandEncoder() -> MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443044-computecommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` func computeCommandEncoder() -> MTLComputeCommandEncoder ``` |
| To | ``` func makeComputeCommandEncoder() -> MTLComputeCommandEncoder ``` |

Modified [MTLCommandBuffer.makeParallelRenderCommandEncoder(descriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443009-parallelrendercommandencoderwith)

|  | Declaration |
| --- | --- |
| From | ``` func parallelRenderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder ``` |
| To | ``` func makeParallelRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> MTLParallelRenderCommandEncoder ``` |

Modified [MTLCommandBuffer.makeRenderCommandEncoder(descriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442999-makerendercommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` func renderCommandEncoderWithDescriptor(_ renderPassDescriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder ``` |
| To | ``` func makeRenderCommandEncoder(descriptor renderPassDescriptor: MTLRenderPassDescriptor) -> MTLRenderCommandEncoder ``` |

Modified [MTLCommandBuffer.present(_: MTLDrawable)](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443029-present)

|  | Declaration |
| --- | --- |
| From | ``` func presentDrawable(_ drawable: MTLDrawable) ``` |
| To | ``` func present(_ drawable: MTLDrawable) ``` |

Modified [MTLCommandBuffer.present(_: MTLDrawable, atTime: CFTimeInterval)](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442989-present)

|  | Declaration |
| --- | --- |
| From | ``` func presentDrawable(_ drawable: MTLDrawable, atTime presentationTime: CFTimeInterval) ``` |
| To | ``` func present(_ drawable: MTLDrawable, atTime presentationTime: CFTimeInterval) ``` |

Modified [MTLCommandBufferErrorDomain [enum]](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLCommandBufferError : UInt {     case None     case Internal     case Timeout     case PageFault     case Blacklisted     case NotPermitted     case OutOfMemory     case InvalidResource } ``` |
| To | ``` enum MTLCommandBufferErrorDomain : UInt {     case none     case `internal`     case timeout     case pageFault     case blacklisted     case notPermitted     case outOfMemory     case invalidResource     case memoryless } ``` |

Modified [MTLCommandBufferErrorDomain.blacklisted](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/mtlcommandbuffererrorblacklisted)

|  | Declaration |
| --- | --- |
| From | ``` case Blacklisted ``` |
| To | ``` case blacklisted ``` |

Modified [MTLCommandBufferErrorDomain.internal](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/mtlcommandbuffererrorinternal)

|  | Declaration |
| --- | --- |
| From | ``` case Internal ``` |
| To | ``` case `internal` ``` |

Modified [MTLCommandBufferErrorDomain.invalidResource](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/mtlcommandbuffererrorinvalidresource)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidResource ``` |
| To | ``` case invalidResource ``` |

Modified [MTLCommandBufferErrorDomain.none](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/mtlcommandbuffererrornone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MTLCommandBufferErrorDomain.notPermitted](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/mtlcommandbuffererrornotpermitted)

|  | Declaration |
| --- | --- |
| From | ``` case NotPermitted ``` |
| To | ``` case notPermitted ``` |

Modified [MTLCommandBufferErrorDomain.outOfMemory](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/mtlcommandbuffererroroutofmemory)

|  | Declaration |
| --- | --- |
| From | ``` case OutOfMemory ``` |
| To | ``` case outOfMemory ``` |

Modified [MTLCommandBufferErrorDomain.pageFault](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/code/pagefault)

|  | Declaration |
| --- | --- |
| From | ``` case PageFault ``` |
| To | ``` case pageFault ``` |

Modified [MTLCommandBufferErrorDomain.timeout](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/mtlcommandbuffererrortimeout)

|  | Declaration |
| --- | --- |
| From | ``` case Timeout ``` |
| To | ``` case timeout ``` |

Modified [MTLCommandBufferStatus [enum]](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLCommandBufferStatus : UInt {     case NotEnqueued     case Enqueued     case Committed     case Scheduled     case Completed     case Error } ``` |
| To | ``` enum MTLCommandBufferStatus : UInt {     case notEnqueued     case enqueued     case committed     case scheduled     case completed     case error } ``` |

Modified [MTLCommandBufferStatus.committed](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/mtlcommandbufferstatuscommitted)

|  | Declaration |
| --- | --- |
| From | ``` case Committed ``` |
| To | ``` case committed ``` |

Modified [MTLCommandBufferStatus.completed](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/completed)

|  | Declaration |
| --- | --- |
| From | ``` case Completed ``` |
| To | ``` case completed ``` |

Modified [MTLCommandBufferStatus.enqueued](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/mtlcommandbufferstatusenqueued)

|  | Declaration |
| --- | --- |
| From | ``` case Enqueued ``` |
| To | ``` case enqueued ``` |

Modified [MTLCommandBufferStatus.error](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/error)

|  | Declaration |
| --- | --- |
| From | ``` case Error ``` |
| To | ``` case error ``` |

Modified [MTLCommandBufferStatus.notEnqueued](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/mtlcommandbufferstatusnotenqueued)

|  | Declaration |
| --- | --- |
| From | ``` case NotEnqueued ``` |
| To | ``` case notEnqueued ``` |

Modified [MTLCommandBufferStatus.scheduled](https://developer.apple.com/documentation/metal/mtlcommandbufferstatus/scheduled)

|  | Declaration |
| --- | --- |
| From | ``` case Scheduled ``` |
| To | ``` case scheduled ``` |

Modified [MTLCommandQueue](https://developer.apple.com/documentation/metal/mtlcommandqueue)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLCommandQueue : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     func commandBuffer() -> MTLCommandBuffer     func commandBufferWithUnretainedReferences() -> MTLCommandBuffer     func insertDebugCaptureBoundary() } ``` |
| To | ``` protocol MTLCommandQueue : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     func makeCommandBuffer() -> MTLCommandBuffer     func makeCommandBufferWithUnretainedReferences() -> MTLCommandBuffer     func insertDebugCaptureBoundary() } ``` |

Modified [MTLCommandQueue.makeCommandBuffer() -> MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandqueue/1508686-commandbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func commandBuffer() -> MTLCommandBuffer ``` |
| To | ``` func makeCommandBuffer() -> MTLCommandBuffer ``` |

Modified [MTLCommandQueue.makeCommandBufferWithUnretainedReferences() -> MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandqueue/1508684-makecommandbufferwithunretainedr)

|  | Declaration |
| --- | --- |
| From | ``` func commandBufferWithUnretainedReferences() -> MTLCommandBuffer ``` |
| To | ``` func makeCommandBufferWithUnretainedReferences() -> MTLCommandBuffer ``` |

Modified [MTLCompareFunction [enum]](https://developer.apple.com/documentation/metal/mtlcomparefunction)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLCompareFunction : UInt {     case Never     case Less     case Equal     case LessEqual     case Greater     case NotEqual     case GreaterEqual     case Always } ``` |
| To | ``` enum MTLCompareFunction : UInt {     case never     case less     case equal     case lessEqual     case greater     case notEqual     case greaterEqual     case always } ``` |

Modified [MTLCompareFunction.always](https://developer.apple.com/documentation/metal/mtlcomparefunction/mtlcomparefunctionalways)

|  | Declaration |
| --- | --- |
| From | ``` case Always ``` |
| To | ``` case always ``` |

Modified [MTLCompareFunction.equal](https://developer.apple.com/documentation/metal/mtlcomparefunction/equal)

|  | Declaration |
| --- | --- |
| From | ``` case Equal ``` |
| To | ``` case equal ``` |

Modified [MTLCompareFunction.greater](https://developer.apple.com/documentation/metal/mtlcomparefunction/mtlcomparefunctiongreater)

|  | Declaration |
| --- | --- |
| From | ``` case Greater ``` |
| To | ``` case greater ``` |

Modified [MTLCompareFunction.greaterEqual](https://developer.apple.com/documentation/metal/mtlcomparefunction/mtlcomparefunctiongreaterequal)

|  | Declaration |
| --- | --- |
| From | ``` case GreaterEqual ``` |
| To | ``` case greaterEqual ``` |

Modified [MTLCompareFunction.less](https://developer.apple.com/documentation/metal/mtlcomparefunction/mtlcomparefunctionless)

|  | Declaration |
| --- | --- |
| From | ``` case Less ``` |
| To | ``` case less ``` |

Modified [MTLCompareFunction.lessEqual](https://developer.apple.com/documentation/metal/mtlcomparefunction/mtlcomparefunctionlessequal)

|  | Declaration |
| --- | --- |
| From | ``` case LessEqual ``` |
| To | ``` case lessEqual ``` |

Modified [MTLCompareFunction.never](https://developer.apple.com/documentation/metal/mtlcomparefunction/never)

|  | Declaration |
| --- | --- |
| From | ``` case Never ``` |
| To | ``` case never ``` |

Modified [MTLCompareFunction.notEqual](https://developer.apple.com/documentation/metal/mtlcomparefunction/notequal)

|  | Declaration |
| --- | --- |
| From | ``` case NotEqual ``` |
| To | ``` case notEqual ``` |

Modified [MTLCompileOptions](https://developer.apple.com/documentation/metal/mtlcompileoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLCompileOptions : NSObject, NSCopying {     var preprocessorMacros: [String : NSObject]?     var fastMathEnabled: Bool     var languageVersion: MTLLanguageVersion } ``` | NSCopying |
| To | ``` class MTLCompileOptions : NSObject, NSCopying {     var preprocessorMacros: [String : NSObject]?     var fastMathEnabled: Bool     var languageVersion: MTLLanguageVersion     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLCompileOptions : CVarArg { } extension MTLCompileOptions : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLComputeCommandEncoder : MTLCommandEncoder {     func setComputePipelineState(_ state: MTLComputePipelineState)     func setBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setBufferOffset(_ offset: Int, atIndex index: Int)     func setBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange)     func setTexture(_ texture: MTLTexture?, atIndex index: Int)     func setTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setThreadgroupMemoryLength(_ length: Int, atIndex index: Int)     func dispatchThreadgroups(_ threadgroupsPerGrid: MTLSize, threadsPerThreadgroup threadsPerThreadgroup: MTLSize)     func dispatchThreadgroupsWithIndirectBuffer(_ indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int, threadsPerThreadgroup threadsPerThreadgroup: MTLSize) } ``` |
| To | ``` protocol MTLComputeCommandEncoder : MTLCommandEncoder {     func setComputePipelineState(_ state: MTLComputePipelineState)     func setBytes(_ bytes: UnsafeRawPointer, length length: Int, at index: Int)     func setBuffer(_ buffer: MTLBuffer?, offset offset: Int, at index: Int)     func setBufferOffset(_ offset: Int, at index: Int)     func setBuffers(_ buffers: UnsafePointer<MTLBuffer?>!, offsets offsets: UnsafePointer<Int>!, with range: NSRange)     func setTexture(_ texture: MTLTexture?, at index: Int)     func setTextures(_ textures: UnsafePointer<MTLTexture?>!, with range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState?, at index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, with range: NSRange)     func setSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, at index: Int)     func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, lodMinClamps lodMinClamps: UnsafePointer<Float>!, lodMaxClamps lodMaxClamps: UnsafePointer<Float>!, with range: NSRange)     func setThreadgroupMemoryLength(_ length: Int, at index: Int)     func setStageInRegion(_ region: MTLRegion)     func dispatchThreadgroups(_ threadgroupsPerGrid: MTLSize, threadsPerThreadgroup threadsPerThreadgroup: MTLSize)     func dispatchThreadgroups(indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int, threadsPerThreadgroup threadsPerThreadgroup: MTLSize)     func updateFence(_ fence: MTLFence)     func waitForFence(_ fence: MTLFence) } ``` |

Modified [MTLComputeCommandEncoder.dispatchThreadgroups(indirectBuffer: MTLBuffer, indirectBufferOffset: Int, threadsPerThreadgroup: MTLSize)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443157-dispatchthreadgroupswithindirect)

|  | Declaration |
| --- | --- |
| From | ``` func dispatchThreadgroupsWithIndirectBuffer(_ indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int, threadsPerThreadgroup threadsPerThreadgroup: MTLSize) ``` |
| To | ``` func dispatchThreadgroups(indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int, threadsPerThreadgroup threadsPerThreadgroup: MTLSize) ``` |

Modified [MTLComputeCommandEncoder.setBuffer(_: MTLBuffer?, offset: Int, at: Int)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443126-setbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func setBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int) ``` |
| To | ``` func setBuffer(_ buffer: MTLBuffer?, offset offset: Int, at index: Int) ``` |

Modified [MTLComputeCommandEncoder.setBufferOffset(_: Int, at: Int)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443146-setbufferoffset)

|  | Declaration |
| --- | --- |
| From | ``` func setBufferOffset(_ offset: Int, atIndex index: Int) ``` |
| To | ``` func setBufferOffset(_ offset: Int, at index: Int) ``` |

Modified [MTLComputeCommandEncoder.setBuffers(_: UnsafePointer<MTLBuffer?>!, offsets: UnsafePointer<Int>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443134-setbuffers)

|  | Declaration |
| --- | --- |
| From | ``` func setBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange) ``` |
| To | ``` func setBuffers(_ buffers: UnsafePointer<MTLBuffer?>!, offsets offsets: UnsafePointer<Int>!, with range: NSRange) ``` |

Modified [MTLComputeCommandEncoder.setBytes(_: UnsafeRawPointer, length: Int, at: Int)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443159-setbytes)

|  | Declaration |
| --- | --- |
| From | ``` func setBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int) ``` |
| To | ``` func setBytes(_ bytes: UnsafeRawPointer, length length: Int, at index: Int) ``` |

Modified [MTLComputeCommandEncoder.setSamplerState(_: MTLSamplerState?, at: Int)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443144-setsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int) ``` |
| To | ``` func setSamplerState(_ sampler: MTLSamplerState?, at index: Int) ``` |

Modified [MTLComputeCommandEncoder.setSamplerState(_: MTLSamplerState?, lodMinClamp: Float, lodMaxClamp: Float, at: Int)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443153-setsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int) ``` |
| To | ``` func setSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, at index: Int) ``` |

Modified [MTLComputeCommandEncoder.setSamplerStates(_: UnsafePointer<MTLSamplerState?>!, lodMinClamps: UnsafePointer<Float>!, lodMaxClamps: UnsafePointer<Float>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443128-setsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange) ``` |
| To | ``` func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, lodMinClamps lodMinClamps: UnsafePointer<Float>!, lodMaxClamps lodMaxClamps: UnsafePointer<Float>!, with range: NSRange) ``` |

Modified [MTLComputeCommandEncoder.setSamplerStates(_: UnsafePointer<MTLSamplerState?>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443155-setsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange) ``` |
| To | ``` func setSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, with range: NSRange) ``` |

Modified [MTLComputeCommandEncoder.setTexture(_: MTLTexture?, at: Int)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443130-settexture)

|  | Declaration |
| --- | --- |
| From | ``` func setTexture(_ texture: MTLTexture?, atIndex index: Int) ``` |
| To | ``` func setTexture(_ texture: MTLTexture?, at index: Int) ``` |

Modified [MTLComputeCommandEncoder.setTextures(_: UnsafePointer<MTLTexture?>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443148-settextures)

|  | Declaration |
| --- | --- |
| From | ``` func setTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange) ``` |
| To | ``` func setTextures(_ textures: UnsafePointer<MTLTexture?>!, with range: NSRange) ``` |

Modified [MTLComputeCommandEncoder.setThreadgroupMemoryLength(_: Int, at: Int)](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1443142-setthreadgroupmemorylength)

|  | Declaration |
| --- | --- |
| From | ``` func setThreadgroupMemoryLength(_ length: Int, atIndex index: Int) ``` |
| To | ``` func setThreadgroupMemoryLength(_ length: Int, at index: Int) ``` |

Modified [MTLComputePipelineDescriptor](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLComputePipelineDescriptor : NSObject, NSCopying {     var label: String?     var computeFunction: MTLFunction?     var threadGroupSizeIsMultipleOfThreadExecutionWidth: Bool     func reset() } ``` | NSCopying |
| To | ``` class MTLComputePipelineDescriptor : NSObject, NSCopying {     var label: String?     var computeFunction: MTLFunction?     var threadGroupSizeIsMultipleOfThreadExecutionWidth: Bool     @NSCopying var stageInputDescriptor: MTLStageInputOutputDescriptor?     func reset()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLComputePipelineDescriptor : CVarArg { } extension MTLComputePipelineDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLComputePipelineReflection](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLComputePipelineReflection : NSObject {     var arguments: [MTLArgument] { get } } ``` | -- |
| To | ``` class MTLComputePipelineReflection : NSObject {     var arguments: [MTLArgument] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLComputePipelineReflection : CVarArg { } extension MTLComputePipelineReflection : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLCPUCacheMode [enum]](https://developer.apple.com/documentation/metal/mtlcpucachemode)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLCPUCacheMode : UInt {     case DefaultCache     case WriteCombined } ``` |
| To | ``` enum MTLCPUCacheMode : UInt {     case defaultCache     case writeCombined } ``` |

Modified [MTLCPUCacheMode.defaultCache](https://developer.apple.com/documentation/metal/mtlcpucachemode/mtlcpucachemodedefaultcache)

|  | Declaration |
| --- | --- |
| From | ``` case DefaultCache ``` |
| To | ``` case defaultCache ``` |

Modified [MTLCPUCacheMode.writeCombined](https://developer.apple.com/documentation/metal/mtlcpucachemode/writecombined)

|  | Declaration |
| --- | --- |
| From | ``` case WriteCombined ``` |
| To | ``` case writeCombined ``` |

Modified [MTLCullMode [enum]](https://developer.apple.com/documentation/metal/mtlcullmode)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLCullMode : UInt {     case None     case Front     case Back } ``` |
| To | ``` enum MTLCullMode : UInt {     case none     case front     case back } ``` |

Modified [MTLCullMode.back](https://developer.apple.com/documentation/metal/mtlcullmode/back)

|  | Declaration |
| --- | --- |
| From | ``` case Back ``` |
| To | ``` case back ``` |

Modified [MTLCullMode.front](https://developer.apple.com/documentation/metal/mtlcullmode/front)

|  | Declaration |
| --- | --- |
| From | ``` case Front ``` |
| To | ``` case front ``` |

Modified [MTLCullMode.none](https://developer.apple.com/documentation/metal/mtlcullmode/mtlcullmodenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MTLDataType [enum]](https://developer.apple.com/documentation/metal/mtldatatype)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLDataType : UInt {     case None     case Struct     case Array     case Float     case Float2     case Float3     case Float4     case Float2x2     case Float2x3     case Float2x4     case Float3x2     case Float3x3     case Float3x4     case Float4x2     case Float4x3     case Float4x4     case Half     case Half2     case Half3     case Half4     case Half2x2     case Half2x3     case Half2x4     case Half3x2     case Half3x3     case Half3x4     case Half4x2     case Half4x3     case Half4x4     case Int     case Int2     case Int3     case Int4     case UInt     case UInt2     case UInt3     case UInt4     case Short     case Short2     case Short3     case Short4     case UShort     case UShort2     case UShort3     case UShort4     case Char     case Char2     case Char3     case Char4     case UChar     case UChar2     case UChar3     case UChar4     case Bool     case Bool2     case Bool3     case Bool4 } ``` |
| To | ``` enum MTLDataType : UInt {     case none     case `struct`     case array     case float     case float2     case float3     case float4     case float2x2     case float2x3     case float2x4     case float3x2     case float3x3     case float3x4     case float4x2     case float4x3     case float4x4     case half     case half2     case half3     case half4     case half2x2     case half2x3     case half2x4     case half3x2     case half3x3     case half3x4     case half4x2     case half4x3     case half4x4     case int     case int2     case int3     case int4     case uint     case uint2     case uint3     case uint4     case short     case short2     case short3     case short4     case ushort     case ushort2     case ushort3     case ushort4     case char     case char2     case char3     case char4     case uchar     case uchar2     case uchar3     case uchar4     case bool     case bool2     case bool3     case bool4 } ``` |

Modified [MTLDataType.array](https://developer.apple.com/documentation/metal/mtldatatype/array)

|  | Declaration |
| --- | --- |
| From | ``` case Array ``` |
| To | ``` case array ``` |

Modified [MTLDataType.bool](https://developer.apple.com/documentation/metal/mtldatatype/bool)

|  | Declaration |
| --- | --- |
| From | ``` case Bool ``` |
| To | ``` case bool ``` |

Modified [MTLDataType.bool2](https://developer.apple.com/documentation/metal/mtldatatype/bool2)

|  | Declaration |
| --- | --- |
| From | ``` case Bool2 ``` |
| To | ``` case bool2 ``` |

Modified [MTLDataType.bool3](https://developer.apple.com/documentation/metal/mtldatatype/bool3)

|  | Declaration |
| --- | --- |
| From | ``` case Bool3 ``` |
| To | ``` case bool3 ``` |

Modified [MTLDataType.bool4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypebool4)

|  | Declaration |
| --- | --- |
| From | ``` case Bool4 ``` |
| To | ``` case bool4 ``` |

Modified [MTLDataType.char](https://developer.apple.com/documentation/metal/mtldatatype/char)

|  | Declaration |
| --- | --- |
| From | ``` case Char ``` |
| To | ``` case char ``` |

Modified [MTLDataType.char2](https://developer.apple.com/documentation/metal/mtldatatype/char2)

|  | Declaration |
| --- | --- |
| From | ``` case Char2 ``` |
| To | ``` case char2 ``` |

Modified [MTLDataType.char3](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypechar3)

|  | Declaration |
| --- | --- |
| From | ``` case Char3 ``` |
| To | ``` case char3 ``` |

Modified [MTLDataType.char4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypechar4)

|  | Declaration |
| --- | --- |
| From | ``` case Char4 ``` |
| To | ``` case char4 ``` |

Modified [MTLDataType.float](https://developer.apple.com/documentation/metal/mtldatatype/float)

|  | Declaration |
| --- | --- |
| From | ``` case Float ``` |
| To | ``` case float ``` |

Modified [MTLDataType.float2](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypefloat2)

|  | Declaration |
| --- | --- |
| From | ``` case Float2 ``` |
| To | ``` case float2 ``` |

Modified [MTLDataType.float2x2](https://developer.apple.com/documentation/metal/mtldatatype/float2x2)

|  | Declaration |
| --- | --- |
| From | ``` case Float2x2 ``` |
| To | ``` case float2x2 ``` |

Modified [MTLDataType.float2x3](https://developer.apple.com/documentation/metal/mtldatatype/float2x3)

|  | Declaration |
| --- | --- |
| From | ``` case Float2x3 ``` |
| To | ``` case float2x3 ``` |

Modified [MTLDataType.float2x4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypefloat2x4)

|  | Declaration |
| --- | --- |
| From | ``` case Float2x4 ``` |
| To | ``` case float2x4 ``` |

Modified [MTLDataType.float3](https://developer.apple.com/documentation/metal/mtldatatype/float3)

|  | Declaration |
| --- | --- |
| From | ``` case Float3 ``` |
| To | ``` case float3 ``` |

Modified [MTLDataType.float3x2](https://developer.apple.com/documentation/metal/mtldatatype/float3x2)

|  | Declaration |
| --- | --- |
| From | ``` case Float3x2 ``` |
| To | ``` case float3x2 ``` |

Modified [MTLDataType.float3x3](https://developer.apple.com/documentation/metal/mtldatatype/float3x3)

|  | Declaration |
| --- | --- |
| From | ``` case Float3x3 ``` |
| To | ``` case float3x3 ``` |

Modified [MTLDataType.float3x4](https://developer.apple.com/documentation/metal/mtldatatype/float3x4)

|  | Declaration |
| --- | --- |
| From | ``` case Float3x4 ``` |
| To | ``` case float3x4 ``` |

Modified [MTLDataType.float4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypefloat4)

|  | Declaration |
| --- | --- |
| From | ``` case Float4 ``` |
| To | ``` case float4 ``` |

Modified [MTLDataType.float4x2](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypefloat4x2)

|  | Declaration |
| --- | --- |
| From | ``` case Float4x2 ``` |
| To | ``` case float4x2 ``` |

Modified [MTLDataType.float4x3](https://developer.apple.com/documentation/metal/mtldatatype/float4x3)

|  | Declaration |
| --- | --- |
| From | ``` case Float4x3 ``` |
| To | ``` case float4x3 ``` |

Modified [MTLDataType.float4x4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypefloat4x4)

|  | Declaration |
| --- | --- |
| From | ``` case Float4x4 ``` |
| To | ``` case float4x4 ``` |

Modified [MTLDataType.half](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypehalf)

|  | Declaration |
| --- | --- |
| From | ``` case Half ``` |
| To | ``` case half ``` |

Modified [MTLDataType.half2](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypehalf2)

|  | Declaration |
| --- | --- |
| From | ``` case Half2 ``` |
| To | ``` case half2 ``` |

Modified [MTLDataType.half2x2](https://developer.apple.com/documentation/metal/mtldatatype/half2x2)

|  | Declaration |
| --- | --- |
| From | ``` case Half2x2 ``` |
| To | ``` case half2x2 ``` |

Modified [MTLDataType.half2x3](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypehalf2x3)

|  | Declaration |
| --- | --- |
| From | ``` case Half2x3 ``` |
| To | ``` case half2x3 ``` |

Modified [MTLDataType.half2x4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypehalf2x4)

|  | Declaration |
| --- | --- |
| From | ``` case Half2x4 ``` |
| To | ``` case half2x4 ``` |

Modified [MTLDataType.half3](https://developer.apple.com/documentation/metal/mtldatatype/half3)

|  | Declaration |
| --- | --- |
| From | ``` case Half3 ``` |
| To | ``` case half3 ``` |

Modified [MTLDataType.half3x2](https://developer.apple.com/documentation/metal/mtldatatype/half3x2)

|  | Declaration |
| --- | --- |
| From | ``` case Half3x2 ``` |
| To | ``` case half3x2 ``` |

Modified [MTLDataType.half3x3](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypehalf3x3)

|  | Declaration |
| --- | --- |
| From | ``` case Half3x3 ``` |
| To | ``` case half3x3 ``` |

Modified [MTLDataType.half3x4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypehalf3x4)

|  | Declaration |
| --- | --- |
| From | ``` case Half3x4 ``` |
| To | ``` case half3x4 ``` |

Modified [MTLDataType.half4](https://developer.apple.com/documentation/metal/mtldatatype/half4)

|  | Declaration |
| --- | --- |
| From | ``` case Half4 ``` |
| To | ``` case half4 ``` |

Modified [MTLDataType.half4x2](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypehalf4x2)

|  | Declaration |
| --- | --- |
| From | ``` case Half4x2 ``` |
| To | ``` case half4x2 ``` |

Modified [MTLDataType.half4x3](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypehalf4x3)

|  | Declaration |
| --- | --- |
| From | ``` case Half4x3 ``` |
| To | ``` case half4x3 ``` |

Modified [MTLDataType.half4x4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypehalf4x4)

|  | Declaration |
| --- | --- |
| From | ``` case Half4x4 ``` |
| To | ``` case half4x4 ``` |

Modified [MTLDataType.int](https://developer.apple.com/documentation/metal/mtldatatype/int)

|  | Declaration |
| --- | --- |
| From | ``` case Int ``` |
| To | ``` case int ``` |

Modified [MTLDataType.int2](https://developer.apple.com/documentation/metal/mtldatatype/int2)

|  | Declaration |
| --- | --- |
| From | ``` case Int2 ``` |
| To | ``` case int2 ``` |

Modified [MTLDataType.int3](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeint3)

|  | Declaration |
| --- | --- |
| From | ``` case Int3 ``` |
| To | ``` case int3 ``` |

Modified [MTLDataType.int4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeint4)

|  | Declaration |
| --- | --- |
| From | ``` case Int4 ``` |
| To | ``` case int4 ``` |

Modified [MTLDataType.none](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MTLDataType.short](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeshort)

|  | Declaration |
| --- | --- |
| From | ``` case Short ``` |
| To | ``` case short ``` |

Modified [MTLDataType.short2](https://developer.apple.com/documentation/metal/mtldatatype/short2)

|  | Declaration |
| --- | --- |
| From | ``` case Short2 ``` |
| To | ``` case short2 ``` |

Modified [MTLDataType.short3](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeshort3)

|  | Declaration |
| --- | --- |
| From | ``` case Short3 ``` |
| To | ``` case short3 ``` |

Modified [MTLDataType.short4](https://developer.apple.com/documentation/metal/mtldatatype/short4)

|  | Declaration |
| --- | --- |
| From | ``` case Short4 ``` |
| To | ``` case short4 ``` |

Modified [MTLDataType.struct](https://developer.apple.com/documentation/metal/mtldatatype/struct)

|  | Declaration |
| --- | --- |
| From | ``` case Struct ``` |
| To | ``` case `struct` ``` |

Modified [MTLDataType.uchar](https://developer.apple.com/documentation/metal/mtldatatype/uchar)

|  | Declaration |
| --- | --- |
| From | ``` case UChar ``` |
| To | ``` case uchar ``` |

Modified [MTLDataType.uchar2](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeuchar2)

|  | Declaration |
| --- | --- |
| From | ``` case UChar2 ``` |
| To | ``` case uchar2 ``` |

Modified [MTLDataType.uchar3](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeuchar3)

|  | Declaration |
| --- | --- |
| From | ``` case UChar3 ``` |
| To | ``` case uchar3 ``` |

Modified [MTLDataType.uchar4](https://developer.apple.com/documentation/metal/mtldatatype/uchar4)

|  | Declaration |
| --- | --- |
| From | ``` case UChar4 ``` |
| To | ``` case uchar4 ``` |

Modified [MTLDataType.uint](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeuint)

|  | Declaration |
| --- | --- |
| From | ``` case UInt ``` |
| To | ``` case uint ``` |

Modified [MTLDataType.uint2](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeuint2)

|  | Declaration |
| --- | --- |
| From | ``` case UInt2 ``` |
| To | ``` case uint2 ``` |

Modified [MTLDataType.uint3](https://developer.apple.com/documentation/metal/mtldatatype/uint3)

|  | Declaration |
| --- | --- |
| From | ``` case UInt3 ``` |
| To | ``` case uint3 ``` |

Modified [MTLDataType.uint4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeuint4)

|  | Declaration |
| --- | --- |
| From | ``` case UInt4 ``` |
| To | ``` case uint4 ``` |

Modified [MTLDataType.ushort](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeushort)

|  | Declaration |
| --- | --- |
| From | ``` case UShort ``` |
| To | ``` case ushort ``` |

Modified [MTLDataType.ushort2](https://developer.apple.com/documentation/metal/mtldatatype/ushort2)

|  | Declaration |
| --- | --- |
| From | ``` case UShort2 ``` |
| To | ``` case ushort2 ``` |

Modified [MTLDataType.ushort3](https://developer.apple.com/documentation/metal/mtldatatype/ushort3)

|  | Declaration |
| --- | --- |
| From | ``` case UShort3 ``` |
| To | ``` case ushort3 ``` |

Modified [MTLDataType.ushort4](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypeushort4)

|  | Declaration |
| --- | --- |
| From | ``` case UShort4 ``` |
| To | ``` case ushort4 ``` |

Modified [MTLDepthClipMode [enum]](https://developer.apple.com/documentation/metal/mtldepthclipmode)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLDepthClipMode : UInt {     case Clip     case Clamp } ``` |
| To | ``` enum MTLDepthClipMode : UInt {     case clip     case clamp } ``` |

Modified [MTLDepthClipMode.clamp](https://developer.apple.com/documentation/metal/mtldepthclipmode/clamp)

|  | Declaration |
| --- | --- |
| From | ``` case Clamp ``` |
| To | ``` case clamp ``` |

Modified [MTLDepthClipMode.clip](https://developer.apple.com/documentation/metal/mtldepthclipmode/mtldepthclipmodeclip)

|  | Declaration |
| --- | --- |
| From | ``` case Clip ``` |
| To | ``` case clip ``` |

Modified [MTLDepthStencilDescriptor](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLDepthStencilDescriptor : NSObject, NSCopying {     var depthCompareFunction: MTLCompareFunction     var depthWriteEnabled: Bool     @NSCopying var frontFaceStencil: MTLStencilDescriptor!     @NSCopying var backFaceStencil: MTLStencilDescriptor!     var label: String? } ``` | NSCopying |
| To | ``` class MTLDepthStencilDescriptor : NSObject, NSCopying {     var depthCompareFunction: MTLCompareFunction     var isDepthWriteEnabled: Bool     @NSCopying var frontFaceStencil: MTLStencilDescriptor!     @NSCopying var backFaceStencil: MTLStencilDescriptor!     var label: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLDepthStencilDescriptor : CVarArg { } extension MTLDepthStencilDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLDepthStencilDescriptor.isDepthWriteEnabled](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/1462501-isdepthwriteenabled)

|  | Declaration |
| --- | --- |
| From | ``` var depthWriteEnabled: Bool ``` |
| To | ``` var isDepthWriteEnabled: Bool ``` |

Modified [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLDevice : NSObjectProtocol {     var name: String? { get }     var maxThreadsPerThreadgroup: MTLSize { get }     var lowPower: Bool { get }     var headless: Bool { get }     var depth24Stencil8PixelFormatSupported: Bool { get }     func newCommandQueue() -> MTLCommandQueue     func newCommandQueueWithMaxCommandBufferCount(_ maxCommandBufferCount: Int) -> MTLCommandQueue     func newBufferWithLength(_ length: Int, options options: MTLResourceOptions) -> MTLBuffer     func newBufferWithBytes(_ pointer: UnsafePointer<Void>, length length: Int, options options: MTLResourceOptions) -> MTLBuffer     func newBufferWithBytesNoCopy(_ pointer: UnsafeMutablePointer<Void>, length length: Int, options options: MTLResourceOptions, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?) -> MTLBuffer     func newDepthStencilStateWithDescriptor(_ descriptor: MTLDepthStencilDescriptor) -> MTLDepthStencilState     func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor) -> MTLTexture     func newSamplerStateWithDescriptor(_ descriptor: MTLSamplerDescriptor) -> MTLSamplerState     func newDefaultLibrary() -> MTLLibrary?     func newLibraryWithFile(_ filepath: String) throws -> MTLLibrary     func newLibraryWithData(_ data: dispatch_data_t) throws -> MTLLibrary     func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?) throws -> MTLLibrary     func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?, completionHandler completionHandler: MTLNewLibraryCompletionHandler)     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor) throws -> MTLRenderPipelineState     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>) throws -> MTLRenderPipelineState     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: MTLNewRenderPipelineStateCompletionHandler)     func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewRenderPipelineStateWithReflectionCompletionHandler)     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction) throws -> MTLComputePipelineState     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>) throws -> MTLComputePipelineState     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, completionHandler completionHandler: MTLNewComputePipelineStateCompletionHandler)     func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewComputePipelineStateWithReflectionCompletionHandler)     func newComputePipelineStateWithDescriptor(_ descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>) throws -> MTLComputePipelineState     func newComputePipelineStateWithDescriptor(_ descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewComputePipelineStateWithReflectionCompletionHandler)     func supportsFeatureSet(_ featureSet: MTLFeatureSet) -> Bool     func supportsTextureSampleCount(_ sampleCount: Int) -> Bool } ``` |
| To | ``` protocol MTLDevice : NSObjectProtocol {     var name: String? { get }     var maxThreadsPerThreadgroup: MTLSize { get }     var isLowPower: Bool { get }     var isHeadless: Bool { get }     var recommendedMaxWorkingSetSize: UInt64 { get }     var isDepth24Stencil8PixelFormatSupported: Bool { get }     func makeCommandQueue() -> MTLCommandQueue     func makeCommandQueue(maxCommandBufferCount maxCommandBufferCount: Int) -> MTLCommandQueue     func heapTextureSizeAndAlign(descriptor desc: MTLTextureDescriptor) -> MTLSizeAndAlign     func heapBufferSizeAndAlign(length length: Int, options options: MTLResourceOptions = []) -> MTLSizeAndAlign     func makeHeap(descriptor descriptor: MTLHeapDescriptor) -> MTLHeap     func makeBuffer(length length: Int, options options: MTLResourceOptions = []) -> MTLBuffer     func makeBuffer(bytes pointer: UnsafeRawPointer, length length: Int, options options: MTLResourceOptions = []) -> MTLBuffer     func makeBuffer(bytesNoCopy pointer: UnsafeMutableRawPointer, length length: Int, options options: MTLResourceOptions = [], deallocator deallocator: (@escaping (UnsafeMutableRawPointer, Int) -> Swift.Void)? = nil) -> MTLBuffer     func makeDepthStencilState(descriptor descriptor: MTLDepthStencilDescriptor) -> MTLDepthStencilState     func makeTexture(descriptor descriptor: MTLTextureDescriptor) -> MTLTexture     func makeSamplerState(descriptor descriptor: MTLSamplerDescriptor) -> MTLSamplerState     func newDefaultLibrary() -> MTLLibrary?     func makeDefaultLibrary(bundle bundle: Bundle) throws -> MTLLibrary     func makeLibrary(filepath filepath: String) throws -> MTLLibrary     func makeLibrary(data data: __DispatchData) throws -> MTLLibrary     func makeLibrary(source source: String, options options: MTLCompileOptions?) throws -> MTLLibrary     func makeLibrary(source source: String, options options: MTLCompileOptions?, completionHandler completionHandler: Metal.MTLNewLibraryCompletionHandler)     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor) throws -> MTLRenderPipelineState     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> MTLRenderPipelineState     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: Metal.MTLNewRenderPipelineStateCompletionHandler)     func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewRenderPipelineStateWithReflectionCompletionHandler)     func makeComputePipelineState(function computeFunction: MTLFunction) throws -> MTLComputePipelineState     func makeComputePipelineState(function computeFunction: MTLFunction, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> MTLComputePipelineState     func makeComputePipelineState(function computeFunction: MTLFunction, completionHandler completionHandler: Metal.MTLNewComputePipelineStateCompletionHandler)     func makeComputePipelineState(function computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler)     func makeComputePipelineState(descriptor descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> MTLComputePipelineState     func makeComputePipelineState(descriptor descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler)     func makeFence() -> MTLFence     func supportsFeatureSet(_ featureSet: MTLFeatureSet) -> Bool     func supportsTextureSampleCount(_ sampleCount: Int) -> Bool } ``` |

Modified [MTLDevice.makeBuffer() -> MTLBuffer](https://developer.apple.com/documentation/metal/mtldevice/1433429-newbufferwithbytes)

|  | Declaration |
| --- | --- |
| From | ``` func newBufferWithBytes(_ pointer: UnsafePointer<Void>, length length: Int, options options: MTLResourceOptions) -> MTLBuffer ``` |
| To | ``` func makeBuffer(bytes pointer: UnsafeRawPointer, length length: Int, options options: MTLResourceOptions = []) -> MTLBuffer ``` |

Modified [MTLDevice.makeBuffer() -> Swift.Void)? = nil) -> MTLBuffer](https://developer.apple.com/documentation/metal/mtldevice/1433382-newbufferwithbytesnocopy)

|  | Declaration |
| --- | --- |
| From | ``` func newBufferWithBytesNoCopy(_ pointer: UnsafeMutablePointer<Void>, length length: Int, options options: MTLResourceOptions, deallocator deallocator: ((UnsafeMutablePointer<Void>, Int) -> Void)?) -> MTLBuffer ``` |
| To | ``` func makeBuffer(bytesNoCopy pointer: UnsafeMutableRawPointer, length length: Int, options options: MTLResourceOptions = [], deallocator deallocator: (@escaping (UnsafeMutableRawPointer, Int) -> Swift.Void)? = nil) -> MTLBuffer ``` |

Modified [MTLDevice.makeBuffer() -> MTLBuffer](https://developer.apple.com/documentation/metal/mtldevice/1433375-makebuffer)

|  | Declaration |
| --- | --- |
| From | ``` func newBufferWithLength(_ length: Int, options options: MTLResourceOptions) -> MTLBuffer ``` |
| To | ``` func makeBuffer(length length: Int, options options: MTLResourceOptions = []) -> MTLBuffer ``` |

Modified [MTLDevice.makeCommandQueue() -> MTLCommandQueue](https://developer.apple.com/documentation/metal/mtldevice/1433388-makecommandqueue)

|  | Declaration |
| --- | --- |
| From | ``` func newCommandQueue() -> MTLCommandQueue ``` |
| To | ``` func makeCommandQueue() -> MTLCommandQueue ``` |

Modified [MTLDevice.makeCommandQueue(maxCommandBufferCount: Int) -> MTLCommandQueue](https://developer.apple.com/documentation/metal/mtldevice/1433433-makecommandqueue)

|  | Declaration |
| --- | --- |
| From | ``` func newCommandQueueWithMaxCommandBufferCount(_ maxCommandBufferCount: Int) -> MTLCommandQueue ``` |
| To | ``` func makeCommandQueue(maxCommandBufferCount maxCommandBufferCount: Int) -> MTLCommandQueue ``` |

Modified [MTLDevice.makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433403-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newComputePipelineStateWithDescriptor(_ descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewComputePipelineStateWithReflectionCompletionHandler) ``` |
| To | ``` func makeComputePipelineState(descriptor descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler) ``` |

Modified [MTLDevice.makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtldevice/1433353-newcomputepipelinestatewithdescr)

|  | Declaration |
| --- | --- |
| From | ``` func newComputePipelineStateWithDescriptor(_ descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>) throws -> MTLComputePipelineState ``` |
| To | ``` func makeComputePipelineState(descriptor descriptor: MTLComputePipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> MTLComputePipelineState ``` |

Modified [MTLDevice.makeComputePipelineState(function: MTLFunction) throws -> MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtldevice/1433395-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction) throws -> MTLComputePipelineState ``` |
| To | ``` func makeComputePipelineState(function computeFunction: MTLFunction) throws -> MTLComputePipelineState ``` |

Modified [MTLDevice.makeComputePipelineState(function: MTLFunction, completionHandler: Metal.MTLNewComputePipelineStateCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433427-newcomputepipelinestatewithfunct)

|  | Declaration |
| --- | --- |
| From | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, completionHandler completionHandler: MTLNewComputePipelineStateCompletionHandler) ``` |
| To | ``` func makeComputePipelineState(function computeFunction: MTLFunction, completionHandler completionHandler: Metal.MTLNewComputePipelineStateCompletionHandler) ``` |

Modified [MTLDevice.makeComputePipelineState(function: MTLFunction, options: MTLPipelineOption, completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433410-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewComputePipelineStateWithReflectionCompletionHandler) ``` |
| To | ``` func makeComputePipelineState(function computeFunction: MTLFunction, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewComputePipelineStateWithReflectionCompletionHandler) ``` |

Modified [MTLDevice.makeComputePipelineState(function: MTLFunction, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtldevice/1433419-makecomputepipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newComputePipelineStateWithFunction(_ computeFunction: MTLFunction, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>) throws -> MTLComputePipelineState ``` |
| To | ``` func makeComputePipelineState(function computeFunction: MTLFunction, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> MTLComputePipelineState ``` |

Modified [MTLDevice.makeDepthStencilState(descriptor: MTLDepthStencilDescriptor) -> MTLDepthStencilState](https://developer.apple.com/documentation/metal/mtldevice/1433412-newdepthstencilstatewithdescript)

|  | Declaration |
| --- | --- |
| From | ``` func newDepthStencilStateWithDescriptor(_ descriptor: MTLDepthStencilDescriptor) -> MTLDepthStencilState ``` |
| To | ``` func makeDepthStencilState(descriptor descriptor: MTLDepthStencilDescriptor) -> MTLDepthStencilState ``` |

Modified [MTLDevice.makeLibrary(data: __DispatchData) throws -> MTLLibrary](https://developer.apple.com/documentation/metal/mtldevice/1433391-newlibrarywithdata)

|  | Declaration |
| --- | --- |
| From | ``` func newLibraryWithData(_ data: dispatch_data_t) throws -> MTLLibrary ``` |
| To | ``` func makeLibrary(data data: __DispatchData) throws -> MTLLibrary ``` |

Modified [MTLDevice.makeLibrary(filepath: String) throws -> MTLLibrary](https://developer.apple.com/documentation/metal/mtldevice/1433416-newlibrarywithfile)

|  | Declaration |
| --- | --- |
| From | ``` func newLibraryWithFile(_ filepath: String) throws -> MTLLibrary ``` |
| To | ``` func makeLibrary(filepath filepath: String) throws -> MTLLibrary ``` |

Modified [MTLDevice.makeLibrary(source: String, options: MTLCompileOptions?) throws -> MTLLibrary](https://developer.apple.com/documentation/metal/mtldevice/1433431-newlibrarywithsource)

|  | Declaration |
| --- | --- |
| From | ``` func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?) throws -> MTLLibrary ``` |
| To | ``` func makeLibrary(source source: String, options options: MTLCompileOptions?) throws -> MTLLibrary ``` |

Modified [MTLDevice.makeLibrary(source: String, options: MTLCompileOptions?, completionHandler: Metal.MTLNewLibraryCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433351-newlibrarywithsource)

|  | Declaration |
| --- | --- |
| From | ``` func newLibraryWithSource(_ source: String, options options: MTLCompileOptions?, completionHandler completionHandler: MTLNewLibraryCompletionHandler) ``` |
| To | ``` func makeLibrary(source source: String, options options: MTLCompileOptions?, completionHandler completionHandler: Metal.MTLNewLibraryCompletionHandler) ``` |

Modified [MTLDevice.makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor) throws -> MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtldevice/1433369-newrenderpipelinestatewithdescri)

|  | Declaration |
| --- | --- |
| From | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor) throws -> MTLRenderPipelineState ``` |
| To | ``` func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor) throws -> MTLRenderPipelineState ``` |

Modified [MTLDevice.makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, completionHandler: Metal.MTLNewRenderPipelineStateCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433363-makerenderpipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: MTLNewRenderPipelineStateCompletionHandler) ``` |
| To | ``` func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, completionHandler completionHandler: Metal.MTLNewRenderPipelineStateCompletionHandler) ``` |

Modified [MTLDevice.makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: Metal.MTLNewRenderPipelineStateWithReflectionCompletionHandler)](https://developer.apple.com/documentation/metal/mtldevice/1433365-newrenderpipelinestatewithdescri)

|  | Declaration |
| --- | --- |
| From | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: MTLNewRenderPipelineStateWithReflectionCompletionHandler) ``` |
| To | ``` func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, completionHandler completionHandler: Metal.MTLNewRenderPipelineStateWithReflectionCompletionHandler) ``` |

Modified [MTLDevice.makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> MTLRenderPipelineState](https://developer.apple.com/documentation/metal/mtldevice/1433361-makerenderpipelinestate)

|  | Declaration |
| --- | --- |
| From | ``` func newRenderPipelineStateWithDescriptor(_ descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>) throws -> MTLRenderPipelineState ``` |
| To | ``` func makeRenderPipelineState(descriptor descriptor: MTLRenderPipelineDescriptor, options options: MTLPipelineOption, reflection reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> MTLRenderPipelineState ``` |

Modified [MTLDevice.makeSamplerState(descriptor: MTLSamplerDescriptor) -> MTLSamplerState](https://developer.apple.com/documentation/metal/mtldevice/1433408-makesamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func newSamplerStateWithDescriptor(_ descriptor: MTLSamplerDescriptor) -> MTLSamplerState ``` |
| To | ``` func makeSamplerState(descriptor descriptor: MTLSamplerDescriptor) -> MTLSamplerState ``` |

Modified [MTLDevice.makeTexture(descriptor: MTLTextureDescriptor) -> MTLTexture](https://developer.apple.com/documentation/metal/mtldevice/1433425-newtexturewithdescriptor)

|  | Declaration |
| --- | --- |
| From | ``` func newTextureWithDescriptor(_ descriptor: MTLTextureDescriptor) -> MTLTexture ``` |
| To | ``` func makeTexture(descriptor descriptor: MTLTextureDescriptor) -> MTLTexture ``` |

Modified [MTLDrawable](https://developer.apple.com/documentation/metal/mtldrawable)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLDrawable : NSObjectProtocol {     func present()     func presentAtTime(_ presentationTime: CFTimeInterval) } ``` |
| To | ``` protocol MTLDrawable : NSObjectProtocol {     func present()     func present(at presentationTime: CFTimeInterval) } ``` |

Modified [MTLDrawable.present(at: CFTimeInterval)](https://developer.apple.com/documentation/metal/mtldrawable/1470282-present)

|  | Declaration |
| --- | --- |
| From | ``` func presentAtTime(_ presentationTime: CFTimeInterval) ``` |
| To | ``` func present(at presentationTime: CFTimeInterval) ``` |

Modified [MTLFeatureSet [enum]](https://developer.apple.com/documentation/metal/mtlfeatureset)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLFeatureSet : UInt {     case iOS_GPUFamily1_v1     case iOS_GPUFamily2_v1     case iOS_GPUFamily1_v2     case iOS_GPUFamily2_v2     case iOS_GPUFamily3_v1     case OSX_GPUFamily1_v1     case TVOS_GPUFamily1_v1 } ``` |
| To | ``` enum MTLFeatureSet : UInt {     case iOS_GPUFamily1_v1     case iOS_GPUFamily2_v1     case iOS_GPUFamily1_v2     case iOS_GPUFamily2_v2     case iOS_GPUFamily3_v1     case iOS_GPUFamily1_v3     case iOS_GPUFamily2_v3     case iOS_GPUFamily3_v2     case osx_GPUFamily1_v1     case osx_GPUFamily1_v2     case osx_ReadWriteTextureTier2     case tvOS_GPUFamily1_v1     case tvOS_GPUFamily1_v2 } ``` |

Modified [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLFunction : NSObjectProtocol {     var device: MTLDevice { get }     var functionType: MTLFunctionType { get }     var vertexAttributes: [MTLVertexAttribute]? { get }     var name: String { get } } ``` |
| To | ``` protocol MTLFunction : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     var functionType: MTLFunctionType { get }     var patchType: MTLPatchType { get }     var patchControlPointCount: Int { get }     var vertexAttributes: [MTLVertexAttribute]? { get }     var stageInputAttributes: [MTLAttribute]? { get }     var name: String { get }     var functionConstantsDictionary: [String : MTLFunctionConstant] { get } } ``` |

Modified [MTLFunctionType [enum]](https://developer.apple.com/documentation/metal/mtlfunctiontype)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLFunctionType : UInt {     case Vertex     case Fragment     case Kernel } ``` |
| To | ``` enum MTLFunctionType : UInt {     case vertex     case fragment     case kernel } ``` |

Modified [MTLFunctionType.fragment](https://developer.apple.com/documentation/metal/mtlfunctiontype/fragment)

|  | Declaration |
| --- | --- |
| From | ``` case Fragment ``` |
| To | ``` case fragment ``` |

Modified [MTLFunctionType.kernel](https://developer.apple.com/documentation/metal/mtlfunctiontype/mtlfunctiontypekernel)

|  | Declaration |
| --- | --- |
| From | ``` case Kernel ``` |
| To | ``` case kernel ``` |

Modified [MTLFunctionType.vertex](https://developer.apple.com/documentation/metal/mtlfunctiontype/mtlfunctiontypevertex)

|  | Declaration |
| --- | --- |
| From | ``` case Vertex ``` |
| To | ``` case vertex ``` |

Modified [MTLIndexType [enum]](https://developer.apple.com/documentation/metal/mtlindextype)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLIndexType : UInt {     case UInt16     case UInt32 } ``` |
| To | ``` enum MTLIndexType : UInt {     case uint16     case uint32 } ``` |

Modified [MTLIndexType.uint16](https://developer.apple.com/documentation/metal/mtlindextype/mtlindextypeuint16)

|  | Declaration |
| --- | --- |
| From | ``` case UInt16 ``` |
| To | ``` case uint16 ``` |

Modified [MTLIndexType.uint32](https://developer.apple.com/documentation/metal/mtlindextype/uint32)

|  | Declaration |
| --- | --- |
| From | ``` case UInt32 ``` |
| To | ``` case uint32 ``` |

Modified [MTLLanguageVersion [enum]](https://developer.apple.com/documentation/metal/mtllanguageversion)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLLanguageVersion : UInt {     case Version1_0     case Version1_1 } ``` |
| To | ``` enum MTLLanguageVersion : UInt {     case version1_0     case version1_1     case version1_2 } ``` |

Modified [MTLLanguageVersion.version1_0](https://developer.apple.com/documentation/metal/mtllanguageversion/version1_0)

|  | Declaration |
| --- | --- |
| From | ``` case Version1_0 ``` |
| To | ``` case version1_0 ``` |

Modified [MTLLanguageVersion.version1_1](https://developer.apple.com/documentation/metal/mtllanguageversion/version1_1)

|  | Declaration |
| --- | --- |
| From | ``` case Version1_1 ``` |
| To | ``` case version1_1 ``` |

Modified [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLLibrary : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     func newFunctionWithName(_ functionName: String) -> MTLFunction?     var functionNames: [String] { get } } ``` |
| To | ``` protocol MTLLibrary : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     func makeFunction(name functionName: String) -> MTLFunction?     func makeFunction(name name: String, constantValues constantValues: MTLFunctionConstantValues) throws -> MTLFunction     func makeFunction(name name: String, constantValues constantValues: MTLFunctionConstantValues, completionHandler completionHandler: @escaping (MTLFunction?, Error) -> Swift.Void)     var functionNames: [String] { get } } ``` |

Modified [MTLLibrary.makeFunction(name: String) -> MTLFunction?](https://developer.apple.com/documentation/metal/mtllibrary/1515524-newfunctionwithname)

|  | Declaration |
| --- | --- |
| From | ``` func newFunctionWithName(_ functionName: String) -> MTLFunction? ``` |
| To | ``` func makeFunction(name functionName: String) -> MTLFunction? ``` |

Modified [MTLLibraryErrorDomain [enum]](https://developer.apple.com/documentation/metal/mtllibraryerror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLLibraryError : UInt {     case Unsupported     case Internal     case CompileFailure     case CompileWarning } ``` |
| To | ``` enum MTLLibraryErrorDomain : UInt {     case unsupported     case `internal`     case compileFailure     case compileWarning     case functionNotFound     case fileNotFound } ``` |

Modified [MTLLibraryErrorDomain.compileFailure](https://developer.apple.com/documentation/metal/mtllibraryerror/mtllibraryerrorcompilefailure)

|  | Declaration |
| --- | --- |
| From | ``` case CompileFailure ``` |
| To | ``` case compileFailure ``` |

Modified [MTLLibraryErrorDomain.compileWarning](https://developer.apple.com/documentation/metal/mtllibraryerror/mtllibraryerrorcompilewarning)

|  | Declaration |
| --- | --- |
| From | ``` case CompileWarning ``` |
| To | ``` case compileWarning ``` |

Modified [MTLLibraryErrorDomain.internal](https://developer.apple.com/documentation/metal/mtllibraryerror/code/internal)

|  | Declaration |
| --- | --- |
| From | ``` case Internal ``` |
| To | ``` case `internal` ``` |

Modified [MTLLibraryErrorDomain.unsupported](https://developer.apple.com/documentation/metal/mtllibraryerror/mtllibraryerrorunsupported)

|  | Declaration |
| --- | --- |
| From | ``` case Unsupported ``` |
| To | ``` case unsupported ``` |

Modified [MTLLoadAction [enum]](https://developer.apple.com/documentation/metal/mtlloadaction)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLLoadAction : UInt {     case DontCare     case Load     case Clear } ``` |
| To | ``` enum MTLLoadAction : UInt {     case dontCare     case load     case clear } ``` |

Modified [MTLLoadAction.clear](https://developer.apple.com/documentation/metal/mtlloadaction/clear)

|  | Declaration |
| --- | --- |
| From | ``` case Clear ``` |
| To | ``` case clear ``` |

Modified [MTLLoadAction.dontCare](https://developer.apple.com/documentation/metal/mtlloadaction/dontcare)

|  | Declaration |
| --- | --- |
| From | ``` case DontCare ``` |
| To | ``` case dontCare ``` |

Modified [MTLLoadAction.load](https://developer.apple.com/documentation/metal/mtlloadaction/load)

|  | Declaration |
| --- | --- |
| From | ``` case Load ``` |
| To | ``` case load ``` |

Modified [MTLMultisampleDepthResolveFilter [enum]](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLMultisampleDepthResolveFilter : UInt {     case Sample0     case Min     case Max } ``` |
| To | ``` enum MTLMultisampleDepthResolveFilter : UInt {     case sample0     case min     case max } ``` |

Modified [MTLMultisampleDepthResolveFilter.max](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter/mtlmultisampledepthresolvefiltermax)

|  | Declaration |
| --- | --- |
| From | ``` case Max ``` |
| To | ``` case max ``` |

Modified [MTLMultisampleDepthResolveFilter.min](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter/mtlmultisampledepthresolvefiltermin)

|  | Declaration |
| --- | --- |
| From | ``` case Min ``` |
| To | ``` case min ``` |

Modified [MTLMultisampleDepthResolveFilter.sample0](https://developer.apple.com/documentation/metal/mtlmultisampledepthresolvefilter/mtlmultisampledepthresolvefiltersample0)

|  | Declaration |
| --- | --- |
| From | ``` case Sample0 ``` |
| To | ``` case sample0 ``` |

Modified [MTLParallelRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLParallelRenderCommandEncoder : MTLCommandEncoder {     func renderCommandEncoder() -> MTLRenderCommandEncoder } ``` |
| To | ``` protocol MTLParallelRenderCommandEncoder : MTLCommandEncoder {     func makeRenderCommandEncoder() -> MTLRenderCommandEncoder     func setColorStoreAction(_ storeAction: MTLStoreAction, at colorAttachmentIndex: Int)     func setDepthStoreAction(_ storeAction: MTLStoreAction)     func setStencilStoreAction(_ storeAction: MTLStoreAction) } ``` |

Modified [MTLParallelRenderCommandEncoder.makeRenderCommandEncoder() -> MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/1515911-makerendercommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` func renderCommandEncoder() -> MTLRenderCommandEncoder ``` |
| To | ``` func makeRenderCommandEncoder() -> MTLRenderCommandEncoder ``` |

Modified [MTLPipelineOption [struct]](https://developer.apple.com/documentation/metal/mtlpipelineoption)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MTLPipelineOption : OptionSetType {     init(rawValue rawValue: UInt)     static var None: MTLPipelineOption { get }     static var ArgumentInfo: MTLPipelineOption { get }     static var BufferTypeInfo: MTLPipelineOption { get } } ``` | OptionSetType |
| To | ``` struct MTLPipelineOption : OptionSet {     init(rawValue rawValue: UInt)     static var none: MTLPipelineOption { get }     static var argumentInfo: MTLPipelineOption { get }     static var bufferTypeInfo: MTLPipelineOption { get }     func intersect(_ other: MTLPipelineOption) -> MTLPipelineOption     func exclusiveOr(_ other: MTLPipelineOption) -> MTLPipelineOption     mutating func unionInPlace(_ other: MTLPipelineOption)     mutating func intersectInPlace(_ other: MTLPipelineOption)     mutating func exclusiveOrInPlace(_ other: MTLPipelineOption)     func isSubsetOf(_ other: MTLPipelineOption) -> Bool     func isDisjointWith(_ other: MTLPipelineOption) -> Bool     func isSupersetOf(_ other: MTLPipelineOption) -> Bool     mutating func subtractInPlace(_ other: MTLPipelineOption)     func isStrictSupersetOf(_ other: MTLPipelineOption) -> Bool     func isStrictSubsetOf(_ other: MTLPipelineOption) -> Bool } extension MTLPipelineOption {     func union(_ other: MTLPipelineOption) -> MTLPipelineOption     func intersection(_ other: MTLPipelineOption) -> MTLPipelineOption     func symmetricDifference(_ other: MTLPipelineOption) -> MTLPipelineOption } extension MTLPipelineOption {     func contains(_ member: MTLPipelineOption) -> Bool     mutating func insert(_ newMember: MTLPipelineOption) -> (inserted: Bool, memberAfterInsert: MTLPipelineOption)     mutating func remove(_ member: MTLPipelineOption) -> MTLPipelineOption?     mutating func update(with newMember: MTLPipelineOption) -> MTLPipelineOption? } extension MTLPipelineOption {     convenience init()     mutating func formUnion(_ other: MTLPipelineOption)     mutating func formIntersection(_ other: MTLPipelineOption)     mutating func formSymmetricDifference(_ other: MTLPipelineOption) } extension MTLPipelineOption {     convenience init<S : Sequence where S.Iterator.Element == MTLPipelineOption>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MTLPipelineOption...)     mutating func subtract(_ other: MTLPipelineOption)     func isSubset(of other: MTLPipelineOption) -> Bool     func isSuperset(of other: MTLPipelineOption) -> Bool     func isDisjoint(with other: MTLPipelineOption) -> Bool     func subtracting(_ other: MTLPipelineOption) -> MTLPipelineOption     var isEmpty: Bool { get }     func isStrictSuperset(of other: MTLPipelineOption) -> Bool     func isStrictSubset(of other: MTLPipelineOption) -> Bool } ``` | OptionSet |

Modified [MTLPipelineOption.argumentInfo](https://developer.apple.com/documentation/metal/mtlpipelineoption/mtlpipelineoptionargumentinfo)

|  | Declaration |
| --- | --- |
| From | ``` static var ArgumentInfo: MTLPipelineOption { get } ``` |
| To | ``` static var argumentInfo: MTLPipelineOption { get } ``` |

Modified [MTLPipelineOption.bufferTypeInfo](https://developer.apple.com/documentation/metal/mtlpipelineoption/mtlpipelineoptionbuffertypeinfo)

|  | Declaration |
| --- | --- |
| From | ``` static var BufferTypeInfo: MTLPipelineOption { get } ``` |
| To | ``` static var bufferTypeInfo: MTLPipelineOption { get } ``` |

Modified [MTLPixelFormat [enum]](https://developer.apple.com/documentation/metal/mtlpixelformat)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLPixelFormat : UInt {     case Invalid     case A8Unorm     case R8Unorm     case R8Unorm_sRGB     case R8Snorm     case R8Uint     case R8Sint     case R16Unorm     case R16Snorm     case R16Uint     case R16Sint     case R16Float     case RG8Unorm     case RG8Unorm_sRGB     case RG8Snorm     case RG8Uint     case RG8Sint     case B5G6R5Unorm     case A1BGR5Unorm     case ABGR4Unorm     case BGR5A1Unorm     case R32Uint     case R32Sint     case R32Float     case RG16Unorm     case RG16Snorm     case RG16Uint     case RG16Sint     case RG16Float     case RGBA8Unorm     case RGBA8Unorm_sRGB     case RGBA8Snorm     case RGBA8Uint     case RGBA8Sint     case BGRA8Unorm     case BGRA8Unorm_sRGB     case RGB10A2Unorm     case RGB10A2Uint     case RG11B10Float     case RGB9E5Float     case RG32Uint     case RG32Sint     case RG32Float     case RGBA16Unorm     case RGBA16Snorm     case RGBA16Uint     case RGBA16Sint     case RGBA16Float     case RGBA32Uint     case RGBA32Sint     case RGBA32Float     case BC1_RGBA     case BC1_RGBA_sRGB     case BC2_RGBA     case BC2_RGBA_sRGB     case BC3_RGBA     case BC3_RGBA_sRGB     case BC4_RUnorm     case BC4_RSnorm     case BC5_RGUnorm     case BC5_RGSnorm     case BC6H_RGBFloat     case BC6H_RGBUfloat     case BC7_RGBAUnorm     case BC7_RGBAUnorm_sRGB     case PVRTC_RGB_2BPP     case PVRTC_RGB_2BPP_sRGB     case PVRTC_RGB_4BPP     case PVRTC_RGB_4BPP_sRGB     case PVRTC_RGBA_2BPP     case PVRTC_RGBA_2BPP_sRGB     case PVRTC_RGBA_4BPP     case PVRTC_RGBA_4BPP_sRGB     case EAC_R11Unorm     case EAC_R11Snorm     case EAC_RG11Unorm     case EAC_RG11Snorm     case EAC_RGBA8     case EAC_RGBA8_sRGB     case ETC2_RGB8     case ETC2_RGB8_sRGB     case ETC2_RGB8A1     case ETC2_RGB8A1_sRGB     case ASTC_4x4_sRGB     case ASTC_5x4_sRGB     case ASTC_5x5_sRGB     case ASTC_6x5_sRGB     case ASTC_6x6_sRGB     case ASTC_8x5_sRGB     case ASTC_8x6_sRGB     case ASTC_8x8_sRGB     case ASTC_10x5_sRGB     case ASTC_10x6_sRGB     case ASTC_10x8_sRGB     case ASTC_10x10_sRGB     case ASTC_12x10_sRGB     case ASTC_12x12_sRGB     case ASTC_4x4_LDR     case ASTC_5x4_LDR     case ASTC_5x5_LDR     case ASTC_6x5_LDR     case ASTC_6x6_LDR     case ASTC_8x5_LDR     case ASTC_8x6_LDR     case ASTC_8x8_LDR     case ASTC_10x5_LDR     case ASTC_10x6_LDR     case ASTC_10x8_LDR     case ASTC_10x10_LDR     case ASTC_12x10_LDR     case ASTC_12x12_LDR     case GBGR422     case BGRG422     case Depth32Float     case Stencil8     case Depth24Unorm_Stencil8     case Depth32Float_Stencil8 } ``` |
| To | ``` enum MTLPixelFormat : UInt {     case invalid     case a8Unorm     case r8Unorm     case r8Unorm_srgb     case r8Snorm     case r8Uint     case r8Sint     case r16Unorm     case r16Snorm     case r16Uint     case r16Sint     case r16Float     case rg8Unorm     case rg8Unorm_srgb     case rg8Snorm     case rg8Uint     case rg8Sint     case b5g6r5Unorm     case a1bgr5Unorm     case abgr4Unorm     case bgr5A1Unorm     case r32Uint     case r32Sint     case r32Float     case rg16Unorm     case rg16Snorm     case rg16Uint     case rg16Sint     case rg16Float     case rgba8Unorm     case rgba8Unorm_srgb     case rgba8Snorm     case rgba8Uint     case rgba8Sint     case bgra8Unorm     case bgra8Unorm_srgb     case rgb10a2Unorm     case rgb10a2Uint     case rg11b10Float     case rgb9e5Float     case bgr10_xr     case bgr10_xr_srgb     case rg32Uint     case rg32Sint     case rg32Float     case rgba16Unorm     case rgba16Snorm     case rgba16Uint     case rgba16Sint     case rgba16Float     case BGRA10_XR     case bgra10_XR_sRGB     case rgba32Uint     case rgba32Sint     case rgba32Float     case bc1_rgba     case bc1_rgba_srgb     case bc2_rgba     case bc2_rgba_srgb     case bc3_rgba     case bc3_rgba_srgb     case bc4_rUnorm     case bc4_rSnorm     case bc5_rgUnorm     case bc5_rgSnorm     case bc6H_rgbFloat     case bc6H_rgbuFloat     case bc7_rgbaUnorm     case bc7_rgbaUnorm_srgb     case pvrtc_rgb_2bpp     case pvrtc_rgb_2bpp_srgb     case pvrtc_rgb_4bpp     case pvrtc_rgb_4bpp_srgb     case pvrtc_rgba_2bpp     case pvrtc_rgba_2bpp_srgb     case pvrtc_rgba_4bpp     case pvrtc_rgba_4bpp_srgb     case eac_r11Unorm     case eac_r11Snorm     case eac_rg11Unorm     case eac_rg11Snorm     case eac_rgba8     case eac_rgba8_srgb     case etc2_rgb8     case etc2_rgb8_srgb     case etc2_rgb8a1     case etc2_rgb8a1_srgb     case astc_4x4_srgb     case astc_5x4_srgb     case astc_5x5_srgb     case astc_6x5_srgb     case astc_6x6_srgb     case astc_8x5_srgb     case astc_8x6_srgb     case astc_8x8_srgb     case astc_10x5_srgb     case astc_10x6_srgb     case astc_10x8_srgb     case astc_10x10_srgb     case astc_12x10_srgb     case astc_12x12_srgb     case astc_4x4_ldr     case astc_5x4_ldr     case astc_5x5_ldr     case astc_6x5_ldr     case astc_6x6_ldr     case astc_8x5_ldr     case astc_8x6_ldr     case astc_8x8_ldr     case astc_10x5_ldr     case astc_10x6_ldr     case astc_10x8_ldr     case astc_10x10_ldr     case astc_12x10_ldr     case astc_12x12_ldr     case gbgr422     case bgrg422     case depth32Float     case stencil8     case depth24Unorm_stencil8     case depth32Float_stencil8     case x32_stencil8     case x24_stencil8 } ``` |

Modified [MTLPixelFormat.a1bgr5Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformata1bgr5unorm)

|  | Declaration |
| --- | --- |
| From | ``` case A1BGR5Unorm ``` |
| To | ``` case a1bgr5Unorm ``` |

Modified [MTLPixelFormat.a8Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/a8unorm)

|  | Declaration |
| --- | --- |
| From | ``` case A8Unorm ``` |
| To | ``` case a8Unorm ``` |

Modified [MTLPixelFormat.abgr4Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/abgr4unorm)

|  | Declaration |
| --- | --- |
| From | ``` case ABGR4Unorm ``` |
| To | ``` case abgr4Unorm ``` |

Modified [MTLPixelFormat.astc_10x10_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatastc_10x10_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_10x10_LDR ``` |
| To | ``` case astc_10x10_ldr ``` |

Modified [MTLPixelFormat.astc_10x10_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatastc_10x10_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_10x10_sRGB ``` |
| To | ``` case astc_10x10_srgb ``` |

Modified [MTLPixelFormat.astc_10x5_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_10x5_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_10x5_LDR ``` |
| To | ``` case astc_10x5_ldr ``` |

Modified [MTLPixelFormat.astc_10x5_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_10x5_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_10x5_sRGB ``` |
| To | ``` case astc_10x5_srgb ``` |

Modified [MTLPixelFormat.astc_10x6_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatastc_10x6_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_10x6_LDR ``` |
| To | ``` case astc_10x6_ldr ``` |

Modified [MTLPixelFormat.astc_10x6_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_10x6_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_10x6_sRGB ``` |
| To | ``` case astc_10x6_srgb ``` |

Modified [MTLPixelFormat.astc_10x8_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatastc_10x8_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_10x8_LDR ``` |
| To | ``` case astc_10x8_ldr ``` |

Modified [MTLPixelFormat.astc_10x8_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_10x8_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_10x8_sRGB ``` |
| To | ``` case astc_10x8_srgb ``` |

Modified [MTLPixelFormat.astc_12x10_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_12x10_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_12x10_LDR ``` |
| To | ``` case astc_12x10_ldr ``` |

Modified [MTLPixelFormat.astc_12x10_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_12x10_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_12x10_sRGB ``` |
| To | ``` case astc_12x10_srgb ``` |

Modified [MTLPixelFormat.astc_12x12_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatastc_12x12_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_12x12_LDR ``` |
| To | ``` case astc_12x12_ldr ``` |

Modified [MTLPixelFormat.astc_12x12_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_12x12_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_12x12_sRGB ``` |
| To | ``` case astc_12x12_srgb ``` |

Modified [MTLPixelFormat.astc_4x4_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatastc_4x4_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_4x4_LDR ``` |
| To | ``` case astc_4x4_ldr ``` |

Modified [MTLPixelFormat.astc_4x4_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_4x4_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_4x4_sRGB ``` |
| To | ``` case astc_4x4_srgb ``` |

Modified [MTLPixelFormat.astc_5x4_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_5x4_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_5x4_LDR ``` |
| To | ``` case astc_5x4_ldr ``` |

Modified [MTLPixelFormat.astc_5x4_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_5x4_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_5x4_sRGB ``` |
| To | ``` case astc_5x4_srgb ``` |

Modified [MTLPixelFormat.astc_5x5_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_5x5_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_5x5_LDR ``` |
| To | ``` case astc_5x5_ldr ``` |

Modified [MTLPixelFormat.astc_5x5_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_5x5_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_5x5_sRGB ``` |
| To | ``` case astc_5x5_srgb ``` |

Modified [MTLPixelFormat.astc_6x5_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_6x5_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_6x5_LDR ``` |
| To | ``` case astc_6x5_ldr ``` |

Modified [MTLPixelFormat.astc_6x5_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_6x5_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_6x5_sRGB ``` |
| To | ``` case astc_6x5_srgb ``` |

Modified [MTLPixelFormat.astc_6x6_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_6x6_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_6x6_LDR ``` |
| To | ``` case astc_6x6_ldr ``` |

Modified [MTLPixelFormat.astc_6x6_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatastc_6x6_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_6x6_sRGB ``` |
| To | ``` case astc_6x6_srgb ``` |

Modified [MTLPixelFormat.astc_8x5_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_8x5_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_8x5_LDR ``` |
| To | ``` case astc_8x5_ldr ``` |

Modified [MTLPixelFormat.astc_8x5_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatastc_8x5_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_8x5_sRGB ``` |
| To | ``` case astc_8x5_srgb ``` |

Modified [MTLPixelFormat.astc_8x6_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatastc_8x6_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_8x6_LDR ``` |
| To | ``` case astc_8x6_ldr ``` |

Modified [MTLPixelFormat.astc_8x6_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_8x6_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_8x6_sRGB ``` |
| To | ``` case astc_8x6_srgb ``` |

Modified [MTLPixelFormat.astc_8x8_ldr](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatastc_8x8_ldr)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_8x8_LDR ``` |
| To | ``` case astc_8x8_ldr ``` |

Modified [MTLPixelFormat.astc_8x8_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/astc_8x8_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ASTC_8x8_sRGB ``` |
| To | ``` case astc_8x8_srgb ``` |

Modified [MTLPixelFormat.b5g6r5Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/b5g6r5unorm)

|  | Declaration |
| --- | --- |
| From | ``` case B5G6R5Unorm ``` |
| To | ``` case b5g6r5Unorm ``` |

Modified [MTLPixelFormat.bgr5A1Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr5a1unorm)

|  | Declaration |
| --- | --- |
| From | ``` case BGR5A1Unorm ``` |
| To | ``` case bgr5A1Unorm ``` |

Modified [MTLPixelFormat.bgra8Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatbgra8unorm)

|  | Declaration |
| --- | --- |
| From | ``` case BGRA8Unorm ``` |
| To | ``` case bgra8Unorm ``` |

Modified [MTLPixelFormat.bgra8Unorm_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatbgra8unorm_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case BGRA8Unorm_sRGB ``` |
| To | ``` case bgra8Unorm_srgb ``` |

Modified [MTLPixelFormat.bgrg422](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatbgrg422)

|  | Declaration |
| --- | --- |
| From | ``` case BGRG422 ``` |
| To | ``` case bgrg422 ``` |

Modified [MTLPixelFormat.depth32Float](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatdepth32float)

|  | Declaration |
| --- | --- |
| From | ``` case Depth32Float ``` |
| To | ``` case depth32Float ``` |

Modified [MTLPixelFormat.depth32Float_stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/depth32float_stencil8)

|  | Declaration |
| --- | --- |
| From | ``` case Depth32Float_Stencil8 ``` |
| To | ``` case depth32Float_stencil8 ``` |

Modified [MTLPixelFormat.eac_r11Snorm](https://developer.apple.com/documentation/metal/mtlpixelformat/eac_r11snorm)

|  | Declaration |
| --- | --- |
| From | ``` case EAC_R11Snorm ``` |
| To | ``` case eac_r11Snorm ``` |

Modified [MTLPixelFormat.eac_r11Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/eac_r11unorm)

|  | Declaration |
| --- | --- |
| From | ``` case EAC_R11Unorm ``` |
| To | ``` case eac_r11Unorm ``` |

Modified [MTLPixelFormat.eac_rg11Snorm](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformateac_rg11snorm)

|  | Declaration |
| --- | --- |
| From | ``` case EAC_RG11Snorm ``` |
| To | ``` case eac_rg11Snorm ``` |

Modified [MTLPixelFormat.eac_rg11Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformateac_rg11unorm)

|  | Declaration |
| --- | --- |
| From | ``` case EAC_RG11Unorm ``` |
| To | ``` case eac_rg11Unorm ``` |

Modified [MTLPixelFormat.eac_rgba8](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformateac_rgba8)

|  | Declaration |
| --- | --- |
| From | ``` case EAC_RGBA8 ``` |
| To | ``` case eac_rgba8 ``` |

Modified [MTLPixelFormat.eac_rgba8_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformateac_rgba8_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case EAC_RGBA8_sRGB ``` |
| To | ``` case eac_rgba8_srgb ``` |

Modified [MTLPixelFormat.etc2_rgb8](https://developer.apple.com/documentation/metal/mtlpixelformat/etc2_rgb8)

|  | Declaration |
| --- | --- |
| From | ``` case ETC2_RGB8 ``` |
| To | ``` case etc2_rgb8 ``` |

Modified [MTLPixelFormat.etc2_rgb8_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/etc2_rgb8_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ETC2_RGB8_sRGB ``` |
| To | ``` case etc2_rgb8_srgb ``` |

Modified [MTLPixelFormat.etc2_rgb8a1](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatetc2_rgb8a1)

|  | Declaration |
| --- | --- |
| From | ``` case ETC2_RGB8A1 ``` |
| To | ``` case etc2_rgb8a1 ``` |

Modified [MTLPixelFormat.etc2_rgb8a1_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatetc2_rgb8a1_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case ETC2_RGB8A1_sRGB ``` |
| To | ``` case etc2_rgb8a1_srgb ``` |

Modified [MTLPixelFormat.gbgr422](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatgbgr422)

|  | Declaration |
| --- | --- |
| From | ``` case GBGR422 ``` |
| To | ``` case gbgr422 ``` |

Modified [MTLPixelFormat.invalid](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [MTLPixelFormat.pvrtc_rgb_2bpp](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatpvrtc_rgb_2bpp)

|  | Declaration |
| --- | --- |
| From | ``` case PVRTC_RGB_2BPP ``` |
| To | ``` case pvrtc_rgb_2bpp ``` |

Modified [MTLPixelFormat.pvrtc_rgb_2bpp_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatpvrtc_rgb_2bpp_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case PVRTC_RGB_2BPP_sRGB ``` |
| To | ``` case pvrtc_rgb_2bpp_srgb ``` |

Modified [MTLPixelFormat.pvrtc_rgb_4bpp](https://developer.apple.com/documentation/metal/mtlpixelformat/pvrtc_rgb_4bpp)

|  | Declaration |
| --- | --- |
| From | ``` case PVRTC_RGB_4BPP ``` |
| To | ``` case pvrtc_rgb_4bpp ``` |

Modified [MTLPixelFormat.pvrtc_rgb_4bpp_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/pvrtc_rgb_4bpp_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case PVRTC_RGB_4BPP_sRGB ``` |
| To | ``` case pvrtc_rgb_4bpp_srgb ``` |

Modified [MTLPixelFormat.pvrtc_rgba_2bpp](https://developer.apple.com/documentation/metal/mtlpixelformat/pvrtc_rgba_2bpp)

|  | Declaration |
| --- | --- |
| From | ``` case PVRTC_RGBA_2BPP ``` |
| To | ``` case pvrtc_rgba_2bpp ``` |

Modified [MTLPixelFormat.pvrtc_rgba_2bpp_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatpvrtc_rgba_2bpp_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case PVRTC_RGBA_2BPP_sRGB ``` |
| To | ``` case pvrtc_rgba_2bpp_srgb ``` |

Modified [MTLPixelFormat.pvrtc_rgba_4bpp](https://developer.apple.com/documentation/metal/mtlpixelformat/pvrtc_rgba_4bpp)

|  | Declaration |
| --- | --- |
| From | ``` case PVRTC_RGBA_4BPP ``` |
| To | ``` case pvrtc_rgba_4bpp ``` |

Modified [MTLPixelFormat.pvrtc_rgba_4bpp_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/pvrtc_rgba_4bpp_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case PVRTC_RGBA_4BPP_sRGB ``` |
| To | ``` case pvrtc_rgba_4bpp_srgb ``` |

Modified [MTLPixelFormat.r16Float](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatr16float)

|  | Declaration |
| --- | --- |
| From | ``` case R16Float ``` |
| To | ``` case r16Float ``` |

Modified [MTLPixelFormat.r16Sint](https://developer.apple.com/documentation/metal/mtlpixelformat/r16sint)

|  | Declaration |
| --- | --- |
| From | ``` case R16Sint ``` |
| To | ``` case r16Sint ``` |

Modified [MTLPixelFormat.r16Snorm](https://developer.apple.com/documentation/metal/mtlpixelformat/r16snorm)

|  | Declaration |
| --- | --- |
| From | ``` case R16Snorm ``` |
| To | ``` case r16Snorm ``` |

Modified [MTLPixelFormat.r16Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/r16uint)

|  | Declaration |
| --- | --- |
| From | ``` case R16Uint ``` |
| To | ``` case r16Uint ``` |

Modified [MTLPixelFormat.r16Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/r16unorm)

|  | Declaration |
| --- | --- |
| From | ``` case R16Unorm ``` |
| To | ``` case r16Unorm ``` |

Modified [MTLPixelFormat.r32Float](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatr32float)

|  | Declaration |
| --- | --- |
| From | ``` case R32Float ``` |
| To | ``` case r32Float ``` |

Modified [MTLPixelFormat.r32Sint](https://developer.apple.com/documentation/metal/mtlpixelformat/r32sint)

|  | Declaration |
| --- | --- |
| From | ``` case R32Sint ``` |
| To | ``` case r32Sint ``` |

Modified [MTLPixelFormat.r32Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatr32uint)

|  | Declaration |
| --- | --- |
| From | ``` case R32Uint ``` |
| To | ``` case r32Uint ``` |

Modified [MTLPixelFormat.r8Sint](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatr8sint)

|  | Declaration |
| --- | --- |
| From | ``` case R8Sint ``` |
| To | ``` case r8Sint ``` |

Modified [MTLPixelFormat.r8Snorm](https://developer.apple.com/documentation/metal/mtlpixelformat/r8snorm)

|  | Declaration |
| --- | --- |
| From | ``` case R8Snorm ``` |
| To | ``` case r8Snorm ``` |

Modified [MTLPixelFormat.r8Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatr8uint)

|  | Declaration |
| --- | --- |
| From | ``` case R8Uint ``` |
| To | ``` case r8Uint ``` |

Modified [MTLPixelFormat.r8Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/r8unorm)

|  | Declaration |
| --- | --- |
| From | ``` case R8Unorm ``` |
| To | ``` case r8Unorm ``` |

Modified [MTLPixelFormat.r8Unorm_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatr8unorm_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case R8Unorm_sRGB ``` |
| To | ``` case r8Unorm_srgb ``` |

Modified [MTLPixelFormat.rg11b10Float](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrg11b10float)

|  | Declaration |
| --- | --- |
| From | ``` case RG11B10Float ``` |
| To | ``` case rg11b10Float ``` |

Modified [MTLPixelFormat.rg16Float](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrg16float)

|  | Declaration |
| --- | --- |
| From | ``` case RG16Float ``` |
| To | ``` case rg16Float ``` |

Modified [MTLPixelFormat.rg16Sint](https://developer.apple.com/documentation/metal/mtlpixelformat/rg16sint)

|  | Declaration |
| --- | --- |
| From | ``` case RG16Sint ``` |
| To | ``` case rg16Sint ``` |

Modified [MTLPixelFormat.rg16Snorm](https://developer.apple.com/documentation/metal/mtlpixelformat/rg16snorm)

|  | Declaration |
| --- | --- |
| From | ``` case RG16Snorm ``` |
| To | ``` case rg16Snorm ``` |

Modified [MTLPixelFormat.rg16Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrg16uint)

|  | Declaration |
| --- | --- |
| From | ``` case RG16Uint ``` |
| To | ``` case rg16Uint ``` |

Modified [MTLPixelFormat.rg16Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/rg16unorm)

|  | Declaration |
| --- | --- |
| From | ``` case RG16Unorm ``` |
| To | ``` case rg16Unorm ``` |

Modified [MTLPixelFormat.rg32Float](https://developer.apple.com/documentation/metal/mtlpixelformat/rg32float)

|  | Declaration |
| --- | --- |
| From | ``` case RG32Float ``` |
| To | ``` case rg32Float ``` |

Modified [MTLPixelFormat.rg32Sint](https://developer.apple.com/documentation/metal/mtlpixelformat/rg32sint)

|  | Declaration |
| --- | --- |
| From | ``` case RG32Sint ``` |
| To | ``` case rg32Sint ``` |

Modified [MTLPixelFormat.rg32Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/rg32uint)

|  | Declaration |
| --- | --- |
| From | ``` case RG32Uint ``` |
| To | ``` case rg32Uint ``` |

Modified [MTLPixelFormat.rg8Sint](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrg8sint)

|  | Declaration |
| --- | --- |
| From | ``` case RG8Sint ``` |
| To | ``` case rg8Sint ``` |

Modified [MTLPixelFormat.rg8Snorm](https://developer.apple.com/documentation/metal/mtlpixelformat/rg8snorm)

|  | Declaration |
| --- | --- |
| From | ``` case RG8Snorm ``` |
| To | ``` case rg8Snorm ``` |

Modified [MTLPixelFormat.rg8Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/rg8uint)

|  | Declaration |
| --- | --- |
| From | ``` case RG8Uint ``` |
| To | ``` case rg8Uint ``` |

Modified [MTLPixelFormat.rg8Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/rg8unorm)

|  | Declaration |
| --- | --- |
| From | ``` case RG8Unorm ``` |
| To | ``` case rg8Unorm ``` |

Modified [MTLPixelFormat.rg8Unorm_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrg8unorm_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case RG8Unorm_sRGB ``` |
| To | ``` case rg8Unorm_srgb ``` |

Modified [MTLPixelFormat.rgb10a2Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/rgb10a2uint)

|  | Declaration |
| --- | --- |
| From | ``` case RGB10A2Uint ``` |
| To | ``` case rgb10a2Uint ``` |

Modified [MTLPixelFormat.rgb10a2Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/rgb10a2unorm)

|  | Declaration |
| --- | --- |
| From | ``` case RGB10A2Unorm ``` |
| To | ``` case rgb10a2Unorm ``` |

Modified [MTLPixelFormat.rgb9e5Float](https://developer.apple.com/documentation/metal/mtlpixelformat/rgb9e5float)

|  | Declaration |
| --- | --- |
| From | ``` case RGB9E5Float ``` |
| To | ``` case rgb9e5Float ``` |

Modified [MTLPixelFormat.rgba16Float](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrgba16float)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA16Float ``` |
| To | ``` case rgba16Float ``` |

Modified [MTLPixelFormat.rgba16Sint](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrgba16sint)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA16Sint ``` |
| To | ``` case rgba16Sint ``` |

Modified [MTLPixelFormat.rgba16Snorm](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrgba16snorm)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA16Snorm ``` |
| To | ``` case rgba16Snorm ``` |

Modified [MTLPixelFormat.rgba16Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/rgba16uint)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA16Uint ``` |
| To | ``` case rgba16Uint ``` |

Modified [MTLPixelFormat.rgba16Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/rgba16unorm)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA16Unorm ``` |
| To | ``` case rgba16Unorm ``` |

Modified [MTLPixelFormat.rgba32Float](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrgba32float)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA32Float ``` |
| To | ``` case rgba32Float ``` |

Modified [MTLPixelFormat.rgba32Sint](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrgba32sint)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA32Sint ``` |
| To | ``` case rgba32Sint ``` |

Modified [MTLPixelFormat.rgba32Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrgba32uint)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA32Uint ``` |
| To | ``` case rgba32Uint ``` |

Modified [MTLPixelFormat.rgba8Sint](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrgba8sint)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA8Sint ``` |
| To | ``` case rgba8Sint ``` |

Modified [MTLPixelFormat.rgba8Snorm](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatrgba8snorm)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA8Snorm ``` |
| To | ``` case rgba8Snorm ``` |

Modified [MTLPixelFormat.rgba8Uint](https://developer.apple.com/documentation/metal/mtlpixelformat/rgba8uint)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA8Uint ``` |
| To | ``` case rgba8Uint ``` |

Modified [MTLPixelFormat.rgba8Unorm](https://developer.apple.com/documentation/metal/mtlpixelformat/rgba8unorm)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA8Unorm ``` |
| To | ``` case rgba8Unorm ``` |

Modified [MTLPixelFormat.rgba8Unorm_srgb](https://developer.apple.com/documentation/metal/mtlpixelformat/rgba8unorm_srgb)

|  | Declaration |
| --- | --- |
| From | ``` case RGBA8Unorm_sRGB ``` |
| To | ``` case rgba8Unorm_srgb ``` |

Modified [MTLPixelFormat.stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatstencil8)

|  | Declaration |
| --- | --- |
| From | ``` case Stencil8 ``` |
| To | ``` case stencil8 ``` |

Modified [MTLPrimitiveType [enum]](https://developer.apple.com/documentation/metal/mtlprimitivetype)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLPrimitiveType : UInt {     case Point     case Line     case LineStrip     case Triangle     case TriangleStrip } ``` |
| To | ``` enum MTLPrimitiveType : UInt {     case point     case line     case lineStrip     case triangle     case triangleStrip } ``` |

Modified [MTLPrimitiveType.line](https://developer.apple.com/documentation/metal/mtlprimitivetype/line)

|  | Declaration |
| --- | --- |
| From | ``` case Line ``` |
| To | ``` case line ``` |

Modified [MTLPrimitiveType.lineStrip](https://developer.apple.com/documentation/metal/mtlprimitivetype/linestrip)

|  | Declaration |
| --- | --- |
| From | ``` case LineStrip ``` |
| To | ``` case lineStrip ``` |

Modified [MTLPrimitiveType.point](https://developer.apple.com/documentation/metal/mtlprimitivetype/point)

|  | Declaration |
| --- | --- |
| From | ``` case Point ``` |
| To | ``` case point ``` |

Modified [MTLPrimitiveType.triangle](https://developer.apple.com/documentation/metal/mtlprimitivetype/mtlprimitivetypetriangle)

|  | Declaration |
| --- | --- |
| From | ``` case Triangle ``` |
| To | ``` case triangle ``` |

Modified [MTLPrimitiveType.triangleStrip](https://developer.apple.com/documentation/metal/mtlprimitivetype/mtlprimitivetypetrianglestrip)

|  | Declaration |
| --- | --- |
| From | ``` case TriangleStrip ``` |
| To | ``` case triangleStrip ``` |

Modified [MTLPurgeableState [enum]](https://developer.apple.com/documentation/metal/mtlpurgeablestate)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLPurgeableState : UInt {     case KeepCurrent     case NonVolatile     case Volatile     case Empty } ``` |
| To | ``` enum MTLPurgeableState : UInt {     case keepCurrent     case nonVolatile     case volatile     case empty } ``` |

Modified [MTLPurgeableState.empty](https://developer.apple.com/documentation/metal/mtlpurgeablestate/mtlpurgeablestateempty)

|  | Declaration |
| --- | --- |
| From | ``` case Empty ``` |
| To | ``` case empty ``` |

Modified [MTLPurgeableState.keepCurrent](https://developer.apple.com/documentation/metal/mtlpurgeablestate/keepcurrent)

|  | Declaration |
| --- | --- |
| From | ``` case KeepCurrent ``` |
| To | ``` case keepCurrent ``` |

Modified [MTLPurgeableState.nonVolatile](https://developer.apple.com/documentation/metal/mtlpurgeablestate/mtlpurgeablestatenonvolatile)

|  | Declaration |
| --- | --- |
| From | ``` case NonVolatile ``` |
| To | ``` case nonVolatile ``` |

Modified [MTLPurgeableState.volatile](https://developer.apple.com/documentation/metal/mtlpurgeablestate/mtlpurgeablestatevolatile)

|  | Declaration |
| --- | --- |
| From | ``` case Volatile ``` |
| To | ``` case volatile ``` |

Modified [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLRenderCommandEncoder : MTLCommandEncoder {     func setRenderPipelineState(_ pipelineState: MTLRenderPipelineState)     func setVertexBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setVertexBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setVertexBufferOffset(_ offset: Int, atIndex index: Int)     func setVertexBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange)     func setVertexTexture(_ texture: MTLTexture?, atIndex index: Int)     func setVertexTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setViewport(_ viewport: MTLViewport)     func setFrontFacingWinding(_ frontFacingWinding: MTLWinding)     func setCullMode(_ cullMode: MTLCullMode)     func setDepthClipMode(_ depthClipMode: MTLDepthClipMode)     func setDepthBias(_ depthBias: Float, slopeScale slopeScale: Float, clamp clamp: Float)     func setScissorRect(_ rect: MTLScissorRect)     func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)     func setFragmentBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int)     func setFragmentBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int)     func setFragmentBufferOffset(_ offset: Int, atIndex index: Int)     func setFragmentBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offset: UnsafePointer<Int>, withRange range: NSRange)     func setFragmentTexture(_ texture: MTLTexture?, atIndex index: Int)     func setFragmentTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange)     func setBlendColorRed(_ red: Float, green green: Float, blue blue: Float, alpha alpha: Float)     func setDepthStencilState(_ depthStencilState: MTLDepthStencilState?)     func setStencilReferenceValue(_ referenceValue: UInt32)     func setStencilFrontReferenceValue(_ frontReferenceValue: UInt32, backReferenceValue backReferenceValue: UInt32)     func setVisibilityResultMode(_ mode: MTLVisibilityResultMode, offset offset: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int, baseInstance baseInstance: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int, baseVertex baseVertex: Int, baseInstance baseInstance: Int)     func drawPrimitives(_ primitiveType: MTLPrimitiveType, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int)     func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int) } ``` |
| To | ``` protocol MTLRenderCommandEncoder : MTLCommandEncoder {     func setRenderPipelineState(_ pipelineState: MTLRenderPipelineState)     func setVertexBytes(_ bytes: UnsafeRawPointer, length length: Int, at index: Int)     func setVertexBuffer(_ buffer: MTLBuffer?, offset offset: Int, at index: Int)     func setVertexBufferOffset(_ offset: Int, at index: Int)     func setVertexBuffers(_ buffers: UnsafePointer<MTLBuffer?>!, offsets offsets: UnsafePointer<Int>!, with range: NSRange)     func setVertexTexture(_ texture: MTLTexture?, at index: Int)     func setVertexTextures(_ textures: UnsafePointer<MTLTexture?>!, with range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState?, at index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, with range: NSRange)     func setVertexSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, at index: Int)     func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, lodMinClamps lodMinClamps: UnsafePointer<Float>!, lodMaxClamps lodMaxClamps: UnsafePointer<Float>!, with range: NSRange)     func setViewport(_ viewport: MTLViewport)     func setFrontFacing(_ frontFacingWinding: MTLWinding)     func setCullMode(_ cullMode: MTLCullMode)     func setDepthClipMode(_ depthClipMode: MTLDepthClipMode)     func setDepthBias(_ depthBias: Float, slopeScale slopeScale: Float, clamp clamp: Float)     func setScissorRect(_ rect: MTLScissorRect)     func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)     func setFragmentBytes(_ bytes: UnsafeRawPointer, length length: Int, at index: Int)     func setFragmentBuffer(_ buffer: MTLBuffer?, offset offset: Int, at index: Int)     func setFragmentBufferOffset(_ offset: Int, at index: Int)     func setFragmentBuffers(_ buffers: UnsafePointer<MTLBuffer?>!, offsets offset: UnsafePointer<Int>!, with range: NSRange)     func setFragmentTexture(_ texture: MTLTexture?, at index: Int)     func setFragmentTextures(_ textures: UnsafePointer<MTLTexture?>!, with range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState?, at index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, with range: NSRange)     func setFragmentSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, at index: Int)     func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, lodMinClamps lodMinClamps: UnsafePointer<Float>!, lodMaxClamps lodMaxClamps: UnsafePointer<Float>!, with range: NSRange)     func setBlendColor(red red: Float, green green: Float, blue blue: Float, alpha alpha: Float)     func setDepthStencilState(_ depthStencilState: MTLDepthStencilState?)     func setStencilReferenceValue(_ referenceValue: UInt32)     func setStencilReferenceValues(front frontReferenceValue: UInt32, back backReferenceValue: UInt32)     func setVisibilityResultMode(_ mode: MTLVisibilityResultMode, offset offset: Int)     func setColorStoreAction(_ storeAction: MTLStoreAction, at colorAttachmentIndex: Int)     func setDepthStoreAction(_ storeAction: MTLStoreAction)     func setStencilStoreAction(_ storeAction: MTLStoreAction)     func drawPrimitives(type primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int)     func drawPrimitives(type primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int)     func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int)     func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int)     func drawPrimitives(type primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int, baseInstance baseInstance: Int)     func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int, baseVertex baseVertex: Int, baseInstance baseInstance: Int)     func drawPrimitives(type primitiveType: MTLPrimitiveType, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int)     func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int)     func textureBarrier()     func update(_ fence: MTLFence, after stages: MTLRenderStages)     func wait(for fence: MTLFence, before stages: MTLRenderStages)     func setTessellationFactorBuffer(_ buffer: MTLBuffer?, offset offset: Int, instanceStride instanceStride: Int)     func setTessellationFactorScale(_ scale: Float)     func drawPatches(numberOfPatchControlPoints numberOfPatchControlPoints: Int, patchStart patchStart: Int, patchCount patchCount: Int, patchIndexBuffer patchIndexBuffer: MTLBuffer?, patchIndexBufferOffset patchIndexBufferOffset: Int, instanceCount instanceCount: Int, baseInstance baseInstance: Int)     func drawPatches(numberOfPatchControlPoints numberOfPatchControlPoints: Int, patchIndexBuffer patchIndexBuffer: MTLBuffer?, patchIndexBufferOffset patchIndexBufferOffset: Int, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int)     func drawIndexedPatches(numberOfPatchControlPoints numberOfPatchControlPoints: Int, patchStart patchStart: Int, patchCount patchCount: Int, patchIndexBuffer patchIndexBuffer: MTLBuffer?, patchIndexBufferOffset patchIndexBufferOffset: Int, controlPointIndexBuffer controlPointIndexBuffer: MTLBuffer, controlPointIndexBufferOffset controlPointIndexBufferOffset: Int, instanceCount instanceCount: Int, baseInstance baseInstance: Int)     func drawIndexedPatches(numberOfPatchControlPoints numberOfPatchControlPoints: Int, patchIndexBuffer patchIndexBuffer: MTLBuffer?, patchIndexBufferOffset patchIndexBufferOffset: Int, controlPointIndexBuffer controlPointIndexBuffer: MTLBuffer, controlPointIndexBufferOffset controlPointIndexBufferOffset: Int, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int) } ``` |

Modified [MTLRenderCommandEncoder.drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLBuffer, indexBufferOffset: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515542-drawindexedprimitives)

|  | Declaration |
| --- | --- |
| From | ``` func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int) ``` |
| To | ``` func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int) ``` |

Modified [MTLRenderCommandEncoder.drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLBuffer, indexBufferOffset: Int, instanceCount: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515699-drawindexedprimitives)

|  | Declaration |
| --- | --- |
| From | ``` func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int) ``` |
| To | ``` func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int) ``` |

Modified [MTLRenderCommandEncoder.drawIndexedPrimitives(type: MTLPrimitiveType, indexCount: Int, indexType: MTLIndexType, indexBuffer: MTLBuffer, indexBufferOffset: Int, instanceCount: Int, baseVertex: Int, baseInstance: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515520-drawindexedprimitives)

|  | Declaration |
| --- | --- |
| From | ``` func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int, baseVertex baseVertex: Int, baseInstance baseInstance: Int) ``` |
| To | ``` func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexCount indexCount: Int, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, instanceCount instanceCount: Int, baseVertex baseVertex: Int, baseInstance baseInstance: Int) ``` |

Modified [MTLRenderCommandEncoder.drawIndexedPrimitives(type: MTLPrimitiveType, indexType: MTLIndexType, indexBuffer: MTLBuffer, indexBufferOffset: Int, indirectBuffer: MTLBuffer, indirectBufferOffset: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515392-drawindexedprimitives)

|  | Declaration |
| --- | --- |
| From | ``` func drawIndexedPrimitives(_ primitiveType: MTLPrimitiveType, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int) ``` |
| To | ``` func drawIndexedPrimitives(type primitiveType: MTLPrimitiveType, indexType indexType: MTLIndexType, indexBuffer indexBuffer: MTLBuffer, indexBufferOffset indexBufferOffset: Int, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int) ``` |

Modified [MTLRenderCommandEncoder.drawPrimitives(type: MTLPrimitiveType, indirectBuffer: MTLBuffer, indirectBufferOffset: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515467-drawprimitives)

|  | Declaration |
| --- | --- |
| From | ``` func drawPrimitives(_ primitiveType: MTLPrimitiveType, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int) ``` |
| To | ``` func drawPrimitives(type primitiveType: MTLPrimitiveType, indirectBuffer indirectBuffer: MTLBuffer, indirectBufferOffset indirectBufferOffset: Int) ``` |

Modified [MTLRenderCommandEncoder.drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516326-drawprimitives)

|  | Declaration |
| --- | --- |
| From | ``` func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int) ``` |
| To | ``` func drawPrimitives(type primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int) ``` |

Modified [MTLRenderCommandEncoder.drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515327-drawprimitives)

|  | Declaration |
| --- | --- |
| From | ``` func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int) ``` |
| To | ``` func drawPrimitives(type primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int) ``` |

Modified [MTLRenderCommandEncoder.drawPrimitives(type: MTLPrimitiveType, vertexStart: Int, vertexCount: Int, instanceCount: Int, baseInstance: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515561-drawprimitives)

|  | Declaration |
| --- | --- |
| From | ``` func drawPrimitives(_ primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int, baseInstance baseInstance: Int) ``` |
| To | ``` func drawPrimitives(type primitiveType: MTLPrimitiveType, vertexStart vertexStart: Int, vertexCount vertexCount: Int, instanceCount instanceCount: Int, baseInstance baseInstance: Int) ``` |

Modified [MTLRenderCommandEncoder.setBlendColor(red: Float, green: Float, blue: Float, alpha: Float)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515592-setblendcolorred)

|  | Declaration |
| --- | --- |
| From | ``` func setBlendColorRed(_ red: Float, green green: Float, blue blue: Float, alpha alpha: Float) ``` |
| To | ``` func setBlendColor(red red: Float, green green: Float, blue blue: Float, alpha alpha: Float) ``` |

Modified [MTLRenderCommandEncoder.setFragmentBuffer(_: MTLBuffer?, offset: Int, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515470-setfragmentbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int) ``` |
| To | ``` func setFragmentBuffer(_ buffer: MTLBuffer?, offset offset: Int, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setFragmentBufferOffset(_: Int, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515917-setfragmentbufferoffset)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentBufferOffset(_ offset: Int, atIndex index: Int) ``` |
| To | ``` func setFragmentBufferOffset(_ offset: Int, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setFragmentBuffers(_: UnsafePointer<MTLBuffer?>!, offsets: UnsafePointer<Int>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515724-setfragmentbuffers)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offset: UnsafePointer<Int>, withRange range: NSRange) ``` |
| To | ``` func setFragmentBuffers(_ buffers: UnsafePointer<MTLBuffer?>!, offsets offset: UnsafePointer<Int>!, with range: NSRange) ``` |

Modified [MTLRenderCommandEncoder.setFragmentBytes(_: UnsafeRawPointer, length: Int, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516192-setfragmentbytes)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int) ``` |
| To | ``` func setFragmentBytes(_ bytes: UnsafeRawPointer, length length: Int, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setFragmentSamplerState(_: MTLSamplerState?, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515577-setfragmentsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int) ``` |
| To | ``` func setFragmentSamplerState(_ sampler: MTLSamplerState?, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setFragmentSamplerState(_: MTLSamplerState?, lodMinClamp: Float, lodMaxClamp: Float, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515485-setfragmentsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int) ``` |
| To | ``` func setFragmentSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setFragmentSamplerStates(_: UnsafePointer<MTLSamplerState?>!, lodMinClamps: UnsafePointer<Float>!, lodMaxClamps: UnsafePointer<Float>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515463-setfragmentsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange) ``` |
| To | ``` func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, lodMinClamps lodMinClamps: UnsafePointer<Float>!, lodMaxClamps lodMaxClamps: UnsafePointer<Float>!, with range: NSRange) ``` |

Modified [MTLRenderCommandEncoder.setFragmentSamplerStates(_: UnsafePointer<MTLSamplerState?>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515970-setfragmentsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange) ``` |
| To | ``` func setFragmentSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, with range: NSRange) ``` |

Modified [MTLRenderCommandEncoder.setFragmentTexture(_: MTLTexture?, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515390-setfragmenttexture)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentTexture(_ texture: MTLTexture?, atIndex index: Int) ``` |
| To | ``` func setFragmentTexture(_ texture: MTLTexture?, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setFragmentTextures(_: UnsafePointer<MTLTexture?>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515878-setfragmenttextures)

|  | Declaration |
| --- | --- |
| From | ``` func setFragmentTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange) ``` |
| To | ``` func setFragmentTextures(_ textures: UnsafePointer<MTLTexture?>!, with range: NSRange) ``` |

Modified [MTLRenderCommandEncoder.setFrontFacing(_: MTLWinding)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515499-setfrontfacing)

|  | Declaration |
| --- | --- |
| From | ``` func setFrontFacingWinding(_ frontFacingWinding: MTLWinding) ``` |
| To | ``` func setFrontFacing(_ frontFacingWinding: MTLWinding) ``` |

Modified [MTLRenderCommandEncoder.setStencilReferenceValues(front: UInt32, back: UInt32)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515522-setstencilreferencevalues)

|  | Declaration |
| --- | --- |
| From | ``` func setStencilFrontReferenceValue(_ frontReferenceValue: UInt32, backReferenceValue backReferenceValue: UInt32) ``` |
| To | ``` func setStencilReferenceValues(front frontReferenceValue: UInt32, back backReferenceValue: UInt32) ``` |

Modified [MTLRenderCommandEncoder.setVertexBuffer(_: MTLBuffer?, offset: Int, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515829-setvertexbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexBuffer(_ buffer: MTLBuffer?, offset offset: Int, atIndex index: Int) ``` |
| To | ``` func setVertexBuffer(_ buffer: MTLBuffer?, offset offset: Int, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setVertexBufferOffset(_: Int, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515433-setvertexbufferoffset)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexBufferOffset(_ offset: Int, atIndex index: Int) ``` |
| To | ``` func setVertexBufferOffset(_ offset: Int, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setVertexBuffers(_: UnsafePointer<MTLBuffer?>!, offsets: UnsafePointer<Int>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515987-setvertexbuffers)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexBuffers(_ buffers: UnsafePointer<MTLBuffer?>, offsets offsets: UnsafePointer<Int>, withRange range: NSRange) ``` |
| To | ``` func setVertexBuffers(_ buffers: UnsafePointer<MTLBuffer?>!, offsets offsets: UnsafePointer<Int>!, with range: NSRange) ``` |

Modified [MTLRenderCommandEncoder.setVertexBytes(_: UnsafeRawPointer, length: Int, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515846-setvertexbytes)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexBytes(_ bytes: UnsafePointer<Void>, length length: Int, atIndex index: Int) ``` |
| To | ``` func setVertexBytes(_ bytes: UnsafeRawPointer, length length: Int, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setVertexSamplerState(_: MTLSamplerState?, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515537-setvertexsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexSamplerState(_ sampler: MTLSamplerState?, atIndex index: Int) ``` |
| To | ``` func setVertexSamplerState(_ sampler: MTLSamplerState?, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setVertexSamplerState(_: MTLSamplerState?, lodMinClamp: Float, lodMaxClamp: Float, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515864-setvertexsamplerstate)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, atIndex index: Int) ``` |
| To | ``` func setVertexSamplerState(_ sampler: MTLSamplerState?, lodMinClamp lodMinClamp: Float, lodMaxClamp lodMaxClamp: Float, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setVertexSamplerStates(_: UnsafePointer<MTLSamplerState?>!, lodMinClamps: UnsafePointer<Float>!, lodMaxClamps: UnsafePointer<Float>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516322-setvertexsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, lodMinClamps lodMinClamps: UnsafePointer<Float>, lodMaxClamps lodMaxClamps: UnsafePointer<Float>, withRange range: NSRange) ``` |
| To | ``` func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, lodMinClamps lodMinClamps: UnsafePointer<Float>!, lodMaxClamps lodMaxClamps: UnsafePointer<Float>!, with range: NSRange) ``` |

Modified [MTLRenderCommandEncoder.setVertexSamplerStates(_: UnsafePointer<MTLSamplerState?>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515400-setvertexsamplerstates)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>, withRange range: NSRange) ``` |
| To | ``` func setVertexSamplerStates(_ samplers: UnsafePointer<MTLSamplerState?>!, with range: NSRange) ``` |

Modified [MTLRenderCommandEncoder.setVertexTexture(_: MTLTexture?, at: Int)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1515842-setvertextexture)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexTexture(_ texture: MTLTexture?, atIndex index: Int) ``` |
| To | ``` func setVertexTexture(_ texture: MTLTexture?, at index: Int) ``` |

Modified [MTLRenderCommandEncoder.setVertexTextures(_: UnsafePointer<MTLTexture?>!, with: NSRange)](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516109-setvertextextures)

|  | Declaration |
| --- | --- |
| From | ``` func setVertexTextures(_ textures: UnsafePointer<MTLTexture?>, withRange range: NSRange) ``` |
| To | ``` func setVertexTextures(_ textures: UnsafePointer<MTLTexture?>!, with range: NSRange) ``` |

Modified [MTLRenderPassAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLRenderPassAttachmentDescriptor : NSObject, NSCopying {     var texture: MTLTexture?     var level: Int     var slice: Int     var depthPlane: Int     var resolveTexture: MTLTexture?     var resolveLevel: Int     var resolveSlice: Int     var resolveDepthPlane: Int     var loadAction: MTLLoadAction     var storeAction: MTLStoreAction } ``` | NSCopying |
| To | ``` class MTLRenderPassAttachmentDescriptor : NSObject, NSCopying {     var texture: MTLTexture?     var level: Int     var slice: Int     var depthPlane: Int     var resolveTexture: MTLTexture?     var resolveLevel: Int     var resolveSlice: Int     var resolveDepthPlane: Int     var loadAction: MTLLoadAction     var storeAction: MTLStoreAction     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLRenderPassAttachmentDescriptor : CVarArg { } extension MTLRenderPassAttachmentDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLRenderPassColorAttachmentDescriptorArray](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLRenderPassColorAttachmentDescriptorArray : NSObject {     subscript (_ attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor!     func objectAtIndexedSubscript(_ attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor     func setObject(_ attachment: MTLRenderPassColorAttachmentDescriptor?, atIndexedSubscript attachmentIndex: Int) } ``` | -- |
| To | ``` class MTLRenderPassColorAttachmentDescriptorArray : NSObject {     subscript(_ attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor     func objectAtIndexedSubscript(_ attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor     func setObject(_ attachment: MTLRenderPassColorAttachmentDescriptor?, atIndexedSubscript attachmentIndex: Int)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLRenderPassColorAttachmentDescriptorArray : CVarArg { } extension MTLRenderPassColorAttachmentDescriptorArray : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLRenderPassColorAttachmentDescriptorArray.subscript(_: Int) -> MTLRenderPassColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray/1437977-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor! ``` |
| To | ``` subscript(_ attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor ``` |

Modified [MTLRenderPassDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpassdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLRenderPassDescriptor : NSObject, NSCopying {      init()     class func renderPassDescriptor() -> MTLRenderPassDescriptor     var colorAttachments: MTLRenderPassColorAttachmentDescriptorArray { get }     @NSCopying var depthAttachment: MTLRenderPassDepthAttachmentDescriptor!     @NSCopying var stencilAttachment: MTLRenderPassStencilAttachmentDescriptor!     var visibilityResultBuffer: MTLBuffer? } ``` | NSCopying |
| To | ``` class MTLRenderPassDescriptor : NSObject, NSCopying {      init()     class func renderPassDescriptor() -> MTLRenderPassDescriptor     var colorAttachments: MTLRenderPassColorAttachmentDescriptorArray { get }     @NSCopying var depthAttachment: MTLRenderPassDepthAttachmentDescriptor!     @NSCopying var stencilAttachment: MTLRenderPassStencilAttachmentDescriptor!     var visibilityResultBuffer: MTLBuffer?     var renderTargetArrayLength: Int     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLRenderPassDescriptor : CVarArg { } extension MTLRenderPassDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLRenderPipelineColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLRenderPipelineColorAttachmentDescriptor : NSObject, NSCopying {     var pixelFormat: MTLPixelFormat     var blendingEnabled: Bool     var sourceRGBBlendFactor: MTLBlendFactor     var destinationRGBBlendFactor: MTLBlendFactor     var rgbBlendOperation: MTLBlendOperation     var sourceAlphaBlendFactor: MTLBlendFactor     var destinationAlphaBlendFactor: MTLBlendFactor     var alphaBlendOperation: MTLBlendOperation     var writeMask: MTLColorWriteMask } ``` | NSCopying |
| To | ``` class MTLRenderPipelineColorAttachmentDescriptor : NSObject, NSCopying {     var pixelFormat: MTLPixelFormat     var isBlendingEnabled: Bool     var sourceRGBBlendFactor: MTLBlendFactor     var destinationRGBBlendFactor: MTLBlendFactor     var rgbBlendOperation: MTLBlendOperation     var sourceAlphaBlendFactor: MTLBlendFactor     var destinationAlphaBlendFactor: MTLBlendFactor     var alphaBlendOperation: MTLBlendOperation     var writeMask: MTLColorWriteMask     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLRenderPipelineColorAttachmentDescriptor : CVarArg { } extension MTLRenderPipelineColorAttachmentDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLRenderPipelineColorAttachmentDescriptor.isBlendingEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/1514642-isblendingenabled)

|  | Declaration |
| --- | --- |
| From | ``` var blendingEnabled: Bool ``` |
| To | ``` var isBlendingEnabled: Bool ``` |

Modified [MTLRenderPipelineColorAttachmentDescriptorArray](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLRenderPipelineColorAttachmentDescriptorArray : NSObject {     subscript (_ attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor!     func objectAtIndexedSubscript(_ attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor     func setObject(_ attachment: MTLRenderPipelineColorAttachmentDescriptor?, atIndexedSubscript attachmentIndex: Int) } ``` | -- |
| To | ``` class MTLRenderPipelineColorAttachmentDescriptorArray : NSObject {     subscript(_ attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor     func objectAtIndexedSubscript(_ attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor     func setObject(_ attachment: MTLRenderPipelineColorAttachmentDescriptor?, atIndexedSubscript attachmentIndex: Int)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLRenderPipelineColorAttachmentDescriptorArray : CVarArg { } extension MTLRenderPipelineColorAttachmentDescriptorArray : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLRenderPipelineColorAttachmentDescriptorArray.subscript(_: Int) -> MTLRenderPipelineColorAttachmentDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptorarray/1514673-objectatindexedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor! ``` |
| To | ``` subscript(_ attachmentIndex: Int) -> MTLRenderPipelineColorAttachmentDescriptor ``` |

Modified [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLRenderPipelineDescriptor : NSObject, NSCopying {     var label: String?     var vertexFunction: MTLFunction?     var fragmentFunction: MTLFunction?     @NSCopying var vertexDescriptor: MTLVertexDescriptor?     var sampleCount: Int     var alphaToCoverageEnabled: Bool     var alphaToOneEnabled: Bool     var rasterizationEnabled: Bool     var colorAttachments: MTLRenderPipelineColorAttachmentDescriptorArray { get }     var depthAttachmentPixelFormat: MTLPixelFormat     var stencilAttachmentPixelFormat: MTLPixelFormat     func reset() } ``` | NSCopying |
| To | ``` class MTLRenderPipelineDescriptor : NSObject, NSCopying {     var label: String?     var vertexFunction: MTLFunction?     var fragmentFunction: MTLFunction?     @NSCopying var vertexDescriptor: MTLVertexDescriptor?     var sampleCount: Int     var isAlphaToCoverageEnabled: Bool     var isAlphaToOneEnabled: Bool     var isRasterizationEnabled: Bool     var colorAttachments: MTLRenderPipelineColorAttachmentDescriptorArray { get }     var depthAttachmentPixelFormat: MTLPixelFormat     var stencilAttachmentPixelFormat: MTLPixelFormat     var inputPrimitiveTopology: MTLPrimitiveTopologyClass     var tessellationPartitionMode: MTLTessellationPartitionMode     var maxTessellationFactor: Int     var isTessellationFactorScaleEnabled: Bool     var tessellationFactorFormat: MTLTessellationFactorFormat     var tessellationControlPointIndexType: MTLTessellationControlPointIndexType     var tessellationFactorStepFunction: MTLTessellationFactorStepFunction     var tessellationOutputWindingOrder: MTLWinding     func reset()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLRenderPipelineDescriptor : CVarArg { } extension MTLRenderPipelineDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLRenderPipelineDescriptor.isAlphaToCoverageEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514624-isalphatocoverageenabled)

|  | Declaration |
| --- | --- |
| From | ``` var alphaToCoverageEnabled: Bool ``` |
| To | ``` var isAlphaToCoverageEnabled: Bool ``` |

Modified [MTLRenderPipelineDescriptor.isAlphaToOneEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514697-alphatooneenabled)

|  | Declaration |
| --- | --- |
| From | ``` var alphaToOneEnabled: Bool ``` |
| To | ``` var isAlphaToOneEnabled: Bool ``` |

Modified [MTLRenderPipelineDescriptor.isRasterizationEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1514708-rasterizationenabled)

|  | Declaration |
| --- | --- |
| From | ``` var rasterizationEnabled: Bool ``` |
| To | ``` var isRasterizationEnabled: Bool ``` |

Modified MTLRenderPipelineErrorDomain [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum MTLRenderPipelineError : UInt {     case Internal     case Unsupported     case InvalidInput } ``` |
| To | ``` enum MTLRenderPipelineErrorDomain : UInt {     case `internal`     case unsupported     case invalidInput } ``` |

Modified MTLRenderPipelineErrorDomain.internal

|  | Declaration |
| --- | --- |
| From | ``` case Internal ``` |
| To | ``` case `internal` ``` |

Modified MTLRenderPipelineErrorDomain.invalidInput

|  | Declaration |
| --- | --- |
| From | ``` case InvalidInput ``` |
| To | ``` case invalidInput ``` |

Modified MTLRenderPipelineErrorDomain.unsupported

|  | Declaration |
| --- | --- |
| From | ``` case Unsupported ``` |
| To | ``` case unsupported ``` |

Modified [MTLRenderPipelineReflection](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLRenderPipelineReflection : NSObject {     var vertexArguments: [MTLArgument]? { get }     var fragmentArguments: [MTLArgument]? { get } } ``` | -- |
| To | ``` class MTLRenderPipelineReflection : NSObject {     var vertexArguments: [MTLArgument]? { get }     var fragmentArguments: [MTLArgument]? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLRenderPipelineReflection : CVarArg { } extension MTLRenderPipelineReflection : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLResource](https://developer.apple.com/documentation/metal/mtlresource)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLResource : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     var cpuCacheMode: MTLCPUCacheMode { get }     var storageMode: MTLStorageMode { get }     func setPurgeableState(_ state: MTLPurgeableState) -> MTLPurgeableState } ``` |
| To | ``` protocol MTLResource : NSObjectProtocol {     var label: String? { get set }     var device: MTLDevice { get }     var cpuCacheMode: MTLCPUCacheMode { get }     var storageMode: MTLStorageMode { get }     func setPurgeableState(_ state: MTLPurgeableState) -> MTLPurgeableState     var heap: MTLHeap? { get }     func makeAliasable()     func isAliasable() -> Bool } ``` |

Modified [MTLResourceOptions [struct]](https://developer.apple.com/documentation/metal/mtlresourceoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MTLResourceOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var CPUCacheModeDefaultCache: MTLResourceOptions { get }     static var CPUCacheModeWriteCombined: MTLResourceOptions { get }     static var StorageModeShared: MTLResourceOptions { get }     static var StorageModeManaged: MTLResourceOptions { get }     static var StorageModePrivate: MTLResourceOptions { get }     static var OptionCPUCacheModeDefault: MTLResourceOptions { get }     static var OptionCPUCacheModeWriteCombined: MTLResourceOptions { get } } ``` | OptionSetType |
| To | ``` struct MTLResourceOptions : OptionSet {     init(rawValue rawValue: UInt)     static var cpuCacheModeDefaultCache: MTLResourceOptions { get }     static var cpuCacheModeWriteCombined: MTLResourceOptions { get }     static var storageModeShared: MTLResourceOptions { get }     static var storageModeManaged: MTLResourceOptions { get }     static var storageModePrivate: MTLResourceOptions { get }     static var storageModeMemoryless: MTLResourceOptions { get }     static var hazardTrackingModeUntracked: MTLResourceOptions { get }     static var optionCPUCacheModeDefault: MTLResourceOptions { get }     static var optionCPUCacheModeWriteCombined: MTLResourceOptions { get }     func intersect(_ other: MTLResourceOptions) -> MTLResourceOptions     func exclusiveOr(_ other: MTLResourceOptions) -> MTLResourceOptions     mutating func unionInPlace(_ other: MTLResourceOptions)     mutating func intersectInPlace(_ other: MTLResourceOptions)     mutating func exclusiveOrInPlace(_ other: MTLResourceOptions)     func isSubsetOf(_ other: MTLResourceOptions) -> Bool     func isDisjointWith(_ other: MTLResourceOptions) -> Bool     func isSupersetOf(_ other: MTLResourceOptions) -> Bool     mutating func subtractInPlace(_ other: MTLResourceOptions)     func isStrictSupersetOf(_ other: MTLResourceOptions) -> Bool     func isStrictSubsetOf(_ other: MTLResourceOptions) -> Bool } extension MTLResourceOptions {     func union(_ other: MTLResourceOptions) -> MTLResourceOptions     func intersection(_ other: MTLResourceOptions) -> MTLResourceOptions     func symmetricDifference(_ other: MTLResourceOptions) -> MTLResourceOptions } extension MTLResourceOptions {     func contains(_ member: MTLResourceOptions) -> Bool     mutating func insert(_ newMember: MTLResourceOptions) -> (inserted: Bool, memberAfterInsert: MTLResourceOptions)     mutating func remove(_ member: MTLResourceOptions) -> MTLResourceOptions?     mutating func update(with newMember: MTLResourceOptions) -> MTLResourceOptions? } extension MTLResourceOptions {     convenience init()     mutating func formUnion(_ other: MTLResourceOptions)     mutating func formIntersection(_ other: MTLResourceOptions)     mutating func formSymmetricDifference(_ other: MTLResourceOptions) } extension MTLResourceOptions {     convenience init<S : Sequence where S.Iterator.Element == MTLResourceOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MTLResourceOptions...)     mutating func subtract(_ other: MTLResourceOptions)     func isSubset(of other: MTLResourceOptions) -> Bool     func isSuperset(of other: MTLResourceOptions) -> Bool     func isDisjoint(with other: MTLResourceOptions) -> Bool     func subtracting(_ other: MTLResourceOptions) -> MTLResourceOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: MTLResourceOptions) -> Bool     func isStrictSubset(of other: MTLResourceOptions) -> Bool } ``` | OptionSet |

Modified [MTLResourceOptions.cpuCacheModeWriteCombined](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcecpucachemodewritecombined)

|  | Declaration |
| --- | --- |
| From | ``` static var CPUCacheModeWriteCombined: MTLResourceOptions { get } ``` |
| To | ``` static var cpuCacheModeWriteCombined: MTLResourceOptions { get } ``` |

Modified [MTLResourceOptions.optionCPUCacheModeWriteCombined](https://developer.apple.com/documentation/metal/mtlresourceoptions/1515912-optioncpucachemodewritecombined)

|  | Declaration |
| --- | --- |
| From | ``` static var OptionCPUCacheModeWriteCombined: MTLResourceOptions { get } ``` |
| To | ``` static var optionCPUCacheModeWriteCombined: MTLResourceOptions { get } ``` |

Modified [MTLResourceOptions.storageModePrivate](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcestoragemodeprivate)

|  | Declaration |
| --- | --- |
| From | ``` static var StorageModePrivate: MTLResourceOptions { get } ``` |
| To | ``` static var storageModePrivate: MTLResourceOptions { get } ``` |

Modified [MTLResourceOptions.storageModeShared](https://developer.apple.com/documentation/metal/mtlresourceoptions/1515613-storagemodeshared)

|  | Declaration |
| --- | --- |
| From | ``` static var StorageModeShared: MTLResourceOptions { get } ``` |
| To | ``` static var storageModeShared: MTLResourceOptions { get } ``` |

Modified [MTLSamplerAddressMode [enum]](https://developer.apple.com/documentation/metal/mtlsampleraddressmode)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLSamplerAddressMode : UInt {     case ClampToEdge     case MirrorClampToEdge     case Repeat     case MirrorRepeat     case ClampToZero } ``` |
| To | ``` enum MTLSamplerAddressMode : UInt {     case clampToEdge     case mirrorClampToEdge     case `repeat`     case mirrorRepeat     case clampToZero     case clampToBorderColor } ``` |

Modified [MTLSamplerAddressMode.clampToEdge](https://developer.apple.com/documentation/metal/mtlsampleraddressmode/mtlsampleraddressmodeclamptoedge)

|  | Declaration |
| --- | --- |
| From | ``` case ClampToEdge ``` |
| To | ``` case clampToEdge ``` |

Modified [MTLSamplerAddressMode.clampToZero](https://developer.apple.com/documentation/metal/mtlsampleraddressmode/mtlsampleraddressmodeclamptozero)

|  | Declaration |
| --- | --- |
| From | ``` case ClampToZero ``` |
| To | ``` case clampToZero ``` |

Modified [MTLSamplerAddressMode.mirrorRepeat](https://developer.apple.com/documentation/metal/mtlsampleraddressmode/mirrorrepeat)

|  | Declaration |
| --- | --- |
| From | ``` case MirrorRepeat ``` |
| To | ``` case mirrorRepeat ``` |

Modified [MTLSamplerAddressMode.repeat](https://developer.apple.com/documentation/metal/mtlsampleraddressmode/mtlsampleraddressmoderepeat)

|  | Declaration |
| --- | --- |
| From | ``` case Repeat ``` |
| To | ``` case `repeat` ``` |

Modified [MTLSamplerDescriptor](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLSamplerDescriptor : NSObject, NSCopying {     var minFilter: MTLSamplerMinMagFilter     var magFilter: MTLSamplerMinMagFilter     var mipFilter: MTLSamplerMipFilter     var maxAnisotropy: Int     var sAddressMode: MTLSamplerAddressMode     var tAddressMode: MTLSamplerAddressMode     var rAddressMode: MTLSamplerAddressMode     var normalizedCoordinates: Bool     var lodMinClamp: Float     var lodMaxClamp: Float     var lodAverage: Bool     var compareFunction: MTLCompareFunction     var label: String? } ``` | NSCopying |
| To | ``` class MTLSamplerDescriptor : NSObject, NSCopying {     var minFilter: MTLSamplerMinMagFilter     var magFilter: MTLSamplerMinMagFilter     var mipFilter: MTLSamplerMipFilter     var maxAnisotropy: Int     var sAddressMode: MTLSamplerAddressMode     var tAddressMode: MTLSamplerAddressMode     var rAddressMode: MTLSamplerAddressMode     var borderColor: MTLSamplerBorderColor     var normalizedCoordinates: Bool     var lodMinClamp: Float     var lodMaxClamp: Float     var lodAverage: Bool     var compareFunction: MTLCompareFunction     var label: String?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLSamplerDescriptor : CVarArg { } extension MTLSamplerDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLSamplerMinMagFilter [enum]](https://developer.apple.com/documentation/metal/mtlsamplerminmagfilter)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLSamplerMinMagFilter : UInt {     case Nearest     case Linear } ``` |
| To | ``` enum MTLSamplerMinMagFilter : UInt {     case nearest     case linear } ``` |

Modified [MTLSamplerMinMagFilter.linear](https://developer.apple.com/documentation/metal/mtlsamplerminmagfilter/linear)

|  | Declaration |
| --- | --- |
| From | ``` case Linear ``` |
| To | ``` case linear ``` |

Modified [MTLSamplerMinMagFilter.nearest](https://developer.apple.com/documentation/metal/mtlsamplerminmagfilter/mtlsamplerminmagfilternearest)

|  | Declaration |
| --- | --- |
| From | ``` case Nearest ``` |
| To | ``` case nearest ``` |

Modified [MTLSamplerMipFilter [enum]](https://developer.apple.com/documentation/metal/mtlsamplermipfilter)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLSamplerMipFilter : UInt {     case NotMipmapped     case Nearest     case Linear } ``` |
| To | ``` enum MTLSamplerMipFilter : UInt {     case notMipmapped     case nearest     case linear } ``` |

Modified [MTLSamplerMipFilter.linear](https://developer.apple.com/documentation/metal/mtlsamplermipfilter/mtlsamplermipfilterlinear)

|  | Declaration |
| --- | --- |
| From | ``` case Linear ``` |
| To | ``` case linear ``` |

Modified [MTLSamplerMipFilter.nearest](https://developer.apple.com/documentation/metal/mtlsamplermipfilter/mtlsamplermipfilternearest)

|  | Declaration |
| --- | --- |
| From | ``` case Nearest ``` |
| To | ``` case nearest ``` |

Modified [MTLSamplerMipFilter.notMipmapped](https://developer.apple.com/documentation/metal/mtlsamplermipfilter/mtlsamplermipfilternotmipmapped)

|  | Declaration |
| --- | --- |
| From | ``` case NotMipmapped ``` |
| To | ``` case notMipmapped ``` |

Modified [MTLStencilDescriptor](https://developer.apple.com/documentation/metal/mtlstencildescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLStencilDescriptor : NSObject, NSCopying {     var stencilCompareFunction: MTLCompareFunction     var stencilFailureOperation: MTLStencilOperation     var depthFailureOperation: MTLStencilOperation     var depthStencilPassOperation: MTLStencilOperation     var readMask: UInt32     var writeMask: UInt32 } ``` | NSCopying |
| To | ``` class MTLStencilDescriptor : NSObject, NSCopying {     var stencilCompareFunction: MTLCompareFunction     var stencilFailureOperation: MTLStencilOperation     var depthFailureOperation: MTLStencilOperation     var depthStencilPassOperation: MTLStencilOperation     var readMask: UInt32     var writeMask: UInt32     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLStencilDescriptor : CVarArg { } extension MTLStencilDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLStencilOperation [enum]](https://developer.apple.com/documentation/metal/mtlstenciloperation)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLStencilOperation : UInt {     case Keep     case Zero     case Replace     case IncrementClamp     case DecrementClamp     case Invert     case IncrementWrap     case DecrementWrap } ``` |
| To | ``` enum MTLStencilOperation : UInt {     case keep     case zero     case replace     case incrementClamp     case decrementClamp     case invert     case incrementWrap     case decrementWrap } ``` |

Modified [MTLStencilOperation.decrementClamp](https://developer.apple.com/documentation/metal/mtlstenciloperation/decrementclamp)

|  | Declaration |
| --- | --- |
| From | ``` case DecrementClamp ``` |
| To | ``` case decrementClamp ``` |

Modified [MTLStencilOperation.decrementWrap](https://developer.apple.com/documentation/metal/mtlstenciloperation/mtlstenciloperationdecrementwrap)

|  | Declaration |
| --- | --- |
| From | ``` case DecrementWrap ``` |
| To | ``` case decrementWrap ``` |

Modified [MTLStencilOperation.incrementClamp](https://developer.apple.com/documentation/metal/mtlstenciloperation/incrementclamp)

|  | Declaration |
| --- | --- |
| From | ``` case IncrementClamp ``` |
| To | ``` case incrementClamp ``` |

Modified [MTLStencilOperation.incrementWrap](https://developer.apple.com/documentation/metal/mtlstenciloperation/mtlstenciloperationincrementwrap)

|  | Declaration |
| --- | --- |
| From | ``` case IncrementWrap ``` |
| To | ``` case incrementWrap ``` |

Modified [MTLStencilOperation.invert](https://developer.apple.com/documentation/metal/mtlstenciloperation/mtlstenciloperationinvert)

|  | Declaration |
| --- | --- |
| From | ``` case Invert ``` |
| To | ``` case invert ``` |

Modified [MTLStencilOperation.keep](https://developer.apple.com/documentation/metal/mtlstenciloperation/keep)

|  | Declaration |
| --- | --- |
| From | ``` case Keep ``` |
| To | ``` case keep ``` |

Modified [MTLStencilOperation.replace](https://developer.apple.com/documentation/metal/mtlstenciloperation/mtlstenciloperationreplace)

|  | Declaration |
| --- | --- |
| From | ``` case Replace ``` |
| To | ``` case replace ``` |

Modified [MTLStencilOperation.zero](https://developer.apple.com/documentation/metal/mtlstenciloperation/zero)

|  | Declaration |
| --- | --- |
| From | ``` case Zero ``` |
| To | ``` case zero ``` |

Modified [MTLStorageMode [enum]](https://developer.apple.com/documentation/metal/mtlstoragemode)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLStorageMode : UInt {     case Shared     case Managed     case Private } ``` |
| To | ``` enum MTLStorageMode : UInt {     case shared     case managed     case `private`     case memoryless } ``` |

Modified [MTLStorageMode.private](https://developer.apple.com/documentation/metal/mtlstoragemode/private)

|  | Declaration |
| --- | --- |
| From | ``` case Private ``` |
| To | ``` case `private` ``` |

Modified [MTLStorageMode.shared](https://developer.apple.com/documentation/metal/mtlstoragemode/mtlstoragemodeshared)

|  | Declaration |
| --- | --- |
| From | ``` case Shared ``` |
| To | ``` case shared ``` |

Modified [MTLStoreAction [enum]](https://developer.apple.com/documentation/metal/mtlstoreaction)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLStoreAction : UInt {     case DontCare     case Store     case MultisampleResolve } ``` |
| To | ``` enum MTLStoreAction : UInt {     case dontCare     case store     case multisampleResolve     case storeAndMultisampleResolve     case unknown } ``` |

Modified [MTLStoreAction.dontCare](https://developer.apple.com/documentation/metal/mtlstoreaction/dontcare)

|  | Declaration |
| --- | --- |
| From | ``` case DontCare ``` |
| To | ``` case dontCare ``` |

Modified [MTLStoreAction.multisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionmultisampleresolve)

|  | Declaration |
| --- | --- |
| From | ``` case MultisampleResolve ``` |
| To | ``` case multisampleResolve ``` |

Modified [MTLStoreAction.store](https://developer.apple.com/documentation/metal/mtlstoreaction/store)

|  | Declaration |
| --- | --- |
| From | ``` case Store ``` |
| To | ``` case store ``` |

Modified [MTLStructMember](https://developer.apple.com/documentation/metal/mtlstructmember)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLStructMember : NSObject {     var name: String { get }     var offset: Int { get }     var dataType: MTLDataType { get }     func structType() -> MTLStructType?     func arrayType() -> MTLArrayType? } ``` | -- |
| To | ``` class MTLStructMember : NSObject {     var name: String { get }     var offset: Int { get }     var dataType: MTLDataType { get }     func structType() -> MTLStructType?     func arrayType() -> MTLArrayType?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLStructMember : CVarArg { } extension MTLStructMember : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLStructType](https://developer.apple.com/documentation/metal/mtlstructtype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLStructType : NSObject {     var members: [MTLStructMember] { get }     func memberByName(_ name: String) -> MTLStructMember? } ``` | -- |
| To | ``` class MTLStructType : NSObject {     var members: [MTLStructMember] { get }     func memberByName(_ name: String) -> MTLStructMember?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLStructType : CVarArg { } extension MTLStructType : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLTexture](https://developer.apple.com/documentation/metal/mtltexture)

|  | Declaration |
| --- | --- |
| From | ``` protocol MTLTexture : MTLResource {     var rootResource: MTLResource? { get }     var parentTexture: MTLTexture? { get }     var parentRelativeLevel: Int { get }     var parentRelativeSlice: Int { get }     var buffer: MTLBuffer? { get }     var bufferOffset: Int { get }     var bufferBytesPerRow: Int { get }     var textureType: MTLTextureType { get }     var pixelFormat: MTLPixelFormat { get }     var width: Int { get }     var height: Int { get }     var depth: Int { get }     var mipmapLevelCount: Int { get }     var sampleCount: Int { get }     var arrayLength: Int { get }     var usage: MTLTextureUsage { get }     var framebufferOnly: Bool { get }     func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int, fromRegion region: MTLRegion, mipmapLevel level: Int, slice slice: Int)     func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, slice slice: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int)     func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, fromRegion region: MTLRegion, mipmapLevel level: Int)     func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int)     func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat) -> MTLTexture     func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat, textureType textureType: MTLTextureType, levels levelRange: NSRange, slices sliceRange: NSRange) -> MTLTexture } ``` |
| To | ``` protocol MTLTexture : MTLResource {     var rootResource: MTLResource? { get }     var parent: MTLTexture? { get }     var parentRelativeLevel: Int { get }     var parentRelativeSlice: Int { get }     var buffer: MTLBuffer? { get }     var bufferOffset: Int { get }     var bufferBytesPerRow: Int { get }     var textureType: MTLTextureType { get }     var pixelFormat: MTLPixelFormat { get }     var width: Int { get }     var height: Int { get }     var depth: Int { get }     var mipmapLevelCount: Int { get }     var sampleCount: Int { get }     var arrayLength: Int { get }     var usage: MTLTextureUsage { get }     var isFramebufferOnly: Bool { get }     func getBytes(_ pixelBytes: UnsafeMutableRawPointer, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int, from region: MTLRegion, mipmapLevel level: Int, slice slice: Int)     func replace(region region: MTLRegion, mipmapLevel level: Int, slice slice: Int, withBytes pixelBytes: UnsafeRawPointer, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int)     func getBytes(_ pixelBytes: UnsafeMutableRawPointer, bytesPerRow bytesPerRow: Int, from region: MTLRegion, mipmapLevel level: Int)     func replace(region region: MTLRegion, mipmapLevel level: Int, withBytes pixelBytes: UnsafeRawPointer, bytesPerRow bytesPerRow: Int)     func makeTextureView(pixelFormat pixelFormat: MTLPixelFormat) -> MTLTexture     func makeTextureView(pixelFormat pixelFormat: MTLPixelFormat, textureType textureType: MTLTextureType, levels levelRange: NSRange, slices sliceRange: NSRange) -> MTLTexture } ``` |

Modified [MTLTexture.getBytes(_: UnsafeMutableRawPointer, bytesPerRow: Int, bytesPerImage: Int, from: MTLRegion, mipmapLevel: Int, slice: Int)](https://developer.apple.com/documentation/metal/mtltexture/1516318-getbytes)

|  | Declaration |
| --- | --- |
| From | ``` func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int, fromRegion region: MTLRegion, mipmapLevel level: Int, slice slice: Int) ``` |
| To | ``` func getBytes(_ pixelBytes: UnsafeMutableRawPointer, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int, from region: MTLRegion, mipmapLevel level: Int, slice slice: Int) ``` |

Modified [MTLTexture.getBytes(_: UnsafeMutableRawPointer, bytesPerRow: Int, from: MTLRegion, mipmapLevel: Int)](https://developer.apple.com/documentation/metal/mtltexture/1515751-getbytes)

|  | Declaration |
| --- | --- |
| From | ``` func getBytes(_ pixelBytes: UnsafeMutablePointer<Void>, bytesPerRow bytesPerRow: Int, fromRegion region: MTLRegion, mipmapLevel level: Int) ``` |
| To | ``` func getBytes(_ pixelBytes: UnsafeMutableRawPointer, bytesPerRow bytesPerRow: Int, from region: MTLRegion, mipmapLevel level: Int) ``` |

Modified [MTLTexture.isFramebufferOnly](https://developer.apple.com/documentation/metal/mtltexture/1515749-isframebufferonly)

|  | Declaration |
| --- | --- |
| From | ``` var framebufferOnly: Bool { get } ``` |
| To | ``` var isFramebufferOnly: Bool { get } ``` |

Modified [MTLTexture.makeTextureView(pixelFormat: MTLPixelFormat) -> MTLTexture](https://developer.apple.com/documentation/metal/mtltexture/1515598-maketextureview)

|  | Declaration |
| --- | --- |
| From | ``` func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat) -> MTLTexture ``` |
| To | ``` func makeTextureView(pixelFormat pixelFormat: MTLPixelFormat) -> MTLTexture ``` |

Modified [MTLTexture.makeTextureView(pixelFormat: MTLPixelFormat, textureType: MTLTextureType, levels: NSRange, slices: NSRange) -> MTLTexture](https://developer.apple.com/documentation/metal/mtltexture/1515409-newtextureviewwithpixelformat)

|  | Declaration |
| --- | --- |
| From | ``` func newTextureViewWithPixelFormat(_ pixelFormat: MTLPixelFormat, textureType textureType: MTLTextureType, levels levelRange: NSRange, slices sliceRange: NSRange) -> MTLTexture ``` |
| To | ``` func makeTextureView(pixelFormat pixelFormat: MTLPixelFormat, textureType textureType: MTLTextureType, levels levelRange: NSRange, slices sliceRange: NSRange) -> MTLTexture ``` |

Modified [MTLTexture.parent](https://developer.apple.com/documentation/metal/mtltexture/1515372-parenttexture)

|  | Declaration |
| --- | --- |
| From | ``` var parentTexture: MTLTexture? { get } ``` |
| To | ``` var parent: MTLTexture? { get } ``` |

Modified [MTLTexture.replace(region: MTLRegion, mipmapLevel: Int, slice: Int, withBytes: UnsafeRawPointer, bytesPerRow: Int, bytesPerImage: Int)](https://developer.apple.com/documentation/metal/mtltexture/1515679-replaceregion)

|  | Declaration |
| --- | --- |
| From | ``` func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, slice slice: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int) ``` |
| To | ``` func replace(region region: MTLRegion, mipmapLevel level: Int, slice slice: Int, withBytes pixelBytes: UnsafeRawPointer, bytesPerRow bytesPerRow: Int, bytesPerImage bytesPerImage: Int) ``` |

Modified [MTLTexture.replace(region: MTLRegion, mipmapLevel: Int, withBytes: UnsafeRawPointer, bytesPerRow: Int)](https://developer.apple.com/documentation/metal/mtltexture/1515464-replaceregion)

|  | Declaration |
| --- | --- |
| From | ``` func replaceRegion(_ region: MTLRegion, mipmapLevel level: Int, withBytes pixelBytes: UnsafePointer<Void>, bytesPerRow bytesPerRow: Int) ``` |
| To | ``` func replace(region region: MTLRegion, mipmapLevel level: Int, withBytes pixelBytes: UnsafeRawPointer, bytesPerRow bytesPerRow: Int) ``` |

Modified [MTLTexture.rootResource](https://developer.apple.com/documentation/metal/mtltexture/1515579-rootresource)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

Modified [MTLTextureDescriptor](https://developer.apple.com/documentation/metal/mtltexturedescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLTextureDescriptor : NSObject, NSCopying {     class func texture2DDescriptorWithPixelFormat(_ pixelFormat: MTLPixelFormat, width width: Int, height height: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor     class func textureCubeDescriptorWithPixelFormat(_ pixelFormat: MTLPixelFormat, size size: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor     var textureType: MTLTextureType     var pixelFormat: MTLPixelFormat     var width: Int     var height: Int     var depth: Int     var mipmapLevelCount: Int     var sampleCount: Int     var arrayLength: Int     var resourceOptions: MTLResourceOptions     var cpuCacheMode: MTLCPUCacheMode     var storageMode: MTLStorageMode     var usage: MTLTextureUsage } ``` | NSCopying |
| To | ``` class MTLTextureDescriptor : NSObject, NSCopying {     class func texture2DDescriptor(pixelFormat pixelFormat: MTLPixelFormat, width width: Int, height height: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor     class func textureCubeDescriptor(pixelFormat pixelFormat: MTLPixelFormat, size size: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor     var textureType: MTLTextureType     var pixelFormat: MTLPixelFormat     var width: Int     var height: Int     var depth: Int     var mipmapLevelCount: Int     var sampleCount: Int     var arrayLength: Int     var resourceOptions: MTLResourceOptions     var cpuCacheMode: MTLCPUCacheMode     var storageMode: MTLStorageMode     var usage: MTLTextureUsage     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLTextureDescriptor : CVarArg { } extension MTLTextureDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLTextureDescriptor.texture2DDescriptor(pixelFormat: MTLPixelFormat, width: Int, height: Int, mipmapped: Bool) -> MTLTextureDescriptor [class]](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1515511-texture2ddescriptor)

|  | Declaration |
| --- | --- |
| From | ``` class func texture2DDescriptorWithPixelFormat(_ pixelFormat: MTLPixelFormat, width width: Int, height height: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor ``` |
| To | ``` class func texture2DDescriptor(pixelFormat pixelFormat: MTLPixelFormat, width width: Int, height height: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor ``` |

Modified [MTLTextureDescriptor.textureCubeDescriptor(pixelFormat: MTLPixelFormat, size: Int, mipmapped: Bool) -> MTLTextureDescriptor [class]](https://developer.apple.com/documentation/metal/mtltexturedescriptor/1516090-texturecubedescriptorwithpixelfo)

|  | Declaration |
| --- | --- |
| From | ``` class func textureCubeDescriptorWithPixelFormat(_ pixelFormat: MTLPixelFormat, size size: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor ``` |
| To | ``` class func textureCubeDescriptor(pixelFormat pixelFormat: MTLPixelFormat, size size: Int, mipmapped mipmapped: Bool) -> MTLTextureDescriptor ``` |

Modified [MTLTextureType [enum]](https://developer.apple.com/documentation/metal/mtltexturetype)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLTextureType : UInt {     case Type1D     case Type1DArray     case Type2D     case Type2DArray     case Type2DMultisample     case TypeCube     case TypeCubeArray     case Type3D } ``` |
| To | ``` enum MTLTextureType : UInt {     case type1D     case type1DArray     case type2D     case type2DArray     case type2DMultisample     case typeCube     case typeCubeArray     case type3D } ``` |

Modified [MTLTextureType.type1D](https://developer.apple.com/documentation/metal/mtltexturetype/type1d)

|  | Declaration |
| --- | --- |
| From | ``` case Type1D ``` |
| To | ``` case type1D ``` |

Modified [MTLTextureType.type1DArray](https://developer.apple.com/documentation/metal/mtltexturetype/type1darray)

|  | Declaration |
| --- | --- |
| From | ``` case Type1DArray ``` |
| To | ``` case type1DArray ``` |

Modified [MTLTextureType.type2D](https://developer.apple.com/documentation/metal/mtltexturetype/mtltexturetype2d)

|  | Declaration |
| --- | --- |
| From | ``` case Type2D ``` |
| To | ``` case type2D ``` |

Modified [MTLTextureType.type2DArray](https://developer.apple.com/documentation/metal/mtltexturetype/type2darray)

|  | Declaration |
| --- | --- |
| From | ``` case Type2DArray ``` |
| To | ``` case type2DArray ``` |

Modified [MTLTextureType.type2DMultisample](https://developer.apple.com/documentation/metal/mtltexturetype/mtltexturetype2dmultisample)

|  | Declaration |
| --- | --- |
| From | ``` case Type2DMultisample ``` |
| To | ``` case type2DMultisample ``` |

Modified [MTLTextureType.type3D](https://developer.apple.com/documentation/metal/mtltexturetype/mtltexturetype3d)

|  | Declaration |
| --- | --- |
| From | ``` case Type3D ``` |
| To | ``` case type3D ``` |

Modified [MTLTextureType.typeCube](https://developer.apple.com/documentation/metal/mtltexturetype/typecube)

|  | Declaration |
| --- | --- |
| From | ``` case TypeCube ``` |
| To | ``` case typeCube ``` |

Modified [MTLTextureUsage [struct]](https://developer.apple.com/documentation/metal/mtltextureusage)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MTLTextureUsage : OptionSetType {     init(rawValue rawValue: UInt)     static var Unknown: MTLTextureUsage { get }     static var ShaderRead: MTLTextureUsage { get }     static var ShaderWrite: MTLTextureUsage { get }     static var RenderTarget: MTLTextureUsage { get }     static var PixelFormatView: MTLTextureUsage { get } } ``` | OptionSetType |
| To | ``` struct MTLTextureUsage : OptionSet {     init(rawValue rawValue: UInt)     static var unknown: MTLTextureUsage { get }     static var shaderRead: MTLTextureUsage { get }     static var shaderWrite: MTLTextureUsage { get }     static var renderTarget: MTLTextureUsage { get }     static var pixelFormatView: MTLTextureUsage { get }     func intersect(_ other: MTLTextureUsage) -> MTLTextureUsage     func exclusiveOr(_ other: MTLTextureUsage) -> MTLTextureUsage     mutating func unionInPlace(_ other: MTLTextureUsage)     mutating func intersectInPlace(_ other: MTLTextureUsage)     mutating func exclusiveOrInPlace(_ other: MTLTextureUsage)     func isSubsetOf(_ other: MTLTextureUsage) -> Bool     func isDisjointWith(_ other: MTLTextureUsage) -> Bool     func isSupersetOf(_ other: MTLTextureUsage) -> Bool     mutating func subtractInPlace(_ other: MTLTextureUsage)     func isStrictSupersetOf(_ other: MTLTextureUsage) -> Bool     func isStrictSubsetOf(_ other: MTLTextureUsage) -> Bool } extension MTLTextureUsage {     func union(_ other: MTLTextureUsage) -> MTLTextureUsage     func intersection(_ other: MTLTextureUsage) -> MTLTextureUsage     func symmetricDifference(_ other: MTLTextureUsage) -> MTLTextureUsage } extension MTLTextureUsage {     func contains(_ member: MTLTextureUsage) -> Bool     mutating func insert(_ newMember: MTLTextureUsage) -> (inserted: Bool, memberAfterInsert: MTLTextureUsage)     mutating func remove(_ member: MTLTextureUsage) -> MTLTextureUsage?     mutating func update(with newMember: MTLTextureUsage) -> MTLTextureUsage? } extension MTLTextureUsage {     convenience init()     mutating func formUnion(_ other: MTLTextureUsage)     mutating func formIntersection(_ other: MTLTextureUsage)     mutating func formSymmetricDifference(_ other: MTLTextureUsage) } extension MTLTextureUsage {     convenience init<S : Sequence where S.Iterator.Element == MTLTextureUsage>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MTLTextureUsage...)     mutating func subtract(_ other: MTLTextureUsage)     func isSubset(of other: MTLTextureUsage) -> Bool     func isSuperset(of other: MTLTextureUsage) -> Bool     func isDisjoint(with other: MTLTextureUsage) -> Bool     func subtracting(_ other: MTLTextureUsage) -> MTLTextureUsage     var isEmpty: Bool { get }     func isStrictSuperset(of other: MTLTextureUsage) -> Bool     func isStrictSubset(of other: MTLTextureUsage) -> Bool } ``` | OptionSet |

Modified [MTLTextureUsage.pixelFormatView](https://developer.apple.com/documentation/metal/mtltextureusage/1516223-pixelformatview)

|  | Declaration |
| --- | --- |
| From | ``` static var PixelFormatView: MTLTextureUsage { get } ``` |
| To | ``` static var pixelFormatView: MTLTextureUsage { get } ``` |

Modified [MTLTextureUsage.renderTarget](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusagerendertarget)

|  | Declaration |
| --- | --- |
| From | ``` static var RenderTarget: MTLTextureUsage { get } ``` |
| To | ``` static var renderTarget: MTLTextureUsage { get } ``` |

Modified [MTLTextureUsage.shaderRead](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusageshaderread)

|  | Declaration |
| --- | --- |
| From | ``` static var ShaderRead: MTLTextureUsage { get } ``` |
| To | ``` static var shaderRead: MTLTextureUsage { get } ``` |

Modified [MTLTextureUsage.shaderWrite](https://developer.apple.com/documentation/metal/mtltextureusage/1515854-shaderwrite)

|  | Declaration |
| --- | --- |
| From | ``` static var ShaderWrite: MTLTextureUsage { get } ``` |
| To | ``` static var shaderWrite: MTLTextureUsage { get } ``` |

Modified [MTLTextureUsage.unknown](https://developer.apple.com/documentation/metal/mtltextureusage/mtltextureusageunknown)

|  | Declaration |
| --- | --- |
| From | ``` static var Unknown: MTLTextureUsage { get } ``` |
| To | ``` static var unknown: MTLTextureUsage { get } ``` |

Modified [MTLTriangleFillMode [enum]](https://developer.apple.com/documentation/metal/mtltrianglefillmode)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLTriangleFillMode : UInt {     case Fill     case Lines } ``` |
| To | ``` enum MTLTriangleFillMode : UInt {     case fill     case lines } ``` |

Modified [MTLTriangleFillMode.fill](https://developer.apple.com/documentation/metal/mtltrianglefillmode/mtltrianglefillmodefill)

|  | Declaration |
| --- | --- |
| From | ``` case Fill ``` |
| To | ``` case fill ``` |

Modified [MTLTriangleFillMode.lines](https://developer.apple.com/documentation/metal/mtltrianglefillmode/mtltrianglefillmodelines)

|  | Declaration |
| --- | --- |
| From | ``` case Lines ``` |
| To | ``` case lines ``` |

Modified [MTLVertexAttribute](https://developer.apple.com/documentation/metal/mtlvertexattribute)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLVertexAttribute : NSObject {     var name: String? { get }     var attributeIndex: Int { get }     var attributeType: MTLDataType { get }     var active: Bool { get } } ``` | -- |
| To | ``` class MTLVertexAttribute : NSObject {     var name: String? { get }     var attributeIndex: Int { get }     var attributeType: MTLDataType { get }     var isActive: Bool { get }     var isPatchData: Bool { get }     var isPatchControlPointData: Bool { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLVertexAttribute : CVarArg { } extension MTLVertexAttribute : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLVertexAttribute.isActive](https://developer.apple.com/documentation/metal/mtlvertexattribute/1515994-active)

|  | Declaration |
| --- | --- |
| From | ``` var active: Bool { get } ``` |
| To | ``` var isActive: Bool { get } ``` |

Modified [MTLVertexAttributeDescriptor](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLVertexAttributeDescriptor : NSObject, NSCopying {     var format: MTLVertexFormat     var offset: Int     var bufferIndex: Int } ``` | NSCopying |
| To | ``` class MTLVertexAttributeDescriptor : NSObject, NSCopying {     var format: MTLVertexFormat     var offset: Int     var bufferIndex: Int     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLVertexAttributeDescriptor : CVarArg { } extension MTLVertexAttributeDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLVertexAttributeDescriptorArray](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLVertexAttributeDescriptorArray : NSObject {     subscript (_ index: Int) -> MTLVertexAttributeDescriptor!     func objectAtIndexedSubscript(_ index: Int) -> MTLVertexAttributeDescriptor     func setObject(_ attributeDesc: MTLVertexAttributeDescriptor?, atIndexedSubscript index: Int) } ``` | -- |
| To | ``` class MTLVertexAttributeDescriptorArray : NSObject {     subscript(_ index: Int) -> MTLVertexAttributeDescriptor     func objectAtIndexedSubscript(_ index: Int) -> MTLVertexAttributeDescriptor     func setObject(_ attributeDesc: MTLVertexAttributeDescriptor?, atIndexedSubscript index: Int)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLVertexAttributeDescriptorArray : CVarArg { } extension MTLVertexAttributeDescriptorArray : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLVertexAttributeDescriptorArray.subscript(_: Int) -> MTLVertexAttributeDescriptor](https://developer.apple.com/documentation/metal/mtlvertexattributedescriptorarray/1516138-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> MTLVertexAttributeDescriptor! ``` |
| To | ``` subscript(_ index: Int) -> MTLVertexAttributeDescriptor ``` |

Modified [MTLVertexBufferLayoutDescriptor](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLVertexBufferLayoutDescriptor : NSObject, NSCopying {     var stride: Int     var stepFunction: MTLVertexStepFunction     var stepRate: Int } ``` | NSCopying |
| To | ``` class MTLVertexBufferLayoutDescriptor : NSObject, NSCopying {     var stride: Int     var stepFunction: MTLVertexStepFunction     var stepRate: Int     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLVertexBufferLayoutDescriptor : CVarArg { } extension MTLVertexBufferLayoutDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLVertexBufferLayoutDescriptorArray](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLVertexBufferLayoutDescriptorArray : NSObject {     subscript (_ index: Int) -> MTLVertexBufferLayoutDescriptor!     func objectAtIndexedSubscript(_ index: Int) -> MTLVertexBufferLayoutDescriptor     func setObject(_ bufferDesc: MTLVertexBufferLayoutDescriptor?, atIndexedSubscript index: Int) } ``` | -- |
| To | ``` class MTLVertexBufferLayoutDescriptorArray : NSObject {     subscript(_ index: Int) -> MTLVertexBufferLayoutDescriptor     func objectAtIndexedSubscript(_ index: Int) -> MTLVertexBufferLayoutDescriptor     func setObject(_ bufferDesc: MTLVertexBufferLayoutDescriptor?, atIndexedSubscript index: Int)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLVertexBufferLayoutDescriptorArray : CVarArg { } extension MTLVertexBufferLayoutDescriptorArray : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MTLVertexBufferLayoutDescriptorArray.subscript(_: Int) -> MTLVertexBufferLayoutDescriptor](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptorarray/1516230-subscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ index: Int) -> MTLVertexBufferLayoutDescriptor! ``` |
| To | ``` subscript(_ index: Int) -> MTLVertexBufferLayoutDescriptor ``` |

Modified [MTLVertexDescriptor](https://developer.apple.com/documentation/metal/mtlvertexdescriptor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MTLVertexDescriptor : NSObject, NSCopying {      init()     class func vertexDescriptor() -> MTLVertexDescriptor     var layouts: MTLVertexBufferLayoutDescriptorArray { get }     var attributes: MTLVertexAttributeDescriptorArray { get }     func reset() } ``` | NSCopying |
| To | ``` class MTLVertexDescriptor : NSObject, NSCopying {      init()     class func vertexDescriptor() -> MTLVertexDescriptor     var layouts: MTLVertexBufferLayoutDescriptorArray { get }     var attributes: MTLVertexAttributeDescriptorArray { get }     func reset()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MTLVertexDescriptor : CVarArg { } extension MTLVertexDescriptor : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MTLVertexFormat [enum]](https://developer.apple.com/documentation/metal/mtlvertexformat)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLVertexFormat : UInt {     case Invalid     case UChar2     case UChar3     case UChar4     case Char2     case Char3     case Char4     case UChar2Normalized     case UChar3Normalized     case UChar4Normalized     case Char2Normalized     case Char3Normalized     case Char4Normalized     case UShort2     case UShort3     case UShort4     case Short2     case Short3     case Short4     case UShort2Normalized     case UShort3Normalized     case UShort4Normalized     case Short2Normalized     case Short3Normalized     case Short4Normalized     case Half2     case Half3     case Half4     case Float     case Float2     case Float3     case Float4     case Int     case Int2     case Int3     case Int4     case UInt     case UInt2     case UInt3     case UInt4     case Int1010102Normalized     case UInt1010102Normalized } ``` |
| To | ``` enum MTLVertexFormat : UInt {     case invalid     case uchar2     case uchar3     case uchar4     case char2     case char3     case char4     case uchar2Normalized     case uchar3Normalized     case uchar4Normalized     case char2Normalized     case char3Normalized     case char4Normalized     case ushort2     case ushort3     case ushort4     case short2     case short3     case short4     case ushort2Normalized     case ushort3Normalized     case ushort4Normalized     case short2Normalized     case short3Normalized     case short4Normalized     case half2     case half3     case half4     case float     case float2     case float3     case float4     case int     case int2     case int3     case int4     case uint     case uint2     case uint3     case uint4     case int1010102Normalized     case uint1010102Normalized } ``` |

Modified [MTLVertexFormat.char2](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatchar2)

|  | Declaration |
| --- | --- |
| From | ``` case Char2 ``` |
| To | ``` case char2 ``` |

Modified [MTLVertexFormat.char2Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatchar2normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Char2Normalized ``` |
| To | ``` case char2Normalized ``` |

Modified [MTLVertexFormat.char3](https://developer.apple.com/documentation/metal/mtlvertexformat/char3)

|  | Declaration |
| --- | --- |
| From | ``` case Char3 ``` |
| To | ``` case char3 ``` |

Modified [MTLVertexFormat.char3Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/char3normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Char3Normalized ``` |
| To | ``` case char3Normalized ``` |

Modified [MTLVertexFormat.char4](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatchar4)

|  | Declaration |
| --- | --- |
| From | ``` case Char4 ``` |
| To | ``` case char4 ``` |

Modified [MTLVertexFormat.char4Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/char4normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Char4Normalized ``` |
| To | ``` case char4Normalized ``` |

Modified [MTLVertexFormat.float](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatfloat)

|  | Declaration |
| --- | --- |
| From | ``` case Float ``` |
| To | ``` case float ``` |

Modified [MTLVertexFormat.float2](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatfloat2)

|  | Declaration |
| --- | --- |
| From | ``` case Float2 ``` |
| To | ``` case float2 ``` |

Modified [MTLVertexFormat.float3](https://developer.apple.com/documentation/metal/mtlvertexformat/float3)

|  | Declaration |
| --- | --- |
| From | ``` case Float3 ``` |
| To | ``` case float3 ``` |

Modified [MTLVertexFormat.float4](https://developer.apple.com/documentation/metal/mtlvertexformat/float4)

|  | Declaration |
| --- | --- |
| From | ``` case Float4 ``` |
| To | ``` case float4 ``` |

Modified [MTLVertexFormat.half2](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformathalf2)

|  | Declaration |
| --- | --- |
| From | ``` case Half2 ``` |
| To | ``` case half2 ``` |

Modified [MTLVertexFormat.half3](https://developer.apple.com/documentation/metal/mtlvertexformat/half3)

|  | Declaration |
| --- | --- |
| From | ``` case Half3 ``` |
| To | ``` case half3 ``` |

Modified [MTLVertexFormat.half4](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformathalf4)

|  | Declaration |
| --- | --- |
| From | ``` case Half4 ``` |
| To | ``` case half4 ``` |

Modified [MTLVertexFormat.int](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatint)

|  | Declaration |
| --- | --- |
| From | ``` case Int ``` |
| To | ``` case int ``` |

Modified [MTLVertexFormat.int1010102Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatint1010102normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Int1010102Normalized ``` |
| To | ``` case int1010102Normalized ``` |

Modified [MTLVertexFormat.int2](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatint2)

|  | Declaration |
| --- | --- |
| From | ``` case Int2 ``` |
| To | ``` case int2 ``` |

Modified [MTLVertexFormat.int3](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatint3)

|  | Declaration |
| --- | --- |
| From | ``` case Int3 ``` |
| To | ``` case int3 ``` |

Modified [MTLVertexFormat.int4](https://developer.apple.com/documentation/metal/mtlvertexformat/int4)

|  | Declaration |
| --- | --- |
| From | ``` case Int4 ``` |
| To | ``` case int4 ``` |

Modified [MTLVertexFormat.invalid](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [MTLVertexFormat.short2](https://developer.apple.com/documentation/metal/mtlvertexformat/short2)

|  | Declaration |
| --- | --- |
| From | ``` case Short2 ``` |
| To | ``` case short2 ``` |

Modified [MTLVertexFormat.short2Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/short2normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Short2Normalized ``` |
| To | ``` case short2Normalized ``` |

Modified [MTLVertexFormat.short3](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatshort3)

|  | Declaration |
| --- | --- |
| From | ``` case Short3 ``` |
| To | ``` case short3 ``` |

Modified [MTLVertexFormat.short3Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/short3normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Short3Normalized ``` |
| To | ``` case short3Normalized ``` |

Modified [MTLVertexFormat.short4](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatshort4)

|  | Declaration |
| --- | --- |
| From | ``` case Short4 ``` |
| To | ``` case short4 ``` |

Modified [MTLVertexFormat.short4Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/short4normalized)

|  | Declaration |
| --- | --- |
| From | ``` case Short4Normalized ``` |
| To | ``` case short4Normalized ``` |

Modified [MTLVertexFormat.uchar2](https://developer.apple.com/documentation/metal/mtlvertexformat/uchar2)

|  | Declaration |
| --- | --- |
| From | ``` case UChar2 ``` |
| To | ``` case uchar2 ``` |

Modified [MTLVertexFormat.uchar2Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/uchar2normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UChar2Normalized ``` |
| To | ``` case uchar2Normalized ``` |

Modified [MTLVertexFormat.uchar3](https://developer.apple.com/documentation/metal/mtlvertexformat/uchar3)

|  | Declaration |
| --- | --- |
| From | ``` case UChar3 ``` |
| To | ``` case uchar3 ``` |

Modified [MTLVertexFormat.uchar3Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatuchar3normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UChar3Normalized ``` |
| To | ``` case uchar3Normalized ``` |

Modified [MTLVertexFormat.uchar4](https://developer.apple.com/documentation/metal/mtlvertexformat/uchar4)

|  | Declaration |
| --- | --- |
| From | ``` case UChar4 ``` |
| To | ``` case uchar4 ``` |

Modified [MTLVertexFormat.uchar4Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/uchar4normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UChar4Normalized ``` |
| To | ``` case uchar4Normalized ``` |

Modified [MTLVertexFormat.uint](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatuint)

|  | Declaration |
| --- | --- |
| From | ``` case UInt ``` |
| To | ``` case uint ``` |

Modified [MTLVertexFormat.uint1010102Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatuint1010102normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UInt1010102Normalized ``` |
| To | ``` case uint1010102Normalized ``` |

Modified [MTLVertexFormat.uint2](https://developer.apple.com/documentation/metal/mtlvertexformat/uint2)

|  | Declaration |
| --- | --- |
| From | ``` case UInt2 ``` |
| To | ``` case uint2 ``` |

Modified [MTLVertexFormat.uint3](https://developer.apple.com/documentation/metal/mtlvertexformat/uint3)

|  | Declaration |
| --- | --- |
| From | ``` case UInt3 ``` |
| To | ``` case uint3 ``` |

Modified [MTLVertexFormat.uint4](https://developer.apple.com/documentation/metal/mtlvertexformat/uint4)

|  | Declaration |
| --- | --- |
| From | ``` case UInt4 ``` |
| To | ``` case uint4 ``` |

Modified [MTLVertexFormat.ushort2](https://developer.apple.com/documentation/metal/mtlvertexformat/ushort2)

|  | Declaration |
| --- | --- |
| From | ``` case UShort2 ``` |
| To | ``` case ushort2 ``` |

Modified [MTLVertexFormat.ushort2Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/ushort2normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UShort2Normalized ``` |
| To | ``` case ushort2Normalized ``` |

Modified [MTLVertexFormat.ushort3](https://developer.apple.com/documentation/metal/mtlvertexformat/ushort3)

|  | Declaration |
| --- | --- |
| From | ``` case UShort3 ``` |
| To | ``` case ushort3 ``` |

Modified [MTLVertexFormat.ushort3Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/ushort3normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UShort3Normalized ``` |
| To | ``` case ushort3Normalized ``` |

Modified [MTLVertexFormat.ushort4](https://developer.apple.com/documentation/metal/mtlvertexformat/ushort4)

|  | Declaration |
| --- | --- |
| From | ``` case UShort4 ``` |
| To | ``` case ushort4 ``` |

Modified [MTLVertexFormat.ushort4Normalized](https://developer.apple.com/documentation/metal/mtlvertexformat/mtlvertexformatushort4normalized)

|  | Declaration |
| --- | --- |
| From | ``` case UShort4Normalized ``` |
| To | ``` case ushort4Normalized ``` |

Modified [MTLVertexStepFunction [enum]](https://developer.apple.com/documentation/metal/mtlvertexstepfunction)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLVertexStepFunction : UInt {     case Constant     case PerVertex     case PerInstance } ``` |
| To | ``` enum MTLVertexStepFunction : UInt {     case constant     case perVertex     case perInstance     case perPatch     case perPatchControlPoint } ``` |

Modified [MTLVertexStepFunction.constant](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/constant)

|  | Declaration |
| --- | --- |
| From | ``` case Constant ``` |
| To | ``` case constant ``` |

Modified [MTLVertexStepFunction.perInstance](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/perinstance)

|  | Declaration |
| --- | --- |
| From | ``` case PerInstance ``` |
| To | ``` case perInstance ``` |

Modified [MTLVertexStepFunction.perVertex](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/mtlvertexstepfunctionpervertex)

|  | Declaration |
| --- | --- |
| From | ``` case PerVertex ``` |
| To | ``` case perVertex ``` |

Modified [MTLVisibilityResultMode [enum]](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLVisibilityResultMode : UInt {     case Disabled     case Boolean     case Counting } ``` |
| To | ``` enum MTLVisibilityResultMode : UInt {     case disabled     case boolean     case counting } ``` |

Modified [MTLVisibilityResultMode.boolean](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/mtlvisibilityresultmodeboolean)

|  | Declaration |
| --- | --- |
| From | ``` case Boolean ``` |
| To | ``` case boolean ``` |

Modified [MTLVisibilityResultMode.counting](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/counting)

|  | Declaration |
| --- | --- |
| From | ``` case Counting ``` |
| To | ``` case counting ``` |

Modified [MTLVisibilityResultMode.disabled](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode/disabled)

|  | Declaration |
| --- | --- |
| From | ``` case Disabled ``` |
| To | ``` case disabled ``` |

Modified [MTLWinding [enum]](https://developer.apple.com/documentation/metal/mtlwinding)

|  | Declaration |
| --- | --- |
| From | ``` enum MTLWinding : UInt {     case Clockwise     case CounterClockwise } ``` |
| To | ``` enum MTLWinding : UInt {     case clockwise     case counterClockwise } ``` |

Modified [MTLWinding.clockwise](https://developer.apple.com/documentation/metal/mtlwinding/mtlwindingclockwise)

|  | Declaration |
| --- | --- |
| From | ``` case Clockwise ``` |
| To | ``` case clockwise ``` |

Modified [MTLWinding.counterClockwise](https://developer.apple.com/documentation/metal/mtlwinding/mtlwindingcounterclockwise)

|  | Declaration |
| --- | --- |
| From | ``` case CounterClockwise ``` |
| To | ``` case counterClockwise ``` |

Modified [MTLCommandBufferHandler](https://developer.apple.com/documentation/metal/mtlcommandbufferhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MTLCommandBufferHandler = (MTLCommandBuffer) -> Void ``` |
| To | ``` typealias MTLCommandBufferHandler = (MTLCommandBuffer) -> Swift.Void ``` |

Modified [MTLNewComputePipelineStateCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewcomputepipelinestatecompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MTLNewComputePipelineStateCompletionHandler = (MTLComputePipelineState?, NSError?) -> Void ``` |
| To | ``` typealias MTLNewComputePipelineStateCompletionHandler = (MTLComputePipelineState?, Error?) -> Swift.Void ``` |

Modified [MTLNewComputePipelineStateWithReflectionCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewcomputepipelinestatewithreflectioncompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MTLNewComputePipelineStateWithReflectionCompletionHandler = (MTLComputePipelineState?, MTLComputePipelineReflection?, NSError?) -> Void ``` |
| To | ``` typealias MTLNewComputePipelineStateWithReflectionCompletionHandler = (MTLComputePipelineState?, MTLComputePipelineReflection?, Error?) -> Swift.Void ``` |

Modified [MTLNewLibraryCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewlibrarycompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MTLNewLibraryCompletionHandler = (MTLLibrary?, NSError?) -> Void ``` |
| To | ``` typealias MTLNewLibraryCompletionHandler = (MTLLibrary?, Error?) -> Swift.Void ``` |

Modified [MTLNewRenderPipelineStateCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatecompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MTLNewRenderPipelineStateCompletionHandler = (MTLRenderPipelineState?, NSError?) -> Void ``` |
| To | ``` typealias MTLNewRenderPipelineStateCompletionHandler = (MTLRenderPipelineState?, Error?) -> Swift.Void ``` |

Modified [MTLNewRenderPipelineStateWithReflectionCompletionHandler](https://developer.apple.com/documentation/metal/mtlnewrenderpipelinestatewithreflectioncompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MTLNewRenderPipelineStateWithReflectionCompletionHandler = (MTLRenderPipelineState?, MTLRenderPipelineReflection?, NSError?) -> Void ``` |
| To | ``` typealias MTLNewRenderPipelineStateWithReflectionCompletionHandler = (MTLRenderPipelineState?, MTLRenderPipelineReflection?, Error?) -> Swift.Void ``` |

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
