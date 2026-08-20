---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/MetalPerformanceShaders.html
archived_at: '2026-07-18T02:56:35.204114Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# MetalPerformanceShaders Changes for Objective-C

### MetalPerformanceShaders (Added)

#### MPSImageConvolution.h (Added)

Added [MPSImageBox](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagebox)Added [-[MPSImageBox initWithDevice:kernelWidth:kernelHeight:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagebox/1618789-init)Added [MPSImageBox.kernelHeight](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagebox/1618739-kernelheight)Added [MPSImageBox.kernelWidth](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagebox/1618834-kernelwidth)Added [MPSImageConvolution](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconvolution)Added [MPSImageConvolution.bias](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconvolution/1618841-bias)Added [-[MPSImageConvolution initWithDevice:kernelWidth:kernelHeight:weights:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconvolution/1618902-initwithdevice)Added [MPSImageConvolution.kernelHeight](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconvolution/1618842-kernelheight)Added [MPSImageConvolution.kernelWidth](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageconvolution/1618868-kernelwidth)Added [MPSImageGaussianBlur](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagegaussianblur)Added [-[MPSImageGaussianBlur initWithDevice:sigma:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagegaussianblur/1618813-initwithdevice)Added [MPSImageGaussianBlur.sigma](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagegaussianblur/1618850-sigma)Added [MPSImageSobel](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagesobel)Added [MPSImageSobel.colorTransform](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagesobel/1618777-colortransform)Added [-[MPSImageSobel initWithDevice:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagesobel/1618843-initwithdevice)Added [-[MPSImageSobel initWithDevice:linearGrayColorTransform:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagesobel/1618899-initwithdevice)Added [MPSImageTent](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetent)

#### MPSImageHistogram.h (Added)

Added [MPSImageHistogram](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram)Added [MPSImageHistogram.clipRectSource](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/1618765-cliprectsource)Added [-[MPSImageHistogram encodeToCommandBuffer:sourceTexture:histogram:histogramOffset:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/1618853-encode)Added [MPSImageHistogram.histogramInfo](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/1618844-histograminfo)Added [-[MPSImageHistogram histogramSizeForSourceFormat:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/1618839-histogramsizeforsourceformat)Added [-[MPSImageHistogram initWithDevice:histogramInfo:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/1618910-init)Added [MPSImageHistogram.zeroHistogram](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/1618891-zerohistogram)Added [MPSImageHistogramEqualization](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramequalization)Added [-[MPSImageHistogramEqualization encodeTransformToCommandBuffer:sourceTexture:histogram:histogramOffset:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramequalization/1618746-encodetransformtocommandbuffer)Added [MPSImageHistogramEqualization.histogramInfo](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramequalization/1618775-histograminfo)Added [-[MPSImageHistogramEqualization initWithDevice:histogramInfo:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramequalization/1618856-initwithdevice)Added [MPSImageHistogramSpecification](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramspecification)Added [-[MPSImageHistogramSpecification encodeTransformToCommandBuffer:sourceTexture:sourceHistogram:sourceHistogramOffset:desiredHistogram:desiredHistogramOffset:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramspecification/1618854-encodetransform)Added [MPSImageHistogramSpecification.histogramInfo](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramspecification/1618810-histograminfo)Added [-[MPSImageHistogramSpecification initWithDevice:histogramInfo:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogramspecification/1618907-initwithdevice)Added [MPSImageHistogramInfo](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistograminfo)

#### MPSImageIntegral.h (Added)

Added [MPSImageIntegral](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageintegral)Added [MPSImageIntegralOfSquares](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageintegralofsquares)

#### MPSImageKernel.h (Added)

Added [MPSBinaryImageKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel)Added [MPSBinaryImageKernel.clipRect](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618879-cliprect)Added [-[MPSBinaryImageKernel encodeToCommandBuffer:inPlacePrimaryTexture:secondaryTexture:fallbackCopyAllocator:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618771-encode)Added [-[MPSBinaryImageKernel encodeToCommandBuffer:primaryTexture:inPlaceSecondaryTexture:fallbackCopyAllocator:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618890-encode)Added [-[MPSBinaryImageKernel encodeToCommandBuffer:primaryTexture:secondaryTexture:destinationTexture:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618871-encodetocommandbuffer)Added [MPSBinaryImageKernel.primaryEdgeMode](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618782-primaryedgemode)Added [MPSBinaryImageKernel.primaryOffset](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618880-primaryoffset)Added [-[MPSBinaryImageKernel primarySourceRegionForDestinationSize:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618900-primarysourceregion)Added [MPSBinaryImageKernel.secondaryEdgeMode](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618848-secondaryedgemode)Added [MPSBinaryImageKernel.secondaryOffset](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618755-secondaryoffset)Added [-[MPSBinaryImageKernel secondarySourceRegionForDestinationSize:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/1618838-secondarysourceregionfordestinat)Added [MPSUnaryImageKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel)Added [MPSUnaryImageKernel.clipRect](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618859-cliprect)Added [MPSUnaryImageKernel.edgeMode](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618812-edgemode)Added [-[MPSUnaryImageKernel encodeToCommandBuffer:inPlaceTexture:fallbackCopyAllocator:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618873-encodetocommandbuffer)Added [-[MPSUnaryImageKernel encodeToCommandBuffer:sourceTexture:destinationTexture:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618741-encodetocommandbuffer)Added [MPSUnaryImageKernel.offset](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618884-offset)Added [-[MPSUnaryImageKernel sourceRegionForDestinationSize:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/1618754-sourceregionfordestinationsize)

#### MPSImageMedian.h (Added)

Added [MPSImageMedian](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagemedian)Added [-[MPSImageMedian initWithDevice:kernelDiameter:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagemedian/1618837-initwithdevice)Added [MPSImageMedian.kernelDiameter](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagemedian/1618909-kerneldiameter)Added [+[MPSImageMedian maxKernelDiameter]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagemedian/1618830-maxkerneldiameter)Added [+[MPSImageMedian minKernelDiameter]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagemedian/1618864-minkerneldiameter)

#### MPSImageMorphology.h (Added)

Added [MPSImageAreaMax](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageareamax)Added [-[MPSImageAreaMax initWithDevice:kernelWidth:kernelHeight:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageareamax/1618281-initwithdevice)Added [MPSImageAreaMax.kernelHeight](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageareamax/1618277-kernelheight)Added [MPSImageAreaMax.kernelWidth](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageareamax/1618282-kernelwidth)Added [MPSImageAreaMin](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageareamin)Added [MPSImageDilate](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedilate)Added [-[MPSImageDilate initWithDevice:kernelWidth:kernelHeight:values:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedilate/1618285-init)Added [MPSImageDilate.kernelHeight](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedilate/1618280-kernelheight)Added [MPSImageDilate.kernelWidth](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagedilate/1618279-kernelwidth)Added [MPSImageErode](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageerode)

#### MPSImageResampling.h (Added)

Added [MPSImageLanczosScale](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagelanczosscale)Added MPSImageLanczosScale.scaleTransform

#### MPSImageThreshold.h (Added)

Added [MPSImageThresholdBinary](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinary)Added [-[MPSImageThresholdBinary initWithDevice:thresholdValue:maximumValue:linearGrayColorTransform:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinary/1618855-init)Added [MPSImageThresholdBinary.maximumValue](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinary/1618852-maximumvalue)Added [MPSImageThresholdBinary.thresholdValue](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinary/1618851-thresholdvalue)Added [MPSImageThresholdBinary.transform](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinary/1618744-transform)Added [MPSImageThresholdBinaryInverse](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinaryinverse)Added [-[MPSImageThresholdBinaryInverse initWithDevice:thresholdValue:maximumValue:linearGrayColorTransform:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinaryinverse/1618903-initwithdevice)Added [MPSImageThresholdBinaryInverse.maximumValue](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinaryinverse/1618906-maximumvalue)Added [MPSImageThresholdBinaryInverse.thresholdValue](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinaryinverse/1618845-thresholdvalue)Added [MPSImageThresholdBinaryInverse.transform](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdbinaryinverse/1618904-transform)Added [MPSImageThresholdToZero](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozero)Added [-[MPSImageThresholdToZero initWithDevice:thresholdValue:linearGrayColorTransform:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozero/1618865-init)Added [MPSImageThresholdToZero.thresholdValue](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozero/1618767-thresholdvalue)Added [MPSImageThresholdToZero.transform](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozero/1618823-transform)Added [MPSImageThresholdToZeroInverse](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozeroinverse)Added [-[MPSImageThresholdToZeroInverse initWithDevice:thresholdValue:linearGrayColorTransform:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozeroinverse/1618911-init)Added [MPSImageThresholdToZeroInverse.thresholdValue](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozeroinverse/1618914-thresholdvalue)Added [MPSImageThresholdToZeroInverse.transform](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtozeroinverse/1618828-transform)Added [MPSImageThresholdTruncate](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtruncate)Added [-[MPSImageThresholdTruncate initWithDevice:thresholdValue:linearGrayColorTransform:]](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtruncate/1618818-init)Added [MPSImageThresholdTruncate.thresholdValue](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtruncate/1618882-thresholdvalue)Added [MPSImageThresholdTruncate.transform](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagethresholdtruncate/1618787-transform)

#### MPSImageTranspose.h (Added)

Added [MPSImageTranspose](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagetranspose)

#### MPSKernel.h (Added)

Added [MPSKernel](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel)Added [-[MPSKernel copyWithZone:device:]](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel/1618912-copy)Added [MPSKernel.device](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel/1618824-device)Added [-[MPSKernel initWithDevice:]](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel/1618763-init)Added [MPSKernel.label](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel/1618803-label)Added [MPSKernel.options](https://developer.apple.com/documentation/metalperformanceshaders/mpskernel/1618889-options)Added [MPSSupportsMTLDevice()](https://developer.apple.com/documentation/metalperformanceshaders/1618849-mpssupportsmtldevice)

#### MPSTypes.h (Added)

Added [MPSCopyAllocator](https://developer.apple.com/documentation/metalperformanceshaders/mpscopyallocator)Added [MPSImageEdgeMode](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedgemode)Added [MPSImageEdgeModeClamp](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedgemode/mpsimageedgemodeclamp)Added [MPSImageEdgeModeZero](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageedgemode/mpsimageedgemodezero)Added [MPSKernelOptions](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions)Added [MPSKernelOptionsAllowReducedPrecision](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/1618748-allowreducedprecision)Added [MPSKernelOptionsNone](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/mpskerneloptionsnone)Added [MPSKernelOptionsSkipAPIValidation](https://developer.apple.com/documentation/metalperformanceshaders/mpskerneloptions/1618826-skipapivalidation)Added [MPSOffset](https://developer.apple.com/documentation/metalperformanceshaders/mpsoffset)Added [MPSOrigin](https://developer.apple.com/documentation/metalperformanceshaders/mpsorigin)Added [MPSRectNoClip](https://developer.apple.com/documentation/metalperformanceshaders/mpsrectnoclip)Added [MPSRegion](https://developer.apple.com/documentation/metalperformanceshaders/mpsregion)Added [MPSScaleTransform](https://developer.apple.com/documentation/metalperformanceshaders/mpsscaletransform)Added [MPSSize](https://developer.apple.com/documentation/metalperformanceshaders/mpssize)

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
