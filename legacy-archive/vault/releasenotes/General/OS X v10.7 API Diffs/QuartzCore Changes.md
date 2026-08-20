---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/QuartzCore.html
archived_at: '2026-07-18T02:54:38.850417Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# QuartzCore Changes

## QuartzCore

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

CAAnimation.hAdded [CAKeyframeAnimation.biasValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412485-biasvalues)Added [CAKeyframeAnimation.continuityValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412491-continuityvalues)Added [CAKeyframeAnimation.tensionValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412475-tensionvalues)Added [kCAAnimationCubic](https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode/1412481-cubic)Added [kCAAnimationCubicPaced](https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode/1412452-cubicpaced)CABase.hAdded #def CA_OS_VERSIONCALayer.hAdded [CALayer.contentsScale](https://developer.apple.com/documentation/quartzcore/calayer/1410746-contentsscale)Added [CALayer.rasterizationScale](https://developer.apple.com/documentation/quartzcore/calayer/1410801-rasterizationscale)Added [CALayer.shadowPath](https://developer.apple.com/documentation/quartzcore/calayer/1410771-shadowpath)Added [CALayer.shouldRasterize](https://developer.apple.com/documentation/quartzcore/calayer/1410905-shouldrasterize)CARemoteLayerClient.hAdded [CARemoteLayerClient](https://developer.apple.com/documentation/quartzcore/caremotelayerclient)Added [CARemoteLayerClient.clientId](https://developer.apple.com/documentation/quartzcore/caremotelayerclient/1418375-clientid)Added [-[CARemoteLayerClient initWithServerPort:]](https://developer.apple.com/documentation/quartzcore/caremotelayerclient/1418377-init)Added [-[CARemoteLayerClient invalidate]](https://developer.apple.com/documentation/quartzcore/caremotelayerclient/1418372-invalidate)Added [CARemoteLayerClient.layer](https://developer.apple.com/documentation/quartzcore/caremotelayerclient/1418373-layer)CARemoteLayerServer.hAdded [+[CALayer layerWithRemoteClientId:]](https://developer.apple.com/documentation/quartzcore/calayer/1522119-layerwithremoteclientid)Added [CARemoteLayerServer](https://developer.apple.com/documentation/quartzcore/caremotelayerserver)Added [CARemoteLayerServer.serverPort](https://developer.apple.com/documentation/quartzcore/caremotelayerserver/1521922-serverport)Added [+[CARemoteLayerServer sharedServer]](https://developer.apple.com/documentation/quartzcore/caremotelayerserver/1521954-sharedserver)Added CALayer(CARemoteLayerServer)CAShapeLayer.hAdded [CAShapeLayer.strokeEnd](https://developer.apple.com/documentation/quartzcore/cashapelayer/1522252-strokeend)Added [CAShapeLayer.strokeStart](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521929-strokestart)CIContext.hRemoved #def AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_6Removed #def AVAILABLE_MAC_OS_X_VERSION_10_6_AND_LATERCIDetector.hAdded [CIDetector](https://developer.apple.com/documentation/coreimage/cidetector)Added [+[CIDetector detectorOfType:context:options:]](https://developer.apple.com/documentation/coreimage/cidetector/1437884-init)Added [-[CIDetector featuresInImage:]](https://developer.apple.com/documentation/coreimage/cidetector/1438049-featuresinimage)Added [CIDetectorAccuracy](https://developer.apple.com/documentation/coreimage/cidetectoraccuracy)Added [CIDetectorAccuracyHigh](https://developer.apple.com/documentation/coreimage/cidetectoraccuracyhigh)Added [CIDetectorAccuracyLow](https://developer.apple.com/documentation/coreimage/cidetectoraccuracylow)Added [CIDetectorTypeFace](https://developer.apple.com/documentation/coreimage/cidetectortypeface)CIFeature.hAdded [CIFaceFeature](https://developer.apple.com/documentation/coreimage/cifacefeature)Added [CIFaceFeature.hasLeftEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437900-haslefteyeposition)Added [CIFaceFeature.hasMouthPosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437976-hasmouthposition)Added [CIFaceFeature.hasRightEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438076-hasrighteyeposition)Added [CIFaceFeature.leftEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437923-lefteyeposition)Added [CIFaceFeature.mouthPosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438020-mouthposition)Added [CIFaceFeature.rightEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438213-righteyeposition)Added [CIFeature](https://developer.apple.com/documentation/coreimage/cifeature)Added [CIFeature.bounds](https://developer.apple.com/documentation/coreimage/cifeature/1437782-bounds)Added [CIFeature.type](https://developer.apple.com/documentation/coreimage/cifeature/1438092-type)Added [CIFeatureTypeFace](https://developer.apple.com/documentation/coreimage/cifeaturetypeface)CIFilter.hRemoved #def AVAILABLE_MAC_OS_X_VERSION_10_5_AND_LATERRemoved #def DEPRECATED_IN_MAC_OS_X_VERSION_10_5_AND_LATERAdded [kCIApplyOptionColorSpace](https://developer.apple.com/documentation/coreimage/kciapplyoptioncolorspace)Modified [+[CIFilter registerFilterName:constructor:classAttributes:]](https://developer.apple.com/documentation/coreimage/cifilter/1437889-registername)

