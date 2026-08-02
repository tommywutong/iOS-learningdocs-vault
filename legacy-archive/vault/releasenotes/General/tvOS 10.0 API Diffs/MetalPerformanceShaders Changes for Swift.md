---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/MetalPerformanceShaders.html
archived_at: '2026-07-18T02:57:52.343974Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# MetalPerformanceShaders Changes for Swift

### MetalPerformanceShaders

Removed [MPSKernelOptions.none](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/mpskerneloptionsnone)Added [MPSAlphaType [enum]](https://developer.apple.com/documentation/metalperformanceshaders/mpsalphatype)Added [MPSAlphaType.alphaIsOne](https://developer.apple.com/documentation/metalperformanceshaders/mpsalphatype/alphaisone)Added [MPSAlphaType.nonPremultiplied](https://developer.apple.com/documentation/metalperformanceshaders/mpsalphatype/mpsalphatypenonpremultiplied)Added [MPSAlphaType.premultiplied](https://developer.apple.com/documentation/metalperformanceshaders/mpsalphatype/mpsalphatypepremultiplied)Added [MPSCNNConvolution](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution)Added [MPSCNNConvolution.groups](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution/1845269-groups)Added [MPSCNNConvolution.init(device: MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution/1648861-initwithdevice)Added [MPSCNNConvolution.inputFeatureChannels](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution/1845268-inputfeaturechannels)Added MPSCNNConvolution.kernelHeightAdded MPSCNNConvolution.kernelWidthAdded [MPSCNNConvolution.neuron](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution/1845274-neuron)Added [MPSCNNConvolution.outputFeatureChannels](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolution/1845271-outputfeaturechannels)Added MPSCNNConvolution.strideInPixelsXAdded MPSCNNConvolution.strideInPixelsYAdded [MPSCNNConvolutionDescriptor](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor)Added [MPSCNNConvolutionDescriptor.groups](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1648849-groups)Added [MPSCNNConvolutionDescriptor.init(kernelWidth: Int, kernelHeight: Int, inputFeatureChannels: Int, outputFeatureChannels: Int, neuronFilter: MPSCNNNeuron?)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1648876-init)Added [MPSCNNConvolutionDescriptor.inputFeatureChannels](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1648934-inputfeaturechannels)Added [MPSCNNConvolutionDescriptor.kernelHeight](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1648904-kernelheight)Added [MPSCNNConvolutionDescriptor.kernelWidth](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1648959-kernelwidth)Added [MPSCNNConvolutionDescriptor.neuron](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1829442-neuron)Added [MPSCNNConvolutionDescriptor.outputFeatureChannels](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1648852-outputfeaturechannels)Added [MPSCNNConvolutionDescriptor.strideInPixelsX](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1648908-strideinpixelsx)Added [MPSCNNConvolutionDescriptor.strideInPixelsY](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutiondescriptor/1648847-strideinpixelsy)Added [MPSCNNConvolutionFlags [enum]](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutionflags)Added [MPSCNNConvolutionFlags.none](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnconvolutionflags/none)Added [MPSCNNCrossChannelNormalization](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalization)Added [MPSCNNCrossChannelNormalization.alpha](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalization/1648896-alpha)Added [MPSCNNCrossChannelNormalization.beta](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalization/1648879-beta)Added [MPSCNNCrossChannelNormalization.delta](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalization/1648881-delta)Added [MPSCNNCrossChannelNormalization.init(device: MTLDevice, kernelSize: Int)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalization/1648834-initwithdevice)Added [MPSCNNCrossChannelNormalization.kernelSize](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalization/1648811-kernelsize)Added [MPSCNNFullyConnected](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnected)Added [MPSCNNFullyConnected.init(device: MTLDevice, convolutionDescriptor: MPSCNNConvolutionDescriptor, kernelWeights: UnsafePointer<Float>, biasTerms: UnsafePointer<Float>?, flags: MPSCNNConvolutionFlags)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnected/1829441-initwithdevice)Added [MPSCNNKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel)Added [MPSCNNKernel.clipRect](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/1648911-cliprect)Added [MPSCNNKernel.destinationFeatureChannelOffset](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/2097550-destinationfeaturechanneloffset)Added [MPSCNNKernel.edgeMode](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/1648826-edgemode)Added [MPSCNNKernel.encode(commandBuffer: MTLCommandBuffer, sourceImage: MPSImage, destinationImage: MPSImage)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/1648919-encodetocommandbuffer)Added [MPSCNNKernel.offset](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/1648835-offset)Added MPSCNNKernel.sourceRegion(destinationSize: MTLSize) -> MPSRegionAdded [MPSCNNLocalContrastNormalization](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalization)Added [MPSCNNLocalContrastNormalization.alpha](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalization/1648923-alpha)Added [MPSCNNLocalContrastNormalization.beta](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalization/1648905-beta)Added [MPSCNNLocalContrastNormalization.delta](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalization/1648812-delta)Added [MPSCNNLocalContrastNormalization.init(device: MTLDevice, kernelWidth: Int, kernelHeight: Int)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalization/1648924-initwithdevice)Added MPSCNNLocalContrastNormalization.kernelHeightAdded MPSCNNLocalContrastNormalization.kernelWidthAdded [MPSCNNLocalContrastNormalization.p0](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalization/1648953-p0)Added [MPSCNNLocalContrastNormalization.pm](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalization/1648907-pm)Added [MPSCNNLocalContrastNormalization.ps](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlocalcontrastnormalization/1648942-ps)Added [MPSCNNLogSoftMax](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlogsoftmax)Added [MPSCNNNeuron](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuron)Added [MPSCNNNeuronAbsolute](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronabsolute)Added [MPSCNNNeuronAbsolute.init(device: MTLDevice)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronabsolute/1648809-initwithdevice)Added [MPSCNNNeuronLinear](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronlinear)Added MPSCNNNeuronLinear.aAdded MPSCNNNeuronLinear.bAdded [MPSCNNNeuronLinear.init(device: MTLDevice, a: Float, b: Float)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronlinear/1648888-init)Added [MPSCNNNeuronReLU](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronrelu)Added MPSCNNNeuronReLU.aAdded [MPSCNNNeuronReLU.init(device: MTLDevice, a: Float)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronrelu/1648926-init)Added [MPSCNNNeuronSigmoid](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronsigmoid)Added [MPSCNNNeuronSigmoid.init(device: MTLDevice)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneuronsigmoid/1648890-init)Added [MPSCNNNeuronTanH](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneurontanh)Added MPSCNNNeuronTanH.aAdded MPSCNNNeuronTanH.bAdded [MPSCNNNeuronTanH.init(device: MTLDevice, a: Float, b: Float)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnneurontanh/1648815-init)Added [MPSCNNPooling](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpooling)Added [MPSCNNPooling.init(device: MTLDevice, kernelWidth: Int, kernelHeight: Int)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpooling/1648887-initwithdevice)Added [MPSCNNPooling.init(device: MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpooling/1648902-init)Added MPSCNNPooling.kernelHeightAdded MPSCNNPooling.kernelWidthAdded MPSCNNPooling.strideInPixelsXAdded MPSCNNPooling.strideInPixelsYAdded [MPSCNNPoolingAverage](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingaverage)Added [MPSCNNPoolingMax](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingmax)Added [MPSCNNSoftMax](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnsoftmax)Added [MPSCNNSpatialNormalization](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnspatialnormalization)Added [MPSCNNSpatialNormalization.alpha](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnspatialnormalization/1648825-alpha)Added [MPSCNNSpatialNormalization.beta](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnspatialnormalization/1648936-beta)Added [MPSCNNSpatialNormalization.delta](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnspatialnormalization/1648933-delta)Added [MPSCNNSpatialNormalization.init(device: MTLDevice, kernelWidth: Int, kernelHeight: Int)](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnspatialnormalization/1648831-init)Added MPSCNNSpatialNormalization.kernelHeightAdded MPSCNNSpatialNormalization.kernelWidthAdded [MPSDataType [enum]](https://developer.apple.com/documentation/metalperformanceshaders/mpsdatatype)Added [MPSDataType.float32](https://developer.apple.com/documentation/metalperformanceshaders/mpsdatatype/mpsdatatypefloat32)Added [MPSDataType.floatBit](https://developer.apple.com/documentation/metalperformanceshaders/mpsdatatype/mpsdatatypefloatbit)Added [MPSImage](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage)Added [MPSImage.device](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648857-device)Added [MPSImage.featureChannels](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648901-featurechannels)Added [MPSImage.height](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648952-height)Added [MPSImage.init(device: MTLDevice, imageDescriptor: MPSImageDescriptor)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648920-initwithdevice)Added [MPSImage.init(texture: MTLTexture, featureChannels: Int)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/2097547-init)Added [MPSImage.label](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648899-label)Added [MPSImage.numberOfImages](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648900-numberofimages)Added [MPSImage.pixelFormat](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648844-pixelformat)Added [MPSImage.pixelSize](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648854-pixelsize)Added [MPSImage.precision](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648880-precision)Added [MPSImage.setPurgeableState(_: MPSPurgeableState) -> MPSPurgeableState](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648820-setpurgeablestate)Added [MPSImage.texture](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648903-texture)Added [MPSImage.textureType](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648948-texturetype)Added [MPSImage.usage](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648828-usage)Added [MPSImage.width](https://developer.apple.com/documentation/metalperformanceshaders/mpsimage/1648884-width)Added [MPSImageConversion](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconversion)Added [MPSImageConversion.destinationAlpha](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconversion/1648515-destinationalpha)Added [MPSImageConversion.init(device: MTLDevice, srcAlpha: MPSAlphaType, destAlpha: MPSAlphaType, backgroundColor: UnsafeMutablePointer<CGFloat>?, conversionInfo: CGColorConversionInfo?)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconversion/2206722-initwithdevice)Added [MPSImageConversion.sourceAlpha](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconversion/1648518-sourcealpha)Added [MPSImageDescriptor](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor)Added [MPSImageDescriptor.channelFormat](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648818-channelformat)Added [MPSImageDescriptor.cpuCacheMode](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648930-cpucachemode)Added [MPSImageDescriptor.featureChannels](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648918-featurechannels)Added [MPSImageDescriptor.height](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648947-height)Added [MPSImageDescriptor.init(channelFormat: MPSImageFeatureChannelFormat, width: Int, height: Int, featureChannels: Int)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648819-init)Added [MPSImageDescriptor.init(channelFormat: MPSImageFeatureChannelFormat, width: Int, height: Int, featureChannels: Int, numberOfImages: Int, usage: MTLTextureUsage)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648893-init)Added [MPSImageDescriptor.numberOfImages](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648846-numberofimages)Added [MPSImageDescriptor.pixelFormat](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648913-pixelformat)Added [MPSImageDescriptor.storageMode](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648955-storagemode)Added [MPSImageDescriptor.usage](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648937-usage)Added [MPSImageDescriptor.width](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedescriptor/1648830-width)Added [MPSImageFeatureChannelFormat [enum]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefeaturechannelformat)Added [MPSImageFeatureChannelFormat.float16](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefeaturechannelformat/mpsimagefeaturechannelformatfloat16)Added [MPSImageFeatureChannelFormat.float32](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefeaturechannelformat/float32)Added MPSImageFeatureChannelFormat.invalidAdded [MPSImageFeatureChannelFormat.unorm16](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefeaturechannelformat/unorm16)Added [MPSImageFeatureChannelFormat.unorm8](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagefeaturechannelformat/unorm8)Added [MPSImageGaussianPyramid](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagegaussianpyramid)Added [MPSImageLaplacian](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagelaplacian)Added [MPSImageLaplacian.bias](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagelaplacian/1648929-bias)Added [MPSImagePyramid](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagepyramid)Added [MPSImagePyramid.init(device: MTLDevice)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagepyramid/1648935-init)Added [MPSImagePyramid.init(device: MTLDevice, centerWeight: Float)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagepyramid/1648889-init)Added [MPSImagePyramid.init(device: MTLDevice, kernelWidth: Int, kernelHeight: Int, weights: UnsafePointer<Float>)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagepyramid/1648821-init)Added [MPSImagePyramid.kernelHeight](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagepyramid/1648863-kernelheight)Added [MPSImagePyramid.kernelWidth](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagepyramid/1648842-kernelwidth)Added [MPSKernelOptions.disableInternalTiling](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/1648950-disableinternaltiling)Added [MPSKernelOptions.insertDebugGroups](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/mpskerneloptionsinsertdebuggroups)Added [MPSMatrix](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix)Added [MPSMatrix.columns](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix/2143207-columns)Added [MPSMatrix.data](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix/2143205-data)Added [MPSMatrix.dataType](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix/2143197-datatype)Added [MPSMatrix.device](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix/2143209-device)Added [MPSMatrix.init(buffer: MTLBuffer, descriptor: MPSMatrixDescriptor)](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix/2143201-init)Added [MPSMatrix.rowBytes](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix/2143208-rowbytes)Added [MPSMatrix.rows](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrix/2143210-rows)Added [MPSMatrixDescriptor](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor)Added [MPSMatrixDescriptor.columns](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/2143196-columns)Added [MPSMatrixDescriptor.dataType](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/2143202-datatype)Added [MPSMatrixDescriptor.init(dimensions: Int, columns: Int, rowBytes: Int, dataType: MPSDataType)](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/2143206-init)Added [MPSMatrixDescriptor.rowBytes](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/2143199-rowbytes)Added [MPSMatrixDescriptor.rowBytes(fromColumns: Int, dataType: MPSDataType) -> Int [class]](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/2143204-rowbytesfromcolumns)Added [MPSMatrixDescriptor.rows](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/2143203-rows)Added [MPSMatrixMultiplication](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication)Added [MPSMatrixMultiplication.encode(commandBuffer: MTLCommandBuffer, leftMatrix: MPSMatrix, rightMatrix: MPSMatrix, resultMatrix: MPSMatrix)](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication/2147848-encodetocommandbuffer)Added [MPSMatrixMultiplication.init(device: MTLDevice, transposeLeft: Bool, transposeRight: Bool, resultRows: Int, resultColumns: Int, interiorColumns: Int, alpha: Double, beta: Double)](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication/2147845-initwithdevice)Added [MPSMatrixMultiplication.leftMatrixOrigin](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication/2147846-leftmatrixorigin)Added [MPSMatrixMultiplication.resultMatrixOrigin](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication/2147847-resultmatrixorigin)Added [MPSMatrixMultiplication.rightMatrixOrigin](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixmultiplication/2147851-rightmatrixorigin)Added [MPSPurgeableState [enum]](https://developer.apple.com/documentation/metalperformanceshaders/mpspurgeablestate)Added [MPSPurgeableState.allocationDeferred](https://developer.apple.com/documentation/metalperformanceshaders/mpspurgeablestate/mpspurgeablestateallocationdeferred)Added [MPSPurgeableState.empty](https://developer.apple.com/documentation/metalperformanceshaders/mpspurgeablestate/mpspurgeablestateempty)Added [MPSPurgeableState.keepCurrent](https://developer.apple.com/documentation/metalperformanceshaders/mpspurgeablestate/mpspurgeablestatekeepcurrent)Added [MPSPurgeableState.nonVolatile](https://developer.apple.com/documentation/metalperformanceshaders/mpspurgeablestate/mpspurgeablestatenonvolatile)Added [MPSPurgeableState.volatile](https://developer.apple.com/documentation/metalperformanceshaders/mpspurgeablestate/mpspurgeablestatevolatile)Added [MPSTemporaryImage](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage)Added [MPSTemporaryImage.init(commandBuffer: MTLCommandBuffer, imageDescriptor: MPSImageDescriptor)](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/2097545-temporaryimagewithcommandbuffer)Added [MPSTemporaryImage.init(commandBuffer: MTLCommandBuffer, textureDescriptor: MTLTextureDescriptor)](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/2097543-temporaryimagewithcommandbuffer)Added [MPSTemporaryImage.prefetchStorage(with: MTLCommandBuffer, imageDescriptorList: [MPSImageDescriptor]) [class]](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/2097544-prefetchstoragewithcommandbuffer)Added [MPSTemporaryImage.readCount](https://developer.apple.com/documentation/metalperformanceshaders/mpstemporaryimage/2097546-readcount)Modified [MPSBinaryImageKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel)

|  | Declaration |
| --- | --- |
| From | ``` class MPSBinaryImageKernel : MPSKernel {     var primaryOffset: MPSOffset     var secondaryOffset: MPSOffset     var primaryEdgeMode: MPSImageEdgeMode     var secondaryEdgeMode: MPSImageEdgeMode     var clipRect: MTLRegion     func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, primaryTexture primaryTexture: MTLTexture, inPlaceSecondaryTexture inPlaceSecondaryTexture: UnsafeMutablePointer<MTLTexture?>, fallbackCopyAllocator copyAllocator: MPSCopyAllocator?) -> Bool     func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, inPlacePrimaryTexture inPlacePrimaryTexture: UnsafeMutablePointer<MTLTexture?>, secondaryTexture secondaryTexture: MTLTexture, fallbackCopyAllocator copyAllocator: MPSCopyAllocator?) -> Bool     func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, primaryTexture primaryTexture: MTLTexture, secondaryTexture secondaryTexture: MTLTexture, destinationTexture destinationTexture: MTLTexture)     func primarySourceRegionForDestinationSize(_ destinationSize: MTLSize) -> MPSRegion     func secondarySourceRegionForDestinationSize(_ destinationSize: MTLSize) -> MPSRegion } ``` |
| To | ``` class MPSBinaryImageKernel : MPSKernel {     var primaryOffset: MPSOffset     var secondaryOffset: MPSOffset     var primaryEdgeMode: MPSImageEdgeMode     var secondaryEdgeMode: MPSImageEdgeMode     var clipRect: MTLRegion     func encode(to commandBuffer: MTLCommandBuffer, primaryTexture primaryTexture: MTLTexture, inPlaceSecondaryTexture inPlaceSecondaryTexture: UnsafeMutablePointer<MTLTexture>, fallbackCopyAllocator copyAllocator: MetalPerformanceShaders.MPSCopyAllocator? = nil) -> Bool     func encode(to commandBuffer: MTLCommandBuffer, inPlacePrimaryTexture inPlacePrimaryTexture: UnsafeMutablePointer<MTLTexture>, secondaryTexture secondaryTexture: MTLTexture, fallbackCopyAllocator copyAllocator: MetalPerformanceShaders.MPSCopyAllocator? = nil) -> Bool     func encode(to commandBuffer: MTLCommandBuffer, primaryTexture primaryTexture: MTLTexture, secondaryTexture secondaryTexture: MTLTexture, destinationTexture destinationTexture: MTLTexture)     func primarySourceRegion(forDestinationSize destinationSize: MTLSize) -> MPSRegion     func secondarySourceRegion(forDestinationSize destinationSize: MTLSize) -> MPSRegion } ``` |

Modified [MPSBinaryImageKernel.encode(to: MTLCommandBuffer, inPlacePrimaryTexture: UnsafeMutablePointer<MTLTexture>, secondaryTexture: MTLTexture, fallbackCopyAllocator: MetalPerformanceShaders.MPSCopyAllocator?) -> Bool](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618771-encodetocommandbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, inPlacePrimaryTexture inPlacePrimaryTexture: UnsafeMutablePointer<MTLTexture?>, secondaryTexture secondaryTexture: MTLTexture, fallbackCopyAllocator copyAllocator: MPSCopyAllocator?) -> Bool ``` |
| To | ``` func encode(to commandBuffer: MTLCommandBuffer, inPlacePrimaryTexture inPlacePrimaryTexture: UnsafeMutablePointer<MTLTexture>, secondaryTexture secondaryTexture: MTLTexture, fallbackCopyAllocator copyAllocator: MetalPerformanceShaders.MPSCopyAllocator? = nil) -> Bool ``` |

Modified [MPSBinaryImageKernel.encode(to: MTLCommandBuffer, primaryTexture: MTLTexture, inPlaceSecondaryTexture: UnsafeMutablePointer<MTLTexture>, fallbackCopyAllocator: MetalPerformanceShaders.MPSCopyAllocator?) -> Bool](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618890-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, primaryTexture primaryTexture: MTLTexture, inPlaceSecondaryTexture inPlaceSecondaryTexture: UnsafeMutablePointer<MTLTexture?>, fallbackCopyAllocator copyAllocator: MPSCopyAllocator?) -> Bool ``` |
| To | ``` func encode(to commandBuffer: MTLCommandBuffer, primaryTexture primaryTexture: MTLTexture, inPlaceSecondaryTexture inPlaceSecondaryTexture: UnsafeMutablePointer<MTLTexture>, fallbackCopyAllocator copyAllocator: MetalPerformanceShaders.MPSCopyAllocator? = nil) -> Bool ``` |

Modified [MPSBinaryImageKernel.encode(to: MTLCommandBuffer, primaryTexture: MTLTexture, secondaryTexture: MTLTexture, destinationTexture: MTLTexture)](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618871-encodetocommandbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, primaryTexture primaryTexture: MTLTexture, secondaryTexture secondaryTexture: MTLTexture, destinationTexture destinationTexture: MTLTexture) ``` |
| To | ``` func encode(to commandBuffer: MTLCommandBuffer, primaryTexture primaryTexture: MTLTexture, secondaryTexture secondaryTexture: MTLTexture, destinationTexture destinationTexture: MTLTexture) ``` |

Modified [MPSBinaryImageKernel.primarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618900-primarysourceregion)

|  | Declaration |
| --- | --- |
| From | ``` func primarySourceRegionForDestinationSize(_ destinationSize: MTLSize) -> MPSRegion ``` |
| To | ``` func primarySourceRegion(forDestinationSize destinationSize: MTLSize) -> MPSRegion ``` |

Modified [MPSBinaryImageKernel.secondarySourceRegion(forDestinationSize: MTLSize) -> MPSRegion](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618838-secondarysourceregionfordestinat)

|  | Declaration |
| --- | --- |
| From | ``` func secondarySourceRegionForDestinationSize(_ destinationSize: MTLSize) -> MPSRegion ``` |
| To | ``` func secondarySourceRegion(forDestinationSize destinationSize: MTLSize) -> MPSRegion ``` |

Modified [MPSImageEdgeMode [enum]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedgemode)

|  | Declaration |
| --- | --- |
| From | ``` enum MPSImageEdgeMode : UInt {     case Zero     case Clamp } ``` |
| To | ``` enum MPSImageEdgeMode : UInt {     case zero     case clamp } ``` |

Modified [MPSImageEdgeMode.clamp](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedgemode/clamp)

|  | Declaration |
| --- | --- |
| From | ``` case Clamp ``` |
| To | ``` case clamp ``` |

Modified [MPSImageEdgeMode.zero](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedgemode/mpsimageedgemodezero)

|  | Declaration |
| --- | --- |
| From | ``` case Zero ``` |
| To | ``` case zero ``` |

Modified [MPSImageHistogram](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram)

|  | Declaration |
| --- | --- |
| From | ``` class MPSImageHistogram : MPSKernel {     var clipRectSource: MTLRegion     var zeroHistogram: Bool     var histogramInfo: MPSImageHistogramInfo { get }     init(device device: MTLDevice, histogramInfo histogramInfo: UnsafePointer<MPSImageHistogramInfo>)     func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, histogram histogram: MTLBuffer, histogramOffset histogramOffset: Int)     func histogramSizeForSourceFormat(_ sourceFormat: MTLPixelFormat) -> Int } ``` |
| To | ``` class MPSImageHistogram : MPSKernel {     var clipRectSource: MTLRegion     var zeroHistogram: Bool     var histogramInfo: MPSImageHistogramInfo { get }     init(device device: MTLDevice, histogramInfo histogramInfo: UnsafePointer<MPSImageHistogramInfo>)     func encode(to commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, histogram histogram: MTLBuffer, histogramOffset histogramOffset: Int)     func histogramSize(forSourceFormat sourceFormat: MTLPixelFormat) -> Int } ``` |

Modified [MPSImageHistogram.encode(to: MTLCommandBuffer, sourceTexture: MTLTexture, histogram: MTLBuffer, histogramOffset: Int)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/1618853-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, histogram histogram: MTLBuffer, histogramOffset histogramOffset: Int) ``` |
| To | ``` func encode(to commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, histogram histogram: MTLBuffer, histogramOffset histogramOffset: Int) ``` |

