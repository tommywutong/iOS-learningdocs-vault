---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/ImageIO.html
archived_at: '2026-07-18T02:56:13.768108Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# ImageIO Changes

## ImageIO

Modified CGImageDestinationAddImage(CGImageDestination!, CGImage!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageDestinationAddImageAndMetadata(CGImageDestination!, CGImage!, CGImageMetadata!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageDestinationAddImageFromSource(CGImageDestination!, CGImageSource!, UInt, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageDestinationCopyImageSource(CGImageDestination!, CGImageSource!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageDestinationCopyTypeIdentifiers() -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageDestinationCreateWithData(CFMutableData!, CFString!, UInt, CFDictionary!) -> CGImageDestination!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageDestinationCreateWithDataConsumer(CGDataConsumer!, CFString!, UInt, CFDictionary!) -> CGImageDestination!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageDestinationCreateWithURL(CFURL!, CFString!, UInt, CFDictionary!) -> CGImageDestination!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageDestinationFinalize(CGImageDestination!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageDestinationGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageDestinationSetProperties(CGImageDestination!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageMetadataCopyStringValueWithPath(CGImageMetadata!, CGImageMetadataTag!, CFString!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataCopyTagMatchingImageProperty(CGImageMetadata!, CFString!, CFString!) -> CGImageMetadataTag!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataCopyTagWithPath(CGImageMetadata!, CGImageMetadataTag!, CFString!) -> CGImageMetadataTag!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataCopyTags(CGImageMetadata!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataCreateFromXMPData(CFData!) -> CGImageMetadata!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataCreateMutable() -> CGMutableImageMetadata!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataCreateMutableCopy(CGImageMetadata!) -> CGMutableImageMetadata!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataCreateXMPData(CGImageMetadata!, CFDictionary!) -> CFData!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataEnumerateTagsUsingBlock(CGImageMetadata!, CFString!, CFDictionary!, CGImageMetadataTagBlock!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataRegisterNamespaceForPrefix(CGMutableImageMetadata!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataRemoveTagWithPath(CGMutableImageMetadata!, CGImageMetadataTag!, CFString!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataSetTagWithPath(CGMutableImageMetadata!, CGImageMetadataTag!, CFString!, CGImageMetadataTag!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataSetValueMatchingImageProperty(CGMutableImageMetadata!, CFString!, CFString!, AnyObject!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataSetValueWithPath(CGMutableImageMetadata!, CGImageMetadataTag!, CFString!, AnyObject!) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataTagCopyName(CGImageMetadataTag!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataTagCopyNamespace(CGImageMetadataTag!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataTagCopyPrefix(CGImageMetadataTag!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataTagCopyQualifiers(CGImageMetadataTag!) -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataTagCopyValue(CGImageMetadataTag!) -> AnyObject!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataTagCreate(CFString!, CFString!, CFString!, CGImageMetadataType, AnyObject!) -> CGImageMetadataTag!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataTagGetType(CGImageMetadataTag!) -> CGImageMetadataType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageMetadataTagGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageSourceCopyMetadataAtIndex(CGImageSource!, UInt, CFDictionary!) -> CGImageMetadata!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageSourceCopyProperties(CGImageSource!, CFDictionary!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceCopyPropertiesAtIndex(CGImageSource!, UInt, CFDictionary!) -> CFDictionary!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceCopyTypeIdentifiers() -> CFArray!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceCreateImageAtIndex(CGImageSource!, UInt, CFDictionary!) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceCreateIncremental(CFDictionary!) -> CGImageSource!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceCreateThumbnailAtIndex(CGImageSource!, UInt, CFDictionary!) -> CGImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceCreateWithData(CFData!, CFDictionary!) -> CGImageSource!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceCreateWithDataProvider(CGDataProvider!, CFDictionary!) -> CGImageSource!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceCreateWithURL(CFURL!, CFDictionary!) -> CGImageSource!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceGetCount(CGImageSource!) -> UInt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceGetStatus(CGImageSource!) -> CGImageSourceStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceGetStatusAtIndex(CGImageSource!, UInt) -> CGImageSourceStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceGetType(CGImageSource!) -> CFString!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceRemoveCacheAtIndex(CGImageSource!, UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified CGImageSourceUpdateData(CGImageSource!, CFData!, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified CGImageSourceUpdateDataProvider(CGImageSource!, CGDataProvider!, Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageDestinationBackgroundColor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageDestinationDateTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageDestinationLossyCompressionQuality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageDestinationMergeMetadata

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageDestinationMetadata

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageDestinationOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataEnumerateRecursively

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataNamespaceDublinCore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataNamespaceExif

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataNamespaceExifAux

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataNamespaceExifEX

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataNamespaceIPTCCore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataNamespacePhotoshop

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataNamespaceTIFF

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataNamespaceXMPBasic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataNamespaceXMPRights

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataPrefixDublinCore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataPrefixExif

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataPrefixExifAux

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataPrefixExifEX

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataPrefixIPTCCore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataPrefixPhotoshop

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataPrefixTIFF

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataPrefixXMPBasic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataPrefixXMPRights

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageMetadataShouldExcludeXMP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageProperty8BIMDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageProperty8BIMLayerNames

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFCameraSerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFContinuousDrive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFFirmware

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFFlashExposureComp

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFFocusMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFImageFileName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFImageName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFImageSerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFLensMaxMM

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFLensMinMM

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFLensModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFMeasuredEV

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFMeteringMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFOwnerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFRecordID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFReleaseMethod

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFReleaseTiming

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFSelfTimingTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFShootingMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyCIFFWhiteBalanceIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyColorModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyColorModelCMYK

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyColorModelGray

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyColorModelLab

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyColorModelRGB

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyDNGBackwardVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyDNGCameraSerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyDNGDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyDNGLensInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyDNGLocalizedCameraModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyDNGUniqueCameraModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyDNGVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyDPIHeight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyDPIWidth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyDepth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifApertureValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifAuxDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifAuxFirmware

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifAuxFlashCompensation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifAuxImageNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifAuxLensID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifAuxLensInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifAuxLensModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifAuxLensSerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifAuxOwnerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifAuxSerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifBodySerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyExifBrightnessValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifCFAPattern

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifCameraOwnerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyExifColorSpace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifComponentsConfiguration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifCompressedBitsPerPixel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifContrast

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifCustomRendered

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifDateTimeDigitized

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifDateTimeOriginal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifDeviceSettingDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifDigitalZoomRatio

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifExposureBiasValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifExposureIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifExposureMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifExposureProgram

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifExposureTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifFNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifFileSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifFlash

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifFlashEnergy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifFlashPixVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifFocalLenIn35mmFilm

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifFocalLength

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifFocalPlaneResolutionUnit

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifFocalPlaneXResolution

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifFocalPlaneYResolution

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifGainControl

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifGamma

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifISOSpeed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImagePropertyExifISOSpeedLatitudeyyy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImagePropertyExifISOSpeedLatitudezzz

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImagePropertyExifISOSpeedRatings

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifImageUniqueID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifLensMake

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyExifLensModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyExifLensSerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyExifLensSpecification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyExifLightSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifMakerNote

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifMaxApertureValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifMeteringMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifOECF

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifPixelXDimension

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifPixelYDimension

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifRecommendedExposureIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImagePropertyExifRelatedSoundFile

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSaturation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSceneCaptureType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSceneType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSensingMethod

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSensitivityType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImagePropertyExifSharpness

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifShutterSpeedValue

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSpatialFrequencyResponse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSpectralSensitivity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifStandardOutputSensitivity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImagePropertyExifSubjectArea

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSubjectDistRange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSubjectDistance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSubjectLocation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSubsecTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSubsecTimeDigitized

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifSubsecTimeOrginal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifUserComment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyExifWhiteBalance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyFileSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGIFDelayTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGIFDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGIFHasGlobalColorMap

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGIFImageColorMap

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGIFLoopCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGIFUnclampedDelayTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSAltitude

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSAltitudeRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSAreaInformation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDOP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDateStamp

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDestBearing

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDestBearingRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDestDistance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDestDistanceRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDestLatitude

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDestLatitudeRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDestLongitude

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDestLongitudeRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSDifferental

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSImgDirection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSImgDirectionRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSLatitude

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSLatitudeRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSLongitude

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSLongitudeRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSMapDatum

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSMeasureMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSProcessingMethod

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSSatellites

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSSpeed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSSpeedRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSTimeStamp

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSTrack

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSTrackRef

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyGPSVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyHasAlpha

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCActionAdvised

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCByline

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCBylineTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCCaptionAbstract

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCCategory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCCity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContact

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContactInfoAddress

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContactInfoCity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContactInfoCountry

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContactInfoEmails

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContactInfoPhones

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContactInfoPostalCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContactInfoStateProvince

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContactInfoWebURLs

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContentLocationCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCContentLocationName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCCopyrightNotice

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCCountryPrimaryLocationCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCCountryPrimaryLocationName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCCreatorContactInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCCredit

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCDateCreated

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCDigitalCreationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCDigitalCreationTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCEditStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCEditorialUpdate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCExpirationDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCExpirationTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCFixtureIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCHeadline

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCImageOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCImageType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCKeywords

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCLanguageIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCObjectAttributeReference

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCObjectCycle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCObjectName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCObjectTypeReference

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCOriginalTransmissionReference

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCOriginatingProgram

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCProgramVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCProvinceState

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCReferenceDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCReferenceNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCReferenceService

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCReleaseDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCReleaseTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCRightsUsageTerms

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCScene

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCSource

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCSpecialInstructions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCStarRating

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCSubLocation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCSubjectReference

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCSupplementalCategory

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCTimeCreated

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCUrgency

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIPTCWriterEditor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIsFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyIsIndexed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyJFIFDensityUnit

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyJFIFDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyJFIFIsProgressive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyJFIFVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyJFIFXDensity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyJFIFYDensity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerAppleDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImagePropertyMakerCanonAspectRatioInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerCanonCameraSerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerCanonContinuousDrive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerCanonDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerCanonFirmware

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerCanonFlashExposureComp

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerCanonImageSerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerCanonLensModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerCanonOwnerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerFujiDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerMinoltaDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonCameraSerialNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonColorMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonDigitalZoom

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonFlashExposureComp

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonFlashSetting

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonFocusDistance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonFocusMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonISOSelection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonISOSetting

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonImageAdjustment

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonLensAdapter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonLensInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonLensType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonQuality

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonSharpenMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonShootingMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonShutterCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerNikonWhiteBalanceMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerOlympusDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyMakerPentaxDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyPNGAuthor

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyPNGChromaticities

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyPNGCopyright

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyPNGCreationTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyPNGDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyPNGDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyPNGGamma

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyPNGInterlaceType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyPNGModificationTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyPNGSoftware

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyPNGTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCGImagePropertyPNGXPixelsPerMeter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyPNGYPixelsPerMeter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyPNGsRGBIntent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyPixelHeight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyPixelWidth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyProfileName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyRawDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFCompression

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFCopyright

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFDateTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFDictionary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFDocumentName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFHostComputer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFImageDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFMake

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFModel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFOrientation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFPhotometricInterpretation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFPrimaryChromaticities

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFResolutionUnit

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFSoftware

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFTransferFunction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFWhitePoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFXResolution

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImagePropertyTIFFYResolution

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageSourceCreateThumbnailFromImageAlways

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageSourceCreateThumbnailFromImageIfAbsent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageSourceCreateThumbnailWithTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageSourceShouldAllowFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageSourceShouldCache

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageSourceShouldCacheImmediately

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCGImageSourceThumbnailMaxPixelSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCGImageSourceTypeIdentifierHint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

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
