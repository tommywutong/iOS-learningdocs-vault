---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/ImageIO.html
archived_at: '2026-07-18T02:53:37.005221Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ImageIO Changes for Swift

### ImageIO

Removed CGImageMetadataErrors.init(_: UInt32)Removed CGImageMetadataErrors.valueRemoved CGImageMetadataType.init(_: Int32)Removed CGImageMetadataType.valueRemoved CGImagePropertyOrientation.init(_: UInt32)Removed CGImagePropertyOrientation.valueRemoved CGImageSourceStatus.init(_: Int32)Removed CGImageSourceStatus.valueAdded [IMAGEIO_PNG_FILTER_AVG](https://developer.apple.com/documentation/imageio/imageio_png_filter_avg)Added [IMAGEIO_PNG_FILTER_NONE](https://developer.apple.com/documentation/imageio/imageio_png_filter_none)Added [IMAGEIO_PNG_FILTER_PAETH](https://developer.apple.com/documentation/imageio/imageio_png_filter_paeth)Added [IMAGEIO_PNG_FILTER_SUB](https://developer.apple.com/documentation/imageio/imageio_png_filter_sub)Added [IMAGEIO_PNG_FILTER_UP](https://developer.apple.com/documentation/imageio/imageio_png_filter_up)Added [IMAGEIO_PNG_NO_FILTERS](https://developer.apple.com/documentation/imageio/imageio_png_no_filters)Added [kCGImagePropertyExifSubsecTimeOriginal](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsubsectimeoriginal)Added [kCGImagePropertyPNGCompressionFilter](https://developer.apple.com/documentation/imageio/kcgimagepropertypngcompressionfilter)Added [kCGImagePropertyTIFFTileLength](https://developer.apple.com/documentation/imageio/kcgimagepropertytifftilelength)Added [kCGImagePropertyTIFFTileWidth](https://developer.apple.com/documentation/imageio/kcgimagepropertytifftilewidth)Added [kCGImageSourceSubsampleFactor](https://developer.apple.com/documentation/imageio/kcgimagesourcesubsamplefactor)Modified [CGImageMetadataErrors [enum]](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGImageMetadataErrors {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGImageMetadataErrors : Int32 {     case Unknown     case UnsupportedFormat     case BadArgument     case ConflictingArguments     case PrefixConflict } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGImageMetadataErrors.BadArgument](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/kcgimagemetadataerrorbadargument)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataErrorBadArgument | ``` var kCGImageMetadataErrorBadArgument: CGImageMetadataErrors { get } ``` | OS X 10.10 |
| To | BadArgument | ``` case BadArgument ``` | OS X 10.11 |

Modified [CGImageMetadataErrors.ConflictingArguments](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/kcgimagemetadataerrorconflictingarguments)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataErrorConflictingArguments | ``` var kCGImageMetadataErrorConflictingArguments: CGImageMetadataErrors { get } ``` | OS X 10.10 |
| To | ConflictingArguments | ``` case ConflictingArguments ``` | OS X 10.11 |

Modified [CGImageMetadataErrors.PrefixConflict](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/kcgimagemetadataerrorprefixconflict)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataErrorPrefixConflict | ``` var kCGImageMetadataErrorPrefixConflict: CGImageMetadataErrors { get } ``` | OS X 10.10 |
| To | PrefixConflict | ``` case PrefixConflict ``` | OS X 10.11 |

Modified [CGImageMetadataErrors.Unknown](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/unknown)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataErrorUnknown | ``` var kCGImageMetadataErrorUnknown: CGImageMetadataErrors { get } ``` | OS X 10.10 |
| To | Unknown | ``` case Unknown ``` | OS X 10.11 |

Modified [CGImageMetadataErrors.UnsupportedFormat](https://developer.apple.com/documentation/imageio/cgimagemetadataerrors/kcgimagemetadataerrorunsupportedformat)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataErrorUnsupportedFormat | ``` var kCGImageMetadataErrorUnsupportedFormat: CGImageMetadataErrors { get } ``` | OS X 10.10 |
| To | UnsupportedFormat | ``` case UnsupportedFormat ``` | OS X 10.11 |

Modified [CGImageMetadataType [enum]](https://developer.apple.com/documentation/imageio/cgimagemetadatatype)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGImageMetadataType {     init(_ value: Int32)     var value: Int32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGImageMetadataType : Int32 {     case Invalid     case Default     case String     case ArrayUnordered     case ArrayOrdered     case AlternateArray     case AlternateText     case Structure } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGImageMetadataType.AlternateArray](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypealternatearray)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataTypeAlternateArray | ``` var kCGImageMetadataTypeAlternateArray: CGImageMetadataType { get } ``` | OS X 10.10 |
| To | AlternateArray | ``` case AlternateArray ``` | OS X 10.11 |

Modified [CGImageMetadataType.AlternateText](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/alternatetext)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataTypeAlternateText | ``` var kCGImageMetadataTypeAlternateText: CGImageMetadataType { get } ``` | OS X 10.10 |
| To | AlternateText | ``` case AlternateText ``` | OS X 10.11 |

Modified [CGImageMetadataType.ArrayOrdered](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/arrayordered)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataTypeArrayOrdered | ``` var kCGImageMetadataTypeArrayOrdered: CGImageMetadataType { get } ``` | OS X 10.10 |
| To | ArrayOrdered | ``` case ArrayOrdered ``` | OS X 10.11 |

Modified [CGImageMetadataType.ArrayUnordered](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypearrayunordered)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataTypeArrayUnordered | ``` var kCGImageMetadataTypeArrayUnordered: CGImageMetadataType { get } ``` | OS X 10.10 |
| To | ArrayUnordered | ``` case ArrayUnordered ``` | OS X 10.11 |

Modified [CGImageMetadataType.Default](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/default)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataTypeDefault | ``` var kCGImageMetadataTypeDefault: CGImageMetadataType { get } ``` | OS X 10.10 |
| To | Default | ``` case Default ``` | OS X 10.11 |

Modified [CGImageMetadataType.Invalid](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypeinvalid)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataTypeInvalid | ``` var kCGImageMetadataTypeInvalid: CGImageMetadataType { get } ``` | OS X 10.10 |
| To | Invalid | ``` case Invalid ``` | OS X 10.11 |

Modified [CGImageMetadataType.String](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/string)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataTypeString | ``` var kCGImageMetadataTypeString: CGImageMetadataType { get } ``` | OS X 10.10 |
| To | String | ``` case String ``` | OS X 10.11 |

Modified [CGImageMetadataType.Structure](https://developer.apple.com/documentation/imageio/cgimagemetadatatype/kcgimagemetadatatypestructure)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageMetadataTypeStructure | ``` var kCGImageMetadataTypeStructure: CGImageMetadataType { get } ``` | OS X 10.10 |
| To | Structure | ``` case Structure ``` | OS X 10.11 |

Modified [CGImagePropertyOrientation [enum]](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGImagePropertyOrientation {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGImagePropertyOrientation : UInt32 {     case Up     case UpMirrored     case Down     case DownMirrored     case LeftMirrored     case Right     case RightMirrored     case Left } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | UInt32 |

Modified [CGImagePropertyOrientation.Down](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/down)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImagePropertyOrientationDown | ``` var kCGImagePropertyOrientationDown: CGImagePropertyOrientation { get } ``` | OS X 10.10 |
| To | Down | ``` case Down ``` | OS X 10.11 |

Modified [CGImagePropertyOrientation.DownMirrored](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/downmirrored)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImagePropertyOrientationDownMirrored | ``` var kCGImagePropertyOrientationDownMirrored: CGImagePropertyOrientation { get } ``` | OS X 10.10 |
| To | DownMirrored | ``` case DownMirrored ``` | OS X 10.11 |

Modified [CGImagePropertyOrientation.Left](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/kcgimagepropertyorientationleft)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImagePropertyOrientationLeft | ``` var kCGImagePropertyOrientationLeft: CGImagePropertyOrientation { get } ``` | OS X 10.10 |
| To | Left | ``` case Left ``` | OS X 10.11 |

Modified [CGImagePropertyOrientation.LeftMirrored](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/kcgimagepropertyorientationleftmirrored)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImagePropertyOrientationLeftMirrored | ``` var kCGImagePropertyOrientationLeftMirrored: CGImagePropertyOrientation { get } ``` | OS X 10.10 |
| To | LeftMirrored | ``` case LeftMirrored ``` | OS X 10.11 |

Modified [CGImagePropertyOrientation.Right](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/kcgimagepropertyorientationright)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImagePropertyOrientationRight | ``` var kCGImagePropertyOrientationRight: CGImagePropertyOrientation { get } ``` | OS X 10.10 |
| To | Right | ``` case Right ``` | OS X 10.11 |

Modified [CGImagePropertyOrientation.RightMirrored](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/rightmirrored)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImagePropertyOrientationRightMirrored | ``` var kCGImagePropertyOrientationRightMirrored: CGImagePropertyOrientation { get } ``` | OS X 10.10 |
| To | RightMirrored | ``` case RightMirrored ``` | OS X 10.11 |

Modified [CGImagePropertyOrientation.Up](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/kcgimagepropertyorientationup)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImagePropertyOrientationUp | ``` var kCGImagePropertyOrientationUp: CGImagePropertyOrientation { get } ``` | OS X 10.10 |
| To | Up | ``` case Up ``` | OS X 10.11 |

Modified [CGImagePropertyOrientation.UpMirrored](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation/upmirrored)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImagePropertyOrientationUpMirrored | ``` var kCGImagePropertyOrientationUpMirrored: CGImagePropertyOrientation { get } ``` | OS X 10.10 |
| To | UpMirrored | ``` case UpMirrored ``` | OS X 10.11 |

Modified [CGImageSourceStatus [enum]](https://developer.apple.com/documentation/imageio/cgimagesourcestatus)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct CGImageSourceStatus {     init(_ value: Int32)     var value: Int32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum CGImageSourceStatus : Int32 {     case StatusUnexpectedEOF     case StatusInvalidData     case StatusUnknownType     case StatusReadingHeader     case StatusIncomplete     case StatusComplete } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | Int32 |

Modified [CGImageSourceStatus.StatusComplete](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/kcgimagestatuscomplete)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageStatusComplete | ``` var kCGImageStatusComplete: CGImageSourceStatus { get } ``` | OS X 10.10 |
| To | StatusComplete | ``` case StatusComplete ``` | OS X 10.11 |

Modified [CGImageSourceStatus.StatusIncomplete](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/statusincomplete)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageStatusIncomplete | ``` var kCGImageStatusIncomplete: CGImageSourceStatus { get } ``` | OS X 10.10 |
| To | StatusIncomplete | ``` case StatusIncomplete ``` | OS X 10.11 |

Modified [CGImageSourceStatus.StatusInvalidData](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/kcgimagestatusinvaliddata)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageStatusInvalidData | ``` var kCGImageStatusInvalidData: CGImageSourceStatus { get } ``` | OS X 10.10 |
| To | StatusInvalidData | ``` case StatusInvalidData ``` | OS X 10.11 |

Modified [CGImageSourceStatus.StatusReadingHeader](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/kcgimagestatusreadingheader)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageStatusReadingHeader | ``` var kCGImageStatusReadingHeader: CGImageSourceStatus { get } ``` | OS X 10.10 |
| To | StatusReadingHeader | ``` case StatusReadingHeader ``` | OS X 10.11 |

Modified [CGImageSourceStatus.StatusUnexpectedEOF](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/kcgimagestatusunexpectedeof)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageStatusUnexpectedEOF | ``` var kCGImageStatusUnexpectedEOF: CGImageSourceStatus { get } ``` | OS X 10.10 |
| To | StatusUnexpectedEOF | ``` case StatusUnexpectedEOF ``` | OS X 10.11 |

Modified [CGImageSourceStatus.StatusUnknownType](https://developer.apple.com/documentation/imageio/cgimagesourcestatus/statusunknowntype)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | kCGImageStatusUnknownType | ``` var kCGImageStatusUnknownType: CGImageSourceStatus { get } ``` | OS X 10.10 |
| To | StatusUnknownType | ``` case StatusUnknownType ``` | OS X 10.11 |

Modified [CGImageDestinationAddImage(_: CGImageDestination, _: CGImage, _: CFDictionary?)](https://developer.apple.com/documentation/imageio/1464962-cgimagedestinationaddimage)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationAddImage(_ idst: CGImageDestination!, _ image: CGImage!, _ properties: CFDictionary!) ``` |
| To | ``` func CGImageDestinationAddImage(_ idst: CGImageDestination, _ image: CGImage, _ properties: CFDictionary?) ``` |

Modified [CGImageDestinationAddImageAndMetadata(_: CGImageDestination, _: CGImage, _: CGImageMetadata?, _: CFDictionary?)](https://developer.apple.com/documentation/imageio/1465429-cgimagedestinationaddimageandmet)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationAddImageAndMetadata(_ idst: CGImageDestination!, _ image: CGImage!, _ metadata: CGImageMetadata!, _ options: CFDictionary!) ``` |
| To | ``` func CGImageDestinationAddImageAndMetadata(_ idst: CGImageDestination, _ image: CGImage, _ metadata: CGImageMetadata?, _ options: CFDictionary?) ``` |

Modified [CGImageDestinationAddImageFromSource(_: CGImageDestination, _: CGImageSource, _: Int, _: CFDictionary?)](https://developer.apple.com/documentation/imageio/1465143-cgimagedestinationaddimagefromso)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationAddImageFromSource(_ idst: CGImageDestination!, _ isrc: CGImageSource!, _ index: Int, _ properties: CFDictionary!) ``` |
| To | ``` func CGImageDestinationAddImageFromSource(_ idst: CGImageDestination, _ isrc: CGImageSource, _ index: Int, _ properties: CFDictionary?) ``` |

Modified [CGImageDestinationCopyImageSource(_: CGImageDestination, _: CGImageSource, _: CFDictionary?, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/imageio/1465189-cgimagedestinationcopyimagesourc)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationCopyImageSource(_ idst: CGImageDestination!, _ isrc: CGImageSource!, _ options: CFDictionary!, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CGImageDestinationCopyImageSource(_ idst: CGImageDestination, _ isrc: CGImageSource, _ options: CFDictionary?, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CGImageDestinationCopyTypeIdentifiers() -> CFArray](https://developer.apple.com/documentation/imageio/1465316-cgimagedestinationcopytypeidenti)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationCopyTypeIdentifiers() -> CFArray! ``` |
| To | ``` func CGImageDestinationCopyTypeIdentifiers() -> CFArray ``` |

Modified [CGImageDestinationCreateWithData(_: CFMutableData, _: CFString, _: Int, _: CFDictionary?) -> CGImageDestination?](https://developer.apple.com/documentation/imageio/1465133-cgimagedestinationcreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationCreateWithData(_ data: CFMutableData!, _ type: CFString!, _ count: Int, _ options: CFDictionary!) -> CGImageDestination! ``` |
| To | ``` func CGImageDestinationCreateWithData(_ data: CFMutableData, _ type: CFString, _ count: Int, _ options: CFDictionary?) -> CGImageDestination? ``` |

Modified [CGImageDestinationCreateWithDataConsumer(_: CGDataConsumer, _: CFString, _: Int, _: CFDictionary?) -> CGImageDestination?](https://developer.apple.com/documentation/imageio/1465231-cgimagedestinationcreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationCreateWithDataConsumer(_ consumer: CGDataConsumer!, _ type: CFString!, _ count: Int, _ options: CFDictionary!) -> CGImageDestination! ``` |
| To | ``` func CGImageDestinationCreateWithDataConsumer(_ consumer: CGDataConsumer, _ type: CFString, _ count: Int, _ options: CFDictionary?) -> CGImageDestination? ``` |

Modified [CGImageDestinationCreateWithURL(_: CFURL, _: CFString, _: Int, _: CFDictionary?) -> CGImageDestination?](https://developer.apple.com/documentation/imageio/1465361-cgimagedestinationcreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationCreateWithURL(_ url: CFURL!, _ type: CFString!, _ count: Int, _ options: CFDictionary!) -> CGImageDestination! ``` |
| To | ``` func CGImageDestinationCreateWithURL(_ url: CFURL, _ type: CFString, _ count: Int, _ options: CFDictionary?) -> CGImageDestination? ``` |

Modified [CGImageDestinationFinalize(_: CGImageDestination) -> Bool](https://developer.apple.com/documentation/imageio/1464968-cgimagedestinationfinalize)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationFinalize(_ idst: CGImageDestination!) -> Bool ``` |
| To | ``` func CGImageDestinationFinalize(_ idst: CGImageDestination) -> Bool ``` |

Modified [CGImageDestinationSetProperties(_: CGImageDestination, _: CFDictionary?)](https://developer.apple.com/documentation/imageio/1464919-cgimagedestinationsetproperties)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageDestinationSetProperties(_ idst: CGImageDestination!, _ properties: CFDictionary!) ``` |
| To | ``` func CGImageDestinationSetProperties(_ idst: CGImageDestination, _ properties: CFDictionary?) ``` |

Modified [CGImageMetadataCopyStringValueWithPath(_: CGImageMetadata, _: CGImageMetadataTag?, _: CFString) -> CFString?](https://developer.apple.com/documentation/imageio/1465254-cgimagemetadatacopystringvaluewi)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataCopyStringValueWithPath(_ metadata: CGImageMetadata!, _ parent: CGImageMetadataTag!, _ path: CFString!) -> CFString! ``` |
| To | ``` func CGImageMetadataCopyStringValueWithPath(_ metadata: CGImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString) -> CFString? ``` |

Modified [CGImageMetadataCopyTagMatchingImageProperty(_: CGImageMetadata, _: CFString, _: CFString) -> CGImageMetadataTag?](https://developer.apple.com/documentation/imageio/1465081-cgimagemetadatacopytagmatchingim)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataCopyTagMatchingImageProperty(_ metadata: CGImageMetadata!, _ dictionaryName: CFString!, _ propertyName: CFString!) -> CGImageMetadataTag! ``` |
| To | ``` func CGImageMetadataCopyTagMatchingImageProperty(_ metadata: CGImageMetadata, _ dictionaryName: CFString, _ propertyName: CFString) -> CGImageMetadataTag? ``` |

Modified [CGImageMetadataCopyTags(_: CGImageMetadata) -> CFArray?](https://developer.apple.com/documentation/imageio/1464944-cgimagemetadatacopytags)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataCopyTags(_ metadata: CGImageMetadata!) -> CFArray! ``` |
| To | ``` func CGImageMetadataCopyTags(_ metadata: CGImageMetadata) -> CFArray? ``` |

Modified [CGImageMetadataCopyTagWithPath(_: CGImageMetadata, _: CGImageMetadataTag?, _: CFString) -> CGImageMetadataTag?](https://developer.apple.com/documentation/imageio/1465022-cgimagemetadatacopytagwithpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataCopyTagWithPath(_ metadata: CGImageMetadata!, _ parent: CGImageMetadataTag!, _ path: CFString!) -> CGImageMetadataTag! ``` |
| To | ``` func CGImageMetadataCopyTagWithPath(_ metadata: CGImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString) -> CGImageMetadataTag? ``` |

Modified [CGImageMetadataCreateFromXMPData(_: CFData) -> CGImageMetadata?](https://developer.apple.com/documentation/imageio/1465001-cgimagemetadatacreatefromxmpdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataCreateFromXMPData(_ data: CFData!) -> CGImageMetadata! ``` |
| To | ``` func CGImageMetadataCreateFromXMPData(_ data: CFData) -> CGImageMetadata? ``` |

Modified [CGImageMetadataCreateMutable() -> CGMutableImageMetadata](https://developer.apple.com/documentation/imageio/1465356-cgimagemetadatacreatemutable)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataCreateMutable() -> CGMutableImageMetadata! ``` |
| To | ``` func CGImageMetadataCreateMutable() -> CGMutableImageMetadata ``` |

Modified [CGImageMetadataCreateMutableCopy(_: CGImageMetadata) -> CGMutableImageMetadata?](https://developer.apple.com/documentation/imageio/1465213-cgimagemetadatacreatemutablecopy)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataCreateMutableCopy(_ metadata: CGImageMetadata!) -> CGMutableImageMetadata! ``` |
| To | ``` func CGImageMetadataCreateMutableCopy(_ metadata: CGImageMetadata) -> CGMutableImageMetadata? ``` |

Modified [CGImageMetadataCreateXMPData(_: CGImageMetadata, _: CFDictionary?) -> CFData?](https://developer.apple.com/documentation/imageio/1465217-cgimagemetadatacreatexmpdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataCreateXMPData(_ metadata: CGImageMetadata!, _ options: CFDictionary!) -> CFData! ``` |
| To | ``` func CGImageMetadataCreateXMPData(_ metadata: CGImageMetadata, _ options: CFDictionary?) -> CFData? ``` |

Modified [CGImageMetadataEnumerateTagsUsingBlock(_: CGImageMetadata, _: CFString?, _: CFDictionary?, _: CGImageMetadataTagBlock)](https://developer.apple.com/documentation/imageio/1465182-cgimagemetadataenumeratetagsusin)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataEnumerateTagsUsingBlock(_ metadata: CGImageMetadata!, _ rootPath: CFString!, _ options: CFDictionary!, _ block: CGImageMetadataTagBlock!) ``` |
| To | ``` func CGImageMetadataEnumerateTagsUsingBlock(_ metadata: CGImageMetadata, _ rootPath: CFString?, _ options: CFDictionary?, _ block: CGImageMetadataTagBlock) ``` |

Modified [CGImageMetadataRegisterNamespaceForPrefix(_: CGMutableImageMetadata, _: CFString, _: CFString, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/imageio/1465270-cgimagemetadataregisternamespace)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataRegisterNamespaceForPrefix(_ metadata: CGMutableImageMetadata!, _ xmlns: CFString!, _ prefix: CFString!, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func CGImageMetadataRegisterNamespaceForPrefix(_ metadata: CGMutableImageMetadata, _ xmlns: CFString, _ prefix: CFString, _ err: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [CGImageMetadataRemoveTagWithPath(_: CGMutableImageMetadata, _: CGImageMetadataTag?, _: CFString) -> Bool](https://developer.apple.com/documentation/imageio/1465138-cgimagemetadataremovetagwithpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataRemoveTagWithPath(_ metadata: CGMutableImageMetadata!, _ parent: CGImageMetadataTag!, _ path: CFString!) -> Bool ``` |
| To | ``` func CGImageMetadataRemoveTagWithPath(_ metadata: CGMutableImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString) -> Bool ``` |

Modified [CGImageMetadataSetTagWithPath(_: CGMutableImageMetadata, _: CGImageMetadataTag?, _: CFString, _: CGImageMetadataTag) -> Bool](https://developer.apple.com/documentation/imageio/1465409-cgimagemetadatasettagwithpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataSetTagWithPath(_ metadata: CGMutableImageMetadata!, _ parent: CGImageMetadataTag!, _ path: CFString!, _ tag: CGImageMetadataTag!) -> Bool ``` |
| To | ``` func CGImageMetadataSetTagWithPath(_ metadata: CGMutableImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString, _ tag: CGImageMetadataTag) -> Bool ``` |

Modified [CGImageMetadataSetValueMatchingImageProperty(_: CGMutableImageMetadata, _: CFString, _: CFString, _: AnyObject) -> Bool](https://developer.apple.com/documentation/imageio/1464974-cgimagemetadatasetvaluematchingi)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataSetValueMatchingImageProperty(_ metadata: CGMutableImageMetadata!, _ dictionaryName: CFString!, _ propertyName: CFString!, _ value: AnyObject!) -> Bool ``` |
| To | ``` func CGImageMetadataSetValueMatchingImageProperty(_ metadata: CGMutableImageMetadata, _ dictionaryName: CFString, _ propertyName: CFString, _ value: AnyObject) -> Bool ``` |

Modified [CGImageMetadataSetValueWithPath(_: CGMutableImageMetadata, _: CGImageMetadataTag?, _: CFString, _: AnyObject) -> Bool](https://developer.apple.com/documentation/imageio/1465265-cgimagemetadatasetvaluewithpath)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataSetValueWithPath(_ metadata: CGMutableImageMetadata!, _ parent: CGImageMetadataTag!, _ path: CFString!, _ value: AnyObject!) -> Bool ``` |
| To | ``` func CGImageMetadataSetValueWithPath(_ metadata: CGMutableImageMetadata, _ parent: CGImageMetadataTag?, _ path: CFString, _ value: AnyObject) -> Bool ``` |

Modified [CGImageMetadataTagBlock](https://developer.apple.com/documentation/imageio/cgimagemetadatatagblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGImageMetadataTagBlock = (CFString!, CGImageMetadataTag!) -> Bool ``` |
| To | ``` typealias CGImageMetadataTagBlock = (CFString, CGImageMetadataTag) -> Bool ``` |

Modified [CGImageMetadataTagCopyName(_: CGImageMetadataTag) -> CFString?](https://developer.apple.com/documentation/imageio/1465092-cgimagemetadatatagcopyname)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataTagCopyName(_ tag: CGImageMetadataTag!) -> CFString! ``` |
| To | ``` func CGImageMetadataTagCopyName(_ tag: CGImageMetadataTag) -> CFString? ``` |

Modified [CGImageMetadataTagCopyNamespace(_: CGImageMetadataTag) -> CFString?](https://developer.apple.com/documentation/imageio/1465160-cgimagemetadatatagcopynamespace)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataTagCopyNamespace(_ tag: CGImageMetadataTag!) -> CFString! ``` |
| To | ``` func CGImageMetadataTagCopyNamespace(_ tag: CGImageMetadataTag) -> CFString? ``` |

Modified [CGImageMetadataTagCopyPrefix(_: CGImageMetadataTag) -> CFString?](https://developer.apple.com/documentation/imageio/1465378-cgimagemetadatatagcopyprefix)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataTagCopyPrefix(_ tag: CGImageMetadataTag!) -> CFString! ``` |
| To | ``` func CGImageMetadataTagCopyPrefix(_ tag: CGImageMetadataTag) -> CFString? ``` |

Modified [CGImageMetadataTagCopyQualifiers(_: CGImageMetadataTag) -> CFArray?](https://developer.apple.com/documentation/imageio/1465094-cgimagemetadatatagcopyqualifiers)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataTagCopyQualifiers(_ tag: CGImageMetadataTag!) -> CFArray! ``` |
| To | ``` func CGImageMetadataTagCopyQualifiers(_ tag: CGImageMetadataTag) -> CFArray? ``` |

Modified [CGImageMetadataTagCopyValue(_: CGImageMetadataTag) -> AnyObject?](https://developer.apple.com/documentation/imageio/1464942-cgimagemetadatatagcopyvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataTagCopyValue(_ tag: CGImageMetadataTag!) -> AnyObject! ``` |
| To | ``` func CGImageMetadataTagCopyValue(_ tag: CGImageMetadataTag) -> AnyObject? ``` |

Modified [CGImageMetadataTagCreate(_: CFString, _: CFString?, _: CFString, _: CGImageMetadataType, _: AnyObject) -> CGImageMetadataTag?](https://developer.apple.com/documentation/imageio/1465060-cgimagemetadatatagcreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataTagCreate(_ xmlns: CFString!, _ prefix: CFString!, _ name: CFString!, _ type: CGImageMetadataType, _ value: AnyObject!) -> CGImageMetadataTag! ``` |
| To | ``` func CGImageMetadataTagCreate(_ xmlns: CFString, _ prefix: CFString?, _ name: CFString, _ type: CGImageMetadataType, _ value: AnyObject) -> CGImageMetadataTag? ``` |

Modified [CGImageMetadataTagGetType(_: CGImageMetadataTag) -> CGImageMetadataType](https://developer.apple.com/documentation/imageio/1465337-cgimagemetadatataggettype)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageMetadataTagGetType(_ tag: CGImageMetadataTag!) -> CGImageMetadataType ``` |
| To | ``` func CGImageMetadataTagGetType(_ tag: CGImageMetadataTag) -> CGImageMetadataType ``` |

Modified [CGImageSourceCopyMetadataAtIndex(_: CGImageSource, _: Int, _: CFDictionary?) -> CGImageMetadata?](https://developer.apple.com/documentation/imageio/1465476-cgimagesourcecopymetadataatindex)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCopyMetadataAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CGImageMetadata! ``` |
| To | ``` func CGImageSourceCopyMetadataAtIndex(_ isrc: CGImageSource, _ index: Int, _ options: CFDictionary?) -> CGImageMetadata? ``` |

Modified [CGImageSourceCopyProperties(_: CGImageSource, _: CFDictionary?) -> CFDictionary?](https://developer.apple.com/documentation/imageio/1465443-cgimagesourcecopyproperties)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCopyProperties(_ isrc: CGImageSource!, _ options: CFDictionary!) -> CFDictionary! ``` |
| To | ``` func CGImageSourceCopyProperties(_ isrc: CGImageSource, _ options: CFDictionary?) -> CFDictionary? ``` |

Modified [CGImageSourceCopyPropertiesAtIndex(_: CGImageSource, _: Int, _: CFDictionary?) -> CFDictionary?](https://developer.apple.com/documentation/imageio/1465363-cgimagesourcecopypropertiesatind)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCopyPropertiesAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CFDictionary! ``` |
| To | ``` func CGImageSourceCopyPropertiesAtIndex(_ isrc: CGImageSource, _ index: Int, _ options: CFDictionary?) -> CFDictionary? ``` |

Modified [CGImageSourceCopyTypeIdentifiers() -> CFArray](https://developer.apple.com/documentation/imageio/1465383-cgimagesourcecopytypeidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCopyTypeIdentifiers() -> CFArray! ``` |
| To | ``` func CGImageSourceCopyTypeIdentifiers() -> CFArray ``` |

Modified [CGImageSourceCreateImageAtIndex(_: CGImageSource, _: Int, _: CFDictionary?) -> CGImage?](https://developer.apple.com/documentation/imageio/1465011-cgimagesourcecreateimageatindex)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCreateImageAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CGImage! ``` |
| To | ``` func CGImageSourceCreateImageAtIndex(_ isrc: CGImageSource, _ index: Int, _ options: CFDictionary?) -> CGImage? ``` |

Modified [CGImageSourceCreateIncremental(_: CFDictionary?) -> CGImageSource](https://developer.apple.com/documentation/imageio/1465151-cgimagesourcecreateincremental)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCreateIncremental(_ options: CFDictionary!) -> CGImageSource! ``` |
| To | ``` func CGImageSourceCreateIncremental(_ options: CFDictionary?) -> CGImageSource ``` |

Modified [CGImageSourceCreateThumbnailAtIndex(_: CGImageSource, _: Int, _: CFDictionary?) -> CGImage?](https://developer.apple.com/documentation/imageio/1465099-cgimagesourcecreatethumbnailatin)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCreateThumbnailAtIndex(_ isrc: CGImageSource!, _ index: Int, _ options: CFDictionary!) -> CGImage! ``` |
| To | ``` func CGImageSourceCreateThumbnailAtIndex(_ isrc: CGImageSource, _ index: Int, _ options: CFDictionary?) -> CGImage? ``` |

Modified [CGImageSourceCreateWithData(_: CFData, _: CFDictionary?) -> CGImageSource?](https://developer.apple.com/documentation/imageio/1465073-cgimagesourcecreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCreateWithData(_ data: CFData!, _ options: CFDictionary!) -> CGImageSource! ``` |
| To | ``` func CGImageSourceCreateWithData(_ data: CFData, _ options: CFDictionary?) -> CGImageSource? ``` |

Modified [CGImageSourceCreateWithDataProvider(_: CGDataProvider, _: CFDictionary?) -> CGImageSource?](https://developer.apple.com/documentation/imageio/1465285-cgimagesourcecreatewithdataprovi)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCreateWithDataProvider(_ provider: CGDataProvider!, _ options: CFDictionary!) -> CGImageSource! ``` |
| To | ``` func CGImageSourceCreateWithDataProvider(_ provider: CGDataProvider, _ options: CFDictionary?) -> CGImageSource? ``` |

Modified [CGImageSourceCreateWithURL(_: CFURL, _: CFDictionary?) -> CGImageSource?](https://developer.apple.com/documentation/imageio/1465262-cgimagesourcecreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceCreateWithURL(_ url: CFURL!, _ options: CFDictionary!) -> CGImageSource! ``` |
| To | ``` func CGImageSourceCreateWithURL(_ url: CFURL, _ options: CFDictionary?) -> CGImageSource? ``` |

Modified [CGImageSourceGetCount(_: CGImageSource) -> Int](https://developer.apple.com/documentation/imageio/1465029-cgimagesourcegetcount)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceGetCount(_ isrc: CGImageSource!) -> Int ``` |
| To | ``` func CGImageSourceGetCount(_ isrc: CGImageSource) -> Int ``` |

Modified [CGImageSourceGetStatus(_: CGImageSource) -> CGImageSourceStatus](https://developer.apple.com/documentation/imageio/1465322-cgimagesourcegetstatus)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceGetStatus(_ isrc: CGImageSource!) -> CGImageSourceStatus ``` |
| To | ``` func CGImageSourceGetStatus(_ isrc: CGImageSource) -> CGImageSourceStatus ``` |

Modified [CGImageSourceGetStatusAtIndex(_: CGImageSource, _: Int) -> CGImageSourceStatus](https://developer.apple.com/documentation/imageio/1465401-cgimagesourcegetstatusatindex)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceGetStatusAtIndex(_ isrc: CGImageSource!, _ index: Int) -> CGImageSourceStatus ``` |
| To | ``` func CGImageSourceGetStatusAtIndex(_ isrc: CGImageSource, _ index: Int) -> CGImageSourceStatus ``` |

Modified [CGImageSourceGetType(_: CGImageSource) -> CFString?](https://developer.apple.com/documentation/imageio/1465448-cgimagesourcegettype)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceGetType(_ isrc: CGImageSource!) -> CFString! ``` |
| To | ``` func CGImageSourceGetType(_ isrc: CGImageSource) -> CFString? ``` |

Modified [CGImageSourceRemoveCacheAtIndex(_: CGImageSource, _: Int)](https://developer.apple.com/documentation/imageio/1465077-cgimagesourceremovecacheatindex)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceRemoveCacheAtIndex(_ isrc: CGImageSource!, _ index: Int) ``` |
| To | ``` func CGImageSourceRemoveCacheAtIndex(_ isrc: CGImageSource, _ index: Int) ``` |

Modified [CGImageSourceUpdateData(_: CGImageSource, _: CFData, _: Bool)](https://developer.apple.com/documentation/imageio/1465473-cgimagesourceupdatedata)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceUpdateData(_ isrc: CGImageSource!, _ data: CFData!, _ final: Bool) ``` |
| To | ``` func CGImageSourceUpdateData(_ isrc: CGImageSource, _ data: CFData, _ final: Bool) ``` |

Modified [CGImageSourceUpdateDataProvider(_: CGImageSource, _: CGDataProvider, _: Bool)](https://developer.apple.com/documentation/imageio/1465175-cgimagesourceupdatedataprovider)

|  | Declaration |
| --- | --- |
| From | ``` func CGImageSourceUpdateDataProvider(_ isrc: CGImageSource!, _ provider: CGDataProvider!, _ final: Bool) ``` |
| To | ``` func CGImageSourceUpdateDataProvider(_ isrc: CGImageSource, _ provider: CGDataProvider, _ final: Bool) ``` |

Modified [kCFErrorDomainCGImageMetadata](https://developer.apple.com/documentation/imageio/kcferrordomaincgimagemetadata)

|  | Declaration |
| --- | --- |
| From | ``` let kCFErrorDomainCGImageMetadata: CFString! ``` |
| To | ``` let kCFErrorDomainCGImageMetadata: CFString ``` |

Modified [kCGImageDestinationBackgroundColor](https://developer.apple.com/documentation/imageio/kcgimagedestinationbackgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageDestinationBackgroundColor: CFString! ``` |
| To | ``` let kCGImageDestinationBackgroundColor: CFString ``` |

Modified [kCGImageDestinationDateTime](https://developer.apple.com/documentation/imageio/kcgimagedestinationdatetime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageDestinationDateTime: CFString! ``` |
| To | ``` let kCGImageDestinationDateTime: CFString ``` |

Modified [kCGImageDestinationEmbedThumbnail](https://developer.apple.com/documentation/imageio/kcgimagedestinationembedthumbnail)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageDestinationEmbedThumbnail: CFString! ``` |
| To | ``` let kCGImageDestinationEmbedThumbnail: CFString ``` |

Modified [kCGImageDestinationImageMaxPixelSize](https://developer.apple.com/documentation/imageio/kcgimagedestinationimagemaxpixelsize)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageDestinationImageMaxPixelSize: CFString! ``` |
| To | ``` let kCGImageDestinationImageMaxPixelSize: CFString ``` |

Modified [kCGImageDestinationLossyCompressionQuality](https://developer.apple.com/documentation/imageio/kcgimagedestinationlossycompressionquality)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageDestinationLossyCompressionQuality: CFString! ``` |
| To | ``` let kCGImageDestinationLossyCompressionQuality: CFString ``` |

Modified [kCGImageDestinationMergeMetadata](https://developer.apple.com/documentation/imageio/kcgimagedestinationmergemetadata)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageDestinationMergeMetadata: CFString! ``` |
| To | ``` let kCGImageDestinationMergeMetadata: CFString ``` |

Modified [kCGImageDestinationMetadata](https://developer.apple.com/documentation/imageio/kcgimagedestinationmetadata)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageDestinationMetadata: CFString! ``` |
| To | ``` let kCGImageDestinationMetadata: CFString ``` |

Modified [kCGImageDestinationOrientation](https://developer.apple.com/documentation/imageio/kcgimagedestinationorientation)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageDestinationOrientation: CFString! ``` |
| To | ``` let kCGImageDestinationOrientation: CFString ``` |

Modified [kCGImageMetadataEnumerateRecursively](https://developer.apple.com/documentation/imageio/kcgimagemetadataenumeraterecursively)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataEnumerateRecursively: CFString! ``` |
| To | ``` let kCGImageMetadataEnumerateRecursively: CFString ``` |

Modified [kCGImageMetadataNamespaceDublinCore](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespacedublincore)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataNamespaceDublinCore: CFString! ``` |
| To | ``` let kCGImageMetadataNamespaceDublinCore: CFString ``` |

Modified [kCGImageMetadataNamespaceExif](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespaceexif)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataNamespaceExif: CFString! ``` |
| To | ``` let kCGImageMetadataNamespaceExif: CFString ``` |

Modified [kCGImageMetadataNamespaceExifAux](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespaceexifaux)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataNamespaceExifAux: CFString! ``` |
| To | ``` let kCGImageMetadataNamespaceExifAux: CFString ``` |

Modified [kCGImageMetadataNamespaceExifEX](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespaceexifex)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataNamespaceExifEX: CFString! ``` |
| To | ``` let kCGImageMetadataNamespaceExifEX: CFString ``` |

Modified [kCGImageMetadataNamespaceIPTCCore](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespaceiptccore)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataNamespaceIPTCCore: CFString! ``` |
| To | ``` let kCGImageMetadataNamespaceIPTCCore: CFString ``` |

Modified [kCGImageMetadataNamespacePhotoshop](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespacephotoshop)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataNamespacePhotoshop: CFString! ``` |
| To | ``` let kCGImageMetadataNamespacePhotoshop: CFString ``` |

Modified [kCGImageMetadataNamespaceTIFF](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespacetiff)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataNamespaceTIFF: CFString! ``` |
| To | ``` let kCGImageMetadataNamespaceTIFF: CFString ``` |

Modified [kCGImageMetadataNamespaceXMPBasic](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespacexmpbasic)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataNamespaceXMPBasic: CFString! ``` |
| To | ``` let kCGImageMetadataNamespaceXMPBasic: CFString ``` |

Modified [kCGImageMetadataNamespaceXMPRights](https://developer.apple.com/documentation/imageio/kcgimagemetadatanamespacexmprights)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataNamespaceXMPRights: CFString! ``` |
| To | ``` let kCGImageMetadataNamespaceXMPRights: CFString ``` |

Modified [kCGImageMetadataPrefixDublinCore](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixdublincore)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataPrefixDublinCore: CFString! ``` |
| To | ``` let kCGImageMetadataPrefixDublinCore: CFString ``` |

Modified [kCGImageMetadataPrefixExif](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixexif)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataPrefixExif: CFString! ``` |
| To | ``` let kCGImageMetadataPrefixExif: CFString ``` |

Modified [kCGImageMetadataPrefixExifAux](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixexifaux)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataPrefixExifAux: CFString! ``` |
| To | ``` let kCGImageMetadataPrefixExifAux: CFString ``` |

Modified [kCGImageMetadataPrefixExifEX](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixexifex)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataPrefixExifEX: CFString! ``` |
| To | ``` let kCGImageMetadataPrefixExifEX: CFString ``` |

Modified [kCGImageMetadataPrefixIPTCCore](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixiptccore)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataPrefixIPTCCore: CFString! ``` |
| To | ``` let kCGImageMetadataPrefixIPTCCore: CFString ``` |

Modified [kCGImageMetadataPrefixPhotoshop](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixphotoshop)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataPrefixPhotoshop: CFString! ``` |
| To | ``` let kCGImageMetadataPrefixPhotoshop: CFString ``` |

Modified [kCGImageMetadataPrefixTIFF](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixtiff)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataPrefixTIFF: CFString! ``` |
| To | ``` let kCGImageMetadataPrefixTIFF: CFString ``` |

Modified [kCGImageMetadataPrefixXMPBasic](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixxmpbasic)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataPrefixXMPBasic: CFString! ``` |
| To | ``` let kCGImageMetadataPrefixXMPBasic: CFString ``` |

Modified [kCGImageMetadataPrefixXMPRights](https://developer.apple.com/documentation/imageio/kcgimagemetadataprefixxmprights)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataPrefixXMPRights: CFString! ``` |
| To | ``` let kCGImageMetadataPrefixXMPRights: CFString ``` |

Modified [kCGImageMetadataShouldExcludeGPS](https://developer.apple.com/documentation/imageio/kcgimagemetadatashouldexcludegps)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataShouldExcludeGPS: CFString! ``` |
| To | ``` let kCGImageMetadataShouldExcludeGPS: CFString ``` |

Modified [kCGImageMetadataShouldExcludeXMP](https://developer.apple.com/documentation/imageio/kcgimagemetadatashouldexcludexmp)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageMetadataShouldExcludeXMP: CFString! ``` |
| To | ``` let kCGImageMetadataShouldExcludeXMP: CFString ``` |

Modified [kCGImageProperty8BIMDictionary](https://developer.apple.com/documentation/imageio/kcgimageproperty8bimdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageProperty8BIMDictionary: CFString! ``` |
| To | ``` let kCGImageProperty8BIMDictionary: CFString ``` |

Modified [kCGImageProperty8BIMLayerNames](https://developer.apple.com/documentation/imageio/kcgimageproperty8bimlayernames)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageProperty8BIMLayerNames: CFString! ``` |
| To | ``` let kCGImageProperty8BIMLayerNames: CFString ``` |

Modified [kCGImageProperty8BIMVersion](https://developer.apple.com/documentation/imageio/kcgimageproperty8bimversion)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageProperty8BIMVersion: CFString! ``` |
| To | ``` let kCGImageProperty8BIMVersion: CFString ``` |

Modified [kCGImagePropertyAPNGDelayTime](https://developer.apple.com/documentation/imageio/kcgimagepropertyapngdelaytime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyAPNGDelayTime: CFString! ``` |
| To | ``` let kCGImagePropertyAPNGDelayTime: CFString ``` |

Modified [kCGImagePropertyAPNGLoopCount](https://developer.apple.com/documentation/imageio/kcgimagepropertyapngloopcount)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyAPNGLoopCount: CFString! ``` |
| To | ``` let kCGImagePropertyAPNGLoopCount: CFString ``` |

Modified [kCGImagePropertyAPNGUnclampedDelayTime](https://developer.apple.com/documentation/imageio/kcgimagepropertyapngunclampeddelaytime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyAPNGUnclampedDelayTime: CFString! ``` |
| To | ``` let kCGImagePropertyAPNGUnclampedDelayTime: CFString ``` |

Modified [kCGImagePropertyCIFFCameraSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffcameraserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFCameraSerialNumber: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFCameraSerialNumber: CFString ``` |

Modified [kCGImagePropertyCIFFContinuousDrive](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffcontinuousdrive)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFContinuousDrive: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFContinuousDrive: CFString ``` |

Modified [kCGImagePropertyCIFFDescription](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffdescription)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFDescription: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFDescription: CFString ``` |

Modified [kCGImagePropertyCIFFDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFDictionary: CFString ``` |

Modified [kCGImagePropertyCIFFFirmware](https://developer.apple.com/documentation/imageio/kcgimagepropertycifffirmware)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFFirmware: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFFirmware: CFString ``` |

Modified [kCGImagePropertyCIFFFlashExposureComp](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffflashexposurecomp)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFFlashExposureComp: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFFlashExposureComp: CFString ``` |

Modified [kCGImagePropertyCIFFFocusMode](https://developer.apple.com/documentation/imageio/kcgimagepropertycifffocusmode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFFocusMode: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFFocusMode: CFString ``` |

Modified [kCGImagePropertyCIFFImageFileName](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffimagefilename)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFImageFileName: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFImageFileName: CFString ``` |

Modified [kCGImagePropertyCIFFImageName](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffimagename)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFImageName: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFImageName: CFString ``` |

Modified [kCGImagePropertyCIFFImageSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffimageserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFImageSerialNumber: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFImageSerialNumber: CFString ``` |

Modified [kCGImagePropertyCIFFLensMaxMM](https://developer.apple.com/documentation/imageio/kcgimagepropertycifflensmaxmm)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFLensMaxMM: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFLensMaxMM: CFString ``` |

Modified [kCGImagePropertyCIFFLensMinMM](https://developer.apple.com/documentation/imageio/kcgimagepropertycifflensminmm)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFLensMinMM: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFLensMinMM: CFString ``` |

Modified [kCGImagePropertyCIFFLensModel](https://developer.apple.com/documentation/imageio/kcgimagepropertycifflensmodel)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFLensModel: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFLensModel: CFString ``` |

Modified [kCGImagePropertyCIFFMeasuredEV](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffmeasuredev)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFMeasuredEV: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFMeasuredEV: CFString ``` |

Modified [kCGImagePropertyCIFFMeteringMode](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffmeteringmode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFMeteringMode: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFMeteringMode: CFString ``` |

Modified [kCGImagePropertyCIFFOwnerName](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffownername)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFOwnerName: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFOwnerName: CFString ``` |

Modified [kCGImagePropertyCIFFRecordID](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffrecordid)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFRecordID: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFRecordID: CFString ``` |

Modified [kCGImagePropertyCIFFReleaseMethod](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffreleasemethod)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFReleaseMethod: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFReleaseMethod: CFString ``` |

Modified [kCGImagePropertyCIFFReleaseTiming](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffreleasetiming)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFReleaseTiming: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFReleaseTiming: CFString ``` |

Modified [kCGImagePropertyCIFFSelfTimingTime](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffselftimingtime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFSelfTimingTime: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFSelfTimingTime: CFString ``` |

Modified [kCGImagePropertyCIFFShootingMode](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffshootingmode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFShootingMode: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFShootingMode: CFString ``` |

Modified [kCGImagePropertyCIFFWhiteBalanceIndex](https://developer.apple.com/documentation/imageio/kcgimagepropertyciffwhitebalanceindex)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyCIFFWhiteBalanceIndex: CFString! ``` |
| To | ``` let kCGImagePropertyCIFFWhiteBalanceIndex: CFString ``` |

Modified [kCGImagePropertyColorModel](https://developer.apple.com/documentation/imageio/kcgimagepropertycolormodel)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyColorModel: CFString! ``` |
| To | ``` let kCGImagePropertyColorModel: CFString ``` |

Modified [kCGImagePropertyColorModelCMYK](https://developer.apple.com/documentation/imageio/kcgimagepropertycolormodelcmyk)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyColorModelCMYK: CFString! ``` |
| To | ``` let kCGImagePropertyColorModelCMYK: CFString ``` |

Modified [kCGImagePropertyColorModelGray](https://developer.apple.com/documentation/imageio/kcgimagepropertycolormodelgray)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyColorModelGray: CFString! ``` |
| To | ``` let kCGImagePropertyColorModelGray: CFString ``` |

Modified [kCGImagePropertyColorModelLab](https://developer.apple.com/documentation/imageio/kcgimagepropertycolormodellab)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyColorModelLab: CFString! ``` |
| To | ``` let kCGImagePropertyColorModelLab: CFString ``` |

Modified [kCGImagePropertyColorModelRGB](https://developer.apple.com/documentation/imageio/kcgimagepropertycolormodelrgb)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyColorModelRGB: CFString! ``` |
| To | ``` let kCGImagePropertyColorModelRGB: CFString ``` |

Modified [kCGImagePropertyDepth](https://developer.apple.com/documentation/imageio/kcgimagepropertydepth)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyDepth: CFString! ``` |
| To | ``` let kCGImagePropertyDepth: CFString ``` |

Modified [kCGImagePropertyDNGBackwardVersion](https://developer.apple.com/documentation/imageio/kcgimagepropertydngbackwardversion)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyDNGBackwardVersion: CFString! ``` |
| To | ``` let kCGImagePropertyDNGBackwardVersion: CFString ``` |

Modified [kCGImagePropertyDNGCameraSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertydngcameraserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyDNGCameraSerialNumber: CFString! ``` |
| To | ``` let kCGImagePropertyDNGCameraSerialNumber: CFString ``` |

Modified [kCGImagePropertyDNGDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertydngdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyDNGDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyDNGDictionary: CFString ``` |

Modified [kCGImagePropertyDNGLensInfo](https://developer.apple.com/documentation/imageio/kcgimagepropertydnglensinfo)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyDNGLensInfo: CFString! ``` |
| To | ``` let kCGImagePropertyDNGLensInfo: CFString ``` |

Modified [kCGImagePropertyDNGLocalizedCameraModel](https://developer.apple.com/documentation/imageio/kcgimagepropertydnglocalizedcameramodel)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyDNGLocalizedCameraModel: CFString! ``` |
| To | ``` let kCGImagePropertyDNGLocalizedCameraModel: CFString ``` |

Modified [kCGImagePropertyDNGUniqueCameraModel](https://developer.apple.com/documentation/imageio/kcgimagepropertydnguniquecameramodel)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyDNGUniqueCameraModel: CFString! ``` |
| To | ``` let kCGImagePropertyDNGUniqueCameraModel: CFString ``` |

Modified [kCGImagePropertyDNGVersion](https://developer.apple.com/documentation/imageio/kcgimagepropertydngversion)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyDNGVersion: CFString! ``` |
| To | ``` let kCGImagePropertyDNGVersion: CFString ``` |

Modified [kCGImagePropertyDPIHeight](https://developer.apple.com/documentation/imageio/kcgimagepropertydpiheight)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyDPIHeight: CFString! ``` |
| To | ``` let kCGImagePropertyDPIHeight: CFString ``` |

Modified [kCGImagePropertyDPIWidth](https://developer.apple.com/documentation/imageio/kcgimagepropertydpiwidth)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyDPIWidth: CFString! ``` |
| To | ``` let kCGImagePropertyDPIWidth: CFString ``` |

Modified [kCGImagePropertyExifApertureValue](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifaperturevalue)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifApertureValue: CFString! ``` |
| To | ``` let kCGImagePropertyExifApertureValue: CFString ``` |

Modified [kCGImagePropertyExifAuxDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifauxdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifAuxDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyExifAuxDictionary: CFString ``` |

Modified [kCGImagePropertyExifAuxFirmware](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifauxfirmware)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifAuxFirmware: CFString! ``` |
| To | ``` let kCGImagePropertyExifAuxFirmware: CFString ``` |

Modified [kCGImagePropertyExifAuxFlashCompensation](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifauxflashcompensation)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifAuxFlashCompensation: CFString! ``` |
| To | ``` let kCGImagePropertyExifAuxFlashCompensation: CFString ``` |

Modified [kCGImagePropertyExifAuxImageNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifauximagenumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifAuxImageNumber: CFString! ``` |
| To | ``` let kCGImagePropertyExifAuxImageNumber: CFString ``` |

Modified [kCGImagePropertyExifAuxLensID](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifauxlensid)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifAuxLensID: CFString! ``` |
| To | ``` let kCGImagePropertyExifAuxLensID: CFString ``` |

Modified [kCGImagePropertyExifAuxLensInfo](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifauxlensinfo)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifAuxLensInfo: CFString! ``` |
| To | ``` let kCGImagePropertyExifAuxLensInfo: CFString ``` |

Modified [kCGImagePropertyExifAuxLensModel](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifauxlensmodel)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifAuxLensModel: CFString! ``` |
| To | ``` let kCGImagePropertyExifAuxLensModel: CFString ``` |

Modified [kCGImagePropertyExifAuxLensSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifauxlensserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifAuxLensSerialNumber: CFString! ``` |
| To | ``` let kCGImagePropertyExifAuxLensSerialNumber: CFString ``` |

Modified [kCGImagePropertyExifAuxOwnerName](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifauxownername)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifAuxOwnerName: CFString! ``` |
| To | ``` let kCGImagePropertyExifAuxOwnerName: CFString ``` |

Modified [kCGImagePropertyExifAuxSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifauxserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifAuxSerialNumber: CFString! ``` |
| To | ``` let kCGImagePropertyExifAuxSerialNumber: CFString ``` |

Modified [kCGImagePropertyExifBodySerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifbodyserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifBodySerialNumber: CFString! ``` |
| To | ``` let kCGImagePropertyExifBodySerialNumber: CFString ``` |

Modified [kCGImagePropertyExifBrightnessValue](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifbrightnessvalue)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifBrightnessValue: CFString! ``` |
| To | ``` let kCGImagePropertyExifBrightnessValue: CFString ``` |

Modified [kCGImagePropertyExifCameraOwnerName](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifcameraownername)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifCameraOwnerName: CFString! ``` |
| To | ``` let kCGImagePropertyExifCameraOwnerName: CFString ``` |

Modified [kCGImagePropertyExifCFAPattern](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifcfapattern)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifCFAPattern: CFString! ``` |
| To | ``` let kCGImagePropertyExifCFAPattern: CFString ``` |

Modified [kCGImagePropertyExifColorSpace](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifcolorspace)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifColorSpace: CFString! ``` |
| To | ``` let kCGImagePropertyExifColorSpace: CFString ``` |

Modified [kCGImagePropertyExifComponentsConfiguration](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifcomponentsconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifComponentsConfiguration: CFString! ``` |
| To | ``` let kCGImagePropertyExifComponentsConfiguration: CFString ``` |

Modified [kCGImagePropertyExifCompressedBitsPerPixel](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifcompressedbitsperpixel)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifCompressedBitsPerPixel: CFString! ``` |
| To | ``` let kCGImagePropertyExifCompressedBitsPerPixel: CFString ``` |

Modified [kCGImagePropertyExifContrast](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifcontrast)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifContrast: CFString! ``` |
| To | ``` let kCGImagePropertyExifContrast: CFString ``` |

Modified [kCGImagePropertyExifCustomRendered](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifcustomrendered)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifCustomRendered: CFString! ``` |
| To | ``` let kCGImagePropertyExifCustomRendered: CFString ``` |

Modified [kCGImagePropertyExifDateTimeDigitized](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifdatetimedigitized)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifDateTimeDigitized: CFString! ``` |
| To | ``` let kCGImagePropertyExifDateTimeDigitized: CFString ``` |

Modified [kCGImagePropertyExifDateTimeOriginal](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifdatetimeoriginal)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifDateTimeOriginal: CFString! ``` |
| To | ``` let kCGImagePropertyExifDateTimeOriginal: CFString ``` |

Modified [kCGImagePropertyExifDeviceSettingDescription](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifdevicesettingdescription)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifDeviceSettingDescription: CFString! ``` |
| To | ``` let kCGImagePropertyExifDeviceSettingDescription: CFString ``` |

Modified [kCGImagePropertyExifDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyExifDictionary: CFString ``` |

Modified [kCGImagePropertyExifDigitalZoomRatio](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifdigitalzoomratio)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifDigitalZoomRatio: CFString! ``` |
| To | ``` let kCGImagePropertyExifDigitalZoomRatio: CFString ``` |

Modified [kCGImagePropertyExifExposureBiasValue](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifexposurebiasvalue)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifExposureBiasValue: CFString! ``` |
| To | ``` let kCGImagePropertyExifExposureBiasValue: CFString ``` |

Modified [kCGImagePropertyExifExposureIndex](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifexposureindex)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifExposureIndex: CFString! ``` |
| To | ``` let kCGImagePropertyExifExposureIndex: CFString ``` |

Modified [kCGImagePropertyExifExposureMode](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifexposuremode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifExposureMode: CFString! ``` |
| To | ``` let kCGImagePropertyExifExposureMode: CFString ``` |

Modified [kCGImagePropertyExifExposureProgram](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifexposureprogram)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifExposureProgram: CFString! ``` |
| To | ``` let kCGImagePropertyExifExposureProgram: CFString ``` |

Modified [kCGImagePropertyExifExposureTime](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifexposuretime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifExposureTime: CFString! ``` |
| To | ``` let kCGImagePropertyExifExposureTime: CFString ``` |

Modified [kCGImagePropertyExifFileSource](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiffilesource)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifFileSource: CFString! ``` |
| To | ``` let kCGImagePropertyExifFileSource: CFString ``` |

Modified [kCGImagePropertyExifFlash](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifflash)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifFlash: CFString! ``` |
| To | ``` let kCGImagePropertyExifFlash: CFString ``` |

Modified [kCGImagePropertyExifFlashEnergy](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifflashenergy)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifFlashEnergy: CFString! ``` |
| To | ``` let kCGImagePropertyExifFlashEnergy: CFString ``` |

Modified [kCGImagePropertyExifFlashPixVersion](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifflashpixversion)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifFlashPixVersion: CFString! ``` |
| To | ``` let kCGImagePropertyExifFlashPixVersion: CFString ``` |

Modified [kCGImagePropertyExifFNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiffnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifFNumber: CFString! ``` |
| To | ``` let kCGImagePropertyExifFNumber: CFString ``` |

Modified [kCGImagePropertyExifFocalLength](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiffocallength)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifFocalLength: CFString! ``` |
| To | ``` let kCGImagePropertyExifFocalLength: CFString ``` |

Modified [kCGImagePropertyExifFocalLenIn35mmFilm](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiffocallenin35mmfilm)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifFocalLenIn35mmFilm: CFString! ``` |
| To | ``` let kCGImagePropertyExifFocalLenIn35mmFilm: CFString ``` |

Modified [kCGImagePropertyExifFocalPlaneResolutionUnit](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiffocalplaneresolutionunit)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifFocalPlaneResolutionUnit: CFString! ``` |
| To | ``` let kCGImagePropertyExifFocalPlaneResolutionUnit: CFString ``` |

Modified [kCGImagePropertyExifFocalPlaneXResolution](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiffocalplanexresolution)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifFocalPlaneXResolution: CFString! ``` |
| To | ``` let kCGImagePropertyExifFocalPlaneXResolution: CFString ``` |

Modified [kCGImagePropertyExifFocalPlaneYResolution](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiffocalplaneyresolution)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifFocalPlaneYResolution: CFString! ``` |
| To | ``` let kCGImagePropertyExifFocalPlaneYResolution: CFString ``` |

Modified [kCGImagePropertyExifGainControl](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifgaincontrol)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifGainControl: CFString! ``` |
| To | ``` let kCGImagePropertyExifGainControl: CFString ``` |

Modified [kCGImagePropertyExifGamma](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifgamma)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifGamma: CFString! ``` |
| To | ``` let kCGImagePropertyExifGamma: CFString ``` |

Modified [kCGImagePropertyExifImageUniqueID](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifimageuniqueid)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifImageUniqueID: CFString! ``` |
| To | ``` let kCGImagePropertyExifImageUniqueID: CFString ``` |

Modified [kCGImagePropertyExifISOSpeed](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifisospeed)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifISOSpeed: CFString! ``` |
| To | ``` let kCGImagePropertyExifISOSpeed: CFString ``` |

Modified [kCGImagePropertyExifISOSpeedLatitudeyyy](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifisospeedlatitudeyyy)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifISOSpeedLatitudeyyy: CFString! ``` |
| To | ``` let kCGImagePropertyExifISOSpeedLatitudeyyy: CFString ``` |

Modified [kCGImagePropertyExifISOSpeedLatitudezzz](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifisospeedlatitudezzz)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifISOSpeedLatitudezzz: CFString! ``` |
| To | ``` let kCGImagePropertyExifISOSpeedLatitudezzz: CFString ``` |

Modified [kCGImagePropertyExifISOSpeedRatings](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifisospeedratings)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifISOSpeedRatings: CFString! ``` |
| To | ``` let kCGImagePropertyExifISOSpeedRatings: CFString ``` |

Modified [kCGImagePropertyExifLensMake](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensmake)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifLensMake: CFString! ``` |
| To | ``` let kCGImagePropertyExifLensMake: CFString ``` |

Modified [kCGImagePropertyExifLensModel](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensmodel)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifLensModel: CFString! ``` |
| To | ``` let kCGImagePropertyExifLensModel: CFString ``` |

Modified [kCGImagePropertyExifLensSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifLensSerialNumber: CFString! ``` |
| To | ``` let kCGImagePropertyExifLensSerialNumber: CFString ``` |

Modified [kCGImagePropertyExifLensSpecification](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensspecification)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifLensSpecification: CFString! ``` |
| To | ``` let kCGImagePropertyExifLensSpecification: CFString ``` |

Modified [kCGImagePropertyExifLightSource](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflightsource)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifLightSource: CFString! ``` |
| To | ``` let kCGImagePropertyExifLightSource: CFString ``` |

Modified [kCGImagePropertyExifMakerNote](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifmakernote)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifMakerNote: CFString! ``` |
| To | ``` let kCGImagePropertyExifMakerNote: CFString ``` |

Modified [kCGImagePropertyExifMaxApertureValue](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifmaxaperturevalue)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifMaxApertureValue: CFString! ``` |
| To | ``` let kCGImagePropertyExifMaxApertureValue: CFString ``` |

Modified [kCGImagePropertyExifMeteringMode](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifmeteringmode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifMeteringMode: CFString! ``` |
| To | ``` let kCGImagePropertyExifMeteringMode: CFString ``` |

Modified [kCGImagePropertyExifOECF](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifoecf)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifOECF: CFString! ``` |
| To | ``` let kCGImagePropertyExifOECF: CFString ``` |

Modified [kCGImagePropertyExifPixelXDimension](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifpixelxdimension)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifPixelXDimension: CFString! ``` |
| To | ``` let kCGImagePropertyExifPixelXDimension: CFString ``` |

Modified [kCGImagePropertyExifPixelYDimension](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifpixelydimension)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifPixelYDimension: CFString! ``` |
| To | ``` let kCGImagePropertyExifPixelYDimension: CFString ``` |

Modified [kCGImagePropertyExifRecommendedExposureIndex](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifrecommendedexposureindex)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifRecommendedExposureIndex: CFString! ``` |
| To | ``` let kCGImagePropertyExifRecommendedExposureIndex: CFString ``` |

Modified [kCGImagePropertyExifRelatedSoundFile](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifrelatedsoundfile)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifRelatedSoundFile: CFString! ``` |
| To | ``` let kCGImagePropertyExifRelatedSoundFile: CFString ``` |

Modified [kCGImagePropertyExifSaturation](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsaturation)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSaturation: CFString! ``` |
| To | ``` let kCGImagePropertyExifSaturation: CFString ``` |

Modified [kCGImagePropertyExifSceneCaptureType](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifscenecapturetype)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSceneCaptureType: CFString! ``` |
| To | ``` let kCGImagePropertyExifSceneCaptureType: CFString ``` |

Modified [kCGImagePropertyExifSceneType](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifscenetype)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSceneType: CFString! ``` |
| To | ``` let kCGImagePropertyExifSceneType: CFString ``` |

Modified [kCGImagePropertyExifSensingMethod](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsensingmethod)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSensingMethod: CFString! ``` |
| To | ``` let kCGImagePropertyExifSensingMethod: CFString ``` |

Modified [kCGImagePropertyExifSensitivityType](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsensitivitytype)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSensitivityType: CFString! ``` |
| To | ``` let kCGImagePropertyExifSensitivityType: CFString ``` |

Modified [kCGImagePropertyExifSharpness](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsharpness)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSharpness: CFString! ``` |
| To | ``` let kCGImagePropertyExifSharpness: CFString ``` |

Modified [kCGImagePropertyExifShutterSpeedValue](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifshutterspeedvalue)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifShutterSpeedValue: CFString! ``` |
| To | ``` let kCGImagePropertyExifShutterSpeedValue: CFString ``` |

Modified [kCGImagePropertyExifSpatialFrequencyResponse](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifspatialfrequencyresponse)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSpatialFrequencyResponse: CFString! ``` |
| To | ``` let kCGImagePropertyExifSpatialFrequencyResponse: CFString ``` |

Modified [kCGImagePropertyExifSpectralSensitivity](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifspectralsensitivity)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSpectralSensitivity: CFString! ``` |
| To | ``` let kCGImagePropertyExifSpectralSensitivity: CFString ``` |

Modified [kCGImagePropertyExifStandardOutputSensitivity](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifstandardoutputsensitivity)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifStandardOutputSensitivity: CFString! ``` |
| To | ``` let kCGImagePropertyExifStandardOutputSensitivity: CFString ``` |

Modified [kCGImagePropertyExifSubjectArea](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsubjectarea)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSubjectArea: CFString! ``` |
| To | ``` let kCGImagePropertyExifSubjectArea: CFString ``` |

Modified [kCGImagePropertyExifSubjectDistance](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsubjectdistance)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSubjectDistance: CFString! ``` |
| To | ``` let kCGImagePropertyExifSubjectDistance: CFString ``` |

Modified [kCGImagePropertyExifSubjectDistRange](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsubjectdistrange)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSubjectDistRange: CFString! ``` |
| To | ``` let kCGImagePropertyExifSubjectDistRange: CFString ``` |

Modified [kCGImagePropertyExifSubjectLocation](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsubjectlocation)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSubjectLocation: CFString! ``` |
| To | ``` let kCGImagePropertyExifSubjectLocation: CFString ``` |

Modified [kCGImagePropertyExifSubsecTime](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsubsectime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSubsecTime: CFString! ``` |
| To | ``` let kCGImagePropertyExifSubsecTime: CFString ``` |

Modified [kCGImagePropertyExifSubsecTimeDigitized](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsubsectimedigitized)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSubsecTimeDigitized: CFString! ``` |
| To | ``` let kCGImagePropertyExifSubsecTimeDigitized: CFString ``` |

Modified [kCGImagePropertyExifSubsecTimeOrginal](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifsubsectimeorginal)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifSubsecTimeOrginal: CFString! ``` |
| To | ``` let kCGImagePropertyExifSubsecTimeOrginal: CFString ``` |

Modified [kCGImagePropertyExifUserComment](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifusercomment)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifUserComment: CFString! ``` |
| To | ``` let kCGImagePropertyExifUserComment: CFString ``` |

Modified [kCGImagePropertyExifVersion](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifversion)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifVersion: CFString! ``` |
| To | ``` let kCGImagePropertyExifVersion: CFString ``` |

Modified [kCGImagePropertyExifWhiteBalance](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifwhitebalance)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyExifWhiteBalance: CFString! ``` |
| To | ``` let kCGImagePropertyExifWhiteBalance: CFString ``` |

Modified [kCGImagePropertyFileSize](https://developer.apple.com/documentation/imageio/kcgimagepropertyfilesize)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyFileSize: CFString! ``` |
| To | ``` let kCGImagePropertyFileSize: CFString ``` |

Modified [kCGImagePropertyGIFDelayTime](https://developer.apple.com/documentation/imageio/kcgimagepropertygifdelaytime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGIFDelayTime: CFString! ``` |
| To | ``` let kCGImagePropertyGIFDelayTime: CFString ``` |

Modified [kCGImagePropertyGIFDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertygifdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGIFDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyGIFDictionary: CFString ``` |

Modified [kCGImagePropertyGIFHasGlobalColorMap](https://developer.apple.com/documentation/imageio/kcgimagepropertygifhasglobalcolormap)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGIFHasGlobalColorMap: CFString! ``` |
| To | ``` let kCGImagePropertyGIFHasGlobalColorMap: CFString ``` |

Modified [kCGImagePropertyGIFImageColorMap](https://developer.apple.com/documentation/imageio/kcgimagepropertygifimagecolormap)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGIFImageColorMap: CFString! ``` |
| To | ``` let kCGImagePropertyGIFImageColorMap: CFString ``` |

Modified [kCGImagePropertyGIFLoopCount](https://developer.apple.com/documentation/imageio/kcgimagepropertygifloopcount)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGIFLoopCount: CFString! ``` |
| To | ``` let kCGImagePropertyGIFLoopCount: CFString ``` |

Modified [kCGImagePropertyGIFUnclampedDelayTime](https://developer.apple.com/documentation/imageio/kcgimagepropertygifunclampeddelaytime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGIFUnclampedDelayTime: CFString! ``` |
| To | ``` let kCGImagePropertyGIFUnclampedDelayTime: CFString ``` |

Modified [kCGImagePropertyGPSAltitude](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsaltitude)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSAltitude: CFString! ``` |
| To | ``` let kCGImagePropertyGPSAltitude: CFString ``` |

Modified [kCGImagePropertyGPSAltitudeRef](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsaltituderef)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSAltitudeRef: CFString! ``` |
| To | ``` let kCGImagePropertyGPSAltitudeRef: CFString ``` |

Modified [kCGImagePropertyGPSAreaInformation](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsareainformation)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSAreaInformation: CFString! ``` |
| To | ``` let kCGImagePropertyGPSAreaInformation: CFString ``` |

Modified [kCGImagePropertyGPSDateStamp](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdatestamp)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDateStamp: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDateStamp: CFString ``` |

Modified [kCGImagePropertyGPSDestBearing](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdestbearing)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDestBearing: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDestBearing: CFString ``` |

Modified [kCGImagePropertyGPSDestBearingRef](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdestbearingref)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDestBearingRef: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDestBearingRef: CFString ``` |

Modified [kCGImagePropertyGPSDestDistance](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdestdistance)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDestDistance: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDestDistance: CFString ``` |

Modified [kCGImagePropertyGPSDestDistanceRef](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdestdistanceref)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDestDistanceRef: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDestDistanceRef: CFString ``` |

Modified [kCGImagePropertyGPSDestLatitude](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdestlatitude)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDestLatitude: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDestLatitude: CFString ``` |

Modified [kCGImagePropertyGPSDestLatitudeRef](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdestlatituderef)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDestLatitudeRef: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDestLatitudeRef: CFString ``` |

Modified [kCGImagePropertyGPSDestLongitude](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdestlongitude)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDestLongitude: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDestLongitude: CFString ``` |

Modified [kCGImagePropertyGPSDestLongitudeRef](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdestlongituderef)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDestLongitudeRef: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDestLongitudeRef: CFString ``` |

Modified [kCGImagePropertyGPSDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDictionary: CFString ``` |

Modified [kCGImagePropertyGPSDifferental](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdifferental)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDifferental: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDifferental: CFString ``` |

Modified [kCGImagePropertyGPSDOP](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsdop)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSDOP: CFString! ``` |
| To | ``` let kCGImagePropertyGPSDOP: CFString ``` |

Modified [kCGImagePropertyGPSHPositioningError](https://developer.apple.com/documentation/imageio/kcgimagepropertygpshpositioningerror)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSHPositioningError: CFString! ``` |
| To | ``` let kCGImagePropertyGPSHPositioningError: CFString ``` |

Modified [kCGImagePropertyGPSImgDirection](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsimgdirection)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSImgDirection: CFString! ``` |
| To | ``` let kCGImagePropertyGPSImgDirection: CFString ``` |

Modified [kCGImagePropertyGPSImgDirectionRef](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsimgdirectionref)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSImgDirectionRef: CFString! ``` |
| To | ``` let kCGImagePropertyGPSImgDirectionRef: CFString ``` |

Modified [kCGImagePropertyGPSLatitude](https://developer.apple.com/documentation/imageio/kcgimagepropertygpslatitude)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSLatitude: CFString! ``` |
| To | ``` let kCGImagePropertyGPSLatitude: CFString ``` |

Modified [kCGImagePropertyGPSLatitudeRef](https://developer.apple.com/documentation/imageio/kcgimagepropertygpslatituderef)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSLatitudeRef: CFString! ``` |
| To | ``` let kCGImagePropertyGPSLatitudeRef: CFString ``` |

Modified [kCGImagePropertyGPSLongitude](https://developer.apple.com/documentation/imageio/kcgimagepropertygpslongitude)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSLongitude: CFString! ``` |
| To | ``` let kCGImagePropertyGPSLongitude: CFString ``` |

Modified [kCGImagePropertyGPSLongitudeRef](https://developer.apple.com/documentation/imageio/kcgimagepropertygpslongituderef)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSLongitudeRef: CFString! ``` |
| To | ``` let kCGImagePropertyGPSLongitudeRef: CFString ``` |

Modified [kCGImagePropertyGPSMapDatum](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsmapdatum)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSMapDatum: CFString! ``` |
| To | ``` let kCGImagePropertyGPSMapDatum: CFString ``` |

Modified [kCGImagePropertyGPSMeasureMode](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsmeasuremode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSMeasureMode: CFString! ``` |
| To | ``` let kCGImagePropertyGPSMeasureMode: CFString ``` |

Modified [kCGImagePropertyGPSProcessingMethod](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsprocessingmethod)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSProcessingMethod: CFString! ``` |
| To | ``` let kCGImagePropertyGPSProcessingMethod: CFString ``` |

Modified [kCGImagePropertyGPSSatellites](https://developer.apple.com/documentation/imageio/kcgimagepropertygpssatellites)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSSatellites: CFString! ``` |
| To | ``` let kCGImagePropertyGPSSatellites: CFString ``` |

Modified [kCGImagePropertyGPSSpeed](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsspeed)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSSpeed: CFString! ``` |
| To | ``` let kCGImagePropertyGPSSpeed: CFString ``` |

Modified [kCGImagePropertyGPSSpeedRef](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsspeedref)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSSpeedRef: CFString! ``` |
| To | ``` let kCGImagePropertyGPSSpeedRef: CFString ``` |

Modified [kCGImagePropertyGPSStatus](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsstatus)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSStatus: CFString! ``` |
| To | ``` let kCGImagePropertyGPSStatus: CFString ``` |

Modified [kCGImagePropertyGPSTimeStamp](https://developer.apple.com/documentation/imageio/kcgimagepropertygpstimestamp)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSTimeStamp: CFString! ``` |
| To | ``` let kCGImagePropertyGPSTimeStamp: CFString ``` |

Modified [kCGImagePropertyGPSTrack](https://developer.apple.com/documentation/imageio/kcgimagepropertygpstrack)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSTrack: CFString! ``` |
| To | ``` let kCGImagePropertyGPSTrack: CFString ``` |

Modified [kCGImagePropertyGPSTrackRef](https://developer.apple.com/documentation/imageio/kcgimagepropertygpstrackref)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSTrackRef: CFString! ``` |
| To | ``` let kCGImagePropertyGPSTrackRef: CFString ``` |

Modified [kCGImagePropertyGPSVersion](https://developer.apple.com/documentation/imageio/kcgimagepropertygpsversion)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyGPSVersion: CFString! ``` |
| To | ``` let kCGImagePropertyGPSVersion: CFString ``` |

Modified [kCGImagePropertyHasAlpha](https://developer.apple.com/documentation/imageio/kcgimagepropertyhasalpha)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyHasAlpha: CFString! ``` |
| To | ``` let kCGImagePropertyHasAlpha: CFString ``` |

Modified [kCGImagePropertyIPTCActionAdvised](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcactionadvised)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCActionAdvised: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCActionAdvised: CFString ``` |

Modified [kCGImagePropertyIPTCByline](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcbyline)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCByline: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCByline: CFString ``` |

Modified [kCGImagePropertyIPTCBylineTitle](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcbylinetitle)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCBylineTitle: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCBylineTitle: CFString ``` |

Modified [kCGImagePropertyIPTCCaptionAbstract](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccaptionabstract)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCCaptionAbstract: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCCaptionAbstract: CFString ``` |

Modified [kCGImagePropertyIPTCCategory](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccategory)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCCategory: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCCategory: CFString ``` |

Modified [kCGImagePropertyIPTCCity](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccity)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCCity: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCCity: CFString ``` |

Modified [kCGImagePropertyIPTCContact](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontact)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContact: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContact: CFString ``` |

Modified [kCGImagePropertyIPTCContactInfoAddress](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontactinfoaddress)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContactInfoAddress: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContactInfoAddress: CFString ``` |

Modified [kCGImagePropertyIPTCContactInfoCity](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontactinfocity)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContactInfoCity: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContactInfoCity: CFString ``` |

Modified [kCGImagePropertyIPTCContactInfoCountry](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontactinfocountry)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContactInfoCountry: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContactInfoCountry: CFString ``` |

Modified [kCGImagePropertyIPTCContactInfoEmails](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontactinfoemails)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContactInfoEmails: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContactInfoEmails: CFString ``` |

Modified [kCGImagePropertyIPTCContactInfoPhones](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontactinfophones)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContactInfoPhones: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContactInfoPhones: CFString ``` |

Modified [kCGImagePropertyIPTCContactInfoPostalCode](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontactinfopostalcode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContactInfoPostalCode: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContactInfoPostalCode: CFString ``` |

Modified [kCGImagePropertyIPTCContactInfoStateProvince](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontactinfostateprovince)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContactInfoStateProvince: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContactInfoStateProvince: CFString ``` |

Modified [kCGImagePropertyIPTCContactInfoWebURLs](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontactinfoweburls)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContactInfoWebURLs: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContactInfoWebURLs: CFString ``` |

Modified [kCGImagePropertyIPTCContentLocationCode](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontentlocationcode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContentLocationCode: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContentLocationCode: CFString ``` |

Modified [kCGImagePropertyIPTCContentLocationName](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccontentlocationname)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCContentLocationName: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCContentLocationName: CFString ``` |

Modified [kCGImagePropertyIPTCCopyrightNotice](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccopyrightnotice)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCCopyrightNotice: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCCopyrightNotice: CFString ``` |

Modified [kCGImagePropertyIPTCCountryPrimaryLocationCode](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccountryprimarylocationcode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCCountryPrimaryLocationCode: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCCountryPrimaryLocationCode: CFString ``` |

Modified [kCGImagePropertyIPTCCountryPrimaryLocationName](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccountryprimarylocationname)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCCountryPrimaryLocationName: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCCountryPrimaryLocationName: CFString ``` |

Modified [kCGImagePropertyIPTCCreatorContactInfo](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccreatorcontactinfo)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCCreatorContactInfo: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCCreatorContactInfo: CFString ``` |

Modified [kCGImagePropertyIPTCCredit](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptccredit)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCCredit: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCCredit: CFString ``` |

Modified [kCGImagePropertyIPTCDateCreated](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcdatecreated)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCDateCreated: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCDateCreated: CFString ``` |

Modified [kCGImagePropertyIPTCDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCDictionary: CFString ``` |

Modified [kCGImagePropertyIPTCDigitalCreationDate](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcdigitalcreationdate)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCDigitalCreationDate: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCDigitalCreationDate: CFString ``` |

Modified [kCGImagePropertyIPTCDigitalCreationTime](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcdigitalcreationtime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCDigitalCreationTime: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCDigitalCreationTime: CFString ``` |

Modified [kCGImagePropertyIPTCEditorialUpdate](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptceditorialupdate)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCEditorialUpdate: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCEditorialUpdate: CFString ``` |

Modified [kCGImagePropertyIPTCEditStatus](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptceditstatus)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCEditStatus: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCEditStatus: CFString ``` |

Modified [kCGImagePropertyIPTCExpirationDate](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcexpirationdate)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCExpirationDate: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCExpirationDate: CFString ``` |

Modified [kCGImagePropertyIPTCExpirationTime](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcexpirationtime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCExpirationTime: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCExpirationTime: CFString ``` |

Modified [kCGImagePropertyIPTCFixtureIdentifier](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcfixtureidentifier)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCFixtureIdentifier: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCFixtureIdentifier: CFString ``` |

Modified [kCGImagePropertyIPTCHeadline](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcheadline)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCHeadline: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCHeadline: CFString ``` |

Modified [kCGImagePropertyIPTCImageOrientation](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcimageorientation)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCImageOrientation: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCImageOrientation: CFString ``` |

Modified [kCGImagePropertyIPTCImageType](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcimagetype)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCImageType: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCImageType: CFString ``` |

Modified [kCGImagePropertyIPTCKeywords](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptckeywords)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCKeywords: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCKeywords: CFString ``` |

Modified [kCGImagePropertyIPTCLanguageIdentifier](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptclanguageidentifier)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCLanguageIdentifier: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCLanguageIdentifier: CFString ``` |

Modified [kCGImagePropertyIPTCObjectAttributeReference](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcobjectattributereference)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCObjectAttributeReference: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCObjectAttributeReference: CFString ``` |

Modified [kCGImagePropertyIPTCObjectCycle](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcobjectcycle)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCObjectCycle: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCObjectCycle: CFString ``` |

Modified [kCGImagePropertyIPTCObjectName](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcobjectname)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCObjectName: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCObjectName: CFString ``` |

Modified [kCGImagePropertyIPTCObjectTypeReference](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcobjecttypereference)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCObjectTypeReference: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCObjectTypeReference: CFString ``` |

Modified [kCGImagePropertyIPTCOriginalTransmissionReference](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcoriginaltransmissionreference)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCOriginalTransmissionReference: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCOriginalTransmissionReference: CFString ``` |

Modified [kCGImagePropertyIPTCOriginatingProgram](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcoriginatingprogram)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCOriginatingProgram: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCOriginatingProgram: CFString ``` |

Modified [kCGImagePropertyIPTCProgramVersion](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcprogramversion)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCProgramVersion: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCProgramVersion: CFString ``` |

Modified [kCGImagePropertyIPTCProvinceState](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcprovincestate)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCProvinceState: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCProvinceState: CFString ``` |

Modified [kCGImagePropertyIPTCReferenceDate](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcreferencedate)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCReferenceDate: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCReferenceDate: CFString ``` |

Modified [kCGImagePropertyIPTCReferenceNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcreferencenumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCReferenceNumber: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCReferenceNumber: CFString ``` |

Modified [kCGImagePropertyIPTCReferenceService](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcreferenceservice)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCReferenceService: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCReferenceService: CFString ``` |

Modified [kCGImagePropertyIPTCReleaseDate](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcreleasedate)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCReleaseDate: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCReleaseDate: CFString ``` |

Modified [kCGImagePropertyIPTCReleaseTime](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcreleasetime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCReleaseTime: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCReleaseTime: CFString ``` |

Modified [kCGImagePropertyIPTCRightsUsageTerms](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcrightsusageterms)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCRightsUsageTerms: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCRightsUsageTerms: CFString ``` |

Modified [kCGImagePropertyIPTCScene](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcscene)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCScene: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCScene: CFString ``` |

Modified [kCGImagePropertyIPTCSource](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcsource)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCSource: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCSource: CFString ``` |

Modified [kCGImagePropertyIPTCSpecialInstructions](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcspecialinstructions)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCSpecialInstructions: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCSpecialInstructions: CFString ``` |

Modified [kCGImagePropertyIPTCStarRating](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcstarrating)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCStarRating: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCStarRating: CFString ``` |

Modified [kCGImagePropertyIPTCSubjectReference](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcsubjectreference)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCSubjectReference: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCSubjectReference: CFString ``` |

Modified [kCGImagePropertyIPTCSubLocation](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcsublocation)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCSubLocation: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCSubLocation: CFString ``` |

Modified [kCGImagePropertyIPTCSupplementalCategory](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcsupplementalcategory)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCSupplementalCategory: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCSupplementalCategory: CFString ``` |

Modified [kCGImagePropertyIPTCTimeCreated](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptctimecreated)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCTimeCreated: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCTimeCreated: CFString ``` |

Modified [kCGImagePropertyIPTCUrgency](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcurgency)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCUrgency: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCUrgency: CFString ``` |

Modified [kCGImagePropertyIPTCWriterEditor](https://developer.apple.com/documentation/imageio/kcgimagepropertyiptcwritereditor)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIPTCWriterEditor: CFString! ``` |
| To | ``` let kCGImagePropertyIPTCWriterEditor: CFString ``` |

Modified [kCGImagePropertyIsFloat](https://developer.apple.com/documentation/imageio/kcgimagepropertyisfloat)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIsFloat: CFString! ``` |
| To | ``` let kCGImagePropertyIsFloat: CFString ``` |

Modified [kCGImagePropertyIsIndexed](https://developer.apple.com/documentation/imageio/kcgimagepropertyisindexed)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyIsIndexed: CFString! ``` |
| To | ``` let kCGImagePropertyIsIndexed: CFString ``` |

Modified [kCGImagePropertyJFIFDensityUnit](https://developer.apple.com/documentation/imageio/kcgimagepropertyjfifdensityunit)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyJFIFDensityUnit: CFString! ``` |
| To | ``` let kCGImagePropertyJFIFDensityUnit: CFString ``` |

Modified [kCGImagePropertyJFIFDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertyjfifdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyJFIFDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyJFIFDictionary: CFString ``` |

Modified [kCGImagePropertyJFIFIsProgressive](https://developer.apple.com/documentation/imageio/kcgimagepropertyjfifisprogressive)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyJFIFIsProgressive: CFString! ``` |
| To | ``` let kCGImagePropertyJFIFIsProgressive: CFString ``` |

Modified [kCGImagePropertyJFIFVersion](https://developer.apple.com/documentation/imageio/kcgimagepropertyjfifversion)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyJFIFVersion: CFString! ``` |
| To | ``` let kCGImagePropertyJFIFVersion: CFString ``` |

Modified [kCGImagePropertyJFIFXDensity](https://developer.apple.com/documentation/imageio/kcgimagepropertyjfifxdensity)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyJFIFXDensity: CFString! ``` |
| To | ``` let kCGImagePropertyJFIFXDensity: CFString ``` |

Modified [kCGImagePropertyJFIFYDensity](https://developer.apple.com/documentation/imageio/kcgimagepropertyjfifydensity)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyJFIFYDensity: CFString! ``` |
| To | ``` let kCGImagePropertyJFIFYDensity: CFString ``` |

Modified [kCGImagePropertyMakerAppleDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerappledictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerAppleDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyMakerAppleDictionary: CFString ``` |

Modified [kCGImagePropertyMakerCanonAspectRatioInfo](https://developer.apple.com/documentation/imageio/kcgimagepropertymakercanonaspectratioinfo)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerCanonAspectRatioInfo: CFString! ``` |
| To | ``` let kCGImagePropertyMakerCanonAspectRatioInfo: CFString ``` |

Modified [kCGImagePropertyMakerCanonCameraSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertymakercanoncameraserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerCanonCameraSerialNumber: CFString! ``` |
| To | ``` let kCGImagePropertyMakerCanonCameraSerialNumber: CFString ``` |

Modified [kCGImagePropertyMakerCanonContinuousDrive](https://developer.apple.com/documentation/imageio/kcgimagepropertymakercanoncontinuousdrive)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerCanonContinuousDrive: CFString! ``` |
| To | ``` let kCGImagePropertyMakerCanonContinuousDrive: CFString ``` |

Modified [kCGImagePropertyMakerCanonDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakercanondictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerCanonDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyMakerCanonDictionary: CFString ``` |

Modified [kCGImagePropertyMakerCanonFirmware](https://developer.apple.com/documentation/imageio/kcgimagepropertymakercanonfirmware)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerCanonFirmware: CFString! ``` |
| To | ``` let kCGImagePropertyMakerCanonFirmware: CFString ``` |

Modified [kCGImagePropertyMakerCanonFlashExposureComp](https://developer.apple.com/documentation/imageio/kcgimagepropertymakercanonflashexposurecomp)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerCanonFlashExposureComp: CFString! ``` |
| To | ``` let kCGImagePropertyMakerCanonFlashExposureComp: CFString ``` |

Modified [kCGImagePropertyMakerCanonImageSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertymakercanonimageserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerCanonImageSerialNumber: CFString! ``` |
| To | ``` let kCGImagePropertyMakerCanonImageSerialNumber: CFString ``` |

Modified [kCGImagePropertyMakerCanonLensModel](https://developer.apple.com/documentation/imageio/kcgimagepropertymakercanonlensmodel)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerCanonLensModel: CFString! ``` |
| To | ``` let kCGImagePropertyMakerCanonLensModel: CFString ``` |

Modified [kCGImagePropertyMakerCanonOwnerName](https://developer.apple.com/documentation/imageio/kcgimagepropertymakercanonownername)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerCanonOwnerName: CFString! ``` |
| To | ``` let kCGImagePropertyMakerCanonOwnerName: CFString ``` |

Modified [kCGImagePropertyMakerFujiDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerfujidictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerFujiDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyMakerFujiDictionary: CFString ``` |

Modified [kCGImagePropertyMakerMinoltaDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerminoltadictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerMinoltaDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyMakerMinoltaDictionary: CFString ``` |

Modified [kCGImagePropertyMakerNikonCameraSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikoncameraserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonCameraSerialNumber: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonCameraSerialNumber: CFString ``` |

Modified [kCGImagePropertyMakerNikonColorMode](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikoncolormode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonColorMode: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonColorMode: CFString ``` |

Modified [kCGImagePropertyMakerNikonDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikondictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonDictionary: CFString ``` |

Modified [kCGImagePropertyMakerNikonDigitalZoom](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikondigitalzoom)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonDigitalZoom: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonDigitalZoom: CFString ``` |

Modified [kCGImagePropertyMakerNikonFlashExposureComp](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonflashexposurecomp)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonFlashExposureComp: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonFlashExposureComp: CFString ``` |

Modified [kCGImagePropertyMakerNikonFlashSetting](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonflashsetting)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonFlashSetting: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonFlashSetting: CFString ``` |

Modified [kCGImagePropertyMakerNikonFocusDistance](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonfocusdistance)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonFocusDistance: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonFocusDistance: CFString ``` |

Modified [kCGImagePropertyMakerNikonFocusMode](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonfocusmode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonFocusMode: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonFocusMode: CFString ``` |

Modified [kCGImagePropertyMakerNikonImageAdjustment](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonimageadjustment)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonImageAdjustment: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonImageAdjustment: CFString ``` |

Modified [kCGImagePropertyMakerNikonISOSelection](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonisoselection)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonISOSelection: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonISOSelection: CFString ``` |

Modified [kCGImagePropertyMakerNikonISOSetting](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonisosetting)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonISOSetting: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonISOSetting: CFString ``` |

Modified [kCGImagePropertyMakerNikonLensAdapter](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonlensadapter)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonLensAdapter: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonLensAdapter: CFString ``` |

Modified [kCGImagePropertyMakerNikonLensInfo](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonlensinfo)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonLensInfo: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonLensInfo: CFString ``` |

Modified [kCGImagePropertyMakerNikonLensType](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonlenstype)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonLensType: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonLensType: CFString ``` |

Modified [kCGImagePropertyMakerNikonQuality](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonquality)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonQuality: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonQuality: CFString ``` |

Modified [kCGImagePropertyMakerNikonSharpenMode](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonsharpenmode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonSharpenMode: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonSharpenMode: CFString ``` |

Modified [kCGImagePropertyMakerNikonShootingMode](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonshootingmode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonShootingMode: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonShootingMode: CFString ``` |

Modified [kCGImagePropertyMakerNikonShutterCount](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonshuttercount)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonShutterCount: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonShutterCount: CFString ``` |

Modified [kCGImagePropertyMakerNikonWhiteBalanceMode](https://developer.apple.com/documentation/imageio/kcgimagepropertymakernikonwhitebalancemode)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerNikonWhiteBalanceMode: CFString! ``` |
| To | ``` let kCGImagePropertyMakerNikonWhiteBalanceMode: CFString ``` |

Modified [kCGImagePropertyMakerOlympusDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerolympusdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerOlympusDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyMakerOlympusDictionary: CFString ``` |

Modified [kCGImagePropertyMakerPentaxDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertymakerpentaxdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyMakerPentaxDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyMakerPentaxDictionary: CFString ``` |

Modified [kCGImagePropertyOpenEXRAspectRatio](https://developer.apple.com/documentation/imageio/kcgimagepropertyopenexraspectratio)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyOpenEXRAspectRatio: CFString! ``` |
| To | ``` let kCGImagePropertyOpenEXRAspectRatio: CFString ``` |

Modified [kCGImagePropertyOpenEXRDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertyopenexrdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyOpenEXRDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyOpenEXRDictionary: CFString ``` |

Modified [kCGImagePropertyOrientation](https://developer.apple.com/documentation/imageio/kcgimagepropertyorientation)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyOrientation: CFString! ``` |
| To | ``` let kCGImagePropertyOrientation: CFString ``` |

Modified [kCGImagePropertyPixelHeight](https://developer.apple.com/documentation/imageio/kcgimagepropertypixelheight)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPixelHeight: CFString! ``` |
| To | ``` let kCGImagePropertyPixelHeight: CFString ``` |

Modified [kCGImagePropertyPixelWidth](https://developer.apple.com/documentation/imageio/kcgimagepropertypixelwidth)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPixelWidth: CFString! ``` |
| To | ``` let kCGImagePropertyPixelWidth: CFString ``` |

Modified [kCGImagePropertyPNGAuthor](https://developer.apple.com/documentation/imageio/kcgimagepropertypngauthor)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGAuthor: CFString! ``` |
| To | ``` let kCGImagePropertyPNGAuthor: CFString ``` |

Modified [kCGImagePropertyPNGChromaticities](https://developer.apple.com/documentation/imageio/kcgimagepropertypngchromaticities)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGChromaticities: CFString! ``` |
| To | ``` let kCGImagePropertyPNGChromaticities: CFString ``` |

Modified [kCGImagePropertyPNGCopyright](https://developer.apple.com/documentation/imageio/kcgimagepropertypngcopyright)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGCopyright: CFString! ``` |
| To | ``` let kCGImagePropertyPNGCopyright: CFString ``` |

Modified [kCGImagePropertyPNGCreationTime](https://developer.apple.com/documentation/imageio/kcgimagepropertypngcreationtime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGCreationTime: CFString! ``` |
| To | ``` let kCGImagePropertyPNGCreationTime: CFString ``` |

Modified [kCGImagePropertyPNGDescription](https://developer.apple.com/documentation/imageio/kcgimagepropertypngdescription)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGDescription: CFString! ``` |
| To | ``` let kCGImagePropertyPNGDescription: CFString ``` |

Modified [kCGImagePropertyPNGDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertypngdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyPNGDictionary: CFString ``` |

Modified [kCGImagePropertyPNGGamma](https://developer.apple.com/documentation/imageio/kcgimagepropertypnggamma)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGGamma: CFString! ``` |
| To | ``` let kCGImagePropertyPNGGamma: CFString ``` |

Modified [kCGImagePropertyPNGInterlaceType](https://developer.apple.com/documentation/imageio/kcgimagepropertypnginterlacetype)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGInterlaceType: CFString! ``` |
| To | ``` let kCGImagePropertyPNGInterlaceType: CFString ``` |

Modified [kCGImagePropertyPNGModificationTime](https://developer.apple.com/documentation/imageio/kcgimagepropertypngmodificationtime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGModificationTime: CFString! ``` |
| To | ``` let kCGImagePropertyPNGModificationTime: CFString ``` |

Modified [kCGImagePropertyPNGSoftware](https://developer.apple.com/documentation/imageio/kcgimagepropertypngsoftware)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGSoftware: CFString! ``` |
| To | ``` let kCGImagePropertyPNGSoftware: CFString ``` |

Modified [kCGImagePropertyPNGsRGBIntent](https://developer.apple.com/documentation/imageio/kcgimagepropertypngsrgbintent)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGsRGBIntent: CFString! ``` |
| To | ``` let kCGImagePropertyPNGsRGBIntent: CFString ``` |

Modified [kCGImagePropertyPNGTitle](https://developer.apple.com/documentation/imageio/kcgimagepropertypngtitle)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGTitle: CFString! ``` |
| To | ``` let kCGImagePropertyPNGTitle: CFString ``` |

Modified [kCGImagePropertyPNGXPixelsPerMeter](https://developer.apple.com/documentation/imageio/kcgimagepropertypngxpixelspermeter)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGXPixelsPerMeter: CFString! ``` |
| To | ``` let kCGImagePropertyPNGXPixelsPerMeter: CFString ``` |

Modified [kCGImagePropertyPNGYPixelsPerMeter](https://developer.apple.com/documentation/imageio/kcgimagepropertypngypixelspermeter)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyPNGYPixelsPerMeter: CFString! ``` |
| To | ``` let kCGImagePropertyPNGYPixelsPerMeter: CFString ``` |

Modified [kCGImagePropertyProfileName](https://developer.apple.com/documentation/imageio/kcgimagepropertyprofilename)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyProfileName: CFString! ``` |
| To | ``` let kCGImagePropertyProfileName: CFString ``` |

Modified [kCGImagePropertyRawDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertyrawdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyRawDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyRawDictionary: CFString ``` |

Modified [kCGImagePropertyTIFFArtist](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffartist)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFArtist: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFArtist: CFString ``` |

Modified [kCGImagePropertyTIFFCompression](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffcompression)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFCompression: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFCompression: CFString ``` |

Modified [kCGImagePropertyTIFFCopyright](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffcopyright)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFCopyright: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFCopyright: CFString ``` |

Modified [kCGImagePropertyTIFFDateTime](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffdatetime)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFDateTime: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFDateTime: CFString ``` |

Modified [kCGImagePropertyTIFFDictionary](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffdictionary)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFDictionary: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFDictionary: CFString ``` |

Modified [kCGImagePropertyTIFFDocumentName](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffdocumentname)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFDocumentName: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFDocumentName: CFString ``` |

Modified [kCGImagePropertyTIFFHostComputer](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffhostcomputer)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFHostComputer: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFHostComputer: CFString ``` |

Modified [kCGImagePropertyTIFFImageDescription](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffimagedescription)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFImageDescription: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFImageDescription: CFString ``` |

Modified [kCGImagePropertyTIFFMake](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffmake)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFMake: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFMake: CFString ``` |

Modified [kCGImagePropertyTIFFModel](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffmodel)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFModel: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFModel: CFString ``` |

Modified [kCGImagePropertyTIFFOrientation](https://developer.apple.com/documentation/imageio/kcgimagepropertytifforientation)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFOrientation: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFOrientation: CFString ``` |

Modified [kCGImagePropertyTIFFPhotometricInterpretation](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffphotometricinterpretation)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFPhotometricInterpretation: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFPhotometricInterpretation: CFString ``` |

Modified [kCGImagePropertyTIFFPrimaryChromaticities](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffprimarychromaticities)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFPrimaryChromaticities: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFPrimaryChromaticities: CFString ``` |

Modified [kCGImagePropertyTIFFResolutionUnit](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffresolutionunit)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFResolutionUnit: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFResolutionUnit: CFString ``` |

Modified [kCGImagePropertyTIFFSoftware](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffsoftware)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFSoftware: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFSoftware: CFString ``` |

Modified [kCGImagePropertyTIFFTransferFunction](https://developer.apple.com/documentation/imageio/kcgimagepropertytifftransferfunction)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFTransferFunction: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFTransferFunction: CFString ``` |

Modified [kCGImagePropertyTIFFWhitePoint](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffwhitepoint)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFWhitePoint: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFWhitePoint: CFString ``` |

Modified [kCGImagePropertyTIFFXResolution](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffxresolution)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFXResolution: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFXResolution: CFString ``` |

Modified [kCGImagePropertyTIFFYResolution](https://developer.apple.com/documentation/imageio/kcgimagepropertytiffyresolution)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImagePropertyTIFFYResolution: CFString! ``` |
| To | ``` let kCGImagePropertyTIFFYResolution: CFString ``` |

Modified [kCGImageSourceCreateThumbnailFromImageAlways](https://developer.apple.com/documentation/imageio/kcgimagesourcecreatethumbnailfromimagealways)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageSourceCreateThumbnailFromImageAlways: CFString! ``` |
| To | ``` let kCGImageSourceCreateThumbnailFromImageAlways: CFString ``` |

Modified [kCGImageSourceCreateThumbnailFromImageIfAbsent](https://developer.apple.com/documentation/imageio/kcgimagesourcecreatethumbnailfromimageifabsent)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageSourceCreateThumbnailFromImageIfAbsent: CFString! ``` |
| To | ``` let kCGImageSourceCreateThumbnailFromImageIfAbsent: CFString ``` |

Modified [kCGImageSourceCreateThumbnailWithTransform](https://developer.apple.com/documentation/imageio/kcgimagesourcecreatethumbnailwithtransform)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageSourceCreateThumbnailWithTransform: CFString! ``` |
| To | ``` let kCGImageSourceCreateThumbnailWithTransform: CFString ``` |

Modified [kCGImageSourceShouldAllowFloat](https://developer.apple.com/documentation/imageio/kcgimagesourceshouldallowfloat)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageSourceShouldAllowFloat: CFString! ``` |
| To | ``` let kCGImageSourceShouldAllowFloat: CFString ``` |

Modified [kCGImageSourceShouldCache](https://developer.apple.com/documentation/imageio/kcgimagesourceshouldcache)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageSourceShouldCache: CFString! ``` |
| To | ``` let kCGImageSourceShouldCache: CFString ``` |

Modified [kCGImageSourceShouldCacheImmediately](https://developer.apple.com/documentation/imageio/kcgimagesourceshouldcacheimmediately)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageSourceShouldCacheImmediately: CFString! ``` |
| To | ``` let kCGImageSourceShouldCacheImmediately: CFString ``` |

Modified [kCGImageSourceThumbnailMaxPixelSize](https://developer.apple.com/documentation/imageio/kcgimagesourcethumbnailmaxpixelsize)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageSourceThumbnailMaxPixelSize: CFString! ``` |
| To | ``` let kCGImageSourceThumbnailMaxPixelSize: CFString ``` |

Modified [kCGImageSourceTypeIdentifierHint](https://developer.apple.com/documentation/imageio/kcgimagesourcetypeidentifierhint)

|  | Declaration |
| --- | --- |
| From | ``` let kCGImageSourceTypeIdentifierHint: CFString! ``` |
| To | ``` let kCGImageSourceTypeIdentifierHint: CFString ``` |

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