Modified [MPSImageHistogram.histogramSize(forSourceFormat: MTLPixelFormat) -> Int](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/1618839-histogramsizeforsourceformat)

|  | Declaration |
| --- | --- |
| From | ``` func histogramSizeForSourceFormat(_ sourceFormat: MTLPixelFormat) -> Int ``` |
| To | ``` func histogramSize(forSourceFormat sourceFormat: MTLPixelFormat) -> Int ``` |

Modified [MPSImageHistogramEqualization](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramequalization)

|  | Declaration |
| --- | --- |
| From | ``` class MPSImageHistogramEqualization : MPSUnaryImageKernel {     var histogramInfo: MPSImageHistogramInfo { get }     init(device device: MTLDevice, histogramInfo histogramInfo: UnsafePointer<MPSImageHistogramInfo>)     func encodeTransformToCommandBuffer(_ commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, histogram histogram: MTLBuffer, histogramOffset histogramOffset: Int) } ``` |
| To | ``` class MPSImageHistogramEqualization : MPSUnaryImageKernel {     var histogramInfo: MPSImageHistogramInfo { get }     init(device device: MTLDevice, histogramInfo histogramInfo: UnsafePointer<MPSImageHistogramInfo>)     func encodeTransform(to commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, histogram histogram: MTLBuffer, histogramOffset histogramOffset: Int) } ``` |

