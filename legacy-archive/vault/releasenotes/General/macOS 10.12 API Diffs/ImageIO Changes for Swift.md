---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/ImageIO.html
archived_at: '2026-07-18T02:51:27.303570Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# ImageIO Changes for Swift

### ImageIO

Added [kCGImageDestinationOptimizeColorForSharing](https://developer.apple.com/documentation/imageio/kcgimagedestinationoptimizecolorforsharing)Added [kCGImagePropertyDNGAsShotNeutral](https://developer.apple.com/documentation/imageio/kcgimagepropertydngasshotneutral)Added [kCGImagePropertyDNGAsShotWhiteXY](https://developer.apple.com/documentation/imageio/kcgimagepropertydngasshotwhitexy)Added [kCGImagePropertyDNGBaselineExposure](https://developer.apple.com/documentation/imageio/kcgimagepropertydngbaselineexposure)Added [kCGImagePropertyDNGBaselineNoise](https://developer.apple.com/documentation/imageio/kcgimagepropertydngbaselinenoise)Added [kCGImagePropertyDNGBaselineSharpness](https://developer.apple.com/documentation/imageio/kcgimagepropertydngbaselinesharpness)Added [kCGImagePropertyDNGBlackLevel](https://developer.apple.com/documentation/imageio/kcgimagepropertydngblacklevel)Added [kCGImagePropertyDNGCalibrationIlluminant1](https://developer.apple.com/documentation/imageio/kcgimagepropertydngcalibrationilluminant1)Added [kCGImagePropertyDNGCalibrationIlluminant2](https://developer.apple.com/documentation/imageio/kcgimagepropertydngcalibrationilluminant2)Added [kCGImagePropertyDNGCameraCalibration1](https://developer.apple.com/documentation/imageio/kcgimagepropertydngcameracalibration1)Added [kCGImagePropertyDNGCameraCalibration2](https://developer.apple.com/documentation/imageio/kcgimagepropertydngcameracalibration2)Added [kCGImagePropertyDNGCameraCalibrationSignature](https://developer.apple.com/documentation/imageio/kcgimagepropertydngcameracalibrationsignature)Added [kCGImagePropertyDNGColorMatrix1](https://developer.apple.com/documentation/imageio/kcgimagepropertydngcolormatrix1)Added [kCGImagePropertyDNGColorMatrix2](https://developer.apple.com/documentation/imageio/kcgimagepropertydngcolormatrix2)Added [kCGImagePropertyDNGFixVignetteRadial](https://developer.apple.com/documentation/imageio/kcgimagepropertydngfixvignetteradial)Added [kCGImagePropertyDNGNoiseProfile](https://developer.apple.com/documentation/imageio/kcgimagepropertydngnoiseprofile)Added [kCGImagePropertyDNGPrivateData](https://developer.apple.com/documentation/imageio/kcgimagepropertydngprivatedata)Added [kCGImagePropertyDNGProfileCalibrationSignature](https://developer.apple.com/documentation/imageio/kcgimagepropertydngprofilecalibrationsignature)Added [kCGImagePropertyDNGWarpFisheye](https://developer.apple.com/documentation/imageio/kcgimagepropertydngwarpfisheye)Added [kCGImagePropertyDNGWarpRectilinear](https://developer.apple.com/documentation/imageio/kcgimagepropertydngwarprectilinear)Added [kCGImagePropertyDNGWhiteLevel](https://developer.apple.com/documentation/imageio/kcgimagepropertydngwhitelevel)Modified [CGImageMetadataErrors [enum]](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors)

|  | Declaration |
| --- | --- |
| From | ``` enum CGImageMetadataErrors : Int32 {     case Unknown     case UnsupportedFormat     case BadArgument     case ConflictingArguments     case PrefixConflict } ``` |
| To | ``` enum CGImageMetadataErrors : Int32 {     case unknown     case unsupportedFormat     case badArgument     case conflictingArguments     case prefixConflict } ``` |

Modified [CGImageMetadataErrors.badArgument](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/kcgimagemetadataerrorbadargument)

|  | Declaration |
| --- | --- |
| From | ``` case BadArgument ``` |
| To | ``` case badArgument ``` |

Modified [CGImageMetadataErrors.conflictingArguments](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/kcgimagemetadataerrorconflictingarguments)

|  | Declaration |
| --- | --- |
| From | ``` case ConflictingArguments ``` |
| To | ``` case conflictingArguments ``` |

Modified [CGImageMetadataErrors.prefixConflict](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/kcgimagemetadataerrorprefixconflict)

|  | Declaration |
| --- | --- |
| From | ``` case PrefixConflict ``` |
| To | ``` case prefixConflict ``` |

Modified [CGImageMetadataErrors.unknown](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CGImageMetadataErrors.unsupportedFormat](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/kcgimagemetadataerrorunsupportedformat)

|  | Declaration |
| --- | --- |
| From | ``` case UnsupportedFormat ``` |
| To | ``` case unsupportedFormat ``` |

Modified [CGImageMetadataType [enum]](https://developer.apple.com/documentation/imageio/cgimagemetadatatype)

|  | Declaration |
| --- | --- |
| From | ``` enum CGImageMetadataType : Int32 {     case Invalid     case Default     case String     case ArrayUnordered     case ArrayOrdered     case AlternateArray     case AlternateText     case Structure } ``` |
| To | ``` enum CGImageMetadataType : Int32 {     case invalid     case `default`     case string     case arrayUnordered     case arrayOrdered     case alternateArray     case alternateText     case structure } ``` |

Modified [CGImageMetadataType.alternateArray](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypealternatearray)

|  | Declaration |
| --- | --- |
| From | ``` case AlternateArray ``` |
| To | ``` case alternateArray ``` |

Modified [CGImageMetadataType.alternateText](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/alternatetext)

|  | Declaration |
| --- | --- |
| From | ``` case AlternateText ``` |
| To | ``` case alternateText ``` |

Modified [CGImageMetadataType.arrayOrdered](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/arrayordered)

|  | Declaration |
| --- | --- |
| From | ``` case ArrayOrdered ``` |
| To | ``` case arrayOrdered ``` |

Modified [CGImageMetadataType.arrayUnordered](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypearrayunordered)

|  | Declaration |
| --- | --- |
| From | ``` case ArrayUnordered ``` |
| To | ``` case arrayUnordered ``` |

Modified [CGImageMetadataType.default](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/default)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [CGImageMetadataType.invalid](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypeinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [CGImageMetadataType.string](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/string)

|  | Declaration |
| --- | --- |
| From | ``` case String ``` |
| To | ``` case string ``` |

Modified [CGImageMetadataType.structure](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypestructure)

|  | Declaration |
| --- | --- |
| From | ``` case Structure ``` |
| To | ``` case structure ``` |

Modified [CGImagePropertyOrientation [enum]](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation)

|  | Declaration |
| --- | --- |
| From | ``` enum CGImagePropertyOrientation : UInt32 {     case Up     case UpMirrored     case Down     case DownMirrored     case LeftMirrored     case Right     case RightMirrored     case Left } ``` |
| To | ``` enum CGImagePropertyOrientation : UInt32 {     case up     case upMirrored     case down     case downMirrored     case leftMirrored     case right     case rightMirrored     case left } ``` |

Modified [CGImagePropertyOrientation.down](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/down)

|  | Declaration |
| --- | --- |
| From | ``` case Down ``` |
| To | ``` case down ``` |

Modified [CGImagePropertyOrientation.downMirrored](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/downmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case DownMirrored ``` |
| To | ``` case downMirrored ``` |

Modified [CGImagePropertyOrientation.left](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/kcgimagepropertyorientationleft)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [CGImagePropertyOrientation.leftMirrored](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/kcgimagepropertyorientationleftmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case LeftMirrored ``` |
| To | ``` case leftMirrored ``` |

Modified [CGImagePropertyOrientation.right](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/kcgimagepropertyorientationright)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [CGImagePropertyOrientation.rightMirrored](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/rightmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case RightMirrored ``` |
| To | ``` case rightMirrored ``` |

Modified [CGImagePropertyOrientation.up](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/kcgimagepropertyorientationup)

|  | Declaration |
| --- | --- |
| From | ``` case Up ``` |
| To | ``` case up ``` |

Modified [CGImagePropertyOrientation.upMirrored](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/upmirrored)

|  | Declaration |
| --- | --- |
| From | ``` case UpMirrored ``` |
| To | ``` case upMirrored ``` |

Modified [CGImageSourceStatus [enum]](https://developer.apple.com/documentation/imageio/cgimagesourcestatus)

|  | Declaration |
| --- | --- |
| From | ``` enum CGImageSourceStatus : Int32 {     case StatusUnexpectedEOF     case StatusInvalidData     case StatusUnknownType     case StatusReadingHeader     case StatusIncomplete     case StatusComplete } ``` |
| To | ``` enum CGImageSourceStatus : Int32 {     case statusUnexpectedEOF     case statusInvalidData     case statusUnknownType     case statusReadingHeader     case statusIncomplete     case statusComplete } ``` |

Modified [CGImageSourceStatus.statusComplete](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/kcgimagestatuscomplete)

|  | Declaration |
| --- | --- |
| From | ``` case StatusComplete ``` |
| To | ``` case statusComplete ``` |

Modified [CGImageSourceStatus.statusIncomplete](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/statusincomplete)

|  | Declaration |
| --- | --- |
| From | ``` case StatusIncomplete ``` |
| To | ``` case statusIncomplete ``` |

Modified [CGImageSourceStatus.statusInvalidData](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/kcgimagestatusinvaliddata)

|  | Declaration |
| --- | --- |
| From | ``` case StatusInvalidData ``` |
| To | ``` case statusInvalidData ``` |

Modified [CGImageSourceStatus.statusReadingHeader](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/kcgimagestatusreadingheader)

|  | Declaration |
| --- | --- |
| From | ``` case StatusReadingHeader ``` |
| To | ``` case statusReadingHeader ``` |

Modified [CGImageSourceStatus.statusUnexpectedEOF](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/kcgimagestatusunexpectedeof)

|  | Declaration |
| --- | --- |
| From | ``` case StatusUnexpectedEOF ``` |
| To | ``` case statusUnexpectedEOF ``` |

Modified [CGImageSourceStatus.statusUnknownType](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/statusunknowntype)

|  | Declaration |
| --- | --- |
| From | ``` case StatusUnknownType ``` |
| To | ``` case statusUnknownType ``` |

Modified [CGImageDestinationCopyImageSource(_: CGImageDestination, _: CGImageSource, _: CFDictionary?, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](https://developer.apple.com/documentation/imageio/1465189-cgimagedestinationcopyimagesourc)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationCopyImageSource(_ idst: CGImageDestination, _ isrc: CGImageSource, _ options: CFDictionary?, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CGImageDestinationCopyImageSource(_ idst: CGImageDestination, _ isrc: CGImageSource, _ options: CFDictionary?, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool ``` |

Modified [CGImageMetadataEnumerateTagsUsingBlock(_: CGImageMetadata, _: CFString?, _: CFDictionary?, _: ImageIO.CGImageMetadataTagBlock)](https://developer.apple.com/documentation/imageio/1465182-cgimagemetadataenumeratetagsusin)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataEnumerateTagsUsingBlock(_ metadata: CGImageMetadata, _ rootPath: CFString?, _ options: CFDictionary?, _ block: CGImageMetadataTagBlock) ``` |
| To | ``` func CGImageMetadataEnumerateTagsUsingBlock(_ metadata: CGImageMetadata, _ rootPath: CFString?, _ options: CFDictionary?, _ block: ImageIO.CGImageMetadataTagBlock) ``` |

Modified [CGImageMetadataRegisterNamespaceForPrefix(_: CGMutableImageMetadata, _: CFString, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](https://developer.apple.com/documentation/imageio/1465270-cgimagemetadataregisternamespace)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataRegisterNamespaceForPrefix(_ metadata: CGMutableImageMetadata, _ xmlns: CFString, _ prefix: CFString, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CGImageMetadataRegisterNamespaceForPrefix(_ metadata: CGMutableImageMetadata, _ xmlns: CFString, _ prefix: CFString, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool ``` |

Modified [CGImageMetadataSetValueMatchingImageProperty(_: CGMutableImageMetadata, _: CFString, _: CFString, _: CFTypeRef) -> Bool](https://developer.apple.com/documentation/imageio/1464974-cgimagemetadatasetvaluematchingi)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataSetValueMatchingImageProperty(_ metadata: CGMutableImageMetadata, _ dictionaryName: CFString, _ propertyName: CFString, _ value: AnyObject) -> Bool ``` |
| To | ``` func CGImageMetadataSetValueMatchingImageProperty(_ metadata: CGMutableImageMetadata, _ dictionaryName: CFString, _ propertyName: CFString, _ value: CFTypeRef) -> Bool ``` |

Modified [CGImageMetadataSetValueWithPath(_: CGMutableImageMetadata, _: CGImageMetadataTag?, _: CFString, _: CFTypeRef) -> Bool](https://developer.apple.com/documentation/imageio/1465265-cgimagemetadatasetvaluewithpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataSetValueWithPath(_ metadata: CGMutableImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString, _ value: AnyObject) -> Bool ``` |
| To | ``` func CGImageMetadataSetValueWithPath(_ metadata: CGMutableImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString, _ value: CFTypeRef) -> Bool ``` |

Modified [CGImageMetadataTagCopyValue(_: CGImageMetadataTag) -> CFTypeRef?](https://developer.apple.com/documentation/imageio/1464942-cgimagemetadatatagcopyvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataTagCopyValue(_ tag: CGImageMetadataTag) -> AnyObject? ``` |
| To | ``` func CGImageMetadataTagCopyValue(_ tag: CGImageMetadataTag) -> CFTypeRef? ``` |

Modified [CGImageMetadataTagCreate(_: CFString, _: CFString?, _: CFString, _: CGImageMetadataType, _: CFTypeRef) -> CGImageMetadataTag?](https://developer.apple.com/documentation/imageio/1465060-cgimagemetadatatagcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataTagCreate(_ xmlns: CFString, _ prefix: CFString?, _ name: CFString, _ type: CGImageMetadataType, _ value: AnyObject) -> CGImageMetadataTag? ``` |
| To | ``` func CGImageMetadataTagCreate(_ xmlns: CFString, _ prefix: CFString?, _ name: CFString, _ type: CGImageMetadataType, _ value: CFTypeRef) -> CGImageMetadataTag? ``` |

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
