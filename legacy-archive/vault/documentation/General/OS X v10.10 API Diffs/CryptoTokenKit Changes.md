---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/CryptoTokenKit.html
archived_at: '2026-07-15T07:34:45.465398Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# CryptoTokenKit Changes

## CryptoTokenKit (Added)

CryptoTokenKit.h (Added)TKError.h (Added)Added [TKErrorAuthenticationFailed](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorauthenticationfailed)Added [TKErrorCode](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code)Added [TKErrorCodeCanceledByUser](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/canceledbyuser)Added [TKErrorCodeCommunicationError](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/communicationerror)Added [TKErrorCodeCorruptedData](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/corrupteddata)Added [TKErrorCodeNotImplemented](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodenotimplemented)Added [TKErrorDomain](https://developer.apple.com/documentation/cryptotokenkit/tkerrordomain)Added [TKErrorObjectNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/1393807-tkerrorobjectnotfound)Added [TKErrorTokenNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrortokennotfound)TKSmartCard.h (Added)Added [TKSmartCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard)Added [TKSmartCard.allowedProtocols](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390253-allowedprotocols)Added [-[TKSmartCard beginSessionWithReply:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390168-beginsession)Added [TKSmartCard.cla](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390158-cla)Added [TKSmartCard.context](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390243-context)Added [TKSmartCard.currentProtocol](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390172-currentprotocol)Added [-[TKSmartCard endSession]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390271-endsession)Added [-[TKSmartCard sendIns:p1:p2:data:le:reply:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390283-sendins)Added [TKSmartCard.sensitive](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390216-issensitive)Added [TKSmartCard.slot](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390281-slot)Added [-[TKSmartCard transmitRequest:reply:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390161-transmitrequest)Added [TKSmartCard.useExtendedLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390239-useextendedlength)Added [TKSmartCard.valid](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390194-valid)Added [TKSmartCardSlot](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot)Added [TKSmartCardSlot.ATR](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390285-atr)Added [-[TKSmartCardSlot makeSmartCard]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390225-makesmartcard)Added [TKSmartCardSlot.maxInputLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390302-maxinputlength)Added [TKSmartCardSlot.maxOutputLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390170-maxoutputlength)Added [TKSmartCardSlot.name](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390186-name)Added [TKSmartCardSlot.state](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390293-state)Added [TKSmartCardSlotManager](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager)Added [+[TKSmartCardSlotManager defaultManager]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390245-defaultmanager)Added [-[TKSmartCardSlotManager getSlotWithName:reply:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390265-getslotwithname)Added [TKSmartCardSlotManager.slotNames](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390156-slotnames)Added TKSmartCard(APDULevelTransmit)Added TKSmartCardNoSlotAdded TKSmartCardSlotEmptyAdded TKSmartCardSlotMuteCardAdded TKSmartCardSlotProbingAdded [TKSmartCardSlotState](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotstate)Added [TKSmartCardSlotStateEmpty](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state/empty)Added [TKSmartCardSlotStateMissing](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state/missing)Added [TKSmartCardSlotStateMuteCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotstate/tksmartcardslotstatemutecard)Added [TKSmartCardSlotStateProbing](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state/probing)Added [TKSmartCardSlotStateValidCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state/validcard)Added TKSmartCardSlotValidCardTKSmartCardATR.h (Added)Added [TKSmartCardATR](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr)Added [TKSmartCardATR.bytes](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403518-bytes)Added [TKSmartCardATR.historicalBytes](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403513-historicalbytes)Added [-[TKSmartCardATR initWithBytes:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403560-init)Added [-[TKSmartCardATR initWithSource:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403516-initwithsource)Added [-[TKSmartCardATR interfaceGroupAtIndex:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403537-interfacegroup)Added [-[TKSmartCardATR interfaceGroupForProtocol:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403483-interfacegroup)Added [TKSmartCardATR.protocols](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403472-protocols)Added [TKSmartCardATRInterfaceGroup](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatrinterfacegroup)Added [TKSmartCardATRInterfaceGroup.TA](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup/1403499-ta)Added [TKSmartCardATRInterfaceGroup.TB](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatrinterfacegroup/1403452-tb)Added [TKSmartCardATRInterfaceGroup.TC](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup/1403438-tc)Added [TKSmartCardATRInterfaceGroup.protocol](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatrinterfacegroup/1403429-protocol)Added [TKSmartCardProtocol](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol)Added [TKSmartCardProtocolAny](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol/tksmartcardprotocolany)Added [TKSmartCardProtocolNone](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol/tksmartcardprotocolnone)Added [TKSmartCardProtocolT0](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol/1403431-t0)Added [TKSmartCardProtocolT1](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol/1403553-t1)Added [TKSmartCardProtocolT15](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol/1403443-t15)

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
