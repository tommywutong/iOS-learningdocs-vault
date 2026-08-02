---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/DVDPlayback.html
archived_at: '2026-07-18T02:52:18.093779Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# DVDPlayback Changes

## DVDPlayback

Modified DVDClearLastPlayBookmark() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDCloseMediaFile() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDCloseMediaVolume() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDDisplaySubPicture(Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDDispose() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDDoButtonActivate(Int32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified DVDDoMenuCGClick(UnsafeMutablePointer<CGPoint>, UnsafeMutablePointer<Int32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDDoMenuCGClick(_ inPt: UnsafePointer<CGPoint>, _ outIndex: UnsafePointer<Int32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDDoMenuCGClick(_ inPt: UnsafeMutablePointer<CGPoint>, _ outIndex: UnsafeMutablePointer<Int32>) -> OSStatus ``` | OS X 10.5 |

Modified DVDDoMenuCGMouseOver(UnsafeMutablePointer<CGPoint>, UnsafeMutablePointer<Int32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDDoMenuCGMouseOver(_ inPt: UnsafePointer<CGPoint>, _ outIndex: UnsafePointer<Int32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDDoMenuCGMouseOver(_ inPt: UnsafeMutablePointer<CGPoint>, _ outIndex: UnsafeMutablePointer<Int32>) -> OSStatus ``` | OS X 10.5 |

Modified DVDDoUserNavigation(DVDUserNavigation) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDEnableWebAccess(Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDEventCallBackFunctionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DVDEventCallBackFunctionPtr = CFunctionPointer<((DVDEventCode, DVDEventValue, DVDEventValue, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DVDEventCallBackFunctionPtr = CFunctionPointer<((DVDEventCode, DVDEventValue, DVDEventValue, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DVDEventCallBackRef

|  | Declaration |
| --- | --- |
| From | ``` typealias DVDEventCallBackRef = UnsafePointer<()> ``` |
| To | ``` typealias DVDEventCallBackRef = UnsafeMutablePointer<Void> ``` |

Modified DVDFatalErrCallBackFunctionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DVDFatalErrCallBackFunctionPtr = CFunctionPointer<((DVDErrorCode, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias DVDFatalErrCallBackFunctionPtr = CFunctionPointer<((DVDErrorCode, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified DVDGetAngle(UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAngle(_ outAngleNum: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAngle(_ outAngleNum: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetAspectRatio(UnsafeMutablePointer<DVDAspectRatio>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAspectRatio(_ outRatio: UnsafePointer<DVDAspectRatio>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAspectRatio(_ outRatio: UnsafeMutablePointer<DVDAspectRatio>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetAudioLanguageCode(UnsafeMutablePointer<DVDLanguageCode>, UnsafeMutablePointer<DVDAudioExtensionCode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAudioLanguageCode(_ outCode: UnsafePointer<DVDLanguageCode>, _ outExtension: UnsafePointer<DVDAudioExtensionCode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAudioLanguageCode(_ outCode: UnsafeMutablePointer<DVDLanguageCode>, _ outExtension: UnsafeMutablePointer<DVDAudioExtensionCode>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetAudioLanguageCodeByStream(UInt16, UnsafeMutablePointer<DVDLanguageCode>, UnsafeMutablePointer<DVDAudioExtensionCode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAudioLanguageCodeByStream(_ inStreamNum: UInt16, _ outCode: UnsafePointer<DVDLanguageCode>, _ outExtension: UnsafePointer<DVDAudioExtensionCode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAudioLanguageCodeByStream(_ inStreamNum: UInt16, _ outCode: UnsafeMutablePointer<DVDLanguageCode>, _ outExtension: UnsafeMutablePointer<DVDAudioExtensionCode>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetAudioOutputMode(UnsafeMutablePointer<DVDAudioMode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAudioOutputMode(_ outMode: UnsafePointer<DVDAudioMode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAudioOutputMode(_ outMode: UnsafeMutablePointer<DVDAudioMode>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetAudioOutputModeCapabilities(UnsafeMutablePointer<DVDAudioMode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAudioOutputModeCapabilities(_ outModes: UnsafePointer<DVDAudioMode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAudioOutputModeCapabilities(_ outModes: UnsafeMutablePointer<DVDAudioMode>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetAudioStream(UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAudioStream(_ outStreamNum: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAudioStream(_ outStreamNum: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetAudioStreamFormat(UnsafeMutablePointer<DVDAudioFormat>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAudioStreamFormat(_ outFormat: UnsafePointer<DVDAudioFormat>, _ outBitsPerSample: UnsafePointer<UInt32>, _ outSamplesPerSecond: UnsafePointer<UInt32>, _ outChannels: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAudioStreamFormat(_ outFormat: UnsafeMutablePointer<DVDAudioFormat>, _ outBitsPerSample: UnsafeMutablePointer<UInt32>, _ outSamplesPerSecond: UnsafeMutablePointer<UInt32>, _ outChannels: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetAudioStreamFormatByStream(UInt32, UnsafeMutablePointer<DVDAudioFormat>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAudioStreamFormatByStream(_ inStreamNum: UInt32, _ outFormat: UnsafePointer<DVDAudioFormat>, _ outBitsPerSample: UnsafePointer<UInt32>, _ outSamplesPerSecond: UnsafePointer<UInt32>, _ outChannels: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAudioStreamFormatByStream(_ inStreamNum: UInt32, _ outFormat: UnsafeMutablePointer<DVDAudioFormat>, _ outBitsPerSample: UnsafeMutablePointer<UInt32>, _ outSamplesPerSecond: UnsafeMutablePointer<UInt32>, _ outChannels: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified DVDGetAudioVolume(UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAudioVolume(_ outVolume: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAudioVolume(_ outVolume: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetAudioVolumeInfo(UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetAudioVolumeInfo(_ outMinVolume: UnsafePointer<UInt16>, _ outCurVolume: UnsafePointer<UInt16>, _ outMaxVolume: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetAudioVolumeInfo(_ outMinVolume: UnsafeMutablePointer<UInt16>, _ outCurVolume: UnsafeMutablePointer<UInt16>, _ outMaxVolume: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetBookmark(UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetBookmark(_ outBookMarkData: UnsafePointer<()>, _ ioBookMarkDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetBookmark(_ outBookMarkData: UnsafeMutablePointer<Void>, _ ioBookMarkDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetButtonPosition(UInt32, UnsafeMutablePointer<CGRect>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetButtonPosition(_ index: UInt32, _ outRect: UnsafePointer<CGRect>, _ autoAction: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetButtonPosition(_ index: UInt32, _ outRect: UnsafeMutablePointer<CGRect>, _ autoAction: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified DVDGetButtoninfo(UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetButtoninfo(_ numberOfButtons: UnsafePointer<UInt32>, _ selectedButton: UnsafePointer<UInt32>, _ forcedActivateButton: UnsafePointer<UInt32>, _ userButtonOffset: UnsafePointer<UInt32>, _ numberOfUserButtons: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetButtoninfo(_ numberOfButtons: UnsafeMutablePointer<UInt32>, _ selectedButton: UnsafeMutablePointer<UInt32>, _ forcedActivateButton: UnsafeMutablePointer<UInt32>, _ userButtonOffset: UnsafeMutablePointer<UInt32>, _ numberOfUserButtons: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified DVDGetChapter(UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetChapter(_ outChapterNum: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetChapter(_ outChapterNum: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetDiscRegionCode(UnsafeMutablePointer<DVDRegionCode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetDiscRegionCode(_ outCode: UnsafePointer<DVDRegionCode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetDiscRegionCode(_ outCode: UnsafeMutablePointer<DVDRegionCode>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetDriveRegionCode(UnsafeMutablePointer<DVDRegionCode>, UnsafeMutablePointer<Int16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetDriveRegionCode(_ outCode: UnsafePointer<DVDRegionCode>, _ outNumberChangesLeft: UnsafePointer<Int16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetDriveRegionCode(_ outCode: UnsafeMutablePointer<DVDRegionCode>, _ outNumberChangesLeft: UnsafeMutablePointer<Int16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetFormatStandard(UnsafeMutablePointer<DVDFormat>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetFormatStandard(_ outFormat: UnsafePointer<DVDFormat>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetFormatStandard(_ outFormat: UnsafeMutablePointer<DVDFormat>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetGPRMValue(UInt32, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetGPRMValue(_ index: UInt32, _ value: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetGPRMValue(_ index: UInt32, _ value: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.4 |

Modified DVDGetLastPlayBookmark(UnsafeMutablePointer<Void>, UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetLastPlayBookmark(_ outBookMarkData: UnsafePointer<()>, _ ioBookMarkDataSize: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetLastPlayBookmark(_ outBookMarkData: UnsafeMutablePointer<Void>, _ ioBookMarkDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetMediaUniqueID(UnsafeMutablePointer<UInt8>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetMediaUniqueID(_ outDiscID: UnsafePointer<UInt8>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetMediaUniqueID(_ outDiscID: UnsafeMutablePointer<UInt8>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetMediaVolumeCFName(UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetMediaVolumeCFName(_ outDiscVolumeCFName: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetMediaVolumeCFName(_ outDiscVolumeCFName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.4 |

Modified DVDGetMediaVolumeName(UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetMediaVolumeName(_ outDiscVolumeName: UnsafePointer<UnsafePointer<Int8>>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetMediaVolumeName(_ outDiscVolumeName: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetMenuLanguageCode(UnsafeMutablePointer<DVDLanguageCode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetMenuLanguageCode(_ outCode: UnsafePointer<DVDLanguageCode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetMenuLanguageCode(_ outCode: UnsafeMutablePointer<DVDLanguageCode>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetNativeVideoSize(UnsafeMutablePointer<UInt16>, UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetNativeVideoSize(_ outWidth: UnsafePointer<UInt16>, _ outHeight: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetNativeVideoSize(_ outWidth: UnsafeMutablePointer<UInt16>, _ outHeight: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetNumAngles(UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetNumAngles(_ outNumAngles: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetNumAngles(_ outNumAngles: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetNumAudioStreams(UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetNumAudioStreams(_ outNumStreams: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetNumAudioStreams(_ outNumStreams: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetNumChapters(UInt16, UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetNumChapters(_ inTitleNum: UInt16, _ outNumChapters: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetNumChapters(_ inTitleNum: UInt16, _ outNumChapters: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetNumSubPictureStreams(UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetNumSubPictureStreams(_ outNumStreams: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetNumSubPictureStreams(_ outNumStreams: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetNumTitles(UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetNumTitles(_ outNumTitles: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetNumTitles(_ outNumTitles: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetSPDIFDataOutDevice(UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetSPDIFDataOutDevice(_ outIndex: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetSPDIFDataOutDevice(_ outIndex: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetSPDIFDataOutDeviceCFName(UInt32, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetSPDIFDataOutDeviceCFName(_ inIndex: UInt32, _ outName: UnsafePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetSPDIFDataOutDeviceCFName(_ inIndex: UInt32, _ outName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetSPDIFDataOutDeviceCount(UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetSPDIFDataOutDeviceCount(_ outCount: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetSPDIFDataOutDeviceCount(_ outCount: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetScanRate(UnsafeMutablePointer<DVDScanRate>, UnsafeMutablePointer<DVDScanDirection>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetScanRate(_ outRate: UnsafePointer<DVDScanRate>, _ outDirection: UnsafePointer<DVDScanDirection>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetScanRate(_ outRate: UnsafeMutablePointer<DVDScanRate>, _ outDirection: UnsafeMutablePointer<DVDScanDirection>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetState(UnsafeMutablePointer<DVDState>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetState(_ outState: UnsafePointer<DVDState>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetState(_ outState: UnsafeMutablePointer<DVDState>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetSubPictureLanguageCode(UnsafeMutablePointer<DVDLanguageCode>, UnsafeMutablePointer<DVDSubpictureExtensionCode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetSubPictureLanguageCode(_ outCode: UnsafePointer<DVDLanguageCode>, _ outExtension: UnsafePointer<DVDSubpictureExtensionCode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetSubPictureLanguageCode(_ outCode: UnsafeMutablePointer<DVDLanguageCode>, _ outExtension: UnsafeMutablePointer<DVDSubpictureExtensionCode>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetSubPictureLanguageCodeByStream(UInt16, UnsafeMutablePointer<DVDLanguageCode>, UnsafeMutablePointer<DVDSubpictureExtensionCode>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetSubPictureLanguageCodeByStream(_ inStreamNum: UInt16, _ outCode: UnsafePointer<DVDLanguageCode>, _ outExtension: UnsafePointer<DVDSubpictureExtensionCode>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetSubPictureLanguageCodeByStream(_ inStreamNum: UInt16, _ outCode: UnsafeMutablePointer<DVDLanguageCode>, _ outExtension: UnsafeMutablePointer<DVDSubpictureExtensionCode>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetSubPictureStream(UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetSubPictureStream(_ outStreamNum: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetSubPictureStream(_ outStreamNum: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetTime(DVDTimeCode, UnsafeMutablePointer<DVDTimePosition>, UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetTime(_ inTimeCode: DVDTimeCode, _ outTime: UnsafePointer<DVDTimePosition>, _ outFrames: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetTime(_ inTimeCode: DVDTimeCode, _ outTime: UnsafeMutablePointer<DVDTimePosition>, _ outFrames: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetTimeEventRate(UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetTimeEventRate(_ outMilliseconds: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetTimeEventRate(_ outMilliseconds: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetTitle(UnsafeMutablePointer<UInt16>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetTitle(_ outTitleNum: UnsafePointer<UInt16>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetTitle(_ outTitleNum: UnsafeMutablePointer<UInt16>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetVideoCGBounds(UnsafeMutablePointer<CGRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetVideoCGBounds(_ outRect: UnsafePointer<CGRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetVideoCGBounds(_ outRect: UnsafeMutablePointer<CGRect>) -> OSStatus ``` | OS X 10.5 |

Modified DVDGetVideoDisplay(UnsafeMutablePointer<CGDirectDisplayID>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetVideoDisplay(_ outDisplay: UnsafePointer<CGDirectDisplayID>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetVideoDisplay(_ outDisplay: UnsafeMutablePointer<CGDirectDisplayID>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetVideoWindowID(UnsafeMutablePointer<UInt32>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetVideoWindowID(_ outVidWindowID: UnsafePointer<UInt32>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetVideoWindowID(_ outVidWindowID: UnsafeMutablePointer<UInt32>) -> OSStatus ``` | OS X 10.3 |

Modified DVDGetVideoWindowRef(UnsafeMutablePointer<WindowRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGetVideoWindowRef(_ outWindowRef: UnsafePointer<Unmanaged<Window>?>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGetVideoWindowRef(_ outWindowRef: UnsafeMutablePointer<WindowRef>) -> OSStatus ``` | OS X 10.5 |

Modified DVDGoBackOneLevel() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDGoToMenu(DVDMenu) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDGotoBookmark(UnsafeMutablePointer<Void>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDGotoBookmark(_ inBookMarkData: UnsafePointer<()>, _ inBookMarkDataSize: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDGotoBookmark(_ inBookMarkData: UnsafeMutablePointer<Void>, _ inBookMarkDataSize: UInt32) -> OSStatus ``` | OS X 10.3 |

Modified DVDHasMedia(UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDHasMedia(_ outHasMedia: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDHasMedia(_ outHasMedia: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDHasMenu(DVDMenu, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDHasMenu(_ inMenu: DVDMenu, _ outHasMenu: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDHasMenu(_ inMenu: DVDMenu, _ outHasMenu: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDHasNextChapter(UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDHasNextChapter(_ outHasChapter: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDHasNextChapter(_ outHasChapter: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDHasPreviousChapter(UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDHasPreviousChapter(_ outHasChapter: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDHasPreviousChapter(_ outHasChapter: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDIdle() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDInitialize() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDIsDisplayingSubPicture(UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDIsDisplayingSubPicture(_ outDisplayingSubPicture: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDIsDisplayingSubPicture(_ outDisplayingSubPicture: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDIsMuted(UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDIsMuted(_ outIsMuted: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDIsMuted(_ outIsMuted: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDIsOnMenu(UnsafeMutablePointer<Boolean>, UnsafeMutablePointer<DVDMenu>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDIsOnMenu(_ outOnMenu: UnsafePointer<Boolean>, _ outMenu: UnsafePointer<DVDMenu>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDIsOnMenu(_ outOnMenu: UnsafeMutablePointer<Boolean>, _ outMenu: UnsafeMutablePointer<DVDMenu>) -> OSStatus ``` | OS X 10.3 |

Modified DVDIsPaused(UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDIsPaused(_ outIsPaused: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDIsPaused(_ outIsPaused: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDIsPlaying(UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDIsPlaying(_ outIsPlaying: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDIsPlaying(_ outIsPlaying: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDIsRegisteredEventCallBack(DVDEventCallBackRef) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDIsSupportedDisplay(CGDirectDisplayID, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDIsSupportedDisplay(_ inDisplay: CGDirectDisplayID, _ outSupported: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDIsSupportedDisplay(_ inDisplay: CGDirectDisplayID, _ outSupported: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDIsValidMediaRef(UnsafeMutablePointer<FSRef>, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDIsValidMediaRef(_ inRef: UnsafePointer<FSRef>, _ outIsValid: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDIsValidMediaRef(_ inRef: UnsafeMutablePointer<FSRef>, _ outIsValid: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDIsValidMediaURL(CFURL!, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDIsValidMediaURL(_ inRef: CFURL!, _ outIsValid: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDIsValidMediaURL(_ inRef: CFURL!, _ outIsValid: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.5 |

Modified DVDMute(Boolean) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDNextChapter() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDOpenMediaFile(UnsafeMutablePointer<FSRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDOpenMediaFile(_ inFile: UnsafePointer<FSRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDOpenMediaFile(_ inFile: UnsafeMutablePointer<FSRef>) -> OSStatus ``` | OS X 10.3 |

Modified DVDOpenMediaFileWithURL(CFURL!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DVDOpenMediaVolume(UnsafeMutablePointer<FSRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDOpenMediaVolume(_ inVolume: UnsafePointer<FSRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDOpenMediaVolume(_ inVolume: UnsafeMutablePointer<FSRef>) -> OSStatus ``` | OS X 10.3 |

Modified DVDOpenMediaVolumeWithURL(CFURL!) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified DVDPause() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDPlay() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDPreviousChapter() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDRegisterEventCallBack(DVDEventCallBackFunctionPtr, UnsafeMutablePointer<DVDEventCode>, UInt32, UnsafeMutablePointer<Void>, UnsafeMutablePointer<DVDEventCallBackRef>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDRegisterEventCallBack(_ inCallBackProc: DVDEventCallBackFunctionPtr, _ inCode: UnsafePointer<DVDEventCode>, _ inCodeCount: UInt32, _ inRefCon: UnsafePointer<()>, _ outCallBackID: UnsafePointer<DVDEventCallBackRef>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDRegisterEventCallBack(_ inCallBackProc: DVDEventCallBackFunctionPtr, _ inCode: UnsafeMutablePointer<DVDEventCode>, _ inCodeCount: UInt32, _ inRefCon: UnsafeMutablePointer<Void>, _ outCallBackID: UnsafeMutablePointer<DVDEventCallBackRef>) -> OSStatus ``` | OS X 10.3 |

Modified DVDResume() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDReturnToTitle() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDScan(DVDScanRate, DVDScanDirection) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetAngle(UInt16) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetAspectRatio(DVDAspectRatio) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetAudioOutputMode(DVDAudioMode) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetAudioStream(UInt16) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetAudioVolume(UInt16) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetChapter(UInt16) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetDefaultAudioLanguageCode(DVDLanguageCode, DVDAudioExtensionCode) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetDefaultMenuLanguageCode(DVDLanguageCode) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetDefaultSubPictureLanguageCode(DVDLanguageCode, DVDSubpictureExtensionCode) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetDriveRegionCode(DVDRegionCode, AuthorizationRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDSetDriveRegionCode(_ inCode: DVDRegionCode, _ inAuthorization: Authorization!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDSetDriveRegionCode(_ inCode: DVDRegionCode, _ inAuthorization: AuthorizationRef) -> OSStatus ``` | OS X 10.3 |

Modified DVDSetFatalErrorCallBack(DVDFatalErrCallBackFunctionPtr, UnsafeMutablePointer<Void>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDSetFatalErrorCallBack(_ inCallBackProc: DVDFatalErrCallBackFunctionPtr, _ inRefCon: UnsafePointer<()>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDSetFatalErrorCallBack(_ inCallBackProc: DVDFatalErrCallBackFunctionPtr, _ inRefCon: UnsafeMutablePointer<Void>) -> OSStatus ``` | OS X 10.3 |

Modified DVDSetLastPlayBookmark(UnsafeMutablePointer<Void>, UInt32) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDSetLastPlayBookmark(_ inBookMarkData: UnsafePointer<()>, _ inBookMarkDataSize: UInt32) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDSetLastPlayBookmark(_ inBookMarkData: UnsafeMutablePointer<Void>, _ inBookMarkDataSize: UInt32) -> OSStatus ``` | OS X 10.3 |

Modified DVDSetSPDIFDataOutDevice(UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetSubPictureStream(UInt16) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetTime(DVDTimeCode, DVDTimePosition, UInt16) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetTimeEventRate(UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetTitle(UInt16) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetVideoCGBounds(UnsafeMutablePointer<CGRect>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDSetVideoCGBounds(_ inRect: UnsafePointer<CGRect>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDSetVideoCGBounds(_ inRect: UnsafeMutablePointer<CGRect>) -> OSStatus ``` | OS X 10.5 |

Modified DVDSetVideoDisplay(CGDirectDisplayID) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetVideoWindowID(UInt32) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSetVideoWindowRef(WindowRef) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDSetVideoWindowRef(_ inWindowRef: Window!) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDSetVideoWindowRef(_ inWindowRef: WindowRef) -> OSStatus ``` | OS X 10.5 |

Modified DVDSleep() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDStepFrame(DVDScanDirection) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDStop() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDSwitchToDisplay(CGDirectDisplayID, UnsafeMutablePointer<Boolean>) -> OSStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func DVDSwitchToDisplay(_ newDisplay: CGDirectDisplayID, _ outSupported: UnsafePointer<Boolean>) -> OSStatus ``` | OS X 10.10 |
| To | ``` func DVDSwitchToDisplay(_ newDisplay: CGDirectDisplayID, _ outSupported: UnsafeMutablePointer<Boolean>) -> OSStatus ``` | OS X 10.3 |

Modified DVDUnregisterEventCallBack(DVDEventCallBackRef) -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDUpdateVideo() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified DVDWakeUp() -> OSStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

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
