---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/DrawSprocket.html
archived_at: '2026-07-18T02:53:32.215358Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# DrawSprocket Changes for Swift

### DrawSprocket (Removed)

Removed DSpAltBufferAttributes [struct]Removed DSpAltBufferAttributes.heightRemoved DSpAltBufferAttributes.init()Removed DSpAltBufferAttributes.init(width: UInt32, height: UInt32, options: DSpAltBufferOption, reserved: (UInt32, UInt32, UInt32, UInt32))Removed DSpAltBufferAttributes.optionsRemoved DSpAltBufferAttributes.reservedRemoved DSpAltBufferAttributes.widthRemoved DSpAltBufferOption [struct]Removed DSpAltBufferOption.init(_: UInt32)Removed DSpAltBufferOption.valueRemoved DSpBlitInfo [struct]Removed DSpBlitInfo.completionFlagRemoved DSpBlitInfo.completionProcRemoved DSpBlitInfo.dstBufferRemoved DSpBlitInfo.dstContextRemoved DSpBlitInfo.dstKeyRemoved DSpBlitInfo.dstRectRemoved DSpBlitInfo.fillerRemoved DSpBlitInfo.init()Removed DSpBlitInfo.init(completionFlag: Boolean, filler: (Int8, Int8, Int8), completionProc: DSpBlitDoneProc, srcContext: DSpContextReference, srcBuffer: CGrafPtr, srcRect: Rect, srcKey: UInt32, dstContext: DSpContextReference, dstBuffer: CGrafPtr, dstRect: Rect, dstKey: UInt32, mode: DSpBlitMode, reserved: (UInt32, UInt32, UInt32, UInt32))Removed DSpBlitInfo.modeRemoved DSpBlitInfo.reservedRemoved DSpBlitInfo.srcBufferRemoved DSpBlitInfo.srcContextRemoved DSpBlitInfo.srcKeyRemoved DSpBlitInfo.srcRectRemoved DSpBlitMode [struct]Removed DSpBlitMode.init(_: UInt32)Removed DSpBlitMode.valueRemoved DSpBufferKind [struct]Removed DSpBufferKind.init(_: UInt32)Removed DSpBufferKind.valueRemoved DSpColorNeeds [struct]Removed DSpColorNeeds.init(_: UInt32)Removed DSpColorNeeds.valueRemoved DSpContextAttributes [struct]Removed DSpContextAttributes.backBufferBestDepthRemoved DSpContextAttributes.backBufferDepthMaskRemoved DSpContextAttributes.colorNeedsRemoved DSpContextAttributes.colorTableRemoved DSpContextAttributes.contextOptionsRemoved DSpContextAttributes.displayBestDepthRemoved DSpContextAttributes.displayDepthMaskRemoved DSpContextAttributes.displayHeightRemoved DSpContextAttributes.displayWidthRemoved DSpContextAttributes.fillerRemoved DSpContextAttributes.frequencyRemoved DSpContextAttributes.gameMustConfirmSwitchRemoved DSpContextAttributes.init()Removed DSpContextAttributes.init(frequency: Fixed, displayWidth: UInt32, displayHeight: UInt32, reserved1: UInt32, reserved2: UInt32, colorNeeds: UInt32, colorTable: CTabHandle, contextOptions: OptionBits, backBufferDepthMask: OptionBits, displayDepthMask: OptionBits, backBufferBestDepth: UInt32, displayBestDepth: UInt32, pageCount: UInt32, filler: (Int8, Int8, Int8), gameMustConfirmSwitch: Boolean, reserved3: (UInt32, UInt32, UInt32, UInt32))Removed DSpContextAttributes.pageCountRemoved DSpContextAttributes.reserved1Removed DSpContextAttributes.reserved2Removed DSpContextAttributes.reserved3Removed DSpContextOption [struct]Removed DSpContextOption.init(_: UInt32)Removed DSpContextOption.valueRemoved DSpContextState [struct]Removed DSpContextState.init(_: UInt32)Removed DSpContextState.valueRemoved DSpDepthMask [struct]Removed DSpDepthMask.init(_: Int32)Removed DSpDepthMask.valueRemoved DisplayIDTypeRemoved DSpAltBufferReferenceRemoved DSpBlitDoneProcRemoved DSpBlitInfoPtrRemoved DSpCallbackProcPtrRemoved DSpCallbackUPPRemoved DSpContextAttributesPtrRemoved DSpContextReferenceRemoved DSpContextReferenceConstRemoved DSpEventProcPtrRemoved DSpEventUPPRemoved kDSpAltBufferOption_RowBytesEqualsWidthRemoved kDSpBlitMode_DstKeyRemoved kDSpBlitMode_InterpolationRemoved kDSpBlitMode_PlainRemoved kDSpBlitMode_SrcKeyRemoved kDSpBufferKind_NormalRemoved kDSpColorNeeds_DontCareRemoved kDSpColorNeeds_RequestRemoved kDSpColorNeeds_RequireRemoved kDSpContextOption_DontSyncVBLRemoved kDSpContextOption_PageFlipRemoved kDSpContextOption_StereoscopicRemoved kDSpContextState_ActiveRemoved kDSpContextState_InactiveRemoved kDSpContextState_PausedRemoved kDSpDepthMask_1Removed kDSpDepthMask_16Removed kDSpDepthMask_2Removed kDSpDepthMask_32Removed kDSpDepthMask_4Removed kDSpDepthMask_8Removed kDSpDepthMask_All

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