Modified [MPSImageHistogramEqualization.encodeTransform(to: MTLCommandBuffer, sourceTexture: MTLTexture, histogram: MTLBuffer, histogramOffset: Int)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramequalization/1618746-encodetransform)

|  | Declaration |
| --- | --- |
| From | ``` func encodeTransformToCommandBuffer(_ commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, histogram histogram: MTLBuffer, histogramOffset histogramOffset: Int) ``` |
| To | ``` func encodeTransform(to commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, histogram histogram: MTLBuffer, histogramOffset histogramOffset: Int) ``` |

Modified [MPSImageHistogramSpecification](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramspecification)

|  | Declaration |
| --- | --- |
| From | ``` class MPSImageHistogramSpecification : MPSUnaryImageKernel {     var histogramInfo: MPSImageHistogramInfo { get }     init(device device: MTLDevice, histogramInfo histogramInfo: UnsafePointer<MPSImageHistogramInfo>)     func encodeTransformToCommandBuffer(_ commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, sourceHistogram sourceHistogram: MTLBuffer, sourceHistogramOffset sourceHistogramOffset: Int, desiredHistogram desiredHistogram: MTLBuffer, desiredHistogramOffset desiredHistogramOffset: Int) } ``` |
| To | ``` class MPSImageHistogramSpecification : MPSUnaryImageKernel {     var histogramInfo: MPSImageHistogramInfo { get }     init(device device: MTLDevice, histogramInfo histogramInfo: UnsafePointer<MPSImageHistogramInfo>)     func encodeTransform(to commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, sourceHistogram sourceHistogram: MTLBuffer, sourceHistogramOffset sourceHistogramOffset: Int, desiredHistogram desiredHistogram: MTLBuffer, desiredHistogramOffset desiredHistogramOffset: Int) } ``` |

