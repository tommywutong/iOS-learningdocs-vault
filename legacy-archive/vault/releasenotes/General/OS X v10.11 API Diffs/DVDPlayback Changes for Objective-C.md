---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/DVDPlayback.html
archived_at: '2026-07-18T02:53:01.728097Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# DVDPlayback Changes for Objective-C

### DVDPlayback

#### DVDPlayback.h

Added #def DVD_ASSUME_NONNULL_BEGINAdded #def DVD_ASSUME_NONNULL_ENDAdded #def DVD_NONNULLAdded #def DVD_NULLABLEModified DVDDoMenuCGClick()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDDoMenuCGClick (     CGPoint *inPt,     SInt32 *outIndex ); ``` |
| To | ``` OSStatus DVDDoMenuCGClick (     CGPoint * _Nonnull inPt,     SInt32 * _Nonnull outIndex ); ``` |

Modified DVDDoMenuCGMouseOver()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDDoMenuCGMouseOver (     CGPoint *inPt,     SInt32 *outIndex ); ``` |
| To | ``` OSStatus DVDDoMenuCGMouseOver (     CGPoint * _Nonnull inPt,     SInt32 * _Nonnull outIndex ); ``` |

Modified DVDDoMenuClick()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDDoMenuClick (     Point inPortPt,     SInt32 *outIndex ); ``` |
| To | ``` OSStatus DVDDoMenuClick (     Point inPortPt,     SInt32 * _Nonnull outIndex ); ``` |

Modified DVDDoMenuMouseOver()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDDoMenuMouseOver (     Point inPortPt,     SInt32 *outIndex ); ``` |
| To | ``` OSStatus DVDDoMenuMouseOver (     Point inPortPt,     SInt32 * _Nonnull outIndex ); ``` |

Modified DVDGetAngle()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAngle (     UInt16 *outAngleNum ); ``` |
| To | ``` OSStatus DVDGetAngle (     UInt16 * _Nonnull outAngleNum ); ``` |

Modified DVDGetAspectRatio()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAspectRatio (     DVDAspectRatio *outRatio ); ``` |
| To | ``` OSStatus DVDGetAspectRatio (     DVDAspectRatio * _Nonnull outRatio ); ``` |

Modified DVDGetAudioLanguageCode()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAudioLanguageCode (     DVDLanguageCode *outCode,     DVDAudioExtensionCode *outExtension ); ``` |
| To | ``` OSStatus DVDGetAudioLanguageCode (     DVDLanguageCode * _Nullable outCode,     DVDAudioExtensionCode * _Nullable outExtension ); ``` |

Modified DVDGetAudioLanguageCodeByStream()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAudioLanguageCodeByStream (     UInt16 inStreamNum,     DVDLanguageCode *outCode,     DVDAudioExtensionCode *outExtension ); ``` |
| To | ``` OSStatus DVDGetAudioLanguageCodeByStream (     UInt16 inStreamNum,     DVDLanguageCode * _Nullable outCode,     DVDAudioExtensionCode * _Nullable outExtension ); ``` |

Modified DVDGetAudioOutputMode()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAudioOutputMode (     DVDAudioMode *outMode ); ``` |
| To | ``` OSStatus DVDGetAudioOutputMode (     DVDAudioMode * _Nonnull outMode ); ``` |

Modified DVDGetAudioOutputModeCapabilities()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAudioOutputModeCapabilities (     DVDAudioMode *outModes ); ``` |
| To | ``` OSStatus DVDGetAudioOutputModeCapabilities (     DVDAudioMode * _Nonnull outModes ); ``` |

Modified DVDGetAudioStream()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAudioStream (     UInt16 *outStreamNum ); ``` |
| To | ``` OSStatus DVDGetAudioStream (     UInt16 * _Nonnull outStreamNum ); ``` |

