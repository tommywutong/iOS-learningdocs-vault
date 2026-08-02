---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CryptoTokenKit.html
archived_at: '2026-07-18T02:53:01.656143Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CryptoTokenKit Changes for Objective-C

### CryptoTokenKit

#### TKError.h

Added [TKErrorCodeAuthenticationFailed](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/authenticationfailed)Added [TKErrorCodeBadParameter](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/badparameter)Added [TKErrorCodeObjectNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/objectnotfound)Added [TKErrorCodeTokenNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/tokennotfound)Modified [TKErrorAuthenticationFailed](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorauthenticationfailed)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [TKErrorObjectNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/1393807-tkerrorobjectnotfound)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [TKErrorTokenNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrortokennotfound)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### TKSmartCard.h

Removed TKSmartCardNoSlotRemoved TKSmartCardSlotEmptyRemoved TKSmartCardSlotMuteCardRemoved TKSmartCardSlotProbingRemoved TKSmartCardSlotValidCardAdded [-[TKSmartCard userInteractionForSecurePINChangeWithPINFormat:APDU:currentPINByteOffset:newPINByteOffset:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390312-userinteractionforsecurepinchang)Added [-[TKSmartCard userInteractionForSecurePINVerificationWithPINFormat:APDU:PINByteOffset:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390289-userinteractionforsecurepinverif)Added [TKSmartCardPINFormat](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat)Added [TKSmartCardPINFormat.charset](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390176-charset)Added [TKSmartCardPINFormat.encoding](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390241-encoding)Added [TKSmartCardPINFormat.maxPINLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390182-maxpinlength)Added [TKSmartCardPINFormat.minPINLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390188-minpinlength)Added [TKSmartCardPINFormat.PINBitOffset](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390269-pinbitoffset)Added [TKSmartCardPINFormat.PINBlockByteLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390198-pinblockbytelength)Added [TKSmartCardPINFormat.PINJustification](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390190-pinjustification)Added [TKSmartCardPINFormat.PINLengthBitOffset](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390291-pinlengthbitoffset)Added [TKSmartCardPINFormat.PINLengthBitSize](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390314-pinlengthbitsize)Added [TKSmartCardUserInteraction](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction)Added [-[TKSmartCardUserInteraction cancel]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390231-cancel)Added [TKSmartCardUserInteraction.delegate](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390166-delegate)Added [TKSmartCardUserInteraction.initialTimeout](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390178-initialtimeout)Added [TKSmartCardUserInteraction.interactionTimeout](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390206-interactiontimeout)Added [-[TKSmartCardUserInteraction runWithReply:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390212-run)Added [TKSmartCardUserInteractionDelegate](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate)Added [-[TKSmartCardUserInteractionDelegate characterEnteredInUserInteraction:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390259-characterentered)Added [-[TKSmartCardUserInteractionDelegate correctionKeyPressedInUserInteraction:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390160-correctionkeypressedinuserintera)Added [-[TKSmartCardUserInteractionDelegate invalidCharacterEnteredInUserInteraction:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390180-invalidcharacterentered)Added [-[TKSmartCardUserInteractionDelegate newPINConfirmationRequestedInUserInteraction:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390263-newpinconfirmationrequestedinuse)Added [-[TKSmartCardUserInteractionDelegate newPINRequestedInUserInteraction:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390300-newpinrequested)Added [-[TKSmartCardUserInteractionDelegate oldPINRequestedInUserInteraction:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390316-oldpinrequested)Added [-[TKSmartCardUserInteractionDelegate validationKeyPressedInUserInteraction:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390164-validationkeypressedinuserintera)Added [TKSmartCardUserInteractionForPINOperation](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation)Added [TKSmartCardUserInteractionForPINOperation.locale](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390202-locale)Added [TKSmartCardUserInteractionForPINOperation.PINCompletion](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390184-pincompletion)Added [TKSmartCardUserInteractionForPINOperation.PINMessageIndices](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390192-pinmessageindices)Added [TKSmartCardUserInteractionForPINOperation.resultData](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390308-resultdata)Added [TKSmartCardUserInteractionForPINOperation.resultSW](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390200-resultsw)Added [TKSmartCardUserInteractionForSecurePINChange](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange)Added [TKSmartCardUserInteractionForSecurePINChange.PINConfirmation](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/1390310-pinconfirmation)Added [TKSmartCardUserInteractionForSecurePINVerification](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinverification)Added [TKSmartCardPINCharset](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/charset)Added [TKSmartCardPINCharsetAlphanumeric](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/charset/alphanumeric)Added [TKSmartCardPINCharsetNumeric](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/charset/numeric)Added [TKSmartCardPINCharsetUpperAlphanumeric](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/charset/upperalphanumeric)Added [TKSmartCardPINCompletion](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion)Added [TKSmartCardPINCompletionKey](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion/1390220-key)Added [TKSmartCardPINCompletionMaxLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion/1390298-maxlength)Added [TKSmartCardPINCompletionTimeout](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpincompletion/tksmartcardpincompletiontimeout)Added [TKSmartCardPINConfirmation](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinconfirmation)Added [TKSmartCardPINConfirmationCurrent](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/confirmation/1390162-current)Added [TKSmartCardPINConfirmationNew](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/confirmation/1390318-new)Added [TKSmartCardPINConfirmationNone](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinconfirmation/tksmartcardpinconfirmationnone)Added [TKSmartCardPINEncoding](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/encoding)Added [TKSmartCardPINEncodingASCII](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/encoding/ascii)Added [TKSmartCardPINEncodingBCD](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinencoding/tksmartcardpinencodingbcd)Added [TKSmartCardPINEncodingBinary](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinencoding/tksmartcardpinencodingbinary)Added [TKSmartCardPINJustification](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/justification)Added [TKSmartCardPINJustificationLeft](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/justification/left)Added [TKSmartCardPINJustificationRight](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinjustification/tksmartcardpinjustificationright)Modified [-[TKSmartCard beginSessionWithReply:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390168-beginsession)

|  | Declaration |
| --- | --- |
| From | ``` - (void)beginSessionWithReply:(void (^)(BOOL success, NSError *error))reply ``` |
| To | ``` - (void)beginSessionWithReply:(void (^ _Nonnull)(BOOL success, NSError * _Nullable error))reply ``` |

Modified [TKSmartCard.context](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390243-context)

|  | Declaration |
| --- | --- |
| From | ``` @property id context ``` |
| To | ``` @property(nullable) id context ``` |

Modified [-[TKSmartCard sendIns:p1:p2:data:le:reply:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390283-sendins)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sendIns:(UInt8)ins p1:(UInt8)p1 p2:(UInt8)p2 data:(NSData *)requestData le:(NSNumber *)le reply:(void (^)(NSData *replyData, UInt16 sw, NSError *error))reply ``` |
| To | ``` - (void)sendIns:(UInt8)ins p1:(UInt8)p1 p2:(UInt8)p2 data:(NSData * _Nonnull)requestData le:(NSNumber * _Nullable)le reply:(void (^ _Nonnull)(NSData * _Nullable replyData, UInt16 sw, NSError * _Nullable error))reply ``` |

Modified [TKSmartCard.slot](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390281-slot)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) TKSmartCardSlot *slot ``` |
| To | ``` @property(nonatomic, readonly, nonnull) TKSmartCardSlot *slot ``` |

Modified [-[TKSmartCard transmitRequest:reply:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390161-transmitrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (void)transmitRequest:(NSData *)request reply:(void (^)(NSData *response, NSError *error))reply ``` |
| To | ``` - (void)transmitRequest:(NSData * _Nonnull)request reply:(void (^ _Nonnull)(NSData * _Nullable response, NSError * _Nullable error))reply ``` |

Modified [TKSmartCardSlot.ATR](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390285-atr)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) TKSmartCardATR *ATR ``` |
| To | ``` @property(readonly, nullable) TKSmartCardATR *ATR ``` |

Modified [-[TKSmartCardSlot makeSmartCard]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390225-makesmartcard)

|  | Declaration |
| --- | --- |
| From | ``` - (TKSmartCard *)makeSmartCard ``` |
| To | ``` - (TKSmartCard * _Nullable)makeSmartCard ``` |

Modified [TKSmartCardSlot.name](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390186-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *name ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *name ``` |

Modified [+[TKSmartCardSlotManager defaultManager]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390245-defaultmanager)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)defaultManager ``` |
| To | ``` + (instancetype _Nullable)defaultManager ``` |

Modified [-[TKSmartCardSlotManager getSlotWithName:reply:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390265-getslotwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (void)getSlotWithName:(NSString *)name reply:(void (^)(TKSmartCardSlot *slot))reply ``` |
| To | ``` - (void)getSlotWithName:(NSString * _Nonnull)name reply:(void (^ _Nonnull)(TKSmartCardSlot * _Nullable slot))reply ``` |

Modified [TKSmartCardSlotManager.slotNames](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390156-slotnames)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *slotNames ``` |
| To | ``` @property(readonly, nonnull) NSArray<NSString *> *slotNames ``` |

#### TKSmartCardATR.h

Modified [TKSmartCardATR.bytes](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403518-bytes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSData *bytes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSData *bytes ``` |

Modified [TKSmartCardATR.historicalBytes](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403513-historicalbytes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSData *historicalBytes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSData *historicalBytes ``` |

Modified [-[TKSmartCardATR initWithBytes:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403560-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithBytes:(NSData *)bytes ``` |
| To | ``` - (instancetype _Nullable)initWithBytes:(NSData * _Nonnull)bytes ``` |

Modified [-[TKSmartCardATR initWithSource:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403516-initwithsource)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSource:(int (^)(void))source ``` |
| To | ``` - (instancetype _Nullable)initWithSource:(int (^ _Nonnull)(void))source ``` |

Modified [-[TKSmartCardATR interfaceGroupAtIndex:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403537-interfacegroup)

|  | Declaration |
| --- | --- |
| From | ``` - (TKSmartCardATRInterfaceGroup *)interfaceGroupAtIndex:(NSInteger)index ``` |
| To | ``` - (TKSmartCardATRInterfaceGroup * _Nullable)interfaceGroupAtIndex:(NSInteger)index ``` |

Modified [-[TKSmartCardATR interfaceGroupForProtocol:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403483-interfacegroup)

|  | Declaration |
| --- | --- |
| From | ``` - (TKSmartCardATRInterfaceGroup *)interfaceGroupForProtocol:(TKSmartCardProtocol)protocol ``` |
| To | ``` - (TKSmartCardATRInterfaceGroup * _Nullable)interfaceGroupForProtocol:(TKSmartCardProtocol)protocol ``` |

Modified [TKSmartCardATR.protocols](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403472-protocols)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *protocols ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSNumber *> *protocols ``` |

Modified [TKSmartCardATRInterfaceGroup.protocol](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatrinterfacegroup/1403429-protocol)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *protocol ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *protocol ``` |

Modified [TKSmartCardATRInterfaceGroup.TA](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup/1403499-ta)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *TA ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *TA ``` |

Modified [TKSmartCardATRInterfaceGroup.TB](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatrinterfacegroup/1403452-tb)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *TB ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *TB ``` |

Modified [TKSmartCardATRInterfaceGroup.TC](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup/1403438-tc)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSNumber *TC ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSNumber *TC ``` |

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