Modified [MPSImageHistogramSpecification.encodeTransform(to: MTLCommandBuffer, sourceTexture: MTLTexture, sourceHistogram: MTLBuffer, sourceHistogramOffset: Int, desiredHistogram: MTLBuffer, desiredHistogramOffset: Int)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramspecification/1618854-encodetransform)

|  | Declaration |
| --- | --- |
| From | ``` func encodeTransformToCommandBuffer(_ commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, sourceHistogram sourceHistogram: MTLBuffer, sourceHistogramOffset sourceHistogramOffset: Int, desiredHistogram desiredHistogram: MTLBuffer, desiredHistogramOffset desiredHistogramOffset: Int) ``` |
| To | ``` func encodeTransform(to commandBuffer: MTLCommandBuffer, sourceTexture source: MTLTexture, sourceHistogram sourceHistogram: MTLBuffer, sourceHistogramOffset sourceHistogramOffset: Int, desiredHistogram desiredHistogram: MTLBuffer, desiredHistogramOffset desiredHistogramOffset: Int) ``` |

Modified [MPSImageLanczosScale](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagelanczosscale)

|  | Declaration |
| --- | --- |
| From | ``` class MPSImageLanczosScale : MPSUnaryImageKernel {     var scaleTransform: UnsafePointer<MPSScaleTransform> } ``` |
| To | ``` class MPSImageLanczosScale : MPSUnaryImageKernel {     var scaleTransform: UnsafePointer<MPSScaleTransform>? } ``` |