Modified DVDGetAudioStreamFormat()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAudioStreamFormat (     DVDAudioFormat *outFormat,     UInt32 *outBitsPerSample,     UInt32 *outSamplesPerSecond,     UInt32 *outChannels ); ``` |
| To | ``` OSStatus DVDGetAudioStreamFormat (     DVDAudioFormat * _Nullable outFormat,     UInt32 * _Nullable outBitsPerSample,     UInt32 * _Nullable outSamplesPerSecond,     UInt32 * _Nullable outChannels ); ``` |

Modified DVDGetAudioStreamFormatByStream()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAudioStreamFormatByStream (     UInt32 inStreamNum,     DVDAudioFormat *outFormat,     UInt32 *outBitsPerSample,     UInt32 *outSamplesPerSecond,     UInt32 *outChannels ); ``` |
| To | ``` OSStatus DVDGetAudioStreamFormatByStream (     UInt32 inStreamNum,     DVDAudioFormat * _Nullable outFormat,     UInt32 * _Nullable outBitsPerSample,     UInt32 * _Nullable outSamplesPerSecond,     UInt32 * _Nullable outChannels ); ``` |

Modified DVDGetAudioVolume()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAudioVolume (     UInt16 *outVolume ); ``` |
| To | ``` OSStatus DVDGetAudioVolume (     UInt16 * _Nonnull outVolume ); ``` |

Modified DVDGetAudioVolumeInfo()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetAudioVolumeInfo (     UInt16 *outMinVolume,     UInt16 *outCurVolume,     UInt16 *outMaxVolume ); ``` |
| To | ``` OSStatus DVDGetAudioVolumeInfo (     UInt16 * _Nullable outMinVolume,     UInt16 * _Nullable outCurVolume,     UInt16 * _Nullable outMaxVolume ); ``` |

Modified DVDGetBookmark()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetBookmark (     void *outBookMarkData,     UInt32 *ioBookMarkDataSize ); ``` |
| To | ``` OSStatus DVDGetBookmark (     void * _Nullable outBookMarkData,     UInt32 * _Nonnull ioBookMarkDataSize ); ``` |

Modified DVDGetButtoninfo()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetButtoninfo (     UInt32 *numberOfButtons,     UInt32 *selectedButton,     UInt32 *forcedActivateButton,     UInt32 *userButtonOffset,     UInt32 *numberOfUserButtons ); ``` |
| To | ``` OSStatus DVDGetButtoninfo (     UInt32 * _Nullable numberOfButtons,     UInt32 * _Nullable selectedButton,     UInt32 * _Nullable forcedActivateButton,     UInt32 * _Nullable userButtonOffset,     UInt32 * _Nullable numberOfUserButtons ); ``` |

Modified DVDGetButtonPosition()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetButtonPosition (     UInt32 index,     CGRect *outRect,     UInt32 *autoAction ); ``` |
| To | ``` OSStatus DVDGetButtonPosition (     UInt32 index,     CGRect * _Nonnull outRect,     UInt32 * _Nonnull autoAction ); ``` |

Modified DVDGetChapter()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetChapter (     UInt16 *outChapterNum ); ``` |
| To | ``` OSStatus DVDGetChapter (     UInt16 * _Nonnull outChapterNum ); ``` |

Modified DVDGetDiscRegionCode()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetDiscRegionCode (     DVDRegionCode *outCode ); ``` |
| To | ``` OSStatus DVDGetDiscRegionCode (     DVDRegionCode * _Nonnull outCode ); ``` |

Modified DVDGetDriveRegionCode()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetDriveRegionCode (     DVDRegionCode *outCode,     SInt16 *outNumberChangesLeft ); ``` |
| To | ``` OSStatus DVDGetDriveRegionCode (     DVDRegionCode * _Nullable outCode,     SInt16 * _Nullable outNumberChangesLeft ); ``` |

Modified DVDGetFormatStandard()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetFormatStandard (     DVDFormat *outFormat ); ``` |
| To | ``` OSStatus DVDGetFormatStandard (     DVDFormat * _Nonnull outFormat ); ``` |

Modified DVDGetGPRMValue()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetGPRMValue (     UInt32 index,     UInt32 *value ); ``` |
| To | ``` OSStatus DVDGetGPRMValue (     UInt32 index,     UInt32 * _Nonnull value ); ``` |