|  | Declaration |
| --- | --- |
| From | + (void)registerFilterName:(NSString \*)name constructor:(id)anObject classAttributes:(NSDictionary \*)attributes |
| To | + (void)registerFilterName:(NSString \*)name constructor:(id < CIFilterConstructor >)anObject classAttributes:(NSDictionary \*)attributes |

CIFilterConstructor.hAdded [CIFilterConstructor](https://developer.apple.com/documentation/coreimage/cifilterconstructor)Added [-[CIFilterConstructor filterWithName:]](https://developer.apple.com/documentation/coreimage/cifilterconstructor/1438018-filterwithname)CIFilterGenerator.hModified [CIFilterGenerator](https://developer.apple.com/documentation/coreimage/cifiltergenerator)

|  | Protocols |
| --- | --- |
| From | NSCoding, NSCopying |
| To | CIFilterConstructor, NSCoding, NSCopying |

CIImage.hRemoved colorSpace (no architecture available)Removed definition (no architecture available)Removed emptyImage (no architecture available)Removed extent (no architecture available)Removed imageByApplyingTransform (no architecture available)Removed imageByCroppingToRect (no architecture available)Removed imageWithBitmapData (no architecture available)Removed imageWithCGImage (no architecture available)Removed imageWithCGLayer (no architecture available)Removed imageWithCVImageBuffer (no architecture available)Removed imageWithColor (no architecture available)Removed imageWithContentsOfURL (no architecture available)Removed imageWithData (no architecture available)Removed imageWithIOSurface (no architecture available)Removed imageWithTexture (no architecture available)Removed initWithBitmapData (no architecture available)Removed initWithCGImage (no architecture available)Removed initWithCGLayer (no architecture available)Removed initWithCVImageBuffer (no architecture available)Removed initWithColor (no architecture available)Removed initWithContentsOfURL (no architecture available)Removed initWithData (no architecture available)Removed initWithIOSurface (no architecture available)Removed initWithTexture (no architecture available)Removed [kCIFormatARGB8](https://developer.apple.com/documentation/coreimage/ciformat/1437883-argb8) (no architecture available)Removed [kCIFormatRGBA16](https://developer.apple.com/documentation/coreimage/ciformat/1437999-rgba16) (no architecture available)Removed [kCIFormatRGBAf](https://developer.apple.com/documentation/coreimage/kciformatrgbaf) (no architecture available)Removed [kCIImageColorSpace](https://developer.apple.com/documentation/coreimage/ciimageoption/1438131-colorspace) (no architecture available)Removed url (no architecture available)CIImageAccumulator.hAdded [+[CIImageAccumulator imageAccumulatorWithExtent:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427712-imageaccumulatorwithextent)Added [-[CIImageAccumulator initWithExtent:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427710-init)Modified [-[CIImageAccumulator initWithExtent:format:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427718-init)

|  | Declaration |
| --- | --- |
| From | - (id)initWithExtent:(CGRect)r format:(CIFormat)f |
| To | - (id)initWithExtent:(CGRect)extent format:(CIFormat)format |

Modified [+[CIImageAccumulator imageAccumulatorWithExtent:format:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427722-imageaccumulatorwithextent)

|  | Declaration |
| --- | --- |
| From | + (CIImageAccumulator \*)imageAccumulatorWithExtent:(CGRect)r format:(CIFormat)f |
| To | + (CIImageAccumulator \*)imageAccumulatorWithExtent:(CGRect)extent format:(CIFormat)format |

CIImageProvider.hRemoved +[CIImage imageWithImageProvider:size:width:format:colorSpace:options:]Removed -[CIImage initWithImageProvider:size:width:format:colorSpace:options:]Removed -[NSObject provideImageData:bytesPerRow:origin:x:size:width:userInfo:]Added [+[CIImage imageWithImageProvider:size::format:colorSpace:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1579115-imagewithimageprovider)Added [-[CIImage initWithImageProvider:size::format:colorSpace:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437868-init)Added [-[NSObject provideImageData:bytesPerRow:origin::size::userInfo:]](https://developer.apple.com/documentation/objectivec/nsobject/1438175-provideimagedata)CIPlugIn.hAdded [+[CIPlugIn loadPlugIn:allowExecutableCode:]](https://developer.apple.com/documentation/coreimage/ciplugin/1438187-loadplugin)Modified [+[CIPlugIn loadPlugIn:allowNonExecutable:]](https://developer.apple.com/documentation/coreimage/ciplugin/1551323-loadplugin)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

CIRAWFilter.hAdded [kCIActiveKeys](https://developer.apple.com/documentation/coreimage/kciactivekeys)Added [kCIInputLinearSpaceFilter](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438078-linearspacefilter)Added [kCIInputNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/kciinputnoisereductionamountkey)CISampler.hAdded [kCISamplerColorSpace](https://developer.apple.com/documentation/coreimage/kcisamplercolorspace)CoreImageDefines.hAdded #def COREIMAGEDEFINES_H_JUPUTD8MAdded #def CORE_IMAGE_CLASS_EXPORTAdded #def CORE_IMAGE_EXPORTQuartzCore.hAdded #def QUARTZCORE_H

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
