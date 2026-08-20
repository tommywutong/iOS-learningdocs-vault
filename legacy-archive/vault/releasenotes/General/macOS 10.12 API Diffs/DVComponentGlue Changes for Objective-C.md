---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/DVComponentGlue.html
archived_at: '2026-07-18T02:50:38.567027Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# DVComponentGlue Changes for Objective-C

### DVComponentGlue

#### DeviceControl.h (Removed)

Removed DCResponseHandlerRemoved DeviceControlDoAVCTransaction()Removed DVCTransactionParamsRemoved kDeviceControlDoAVCTransactionSelect

#### IsochronousDataHandler.h (Removed)

Removed DisposeIDHNotificationUPP()Removed IDHCancelNotification()Removed IDHCancelPendingIO()Removed IDHCloseDevice()Removed IDHDeviceConnectionEventRemoved IDHDeviceFrameDroppedEventRemoved IDHDeviceIDRemoved IDHDeviceIOEnableEventRemoved IDHDeviceStatusRemoved IDHDimensionRemoved IDHDisposeNotification()Removed IDHEventRemoved IDHEventHeaderRemoved IDHGenericEventRemoved IDHGetDeviceClock()Removed IDHGetDeviceConfiguration()Removed IDHGetDeviceControl()Removed IDHGetDeviceList()Removed IDHGetDeviceStatus()Removed IDHGetDeviceTime()Removed IDHGetFormat()Removed IDHIsochIntervalRemoved IDHNewNotification()Removed IDHNotificationIDRemoved IDHNotificationProcRemoved IDHNotificationProcPtrRemoved IDHNotificationUPPRemoved IDHNotifyMeWhen()Removed IDHOpenDevice()Removed IDHParameterBlockRemoved IDHRead()Removed IDHReleaseBuffer()Removed IDHResolutionRemoved IDHSetDeviceConfiguration()Removed IDHSetFormat()Removed IDHUpdateDeviceList()Removed IDHWrite()Removed InvokeIDHNotificationUPP()Removed kIDHCancelNotificationSelectRemoved kIDHCancelPendingIOSelectRemoved kIDHCloseDeviceSelectRemoved kIDHCloseForReadTransactionsRemoved kIDHCloseForWriteTransactionsRemoved kIDHComponentTypeRemoved kIDHDataBufferSizeAtomTypeRemoved kIDHDataIntervalAtomTypeRemoved kIDHDataIODirectionAtomTypeRemoved kIDHDataSizeAtomTypeRemoved kIDHDataTypeAtomTypeRemoved kIDHDataTypeIsInputRemoved kIDHDataTypeIsInputAndOutputRemoved kIDHDataTypeIsOutputRemoved kIDHDefaultIOTypeRemoved kIDHDeviceAtomTypeRemoved kIDHDeviceIDEveryDeviceRemoved kIDHDeviceIDTypeRemoved kIDHDeviceListAtomTypeRemoved kIDHDisposeNotificationSelectRemoved kIDHDV_HDRemoved kIDHDV_SDRemoved kIDHDV_SDLRemoved kIDHDVCPro_25Removed kIDHDVCPro_50Removed kIDHErrCallNotSupportedRemoved kIDHErrCompletionPendingRemoved kIDHErrDeviceBusyRemoved kIDHErrDeviceCantReadRemoved kIDHErrDeviceCantWriteRemoved kIDHErrDeviceDisconnectedRemoved kIDHErrDeviceInUseRemoved kIDHErrDeviceListRemoved kIDHErrDeviceNotConfiguredRemoved kIDHErrDeviceNotOpenedRemoved kIDHErrDeviceReadErrorRemoved kIDHErrDeviceTimeoutRemoved kIDHErrDeviceWriteErrorRemoved kIDHErrInvalidDeviceIDRemoved kIDHErrInvalidIndexRemoved kIDHEventDeviceAddedRemoved kIDHEventDeviceChangedRemoved kIDHEventDeviceRemovedRemoved kIDHEventEveryEventRemoved kIDHEventFrameDroppedRemoved kIDHEventInvalidRemoved kIDHEventReadDisabledRemoved kIDHEventReadEnabledRemoved kIDHEventReserved2Removed kIDHEventWriteDisabledRemoved kIDHEventWriteEnabledRemoved kIDHGetDeviceClockSelectRemoved kIDHGetDeviceConfigurationSelectRemoved kIDHGetDeviceControlSelectRemoved kIDHGetDeviceListSelectRemoved kIDHGetDeviceStatusSelectRemoved kIDHGetDeviceTimeSelectRemoved kIDHGetFormatSelectRemoved kIDHInterfaceVersion1Removed kIDHInvalidDeviceIDRemoved kIDHIsochMediaTypeRemoved kIDHIsochModeAtomTypeRemoved kIDHIsochServiceAtomTypeRemoved kIDHIsochVersionAtomTypeRemoved kIDHNameAtomTypeRemoved kIDHNewNotificationSelectRemoved kIDHNotifyMeWhenSelectRemoved kIDHOpenDeviceSelectRemoved kIDHOpenForReadTransactionsRemoved kIDHOpenForWriteTransactionsRemoved kIDHOpenWithExclusiveAccessRemoved kIDHOpenWithHeldBuffersRemoved kIDHReadSelectRemoved kIDHReleaseBufferSelectRemoved kIDHSetDeviceConfigurationSelectRemoved kIDHSetFormatSelectRemoved kIDHSoundChannelCountAtomTypeRemoved kIDHSoundMediaAtomTypeRemoved kIDHSoundSampleRateAtomTypeRemoved kIDHSoundSampleSizeAtomTypeRemoved kIDHSoundTypeAtomTypeRemoved kIDHSubtypeDVRemoved kIDHSubtypeFireWireConferenceRemoved kIDHUniqueIDTypeRemoved kIDHUpdateDeviceListSelectRemoved kIDHUseCMPAtomTypeRemoved kIDHVideoDecompressorAtomTypeRemoved kIDHVideoDecompressorComponentAtomTypeRemoved kIDHVideoDecompressorContinuousAtomTypeRemoved kIDHVideoDecompressorTypeAtomTypeRemoved kIDHVideoDimensionsAtomTypeRemoved kIDHVideoMediaAtomTypeRemoved kIDHVideoPixelTypeAtomTypeRemoved kIDHVideoRefreshRateAtomTypeRemoved kIDHVideoResolutionAtomTypeRemoved kIDHWriteSelectRemoved NewIDHNotificationUPP()Removed PsuedoID

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
