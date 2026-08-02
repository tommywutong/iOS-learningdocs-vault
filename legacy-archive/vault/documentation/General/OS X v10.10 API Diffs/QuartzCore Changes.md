---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/QuartzCore.html
archived_at: '2026-07-15T07:34:47.143634Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# QuartzCore Changes

## QuartzCore

CAAnimation.hModified [+[CAAnimation animation]](https://developer.apple.com/documentation/quartzcore/caanimation/1412479-animation)

|  | Declaration |
| --- | --- |
| From | ``` + (id)animation ``` |
| To | ``` + (instancetype)animation ``` |

Modified [CAAnimation.delegate](https://developer.apple.com/documentation/quartzcore/caanimation/1412490-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id delegate ``` |
| To | ``` @property(strong) id delegate ``` |

Modified [CAAnimation.timingFunction](https://developer.apple.com/documentation/quartzcore/caanimation/1412456-timingfunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) CAMediaTimingFunction *timingFunction ``` |
| To | ``` @property(strong) CAMediaTimingFunction *timingFunction ``` |

Modified [CABasicAnimation.byValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412445-byvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id byValue ``` |
| To | ``` @property(strong) id byValue ``` |

Modified [CABasicAnimation.fromValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412519-fromvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id fromValue ``` |
| To | ``` @property(strong) id fromValue ``` |

Modified [CABasicAnimation.toValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412523-tovalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id toValue ``` |
| To | ``` @property(strong) id toValue ``` |

Modified [+[CAPropertyAnimation animationWithKeyPath:]](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412534-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)animationWithKeyPath:(NSString *)path ``` |
| To | ``` + (instancetype)animationWithKeyPath:(NSString *)path ``` |

Modified [CAPropertyAnimation.valueFunction](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412447-valuefunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) CAValueFunction *valueFunction ``` |
| To | ``` @property(strong) CAValueFunction *valueFunction ``` |

Modified [CATransition.filter](https://developer.apple.com/documentation/quartzcore/catransition/1412506-filter)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id filter ``` |
| To | ``` @property(strong) id filter ``` |

CAEmitterBehavior.hModified -[CAEmitterBehavior initWithType:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(NSString *)type ``` |
| To | ``` - (instancetype)initWithType:(NSString *)type ``` |

CAEmitterCell.hModified [CAEmitterCell.contents](https://developer.apple.com/documentation/quartzcore/caemittercell/1522109-contents)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id contents ``` |
| To | ``` @property(strong) id contents ``` |

Modified [+[CAEmitterCell emitterCell]](https://developer.apple.com/documentation/quartzcore/caemittercell/1584370-emittercell)

|  | Declaration |
| --- | --- |
| From | ``` + (id)emitterCell ``` |
| To | ``` + (instancetype)emitterCell ``` |

CALayer.hRemoved CAAutoresizingMaskRemoved CAEdgeAntialiasingMaskAdded [CAAutoresizingMask](https://developer.apple.com/documentation/quartzcore/caautoresizingmask)Added [CAEdgeAntialiasingMask](https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask)Modified [CALayer.autoresizingMask](https://developer.apple.com/documentation/quartzcore/calayer/1410877-autoresizingmask)

|  | Declaration |
| --- | --- |
| From | ``` @property unsigned int autoresizingMask ``` |
| To | ``` @property CAAutoresizingMask autoresizingMask ``` |

Modified [CALayer.compositingFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410748-compositingfilter)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id compositingFilter ``` |
| To | ``` @property(strong) id compositingFilter ``` |

Modified [CALayer.contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id contents ``` |
| To | ``` @property(strong) id contents ``` |

Modified [CALayer.delegate](https://developer.apple.com/documentation/quartzcore/calayer/1410984-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id delegate ``` |
| To | ``` @property(weak) id delegate ``` |

Modified [CALayer.edgeAntialiasingMask](https://developer.apple.com/documentation/quartzcore/calayer/1410892-edgeantialiasingmask)

|  | Declaration |
| --- | --- |
| From | ``` @property unsigned int edgeAntialiasingMask ``` |
| To | ``` @property CAEdgeAntialiasingMask edgeAntialiasingMask ``` |

Modified [-[CALayer init]](https://developer.apple.com/documentation/quartzcore/calayer/1410835-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[CALayer initWithLayer:]](https://developer.apple.com/documentation/quartzcore/calayer/1410842-initwithlayer)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLayer:(id)layer ``` |
| To | ``` - (instancetype)initWithLayer:(id)layer ``` |

Modified [+[CALayer layer]](https://developer.apple.com/documentation/quartzcore/calayer/1410793-layer)

|  | Declaration |
| --- | --- |
| From | ``` + (id)layer ``` |
| To | ``` + (instancetype)layer ``` |

Modified [CALayer.layoutManager](https://developer.apple.com/documentation/quartzcore/calayer/1410749-layoutmanager)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id layoutManager ``` |
| To | ``` @property(strong) id layoutManager ``` |

Modified [CALayer.mask](https://developer.apple.com/documentation/quartzcore/calayer/1410861-mask)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) CALayer *mask ``` |
| To | ``` @property(strong) CALayer *mask ``` |

CAMediaTimingFunction.hModified [+[CAMediaTimingFunction functionWithName:]](https://developer.apple.com/documentation/quartzcore/camediatimingfunction/1521979-functionwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)functionWithName:(NSString *)name ``` |
| To | ``` + (instancetype)functionWithName:(NSString *)name ``` |

CARemoteLayerClient.hModified [CARemoteLayerClient.layer](https://developer.apple.com/documentation/quartzcore/caremotelayerclient/1418373-layer)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) CALayer *layer ``` |
| To | ``` @property(strong) CALayer *layer ``` |

CARenderer.hModified [CARenderer.layer](https://developer.apple.com/documentation/quartzcore/carenderer/1519583-layer)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) CALayer *layer ``` |
| To | ``` @property(strong) CALayer *layer ``` |

CATransaction.hModified [+[CATransaction completionBlock]](https://developer.apple.com/documentation/quartzcore/catransaction/1448280-completionblock)

|  | Declaration |
| --- | --- |
| From | ``` + (void (^)())completionBlock ``` |
| To | ``` + (void (^)(void))completionBlock ``` |

CATransform3D.hRemoved [-[NSValue CATransform3DValue]](https://developer.apple.com/documentation/foundation/nsvalue/1436572-catransform3dvalue)Added [NSValue.CATransform3DValue](https://developer.apple.com/documentation/foundation/nsvalue/1436572-catransform3dvalue)CAValueFunction.hModified [+[CAValueFunction functionWithName:]](https://developer.apple.com/documentation/quartzcore/cavaluefunction/1522115-functionwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)functionWithName:(NSString *)name ``` |
| To | ``` + (instancetype)functionWithName:(NSString *)name ``` |

CIContext.hAdded [+[CIContext contextForOfflineGPUAtIndex:]](https://developer.apple.com/documentation/coreimage/cicontext/1437772-contextforofflinegpuatindex)Added [+[CIContext contextForOfflineGPUAtIndex:colorSpace:options:sharedContext:]](https://developer.apple.com/documentation/coreimage/cicontext/1437758-contextforofflinegpuatindex)Added [+[CIContext offlineGPUCount]](https://developer.apple.com/documentation/coreimage/cicontext/1437817-offlinegpucount)CIDetector.hAdded [CIDetectorAspectRatio](https://developer.apple.com/documentation/coreimage/cidetectoraspectratio)Added [CIDetectorFocalLength](https://developer.apple.com/documentation/coreimage/cidetectorfocallength)Added [CIDetectorTypeQRCode](https://developer.apple.com/documentation/coreimage/cidetectortypeqrcode)Added [CIDetectorTypeRectangle](https://developer.apple.com/documentation/coreimage/cidetectortyperectangle)CIFeature.hAdded [CIQRCodeFeature](https://developer.apple.com/documentation/coreimage/ciqrcodefeature)Added [CIQRCodeFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437985-bottomleft)Added [CIQRCodeFeature.bottomRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438245-bottomright)Added [CIQRCodeFeature.bounds](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438153-bounds)Added [CIQRCodeFeature.messageString](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438035-messagestring)Added [CIQRCodeFeature.topLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437780-topleft)Added [CIQRCodeFeature.topRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437896-topright)Added [CIRectangleFeature](https://developer.apple.com/documentation/coreimage/cirectanglefeature)Added [CIRectangleFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437878-bottomleft)Added [CIRectangleFeature.bottomRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437888-bottomright)Added [CIRectangleFeature.bounds](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438024-bounds)Added [CIRectangleFeature.topLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437951-topleft)Added [CIRectangleFeature.topRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438071-topright)Added [CIFeatureTypeRectangle](https://developer.apple.com/documentation/coreimage/cifeaturetyperectangle)CIFilter.hAdded [+[CIFilter filterWithName:withInputParameters:]](https://developer.apple.com/documentation/coreimage/cifilter/1437894-init)Added [CIFilter.outputImage](https://developer.apple.com/documentation/coreimage/cifilter/1438169-outputimage)CIImage.hAdded [-[CIImage imageByApplyingFilter:withInputParameters:]](https://developer.apple.com/documentation/coreimage/ciimage/1437589-applyingfilter)Added [-[CIImage imageByApplyingOrientation:]](https://developer.apple.com/documentation/coreimage/ciimage/1438223-imagebyapplyingorientation)Added [-[CIImage imageByClampingToExtent]](https://developer.apple.com/documentation/coreimage/ciimage/1437628-clampedtoextent)Added [-[CIImage imageByCompositingOverImage:]](https://developer.apple.com/documentation/coreimage/ciimage/1437837-composited)Added [-[CIImage imageTransformForOrientation:]](https://developer.apple.com/documentation/coreimage/ciimage/1437930-orientationtransform)Added [kCIImageAutoAdjustCrop](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/1438229-crop)Added [kCIImageAutoAdjustLevel](https://developer.apple.com/documentation/coreimage/kciimageautoadjustlevel)CIKernel.hAdded [+[CIKernel kernelWithString:]](https://developer.apple.com/documentation/coreimage/cikernel/1437796-kernelwithstring)CIRAWFilter.hAdded [kCIInputColorNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437640-colornoisereductionamount)Added [kCIInputEnableVendorLensCorrectionKey](https://developer.apple.com/documentation/coreimage/kciinputenablevendorlenscorrectionkey)Added [kCIInputLuminanceNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/kciinputluminancenoisereductionamountkey)Added [kCIInputNoiseReductionContrastAmountKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437681-noisereductioncontrastamount)Added [kCIInputNoiseReductionDetailAmountKey](https://developer.apple.com/documentation/coreimage/kciinputnoisereductiondetailamountkey)Added [kCIInputNoiseReductionSharpnessAmountKey](https://developer.apple.com/documentation/coreimage/kciinputnoisereductionsharpnessamountkey)

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