Modified MPSImageLanczosScale.scaleTransform

|  | Declaration |
| --- | --- |
| From | ``` var scaleTransform: UnsafePointer<MPSScaleTransform> ``` |
| To | ``` var scaleTransform: UnsafePointer<MPSScaleTransform>? ``` |

Modified [MPSImageThresholdBinary](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinary)

|  | Declaration |
| --- | --- |
| From | ``` class MPSImageThresholdBinary : MPSUnaryImageKernel {     init(device device: MTLDevice, thresholdValue thresholdValue: Float, maximumValue maximumValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>)     convenience init(device device: MTLDevice)     var thresholdValue: Float { get }     var maximumValue: Float { get }     var transform: UnsafePointer<Float> { get } } ``` |
| To | ``` class MPSImageThresholdBinary : MPSUnaryImageKernel {     init(device device: MTLDevice, thresholdValue thresholdValue: Float, maximumValue maximumValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?)     convenience init(device device: MTLDevice)     var thresholdValue: Float { get }     var maximumValue: Float { get }     var transform: UnsafePointer<Float> { get } } ``` |

Modified [MPSImageThresholdBinary.init(device: MTLDevice, thresholdValue: Float, maximumValue: Float, linearGrayColorTransform: UnsafePointer<Float>?)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinary/1618855-initwithdevice)

