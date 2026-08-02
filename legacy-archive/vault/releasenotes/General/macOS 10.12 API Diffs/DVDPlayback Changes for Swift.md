---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/DVDPlayback.html
archived_at: '2026-07-18T02:51:13.123106Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# DVDPlayback Changes for Swift

### DVDPlayback

Modified DVDAspectRatio [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum DVDAspectRatio : Int16 {     case RatioUninitialized     case Ratio4x3     case Ratio4x3PanAndScan     case Ratio16x9     case RatioLetterBox } ``` |
| To | ``` enum DVDAspectRatio : Int16 {     case ratioUninitialized     case ratio4x3     case ratio4x3PanAndScan     case ratio16x9     case ratioLetterBox } ``` |

Modified DVDAspectRatio.ratio16x9

|  | Declaration |
| --- | --- |
| From | ``` case Ratio16x9 ``` |
| To | ``` case ratio16x9 ``` |

Modified DVDAspectRatio.ratio4x3

|  | Declaration |
| --- | --- |
| From | ``` case Ratio4x3 ``` |
| To | ``` case ratio4x3 ``` |

Modified DVDAspectRatio.ratio4x3PanAndScan

|  | Declaration |
| --- | --- |
| From | ``` case Ratio4x3PanAndScan ``` |
| To | ``` case ratio4x3PanAndScan ``` |

Modified DVDAspectRatio.ratioLetterBox

|  | Declaration |
| --- | --- |
| From | ``` case RatioLetterBox ``` |
| To | ``` case ratioLetterBox ``` |

Modified DVDAspectRatio.ratioUninitialized

|  | Declaration |
| --- | --- |
| From | ``` case RatioUninitialized ``` |
| To | ``` case ratioUninitialized ``` |

Modified DVDAudioFormat [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum DVDAudioFormat : Int16 {     case UnknownFormat     case AC3Format     case MPEG1Format     case MPEG2Format     case PCMFormat     case DTSFormat     case SDDSFormat     case MLPFormat     case DDPlusFormat     case DTSHDFormat } ``` |
| To | ``` enum DVDAudioFormat : Int16 {     case unknownFormat     case ac3Format     case mpeg1Format     case mpeg2Format     case pcmFormat     case dtsFormat     case sddsFormat     case mlpFormat     case ddPlusFormat     case dtshdFormat } ``` |

Modified DVDAudioFormat.ac3Format

|  | Declaration |
| --- | --- |
| From | ``` case AC3Format ``` |
| To | ``` case ac3Format ``` |

Modified DVDAudioFormat.ddPlusFormat

|  | Declaration |
| --- | --- |
| From | ``` case DDPlusFormat ``` |
| To | ``` case ddPlusFormat ``` |

Modified DVDAudioFormat.dtsFormat

|  | Declaration |
| --- | --- |
| From | ``` case DTSFormat ``` |
| To | ``` case dtsFormat ``` |

Modified DVDAudioFormat.dtshdFormat

|  | Declaration |
| --- | --- |
| From | ``` case DTSHDFormat ``` |
| To | ``` case dtshdFormat ``` |

Modified DVDAudioFormat.mlpFormat

|  | Declaration |
| --- | --- |
| From | ``` case MLPFormat ``` |
| To | ``` case mlpFormat ``` |

Modified DVDAudioFormat.mpeg1Format

|  | Declaration |
| --- | --- |
| From | ``` case MPEG1Format ``` |
| To | ``` case mpeg1Format ``` |

Modified DVDAudioFormat.mpeg2Format

|  | Declaration |
| --- | --- |
| From | ``` case MPEG2Format ``` |
| To | ``` case mpeg2Format ``` |

Modified DVDAudioFormat.pcmFormat

|  | Declaration |
| --- | --- |
| From | ``` case PCMFormat ``` |
| To | ``` case pcmFormat ``` |

Modified DVDAudioFormat.sddsFormat

|  | Declaration |
| --- | --- |
| From | ``` case SDDSFormat ``` |
| To | ``` case sddsFormat ``` |

Modified DVDAudioFormat.unknownFormat

|  | Declaration |
| --- | --- |
| From | ``` case UnknownFormat ``` |
| To | ``` case unknownFormat ``` |

Modified DVDDomainCode [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum DVDDomainCode : UInt32 {     case DVDFPDomain     case DVDVMGMDomain     case DVDVTSMDomain     case DVDTTDomain     case DVDSTOPDomain     case DVDAMGMDomain     case DVDTTGRDomain } ``` |
| To | ``` enum DVDDomainCode : UInt32 {     case dvdfpDomain     case dvdvmgmDomain     case dvdvtsmDomain     case dvdttDomain     case dvdstopDomain     case dvdamgmDomain     case dvdttgrDomain } ``` |

Modified DVDDomainCode.dvdamgmDomain

|  | Declaration |
| --- | --- |
| From | ``` case DVDAMGMDomain ``` |
| To | ``` case dvdamgmDomain ``` |

Modified DVDDomainCode.dvdfpDomain

|  | Declaration |
| --- | --- |
| From | ``` case DVDFPDomain ``` |
| To | ``` case dvdfpDomain ``` |

Modified DVDDomainCode.dvdstopDomain

|  | Declaration |
| --- | --- |
| From | ``` case DVDSTOPDomain ``` |
| To | ``` case dvdstopDomain ``` |

Modified DVDDomainCode.dvdttDomain

|  | Declaration |
| --- | --- |
| From | ``` case DVDTTDomain ``` |
| To | ``` case dvdttDomain ``` |

Modified DVDDomainCode.dvdttgrDomain

|  | Declaration |
| --- | --- |
| From | ``` case DVDTTGRDomain ``` |
| To | ``` case dvdttgrDomain ``` |

Modified DVDDomainCode.dvdvmgmDomain

|  | Declaration |
| --- | --- |
| From | ``` case DVDVMGMDomain ``` |
| To | ``` case dvdvmgmDomain ``` |

Modified DVDDomainCode.dvdvtsmDomain

|  | Declaration |
| --- | --- |
| From | ``` case DVDVTSMDomain ``` |
| To | ``` case dvdvtsmDomain ``` |

Modified DVDEventCode [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum DVDEventCode : UInt32 {     case Title     case PTT     case ValidUOP     case Angle     case AudioStream     case SubpictureStream     case DisplayMode     case Domain     case Bitrate     case Still     case Playback     case VideoStandard     case Streams     case ScanSpeed     case MenuCalled     case Parental     case PGC     case GPRM     case RegionMismatch     case TitleTime     case SubpictureStreamNumbers     case AudioStreamNumbers     case AngleNumbers     case Error     case CCInfo     case ChapterTime } ``` |
| To | ``` enum DVDEventCode : UInt32 {     case title     case PTT     case validUOP     case angle     case audioStream     case subpictureStream     case displayMode     case domain     case bitrate     case still     case playback     case videoStandard     case streams     case scanSpeed     case menuCalled     case parental     case PGC     case GPRM     case regionMismatch     case titleTime     case subpictureStreamNumbers     case audioStreamNumbers     case angleNumbers     case error     case ccInfo     case chapterTime } ``` |

Modified DVDEventCode.angle

|  | Declaration |
| --- | --- |
| From | ``` case Angle ``` |
| To | ``` case angle ``` |

Modified DVDEventCode.angleNumbers

|  | Declaration |
| --- | --- |
| From | ``` case AngleNumbers ``` |
| To | ``` case angleNumbers ``` |

Modified DVDEventCode.audioStream

|  | Declaration |
| --- | --- |
| From | ``` case AudioStream ``` |
| To | ``` case audioStream ``` |

Modified DVDEventCode.audioStreamNumbers

|  | Declaration |
| --- | --- |
| From | ``` case AudioStreamNumbers ``` |
| To | ``` case audioStreamNumbers ``` |

Modified DVDEventCode.bitrate

|  | Declaration |
| --- | --- |
| From | ``` case Bitrate ``` |
| To | ``` case bitrate ``` |

Modified DVDEventCode.ccInfo

|  | Declaration |
| --- | --- |
| From | ``` case CCInfo ``` |
| To | ``` case ccInfo ``` |

Modified DVDEventCode.chapterTime

|  | Declaration |
| --- | --- |
| From | ``` case ChapterTime ``` |
| To | ``` case chapterTime ``` |

Modified DVDEventCode.displayMode

|  | Declaration |
| --- | --- |
| From | ``` case DisplayMode ``` |
| To | ``` case displayMode ``` |

Modified DVDEventCode.domain

|  | Declaration |
| --- | --- |
| From | ``` case Domain ``` |
| To | ``` case domain ``` |

Modified DVDEventCode.error

|  | Declaration |
| --- | --- |
| From | ``` case Error ``` |
| To | ``` case error ``` |

Modified DVDEventCode.menuCalled

|  | Declaration |
| --- | --- |
| From | ``` case MenuCalled ``` |
| To | ``` case menuCalled ``` |

Modified DVDEventCode.parental

|  | Declaration |
| --- | --- |
| From | ``` case Parental ``` |
| To | ``` case parental ``` |

Modified DVDEventCode.playback

|  | Declaration |
| --- | --- |
| From | ``` case Playback ``` |
| To | ``` case playback ``` |

Modified DVDEventCode.regionMismatch

|  | Declaration |
| --- | --- |
| From | ``` case RegionMismatch ``` |
| To | ``` case regionMismatch ``` |

Modified DVDEventCode.scanSpeed

|  | Declaration |
| --- | --- |
| From | ``` case ScanSpeed ``` |
| To | ``` case scanSpeed ``` |

Modified DVDEventCode.still

|  | Declaration |
| --- | --- |
| From | ``` case Still ``` |
| To | ``` case still ``` |

Modified DVDEventCode.streams

|  | Declaration |
| --- | --- |
| From | ``` case Streams ``` |
| To | ``` case streams ``` |

Modified DVDEventCode.subpictureStream

|  | Declaration |
| --- | --- |
| From | ``` case SubpictureStream ``` |
| To | ``` case subpictureStream ``` |

Modified DVDEventCode.subpictureStreamNumbers

|  | Declaration |
| --- | --- |
| From | ``` case SubpictureStreamNumbers ``` |
| To | ``` case subpictureStreamNumbers ``` |

Modified DVDEventCode.title

|  | Declaration |
| --- | --- |
| From | ``` case Title ``` |
| To | ``` case title ``` |

Modified DVDEventCode.titleTime

|  | Declaration |
| --- | --- |
| From | ``` case TitleTime ``` |
| To | ``` case titleTime ``` |

Modified DVDEventCode.validUOP

|  | Declaration |
| --- | --- |
| From | ``` case ValidUOP ``` |
| To | ``` case validUOP ``` |

Modified DVDEventCode.videoStandard

|  | Declaration |
| --- | --- |
| From | ``` case VideoStandard ``` |
| To | ``` case videoStandard ``` |

Modified DVDFormat [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum DVDFormat : Int16 {     case Uninitialized     case NTSC     case PAL     case NTSC_HDTV     case PAL_HDTV } ``` |
| To | ``` enum DVDFormat : Int16 {     case uninitialized     case NTSC     case PAL     case NTSC_HDTV     case PAL_HDTV } ``` |

Modified DVDFormat.uninitialized

|  | Declaration |
| --- | --- |
| From | ``` case Uninitialized ``` |
| To | ``` case uninitialized ``` |

Modified DVDMenu [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum DVDMenu : UInt32 {     case Title     case Root     case SubPicture     case Audio     case Angle     case PTT     case None } ``` |
| To | ``` enum DVDMenu : UInt32 {     case title     case root     case subPicture     case audio     case angle     case PTT     case none } ``` |

Modified DVDMenu.angle

|  | Declaration |
| --- | --- |
| From | ``` case Angle ``` |
| To | ``` case angle ``` |

Modified DVDMenu.audio

|  | Declaration |
| --- | --- |
| From | ``` case Audio ``` |
| To | ``` case audio ``` |

Modified DVDMenu.none

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified DVDMenu.root

|  | Declaration |
| --- | --- |
| From | ``` case Root ``` |
| To | ``` case root ``` |

Modified DVDMenu.subPicture

|  | Declaration |
| --- | --- |
| From | ``` case SubPicture ``` |
| To | ``` case subPicture ``` |

Modified DVDMenu.title

|  | Declaration |
| --- | --- |
| From | ``` case Title ``` |
| To | ``` case title ``` |

Modified DVDScanDirection [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum DVDScanDirection : Int8 {     case Forward     case Backward } ``` |
| To | ``` enum DVDScanDirection : Int8 {     case forward     case backward } ``` |

Modified DVDScanDirection.backward

|  | Declaration |
| --- | --- |
| From | ``` case Backward ``` |
| To | ``` case backward ``` |

Modified DVDScanDirection.forward

|  | Declaration |
| --- | --- |
| From | ``` case Forward ``` |
| To | ``` case forward ``` |

Modified DVDScanRate [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum DVDScanRate : Int16 {     case RateOneEigth     case RateOneFourth     case RateOneHalf     case Rate1x     case Rate2x     case Rate4x     case Rate8x     case Rate16x     case Rate32x } ``` |
| To | ``` enum DVDScanRate : Int16 {     case rateOneEigth     case rateOneFourth     case rateOneHalf     case rate1x     case rate2x     case rate4x     case rate8x     case rate16x     case rate32x } ``` |

Modified DVDScanRate.rate16x

|  | Declaration |
| --- | --- |
| From | ``` case Rate16x ``` |
| To | ``` case rate16x ``` |

Modified DVDScanRate.rate1x

|  | Declaration |
| --- | --- |
| From | ``` case Rate1x ``` |
| To | ``` case rate1x ``` |

Modified DVDScanRate.rate2x

|  | Declaration |
| --- | --- |
| From | ``` case Rate2x ``` |
| To | ``` case rate2x ``` |

Modified DVDScanRate.rate32x

|  | Declaration |
| --- | --- |
| From | ``` case Rate32x ``` |
| To | ``` case rate32x ``` |

Modified DVDScanRate.rate4x

|  | Declaration |
| --- | --- |
| From | ``` case Rate4x ``` |
| To | ``` case rate4x ``` |

Modified DVDScanRate.rate8x

|  | Declaration |
| --- | --- |
| From | ``` case Rate8x ``` |
| To | ``` case rate8x ``` |

Modified DVDScanRate.rateOneEigth

|  | Declaration |
| --- | --- |
| From | ``` case RateOneEigth ``` |
| To | ``` case rateOneEigth ``` |

Modified DVDScanRate.rateOneFourth

|  | Declaration |
| --- | --- |
| From | ``` case RateOneFourth ``` |
| To | ``` case rateOneFourth ``` |

Modified DVDScanRate.rateOneHalf

|  | Declaration |
| --- | --- |
| From | ``` case RateOneHalf ``` |
| To | ``` case rateOneHalf ``` |

Modified DVDState [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum DVDState : OSStatus {     case Unknown     case Playing     case PlayingStill     case Paused     case Stopped     case Scanning     case Idle     case PlayingSlow } ``` |
| To | ``` enum DVDState : OSStatus {     case unknown     case playing     case playingStill     case paused     case stopped     case scanning     case idle     case playingSlow } ``` |

Modified DVDState.idle

|  | Declaration |
| --- | --- |
| From | ``` case Idle ``` |
| To | ``` case idle ``` |

Modified DVDState.paused

|  | Declaration |
| --- | --- |
| From | ``` case Paused ``` |
| To | ``` case paused ``` |

Modified DVDState.playing

|  | Declaration |
| --- | --- |
| From | ``` case Playing ``` |
| To | ``` case playing ``` |

Modified DVDState.playingSlow

|  | Declaration |
| --- | --- |
| From | ``` case PlayingSlow ``` |
| To | ``` case playingSlow ``` |

Modified DVDState.playingStill

|  | Declaration |
| --- | --- |
| From | ``` case PlayingStill ``` |
| To | ``` case playingStill ``` |

Modified DVDState.scanning

|  | Declaration |
| --- | --- |
| From | ``` case Scanning ``` |
| To | ``` case scanning ``` |

Modified DVDState.stopped

|  | Declaration |
| --- | --- |
| From | ``` case Stopped ``` |
| To | ``` case stopped ``` |

Modified DVDState.unknown

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified DVDUserNavigation [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum DVDUserNavigation : UInt32 {     case MoveUp     case MoveDown     case MoveLeft     case MoveRight     case Enter } ``` |
| To | ``` enum DVDUserNavigation : UInt32 {     case moveUp     case moveDown     case moveLeft     case moveRight     case enter } ``` |

Modified DVDUserNavigation.enter

|  | Declaration |
| --- | --- |
| From | ``` case Enter ``` |
| To | ``` case enter ``` |

Modified DVDUserNavigation.moveDown

|  | Declaration |
| --- | --- |
| From | ``` case MoveDown ``` |
| To | ``` case moveDown ``` |

Modified DVDUserNavigation.moveLeft

|  | Declaration |
| --- | --- |
| From | ``` case MoveLeft ``` |
| To | ``` case moveLeft ``` |

Modified DVDUserNavigation.moveRight

|  | Declaration |
| --- | --- |
| From | ``` case MoveRight ``` |
| To | ``` case moveRight ``` |

Modified DVDUserNavigation.moveUp

|  | Declaration |
| --- | --- |
| From | ``` case MoveUp ``` |
| To | ``` case moveUp ``` |

Modified DVDEventCallBackFunctionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DVDEventCallBackFunctionPtr = (DVDEventCode, DVDEventValue, DVDEventValue, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DVDEventCallBackFunctionPtr = (DVDEventCode, DVDEventValue, DVDEventValue, UnsafeMutableRawPointer) -> Swift.Void ``` |

Modified DVDEventCallBackRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DVDEventCallBackRef = UnsafeMutablePointer<Void> ``` |
| To | ``` typealias DVDEventCallBackRef = UnsafeMutableRawPointer ``` |

Modified DVDFatalErrCallBackFunctionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DVDFatalErrCallBackFunctionPtr = (DVDErrorCode, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias DVDFatalErrCallBackFunctionPtr = (DVDErrorCode, UnsafeMutableRawPointer) -> Swift.Void ``` |

Modified DVDGetAudioLanguageCode(_: UnsafeMutablePointer<DVDLanguageCode>?, _: UnsafeMutablePointer<DVDAudioExtensionCode>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetAudioLanguageCode(_ outCode: UnsafeMutablePointer<DVDLanguageCode>, _ outExtension: UnsafeMutablePointer<DVDAudioExtensionCode>) -> OSStatus ``` |
| To | ``` func DVDGetAudioLanguageCode(_ outCode: UnsafeMutablePointer<DVDLanguageCode>?, _ outExtension: UnsafeMutablePointer<DVDAudioExtensionCode>?) -> OSStatus ``` |

Modified DVDGetAudioLanguageCodeByStream(_: UInt16, _: UnsafeMutablePointer<DVDLanguageCode>?, _: UnsafeMutablePointer<DVDAudioExtensionCode>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetAudioLanguageCodeByStream(_ inStreamNum: UInt16, _ outCode: UnsafeMutablePointer<DVDLanguageCode>, _ outExtension: UnsafeMutablePointer<DVDAudioExtensionCode>) -> OSStatus ``` |
| To | ``` func DVDGetAudioLanguageCodeByStream(_ inStreamNum: UInt16, _ outCode: UnsafeMutablePointer<DVDLanguageCode>?, _ outExtension: UnsafeMutablePointer<DVDAudioExtensionCode>?) -> OSStatus ``` |

Modified DVDGetAudioStreamFormat(_: UnsafeMutablePointer<DVDAudioFormat>?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UInt32>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetAudioStreamFormat(_ outFormat: UnsafeMutablePointer<DVDAudioFormat>, _ outBitsPerSample: UnsafeMutablePointer<UInt32>, _ outSamplesPerSecond: UnsafeMutablePointer<UInt32>, _ outChannels: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func DVDGetAudioStreamFormat(_ outFormat: UnsafeMutablePointer<DVDAudioFormat>?, _ outBitsPerSample: UnsafeMutablePointer<UInt32>?, _ outSamplesPerSecond: UnsafeMutablePointer<UInt32>?, _ outChannels: UnsafeMutablePointer<UInt32>?) -> OSStatus ``` |

Modified DVDGetAudioStreamFormatByStream(_: UInt32, _: UnsafeMutablePointer<DVDAudioFormat>?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UInt32>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetAudioStreamFormatByStream(_ inStreamNum: UInt32, _ outFormat: UnsafeMutablePointer<DVDAudioFormat>, _ outBitsPerSample: UnsafeMutablePointer<UInt32>, _ outSamplesPerSecond: UnsafeMutablePointer<UInt32>, _ outChannels: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func DVDGetAudioStreamFormatByStream(_ inStreamNum: UInt32, _ outFormat: UnsafeMutablePointer<DVDAudioFormat>?, _ outBitsPerSample: UnsafeMutablePointer<UInt32>?, _ outSamplesPerSecond: UnsafeMutablePointer<UInt32>?, _ outChannels: UnsafeMutablePointer<UInt32>?) -> OSStatus ``` |

Modified DVDGetAudioVolumeInfo(_: UnsafeMutablePointer<UInt16>?, _: UnsafeMutablePointer<UInt16>?, _: UnsafeMutablePointer<UInt16>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetAudioVolumeInfo(_ outMinVolume: UnsafeMutablePointer<UInt16>, _ outCurVolume: UnsafeMutablePointer<UInt16>, _ outMaxVolume: UnsafeMutablePointer<UInt16>) -> OSStatus ``` |
| To | ``` func DVDGetAudioVolumeInfo(_ outMinVolume: UnsafeMutablePointer<UInt16>?, _ outCurVolume: UnsafeMutablePointer<UInt16>?, _ outMaxVolume: UnsafeMutablePointer<UInt16>?) -> OSStatus ``` |

Modified DVDGetBookmark(_: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetBookmark(_ outBookMarkData: UnsafeMutablePointer<Void>, _ ioBookMarkDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func DVDGetBookmark(_ outBookMarkData: UnsafeMutableRawPointer?, _ ioBookMarkDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified DVDGetButtoninfo(_: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UInt32>?, _: UnsafeMutablePointer<UInt32>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetButtoninfo(_ numberOfButtons: UnsafeMutablePointer<UInt32>, _ selectedButton: UnsafeMutablePointer<UInt32>, _ forcedActivateButton: UnsafeMutablePointer<UInt32>, _ userButtonOffset: UnsafeMutablePointer<UInt32>, _ numberOfUserButtons: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func DVDGetButtoninfo(_ numberOfButtons: UnsafeMutablePointer<UInt32>?, _ selectedButton: UnsafeMutablePointer<UInt32>?, _ forcedActivateButton: UnsafeMutablePointer<UInt32>?, _ userButtonOffset: UnsafeMutablePointer<UInt32>?, _ numberOfUserButtons: UnsafeMutablePointer<UInt32>?) -> OSStatus ``` |

Modified DVDGetDriveRegionCode(_: UnsafeMutablePointer<DVDRegionCode>?, _: UnsafeMutablePointer<Int16>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetDriveRegionCode(_ outCode: UnsafeMutablePointer<DVDRegionCode>, _ outNumberChangesLeft: UnsafeMutablePointer<Int16>) -> OSStatus ``` |
| To | ``` func DVDGetDriveRegionCode(_ outCode: UnsafeMutablePointer<DVDRegionCode>?, _ outNumberChangesLeft: UnsafeMutablePointer<Int16>?) -> OSStatus ``` |

Modified DVDGetLastPlayBookmark(_: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetLastPlayBookmark(_ outBookMarkData: UnsafeMutablePointer<Void>, _ ioBookMarkDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |
| To | ``` func DVDGetLastPlayBookmark(_ outBookMarkData: UnsafeMutableRawPointer?, _ ioBookMarkDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` |

Modified DVDGetMediaUniqueID(_: UnsafeMutablePointer<UInt8>!) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetMediaUniqueID(_ outDiscID: UnsafeMutablePointer<UInt8>) -> OSStatus ``` |
| To | ``` func DVDGetMediaUniqueID(_ outDiscID: UnsafeMutablePointer<UInt8>!) -> OSStatus ``` |

Modified DVDGetMediaVolumeCFName(_: UnsafeMutablePointer<Unmanaged<CFString>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetMediaVolumeCFName(_ outDiscVolumeCFName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func DVDGetMediaVolumeCFName(_ outDiscVolumeCFName: UnsafeMutablePointer<Unmanaged<CFString>>) -> OSStatus ``` |

Modified DVDGetScanRate(_: UnsafeMutablePointer<DVDScanRate>?, _: UnsafeMutablePointer<DVDScanDirection>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetScanRate(_ outRate: UnsafeMutablePointer<DVDScanRate>, _ outDirection: UnsafeMutablePointer<DVDScanDirection>) -> OSStatus ``` |
| To | ``` func DVDGetScanRate(_ outRate: UnsafeMutablePointer<DVDScanRate>?, _ outDirection: UnsafeMutablePointer<DVDScanDirection>?) -> OSStatus ``` |

Modified DVDGetSPDIFDataOutDeviceCFName(_: UInt32, _: UnsafeMutablePointer<Unmanaged<CFString>>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetSPDIFDataOutDeviceCFName(_ inIndex: UInt32, _ outName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` |
| To | ``` func DVDGetSPDIFDataOutDeviceCFName(_ inIndex: UInt32, _ outName: UnsafeMutablePointer<Unmanaged<CFString>>) -> OSStatus ``` |

Modified DVDGetSubPictureLanguageCode(_: UnsafeMutablePointer<DVDLanguageCode>?, _: UnsafeMutablePointer<DVDSubpictureExtensionCode>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetSubPictureLanguageCode(_ outCode: UnsafeMutablePointer<DVDLanguageCode>, _ outExtension: UnsafeMutablePointer<DVDSubpictureExtensionCode>) -> OSStatus ``` |
| To | ``` func DVDGetSubPictureLanguageCode(_ outCode: UnsafeMutablePointer<DVDLanguageCode>?, _ outExtension: UnsafeMutablePointer<DVDSubpictureExtensionCode>?) -> OSStatus ``` |

Modified DVDGetSubPictureLanguageCodeByStream(_: UInt16, _: UnsafeMutablePointer<DVDLanguageCode>?, _: UnsafeMutablePointer<DVDSubpictureExtensionCode>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGetSubPictureLanguageCodeByStream(_ inStreamNum: UInt16, _ outCode: UnsafeMutablePointer<DVDLanguageCode>, _ outExtension: UnsafeMutablePointer<DVDSubpictureExtensionCode>) -> OSStatus ``` |
| To | ``` func DVDGetSubPictureLanguageCodeByStream(_ inStreamNum: UInt16, _ outCode: UnsafeMutablePointer<DVDLanguageCode>?, _ outExtension: UnsafeMutablePointer<DVDSubpictureExtensionCode>?) -> OSStatus ``` |

Modified DVDGotoBookmark(_: UnsafeMutableRawPointer, _: UInt32) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDGotoBookmark(_ inBookMarkData: UnsafeMutablePointer<Void>, _ inBookMarkDataSize: UInt32) -> OSStatus ``` |
| To | ``` func DVDGotoBookmark(_ inBookMarkData: UnsafeMutableRawPointer, _ inBookMarkDataSize: UInt32) -> OSStatus ``` |

Modified DVDIsOnMenu(_: UnsafeMutablePointer<DarwinBoolean>?, _: UnsafeMutablePointer<DVDMenu>?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDIsOnMenu(_ outOnMenu: UnsafeMutablePointer<DarwinBoolean>, _ outMenu: UnsafeMutablePointer<DVDMenu>) -> OSStatus ``` |
| To | ``` func DVDIsOnMenu(_ outOnMenu: UnsafeMutablePointer<DarwinBoolean>?, _ outMenu: UnsafeMutablePointer<DVDMenu>?) -> OSStatus ``` |

Modified DVDRegisterEventCallBack(_: DVDPlayback.DVDEventCallBackFunctionPtr, _: UnsafeMutablePointer<DVDEventCode>, _: UInt32, _: UnsafeMutableRawPointer?, _: UnsafeMutablePointer<DVDEventCallBackRef>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDRegisterEventCallBack(_ inCallBackProc: DVDEventCallBackFunctionPtr, _ inCode: UnsafeMutablePointer<DVDEventCode>, _ inCodeCount: UInt32, _ inRefCon: UnsafeMutablePointer<Void>, _ outCallBackID: UnsafeMutablePointer<DVDEventCallBackRef>) -> OSStatus ``` |
| To | ``` func DVDRegisterEventCallBack(_ inCallBackProc: DVDPlayback.DVDEventCallBackFunctionPtr, _ inCode: UnsafeMutablePointer<DVDEventCode>, _ inCodeCount: UInt32, _ inRefCon: UnsafeMutableRawPointer?, _ outCallBackID: UnsafeMutablePointer<DVDEventCallBackRef>) -> OSStatus ``` |

Modified DVDSetFatalErrorCallBack(_: DVDPlayback.DVDFatalErrCallBackFunctionPtr, _: UnsafeMutableRawPointer?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDSetFatalErrorCallBack(_ inCallBackProc: DVDFatalErrCallBackFunctionPtr, _ inRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` |
| To | ``` func DVDSetFatalErrorCallBack(_ inCallBackProc: DVDPlayback.DVDFatalErrCallBackFunctionPtr, _ inRefCon: UnsafeMutableRawPointer?) -> OSStatus ``` |

Modified DVDSetLastPlayBookmark(_: UnsafeMutableRawPointer, _: UInt32) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDSetLastPlayBookmark(_ inBookMarkData: UnsafeMutablePointer<Void>, _ inBookMarkDataSize: UInt32) -> OSStatus ``` |
| To | ``` func DVDSetLastPlayBookmark(_ inBookMarkData: UnsafeMutableRawPointer, _ inBookMarkDataSize: UInt32) -> OSStatus ``` |

Modified DVDSetVideoWindowRef(_: WindowRef?) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDSetVideoWindowRef(_ inWindowRef: WindowRef) -> OSStatus ``` |
| To | ``` func DVDSetVideoWindowRef(_ inWindowRef: WindowRef?) -> OSStatus ``` |

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
