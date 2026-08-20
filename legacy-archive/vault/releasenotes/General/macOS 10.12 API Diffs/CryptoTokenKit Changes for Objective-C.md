---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/CryptoTokenKit.html
archived_at: '2026-07-18T02:50:38.510691Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CryptoTokenKit Changes for Objective-C

### CryptoTokenKit

#### TKError.h

Added [TKErrorCodeAuthenticationNeeded](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodeauthenticationneeded)

#### TKSmartCard.h

Added [-[TKSmartCard inSessionWithError:executeBlock:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1773461-insessionwitherror)Added [-[TKSmartCard sendIns:p1:p2:data:le:sw:error:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1778266-sendins)Added [TKSmartCard.useCommandChaining](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1773460-usecommandchaining)Added TKSmartCardSlotManager.defaultManagerModified [+[TKSmartCardSlotManager defaultManager]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390245-defaultmanager)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)defaultManager ``` |
| To | ``` + (TKSmartCardSlotManager *)defaultManager ``` |

#### TKSmartCardATR.h

Added [TKSmartCardATR.historicalRecords](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1791962-historicalrecords)

#### TKSmartCardToken.h (Added)

Added [TKSmartCardToken](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtoken)Added [TKSmartCardToken.AID](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtoken/1773457-aid)Added [-[TKSmartCardToken initWithSmartCard:AID:instanceID:tokenDriver:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtoken/1778164-initwithsmartcard)Added [TKSmartCardTokenDriver](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokendriver)Added [TKSmartCardTokenDriverDelegate](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokendriverdelegate)Added [-[TKSmartCardTokenDriverDelegate tokenDriver:createTokenForSmartCard:AID:error:]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokendriverdelegate/1773454-tokendriver)Added [TKSmartCardTokenSession](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokensession)Added [TKSmartCardTokenSession.smartCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokensession/1773453-smartcard)Added [TKTokenSmartCardPINAuthOperation](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation)Added [TKTokenSmartCardPINAuthOperation.APDUTemplate](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/1642174-apdutemplate)Added [TKTokenSmartCardPINAuthOperation.PIN](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/1642146-pin)Added [TKTokenSmartCardPINAuthOperation.PINByteOffset](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/1642178-pinbyteoffset)Added [TKTokenSmartCardPINAuthOperation.PINFormat](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/1642153-pinformat)Added [TKTokenSmartCardPINAuthOperation.smartCard](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/1642172-smartcard)

#### TKTLVRecord.h (Added)

Added [TKBERTLVRecord](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord)Added [+[TKBERTLVRecord dataForTag:]](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord/1791996-data)Added [-[TKBERTLVRecord initWithTag:records:]](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord/1791980-initwithtag)Added [-[TKBERTLVRecord initWithTag:value:]](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord/1791959-initwithtag)Added [TKCompactTLVRecord](https://developer.apple.com/documentation/cryptotokenkit/tkcompacttlvrecord)Added [-[TKCompactTLVRecord initWithTag:value:]](https://developer.apple.com/documentation/cryptotokenkit/tkcompacttlvrecord/1791994-init)Added [TKSimpleTLVRecord](https://developer.apple.com/documentation/cryptotokenkit/tksimpletlvrecord)Added [-[TKSimpleTLVRecord initWithTag:value:]](https://developer.apple.com/documentation/cryptotokenkit/tksimpletlvrecord/1791974-init)Added [TKTLVRecord](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord)Added [TKTLVRecord.data](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/1791946-data)Added [+[TKTLVRecord recordFromData:]](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/1773444-init)Added [+[TKTLVRecord sequenceOfRecordsFromData:]](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/1773446-sequenceofrecordsfromdata)Added [TKTLVRecord.tag](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/1791953-tag)Added [TKTLVRecord.value](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/1791968-value)Added [TKTLVTag](https://developer.apple.com/documentation/cryptotokenkit/tktlvtag)

#### TKToken.h (Added)

Added [TKToken](https://developer.apple.com/documentation/cryptotokenkit/tktoken)Added [TKToken.delegate](https://developer.apple.com/documentation/cryptotokenkit/tktoken/1791954-delegate)Added [-[TKToken initWithTokenDriver:instanceID:]](https://developer.apple.com/documentation/cryptotokenkit/tktoken/1791958-init)Added [TKToken.keychainContents](https://developer.apple.com/documentation/cryptotokenkit/tktoken/1773447-keychaincontents)Added [TKToken.tokenDriver](https://developer.apple.com/documentation/cryptotokenkit/tktoken/1773445-tokendriver)Added [TKTokenAuthOperation](https://developer.apple.com/documentation/cryptotokenkit/tktokenauthoperation)Added [-[TKTokenAuthOperation finishWithError:]](https://developer.apple.com/documentation/cryptotokenkit/tktokenauthoperation/1773440-finish)Added [TKTokenDelegate](https://developer.apple.com/documentation/cryptotokenkit/tktokendelegate)Added [-[TKTokenDelegate token:createSessionWithError:]](https://developer.apple.com/documentation/cryptotokenkit/tktokendelegate/1773438-createsession)Added [-[TKTokenDelegate token:terminateSession:]](https://developer.apple.com/documentation/cryptotokenkit/tktokendelegate/1773439-token)Added [TKTokenDriver](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver)Added [TKTokenDriver.delegate](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver/1773437-delegate)Added [TKTokenDriverDelegate](https://developer.apple.com/documentation/cryptotokenkit/tktokendriverdelegate)Added [-[TKTokenDriverDelegate tokenDriver:terminateToken:]](https://developer.apple.com/documentation/cryptotokenkit/tktokendriverdelegate/1773435-tokendriver)Added [TKTokenKeyAlgorithm](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tktokenkeyalgorithm)Added [-[TKTokenKeyAlgorithm isAlgorithm:]](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tktokenkeyalgorithm/1773432-isalgorithm)Added [-[TKTokenKeyAlgorithm supportsAlgorithm:]](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tktokenkeyalgorithm/1773433-supportsalgorithm)Added [TKTokenKeyExchangeParameters](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tktokenkeyexchangeparameters)Added [TKTokenKeyExchangeParameters.requestedSize](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyexchangeparameters/1642158-requestedsize)Added [TKTokenKeyExchangeParameters.sharedInfo](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyexchangeparameters/1642150-sharedinfo)Added [TKTokenPasswordAuthOperation](https://developer.apple.com/documentation/cryptotokenkit/tktokenpasswordauthoperation)Added [TKTokenPasswordAuthOperation.password](https://developer.apple.com/documentation/cryptotokenkit/tktokenpasswordauthoperation/1642168-password)Added [TKTokenSession](https://developer.apple.com/documentation/cryptotokenkit/tktokensession)Added [TKTokenSession.delegate](https://developer.apple.com/documentation/cryptotokenkit/tktokensession/1773413-delegate)Added [-[TKTokenSession initWithToken:]](https://developer.apple.com/documentation/cryptotokenkit/tktokensession/1791976-init)Added [TKTokenSession.token](https://developer.apple.com/documentation/cryptotokenkit/tktokensession/1791949-token)Added [TKTokenSessionDelegate](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate)Added [-[TKTokenSessionDelegate tokenSession:beginAuthForOperation:constraint:error:]](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/1773415-tokensession)Added [-[TKTokenSessionDelegate tokenSession:decryptData:usingKey:algorithm:error:]](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/1773418-tokensession)Added [-[TKTokenSessionDelegate tokenSession:performKeyExchangeWithPublicKey:usingKey:algorithm:parameters:error:]](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/1791995-tokensession)Added [-[TKTokenSessionDelegate tokenSession:signData:usingKey:algorithm:error:]](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/1773417-tokensession)Added [-[TKTokenSessionDelegate tokenSession:supportsOperation:usingKey:algorithm:]](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/1773416-tokensession)Added [TKTokenObjectID](https://developer.apple.com/documentation/cryptotokenkit/tktokenobjectid)Added [TKTokenOperation](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation)Added [TKTokenOperationConstraint](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperationconstraint)Added [TKTokenOperationDecryptData](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation/tktokenoperationdecryptdata)Added [TKTokenOperationNone](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation/tktokenoperationnone)Added [TKTokenOperationPerformKeyExchange](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation/performkeyexchange)Added [TKTokenOperationReadData](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation/tktokenoperationreaddata)Added [TKTokenOperationSignData](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation/signdata)

#### TKTokenKeychainItem.h (Added)

Added [TKTokenKeychainCertificate](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincertificate)Added [TKTokenKeychainCertificate.data](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincertificate/1773426-data)Added [-[TKTokenKeychainCertificate initWithCertificate:objectID:]](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincertificate/1641929-initwithcertificate)Added [TKTokenKeychainContents](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents)Added [-[TKTokenKeychainContents certificateForObjectID:error:]](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/1773431-certificateforobjectid)Added [-[TKTokenKeychainContents fillWithItems:]](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/1773427-fillwithitems)Added [TKTokenKeychainContents.items](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/1773428-items)Added [-[TKTokenKeychainContents keyForObjectID:error:]](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/1773429-keyforobjectid)Added [TKTokenKeychainItem](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem)Added [TKTokenKeychainItem.constraints](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/1773425-constraints)Added [-[TKTokenKeychainItem initWithObjectID:]](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/1773423-init)Added [TKTokenKeychainItem.label](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/1641926-label)Added [TKTokenKeychainItem.objectID](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/1641927-objectid)Added [TKTokenKeychainKey](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey)Added [TKTokenKeychainKey.applicationTag](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641921-applicationtag)Added [TKTokenKeychainKey.canDecrypt](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641923-candecrypt)Added [TKTokenKeychainKey.canPerformKeyExchange](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641924-canperformkeyexchange)Added [TKTokenKeychainKey.canSign](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641925-cansign)Added [-[TKTokenKeychainKey initWithCertificate:objectID:]](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641930-initwithcertificate)Added [TKTokenKeychainKey.keySizeInBits](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641934-keysizeinbits)Added [TKTokenKeychainKey.keyType](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641935-keytype)Added [TKTokenKeychainKey.publicKeyData](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1773421-publickeydata)Added [TKTokenKeychainKey.publicKeyHash](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1791971-publickeyhash)Added [TKTokenKeychainKey.suitableForLogin](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641931-issuitableforlogin)

#### TKTokenWatcher.h (Added)

Added [TKTokenWatcher](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher)Added [-[TKTokenWatcher addRemovalHandler:forTokenID:]](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/1641144-addremovalhandler)Added [-[TKTokenWatcher init]](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/1641147-init)Added [-[TKTokenWatcher initWithInsertionHandler:]](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/1641143-initwithinsertionhandler)Added [TKTokenWatcher.tokenIDs](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/1641142-tokenids)

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