Modified DVDGetLastPlayBookmark()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetLastPlayBookmark (     void *outBookMarkData,     UInt32 *ioBookMarkDataSize ); ``` |
| To | ``` OSStatus DVDGetLastPlayBookmark (     void * _Nullable outBookMarkData,     UInt32 * _Nonnull ioBookMarkDataSize ); ``` |

Modified DVDGetMediaVolumeCFName()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetMediaVolumeCFName (     CFStringRef *outDiscVolumeCFName ); ``` |
| To | ``` OSStatus DVDGetMediaVolumeCFName (     CFStringRef  _Nonnull * _Nonnull outDiscVolumeCFName ); ``` |

Modified DVDGetMediaVolumeName()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetMediaVolumeName (     char **outDiscVolumeName ); ``` |
| To | ``` OSStatus DVDGetMediaVolumeName (     char * _Nonnull * _Nonnull outDiscVolumeName ); ``` |

Modified DVDGetMenuLanguageCode()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetMenuLanguageCode (     DVDLanguageCode *outCode ); ``` |
| To | ``` OSStatus DVDGetMenuLanguageCode (     DVDLanguageCode * _Nonnull outCode ); ``` |

Modified DVDGetNativeVideoSize()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetNativeVideoSize (     UInt16 *outWidth,     UInt16 *outHeight ); ``` |
| To | ``` OSStatus DVDGetNativeVideoSize (     UInt16 * _Nonnull outWidth,     UInt16 * _Nonnull outHeight ); ``` |

Modified DVDGetNumAngles()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetNumAngles (     UInt16 *outNumAngles ); ``` |
| To | ``` OSStatus DVDGetNumAngles (     UInt16 * _Nonnull outNumAngles ); ``` |

Modified DVDGetNumAudioStreams()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetNumAudioStreams (     UInt16 *outNumStreams ); ``` |
| To | ``` OSStatus DVDGetNumAudioStreams (     UInt16 * _Nonnull outNumStreams ); ``` |

Modified DVDGetNumChapters()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetNumChapters (     UInt16 inTitleNum,     UInt16 *outNumChapters ); ``` |
| To | ``` OSStatus DVDGetNumChapters (     UInt16 inTitleNum,     UInt16 * _Nonnull outNumChapters ); ``` |

Modified DVDGetNumSubPictureStreams()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetNumSubPictureStreams (     UInt16 *outNumStreams ); ``` |
| To | ``` OSStatus DVDGetNumSubPictureStreams (     UInt16 * _Nonnull outNumStreams ); ``` |

Modified DVDGetNumTitles()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetNumTitles (     UInt16 *outNumTitles ); ``` |
| To | ``` OSStatus DVDGetNumTitles (     UInt16 * _Nonnull outNumTitles ); ``` |

Modified DVDGetScanRate()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetScanRate (     DVDScanRate *outRate,     DVDScanDirection *outDirection ); ``` |
| To | ``` OSStatus DVDGetScanRate (     DVDScanRate * _Nullable outRate,     DVDScanDirection * _Nullable outDirection ); ``` |

Modified DVDGetSPDIFDataOutDevice()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetSPDIFDataOutDevice (     UInt32 *outIndex ); ``` |
| To | ``` OSStatus DVDGetSPDIFDataOutDevice (     UInt32 * _Nonnull outIndex ); ``` |

Modified DVDGetSPDIFDataOutDeviceCFName()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetSPDIFDataOutDeviceCFName (     UInt32 inIndex,     CFStringRef *outName ); ``` |
| To | ``` OSStatus DVDGetSPDIFDataOutDeviceCFName (     UInt32 inIndex,     CFStringRef  _Nonnull * _Nonnull outName ); ``` |

Modified DVDGetSPDIFDataOutDeviceCount()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetSPDIFDataOutDeviceCount (     UInt32 *outCount ); ``` |
| To | ``` OSStatus DVDGetSPDIFDataOutDeviceCount (     UInt32 * _Nonnull outCount ); ``` |

