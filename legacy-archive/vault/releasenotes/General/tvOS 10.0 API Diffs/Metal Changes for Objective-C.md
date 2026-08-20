---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/Metal.html
archived_at: '2026-07-18T02:57:27.005883Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# Metal Changes for Objective-C

### Metal

#### MTLArgument.h

Added [MTLArgument.arrayLength](https://developer.apple.com/documentation/metal/mtlargument/1649746-arraylength)Added [MTLArgument.isDepthTexture](https://developer.apple.com/documentation/metal/mtlargument/1639934-isdepthtexture)

#### MTLBlitCommandEncoder.h

Added [-[MTLBlitCommandEncoder updateFence:]](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1649359-updatefence)Added [-[MTLBlitCommandEncoder waitForFence:]](https://developer.apple.com/documentation/metal/mtlblitcommandencoder/1649358-waitforfence)

#### MTLBuffer.h

Added [-[MTLBuffer addDebugMarker:range:]](https://developer.apple.com/documentation/metal/mtlbuffer/1779576-adddebugmarker)Added [-[MTLBuffer removeAllDebugMarkers]](https://developer.apple.com/documentation/metal/mtlbuffer/1779577-removealldebugmarkers)

#### MTLCommandBuffer.h

Added [MTLCommandBufferErrorMemoryless](https://developer.apple.com/documentation/metal/mtlcommandbuffererror/mtlcommandbuffererrormemoryless)

#### MTLComputeCommandEncoder.h

Added [-[MTLComputeCommandEncoder setStageInRegion:]](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/2097047-setstageinregion)Added [-[MTLComputeCommandEncoder updateFence:]](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1649789-updatefence)Added [-[MTLComputeCommandEncoder waitForFence:]](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/1649790-waitforfence)

#### MTLComputePipeline.h

Added [MTLComputePipelineDescriptor.stageInputDescriptor](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/2092373-stageinputdescriptor)

#### MTLDevice.h

Removed MTLFeatureSet_TVOS_GPUFamily1_v1Added [-[MTLDevice heapBufferSizeAndAlignWithLength:options:]](https://developer.apple.com/documentation/metal/mtldevice/1649922-heapbuffersizeandalignwithlength)Added [-[MTLDevice heapTextureSizeAndAlignWithDescriptor:]](https://developer.apple.com/documentation/metal/mtldevice/1649927-heaptexturesizeandalignwithdescr)Added [-[MTLDevice newDefaultLibraryWithBundle:error:]](https://developer.apple.com/documentation/metal/mtldevice/2177054-makedefaultlibrary)Added [-[MTLDevice newFence]](https://developer.apple.com/documentation/metal/mtldevice/1649923-makefence)Added [-[MTLDevice newHeapWithDescriptor:]](https://developer.apple.com/documentation/metal/mtldevice/1649928-newheapwithdescriptor)Added [MTLFeatureSet_tvOS_GPUFamily1_v1](https://developer.apple.com/documentation/metal/mtlfeatureset/tvos_gpufamily1_v1)Added [MTLFeatureSet_tvOS_GPUFamily1_v2](https://developer.apple.com/documentation/metal/mtlfeatureset/tvos_gpufamily1_v2)Added [MTLSizeAndAlign](https://developer.apple.com/documentation/metal/mtlsizeandalign)

#### MTLFence.h (Added)

Added [MTLFence](https://developer.apple.com/documentation/metal/mtlfence)Added [MTLFence.device](https://developer.apple.com/documentation/metal/mtlfence/1648532-device)Added [MTLFence.label](https://developer.apple.com/documentation/metal/mtlfence/1648531-label)

#### MTLFunctionConstantValues.h (Added)

Added [MTLFunctionConstantValues](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues)Added [-[MTLFunctionConstantValues reset]](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/1639526-reset)Added [-[MTLFunctionConstantValues setConstantValue:type:atIndex:]](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/1639531-setconstantvalue)Added [-[MTLFunctionConstantValues setConstantValue:type:withName:]](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/1639530-setconstantvalue)Added [-[MTLFunctionConstantValues setConstantValues:type:withRange:]](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/1639527-setconstantvalues)

#### MTLHeap.h (Added)

Added [MTLHeap](https://developer.apple.com/documentation/metal/mtlheap)Added [MTLHeap.cpuCacheMode](https://developer.apple.com/documentation/metal/mtlheap/1771280-cpucachemode)Added [MTLHeap.device](https://developer.apple.com/documentation/metal/mtlheap/1771285-device)Added [MTLHeap.label](https://developer.apple.com/documentation/metal/mtlheap/1771279-label)Added [-[MTLHeap maxAvailableSizeWithAlignment:]](https://developer.apple.com/documentation/metal/mtlheap/1771284-maxavailablesizewithalignment)Added [-[MTLHeap newBufferWithLength:options:]](https://developer.apple.com/documentation/metal/mtlheap/1649571-makebuffer)Added [-[MTLHeap newTextureWithDescriptor:]](https://developer.apple.com/documentation/metal/mtlheap/1649574-maketexture)Added [-[MTLHeap setPurgeableState:]](https://developer.apple.com/documentation/metal/mtlheap/1771281-setpurgeablestate)Added [MTLHeap.size](https://developer.apple.com/documentation/metal/mtlheap/1649569-size)Added [MTLHeap.storageMode](https://developer.apple.com/documentation/metal/mtlheap/1771282-storagemode)Added [MTLHeap.usedSize](https://developer.apple.com/documentation/metal/mtlheap/2097557-usedsize)Added [MTLHeapDescriptor](https://developer.apple.com/documentation/metal/mtlheapdescriptor)Added [MTLHeapDescriptor.cpuCacheMode](https://developer.apple.com/documentation/metal/mtlheapdescriptor/1649573-cpucachemode)Added [MTLHeapDescriptor.size](https://developer.apple.com/documentation/metal/mtlheapdescriptor/1649568-size)Added [MTLHeapDescriptor.storageMode](https://developer.apple.com/documentation/metal/mtlheapdescriptor/1649567-storagemode)

#### MTLLibrary.h

Added [MTLAttribute](https://developer.apple.com/documentation/metal/mtlattribute)Added [MTLAttribute.active](https://developer.apple.com/documentation/metal/mtlattribute/2097160-isactive)Added [MTLAttribute.attributeIndex](https://developer.apple.com/documentation/metal/mtlattribute/2097158-attributeindex)Added [MTLAttribute.attributeType](https://developer.apple.com/documentation/metal/mtlattribute/2097155-attributetype)Added [MTLAttribute.name](https://developer.apple.com/documentation/metal/mtlattribute/2097161-name)Added [MTLAttribute.patchControlPointData](https://developer.apple.com/documentation/metal/mtlattribute/2097156-ispatchcontrolpointdata)Added [MTLAttribute.patchData](https://developer.apple.com/documentation/metal/mtlattribute/2097157-patchdata)Added [MTLFunction.functionConstantsDictionary](https://developer.apple.com/documentation/metal/mtlfunction/2314777-functionconstantsdictionary)Added [MTLFunction.label](https://developer.apple.com/documentation/metal/mtlfunction/1640034-label)Added [MTLFunction.patchControlPointCount](https://developer.apple.com/documentation/metal/mtlfunction/1639890-patchcontrolpointcount)Added [MTLFunction.patchType](https://developer.apple.com/documentation/metal/mtlfunction/1639909-patchtype)Added [MTLFunction.stageInputAttributes](https://developer.apple.com/documentation/metal/mtlfunction/2097159-stageinputattributes)Added [MTLFunctionConstant](https://developer.apple.com/documentation/metal/mtlfunctionconstant)Added [MTLFunctionConstant.index](https://developer.apple.com/documentation/metal/mtlfunctionconstant/1639905-index)Added [MTLFunctionConstant.name](https://developer.apple.com/documentation/metal/mtlfunctionconstant/1639955-name)Added [MTLFunctionConstant.required](https://developer.apple.com/documentation/metal/mtlfunctionconstant/1639988-required)Added [MTLFunctionConstant.type](https://developer.apple.com/documentation/metal/mtlfunctionconstant/1639950-type)Added [-[MTLLibrary newFunctionWithName:constantValues:completionHandler:]](https://developer.apple.com/documentation/metal/mtllibrary/1640053-makefunction)Added [-[MTLLibrary newFunctionWithName:constantValues:error:]](https://developer.apple.com/documentation/metal/mtllibrary/1640020-newfunctionwithname)Added [MTLVertexAttribute.patchControlPointData](https://developer.apple.com/documentation/metal/mtlvertexattribute/1640013-ispatchcontrolpointdata)Added [MTLVertexAttribute.patchData](https://developer.apple.com/documentation/metal/mtlvertexattribute/1640002-patchdata)Added [MTLLanguageVersion1_2](https://developer.apple.com/documentation/metal/mtllanguageversion/version1_2)Added [MTLLibraryErrorFileNotFound](https://developer.apple.com/documentation/metal/mtllibraryerror/code/filenotfound)Added [MTLLibraryErrorFunctionNotFound](https://developer.apple.com/documentation/metal/mtllibraryerror/code/functionnotfound)Added [MTLPatchType](https://developer.apple.com/documentation/metal/mtlpatchtype)Added [MTLPatchTypeNone](https://developer.apple.com/documentation/metal/mtlpatchtype/none)Added [MTLPatchTypeQuad](https://developer.apple.com/documentation/metal/mtlpatchtype/quad)Added [MTLPatchTypeTriangle](https://developer.apple.com/documentation/metal/mtlpatchtype/triangle)

#### MTLParallelRenderCommandEncoder.h

Added [-[MTLParallelRenderCommandEncoder setColorStoreAction:atIndex:]](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/1639891-setcolorstoreaction)Added [-[MTLParallelRenderCommandEncoder setDepthStoreAction:]](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/1639937-setdepthstoreaction)Added [-[MTLParallelRenderCommandEncoder setStencilStoreAction:]](https://developer.apple.com/documentation/metal/mtlparallelrendercommandencoder/1640016-setstencilstoreaction)

#### MTLPixelFormat.h

Added [MTLPixelFormatBGR10_XR](https://developer.apple.com/documentation/metal/mtlpixelformat/mtlpixelformatbgr10_xr)Added [MTLPixelFormatBGR10_XR_sRGB](https://developer.apple.com/documentation/metal/mtlpixelformat/bgr10_xr_srgb)Added [MTLPixelFormatBGRA10_XR](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra10_xr)Added [MTLPixelFormatBGRA10_XR_sRGB](https://developer.apple.com/documentation/metal/mtlpixelformat/bgra10_xr_srgb)Added [MTLPixelFormatX32_Stencil8](https://developer.apple.com/documentation/metal/mtlpixelformat/x32_stencil8)

#### MTLRenderCommandEncoder.h

Removed [-[MTLRenderCommandEncoder setDepthClipMode:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1516267-setdepthclipmode)Added [-[MTLRenderCommandEncoder drawIndexedPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:instanceCount:baseInstance:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1640031-drawindexedpatches)Added [-[MTLRenderCommandEncoder drawPatches:patchStart:patchCount:patchIndexBuffer:patchIndexBufferOffset:instanceCount:baseInstance:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1639984-drawpatches)Added [-[MTLRenderCommandEncoder setColorStoreAction:atIndex:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1640054-setcolorstoreaction)Added [-[MTLRenderCommandEncoder setDepthStoreAction:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1640036-setdepthstoreaction)Added [-[MTLRenderCommandEncoder setStencilStoreAction:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1639936-setstencilstoreaction)Added [-[MTLRenderCommandEncoder setTessellationFactorBuffer:offset:instanceStride:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1640035-settessellationfactorbuffer)Added [-[MTLRenderCommandEncoder setTessellationFactorScale:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1639992-settessellationfactorscale)Added [-[MTLRenderCommandEncoder updateFence:afterStages:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1648377-updatefence)Added [-[MTLRenderCommandEncoder waitForFence:beforeStages:]](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/1648378-waitforfence)Added [MTLDrawPatchIndirectArguments](https://developer.apple.com/documentation/metal/mtldrawpatchindirectarguments)Added [MTLQuadTessellationFactorsHalf](https://developer.apple.com/documentation/metal/mtlquadtessellationfactorshalf)Added [MTLRenderStageFragment](https://developer.apple.com/documentation/metal/mtlrenderstages/mtlrenderstagefragment)Added [MTLRenderStages](https://developer.apple.com/documentation/metal/mtlrenderstages)Added [MTLRenderStageVertex](https://developer.apple.com/documentation/metal/mtlrenderstages/mtlrenderstagevertex)Added [MTLTriangleTessellationFactorsHalf](https://developer.apple.com/documentation/metal/mtltriangletessellationfactorshalf)Modified [MTLIndexType](https://developer.apple.com/documentation/metal/mtlindextype)

|  | Header |
| --- | --- |
| From | Metal/MTLRenderCommandEncoder.h |
| To | Metal/MTLStageInputOutputDescriptor.h |

Modified [MTLIndexTypeUInt16](https://developer.apple.com/documentation/metal/mtlindextype/uint16)

|  | Header |
| --- | --- |
| From | Metal/MTLRenderCommandEncoder.h |
| To | Metal/MTLStageInputOutputDescriptor.h |

Modified [MTLIndexTypeUInt32](https://developer.apple.com/documentation/metal/mtlindextype/uint32)

|  | Header |
| --- | --- |
| From | Metal/MTLRenderCommandEncoder.h |
| To | Metal/MTLStageInputOutputDescriptor.h |

#### MTLRenderPass.h

Added [MTLStoreActionStoreAndMultisampleResolve](https://developer.apple.com/documentation/metal/mtlstoreaction/storeandmultisampleresolve)Added [MTLStoreActionUnknown](https://developer.apple.com/documentation/metal/mtlstoreaction/mtlstoreactionunknown)

#### MTLRenderPipeline.h

Added [MTLRenderPipelineDescriptor.maxTessellationFactor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1640060-maxtessellationfactor)Added [MTLRenderPipelineDescriptor.tessellationControlPointIndexType](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1640059-tessellationcontrolpointindextyp)Added [MTLRenderPipelineDescriptor.tessellationFactorFormat](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1639951-tessellationfactorformat)Added [MTLRenderPipelineDescriptor.tessellationFactorScaleEnabled](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1640045-istessellationfactorscaleenabled)Added [MTLRenderPipelineDescriptor.tessellationFactorStepFunction](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1640062-tessellationfactorstepfunction)Added [MTLRenderPipelineDescriptor.tessellationOutputWindingOrder](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1639911-tessellationoutputwindingorder)Added [MTLRenderPipelineDescriptor.tessellationPartitionMode](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/1639979-tessellationpartitionmode)Added [MTLPrimitiveTopologyClass](https://developer.apple.com/documentation/metal/mtlprimitivetopologyclass)Added [MTLTessellationControlPointIndexType](https://developer.apple.com/documentation/metal/mtltessellationcontrolpointindextype)Added [MTLTessellationControlPointIndexTypeNone](https://developer.apple.com/documentation/metal/mtltessellationcontrolpointindextype/mtltessellationcontrolpointindextypenone)Added [MTLTessellationControlPointIndexTypeUInt16](https://developer.apple.com/documentation/metal/mtltessellationcontrolpointindextype/mtltessellationcontrolpointindextypeuint16)Added [MTLTessellationControlPointIndexTypeUInt32](https://developer.apple.com/documentation/metal/mtltessellationcontrolpointindextype/uint32)Added [MTLTessellationFactorFormat](https://developer.apple.com/documentation/metal/mtltessellationfactorformat)Added [MTLTessellationFactorFormatHalf](https://developer.apple.com/documentation/metal/mtltessellationfactorformat/half)Added [MTLTessellationFactorStepFunction](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction)Added [MTLTessellationFactorStepFunctionConstant](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/constant)Added [MTLTessellationFactorStepFunctionPerInstance](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/mtltessellationfactorstepfunctionperinstance)Added [MTLTessellationFactorStepFunctionPerPatch](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/perpatch)Added [MTLTessellationFactorStepFunctionPerPatchAndPerInstance](https://developer.apple.com/documentation/metal/mtltessellationfactorstepfunction/perpatchandperinstance)Added [MTLTessellationPartitionMode](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode)Added [MTLTessellationPartitionModeFractionalEven](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode/mtltessellationpartitionmodefractionaleven)Added [MTLTessellationPartitionModeFractionalOdd](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode/mtltessellationpartitionmodefractionalodd)Added [MTLTessellationPartitionModeInteger](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode/integer)Added [MTLTessellationPartitionModePow2](https://developer.apple.com/documentation/metal/mtltessellationpartitionmode/pow2)

#### MTLResource.h

Added [MTLResource.heap](https://developer.apple.com/documentation/metal/mtlresource/1682333-heap)Added [-[MTLResource isAliasable]](https://developer.apple.com/documentation/metal/mtlresource/1771702-isaliasable)Added [-[MTLResource makeAliasable]](https://developer.apple.com/documentation/metal/mtlresource/1771705-makealiasable)Added [MTLResourceHazardTrackingModeUntracked](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcehazardtrackingmodeuntracked)Added [MTLResourceStorageModeMemoryless](https://developer.apple.com/documentation/metal/mtlresourceoptions/mtlresourcestoragemodememoryless)Added [MTLStorageModeMemoryless](https://developer.apple.com/documentation/metal/mtlstoragemode/memoryless)

#### MTLSampler.h

Added [MTLSamplerBorderColor](https://developer.apple.com/documentation/metal/mtlsamplerbordercolor)Added [MTLSamplerBorderColorOpaqueBlack](https://developer.apple.com/documentation/metal/mtlsamplerbordercolor/mtlsamplerbordercoloropaqueblack)Added [MTLSamplerBorderColorOpaqueWhite](https://developer.apple.com/documentation/metal/mtlsamplerbordercolor/mtlsamplerbordercoloropaquewhite)Added [MTLSamplerBorderColorTransparentBlack](https://developer.apple.com/documentation/metal/mtlsamplerbordercolor/mtlsamplerbordercolortransparentblack)

#### MTLStageInputOutputDescriptor.h (Added)

Added [MTLAttributeDescriptor](https://developer.apple.com/documentation/metal/mtlattributedescriptor)Added [MTLAttributeDescriptor.bufferIndex](https://developer.apple.com/documentation/metal/mtlattributedescriptor/2097218-bufferindex)Added [MTLAttributeDescriptor.format](https://developer.apple.com/documentation/metal/mtlattributedescriptor/2097194-format)Added [MTLAttributeDescriptor.offset](https://developer.apple.com/documentation/metal/mtlattributedescriptor/2097220-offset)Added [MTLAttributeDescriptorArray](https://developer.apple.com/documentation/metal/mtlattributedescriptorarray)Added [-[MTLAttributeDescriptorArray objectAtIndexedSubscript:]](https://developer.apple.com/documentation/metal/mtlattributedescriptorarray/2097215-objectatindexedsubscript)Added [-[MTLAttributeDescriptorArray setObject:atIndexedSubscript:]](https://developer.apple.com/documentation/metal/mtlattributedescriptorarray/2097293-setobject)Added [MTLBufferLayoutDescriptor](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor)Added [MTLBufferLayoutDescriptor.stepFunction](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/2097182-stepfunction)Added [MTLBufferLayoutDescriptor.stepRate](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/2097164-steprate)Added [MTLBufferLayoutDescriptor.stride](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptor/2097190-stride)Added [MTLBufferLayoutDescriptorArray](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptorarray)Added [-[MTLBufferLayoutDescriptorArray objectAtIndexedSubscript:]](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptorarray/2097228-objectatindexedsubscript)Added [-[MTLBufferLayoutDescriptorArray setObject:atIndexedSubscript:]](https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptorarray/2097295-setobject)Added [MTLStageInputOutputDescriptor](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor)Added [MTLStageInputOutputDescriptor.attributes](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097206-attributes)Added [MTLStageInputOutputDescriptor.indexBufferIndex](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097237-indexbufferindex)Added [MTLStageInputOutputDescriptor.indexType](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097184-indextype)Added [MTLStageInputOutputDescriptor.layouts](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097202-layouts)Added [-[MTLStageInputOutputDescriptor reset]](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097185-reset)Added [+[MTLStageInputOutputDescriptor stageInputOutputDescriptor]](https://developer.apple.com/documentation/metal/mtlstageinputoutputdescriptor/2097294-stageinputoutputdescriptor)Added [MTLAttributeFormat](https://developer.apple.com/documentation/metal/mtlattributeformat)Added [MTLAttributeFormatChar2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatchar2)Added [MTLAttributeFormatChar2Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatchar2normalized)Added [MTLAttributeFormatChar3](https://developer.apple.com/documentation/metal/mtlattributeformat/char3)Added [MTLAttributeFormatChar3Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatchar3normalized)Added [MTLAttributeFormatChar4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatchar4)Added [MTLAttributeFormatChar4Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatchar4normalized)Added [MTLAttributeFormatFloat](https://developer.apple.com/documentation/metal/mtlattributeformat/float)Added [MTLAttributeFormatFloat2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatfloat2)Added [MTLAttributeFormatFloat3](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatfloat3)Added [MTLAttributeFormatFloat4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatfloat4)Added [MTLAttributeFormatHalf2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformathalf2)Added [MTLAttributeFormatHalf3](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformathalf3)Added [MTLAttributeFormatHalf4](https://developer.apple.com/documentation/metal/mtlattributeformat/half4)Added [MTLAttributeFormatInt](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatint)Added [MTLAttributeFormatInt1010102Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatint1010102normalized)Added [MTLAttributeFormatInt2](https://developer.apple.com/documentation/metal/mtlattributeformat/int2)Added [MTLAttributeFormatInt3](https://developer.apple.com/documentation/metal/mtlattributeformat/int3)Added [MTLAttributeFormatInt4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatint4)Added [MTLAttributeFormatInvalid](https://developer.apple.com/documentation/metal/mtlattributeformat/invalid)Added [MTLAttributeFormatShort2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatshort2)Added [MTLAttributeFormatShort2Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/short2normalized)Added [MTLAttributeFormatShort3](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatshort3)Added [MTLAttributeFormatShort3Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatshort3normalized)Added [MTLAttributeFormatShort4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatshort4)Added [MTLAttributeFormatShort4Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/short4normalized)Added [MTLAttributeFormatUChar2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuchar2)Added [MTLAttributeFormatUChar2Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/uchar2normalized)Added [MTLAttributeFormatUChar3](https://developer.apple.com/documentation/metal/mtlattributeformat/uchar3)Added [MTLAttributeFormatUChar3Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/uchar3normalized)Added [MTLAttributeFormatUChar4](https://developer.apple.com/documentation/metal/mtlattributeformat/uchar4)Added [MTLAttributeFormatUChar4Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuchar4normalized)Added [MTLAttributeFormatUInt](https://developer.apple.com/documentation/metal/mtlattributeformat/uint)Added [MTLAttributeFormatUInt1010102Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuint1010102normalized)Added [MTLAttributeFormatUInt2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuint2)Added [MTLAttributeFormatUInt3](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuint3)Added [MTLAttributeFormatUInt4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatuint4)Added [MTLAttributeFormatUShort2](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatushort2)Added [MTLAttributeFormatUShort2Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatushort2normalized)Added [MTLAttributeFormatUShort3](https://developer.apple.com/documentation/metal/mtlattributeformat/ushort3)Added [MTLAttributeFormatUShort3Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/ushort3normalized)Added [MTLAttributeFormatUShort4](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatushort4)Added [MTLAttributeFormatUShort4Normalized](https://developer.apple.com/documentation/metal/mtlattributeformat/mtlattributeformatushort4normalized)Added [MTLStepFunction](https://developer.apple.com/documentation/metal/mtlstepfunction)Added [MTLStepFunctionConstant](https://developer.apple.com/documentation/metal/mtlstepfunction/mtlstepfunctionconstant)Added [MTLStepFunctionPerInstance](https://developer.apple.com/documentation/metal/mtlstepfunction/perinstance)Added [MTLStepFunctionPerPatch](https://developer.apple.com/documentation/metal/mtlstepfunction/mtlstepfunctionperpatch)Added [MTLStepFunctionPerPatchControlPoint](https://developer.apple.com/documentation/metal/mtlstepfunction/mtlstepfunctionperpatchcontrolpoint)Added [MTLStepFunctionPerVertex](https://developer.apple.com/documentation/metal/mtlstepfunction/pervertex)Added [MTLStepFunctionThreadPositionInGridX](https://developer.apple.com/documentation/metal/mtlstepfunction/threadpositioningridx)Added [MTLStepFunctionThreadPositionInGridXIndexed](https://developer.apple.com/documentation/metal/mtlstepfunction/threadpositioningridxindexed)Added [MTLStepFunctionThreadPositionInGridY](https://developer.apple.com/documentation/metal/mtlstepfunction/mtlstepfunctionthreadpositioningridy)Added [MTLStepFunctionThreadPositionInGridYIndexed](https://developer.apple.com/documentation/metal/mtlstepfunction/mtlstepfunctionthreadpositioningridyindexed)Modified [MTLIndexType](https://developer.apple.com/documentation/metal/mtlindextype)

|  | Header |
| --- | --- |
| From | Metal/MTLRenderCommandEncoder.h |
| To | Metal/MTLStageInputOutputDescriptor.h |

Modified [MTLIndexTypeUInt16](https://developer.apple.com/documentation/metal/mtlindextype/uint16)

|  | Header |
| --- | --- |
| From | Metal/MTLRenderCommandEncoder.h |
| To | Metal/MTLStageInputOutputDescriptor.h |

Modified [MTLIndexTypeUInt32](https://developer.apple.com/documentation/metal/mtlindextype/uint32)

|  | Header |
| --- | --- |
| From | Metal/MTLRenderCommandEncoder.h |
| To | Metal/MTLStageInputOutputDescriptor.h |

#### MTLTexture.h

Modified [MTLTexture.rootResource](https://developer.apple.com/documentation/metal/mtltexture/1515579-rootresource)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 10.0 |

#### MTLVertexDescriptor.h

Added [MTLVertexStepFunctionPerPatch](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/mtlvertexstepfunctionperpatch)Added [MTLVertexStepFunctionPerPatchControlPoint](https://developer.apple.com/documentation/metal/mtlvertexstepfunction/mtlvertexstepfunctionperpatchcontrolpoint)

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