|  | Declaration |
| --- | --- |
| From | ``` init(device device: MTLDevice, thresholdValue thresholdValue: Float, maximumValue maximumValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>) ``` |
| To | ``` init(device device: MTLDevice, thresholdValue thresholdValue: Float, maximumValue maximumValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?) ``` |

Modified [MPSImageThresholdBinaryInverse](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinaryinverse)

|  | Declaration |
| --- | --- |
| From | ``` class MPSImageThresholdBinaryInverse : MPSUnaryImageKernel {     init(device device: MTLDevice, thresholdValue thresholdValue: Float, maximumValue maximumValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>)     convenience init(device device: MTLDevice)     var thresholdValue: Float { get }     var maximumValue: Float { get }     var transform: UnsafePointer<Float> { get } } ``` |
| To | ``` class MPSImageThresholdBinaryInverse : MPSUnaryImageKernel {     init(device device: MTLDevice, thresholdValue thresholdValue: Float, maximumValue maximumValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?)     convenience init(device device: MTLDevice)     var thresholdValue: Float { get }     var maximumValue: Float { get }     var transform: UnsafePointer<Float> { get } } ``` |

Modified [MPSImageThresholdBinaryInverse.init(device: MTLDevice, thresholdValue: Float, maximumValue: Float, linearGrayColorTransform: UnsafePointer<Float>?)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinaryinverse/1618903-initwithdevice)

|  | Declaration |
| --- | --- |
| From | ``` init(device device: MTLDevice, thresholdValue thresholdValue: Float, maximumValue maximumValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>) ``` |
| To | ``` init(device device: MTLDevice, thresholdValue thresholdValue: Float, maximumValue maximumValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?) ``` |

