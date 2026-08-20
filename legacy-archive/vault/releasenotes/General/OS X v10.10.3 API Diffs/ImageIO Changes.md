---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/ImageIO.html
archived_at: '2026-07-18T02:52:32.048468Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# ImageIO Changes

## ImageIO

Modified CGImageDestinationAddImage(CGImageDestination!, CGImage!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageDestinationAddImageAndMetadata(CGImageDestination!, CGImage!, CGImageMetadata!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGImageDestinationAddImageFromSource(CGImageDestination!, CGImageSource!, Int, CFDictionary!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageDestinationAddImageFromSource(_ idst: CGImageDestination!, _ isrc: CGImageSource!, _ index: UInt, _ properties: CFDictionary!) ``` | OS X 10.10 |
| To | ``` func CGImageDestinationAddImageFromSource(_ idst: CGImageDestination!, _ isrc: CGImageSource!, _ index: Int, _ properties: CFDictionary!) ``` | OS X 10.4 |

Modified CGImageDestinationCopyImageSource(CGImageDestination!, CGImageSource!, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageDestinationCopyImageSource(_ idst: CGImageDestination!, _ isrc: CGImageSource!, _ options: CFDictionary!, _ err: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGImageDestinationCopyImageSource(_ idst: CGImageDestination!, _ isrc: CGImageSource!, _ options: CFDictionary!, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.8 |

Modified CGImageDestinationCopyTypeIdentifiers() -> CFArray!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageDestinationCopyTypeIdentifiers() -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func CGImageDestinationCopyTypeIdentifiers() -> CFArray! ``` | OS X 10.4 |

Modified CGImageDestinationCreateWithData(CFMutableData!, CFString!, Int, CFDictionary!) -> CGImageDestination!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageDestinationCreateWithData(_ data: CFMutableData!, _ type: CFString!, _ count: UInt, _ options: CFDictionary!) -> Unmanaged<CGImageDestination>! ``` | OS X 10.10 |
| To | ``` func CGImageDestinationCreateWithData(_ data: CFMutableData!, _ type: CFString!, _ count: Int, _ options: CFDictionary!) -> CGImageDestination! ``` | OS X 10.4 |

Modified CGImageDestinationCreateWithDataConsumer(CGDataConsumer!, CFString!, Int, CFDictionary!) -> CGImageDestination!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageDestinationCreateWithDataConsumer(_ consumer: CGDataConsumer!, _ type: CFString!, _ count: UInt, _ options: CFDictionary!) -> Unmanaged<CGImageDestination>! ``` | OS X 10.10 |
| To | ``` func CGImageDestinationCreateWithDataConsumer(_ consumer: CGDataConsumer!, _ type: CFString!, _ count: Int, _ options: CFDictionary!) -> CGImageDestination! ``` | OS X 10.4 |

Modified CGImageDestinationCreateWithURL(CFURL!, CFString!, Int, CFDictionary!) -> CGImageDestination!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageDestinationCreateWithURL(_ url: CFURL!, _ type: CFString!, _ count: UInt, _ options: CFDictionary!) -> Unmanaged<CGImageDestination>! ``` | OS X 10.10 |
| To | ``` func CGImageDestinationCreateWithURL(_ url: CFURL!, _ type: CFString!, _ count: Int, _ options: CFDictionary!) -> CGImageDestination! ``` | OS X 10.4 |

Modified CGImageDestinationFinalize(CGImageDestination!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageDestinationGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageDestinationSetProperties(CGImageDestination!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageMetadataCopyStringValueWithPath(CGImageMetadata!, CGImageMetadataTag!, CFString!) -> CFString!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataCopyStringValueWithPath(_ metadata: CGImageMetadata!, _ parent: CGImageMetadataTag!, _ path: CFString!) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataCopyStringValueWithPath(_ metadata: CGImageMetadata!, _ parent: CGImageMetadataTag!, _ path: CFString!) -> CFString! ``` | OS X 10.8 |

Modified CGImageMetadataCopyTagMatchingImageProperty(CGImageMetadata!, CFString!, CFString!) -> CGImageMetadataTag!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataCopyTagMatchingImageProperty(_ metadata: CGImageMetadata!, _ dictionaryName: CFString!, _ propertyName: CFString!) -> Unmanaged<CGImageMetadataTag>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataCopyTagMatchingImageProperty(_ metadata: CGImageMetadata!, _ dictionaryName: CFString!, _ propertyName: CFString!) -> CGImageMetadataTag! ``` | OS X 10.8 |

Modified CGImageMetadataCopyTagWithPath(CGImageMetadata!, CGImageMetadataTag!, CFString!) -> CGImageMetadataTag!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataCopyTagWithPath(_ metadata: CGImageMetadata!, _ parent: CGImageMetadataTag!, _ path: CFString!) -> Unmanaged<CGImageMetadataTag>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataCopyTagWithPath(_ metadata: CGImageMetadata!, _ parent: CGImageMetadataTag!, _ path: CFString!) -> CGImageMetadataTag! ``` | OS X 10.8 |

Modified CGImageMetadataCopyTags(CGImageMetadata!) -> CFArray!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataCopyTags(_ metadata: CGImageMetadata!) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataCopyTags(_ metadata: CGImageMetadata!) -> CFArray! ``` | OS X 10.8 |

Modified CGImageMetadataCreateFromXMPData(CFData!) -> CGImageMetadata!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataCreateFromXMPData(_ data: CFData!) -> Unmanaged<CGImageMetadata>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataCreateFromXMPData(_ data: CFData!) -> CGImageMetadata! ``` | OS X 10.8 |

Modified CGImageMetadataCreateMutable() -> CGMutableImageMetadata!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataCreateMutable() -> Unmanaged<CGMutableImageMetadata>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataCreateMutable() -> CGMutableImageMetadata! ``` | OS X 10.8 |

Modified CGImageMetadataCreateMutableCopy(CGImageMetadata!) -> CGMutableImageMetadata!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataCreateMutableCopy(_ metadata: CGImageMetadata!) -> Unmanaged<CGMutableImageMetadata>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataCreateMutableCopy(_ metadata: CGImageMetadata!) -> CGMutableImageMetadata! ``` | OS X 10.8 |

Modified CGImageMetadataCreateXMPData(CGImageMetadata!, CFDictionary!) -> CFData!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataCreateXMPData(_ metadata: CGImageMetadata!, _ options: CFDictionary!) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataCreateXMPData(_ metadata: CGImageMetadata!, _ options: CFDictionary!) -> CFData! ``` | OS X 10.8 |

Modified CGImageMetadataEnumerateTagsUsingBlock(CGImageMetadata!, CFString!, CFDictionary!, CGImageMetadataTagBlock!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGImageMetadataRegisterNamespaceForPrefix(CGMutableImageMetadata!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataRegisterNamespaceForPrefix(_ metadata: CGMutableImageMetadata!, _ xmlns: CFString!, _ prefix: CFString!, _ err: UnsafePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.10 |
| To | ``` func CGImageMetadataRegisterNamespaceForPrefix(_ metadata: CGMutableImageMetadata!, _ xmlns: CFString!, _ prefix: CFString!, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` | OS X 10.8 |

Modified CGImageMetadataRemoveTagWithPath(CGMutableImageMetadata!, CGImageMetadataTag!, CFString!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGImageMetadataSetTagWithPath(CGMutableImageMetadata!, CGImageMetadataTag!, CFString!, CGImageMetadataTag!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGImageMetadataSetValueMatchingImageProperty(CGMutableImageMetadata!, CFString!, CFString!, AnyObject!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGImageMetadataSetValueWithPath(CGMutableImageMetadata!, CGImageMetadataTag!, CFString!, AnyObject!) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGImageMetadataTagCopyName(CGImageMetadataTag!) -> CFString!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataTagCopyName(_ tag: CGImageMetadataTag!) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataTagCopyName(_ tag: CGImageMetadataTag!) -> CFString! ``` | OS X 10.8 |

Modified CGImageMetadataTagCopyNamespace(CGImageMetadataTag!) -> CFString!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataTagCopyNamespace(_ tag: CGImageMetadataTag!) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataTagCopyNamespace(_ tag: CGImageMetadataTag!) -> CFString! ``` | OS X 10.8 |

Modified CGImageMetadataTagCopyPrefix(CGImageMetadataTag!) -> CFString!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataTagCopyPrefix(_ tag: CGImageMetadataTag!) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataTagCopyPrefix(_ tag: CGImageMetadataTag!) -> CFString! ``` | OS X 10.8 |

Modified CGImageMetadataTagCopyQualifiers(CGImageMetadataTag!) -> CFArray!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataTagCopyQualifiers(_ tag: CGImageMetadataTag!) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataTagCopyQualifiers(_ tag: CGImageMetadataTag!) -> CFArray! ``` | OS X 10.8 |

Modified CGImageMetadataTagCopyValue(CGImageMetadataTag!) -> AnyObject!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataTagCopyValue(_ tag: CGImageMetadataTag!) -> Unmanaged<AnyObject>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataTagCopyValue(_ tag: CGImageMetadataTag!) -> AnyObject! ``` | OS X 10.8 |

Modified CGImageMetadataTagCreate(CFString!, CFString!, CFString!, CGImageMetadataType, AnyObject!) -> CGImageMetadataTag!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageMetadataTagCreate(_ xmlns: CFString!, _ prefix: CFString!, _ name: CFString!, _ type: CGImageMetadataType, _ value: AnyObject!) -> Unmanaged<CGImageMetadataTag>! ``` | OS X 10.10 |
| To | ``` func CGImageMetadataTagCreate(_ xmlns: CFString!, _ prefix: CFString!, _ name: CFString!, _ type: CGImageMetadataType, _ value: AnyObject!) -> CGImageMetadataTag! ``` | OS X 10.8 |

Modified CGImageMetadataTagGetType(CGImageMetadataTag!) -> CGImageMetadataType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGImageMetadataTagGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified CGImageSourceCopyMetadataAtIndex(CGImageSource!, Int, CFDictionary!) -> CGImageMetadata!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceCopyMetadataAtIndex(_ isrc: CGImageSource!, _ index: UInt, _ options: CFDictionary!) -> Unmanaged<CGImageMetadata>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceCopyMetadataAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CGImageMetadata! ``` | OS X 10.8 |

Modified CGImageSourceCopyProperties(CGImageSource!, CFDictionary!) -> CFDictionary!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceCopyProperties(_ isrc: CGImageSource!, _ options: CFDictionary!) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceCopyProperties(_ isrc: CGImageSource!, _ options: CFDictionary!) -> CFDictionary! ``` | OS X 10.4 |

Modified CGImageSourceCopyPropertiesAtIndex(CGImageSource!, Int, CFDictionary!) -> CFDictionary!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceCopyPropertiesAtIndex(_ isrc: CGImageSource!, _ index: UInt, _ options: CFDictionary!) -> Unmanaged<CFDictionary>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceCopyPropertiesAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CFDictionary! ``` | OS X 10.4 |

Modified CGImageSourceCopyTypeIdentifiers() -> CFArray!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceCopyTypeIdentifiers() -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceCopyTypeIdentifiers() -> CFArray! ``` | OS X 10.4 |

Modified CGImageSourceCreateImageAtIndex(CGImageSource!, Int, CFDictionary!) -> CGImage!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceCreateImageAtIndex(_ isrc: CGImageSource!, _ index: UInt, _ options: CFDictionary!) -> Unmanaged<CGImage>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceCreateImageAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CGImage! ``` | OS X 10.4 |

Modified CGImageSourceCreateIncremental(CFDictionary!) -> CGImageSource!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceCreateIncremental(_ options: CFDictionary!) -> Unmanaged<CGImageSource>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceCreateIncremental(_ options: CFDictionary!) -> CGImageSource! ``` | OS X 10.4 |

Modified CGImageSourceCreateThumbnailAtIndex(CGImageSource!, Int, CFDictionary!) -> CGImage!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceCreateThumbnailAtIndex(_ isrc: CGImageSource!, _ index: UInt, _ options: CFDictionary!) -> Unmanaged<CGImage>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceCreateThumbnailAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CGImage! ``` | OS X 10.4 |

Modified CGImageSourceCreateWithData(CFData!, CFDictionary!) -> CGImageSource!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceCreateWithData(_ data: CFData!, _ options: CFDictionary!) -> Unmanaged<CGImageSource>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceCreateWithData(_ data: CFData!, _ options: CFDictionary!) -> CGImageSource! ``` | OS X 10.4 |

Modified CGImageSourceCreateWithDataProvider(CGDataProvider!, CFDictionary!) -> CGImageSource!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceCreateWithDataProvider(_ provider: CGDataProvider!, _ options: CFDictionary!) -> Unmanaged<CGImageSource>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceCreateWithDataProvider(_ provider: CGDataProvider!, _ options: CFDictionary!) -> CGImageSource! ``` | OS X 10.4 |

Modified CGImageSourceCreateWithURL(CFURL!, CFDictionary!) -> CGImageSource!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceCreateWithURL(_ url: CFURL!, _ options: CFDictionary!) -> Unmanaged<CGImageSource>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceCreateWithURL(_ url: CFURL!, _ options: CFDictionary!) -> CGImageSource! ``` | OS X 10.4 |

Modified CGImageSourceGetCount(CGImageSource!) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceGetCount(_ isrc: CGImageSource!) -> UInt ``` | OS X 10.10 |
| To | ``` func CGImageSourceGetCount(_ isrc: CGImageSource!) -> Int ``` | OS X 10.4 |

Modified CGImageSourceGetStatus(CGImageSource!) -> CGImageSourceStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageSourceGetStatusAtIndex(CGImageSource!, Int) -> CGImageSourceStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceGetStatusAtIndex(_ isrc: CGImageSource!, _ index: UInt) -> CGImageSourceStatus ``` | OS X 10.10 |
| To | ``` func CGImageSourceGetStatusAtIndex(_ isrc: CGImageSource!, _ index: Int) -> CGImageSourceStatus ``` | OS X 10.4 |

Modified CGImageSourceGetType(CGImageSource!) -> CFString!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceGetType(_ isrc: CGImageSource!) -> Unmanaged<CFString>! ``` | OS X 10.10 |
| To | ``` func CGImageSourceGetType(_ isrc: CGImageSource!) -> CFString! ``` | OS X 10.4 |

Modified CGImageSourceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageSourceRemoveCacheAtIndex(CGImageSource!, Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CGImageSourceRemoveCacheAtIndex(_ isrc: CGImageSource!, _ index: UInt) ``` | OS X 10.10 |
| To | ``` func CGImageSourceRemoveCacheAtIndex(_ isrc: CGImageSource!, _ index: Int) ``` | OS X 10.9 |

Modified CGImageSourceUpdateData(CGImageSource!, CFData!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CGImageSourceUpdateDataProvider(CGImageSource!, CGDataProvider!, Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageDestinationBackgroundColor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageDestinationDateTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageDestinationLossyCompressionQuality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageDestinationMergeMetadata

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageDestinationMetadata

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageDestinationOrientation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataEnumerateRecursively

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataNamespaceDublinCore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataNamespaceExif

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataNamespaceExifAux

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataNamespaceExifEX

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImageMetadataNamespaceIPTCCore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataNamespacePhotoshop

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataNamespaceTIFF

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataNamespaceXMPBasic

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataNamespaceXMPRights

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataPrefixDublinCore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataPrefixExif

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataPrefixExifAux

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataPrefixExifEX

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImageMetadataPrefixIPTCCore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataPrefixPhotoshop

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataPrefixTIFF

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataPrefixXMPBasic

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataPrefixXMPRights

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageMetadataShouldExcludeXMP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCGImageProperty8BIMDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageProperty8BIMLayerNames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyCIFFCameraSerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFContinuousDrive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyCIFFFirmware

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFFlashExposureComp

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFFocusMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFImageFileName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFImageName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFImageSerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFLensMaxMM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFLensMinMM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFLensModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFMeasuredEV

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFMeteringMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFOwnerName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFRecordID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFReleaseMethod

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFReleaseTiming

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFSelfTimingTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFShootingMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyCIFFWhiteBalanceIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyColorModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyColorModelCMYK

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyColorModelGray

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyColorModelLab

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyColorModelRGB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyDNGBackwardVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyDNGCameraSerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyDNGDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyDNGLensInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyDNGLocalizedCameraModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyDNGUniqueCameraModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyDNGVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyDPIHeight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyDPIWidth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyDepth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifApertureValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifAuxDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyExifAuxFirmware

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyExifAuxFlashCompensation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyExifAuxImageNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyExifAuxLensID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyExifAuxLensInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyExifAuxLensModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyExifAuxLensSerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyExifAuxOwnerName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyExifAuxSerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyExifBodySerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyExifBrightnessValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifCFAPattern

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifCameraOwnerName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyExifColorSpace

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifComponentsConfiguration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifCompressedBitsPerPixel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifContrast

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifCustomRendered

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifDateTimeDigitized

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifDateTimeOriginal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifDeviceSettingDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifDigitalZoomRatio

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifExposureBiasValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifExposureIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifExposureMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifExposureProgram

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifExposureTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifFNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifFileSource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifFlash

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifFlashEnergy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifFlashPixVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifFocalLenIn35mmFilm

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifFocalLength

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifFocalPlaneResolutionUnit

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifFocalPlaneXResolution

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifFocalPlaneYResolution

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifGainControl

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifGamma

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifISOSpeed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImagePropertyExifISOSpeedLatitudeyyy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImagePropertyExifISOSpeedLatitudezzz

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImagePropertyExifISOSpeedRatings

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifImageUniqueID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifLensMake

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyExifLensModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyExifLensSerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyExifLensSpecification

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyExifLightSource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifMakerNote

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifMaxApertureValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifMeteringMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifOECF

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifPixelXDimension

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifPixelYDimension

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifRecommendedExposureIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImagePropertyExifRelatedSoundFile

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSaturation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSceneCaptureType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSceneType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSensingMethod

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSensitivityType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImagePropertyExifSharpness

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifShutterSpeedValue

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSpatialFrequencyResponse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSpectralSensitivity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifStandardOutputSensitivity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImagePropertyExifSubjectArea

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSubjectDistRange

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSubjectDistance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSubjectLocation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSubsecTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSubsecTimeDigitized

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifSubsecTimeOrginal

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifUserComment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyExifWhiteBalance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyFileSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGIFDelayTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGIFDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGIFHasGlobalColorMap

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGIFImageColorMap

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGIFLoopCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGIFUnclampedDelayTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyGPSAltitude

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSAltitudeRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSAreaInformation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDOP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDateStamp

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDestBearing

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDestBearingRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDestDistance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDestDistanceRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDestLatitude

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDestLatitudeRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDestLongitude

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDestLongitudeRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSDifferental

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSImgDirection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSImgDirectionRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSLatitude

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSLatitudeRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSLongitude

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSLongitudeRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSMapDatum

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSMeasureMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSProcessingMethod

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSSatellites

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSSpeed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSSpeedRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSTimeStamp

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSTrack

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSTrackRef

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyGPSVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyHasAlpha

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCActionAdvised

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCByline

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCBylineTitle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCCaptionAbstract

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCCategory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCCity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCContact

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCContactInfoAddress

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCContactInfoCity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCContactInfoCountry

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCContactInfoEmails

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCContactInfoPhones

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCContactInfoPostalCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCContactInfoStateProvince

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCContactInfoWebURLs

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCContentLocationCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCContentLocationName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCCopyrightNotice

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCCountryPrimaryLocationCode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCCountryPrimaryLocationName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCCreatorContactInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCCredit

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCDateCreated

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCDigitalCreationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCDigitalCreationTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCEditStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCEditorialUpdate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCExpirationDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCExpirationTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCFixtureIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCHeadline

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCImageOrientation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCImageType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCKeywords

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCLanguageIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCObjectAttributeReference

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCObjectCycle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCObjectName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCObjectTypeReference

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCOriginalTransmissionReference

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCOriginatingProgram

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCProgramVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCProvinceState

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCReferenceDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCReferenceNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCReferenceService

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCReleaseDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCReleaseTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCRightsUsageTerms

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCScene

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCGImagePropertyIPTCSource

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCSpecialInstructions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCStarRating

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCSubLocation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCSubjectReference

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCSupplementalCategory

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCTimeCreated

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCUrgency

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIPTCWriterEditor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIsFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyIsIndexed

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyJFIFDensityUnit

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyJFIFDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyJFIFIsProgressive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyJFIFVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyJFIFXDensity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyJFIFYDensity

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyMakerCanonAspectRatioInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerCanonCameraSerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerCanonContinuousDrive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerCanonDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerCanonFirmware

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerCanonFlashExposureComp

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerCanonImageSerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerCanonLensModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerCanonOwnerName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerFujiDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerMinoltaDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonCameraSerialNumber

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonColorMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonDigitalZoom

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonFlashExposureComp

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonFlashSetting

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonFocusDistance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonFocusMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonISOSelection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonISOSetting

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonImageAdjustment

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonLensAdapter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonLensInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonLensType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonQuality

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonSharpenMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonShootingMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonShutterCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerNikonWhiteBalanceMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerOlympusDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyMakerPentaxDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCGImagePropertyOpenEXRAspectRatio

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImagePropertyOpenEXRDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImagePropertyOrientation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyPNGAuthor

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyPNGChromaticities

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyPNGCopyright

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyPNGCreationTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyPNGDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyPNGDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyPNGGamma

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyPNGInterlaceType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyPNGModificationTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyPNGSoftware

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyPNGTitle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCGImagePropertyPNGXPixelsPerMeter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyPNGYPixelsPerMeter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyPNGsRGBIntent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyPixelHeight

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyPixelWidth

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyProfileName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyRawDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFArtist

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFCompression

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFCopyright

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFDateTime

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFDictionary

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFDocumentName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFHostComputer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFImageDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFMake

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFModel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFOrientation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFPhotometricInterpretation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFPrimaryChromaticities

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFResolutionUnit

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFSoftware

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFTransferFunction

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFWhitePoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFXResolution

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImagePropertyTIFFYResolution

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageSourceCreateThumbnailFromImageAlways

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageSourceCreateThumbnailFromImageIfAbsent

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageSourceCreateThumbnailWithTransform

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageSourceShouldAllowFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageSourceShouldCache

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageSourceShouldCacheImmediately

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCGImageSourceThumbnailMaxPixelSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCGImageSourceTypeIdentifierHint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

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