Modified DVDGetState()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetState (     DVDState *outState ); ``` |
| To | ``` OSStatus DVDGetState (     DVDState * _Nonnull outState ); ``` |

Modified DVDGetSubPictureLanguageCode()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetSubPictureLanguageCode (     DVDLanguageCode *outCode,     DVDSubpictureExtensionCode *outExtension ); ``` |
| To | ``` OSStatus DVDGetSubPictureLanguageCode (     DVDLanguageCode * _Nullable outCode,     DVDSubpictureExtensionCode * _Nullable outExtension ); ``` |

Modified DVDGetSubPictureLanguageCodeByStream()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetSubPictureLanguageCodeByStream (     UInt16 inStreamNum,     DVDLanguageCode *outCode,     DVDSubpictureExtensionCode *outExtension ); ``` |
| To | ``` OSStatus DVDGetSubPictureLanguageCodeByStream (     UInt16 inStreamNum,     DVDLanguageCode * _Nullable outCode,     DVDSubpictureExtensionCode * _Nullable outExtension ); ``` |

Modified DVDGetSubPictureStream()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetSubPictureStream (     UInt16 *outStreamNum ); ``` |
| To | ``` OSStatus DVDGetSubPictureStream (     UInt16 * _Nonnull outStreamNum ); ``` |

Modified DVDGetTime()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetTime (     DVDTimeCode inTimeCode,     DVDTimePosition *outTime,     UInt16 *outFrames ); ``` |
| To | ``` OSStatus DVDGetTime (     DVDTimeCode inTimeCode,     DVDTimePosition * _Nonnull outTime,     UInt16 * _Nonnull outFrames ); ``` |

Modified DVDGetTimeEventRate()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetTimeEventRate (     UInt32 *outMilliseconds ); ``` |
| To | ``` OSStatus DVDGetTimeEventRate (     UInt32 * _Nonnull outMilliseconds ); ``` |

Modified DVDGetTitle()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetTitle (     UInt16 *outTitleNum ); ``` |
| To | ``` OSStatus DVDGetTitle (     UInt16 * _Nonnull outTitleNum ); ``` |

Modified DVDGetVideoBounds()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetVideoBounds (     Rect *outPortRect ); ``` |
| To | ``` OSStatus DVDGetVideoBounds (     Rect * _Nonnull outPortRect ); ``` |

Modified DVDGetVideoCGBounds()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetVideoCGBounds (     CGRect *outRect ); ``` |
| To | ``` OSStatus DVDGetVideoCGBounds (     CGRect * _Nonnull outRect ); ``` |

Modified DVDGetVideoDisplay()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetVideoDisplay (     CGDirectDisplayID *outDisplay ); ``` |
| To | ``` OSStatus DVDGetVideoDisplay (     CGDirectDisplayID * _Nonnull outDisplay ); ``` |

Modified DVDGetVideoKeyColor()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetVideoKeyColor (     RGBColor *outKeyColor ); ``` |
| To | ``` OSStatus DVDGetVideoKeyColor (     RGBColor * _Nonnull outKeyColor ); ``` |

Modified DVDGetVideoWindowID()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetVideoWindowID (     UInt32 *outVidWindowID ); ``` |
| To | ``` OSStatus DVDGetVideoWindowID (     UInt32 * _Nonnull outVidWindowID ); ``` |

Modified DVDGetVideoWindowRef()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGetVideoWindowRef (     WindowRef *outWindowRef ); ``` |
| To | ``` OSStatus DVDGetVideoWindowRef (     WindowRef  _Nonnull * _Nonnull outWindowRef ); ``` |

Modified DVDGotoBookmark()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDGotoBookmark (     void *inBookMarkData,     UInt32 inBookMarkDataSize ); ``` |
| To | ``` OSStatus DVDGotoBookmark (     void * _Nonnull inBookMarkData,     UInt32 inBookMarkDataSize ); ``` |

Modified DVDHasMedia()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDHasMedia (     Boolean *outHasMedia ); ``` |
| To | ``` OSStatus DVDHasMedia (     Boolean * _Nonnull outHasMedia ); ``` |

Modified DVDHasMenu()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDHasMenu (     DVDMenu inMenu,     Boolean *outHasMenu ); ``` |
| To | ``` OSStatus DVDHasMenu (     DVDMenu inMenu,     Boolean * _Nonnull outHasMenu ); ``` |

