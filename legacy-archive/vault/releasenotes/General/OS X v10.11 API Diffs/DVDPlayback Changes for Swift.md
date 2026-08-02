---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/DVDPlayback.html
archived_at: '2026-07-18T02:53:30.602969Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# DVDPlayback Changes for Swift

### DVDPlayback

Removed DVDAspectRatioRemoved DVDAudioFormatRemoved DVDDomainCodeRemoved DVDEventCodeRemoved DVDFormatRemoved DVDMenuRemoved DVDScanDirectionRemoved DVDScanRateRemoved DVDStateRemoved DVDUserNavigationRemoved kDVDAMGMDomainRemoved kDVDAspectRatio16x9Removed kDVDAspectRatio4x3Removed kDVDAspectRatio4x3PanAndScanRemoved kDVDAspectRatioLetterBoxRemoved kDVDAspectRatioUninitializedRemoved kDVDAudioAC3FormatRemoved kDVDAudioDDPlusFormatRemoved kDVDAudioDTSFormatRemoved kDVDAudioDTSHDFormatRemoved kDVDAudioMLPFormatRemoved kDVDAudioMPEG1FormatRemoved kDVDAudioMPEG2FormatRemoved kDVDAudioPCMFormatRemoved kDVDAudioSDDSFormatRemoved kDVDAudioUnknownFormatRemoved kDVDEventAngleRemoved kDVDEventAngleNumbersRemoved kDVDEventAudioStreamRemoved kDVDEventAudioStreamNumbersRemoved kDVDEventBitrateRemoved kDVDEventCCInfoRemoved kDVDEventChapterTimeRemoved kDVDEventDisplayModeRemoved kDVDEventDomainRemoved kDVDEventErrorRemoved kDVDEventGPRMRemoved kDVDEventMenuCalledRemoved kDVDEventParentalRemoved kDVDEventPGCRemoved kDVDEventPlaybackRemoved kDVDEventPTTRemoved kDVDEventRegionMismatchRemoved kDVDEventScanSpeedRemoved kDVDEventStillRemoved kDVDEventStreamsRemoved kDVDEventSubpictureStreamRemoved kDVDEventSubpictureStreamNumbersRemoved kDVDEventTitleRemoved kDVDEventTitleTimeRemoved kDVDEventValidUOPRemoved kDVDEventVideoStandardRemoved kDVDFormatNTSCRemoved kDVDFormatNTSC_HDTVRemoved kDVDFormatPALRemoved kDVDFormatPAL_HDTVRemoved kDVDFormatUninitializedRemoved kDVDFPDomainRemoved kDVDMenuAngleRemoved kDVDMenuAudioRemoved kDVDMenuNoneRemoved kDVDMenuPTTRemoved kDVDMenuRootRemoved kDVDMenuSubPictureRemoved kDVDMenuTitleRemoved kDVDScanDirectionBackwardRemoved kDVDScanDirectionForwardRemoved kDVDScanRate16xRemoved kDVDScanRate1xRemoved kDVDScanRate2xRemoved kDVDScanRate32xRemoved kDVDScanRate4xRemoved kDVDScanRate8xRemoved kDVDScanRateOneEigthRemoved kDVDScanRateOneFourthRemoved kDVDScanRateOneHalfRemoved kDVDStateIdleRemoved kDVDStatePausedRemoved kDVDStatePlayingRemoved kDVDStatePlayingSlowRemoved kDVDStatePlayingStillRemoved kDVDStateScanningRemoved kDVDStateStoppedRemoved kDVDStateUnknownRemoved kDVDSTOPDomainRemoved kDVDTTDomainRemoved kDVDTTGRDomainRemoved kDVDUserNavigationEnterRemoved kDVDUserNavigationMoveDownRemoved kDVDUserNavigationMoveLeftRemoved kDVDUserNavigationMoveRightRemoved kDVDUserNavigationMoveUpRemoved kDVDVMGMDomainRemoved kDVDVTSMDomainAdded DVDAspectRatio [enum]Added DVDAspectRatio.Ratio16x9Added DVDAspectRatio.Ratio4x3Added DVDAspectRatio.Ratio4x3PanAndScanAdded DVDAspectRatio.RatioLetterBoxAdded DVDAspectRatio.RatioUninitializedAdded DVDAudioFormat [enum]Added DVDAudioFormat.AC3FormatAdded DVDAudioFormat.DDPlusFormatAdded DVDAudioFormat.DTSFormatAdded DVDAudioFormat.DTSHDFormatAdded DVDAudioFormat.MLPFormatAdded DVDAudioFormat.MPEG1FormatAdded DVDAudioFormat.MPEG2FormatAdded DVDAudioFormat.PCMFormatAdded DVDAudioFormat.SDDSFormatAdded DVDAudioFormat.UnknownFormatAdded DVDDomainCode [enum]Added DVDDomainCode.DVDAMGMDomainAdded DVDDomainCode.DVDFPDomainAdded DVDDomainCode.DVDSTOPDomainAdded DVDDomainCode.DVDTTDomainAdded DVDDomainCode.DVDTTGRDomainAdded DVDDomainCode.DVDVMGMDomainAdded DVDDomainCode.DVDVTSMDomainAdded DVDEventCode [enum]Added DVDEventCode.AngleAdded DVDEventCode.AngleNumbersAdded DVDEventCode.AudioStreamAdded DVDEventCode.AudioStreamNumbersAdded DVDEventCode.BitrateAdded DVDEventCode.CCInfoAdded DVDEventCode.ChapterTimeAdded DVDEventCode.DisplayModeAdded DVDEventCode.DomainAdded DVDEventCode.ErrorAdded DVDEventCode.GPRMAdded DVDEventCode.MenuCalledAdded DVDEventCode.ParentalAdded DVDEventCode.PGCAdded DVDEventCode.PlaybackAdded DVDEventCode.PTTAdded DVDEventCode.RegionMismatchAdded DVDEventCode.ScanSpeedAdded DVDEventCode.StillAdded DVDEventCode.StreamsAdded DVDEventCode.SubpictureStreamAdded DVDEventCode.SubpictureStreamNumbersAdded DVDEventCode.TitleAdded DVDEventCode.TitleTimeAdded DVDEventCode.ValidUOPAdded DVDEventCode.VideoStandardAdded DVDFormat [enum]Added DVDFormat.NTSCAdded DVDFormat.NTSC_HDTVAdded DVDFormat.PALAdded DVDFormat.PAL_HDTVAdded DVDFormat.UninitializedAdded DVDMenu [enum]Added DVDMenu.AngleAdded DVDMenu.AudioAdded DVDMenu.NoneAdded DVDMenu.PTTAdded DVDMenu.RootAdded DVDMenu.SubPictureAdded DVDMenu.TitleAdded DVDScanDirection [enum]Added DVDScanDirection.BackwardAdded DVDScanDirection.ForwardAdded DVDScanRate [enum]Added DVDScanRate.Rate16xAdded DVDScanRate.Rate1xAdded DVDScanRate.Rate2xAdded DVDScanRate.Rate32xAdded DVDScanRate.Rate4xAdded DVDScanRate.Rate8xAdded DVDScanRate.RateOneEigthAdded DVDScanRate.RateOneFourthAdded DVDScanRate.RateOneHalfAdded DVDState [enum]Added DVDState.IdleAdded DVDState.PausedAdded DVDState.PlayingAdded DVDState.PlayingSlowAdded DVDState.PlayingStillAdded DVDState.ScanningAdded DVDState.StoppedAdded DVDState.UnknownAdded DVDUserNavigation [enum]Added DVDUserNavigation.EnterAdded DVDUserNavigation.MoveDownAdded DVDUserNavigation.MoveLeftAdded DVDUserNavigation.MoveRightAdded DVDUserNavigation.MoveUpModified DVDDisplaySubPicture(_: Bool) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDDisplaySubPicture(_ inDisplay: Boolean) -> OSStatus ``` |
| To | ``` func DVDDisplaySubPicture(_ inDisplay: Bool) -> OSStatus ``` |

Modified DVDEnableWebAccess(_: Bool) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDEnableWebAccess(_ inEnable: Boolean) -> OSStatus ``` |
| To | ``` func DVDEnableWebAccess(_ inEnable: Bool) -> OSStatus ``` |

Modified DVDEventCallBackFunctionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DVDEventCallBackFunctionPtr = CFunctionPointer<((DVDEventCode, DVDEventValue, DVDEventValue, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DVDEventCallBackFunctionPtr = (DVDEventCode, DVDEventValue, DVDEventValue, UnsafeMutablePointer<Void>) -> Void ``` |

Modified DVDFatalErrCallBackFunctionPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DVDFatalErrCallBackFunctionPtr = CFunctionPointer<((DVDErrorCode, UnsafeMutablePointer<Void>) -> Void)> ``` |
| To | ``` typealias DVDFatalErrCallBackFunctionPtr = (DVDErrorCode, UnsafeMutablePointer<Void>) -> Void ``` |

Modified DVDHasMedia(_: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDHasMedia(_ outHasMedia: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDHasMedia(_ outHasMedia: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDHasMenu(_: DVDMenu, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDHasMenu(_ inMenu: DVDMenu, _ outHasMenu: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDHasMenu(_ inMenu: DVDMenu, _ outHasMenu: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDHasNextChapter(_: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDHasNextChapter(_ outHasChapter: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDHasNextChapter(_ outHasChapter: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDHasPreviousChapter(_: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDHasPreviousChapter(_ outHasChapter: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDHasPreviousChapter(_ outHasChapter: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDIsDisplayingSubPicture(_: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDIsDisplayingSubPicture(_ outDisplayingSubPicture: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDIsDisplayingSubPicture(_ outDisplayingSubPicture: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDIsMuted(_: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDIsMuted(_ outIsMuted: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDIsMuted(_ outIsMuted: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDIsOnMenu(_: UnsafeMutablePointer<DarwinBoolean>, _: UnsafeMutablePointer<DVDMenu>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDIsOnMenu(_ outOnMenu: UnsafeMutablePointer<Boolean>, _ outMenu: UnsafeMutablePointer<DVDMenu>) -> OSStatus ``` |
| To | ``` func DVDIsOnMenu(_ outOnMenu: UnsafeMutablePointer<DarwinBoolean>, _ outMenu: UnsafeMutablePointer<DVDMenu>) -> OSStatus ``` |

Modified DVDIsPaused(_: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDIsPaused(_ outIsPaused: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDIsPaused(_ outIsPaused: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDIsPlaying(_: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDIsPlaying(_ outIsPlaying: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDIsPlaying(_ outIsPlaying: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDIsRegisteredEventCallBack(_: DVDEventCallBackRef) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func DVDIsRegisteredEventCallBack(_ inCallBackID: DVDEventCallBackRef) -> Boolean ``` |
| To | ``` func DVDIsRegisteredEventCallBack(_ inCallBackID: DVDEventCallBackRef) -> Bool ``` |

Modified DVDIsSupportedDisplay(_: CGDirectDisplayID, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDIsSupportedDisplay(_ inDisplay: CGDirectDisplayID, _ outSupported: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDIsSupportedDisplay(_ inDisplay: CGDirectDisplayID, _ outSupported: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDIsValidMediaRef(_: UnsafeMutablePointer<FSRef>, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDIsValidMediaRef(_ inRef: UnsafeMutablePointer<FSRef>, _ outIsValid: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDIsValidMediaRef(_ inRef: UnsafeMutablePointer<FSRef>, _ outIsValid: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDIsValidMediaURL(_: CFURL, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDIsValidMediaURL(_ inRef: CFURL!, _ outIsValid: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDIsValidMediaURL(_ inRef: CFURL, _ outIsValid: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

Modified DVDMute(_: Bool) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDMute(_ inMute: Boolean) -> OSStatus ``` |
| To | ``` func DVDMute(_ inMute: Bool) -> OSStatus ``` |

Modified DVDOpenMediaFileWithURL(_: CFURL) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDOpenMediaFileWithURL(_ inFile: CFURL!) -> OSStatus ``` |
| To | ``` func DVDOpenMediaFileWithURL(_ inFile: CFURL) -> OSStatus ``` |

Modified DVDOpenMediaVolumeWithURL(_: CFURL) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDOpenMediaVolumeWithURL(_ inVolume: CFURL!) -> OSStatus ``` |
| To | ``` func DVDOpenMediaVolumeWithURL(_ inVolume: CFURL) -> OSStatus ``` |

Modified DVDSwitchToDisplay(_: CGDirectDisplayID, _: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func DVDSwitchToDisplay(_ newDisplay: CGDirectDisplayID, _ outSupported: UnsafeMutablePointer<Boolean>) -> OSStatus ``` |
| To | ``` func DVDSwitchToDisplay(_ newDisplay: CGDirectDisplayID, _ outSupported: UnsafeMutablePointer<DarwinBoolean>) -> OSStatus ``` |

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
