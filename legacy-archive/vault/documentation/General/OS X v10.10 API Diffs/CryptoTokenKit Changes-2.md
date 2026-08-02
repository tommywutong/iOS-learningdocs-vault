---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/CryptoTokenKit.html
archived_at: '2026-07-15T07:34:53.045814Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CryptoTokenKit Changes

## CryptoTokenKit (Added)

Added TKErrorCode [enum]Added TKErrorCode.AuthenticationFailedAdded TKErrorCode.CodeCanceledByUserAdded TKErrorCode.CodeCommunicationErrorAdded TKErrorCode.CodeCorruptedDataAdded TKErrorCode.CodeNotImplementedAdded TKErrorCode.ObjectNotFoundAdded TKErrorCode.TokenNotFoundAdded TKSmartCardAdded TKSmartCard.allowedProtocolsAdded TKSmartCard.beginSessionWithReply(((Bool, NSError!) -> Void)!)Added TKSmartCard.claAdded TKSmartCard.contextAdded TKSmartCard.currentProtocolAdded TKSmartCard.endSession()Added TKSmartCard.sendIns(UInt8, p1: UInt8, p2: UInt8, data: NSData!, le: NSNumber!, reply:((NSData!, UInt16, NSError!) -> Void)!)Added TKSmartCard.sensitiveAdded TKSmartCard.slotAdded TKSmartCard.transmitRequest(NSData!, reply:((NSData!, NSError!) -> Void)!)Added TKSmartCard.useExtendedLengthAdded TKSmartCard.validAdded TKSmartCardATRAdded TKSmartCardATR.bytesAdded TKSmartCardATR.init(bytes: NSData!)Added TKSmartCardATR.historicalBytesAdded TKSmartCardATR.interfaceGroupAtIndex(Int) -> TKSmartCardATRInterfaceGroup!Added TKSmartCardATR.interfaceGroupForProtocol(TKSmartCardProtocol) -> TKSmartCardATRInterfaceGroup!Added TKSmartCardATR.protocolsAdded TKSmartCardATR.init(source: (() -> Int32)!)Added TKSmartCardATRInterfaceGroupAdded TKSmartCardATRInterfaceGroup.TAAdded TKSmartCardATRInterfaceGroup.TBAdded TKSmartCardATRInterfaceGroup.TCAdded TKSmartCardATRInterfaceGroup.protocolAdded TKSmartCardProtocol [struct]Added TKSmartCardProtocol.AnyAdded TKSmartCardProtocol.NoneAdded TKSmartCardProtocol.T0Added TKSmartCardProtocol.T1Added TKSmartCardProtocol.T15Added TKSmartCardProtocol.init(_: UInt)Added TKSmartCardProtocol.init(rawValue: UInt)Added TKSmartCardSlotAdded TKSmartCardSlot.ATRAdded TKSmartCardSlot.makeSmartCard() -> TKSmartCard!Added TKSmartCardSlot.maxInputLengthAdded TKSmartCardSlot.maxOutputLengthAdded TKSmartCardSlot.nameAdded TKSmartCardSlot.stateAdded TKSmartCardSlotManagerAdded TKSmartCardSlotManager.defaultManager() -> Self! [class]Added TKSmartCardSlotManager.getSlotWithName(String!, reply:((TKSmartCardSlot!) -> Void)!)Added TKSmartCardSlotManager.slotNamesAdded TKSmartCardSlotState [enum]Added TKSmartCardSlotState.SlotStateEmptyAdded TKSmartCardSlotState.SlotStateMissingAdded TKSmartCardSlotState.SlotStateMuteCardAdded TKSmartCardSlotState.SlotStateProbingAdded TKSmartCardSlotState.SlotStateValidCardAdded TKErrorDomain

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