Modified [MPSImageThresholdToZero](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozero)

|  | Declaration |
| --- | --- |
| From | ``` class MPSImageThresholdToZero : MPSUnaryImageKernel {     init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>)     convenience init(device device: MTLDevice)     var thresholdValue: Float { get }     var transform: UnsafePointer<Float> { get } } ``` |
| To | ``` class MPSImageThresholdToZero : MPSUnaryImageKernel {     init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?)     convenience init(device device: MTLDevice)     var thresholdValue: Float { get }     var transform: UnsafePointer<Float> { get } } ``` |

Modified [MPSImageThresholdToZero.init(device: MTLDevice, thresholdValue: Float, linearGrayColorTransform: UnsafePointer<Float>?)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozero/1618865-init)

|  | Declaration |
| --- | --- |
| From | ``` init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>) ``` |
| To | ``` init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?) ``` |

Modified [MPSImageThresholdToZeroInverse](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozeroinverse)

|  | Declaration |
| --- | --- |
| From | ``` class MPSImageThresholdToZeroInverse : MPSUnaryImageKernel {     init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>)     convenience init(device device: MTLDevice)     var thresholdValue: Float { get }     var transform: UnsafePointer<Float> { get } } ``` |
| To | ``` class MPSImageThresholdToZeroInverse : MPSUnaryImageKernel {     init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?)     convenience init(device device: MTLDevice)     var thresholdValue: Float { get }     var transform: UnsafePointer<Float> { get } } ``` |

Modified [MPSImageThresholdToZeroInverse.init(device: MTLDevice, thresholdValue: Float, linearGrayColorTransform: UnsafePointer<Float>?)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozeroinverse/1618911-init)

|  | Declaration |
| --- | --- |
| From | ``` init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>) ``` |
| To | ``` init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?) ``` |

Modified [MPSImageThresholdTruncate](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtruncate)

|  | Declaration |
| --- | --- |
| From | ``` class MPSImageThresholdTruncate : MPSUnaryImageKernel {     init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>)     convenience init(device device: MTLDevice)     var thresholdValue: Float { get }     var transform: UnsafePointer<Float> { get } } ``` |
| To | ``` class MPSImageThresholdTruncate : MPSUnaryImageKernel {     init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?)     convenience init(device device: MTLDevice)     var thresholdValue: Float { get }     var transform: UnsafePointer<Float> { get } } ``` |

Modified [MPSImageThresholdTruncate.init(device: MTLDevice, thresholdValue: Float, linearGrayColorTransform: UnsafePointer<Float>?)](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtruncate/1618818-init)

|  | Declaration |
| --- | --- |
| From | ``` init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>) ``` |
| To | ``` init(device device: MTLDevice, thresholdValue thresholdValue: Float, linearGrayColorTransform transform: UnsafePointer<Float>?) ``` |

