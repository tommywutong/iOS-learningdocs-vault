---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/VideoToolbox.html
archived_at: '2026-07-18T02:53:14.661759Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# VideoToolbox Changes for Objective-C

### VideoToolbox

#### VTCompressionSession.h

Added [VTCompressionOutputHandler](https://developer.apple.com/documentation/videotoolbox/vtcompressionoutputhandler)Added [VTCompressionSessionEncodeFrameWithOutputHandler()](https://developer.apple.com/documentation/videotoolbox/1428281-vtcompressionsessionencodeframew)Modified [VTCompressionSessionBeginPass()](https://developer.apple.com/documentation/videotoolbox/1428289-vtcompressionsessionbeginpass)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTCompressionSessionBeginPass (     VTCompressionSessionRef session,     VTCompressionSessionOptionFlags beginPassFlags,     uint32_t *reserved ); ``` |
| To | ``` OSStatus VTCompressionSessionBeginPass (     VTCompressionSessionRef _Nonnull session,     VTCompressionSessionOptionFlags beginPassFlags,     uint32_t * _Nullable reserved ); ``` |

Modified [VTCompressionSessionCompleteFrames()](https://developer.apple.com/documentation/videotoolbox/1428303-vtcompressionsessioncompletefram)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTCompressionSessionCompleteFrames (     VTCompressionSessionRef session,     CMTime completeUntilPresentationTimeStamp ); ``` |
| To | ``` OSStatus VTCompressionSessionCompleteFrames (     VTCompressionSessionRef _Nonnull session,     CMTime completeUntilPresentationTimeStamp ); ``` |

Modified [VTCompressionSessionCreate()](https://developer.apple.com/documentation/videotoolbox/1428285-vtcompressionsessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTCompressionSessionCreate (     CFAllocatorRef allocator,     int32_t width,     int32_t height,     CMVideoCodecType codecType,     CFDictionaryRef encoderSpecification,     CFDictionaryRef sourceImageBufferAttributes,     CFAllocatorRef compressedDataAllocator,     VTCompressionOutputCallback outputCallback,     void *outputCallbackRefCon,     VTCompressionSessionRef *compressionSessionOut ); ``` |
| To | ``` OSStatus VTCompressionSessionCreate (     CFAllocatorRef _Nullable allocator,     int32_t width,     int32_t height,     CMVideoCodecType codecType,     CFDictionaryRef _Nullable encoderSpecification,     CFDictionaryRef _Nullable sourceImageBufferAttributes,     CFAllocatorRef _Nullable compressedDataAllocator,     VTCompressionOutputCallback _Nullable outputCallback,     void * _Nullable outputCallbackRefCon,     VTCompressionSessionRef  _Nullable * _Nonnull compressionSessionOut ); ``` |

Modified [VTCompressionSessionEncodeFrame()](https://developer.apple.com/documentation/videotoolbox/1428287-vtcompressionsessionencodeframe)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTCompressionSessionEncodeFrame (     VTCompressionSessionRef session,     CVImageBufferRef imageBuffer,     CMTime presentationTimeStamp,     CMTime duration,     CFDictionaryRef frameProperties,     void *sourceFrameRefCon,     VTEncodeInfoFlags *infoFlagsOut ); ``` |
| To | ``` OSStatus VTCompressionSessionEncodeFrame (     VTCompressionSessionRef _Nonnull session,     CVImageBufferRef _Nonnull imageBuffer,     CMTime presentationTimeStamp,     CMTime duration,     CFDictionaryRef _Nullable frameProperties,     void * _Nullable sourceFrameRefCon,     VTEncodeInfoFlags * _Nullable infoFlagsOut ); ``` |

Modified [VTCompressionSessionEndPass()](https://developer.apple.com/documentation/videotoolbox/1428313-vtcompressionsessionendpass)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTCompressionSessionEndPass (     VTCompressionSessionRef session,     Boolean *furtherPassesRequestedOut,     uint32_t *reserved ); ``` |
| To | ``` OSStatus VTCompressionSessionEndPass (     VTCompressionSessionRef _Nonnull session,     Boolean * _Nullable furtherPassesRequestedOut,     uint32_t * _Nullable reserved ); ``` |

Modified [VTCompressionSessionGetPixelBufferPool()](https://developer.apple.com/documentation/videotoolbox/1428293-vtcompressionsessiongetpixelbuff)

|  | Declaration |
| --- | --- |
| From | ``` CVPixelBufferPoolRef VTCompressionSessionGetPixelBufferPool (     VTCompressionSessionRef session ); ``` |
| To | ``` CVPixelBufferPoolRef _Nullable VTCompressionSessionGetPixelBufferPool (     VTCompressionSessionRef _Nonnull session ); ``` |

Modified [VTCompressionSessionGetTimeRangesForNextPass()](https://developer.apple.com/documentation/videotoolbox/1428311-vtcompressionsessiongettimerange)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTCompressionSessionGetTimeRangesForNextPass (     VTCompressionSessionRef session,     CMItemCount *timeRangeCountOut,     const CMTimeRange **timeRangeArrayOut ); ``` |
| To | ``` OSStatus VTCompressionSessionGetTimeRangesForNextPass (     VTCompressionSessionRef _Nonnull session,     CMItemCount * _Nonnull timeRangeCountOut,     const CMTimeRange * _Nullable * _Nonnull timeRangeArrayOut ); ``` |

Modified [VTCompressionSessionInvalidate()](https://developer.apple.com/documentation/videotoolbox/1428295-vtcompressionsessioninvalidate)

|  | Declaration |
| --- | --- |
| From | ``` void VTCompressionSessionInvalidate (     VTCompressionSessionRef session ); ``` |
| To | ``` void VTCompressionSessionInvalidate (     VTCompressionSessionRef _Nonnull session ); ``` |

Modified [VTCompressionSessionPrepareToEncodeFrames()](https://developer.apple.com/documentation/videotoolbox/1428283-vtcompressionsessionpreparetoenc)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTCompressionSessionPrepareToEncodeFrames (     VTCompressionSessionRef session ); ``` |
| To | ``` OSStatus VTCompressionSessionPrepareToEncodeFrames (     VTCompressionSessionRef _Nonnull session ); ``` |

#### VTDecompressionSession.h

Added [VTDecompressionOutputHandler](https://developer.apple.com/documentation/videotoolbox/vtdecompressionoutputhandler)Added [VTDecompressionSessionDecodeFrameWithOutputHandler()](https://developer.apple.com/documentation/videotoolbox/1536067-vtdecompressionsessiondecodefram)Modified [VTDecompressionSessionCanAcceptFormatDescription()](https://developer.apple.com/documentation/videotoolbox/1536112-vtdecompressionsessioncanacceptf)

|  | Declaration |
| --- | --- |
| From | ``` Boolean VTDecompressionSessionCanAcceptFormatDescription (     VTDecompressionSessionRef session,     CMFormatDescriptionRef newFormatDesc ); ``` |
| To | ``` Boolean VTDecompressionSessionCanAcceptFormatDescription (     VTDecompressionSessionRef _Nonnull session,     CMFormatDescriptionRef _Nonnull newFormatDesc ); ``` |

Modified [VTDecompressionSessionCopyBlackPixelBuffer()](https://developer.apple.com/documentation/videotoolbox/1536140-vtdecompressionsessioncopyblackp)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTDecompressionSessionCopyBlackPixelBuffer (     VTDecompressionSessionRef session,     CVPixelBufferRef *pixelBufferOut ); ``` |
| To | ``` OSStatus VTDecompressionSessionCopyBlackPixelBuffer (     VTDecompressionSessionRef _Nonnull session,     CVPixelBufferRef  _Nullable * _Nonnull pixelBufferOut ); ``` |

Modified [VTDecompressionSessionCreate()](https://developer.apple.com/documentation/videotoolbox/1536134-vtdecompressionsessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTDecompressionSessionCreate (     CFAllocatorRef allocator,     CMVideoFormatDescriptionRef videoFormatDescription,     CFDictionaryRef videoDecoderSpecification,     CFDictionaryRef destinationImageBufferAttributes,     const VTDecompressionOutputCallbackRecord *outputCallback,     VTDecompressionSessionRef *decompressionSessionOut ); ``` |
| To | ``` OSStatus VTDecompressionSessionCreate (     CFAllocatorRef _Nullable allocator,     CMVideoFormatDescriptionRef _Nonnull videoFormatDescription,     CFDictionaryRef _Nullable videoDecoderSpecification,     CFDictionaryRef _Nullable destinationImageBufferAttributes,     const VTDecompressionOutputCallbackRecord * _Nullable outputCallback,     VTDecompressionSessionRef  _Nullable * _Nonnull decompressionSessionOut ); ``` |

Modified [VTDecompressionSessionDecodeFrame()](https://developer.apple.com/documentation/videotoolbox/1536071-vtdecompressionsessiondecodefram)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTDecompressionSessionDecodeFrame (     VTDecompressionSessionRef session,     CMSampleBufferRef sampleBuffer,     VTDecodeFrameFlags decodeFlags,     void *sourceFrameRefCon,     VTDecodeInfoFlags *infoFlagsOut ); ``` |
| To | ``` OSStatus VTDecompressionSessionDecodeFrame (     VTDecompressionSessionRef _Nonnull session,     CMSampleBufferRef _Nonnull sampleBuffer,     VTDecodeFrameFlags decodeFlags,     void * _Nullable sourceFrameRefCon,     VTDecodeInfoFlags * _Nullable infoFlagsOut ); ``` |

Modified [VTDecompressionSessionFinishDelayedFrames()](https://developer.apple.com/documentation/videotoolbox/1536101-vtdecompressionsessionfinishdela)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTDecompressionSessionFinishDelayedFrames (     VTDecompressionSessionRef session ); ``` |
| To | ``` OSStatus VTDecompressionSessionFinishDelayedFrames (     VTDecompressionSessionRef _Nonnull session ); ``` |

Modified [VTDecompressionSessionInvalidate()](https://developer.apple.com/documentation/videotoolbox/1536093-vtdecompressionsessioninvalidate)

|  | Declaration |
| --- | --- |
| From | ``` void VTDecompressionSessionInvalidate (     VTDecompressionSessionRef session ); ``` |
| To | ``` void VTDecompressionSessionInvalidate (     VTDecompressionSessionRef _Nonnull session ); ``` |

Modified [VTDecompressionSessionWaitForAsynchronousFrames()](https://developer.apple.com/documentation/videotoolbox/1536066-vtdecompressionsessionwaitforasy)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTDecompressionSessionWaitForAsynchronousFrames (     VTDecompressionSessionRef session ); ``` |
| To | ``` OSStatus VTDecompressionSessionWaitForAsynchronousFrames (     VTDecompressionSessionRef _Nonnull session ); ``` |

#### VTFrameSilo.h

Modified [VTFrameSiloAddSampleBuffer()](https://developer.apple.com/documentation/videotoolbox/1474240-vtframesiloaddsamplebuffer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTFrameSiloAddSampleBuffer (     VTFrameSiloRef silo,     CMSampleBufferRef sampleBuffer ); ``` |
| To | ``` OSStatus VTFrameSiloAddSampleBuffer (     VTFrameSiloRef _Nonnull silo,     CMSampleBufferRef _Nonnull sampleBuffer ); ``` |

Modified [VTFrameSiloCallBlockForEachSampleBuffer()](https://developer.apple.com/documentation/videotoolbox/1474252-vtframesilocallblockforeachsampl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTFrameSiloCallBlockForEachSampleBuffer (     VTFrameSiloRef silo,     CMTimeRange timeRange,     OSStatus (^handler)(CMSampleBufferRef sampleBuffer) ); ``` |
| To | ``` OSStatus VTFrameSiloCallBlockForEachSampleBuffer (     VTFrameSiloRef _Nonnull silo,     CMTimeRange timeRange,     OSStatus (^ _Nonnullhandler)(CMSampleBufferRef _Nonnull sampleBuffer) ); ``` |

Modified [VTFrameSiloCallFunctionForEachSampleBuffer()](https://developer.apple.com/documentation/videotoolbox/1474246-vtframesilocallfunctionforeachsa)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTFrameSiloCallFunctionForEachSampleBuffer (     VTFrameSiloRef silo,     CMTimeRange timeRange,     void *callbackInfo,     OSStatus (*callback)(void *callbackInfo, CMSampleBufferRef sampleBuffer) ); ``` |
| To | ``` OSStatus VTFrameSiloCallFunctionForEachSampleBuffer (     VTFrameSiloRef _Nonnull silo,     CMTimeRange timeRange,     void * _Nullable callbackInfo,     OSStatus (* _Nonnullcallback)(void * _Nullable callbackInfo, CMSampleBufferRef _Nonnull sampleBuffer) ); ``` |

Modified [VTFrameSiloCreate()](https://developer.apple.com/documentation/videotoolbox/1474250-vtframesilocreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTFrameSiloCreate (     CFAllocatorRef allocator,     CFURLRef fileURL,     CMTimeRange timeRange,     CFDictionaryRef options,     VTFrameSiloRef *siloOut ); ``` |
| To | ``` OSStatus VTFrameSiloCreate (     CFAllocatorRef _Nullable allocator,     CFURLRef _Nullable fileURL,     CMTimeRange timeRange,     CFDictionaryRef _Nullable options,     VTFrameSiloRef  _Nullable * _Nonnull siloOut ); ``` |

Modified [VTFrameSiloGetProgressOfCurrentPass()](https://developer.apple.com/documentation/videotoolbox/1474248-vtframesilogetprogressofcurrentp)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTFrameSiloGetProgressOfCurrentPass (     VTFrameSiloRef silo,     Float32 *progressOut ); ``` |
| To | ``` OSStatus VTFrameSiloGetProgressOfCurrentPass (     VTFrameSiloRef _Nonnull silo,     Float32 * _Nonnull progressOut ); ``` |

Modified [VTFrameSiloSetTimeRangesForNextPass()](https://developer.apple.com/documentation/videotoolbox/1474238-vtframesilosettimerangesfornextp)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTFrameSiloSetTimeRangesForNextPass (     VTFrameSiloRef silo,     CMItemCount timeRangeCount,     const CMTimeRange *timeRangeArray ); ``` |
| To | ``` OSStatus VTFrameSiloSetTimeRangesForNextPass (     VTFrameSiloRef _Nonnull silo,     CMItemCount timeRangeCount,     const CMTimeRange * _Nonnull timeRangeArray ); ``` |

#### VTMultiPassStorage.h

Modified [VTMultiPassStorageClose()](https://developer.apple.com/documentation/videotoolbox/1536110-vtmultipassstorageclose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTMultiPassStorageClose (     VTMultiPassStorageRef multiPassStorage ); ``` |
| To | ``` OSStatus VTMultiPassStorageClose (     VTMultiPassStorageRef _Nonnull multiPassStorage ); ``` |

Modified [VTMultiPassStorageCreate()](https://developer.apple.com/documentation/videotoolbox/1536088-vtmultipassstoragecreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTMultiPassStorageCreate (     CFAllocatorRef allocator,     CFURLRef fileURL,     CMTimeRange timeRange,     CFDictionaryRef options,     VTMultiPassStorageRef *multiPassStorageOut ); ``` |
| To | ``` OSStatus VTMultiPassStorageCreate (     CFAllocatorRef _Nullable allocator,     CFURLRef _Nullable fileURL,     CMTimeRange timeRange,     CFDictionaryRef _Nullable options,     VTMultiPassStorageRef  _Nullable * _Nonnull multiPassStorageOut ); ``` |

#### VTPixelTransferSession.h

Modified [VTPixelTransferSessionCreate()](https://developer.apple.com/documentation/videotoolbox/1503546-vtpixeltransfersessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTPixelTransferSessionCreate (     CFAllocatorRef allocator,     VTPixelTransferSessionRef *pixelTransferSessionOut ); ``` |
| To | ``` OSStatus VTPixelTransferSessionCreate (     CFAllocatorRef _Nullable allocator,     VTPixelTransferSessionRef  _Nullable * _Nonnull pixelTransferSessionOut ); ``` |

Modified [VTPixelTransferSessionInvalidate()](https://developer.apple.com/documentation/videotoolbox/1503544-vtpixeltransfersessioninvalidate)

|  | Declaration |
| --- | --- |
| From | ``` void VTPixelTransferSessionInvalidate (     VTPixelTransferSessionRef session ); ``` |
| To | ``` void VTPixelTransferSessionInvalidate (     VTPixelTransferSessionRef _Nonnull session ); ``` |

Modified [VTPixelTransferSessionTransferImage()](https://developer.apple.com/documentation/videotoolbox/1503548-vtpixeltransfersessiontransferim)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTPixelTransferSessionTransferImage (     VTPixelTransferSessionRef session,     CVPixelBufferRef sourceBuffer,     CVPixelBufferRef destinationBuffer ); ``` |
| To | ``` OSStatus VTPixelTransferSessionTransferImage (     VTPixelTransferSessionRef _Nonnull session,     CVPixelBufferRef _Nonnull sourceBuffer,     CVPixelBufferRef _Nonnull destinationBuffer ); ``` |

#### VTSession.h

Modified [VTSessionCopyProperty()](https://developer.apple.com/documentation/videotoolbox/1536169-vtsessioncopyproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTSessionCopyProperty (     VTSessionRef session,     CFStringRef propertyKey,     CFAllocatorRef allocator,     void *propertyValueOut ); ``` |
| To | ``` OSStatus VTSessionCopyProperty (     VTSessionRef _Nonnull session,     CFStringRef _Nonnull propertyKey,     CFAllocatorRef _Nullable allocator,     void * _Nullable propertyValueOut ); ``` |

Modified [VTSessionCopySerializableProperties()](https://developer.apple.com/documentation/videotoolbox/1536142-vtsessioncopyserializablepropert)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTSessionCopySerializableProperties (     VTSessionRef session,     CFAllocatorRef allocator,     CFDictionaryRef *dictionaryOut ); ``` |
| To | ``` OSStatus VTSessionCopySerializableProperties (     VTSessionRef _Nonnull session,     CFAllocatorRef _Nullable allocator,     CFDictionaryRef  _Nullable * _Nonnull dictionaryOut ); ``` |

Modified [VTSessionCopySupportedPropertyDictionary()](https://developer.apple.com/documentation/videotoolbox/1536080-vtsessioncopysupportedpropertydi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTSessionCopySupportedPropertyDictionary (     VTSessionRef session,     CFDictionaryRef *supportedPropertyDictionaryOut ); ``` |
| To | ``` OSStatus VTSessionCopySupportedPropertyDictionary (     VTSessionRef _Nonnull session,     CFDictionaryRef  _Nullable * _Nonnull supportedPropertyDictionaryOut ); ``` |

Modified [VTSessionSetProperties()](https://developer.apple.com/documentation/videotoolbox/1536153-vtsessionsetproperties)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTSessionSetProperties (     VTSessionRef session,     CFDictionaryRef propertyDictionary ); ``` |
| To | ``` OSStatus VTSessionSetProperties (     VTSessionRef _Nonnull session,     CFDictionaryRef _Nonnull propertyDictionary ); ``` |

Modified [VTSessionSetProperty()](https://developer.apple.com/documentation/videotoolbox/1536144-vtsessionsetproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTSessionSetProperty (     VTSessionRef session,     CFStringRef propertyKey,     CFTypeRef propertyValue ); ``` |
| To | ``` OSStatus VTSessionSetProperty (     VTSessionRef _Nonnull session,     CFStringRef _Nonnull propertyKey,     CFTypeRef _Nonnull propertyValue ); ``` |

#### VTUtilities.h (Added)

Added [VTCreateCGImageFromCVPixelBuffer()](https://developer.apple.com/documentation/videotoolbox/1536089-vtcreatecgimagefromcvpixelbuffer)

#### VTVideoEncoderList.h

Modified [VTCopyVideoEncoderList()](https://developer.apple.com/documentation/videotoolbox/1522108-vtcopyvideoencoderlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus VTCopyVideoEncoderList (     CFDictionaryRef options,     CFArrayRef *listOfVideoEncodersOut ); ``` |
| To | ``` OSStatus VTCopyVideoEncoderList (     CFDictionaryRef _Nullable options,     CFArrayRef  _Nullable * _Nonnull listOfVideoEncodersOut ); ``` |

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
