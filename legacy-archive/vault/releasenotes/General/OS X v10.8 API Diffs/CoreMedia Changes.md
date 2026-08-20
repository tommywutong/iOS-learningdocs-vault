---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/CoreMedia.html
archived_at: '2026-07-18T02:53:58.467125Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# CoreMedia Changes

## CoreMedia

CMAudioDeviceClock.hAdded [CMAudioDeviceClockCreate()](https://developer.apple.com/documentation/coremedia/1409883-cmaudiodeviceclockcreate)Added [CMAudioDeviceClockCreateFromAudioDeviceID()](https://developer.apple.com/documentation/coremedia/1409881-cmaudiodeviceclockcreatefromaudi)Added [CMAudioDeviceClockGetAudioDevice()](https://developer.apple.com/documentation/coremedia/1409885-cmaudiodeviceclockgetaudiodevice)Added [CMAudioDeviceClockSetAudioDeviceID()](https://developer.apple.com/documentation/coremedia/1409877-cmaudiodeviceclocksetaudiodevice)Added [CMAudioDeviceClockSetAudioDeviceUID()](https://developer.apple.com/documentation/coremedia/1409879-cmaudiodeviceclocksetaudiodevice)CMBase.hAdded #def AVAILABLE_MAC_OS_X_VERSION_10_8_AND_LATERCMFormatDescription.hRemoved [kCMMediaType_TimedMetadata](https://developer.apple.com/documentation/coremedia/cmmediatype/kcmmediatype_timedmetadata)Removed [kCMTimedMetadataFormatType_Boxed](https://developer.apple.com/documentation/coremedia/cmmetadataformattype/kcmtimedmetadataformattype_boxed)Removed [kCMTimedMetadataFormatType_ICY](https://developer.apple.com/documentation/coremedia/cmmetadataformattype/kcmtimedmetadataformattype_icy)Removed [kCMTimedMetadataFormatType_ID3](https://developer.apple.com/documentation/coremedia/cmmetadataformattype/kcmtimedmetadataformattype_id3)Added #def CMSubtitleFormatDescriptionGetFormatTypeAdded [CMSubtitleFormatType](https://developer.apple.com/documentation/coremedia/cmsubtitleformattype)Added [kCMFormatDescriptionColorPrimaries_P22](https://developer.apple.com/documentation/coremedia/kcmformatdescriptioncolorprimaries_p22)Added [kCMMediaType_Metadata](https://developer.apple.com/documentation/coremedia/kcmmediatype_metadata)Added [kCMMetadataFormatType_Boxed](https://developer.apple.com/documentation/coremedia/kcmmetadataformattype_boxed)Added [kCMMetadataFormatType_ICY](https://developer.apple.com/documentation/coremedia/kcmmetadataformattype_icy)Added [kCMMetadataFormatType_ID3](https://developer.apple.com/documentation/coremedia/1564222-cmmetadataformattype/kcmmetadataformattype_id3)Added [kCMSubtitleFormatType_3GText](https://developer.apple.com/documentation/coremedia/1564237-cmsubtitleformattype/kcmsubtitleformattype_3gtext)Added [kCMSubtitleFormatType_WebVTT](https://developer.apple.com/documentation/coremedia/kcmsubtitleformattype_webvtt)Added [kCMTextDisplayFlag_obeySubtitleFormatting](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_obeysubtitleformatting)CMMemoryPool.hAdded #def CMMEMORYPOOL_HAdded [CMMemoryPoolCreate()](https://developer.apple.com/documentation/coremedia/1489395-cmmemorypoolcreate)Added [CMMemoryPoolFlush()](https://developer.apple.com/documentation/coremedia/1489661-cmmemorypoolflush)Added [CMMemoryPoolGetAllocator()](https://developer.apple.com/documentation/coremedia/1489675-cmmemorypoolgetallocator)Added [CMMemoryPoolGetTypeID()](https://developer.apple.com/documentation/coremedia/1489215-cmmemorypoolgettypeid)Added [CMMemoryPoolInvalidate()](https://developer.apple.com/documentation/coremedia/1489674-cmmemorypoolinvalidate)Added [CMMemoryPoolRef](https://developer.apple.com/documentation/coremedia/cmmemorypoolref)Added [kCMMemoryPoolOption_AgeOutPeriod](https://developer.apple.com/documentation/coremedia/kcmmemorypooloption_ageoutperiod)CMSampleBuffer.hAdded [kCMSampleBufferConduitNotificationParameter_MaxUpcomingOutputPTS](https://developer.apple.com/documentation/coremedia/kcmsamplebufferconduitnotificationparameter_maxupcomingoutputpts)CMSync.hAdded [CMClockConvertHostTimeToSystemUnits()](https://developer.apple.com/documentation/coremedia/1489638-cmclockconverthosttimetosystemun)Added [CMClockGetAnchorTime()](https://developer.apple.com/documentation/coremedia/1489299-cmclockgetanchortime)Added [CMClockGetHostTimeClock()](https://developer.apple.com/documentation/coremedia/1489402-cmclockgethosttimeclock)Added [CMClockGetTime()](https://developer.apple.com/documentation/coremedia/1489382-cmclockgettime)Added [CMClockGetTypeID()](https://developer.apple.com/documentation/coremedia/1489184-cmclockgettypeid)Added [CMClockInvalidate()](https://developer.apple.com/documentation/coremedia/1489202-cmclockinvalidate)Added [CMClockMakeHostTimeFromSystemUnits()](https://developer.apple.com/documentation/coremedia/1489195-cmclockmakehosttimefromsystemuni)Added [CMClockMightDrift()](https://developer.apple.com/documentation/coremedia/1489494-cmclockmightdrift)Added [CMClockOrTimebaseRef](https://developer.apple.com/documentation/coremedia/cmclockortimebaseref)Added [CMClockRef](https://developer.apple.com/documentation/coremedia/cmclockref)Added [CMSyncConvertTime()](https://developer.apple.com/documentation/coremedia/1489632-cmsyncconverttime)Added [CMSyncGetRelativeRate()](https://developer.apple.com/documentation/coremedia/1489528-cmsyncgetrelativerate)Added [CMSyncGetRelativeRateAndAnchorTime()](https://developer.apple.com/documentation/coremedia/1489570-cmsyncgetrelativerateandanchorti)Added [CMSyncGetTime()](https://developer.apple.com/documentation/coremedia/1489233-cmsyncgettime)Added [CMSyncMightDrift()](https://developer.apple.com/documentation/coremedia/1489610-cmsyncmightdrift)Added [CMTimebaseAddTimer()](https://developer.apple.com/documentation/coremedia/1489654-cmtimebaseaddtimer)Added [CMTimebaseAddTimerDispatchSource()](https://developer.apple.com/documentation/coremedia/1489429-cmtimebaseaddtimerdispatchsource)Added [CMTimebaseCreateWithMasterClock()](https://developer.apple.com/documentation/coremedia/1489367-cmtimebasecreatewithmasterclock)Added [CMTimebaseCreateWithMasterTimebase()](https://developer.apple.com/documentation/coremedia/1489132-cmtimebasecreatewithmastertimeba)Added [CMTimebaseGetEffectiveRate()](https://developer.apple.com/documentation/coremedia/1489313-cmtimebasegeteffectiverate)Added [CMTimebaseGetMaster()](https://developer.apple.com/documentation/coremedia/1489764-cmtimebasegetmaster)Added [CMTimebaseGetMasterClock()](https://developer.apple.com/documentation/coremedia/1489691-cmtimebasegetmasterclock)Added [CMTimebaseGetMasterTimebase()](https://developer.apple.com/documentation/coremedia/1489484-cmtimebasegetmastertimebase)Added [CMTimebaseGetRate()](https://developer.apple.com/documentation/coremedia/1489302-cmtimebasegetrate)Added [CMTimebaseGetTime()](https://developer.apple.com/documentation/coremedia/1489812-cmtimebasegettime)Added [CMTimebaseGetTimeAndRate()](https://developer.apple.com/documentation/coremedia/1489415-cmtimebasegettimeandrate)Added [CMTimebaseGetTimeWithTimeScale()](https://developer.apple.com/documentation/coremedia/1489700-cmtimebasegettimewithtimescale)Added [CMTimebaseGetTypeID()](https://developer.apple.com/documentation/coremedia/1489285-cmtimebasegettypeid)Added [CMTimebaseGetUltimateMasterClock()](https://developer.apple.com/documentation/coremedia/1489671-cmtimebasegetultimatemasterclock)Added [CMTimebaseNotificationBarrier()](https://developer.apple.com/documentation/coremedia/1489171-cmtimebasenotificationbarrier)Added [CMTimebaseRef](https://developer.apple.com/documentation/coremedia/cmtimebase)Added [CMTimebaseRemoveTimer()](https://developer.apple.com/documentation/coremedia/1489746-cmtimebaseremovetimer)Added [CMTimebaseRemoveTimerDispatchSource()](https://developer.apple.com/documentation/coremedia/1489198-cmtimebaseremovetimerdispatchsou)Added [CMTimebaseSetAnchorTime()](https://developer.apple.com/documentation/coremedia/1489504-cmtimebasesetanchortime)Added [CMTimebaseSetRate()](https://developer.apple.com/documentation/coremedia/1489590-cmtimebasesetrate)Added [CMTimebaseSetRateAndAnchorTime()](https://developer.apple.com/documentation/coremedia/1489332-cmtimebasesetrateandanchortime)Added [CMTimebaseSetTime()](https://developer.apple.com/documentation/coremedia/1489372-cmtimebasesettime)Added [CMTimebaseSetTimerDispatchSourceNextFireTime()](https://developer.apple.com/documentation/coremedia/1489489-cmtimebasesettimerdispatchsource)Added [CMTimebaseSetTimerDispatchSourceToFireImmediately()](https://developer.apple.com/documentation/coremedia/1489552-cmtimebasesettimerdispatchsource)Added [CMTimebaseSetTimerNextFireTime()](https://developer.apple.com/documentation/coremedia/1489692-cmtimebasesettimernextfiretime)Added [CMTimebaseSetTimerToFireImmediately()](https://developer.apple.com/documentation/coremedia/1489213-cmtimebasesettimertofireimmediat)Added [kCMClockError_AllocationFailed](https://developer.apple.com/documentation/coremedia/kcmclockerror_allocationfailed)Added [kCMClockError_InvalidParameter](https://developer.apple.com/documentation/coremedia/1509592-cmclock_error_codes/kcmclockerror_invalidparameter)Added [kCMClockError_MissingRequiredParameter](https://developer.apple.com/documentation/coremedia/1509592-cmclock_error_codes/kcmclockerror_missingrequiredparameter)Added [kCMClockError_UnsupportedOperation](https://developer.apple.com/documentation/coremedia/kcmclockerror_unsupportedoperation)Added [kCMSyncError_AllocationFailed](https://developer.apple.com/documentation/coremedia/kcmsyncerror_allocationfailed)Added [kCMSyncError_InvalidParameter](https://developer.apple.com/documentation/coremedia/kcmsyncerror_invalidparameter)Added [kCMSyncError_MissingRequiredParameter](https://developer.apple.com/documentation/coremedia/kcmsyncerror_missingrequiredparameter)Added [kCMSyncError_RateMustBeNonZero](https://developer.apple.com/documentation/coremedia/kcmsyncerror_ratemustbenonzero)Added [kCMTimebaseError_AllocationFailed](https://developer.apple.com/documentation/coremedia/1509568-cmtimebase_error_codes/kcmtimebaseerror_allocationfailed)Added [kCMTimebaseError_InvalidParameter](https://developer.apple.com/documentation/coremedia/1509568-cmtimebase_error_codes/kcmtimebaseerror_invalidparameter)Added [kCMTimebaseError_MissingRequiredParameter](https://developer.apple.com/documentation/coremedia/kcmtimebaseerror_missingrequiredparameter)Added [kCMTimebaseError_ReadOnly](https://developer.apple.com/documentation/coremedia/1509568-cmtimebase_error_codes/kcmtimebaseerror_readonly)Added [kCMTimebaseError_TimerIntervalTooShort](https://developer.apple.com/documentation/coremedia/1509568-cmtimebase_error_codes/kcmtimebaseerror_timerintervaltooshort)Added #def kCMTimebaseFarFutureCFAbsoluteTimeAdded [kCMTimebaseNotification_EffectiveRateChanged](https://developer.apple.com/documentation/coremedia/kcmtimebasenotification_effectiveratechanged)Added [kCMTimebaseNotification_TimeJumped](https://developer.apple.com/documentation/coremedia/kcmtimebasenotification_timejumped)Added #def kCMTimebaseVeryLongCFTimeInterval

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