Modified DVDHasNextChapter()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDHasNextChapter (     Boolean *outHasChapter ); ``` |
| To | ``` OSStatus DVDHasNextChapter (     Boolean * _Nonnull outHasChapter ); ``` |

Modified DVDHasPreviousChapter()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDHasPreviousChapter (     Boolean *outHasChapter ); ``` |
| To | ``` OSStatus DVDHasPreviousChapter (     Boolean * _Nonnull outHasChapter ); ``` |

Modified DVDIsDisplayingSubPicture()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDIsDisplayingSubPicture (     Boolean *outDisplayingSubPicture ); ``` |
| To | ``` OSStatus DVDIsDisplayingSubPicture (     Boolean * _Nonnull outDisplayingSubPicture ); ``` |

Modified DVDIsMuted()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDIsMuted (     Boolean *outIsMuted ); ``` |
| To | ``` OSStatus DVDIsMuted (     Boolean * _Nonnull outIsMuted ); ``` |

Modified DVDIsOnMenu()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDIsOnMenu (     Boolean *outOnMenu,     DVDMenu *outMenu ); ``` |
| To | ``` OSStatus DVDIsOnMenu (     Boolean * _Nullable outOnMenu,     DVDMenu * _Nullable outMenu ); ``` |

Modified DVDIsPaused()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDIsPaused (     Boolean *outIsPaused ); ``` |
| To | ``` OSStatus DVDIsPaused (     Boolean * _Nonnull outIsPaused ); ``` |

Modified DVDIsPlaying()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDIsPlaying (     Boolean *outIsPlaying ); ``` |
| To | ``` OSStatus DVDIsPlaying (     Boolean * _Nonnull outIsPlaying ); ``` |

Modified DVDIsRegisteredEventCallBack()

|  | Declaration |
| --- | --- |
| From | ``` Boolean DVDIsRegisteredEventCallBack (     DVDEventCallBackRef inCallBackID ); ``` |
| To | ``` Boolean DVDIsRegisteredEventCallBack (     DVDEventCallBackRef _Nonnull inCallBackID ); ``` |

Modified DVDIsSupportedDevice()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDIsSupportedDevice (     GDHandle inDevice,     Boolean *outSupported ); ``` |
| To | ``` OSStatus DVDIsSupportedDevice (     GDHandle inDevice,     Boolean * _Nonnull outSupported ); ``` |

Modified DVDIsSupportedDisplay()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDIsSupportedDisplay (     CGDirectDisplayID inDisplay,     Boolean *outSupported ); ``` |
| To | ``` OSStatus DVDIsSupportedDisplay (     CGDirectDisplayID inDisplay,     Boolean * _Nonnull outSupported ); ``` |

Modified DVDIsValidMediaRef()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDIsValidMediaRef (     FSRef *inRef,     Boolean *outIsValid ); ``` |
| To | ``` OSStatus DVDIsValidMediaRef (     FSRef * _Nonnull inRef,     Boolean * _Nonnull outIsValid ); ``` |

Modified DVDIsValidMediaURL()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDIsValidMediaURL (     CFURLRef inRef,     Boolean *outIsValid ); ``` |
| To | ``` OSStatus DVDIsValidMediaURL (     CFURLRef _Nonnull inRef,     Boolean * _Nonnull outIsValid ); ``` |

Modified DVDOpenMediaFile()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDOpenMediaFile (     FSRef *inFile ); ``` |
| To | ``` OSStatus DVDOpenMediaFile (     FSRef * _Nonnull inFile ); ``` |

Modified DVDOpenMediaFileWithURL()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDOpenMediaFileWithURL (     CFURLRef inFile ); ``` |
| To | ``` OSStatus DVDOpenMediaFileWithURL (     CFURLRef _Nonnull inFile ); ``` |

Modified DVDOpenMediaVolume()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDOpenMediaVolume (     FSRef *inVolume ); ``` |
| To | ``` OSStatus DVDOpenMediaVolume (     FSRef * _Nonnull inVolume ); ``` |

