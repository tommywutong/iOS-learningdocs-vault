---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/CoreImage.html
archived_at: '2026-07-18T02:50:38.227363Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CoreImage Changes for Objective-C

### CoreImage

#### CIColor.h

Added [+[CIColor blackColor]](https://developer.apple.com/documentation/coreimage/cicolor/1643578-black)Added [+[CIColor blueColor]](https://developer.apple.com/documentation/coreimage/cicolor/1643569-blue)Added [+[CIColor clearColor]](https://developer.apple.com/documentation/coreimage/cicolor/1643577-clearcolor)Added [+[CIColor colorWithRed:green:blue:alpha:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicolor/1643575-colorwithred)Added [+[CIColor colorWithRed:green:blue:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicolor/1643579-colorwithred)Added [+[CIColor cyanColor]](https://developer.apple.com/documentation/coreimage/cicolor/1643581-cyan)Added [+[CIColor grayColor]](https://developer.apple.com/documentation/coreimage/cicolor/1643573-graycolor)Added [+[CIColor greenColor]](https://developer.apple.com/documentation/coreimage/cicolor/1643580-green)Added [-[CIColor initWithRed:green:blue:alpha:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicolor/1643572-init)Added [-[CIColor initWithRed:green:blue:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicolor/1643576-init)Added [+[CIColor magentaColor]](https://developer.apple.com/documentation/coreimage/cicolor/1643574-magenta)Added [+[CIColor redColor]](https://developer.apple.com/documentation/coreimage/cicolor/1643570-red)Added [+[CIColor whiteColor]](https://developer.apple.com/documentation/coreimage/cicolor/1643571-whitecolor)Added [+[CIColor yellowColor]](https://developer.apple.com/documentation/coreimage/cicolor/1643582-yellowcolor)

#### CIContext.h

Removed #def CI_ARRAYRemoved #def CI_DICTIONARYAdded [+[CIContext context]](https://developer.apple.com/documentation/coreimage/cicontext/1642219-context)Added [-[CIContext createCGImage:fromRect:format:colorSpace:deferred:]](https://developer.apple.com/documentation/coreimage/cicontext/1642211-createcgimage)Added [-[CIContext init]](https://developer.apple.com/documentation/coreimage/cicontext/1642212-init)Added [-[CIContext initWithOptions:]](https://developer.apple.com/documentation/coreimage/cicontext/1438261-init)Added [-[CIContext JPEGRepresentationOfImage:colorSpace:options:]](https://developer.apple.com/documentation/coreimage/cicontext/1642214-jpegrepresentation)Added [-[CIContext TIFFRepresentationOfImage:format:colorSpace:options:]](https://developer.apple.com/documentation/coreimage/cicontext/1642220-tiffrepresentationofimage)Added [CIContext.workingFormat](https://developer.apple.com/documentation/coreimage/cicontext/1642215-workingformat)Added [-[CIContext writeJPEGRepresentationOfImage:toURL:colorSpace:options:error:]](https://developer.apple.com/documentation/coreimage/cicontext/1642218-writejpegrepresentation)Added [-[CIContext writeTIFFRepresentationOfImage:toURL:format:colorSpace:options:error:]](https://developer.apple.com/documentation/coreimage/cicontext/1642213-writetiffrepresentationofimage)Added CIContext(ImageRepresentation)Added [kCIContextCacheIntermediates](https://developer.apple.com/documentation/coreimage/kcicontextcacheintermediates)Added [kCIContextOutputPremultiplied](https://developer.apple.com/documentation/coreimage/kcicontextoutputpremultiplied)Added [kCIContextPriorityRequestLow](https://developer.apple.com/documentation/coreimage/kcicontextpriorityrequestlow)

#### CIDetector.h

Removed #def CI_ARRAYRemoved #def CI_DICTIONARYAdded [CIDetectorMaxFeatureCount](https://developer.apple.com/documentation/coreimage/cidetectormaxfeaturecount)

#### CIFilter.h

Removed #def CI_ARRAYRemoved #def CI_DICTIONARYAdded [-[CIFilter name]](https://developer.apple.com/documentation/coreimage/cifilter/1437997-name)Added [-[CIFilter setName:]](https://developer.apple.com/documentation/coreimage/cifilter/1437997-name)

#### CIFilterGenerator.h

Modified [-[CIFilterGenerator disconnectObject:withKey:toObject:withKey:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438075-disconnectobject)

|  | Declaration |
| --- | --- |
| From | ``` - (void)disconnectObject:(id)sourceObject withKey:(NSString *)key toObject:(id)targetObject withKey:(NSString *)targetKey ``` |
| To | ``` - (void)disconnectObject:(id)sourceObject withKey:(NSString *)sourceKey toObject:(id)targetObject withKey:(NSString *)targetKey ``` |

#### CIImage.h

Removed #def CI_ARRAYRemoved #def CI_DICTIONARYAdded [-[CIImage autoAdjustmentFilters]](https://developer.apple.com/documentation/coreimage/ciimage/1645889-autoadjustmentfilters)Added [CIImage.CGImage](https://developer.apple.com/documentation/coreimage/ciimage/1687603-cgimage)Added [-[CIImage imageByApplyingGaussianBlurWithSigma:]](https://developer.apple.com/documentation/coreimage/ciimage/1645897-imagebyapplyinggaussianblurwiths)Added [-[CIImage imageByClampingToRect:]](https://developer.apple.com/documentation/coreimage/ciimage/1645893-imagebyclampingtorect)Added [-[CIImage imageByColorMatchingColorSpaceToWorkingSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1645896-imagebycolormatchingcolorspaceto)Added [-[CIImage imageByColorMatchingWorkingSpaceToColorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1645898-imagebycolormatchingworkingspace)Added [-[CIImage imageByPremultiplyingAlpha]](https://developer.apple.com/documentation/coreimage/ciimage/1645894-imagebypremultiplyingalpha)Added [-[CIImage imageBySettingAlphaOneInExtent:]](https://developer.apple.com/documentation/coreimage/ciimage/1645891-imagebysettingalphaoneinextent)Added [-[CIImage imageBySettingProperties:]](https://developer.apple.com/documentation/coreimage/ciimage/1645895-imagebysettingproperties)Added [-[CIImage imageByUnpremultiplyingAlpha]](https://developer.apple.com/documentation/coreimage/ciimage/1645892-imagebyunpremultiplyingalpha)Added [CIImage.pixelBuffer](https://developer.apple.com/documentation/coreimage/ciimage/1687604-pixelbuffer)

#### CIImageProcessor.h (Added)

Added [CIImageProcessorInput](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput)Added [CIImageProcessorInput.baseAddress](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/1639645-baseaddress)Added [CIImageProcessorInput.bytesPerRow](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/1639655-bytesperrow)Added [CIImageProcessorInput.format](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/1639639-format)Added [CIImageProcessorInput.metalTexture](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/1639651-metaltexture)Added [CIImageProcessorInput.pixelBuffer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/1639649-pixelbuffer)Added [CIImageProcessorInput.region](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/1639633-region)Added [CIImageProcessorInput.surface](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/1639657-surface)Added [CIImageProcessorKernel](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel)Added [+[CIImageProcessorKernel applyWithExtent:inputs:arguments:error:]](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2138284-applywithextent)Added [+[CIImageProcessorKernel formatForInputAtIndex:]](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2138289-formatforinput)Added [+[CIImageProcessorKernel outputFormat]](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2143065-outputformat)Added [CIImageProcessorKernel.outputFormat](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2143065-outputformat)Added [+[CIImageProcessorKernel processWithInputs:arguments:output:error:]](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2138290-processwithinputs)Added [+[CIImageProcessorKernel roiForInput:arguments:outputRect:]](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2138287-roi)Added [+[CIImageProcessorKernel synchronizeInputs]](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2143066-synchronizeinputs)Added [CIImageProcessorKernel.synchronizeInputs](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/2143066-synchronizeinputs)Added [CIImageProcessorOutput](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput)Added [CIImageProcessorOutput.baseAddress](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639626-baseaddress)Added [CIImageProcessorOutput.bytesPerRow](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639635-bytesperrow)Added [CIImageProcessorOutput.format](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639628-format)Added [CIImageProcessorOutput.metalCommandBuffer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639641-metalcommandbuffer)Added [CIImageProcessorOutput.metalTexture](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639631-metaltexture)Added [CIImageProcessorOutput.pixelBuffer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639647-pixelbuffer)Added [CIImageProcessorOutput.region](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639629-region)Added [CIImageProcessorOutput.surface](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/1639627-surface)

#### CIImageProvider.h

Removed #def CI_ARRAYRemoved #def CI_DICTIONARY

#### CIKernel.h

Removed #def CI_ARRAYRemoved #def CI_DICTIONARY

#### CIRAWFilter.h

Added [+[CIFilter filterWithCVPixelBuffer:properties:options:]](https://developer.apple.com/documentation/coreimage/cifilter/2138288-filterwithcvpixelbuffer)Added [kCIInputBaselineExposureKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/2202263-baselineexposure)Added [kCIInputDisableGamutMapKey](https://developer.apple.com/documentation/coreimage/kciinputdisablegamutmapkey)

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