Modified [MPSKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPSKernel : NSObject, NSCopying {     var options: MPSKernelOptions     var device: MTLDevice { get }     var label: String?     init(device device: MTLDevice)     func copyWithZone(_ zone: NSZone, device device: MTLDevice?) -> Self } ``` | NSCopying |
| To | ``` class MPSKernel : NSObject, NSCopying {     var options: MPSKernelOptions     var device: MTLDevice { get }     var label: String?     init(device device: MTLDevice)     func copy(with zone: NSZone? = nil, device device: MTLDevice?) -> Self     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MPSKernel : CVarArg { } extension MPSKernel : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MPSKernel.copy(with: NSZone?, device: MTLDevice?) -> Self](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel/1618912-copywithzone)

|  | Declaration |
| --- | --- |
| From | ``` func copyWithZone(_ zone: NSZone, device device: MTLDevice?) -> Self ``` |
| To | ``` func copy(with zone: NSZone? = nil, device device: MTLDevice?) -> Self ``` |

Modified [MPSKernelOptions [struct]](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MPSKernelOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var None: MPSKernelOptions { get }     static var SkipAPIValidation: MPSKernelOptions { get }     static var AllowReducedPrecision: MPSKernelOptions { get } } ``` | OptionSetType |
| To | ``` struct MPSKernelOptions : OptionSet {     init(rawValue rawValue: UInt)     static var none: MPSKernelOptions { get }     static var skipAPIValidation: MPSKernelOptions { get }     static var allowReducedPrecision: MPSKernelOptions { get }     static var disableInternalTiling: MPSKernelOptions { get }     static var insertDebugGroups: MPSKernelOptions { get }     func intersect(_ other: MPSKernelOptions) -> MPSKernelOptions     func exclusiveOr(_ other: MPSKernelOptions) -> MPSKernelOptions     mutating func unionInPlace(_ other: MPSKernelOptions)     mutating func intersectInPlace(_ other: MPSKernelOptions)     mutating func exclusiveOrInPlace(_ other: MPSKernelOptions)     func isSubsetOf(_ other: MPSKernelOptions) -> Bool     func isDisjointWith(_ other: MPSKernelOptions) -> Bool     func isSupersetOf(_ other: MPSKernelOptions) -> Bool     mutating func subtractInPlace(_ other: MPSKernelOptions)     func isStrictSupersetOf(_ other: MPSKernelOptions) -> Bool     func isStrictSubsetOf(_ other: MPSKernelOptions) -> Bool } extension MPSKernelOptions {     func union(_ other: MPSKernelOptions) -> MPSKernelOptions     func intersection(_ other: MPSKernelOptions) -> MPSKernelOptions     func symmetricDifference(_ other: MPSKernelOptions) -> MPSKernelOptions } extension MPSKernelOptions {     func contains(_ member: MPSKernelOptions) -> Bool     mutating func insert(_ newMember: MPSKernelOptions) -> (inserted: Bool, memberAfterInsert: MPSKernelOptions)     mutating func remove(_ member: MPSKernelOptions) -> MPSKernelOptions?     mutating func update(with newMember: MPSKernelOptions) -> MPSKernelOptions? } extension MPSKernelOptions {     convenience init()     mutating func formUnion(_ other: MPSKernelOptions)     mutating func formIntersection(_ other: MPSKernelOptions)     mutating func formSymmetricDifference(_ other: MPSKernelOptions) } extension MPSKernelOptions {     convenience init<S : Sequence where S.Iterator.Element == MPSKernelOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MPSKernelOptions...)     mutating func subtract(_ other: MPSKernelOptions)     func isSubset(of other: MPSKernelOptions) -> Bool     func isSuperset(of other: MPSKernelOptions) -> Bool     func isDisjoint(with other: MPSKernelOptions) -> Bool     func subtracting(_ other: MPSKernelOptions) -> MPSKernelOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: MPSKernelOptions) -> Bool     func isStrictSubset(of other: MPSKernelOptions) -> Bool } ``` | OptionSet |

Modified [MPSKernelOptions.allowReducedPrecision](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/1618748-allowreducedprecision)

|  | Declaration |
| --- | --- |
| From | ``` static var AllowReducedPrecision: MPSKernelOptions { get } ``` |
| To | ``` static var allowReducedPrecision: MPSKernelOptions { get } ``` |

Modified [MPSKernelOptions.skipAPIValidation](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/mpskerneloptionsskipapivalidation)

|  | Declaration |
| --- | --- |
| From | ``` static var SkipAPIValidation: MPSKernelOptions { get } ``` |
| To | ``` static var skipAPIValidation: MPSKernelOptions { get } ``` |

Modified [MPSUnaryImageKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel)

|  | Declaration |
| --- | --- |
| From | ``` class MPSUnaryImageKernel : MPSKernel {     var offset: MPSOffset     var clipRect: MTLRegion     var edgeMode: MPSImageEdgeMode     func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, inPlaceTexture texture: UnsafeMutablePointer<MTLTexture?>, fallbackCopyAllocator copyAllocator: MPSCopyAllocator?) -> Bool     func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, sourceTexture sourceTexture: MTLTexture, destinationTexture destinationTexture: MTLTexture)     func sourceRegionForDestinationSize(_ destinationSize: MTLSize) -> MPSRegion } ``` |
| To | ``` class MPSUnaryImageKernel : MPSKernel {     var offset: MPSOffset     var clipRect: MTLRegion     var edgeMode: MPSImageEdgeMode     func encode(commandBuffer commandBuffer: MTLCommandBuffer, inPlaceTexture texture: UnsafeMutablePointer<MTLTexture>, fallbackCopyAllocator copyAllocator: MetalPerformanceShaders.MPSCopyAllocator? = nil) -> Bool     func encode(commandBuffer commandBuffer: MTLCommandBuffer, sourceTexture sourceTexture: MTLTexture, destinationTexture destinationTexture: MTLTexture)     func sourceRegion(destinationSize destinationSize: MTLSize) -> MPSRegion } ``` |

Modified [MPSUnaryImageKernel.encode(commandBuffer: MTLCommandBuffer, inPlaceTexture: UnsafeMutablePointer<MTLTexture>, fallbackCopyAllocator: MetalPerformanceShaders.MPSCopyAllocator?) -> Bool](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618873-encodetocommandbuffer)

|  | Declaration |
| --- | --- |
| From | ``` func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, inPlaceTexture texture: UnsafeMutablePointer<MTLTexture?>, fallbackCopyAllocator copyAllocator: MPSCopyAllocator?) -> Bool ``` |
| To | ``` func encode(commandBuffer commandBuffer: MTLCommandBuffer, inPlaceTexture texture: UnsafeMutablePointer<MTLTexture>, fallbackCopyAllocator copyAllocator: MetalPerformanceShaders.MPSCopyAllocator? = nil) -> Bool ``` |

Modified [MPSUnaryImageKernel.encode(commandBuffer: MTLCommandBuffer, sourceTexture: MTLTexture, destinationTexture: MTLTexture)](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618741-encode)

|  | Declaration |
| --- | --- |
| From | ``` func encodeToCommandBuffer(_ commandBuffer: MTLCommandBuffer, sourceTexture sourceTexture: MTLTexture, destinationTexture destinationTexture: MTLTexture) ``` |
| To | ``` func encode(commandBuffer commandBuffer: MTLCommandBuffer, sourceTexture sourceTexture: MTLTexture, destinationTexture destinationTexture: MTLTexture) ``` |

Modified [MPSUnaryImageKernel.sourceRegion(destinationSize: MTLSize) -> MPSRegion](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618754-sourceregionfordestinationsize)

|  | Declaration |
| --- | --- |
| From | ``` func sourceRegionForDestinationSize(_ destinationSize: MTLSize) -> MPSRegion ``` |
| To | ``` func sourceRegion(destinationSize destinationSize: MTLSize) -> MPSRegion ``` |

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