Modified DVDOpenMediaVolumeWithURL()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDOpenMediaVolumeWithURL (     CFURLRef inVolume ); ``` |
| To | ``` OSStatus DVDOpenMediaVolumeWithURL (     CFURLRef _Nonnull inVolume ); ``` |

Modified DVDRegisterEventCallBack()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDRegisterEventCallBack (     DVDEventCallBackFunctionPtr inCallBackProc,     DVDEventCode *inCode,     UInt32 inCodeCount,     void *inRefCon,     DVDEventCallBackRef *outCallBackID ); ``` |
| To | ``` OSStatus DVDRegisterEventCallBack (     DVDEventCallBackFunctionPtr _Nonnull inCallBackProc,     DVDEventCode * _Nonnull inCode,     UInt32 inCodeCount,     void * _Nullable inRefCon,     DVDEventCallBackRef  _Nonnull * _Nonnull outCallBackID ); ``` |

Modified DVDSetDriveRegionCode()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDSetDriveRegionCode (     DVDRegionCode inCode,     AuthorizationRef inAuthorization ); ``` |
| To | ``` OSStatus DVDSetDriveRegionCode (     DVDRegionCode inCode,     AuthorizationRef _Nonnull inAuthorization ); ``` |

Modified DVDSetFatalErrorCallBack()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDSetFatalErrorCallBack (     DVDFatalErrCallBackFunctionPtr inCallBackProc,     void *inRefCon ); ``` |
| To | ``` OSStatus DVDSetFatalErrorCallBack (     DVDFatalErrCallBackFunctionPtr _Nonnull inCallBackProc,     void * _Nullable inRefCon ); ``` |

Modified DVDSetLastPlayBookmark()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDSetLastPlayBookmark (     void *inBookMarkData,     UInt32 inBookMarkDataSize ); ``` |
| To | ``` OSStatus DVDSetLastPlayBookmark (     void * _Nonnull inBookMarkData,     UInt32 inBookMarkDataSize ); ``` |

Modified DVDSetVideoBounds()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDSetVideoBounds (     Rect *inPortRect ); ``` |
| To | ``` OSStatus DVDSetVideoBounds (     Rect * _Nonnull inPortRect ); ``` |

Modified DVDSetVideoCGBounds()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDSetVideoCGBounds (     CGRect *inRect ); ``` |
| To | ``` OSStatus DVDSetVideoCGBounds (     CGRect * _Nonnull inRect ); ``` |

Modified DVDSetVideoPort()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDSetVideoPort (     CGrafPtr inVidPort ); ``` |
| To | ``` OSStatus DVDSetVideoPort (     CGrafPtr _Nonnull inVidPort ); ``` |

Modified DVDSetVideoWindowRef()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDSetVideoWindowRef (     WindowRef inWindowRef ); ``` |
| To | ``` OSStatus DVDSetVideoWindowRef (     WindowRef _Nullable inWindowRef ); ``` |

Modified DVDSwitchToDevice()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDSwitchToDevice (     GDHandle newDevice,     Boolean *outSupported ); ``` |
| To | ``` OSStatus DVDSwitchToDevice (     GDHandle newDevice,     Boolean * _Nonnull outSupported ); ``` |

Modified DVDSwitchToDisplay()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDSwitchToDisplay (     CGDirectDisplayID newDisplay,     Boolean *outSupported ); ``` |
| To | ``` OSStatus DVDSwitchToDisplay (     CGDirectDisplayID newDisplay,     Boolean * _Nonnull outSupported ); ``` |

Modified DVDUnregisterEventCallBack()

|  | Declaration |
| --- | --- |
| From | ``` OSStatus DVDUnregisterEventCallBack (     DVDEventCallBackRef inCallBackID ); ``` |
| To | ``` OSStatus DVDUnregisterEventCallBack (     DVDEventCallBackRef _Nonnull inCallBackID ); ``` |

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
