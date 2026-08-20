---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/CryptoTokenKit.html
archived_at: '2026-07-18T02:51:12.919929Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CryptoTokenKit Changes for Swift

### CryptoTokenKit

Removed [TKErrorCode.TKErrorAuthenticationFailed](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorauthenticationfailed)Removed [TKErrorCode.TKErrorObjectNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/1393807-tkerrorobjectnotfound)Removed [TKErrorCode.TKErrorTokenNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/1393801-tkerrortokennotfound)Removed [TKSmartCard.sendIns(_: UInt8, p1: UInt8, p2: UInt8, data: NSData?, le: NSNumber?, reply: (NSData?, UInt16, NSError?) -> Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390283-sendins)Removed [TKSmartCardPINCompletion.init(rawValue: UInt)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion/1403463-init)Removed [TKSmartCardPINConfirmation.init(rawValue: UInt)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/confirmation/1403541-init)Removed [TKSmartCardPINConfirmation.None](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinconfirmation/tksmartcardpinconfirmationnone)Removed [TKSmartCardProtocol.None](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol/tksmartcardprotocolnone)Removed [TKSmartCardSlotManager.defaultManager() -> Self? [class]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390245-defaultmanager)Added [TKBERTLVRecord](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord)Added [TKBERTLVRecord.data(forTag: TKTLVTag) -> Data [class]](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord/1791996-data)Added [TKBERTLVRecord.init(tag: TKTLVTag, records: [TKTLVRecord])](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord/1791980-init)Added [TKBERTLVRecord.init(tag: TKTLVTag, value: Data)](https://developer.apple.com/documentation/cryptotokenkit/tkbertlvrecord/1791959-initwithtag)Added [TKCompactTLVRecord](https://developer.apple.com/documentation/cryptotokenkit/tkcompacttlvrecord)Added [TKCompactTLVRecord.init(tag: UInt8, value: Data)](https://developer.apple.com/documentation/cryptotokenkit/tkcompacttlvrecord/1791994-init)Added [TKError [struct]](https://developer.apple.com/documentation/cryptotokenkit/tkerror)Added [TKError.authenticationFailed](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432371-authenticationfailed)Added [TKError.authenticationNeeded](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432356-authenticationneeded)Added [TKError.badParameter](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432363-badparameter)Added [TKError.canceledByUser](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432364-canceledbyuser)Added [TKError.communicationError](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432370-communicationerror)Added [TKError.corruptedData](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432367-corrupteddata)Added TKError.init(_nsError: NSError)Added [TKError.notImplemented](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432360-notimplemented)Added [TKError.objectNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432357-objectnotfound)Added [TKError.TKErrorAuthenticationFailed](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432361-tkerrorauthenticationfailed)Added [TKError.TKErrorObjectNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432362-tkerrorobjectnotfound)Added [TKError.TKErrorTokenNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432355-tkerrortokennotfound)Added [TKError.tokenNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/2432368-tokennotfound)Added [TKError.Code.authenticationNeeded](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodeauthenticationneeded)Added [TKError.Code.TKErrorAuthenticationFailed](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/1393805-tkerrorauthenticationfailed)Added [TKError.Code.TKErrorObjectNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorobjectnotfound)Added [TKError.Code.TKErrorTokenNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/1393801-tkerrortokennotfound)Added [TKSimpleTLVRecord](https://developer.apple.com/documentation/cryptotokenkit/tksimpletlvrecord)Added [TKSimpleTLVRecord.init(tag: UInt8, value: Data)](https://developer.apple.com/documentation/cryptotokenkit/tksimpletlvrecord/1791974-init)Added [TKSmartCard.send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?) throws -> (sw: UInt16, response: Data)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/2432365-send)Added [TKSmartCard.send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?, reply: (Data?, UInt16, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/2432358-send)Added [TKSmartCard.useCommandChaining](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1773460-usecommandchaining)Added [TKSmartCard.withSession<T>(_: () throws -> T) throws -> T](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/2432369-withsession)Added [TKSmartCardATR.historicalRecords](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1791962-historicalrecords)Added [TKSmartCardSlotManager.default](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390245-default)Added [TKSmartCardToken](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtoken)Added [TKSmartCardToken.aid](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtoken/1773457-aid)Added [TKSmartCardToken.init(smartCard: TKSmartCard, aid: Data?, instanceID: String, tokenDriver: TKSmartCardTokenDriver)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtoken/1778164-initwithsmartcard)Added [TKSmartCardTokenDriver](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokendriver)Added [TKSmartCardTokenDriverDelegate](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokendriverdelegate)Added [TKSmartCardTokenDriverDelegate.tokenDriver(_: TKSmartCardTokenDriver, createTokenFor: TKSmartCard, aid: Data?) throws -> TKSmartCardToken](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokendriverdelegate/1773454-tokendriver)Added [TKSmartCardTokenSession](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokensession)Added [TKSmartCardTokenSession.smartCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardtokensession/1773453-smartcard)Added [TKSmartCardUserInteractionForPINOperation.Completion.init(rawValue: UInt)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion/1403463-init)Added [TKSmartCardUserInteractionForSecurePINChange.Confirmation.init(rawValue: UInt)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/confirmation/1403541-init)Added [TKTLVRecord](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord)Added [TKTLVRecord.data](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/1791946-data)Added [TKTLVRecord.init(from: Data)](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/1773444-recordfromdata)Added [TKTLVRecord.sequenceOfRecords(from: Data) -> [TKTLVRecord]? [class]](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/1773446-sequenceofrecordsfromdata)Added [TKTLVRecord.tag](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/1791953-tag)Added [TKTLVRecord.value](https://developer.apple.com/documentation/cryptotokenkit/tktlvrecord/1791968-value)Added [TKToken](https://developer.apple.com/documentation/cryptotokenkit/tktoken)Added [TKToken.delegate](https://developer.apple.com/documentation/cryptotokenkit/tktoken/1791954-delegate)Added [TKToken.init(tokenDriver: TKTokenDriver, instanceID: String)](https://developer.apple.com/documentation/cryptotokenkit/tktoken/1791958-init)Added [TKToken.keychainContents](https://developer.apple.com/documentation/cryptotokenkit/tktoken/1773447-keychaincontents)Added [TKToken.tokenDriver](https://developer.apple.com/documentation/cryptotokenkit/tktoken/1773445-tokendriver)Added [TKTokenAuthOperation](https://developer.apple.com/documentation/cryptotokenkit/tktokenauthoperation)Added [TKTokenAuthOperation.finish() throws](https://developer.apple.com/documentation/cryptotokenkit/tktokenauthoperation/1773440-finishwitherror)Added [TKTokenDelegate](https://developer.apple.com/documentation/cryptotokenkit/tktokendelegate)Added [TKTokenDelegate.createSession(_: TKToken) throws -> TKTokenSession](https://developer.apple.com/documentation/cryptotokenkit/tktokendelegate/1773438-token)Added [TKTokenDelegate.token(_: TKToken, terminateSession: TKTokenSession)](https://developer.apple.com/documentation/cryptotokenkit/tktokendelegate/1773439-token)Added [TKTokenDriver](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver)Added [TKTokenDriver.delegate](https://developer.apple.com/documentation/cryptotokenkit/tktokendriver/1773437-delegate)Added [TKTokenDriverDelegate](https://developer.apple.com/documentation/cryptotokenkit/tktokendriverdelegate)Added [TKTokenDriverDelegate.tokenDriver(_: TKTokenDriver, terminateToken: TKToken)](https://developer.apple.com/documentation/cryptotokenkit/tktokendriverdelegate/1773435-tokendriver)Added [TKTokenKeyAlgorithm](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyalgorithm)Added [TKTokenKeyAlgorithm.isAlgorithm(_: SecKeyAlgorithm) -> Bool](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tktokenkeyalgorithm/1773432-isalgorithm)Added [TKTokenKeyAlgorithm.supportsAlgorithm(_: SecKeyAlgorithm) -> Bool](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyalgorithm/1773433-supportsalgorithm)Added [TKTokenKeychainCertificate](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincertificate)Added [TKTokenKeychainCertificate.data](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincertificate/1773426-data)Added [TKTokenKeychainCertificate.init(certificate: SecCertificate, objectID: Any)](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincertificate/1641929-initwithcertificate)Added [TKTokenKeychainContents](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents)Added [TKTokenKeychainContents.certificate(forObjectID: Any) throws -> TKTokenKeychainCertificate](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/1773431-certificate)Added [TKTokenKeychainContents.fill(with: [TKTokenKeychainItem])](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/1773427-fill)Added [TKTokenKeychainContents.items](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/1773428-items)Added [TKTokenKeychainContents.key(forObjectID: Any) throws -> TKTokenKeychainKey](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincontents/1773429-keyforobjectid)Added [TKTokenKeychainItem](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem)Added [TKTokenKeychainItem.constraints](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/1773425-constraints)Added [TKTokenKeychainItem.init(objectID: Any)](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/1773423-initwithobjectid)Added [TKTokenKeychainItem.label](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/1641926-label)Added [TKTokenKeychainItem.objectID](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainitem/1641927-objectid)Added [TKTokenKeychainKey](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey)Added [TKTokenKeychainKey.applicationTag](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641921-applicationtag)Added [TKTokenKeychainKey.canDecrypt](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641923-candecrypt)Added [TKTokenKeychainKey.canPerformKeyExchange](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641924-canperformkeyexchange)Added [TKTokenKeychainKey.canSign](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641925-cansign)Added [TKTokenKeychainKey.init(certificate: SecCertificate?, objectID: Any)](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641930-init)Added [TKTokenKeychainKey.isSuitableForLogin](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641931-issuitableforlogin)Added [TKTokenKeychainKey.keySizeInBits](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641934-keysizeinbits)Added [TKTokenKeychainKey.keyType](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1641935-keytype)Added [TKTokenKeychainKey.publicKeyData](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1773421-publickeydata)Added [TKTokenKeychainKey.publicKeyHash](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychainkey/1791971-publickeyhash)Added [TKTokenKeyExchangeParameters](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tktokenkeyexchangeparameters)Added [TKTokenKeyExchangeParameters.requestedSize](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeyexchangeparameters/1642158-requestedsize)Added [TKTokenKeyExchangeParameters.sharedInfo](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tktokenkeyexchangeparameters/1642150-sharedinfo)Added [TKTokenOperation [enum]](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation)Added [TKTokenOperation.decryptData](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation/tktokenoperationdecryptdata)Added [TKTokenOperation.none](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation/none)Added [TKTokenOperation.performKeyExchange](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation/tktokenoperationperformkeyexchange)Added [TKTokenOperation.readData](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation/readdata)Added [TKTokenOperation.signData](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperation/signdata)Added [TKTokenPasswordAuthOperation](https://developer.apple.com/documentation/cryptotokenkit/tktokenpasswordauthoperation)Added [TKTokenPasswordAuthOperation.password](https://developer.apple.com/documentation/cryptotokenkit/tktokenpasswordauthoperation/1642168-password)Added [TKTokenSession](https://developer.apple.com/documentation/cryptotokenkit/tktokensession)Added [TKTokenSession.delegate](https://developer.apple.com/documentation/cryptotokenkit/tktokensession/1773413-delegate)Added [TKTokenSession.init(token: TKToken)](https://developer.apple.com/documentation/cryptotokenkit/tktokensession/1791976-init)Added [TKTokenSession.token](https://developer.apple.com/documentation/cryptotokenkit/tktokensession/1791949-token)Added [TKTokenSessionDelegate](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate)Added [TKTokenSessionDelegate.tokenSession(_: TKTokenSession, beginAuthFor: TKTokenOperation, constraint: Any) throws -> TKTokenAuthOperation](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/1773415-tokensession)Added [TKTokenSessionDelegate.tokenSession(_: TKTokenSession, decrypt: Data, keyObjectID: Any, algorithm: TKTokenKeyAlgorithm) throws -> Data](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/1773418-tokensession)Added [TKTokenSessionDelegate.tokenSession(_: TKTokenSession, performKeyExchange: Data, keyObjectID: Any, algorithm: TKTokenKeyAlgorithm, parameters: TKTokenKeyExchangeParameters) throws -> Data](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/1791995-tokensession)Added [TKTokenSessionDelegate.tokenSession(_: TKTokenSession, sign: Data, keyObjectID: Any, algorithm: TKTokenKeyAlgorithm) throws -> Data](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/1773417-tokensession)Added [TKTokenSessionDelegate.tokenSession(_: TKTokenSession, supports: TKTokenOperation, keyObjectID: Any, algorithm: TKTokenKeyAlgorithm) -> Bool](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/1773416-tokensession)Added [TKTokenSmartCardPINAuthOperation](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation)Added [TKTokenSmartCardPINAuthOperation.apduTemplate](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/1642174-apdutemplate)Added [TKTokenSmartCardPINAuthOperation.pin](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/1642146-pin)Added [TKTokenSmartCardPINAuthOperation.pinByteOffset](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/1642178-pinbyteoffset)Added [TKTokenSmartCardPINAuthOperation.pinFormat](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/1642153-pinformat)Added [TKTokenSmartCardPINAuthOperation.smartCard](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/1642172-smartcard)Added [TKTokenWatcher](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher)Added [TKTokenWatcher.addRemovalHandler(_: (String) -> Swift.Void, forTokenID: String)](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/1641144-addremovalhandler)Added [TKTokenWatcher.init()](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/1641147-init)Added [TKTokenWatcher.init(insertionHandler: (String) -> Swift.Void)](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/1641143-initwithinsertionhandler)Added [TKTokenWatcher.tokenIDs](https://developer.apple.com/documentation/cryptotokenkit/tktokenwatcher/1641142-tokenids)Added [TKTLVTag](https://developer.apple.com/documentation/cryptotokenkit/tktlvtag)Added [TKTokenObjectID](https://developer.apple.com/documentation/cryptotokenkit/tktokenobjectid)Added [TKTokenOperationConstraint](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperationconstraint)Modified [TKError.Code [enum]](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum TKErrorCode : Int {     case NotImplemented     case CommunicationError     case CorruptedData     case CanceledByUser     case AuthenticationFailed     case ObjectNotFound     case TokenNotFound     case BadParameter     static var TKErrorAuthenticationFailed: TKErrorCode { get }     static var TKErrorObjectNotFound: TKErrorCode { get }     static var TKErrorTokenNotFound: TKErrorCode { get } } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = TKError         case notImplemented         case communicationError         case corruptedData         case canceledByUser         case authenticationFailed         case objectNotFound         case tokenNotFound         case badParameter         case authenticationNeeded         static var TKErrorAuthenticationFailed: TKError.Code { get }         static var TKErrorObjectNotFound: TKError.Code { get }         static var TKErrorTokenNotFound: TKError.Code { get }     } ``` |

Modified [TKError.Code.authenticationFailed](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/authenticationfailed)

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticationFailed ``` |
| To | ``` case authenticationFailed ``` |

Modified [TKError.Code.badParameter](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodebadparameter)

|  | Declaration |
| --- | --- |
| From | ``` case BadParameter ``` |
| To | ``` case badParameter ``` |

Modified [TKError.Code.canceledByUser](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/canceledbyuser)

|  | Declaration |
| --- | --- |
| From | ``` case CanceledByUser ``` |
| To | ``` case canceledByUser ``` |

Modified [TKError.Code.communicationError](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodecommunicationerror)

|  | Declaration |
| --- | --- |
| From | ``` case CommunicationError ``` |
| To | ``` case communicationError ``` |

Modified [TKError.Code.corruptedData](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodecorrupteddata)

|  | Declaration |
| --- | --- |
| From | ``` case CorruptedData ``` |
| To | ``` case corruptedData ``` |

Modified [TKError.Code.notImplemented](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/notimplemented)

|  | Declaration |
| --- | --- |
| From | ``` case NotImplemented ``` |
| To | ``` case notImplemented ``` |

Modified [TKError.Code.objectNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/objectnotfound)

|  | Declaration |
| --- | --- |
| From | ``` case ObjectNotFound ``` |
| To | ``` case objectNotFound ``` |

Modified [TKError.Code.tokenNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodetokennotfound)

|  | Declaration |
| --- | --- |
| From | ``` case TokenNotFound ``` |
| To | ``` case tokenNotFound ``` |

Modified [TKSmartCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TKSmartCard : NSObject {     var slot: TKSmartCardSlot { get }     var valid: Bool { get }     var allowedProtocols: TKSmartCardProtocol     var currentProtocol: TKSmartCardProtocol { get }     var sensitive: Bool     var context: AnyObject?     func beginSessionWithReply(_ reply: (Bool, NSError?) -> Void)     func transmitRequest(_ request: NSData, reply reply: (NSData?, NSError?) -> Void)     func endSession()     func userInteractionForSecurePINVerificationWithPINFormat(_ PINFormat: TKSmartCardPINFormat, APDU APDU: NSData, PINByteOffset PINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification?     func userInteractionForSecurePINChangeWithPINFormat(_ PINFormat: TKSmartCardPINFormat, APDU APDU: NSData, currentPINByteOffset currentPINByteOffset: Int, newPINByteOffset newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange? } extension TKSmartCard {     var cla: UInt8     var useExtendedLength: Bool     func sendIns(_ ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data requestData: NSData?, le le: NSNumber?, reply reply: (NSData?, UInt16, NSError?) -> Void) } ``` | -- |
| To | ``` class TKSmartCard : NSObject {     var slot: TKSmartCardSlot { get }     var isValid: Bool { get }     var allowedProtocols: TKSmartCardProtocol     var currentProtocol: TKSmartCardProtocol { get }     var isSensitive: Bool     var context: Any?     func beginSession(reply reply: @escaping (Bool, Error?) -> Swift.Void)     func transmit(_ request: Data, reply reply: @escaping (Data?, Error?) -> Swift.Void)     func endSession()     func userInteractionForSecurePINVerification(_ PINFormat: TKSmartCardPINFormat, apdu APDU: Data, pinByteOffset PINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification?     func userInteractionForSecurePINChange(_ PINFormat: TKSmartCardPINFormat, apdu APDU: Data, currentPINByteOffset currentPINByteOffset: Int, newPINByteOffset newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange?     func send(ins ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data data: Data? = default, le le: Int? = default, reply reply: @escaping (Data?, UInt16, Error?) -> Swift.Void)     func send(ins ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data data: Data? = default, le le: Int? = default) throws -> (sw: UInt16, response: Data)     func withSession<T>(_ body: @escaping () throws -> T) throws -> T     var cla: UInt8     var useExtendedLength: Bool     var useCommandChaining: Bool     func __sendIns(_ ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data requestData: Data?, le le: NSNumber?, reply reply: @escaping (Data?, UInt16, Error?) -> Swift.Void)     func __inSession(executeBlock block: @escaping (NSErrorPointer) -> Bool) throws     func __sendIns(_ ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data requestData: Data?, le le: NSNumber?, sw sw: UnsafeMutablePointer<UInt16>) throws -> Data     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension TKSmartCard : CVarArg { } extension TKSmartCard : Equatable, Hashable {     var hashValue: Int { get } } extension TKSmartCard {     var cla: UInt8     var useExtendedLength: Bool     var useCommandChaining: Bool     func __sendIns(_ ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data requestData: Data?, le le: NSNumber?, reply reply: @escaping (Data?, UInt16, Error?) -> Swift.Void)     func __inSession(executeBlock block: @escaping (NSErrorPointer) -> Bool) throws     func __sendIns(_ ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data requestData: Data?, le le: NSNumber?, sw sw: UnsafeMutablePointer<UInt16>) throws -> Data } extension TKSmartCard {     func send(ins ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data data: Data? = default, le le: Int? = default, reply reply: @escaping (Data?, UInt16, Error?) -> Swift.Void)     func send(ins ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data data: Data? = default, le le: Int? = default) throws -> (sw: UInt16, response: Data)     func withSession<T>(_ body: @escaping () throws -> T) throws -> T } ``` | CVarArg, Equatable, Hashable |

Modified [TKSmartCard.beginSession(reply: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390168-beginsessionwithreply)

|  | Declaration |
| --- | --- |
| From | ``` func beginSessionWithReply(_ reply: (Bool, NSError?) -> Void) ``` |
| To | ``` func beginSession(reply reply: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [TKSmartCard.context](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390243-context)

|  | Declaration |
| --- | --- |
| From | ``` var context: AnyObject? ``` |
| To | ``` var context: Any? ``` |

Modified [TKSmartCard.isSensitive](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390216-sensitive)

|  | Declaration |
| --- | --- |
| From | ``` var sensitive: Bool ``` |
| To | ``` var isSensitive: Bool ``` |

Modified [TKSmartCard.isValid](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390194-valid)

|  | Declaration |
| --- | --- |
| From | ``` var valid: Bool { get } ``` |
| To | ``` var isValid: Bool { get } ``` |

Modified [TKSmartCard.transmit(_: Data, reply: (Data?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390161-transmit)

|  | Declaration |
| --- | --- |
| From | ``` func transmitRequest(_ request: NSData, reply reply: (NSData?, NSError?) -> Void) ``` |
| To | ``` func transmit(_ request: Data, reply reply: @escaping (Data?, Error?) -> Swift.Void) ``` |

Modified [TKSmartCard.userInteractionForSecurePINChange(_: TKSmartCardPINFormat, apdu: Data, currentPINByteOffset: Int, newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange?](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390312-userinteractionforsecurepinchang)

|  | Declaration |
| --- | --- |
| From | ``` func userInteractionForSecurePINChangeWithPINFormat(_ PINFormat: TKSmartCardPINFormat, APDU APDU: NSData, currentPINByteOffset currentPINByteOffset: Int, newPINByteOffset newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange? ``` |
| To | ``` func userInteractionForSecurePINChange(_ PINFormat: TKSmartCardPINFormat, apdu APDU: Data, currentPINByteOffset currentPINByteOffset: Int, newPINByteOffset newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange? ``` |

Modified [TKSmartCard.userInteractionForSecurePINVerification(_: TKSmartCardPINFormat, apdu: Data, pinByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification?](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390289-userinteractionforsecurepinverif)

|  | Declaration |
| --- | --- |
| From | ``` func userInteractionForSecurePINVerificationWithPINFormat(_ PINFormat: TKSmartCardPINFormat, APDU APDU: NSData, PINByteOffset PINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification? ``` |
| To | ``` func userInteractionForSecurePINVerification(_ PINFormat: TKSmartCardPINFormat, apdu APDU: Data, pinByteOffset PINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification? ``` |

Modified [TKSmartCardATR](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TKSmartCardATR : NSObject {     init?(bytes bytes: NSData)     init?(source source: () -> Int32)     var bytes: NSData { get }     var protocols: [NSNumber] { get }     func interfaceGroupAtIndex(_ index: Int) -> TKSmartCardATRInterfaceGroup?     func interfaceGroupForProtocol(_ protocol: TKSmartCardProtocol) -> TKSmartCardATRInterfaceGroup?     var historicalBytes: NSData { get } } ``` | -- |
| To | ``` class TKSmartCardATR : NSObject {     init?(bytes bytes: Data)     init?(source source: @escaping () -> Int32)     var bytes: Data { get }     var protocols: [NSNumber] { get }     func interfaceGroup(at index: Int) -> TKSmartCardATR.InterfaceGroup?     func interfaceGroup(for protocol: TKSmartCardProtocol) -> TKSmartCardATR.InterfaceGroup?     var historicalBytes: Data { get }     var historicalRecords: [TKCompactTLVRecord]? { get }     class InterfaceGroup : NSObject {         var ta: NSNumber? { get }         var tb: NSNumber? { get }         var tc: NSNumber? { get }         var `protocol`: NSNumber? { get }     }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension TKSmartCardATR {     class InterfaceGroup : NSObject {         var ta: NSNumber? { get }         var tb: NSNumber? { get }         var tc: NSNumber? { get }         var `protocol`: NSNumber? { get }     } } extension TKSmartCardATR : CVarArg { } extension TKSmartCardATR : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [TKSmartCardATR.bytes](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403518-bytes)

|  | Declaration |
| --- | --- |
| From | ``` var bytes: NSData { get } ``` |
| To | ``` var bytes: Data { get } ``` |

Modified [TKSmartCardATR.historicalBytes](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403513-historicalbytes)

|  | Declaration |
| --- | --- |
| From | ``` var historicalBytes: NSData { get } ``` |
| To | ``` var historicalBytes: Data { get } ``` |

Modified [TKSmartCardATR.init(bytes: Data)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403560-init)

|  | Declaration |
| --- | --- |
| From | ``` init?(bytes bytes: NSData) ``` |
| To | ``` init?(bytes bytes: Data) ``` |

Modified [TKSmartCardATR.init(source: () -> Int32)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403516-initwithsource)

|  | Declaration |
| --- | --- |
| From | ``` init?(source source: () -> Int32) ``` |
| To | ``` init?(source source: @escaping () -> Int32) ``` |

Modified [TKSmartCardATR.interfaceGroup(at: Int) -> TKSmartCardATR.InterfaceGroup?](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403537-interfacegroup)

|  | Declaration |
| --- | --- |
| From | ``` func interfaceGroupAtIndex(_ index: Int) -> TKSmartCardATRInterfaceGroup? ``` |
| To | ``` func interfaceGroup(at index: Int) -> TKSmartCardATR.InterfaceGroup? ``` |

Modified [TKSmartCardATR.interfaceGroup(for: TKSmartCardProtocol) -> TKSmartCardATR.InterfaceGroup?](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403483-interfacegroup)

|  | Declaration |
| --- | --- |
| From | ``` func interfaceGroupForProtocol(_ protocol: TKSmartCardProtocol) -> TKSmartCardATRInterfaceGroup? ``` |
| To | ``` func interfaceGroup(for protocol: TKSmartCardProtocol) -> TKSmartCardATR.InterfaceGroup? ``` |

Modified [TKSmartCardATR.InterfaceGroup](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatrinterfacegroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TKSmartCardATRInterfaceGroup : NSObject {     var TA: NSNumber? { get }     var TB: NSNumber? { get }     var TC: NSNumber? { get }     var `protocol`: NSNumber? { get } } ``` | -- |
| To | ``` class InterfaceGroup : NSObject {         var ta: NSNumber? { get }         var tb: NSNumber? { get }         var tc: NSNumber? { get }         var `protocol`: NSNumber? { get }     } extension TKSmartCardATR.InterfaceGroup {     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension TKSmartCardATR.InterfaceGroup : CVarArg { } extension TKSmartCardATR.InterfaceGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [TKSmartCardATR.InterfaceGroup.ta](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatrinterfacegroup/1403499-ta)

|  | Declaration |
| --- | --- |
| From | ``` var TA: NSNumber? { get } ``` |
| To | ``` var ta: NSNumber? { get } ``` |

Modified [TKSmartCardATR.InterfaceGroup.tb](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup/1403452-tb)

|  | Declaration |
| --- | --- |
| From | ``` var TB: NSNumber? { get } ``` |
| To | ``` var tb: NSNumber? { get } ``` |

Modified [TKSmartCardATR.InterfaceGroup.tc](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup/1403438-tc)

|  | Declaration |
| --- | --- |
| From | ``` var TC: NSNumber? { get } ``` |
| To | ``` var tc: NSNumber? { get } ``` |

Modified [TKSmartCardPINFormat](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TKSmartCardPINFormat : NSObject {     var charset: TKSmartCardPINCharset     var encoding: TKSmartCardPINEncoding     var minPINLength: Int     var maxPINLength: Int     var PINBlockByteLength: Int     var PINJustification: TKSmartCardPINJustification     var PINBitOffset: Int     var PINLengthBitOffset: Int     var PINLengthBitSize: Int } ``` | -- |
| To | ``` class TKSmartCardPINFormat : NSObject {     var charset: TKSmartCardPINFormat.Charset     var encoding: TKSmartCardPINFormat.Encoding     var minPINLength: Int     var maxPINLength: Int     var pinBlockByteLength: Int     var pinJustification: TKSmartCardPINFormat.Justification     var pinBitOffset: Int     var pinLengthBitOffset: Int     var pinLengthBitSize: Int     enum Charset : Int {         case numeric         case alphanumeric         case upperAlphanumeric     }     enum Encoding : Int {         case binary         case ascii         case bcd     }     enum Justification : Int {         case left         case right     }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension TKSmartCardPINFormat {     enum Charset : Int {         case numeric         case alphanumeric         case upperAlphanumeric     }     enum Encoding : Int {         case binary         case ascii         case bcd     }     enum Justification : Int {         case left         case right     } } extension TKSmartCardPINFormat : CVarArg { } extension TKSmartCardPINFormat : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [TKSmartCardPINFormat.charset](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390176-charset)

|  | Declaration |
| --- | --- |
| From | ``` var charset: TKSmartCardPINCharset ``` |
| To | ``` var charset: TKSmartCardPINFormat.Charset ``` |

Modified [TKSmartCardPINFormat.encoding](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390241-encoding)

|  | Declaration |
| --- | --- |
| From | ``` var encoding: TKSmartCardPINEncoding ``` |
| To | ``` var encoding: TKSmartCardPINFormat.Encoding ``` |

Modified [TKSmartCardPINFormat.pinBitOffset](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390269-pinbitoffset)

|  | Declaration |
| --- | --- |
| From | ``` var PINBitOffset: Int ``` |
| To | ``` var pinBitOffset: Int ``` |

Modified [TKSmartCardPINFormat.pinBlockByteLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390198-pinblockbytelength)

|  | Declaration |
| --- | --- |
| From | ``` var PINBlockByteLength: Int ``` |
| To | ``` var pinBlockByteLength: Int ``` |

Modified [TKSmartCardPINFormat.pinJustification](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390190-pinjustification)

|  | Declaration |
| --- | --- |
| From | ``` var PINJustification: TKSmartCardPINJustification ``` |
| To | ``` var pinJustification: TKSmartCardPINFormat.Justification ``` |

Modified [TKSmartCardPINFormat.pinLengthBitOffset](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390291-pinlengthbitoffset)

|  | Declaration |
| --- | --- |
| From | ``` var PINLengthBitOffset: Int ``` |
| To | ``` var pinLengthBitOffset: Int ``` |

Modified [TKSmartCardPINFormat.pinLengthBitSize](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390314-pinlengthbitsize)

|  | Declaration |
| --- | --- |
| From | ``` var PINLengthBitSize: Int ``` |
| To | ``` var pinLengthBitSize: Int ``` |

Modified [TKSmartCardPINFormat.Charset [enum]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/charset)

|  | Declaration |
| --- | --- |
| From | ``` enum TKSmartCardPINCharset : Int {     case Numeric     case Alphanumeric     case UpperAlphanumeric } ``` |
| To | ``` enum Charset : Int {         case numeric         case alphanumeric         case upperAlphanumeric     } ``` |

Modified [TKSmartCardPINFormat.Charset.alphanumeric](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/charset/alphanumeric)

|  | Declaration |
| --- | --- |
| From | ``` case Alphanumeric ``` |
| To | ``` case alphanumeric ``` |

Modified [TKSmartCardPINFormat.Charset.numeric](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/charset/numeric)

|  | Declaration |
| --- | --- |
| From | ``` case Numeric ``` |
| To | ``` case numeric ``` |

Modified [TKSmartCardPINFormat.Charset.upperAlphanumeric](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpincharset/tksmartcardpincharsetupperalphanumeric)

|  | Declaration |
| --- | --- |
| From | ``` case UpperAlphanumeric ``` |
| To | ``` case upperAlphanumeric ``` |

Modified [TKSmartCardPINFormat.Encoding [enum]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/encoding)

|  | Declaration |
| --- | --- |
| From | ``` enum TKSmartCardPINEncoding : Int {     case Binary     case ASCII     case BCD } ``` |
| To | ``` enum Encoding : Int {         case binary         case ascii         case bcd     } ``` |

Modified [TKSmartCardPINFormat.Encoding.ascii](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinencoding/tksmartcardpinencodingascii)

|  | Name | Declaration |
| --- | --- | --- |
| From | ASCII | ``` case ASCII ``` |
| To | ascii | ``` case ascii ``` |

Modified [TKSmartCardPINFormat.Encoding.bcd](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinencoding/tksmartcardpinencodingbcd)

|  | Name | Declaration |
| --- | --- | --- |
| From | BCD | ``` case BCD ``` |
| To | bcd | ``` case bcd ``` |

Modified [TKSmartCardPINFormat.Encoding.binary](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/encoding/binary)

|  | Declaration |
| --- | --- |
| From | ``` case Binary ``` |
| To | ``` case binary ``` |

Modified [TKSmartCardPINFormat.Justification [enum]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/justification)

|  | Declaration |
| --- | --- |
| From | ``` enum TKSmartCardPINJustification : Int {     case Left     case Right } ``` |
| To | ``` enum Justification : Int {         case left         case right     } ``` |

Modified [TKSmartCardPINFormat.Justification.left](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinjustification/tksmartcardpinjustificationleft)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [TKSmartCardPINFormat.Justification.right](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/justification/right)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [TKSmartCardProtocol [struct]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct TKSmartCardProtocol : OptionSetType {     init(rawValue rawValue: UInt)     static var None: TKSmartCardProtocol { get }     static var T0: TKSmartCardProtocol { get }     static var T1: TKSmartCardProtocol { get }     static var T15: TKSmartCardProtocol { get }     static var Any: TKSmartCardProtocol { get } } ``` | OptionSetType |
| To | ``` struct TKSmartCardProtocol : OptionSet {     init(rawValue rawValue: UInt)     static var none: TKSmartCardProtocol { get }     static var t0: TKSmartCardProtocol { get }     static var t1: TKSmartCardProtocol { get }     static var t15: TKSmartCardProtocol { get }     static var any: TKSmartCardProtocol { get }     func intersect(_ other: TKSmartCardProtocol) -> TKSmartCardProtocol     func exclusiveOr(_ other: TKSmartCardProtocol) -> TKSmartCardProtocol     mutating func unionInPlace(_ other: TKSmartCardProtocol)     mutating func intersectInPlace(_ other: TKSmartCardProtocol)     mutating func exclusiveOrInPlace(_ other: TKSmartCardProtocol)     func isSubsetOf(_ other: TKSmartCardProtocol) -> Bool     func isDisjointWith(_ other: TKSmartCardProtocol) -> Bool     func isSupersetOf(_ other: TKSmartCardProtocol) -> Bool     mutating func subtractInPlace(_ other: TKSmartCardProtocol)     func isStrictSupersetOf(_ other: TKSmartCardProtocol) -> Bool     func isStrictSubsetOf(_ other: TKSmartCardProtocol) -> Bool } extension TKSmartCardProtocol {     func union(_ other: TKSmartCardProtocol) -> TKSmartCardProtocol     func intersection(_ other: TKSmartCardProtocol) -> TKSmartCardProtocol     func symmetricDifference(_ other: TKSmartCardProtocol) -> TKSmartCardProtocol } extension TKSmartCardProtocol {     func contains(_ member: TKSmartCardProtocol) -> Bool     mutating func insert(_ newMember: TKSmartCardProtocol) -> (inserted: Bool, memberAfterInsert: TKSmartCardProtocol)     mutating func remove(_ member: TKSmartCardProtocol) -> TKSmartCardProtocol?     mutating func update(with newMember: TKSmartCardProtocol) -> TKSmartCardProtocol? } extension TKSmartCardProtocol {     convenience init()     mutating func formUnion(_ other: TKSmartCardProtocol)     mutating func formIntersection(_ other: TKSmartCardProtocol)     mutating func formSymmetricDifference(_ other: TKSmartCardProtocol) } extension TKSmartCardProtocol {     convenience init<S : Sequence where S.Iterator.Element == TKSmartCardProtocol>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: TKSmartCardProtocol...)     mutating func subtract(_ other: TKSmartCardProtocol)     func isSubset(of other: TKSmartCardProtocol) -> Bool     func isSuperset(of other: TKSmartCardProtocol) -> Bool     func isDisjoint(with other: TKSmartCardProtocol) -> Bool     func subtracting(_ other: TKSmartCardProtocol) -> TKSmartCardProtocol     var isEmpty: Bool { get }     func isStrictSuperset(of other: TKSmartCardProtocol) -> Bool     func isStrictSubset(of other: TKSmartCardProtocol) -> Bool } ``` | OptionSet |

Modified [TKSmartCardProtocol.any](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol/1403523-any)

|  | Declaration |
| --- | --- |
| From | ``` static var Any: TKSmartCardProtocol { get } ``` |
| To | ``` static var any: TKSmartCardProtocol { get } ``` |

Modified [TKSmartCardProtocol.t0](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol/1403431-t0)

|  | Declaration |
| --- | --- |
| From | ``` static var T0: TKSmartCardProtocol { get } ``` |
| To | ``` static var t0: TKSmartCardProtocol { get } ``` |

Modified [TKSmartCardProtocol.t1](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol/1403553-t1)

|  | Declaration |
| --- | --- |
| From | ``` static var T1: TKSmartCardProtocol { get } ``` |
| To | ``` static var t1: TKSmartCardProtocol { get } ``` |

Modified [TKSmartCardProtocol.t15](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol/tksmartcardprotocolt15)

|  | Declaration |
| --- | --- |
| From | ``` static var T15: TKSmartCardProtocol { get } ``` |
| To | ``` static var t15: TKSmartCardProtocol { get } ``` |

Modified [TKSmartCardSlot](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TKSmartCardSlot : NSObject {     var state: TKSmartCardSlotState { get }     var ATR: TKSmartCardATR? { get }     var name: String { get }     var maxInputLength: Int { get }     var maxOutputLength: Int { get }     func makeSmartCard() -> TKSmartCard? } ``` | -- |
| To | ``` class TKSmartCardSlot : NSObject {     var state: TKSmartCardSlot.State { get }     var atr: TKSmartCardATR? { get }     var name: String { get }     var maxInputLength: Int { get }     var maxOutputLength: Int { get }     func makeSmartCard() -> TKSmartCard?     enum State : Int {         case missing         case empty         case probing         case muteCard         case validCard     }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension TKSmartCardSlot {     enum State : Int {         case missing         case empty         case probing         case muteCard         case validCard     } } extension TKSmartCardSlot : CVarArg { } extension TKSmartCardSlot : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [TKSmartCardSlot.atr](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390285-atr)

|  | Declaration |
| --- | --- |
| From | ``` var ATR: TKSmartCardATR? { get } ``` |
| To | ``` var atr: TKSmartCardATR? { get } ``` |

Modified [TKSmartCardSlot.state](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390293-state)

|  | Declaration |
| --- | --- |
| From | ``` var state: TKSmartCardSlotState { get } ``` |
| To | ``` var state: TKSmartCardSlot.State { get } ``` |

Modified [TKSmartCardSlot.State [enum]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state)

|  | Declaration |
| --- | --- |
| From | ``` enum TKSmartCardSlotState : Int {     case Missing     case Empty     case Probing     case MuteCard     case ValidCard } ``` |
| To | ``` enum State : Int {         case missing         case empty         case probing         case muteCard         case validCard     } ``` |

Modified [TKSmartCardSlot.State.empty](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotstate/tksmartcardslotstateempty)

|  | Declaration |
| --- | --- |
| From | ``` case Empty ``` |
| To | ``` case empty ``` |

Modified [TKSmartCardSlot.State.missing](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state/missing)

|  | Declaration |
| --- | --- |
| From | ``` case Missing ``` |
| To | ``` case missing ``` |

Modified [TKSmartCardSlot.State.muteCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotstate/tksmartcardslotstatemutecard)

|  | Declaration |
| --- | --- |
| From | ``` case MuteCard ``` |
| To | ``` case muteCard ``` |

Modified [TKSmartCardSlot.State.probing](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotstate/tksmartcardslotstateprobing)

|  | Declaration |
| --- | --- |
| From | ``` case Probing ``` |
| To | ``` case probing ``` |

Modified [TKSmartCardSlot.State.validCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotstate/tksmartcardslotstatevalidcard)

|  | Declaration |
| --- | --- |
| From | ``` case ValidCard ``` |
| To | ``` case validCard ``` |

Modified [TKSmartCardSlotManager](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TKSmartCardSlotManager : NSObject {     class func defaultManager() -> Self?     var slotNames: [String] { get }     func getSlotWithName(_ name: String, reply reply: (TKSmartCardSlot?) -> Void) } ``` | -- |
| To | ``` class TKSmartCardSlotManager : NSObject {     class var `default`: TKSmartCardSlotManager? { get }     var slotNames: [String] { get }     func getSlot(withName name: String, reply reply: @escaping (TKSmartCardSlot?) -> Swift.Void)     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension TKSmartCardSlotManager : CVarArg { } extension TKSmartCardSlotManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [TKSmartCardSlotManager.getSlot(withName: String, reply: (TKSmartCardSlot?) -> Swift.Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390265-getslot)

|  | Declaration |
| --- | --- |
| From | ``` func getSlotWithName(_ name: String, reply reply: (TKSmartCardSlot?) -> Void) ``` |
| To | ``` func getSlot(withName name: String, reply reply: @escaping (TKSmartCardSlot?) -> Swift.Void) ``` |

Modified [TKSmartCardUserInteraction](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class TKSmartCardUserInteraction : NSObject {     weak var delegate: TKSmartCardUserInteractionDelegate?     var initialTimeout: NSTimeInterval     var interactionTimeout: NSTimeInterval     func runWithReply(_ reply: (Bool, NSError?) -> Void)     func cancel() -> Bool } ``` | -- |
| To | ``` class TKSmartCardUserInteraction : NSObject {     weak var delegate: TKSmartCardUserInteractionDelegate?     var initialTimeout: TimeInterval     var interactionTimeout: TimeInterval     func run(reply reply: @escaping (Bool, Error?) -> Swift.Void)     func cancel() -> Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension TKSmartCardUserInteraction : CVarArg { } extension TKSmartCardUserInteraction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [TKSmartCardUserInteraction.initialTimeout](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390178-initialtimeout)

|  | Declaration |
| --- | --- |
| From | ``` var initialTimeout: NSTimeInterval ``` |
| To | ``` var initialTimeout: TimeInterval ``` |

Modified [TKSmartCardUserInteraction.interactionTimeout](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390206-interactiontimeout)

|  | Declaration |
| --- | --- |
| From | ``` var interactionTimeout: NSTimeInterval ``` |
| To | ``` var interactionTimeout: TimeInterval ``` |

Modified [TKSmartCardUserInteraction.run(reply: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390212-run)

|  | Declaration |
| --- | --- |
| From | ``` func runWithReply(_ reply: (Bool, NSError?) -> Void) ``` |
| To | ``` func run(reply reply: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [TKSmartCardUserInteractionDelegate](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol TKSmartCardUserInteractionDelegate {     optional func characterEnteredInUserInteraction(_ interaction: TKSmartCardUserInteraction)     optional func correctionKeyPressedInUserInteraction(_ interaction: TKSmartCardUserInteraction)     optional func validationKeyPressedInUserInteraction(_ interaction: TKSmartCardUserInteraction)     optional func invalidCharacterEnteredInUserInteraction(_ interaction: TKSmartCardUserInteraction)     optional func oldPINRequestedInUserInteraction(_ interaction: TKSmartCardUserInteraction)     optional func newPINRequestedInUserInteraction(_ interaction: TKSmartCardUserInteraction)     optional func newPINConfirmationRequestedInUserInteraction(_ interaction: TKSmartCardUserInteraction) } ``` |
| To | ``` protocol TKSmartCardUserInteractionDelegate {     optional func characterEntered(in interaction: TKSmartCardUserInteraction)     optional func correctionKeyPressed(in interaction: TKSmartCardUserInteraction)     optional func validationKeyPressed(in interaction: TKSmartCardUserInteraction)     optional func invalidCharacterEntered(in interaction: TKSmartCardUserInteraction)     optional func oldPINRequested(in interaction: TKSmartCardUserInteraction)     optional func newPINRequested(in interaction: TKSmartCardUserInteraction)     optional func newPINConfirmationRequested(in interaction: TKSmartCardUserInteraction) } ``` |

Modified [TKSmartCardUserInteractionDelegate.characterEntered(in: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390259-characterentered)

|  | Declaration |
| --- | --- |
| From | ``` optional func characterEnteredInUserInteraction(_ interaction: TKSmartCardUserInteraction) ``` |
| To | ``` optional func characterEntered(in interaction: TKSmartCardUserInteraction) ``` |

Modified [TKSmartCardUserInteractionDelegate.correctionKeyPressed(in: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390160-correctionkeypressed)

|  | Declaration |
| --- | --- |
| From | ``` optional func correctionKeyPressedInUserInteraction(_ interaction: TKSmartCardUserInteraction) ``` |
| To | ``` optional func correctionKeyPressed(in interaction: TKSmartCardUserInteraction) ``` |

Modified [TKSmartCardUserInteractionDelegate.invalidCharacterEntered(in: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390180-invalidcharacterentered)

|  | Declaration |
| --- | --- |
| From | ``` optional func invalidCharacterEnteredInUserInteraction(_ interaction: TKSmartCardUserInteraction) ``` |
| To | ``` optional func invalidCharacterEntered(in interaction: TKSmartCardUserInteraction) ``` |

Modified [TKSmartCardUserInteractionDelegate.newPINConfirmationRequested(in: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390263-newpinconfirmationrequested)

|  | Declaration |
| --- | --- |
| From | ``` optional func newPINConfirmationRequestedInUserInteraction(_ interaction: TKSmartCardUserInteraction) ``` |
| To | ``` optional func newPINConfirmationRequested(in interaction: TKSmartCardUserInteraction) ``` |

Modified [TKSmartCardUserInteractionDelegate.newPINRequested(in: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390300-newpinrequestedinuserinteraction)

|  | Declaration |
| --- | --- |
| From | ``` optional func newPINRequestedInUserInteraction(_ interaction: TKSmartCardUserInteraction) ``` |
| To | ``` optional func newPINRequested(in interaction: TKSmartCardUserInteraction) ``` |

Modified [TKSmartCardUserInteractionDelegate.oldPINRequested(in: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390316-oldpinrequested)

|  | Declaration |
| --- | --- |
| From | ``` optional func oldPINRequestedInUserInteraction(_ interaction: TKSmartCardUserInteraction) ``` |
| To | ``` optional func oldPINRequested(in interaction: TKSmartCardUserInteraction) ``` |

Modified [TKSmartCardUserInteractionDelegate.validationKeyPressed(in: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390164-validationkeypressedinuserintera)

|  | Declaration |
| --- | --- |
| From | ``` optional func validationKeyPressedInUserInteraction(_ interaction: TKSmartCardUserInteraction) ``` |
| To | ``` optional func validationKeyPressed(in interaction: TKSmartCardUserInteraction) ``` |

Modified [TKSmartCardUserInteractionForPINOperation](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation)

|  | Declaration |
| --- | --- |
| From | ``` class TKSmartCardUserInteractionForPINOperation : TKSmartCardUserInteraction {     var PINCompletion: TKSmartCardPINCompletion     var PINMessageIndices: [NSNumber]?     var locale: NSLocale!     var resultSW: UInt16     var resultData: NSData? } ``` |
| To | ``` class TKSmartCardUserInteractionForPINOperation : TKSmartCardUserInteraction {     var pinCompletion: TKSmartCardUserInteractionForPINOperation.Completion     var pinMessageIndices: [NSNumber]?     var locale: Locale!     var resultSW: UInt16     var resultData: Data?     struct Completion : OptionSet {         init(rawValue rawValue: UInt)         static var maxLength: TKSmartCardUserInteractionForPINOperation.Completion { get }         static var key: TKSmartCardUserInteractionForPINOperation.Completion { get }         static var timeout: TKSmartCardUserInteractionForPINOperation.Completion { get }     } } extension TKSmartCardUserInteractionForPINOperation {     struct Completion : OptionSet {         init(rawValue rawValue: UInt)         static var maxLength: TKSmartCardUserInteractionForPINOperation.Completion { get }         static var key: TKSmartCardUserInteractionForPINOperation.Completion { get }         static var timeout: TKSmartCardUserInteractionForPINOperation.Completion { get }     } } ``` |

Modified [TKSmartCardUserInteractionForPINOperation.locale](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390202-locale)

|  | Declaration |
| --- | --- |
| From | ``` var locale: NSLocale! ``` |
| To | ``` var locale: Locale! ``` |

Modified [TKSmartCardUserInteractionForPINOperation.pinCompletion](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390184-pincompletion)

|  | Declaration |
| --- | --- |
| From | ``` var PINCompletion: TKSmartCardPINCompletion ``` |
| To | ``` var pinCompletion: TKSmartCardUserInteractionForPINOperation.Completion ``` |

Modified [TKSmartCardUserInteractionForPINOperation.pinMessageIndices](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390192-pinmessageindices)

|  | Declaration |
| --- | --- |
| From | ``` var PINMessageIndices: [NSNumber]? ``` |
| To | ``` var pinMessageIndices: [NSNumber]? ``` |

Modified [TKSmartCardUserInteractionForPINOperation.resultData](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390308-resultdata)

|  | Declaration |
| --- | --- |
| From | ``` var resultData: NSData? ``` |
| To | ``` var resultData: Data? ``` |

Modified [TKSmartCardUserInteractionForPINOperation.Completion [struct]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpincompletion)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct TKSmartCardPINCompletion : OptionSetType {     init(rawValue rawValue: UInt)     static var MaxLength: TKSmartCardPINCompletion { get }     static var Key: TKSmartCardPINCompletion { get }     static var Timeout: TKSmartCardPINCompletion { get } } ``` | OptionSetType |
| To | ``` struct Completion : OptionSet {         init(rawValue rawValue: UInt)         static var maxLength: TKSmartCardUserInteractionForPINOperation.Completion { get }         static var key: TKSmartCardUserInteractionForPINOperation.Completion { get }         static var timeout: TKSmartCardUserInteractionForPINOperation.Completion { get }     } extension TKSmartCardUserInteractionForPINOperation.Completion {     func union(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> TKSmartCardUserInteractionForPINOperation.Completion     func intersection(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> TKSmartCardUserInteractionForPINOperation.Completion     func symmetricDifference(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> TKSmartCardUserInteractionForPINOperation.Completion } extension TKSmartCardUserInteractionForPINOperation.Completion {     func contains(_ member: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool     mutating func insert(_ newMember: TKSmartCardUserInteractionForPINOperation.Completion) -> (inserted: Bool, memberAfterInsert: TKSmartCardUserInteractionForPINOperation.Completion)     mutating func remove(_ member: TKSmartCardUserInteractionForPINOperation.Completion) -> TKSmartCardUserInteractionForPINOperation.Completion?     mutating func update(with newMember: TKSmartCardUserInteractionForPINOperation.Completion) -> TKSmartCardUserInteractionForPINOperation.Completion? } extension TKSmartCardUserInteractionForPINOperation.Completion {     convenience init()     mutating func formUnion(_ other: TKSmartCardUserInteractionForPINOperation.Completion)     mutating func formIntersection(_ other: TKSmartCardUserInteractionForPINOperation.Completion)     mutating func formSymmetricDifference(_ other: TKSmartCardUserInteractionForPINOperation.Completion) } extension TKSmartCardUserInteractionForPINOperation.Completion {     convenience init<S : Sequence where S.Iterator.Element == TKSmartCardUserInteractionForPINOperation.Completion>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: TKSmartCardUserInteractionForPINOperation.Completion...)     mutating func subtract(_ other: TKSmartCardUserInteractionForPINOperation.Completion)     func isSubset(of other: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool     func isSuperset(of other: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool     func isDisjoint(with other: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool     func subtracting(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> TKSmartCardUserInteractionForPINOperation.Completion     var isEmpty: Bool { get }     func isStrictSuperset(of other: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool     func isStrictSubset(of other: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool } extension TKSmartCardUserInteractionForPINOperation.Completion {     func intersect(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> TKSmartCardUserInteractionForPINOperation.Completion     func exclusiveOr(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> TKSmartCardUserInteractionForPINOperation.Completion     mutating func unionInPlace(_ other: TKSmartCardUserInteractionForPINOperation.Completion)     mutating func intersectInPlace(_ other: TKSmartCardUserInteractionForPINOperation.Completion)     mutating func exclusiveOrInPlace(_ other: TKSmartCardUserInteractionForPINOperation.Completion)     func isSubsetOf(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool     func isDisjointWith(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool     func isSupersetOf(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool     mutating func subtractInPlace(_ other: TKSmartCardUserInteractionForPINOperation.Completion)     func isStrictSupersetOf(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool     func isStrictSubsetOf(_ other: TKSmartCardUserInteractionForPINOperation.Completion) -> Bool } ``` | OptionSet |

Modified [TKSmartCardUserInteractionForPINOperation.Completion.key](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion/1390220-key)

|  | Declaration |
| --- | --- |
| From | ``` static var Key: TKSmartCardPINCompletion { get } ``` |
| To | ``` static var key: TKSmartCardUserInteractionForPINOperation.Completion { get } ``` |

Modified [TKSmartCardUserInteractionForPINOperation.Completion.maxLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion/1390298-maxlength)

|  | Declaration |
| --- | --- |
| From | ``` static var MaxLength: TKSmartCardPINCompletion { get } ``` |
| To | ``` static var maxLength: TKSmartCardUserInteractionForPINOperation.Completion { get } ``` |

Modified [TKSmartCardUserInteractionForPINOperation.Completion.timeout](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpincompletion/tksmartcardpincompletiontimeout)

|  | Declaration |
| --- | --- |
| From | ``` static var Timeout: TKSmartCardPINCompletion { get } ``` |
| To | ``` static var timeout: TKSmartCardUserInteractionForPINOperation.Completion { get } ``` |

Modified [TKSmartCardUserInteractionForSecurePINChange](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange)

|  | Declaration |
| --- | --- |
| From | ``` class TKSmartCardUserInteractionForSecurePINChange : TKSmartCardUserInteractionForPINOperation {     var PINConfirmation: TKSmartCardPINConfirmation } ``` |
| To | ``` class TKSmartCardUserInteractionForSecurePINChange : TKSmartCardUserInteractionForPINOperation {     var pinConfirmation: TKSmartCardUserInteractionForSecurePINChange.Confirmation     struct Confirmation : OptionSet {         init(rawValue rawValue: UInt)         static var none: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get }         static var new: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get }         static var current: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get }     }     struct Completion : OptionSet {         init(rawValue rawValue: UInt)         static var maxLength: TKSmartCardUserInteractionForPINOperation.Completion { get }         static var key: TKSmartCardUserInteractionForPINOperation.Completion { get }         static var timeout: TKSmartCardUserInteractionForPINOperation.Completion { get }     } } extension TKSmartCardUserInteractionForSecurePINChange {     struct Confirmation : OptionSet {         init(rawValue rawValue: UInt)         static var none: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get }         static var new: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get }         static var current: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get }     } } ``` |

Modified [TKSmartCardUserInteractionForSecurePINChange.pinConfirmation](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/1390310-pinconfirmation)

|  | Declaration |
| --- | --- |
| From | ``` var PINConfirmation: TKSmartCardPINConfirmation ``` |
| To | ``` var pinConfirmation: TKSmartCardUserInteractionForSecurePINChange.Confirmation ``` |

Modified [TKSmartCardUserInteractionForSecurePINChange.Confirmation [struct]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/confirmation)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct TKSmartCardPINConfirmation : OptionSetType {     init(rawValue rawValue: UInt)     static var None: TKSmartCardPINConfirmation { get }     static var New: TKSmartCardPINConfirmation { get }     static var Current: TKSmartCardPINConfirmation { get } } ``` | OptionSetType |
| To | ``` struct Confirmation : OptionSet {         init(rawValue rawValue: UInt)         static var none: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get }         static var new: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get }         static var current: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get }     } extension TKSmartCardUserInteractionForSecurePINChange.Confirmation {     func union(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> TKSmartCardUserInteractionForSecurePINChange.Confirmation     func intersection(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> TKSmartCardUserInteractionForSecurePINChange.Confirmation     func symmetricDifference(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> TKSmartCardUserInteractionForSecurePINChange.Confirmation } extension TKSmartCardUserInteractionForSecurePINChange.Confirmation {     func contains(_ member: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool     mutating func insert(_ newMember: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> (inserted: Bool, memberAfterInsert: TKSmartCardUserInteractionForSecurePINChange.Confirmation)     mutating func remove(_ member: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> TKSmartCardUserInteractionForSecurePINChange.Confirmation?     mutating func update(with newMember: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> TKSmartCardUserInteractionForSecurePINChange.Confirmation? } extension TKSmartCardUserInteractionForSecurePINChange.Confirmation {     convenience init()     mutating func formUnion(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation)     mutating func formIntersection(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation)     mutating func formSymmetricDifference(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) } extension TKSmartCardUserInteractionForSecurePINChange.Confirmation {     convenience init<S : Sequence where S.Iterator.Element == TKSmartCardUserInteractionForSecurePINChange.Confirmation>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: TKSmartCardUserInteractionForSecurePINChange.Confirmation...)     mutating func subtract(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation)     func isSubset(of other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool     func isSuperset(of other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool     func isDisjoint(with other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool     func subtracting(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> TKSmartCardUserInteractionForSecurePINChange.Confirmation     var isEmpty: Bool { get }     func isStrictSuperset(of other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool     func isStrictSubset(of other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool } extension TKSmartCardUserInteractionForSecurePINChange.Confirmation {     func intersect(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> TKSmartCardUserInteractionForSecurePINChange.Confirmation     func exclusiveOr(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> TKSmartCardUserInteractionForSecurePINChange.Confirmation     mutating func unionInPlace(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation)     mutating func intersectInPlace(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation)     mutating func exclusiveOrInPlace(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation)     func isSubsetOf(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool     func isDisjointWith(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool     func isSupersetOf(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool     mutating func subtractInPlace(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation)     func isStrictSupersetOf(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool     func isStrictSubsetOf(_ other: TKSmartCardUserInteractionForSecurePINChange.Confirmation) -> Bool } ``` | OptionSet |

Modified [TKSmartCardUserInteractionForSecurePINChange.Confirmation.current](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinconfirmation/tksmartcardpinconfirmationcurrent)

|  | Declaration |
| --- | --- |
| From | ``` static var Current: TKSmartCardPINConfirmation { get } ``` |
| To | ``` static var current: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get } ``` |

Modified [TKSmartCardUserInteractionForSecurePINChange.Confirmation.new](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/confirmation/1390318-new)

|  | Declaration |
| --- | --- |
| From | ``` static var New: TKSmartCardPINConfirmation { get } ``` |
| To | ``` static var new: TKSmartCardUserInteractionForSecurePINChange.Confirmation { get } ``` |

Modified [TKSmartCardUserInteractionForSecurePINVerification](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinverification)

|  | Declaration |
| --- | --- |
| From | ``` class TKSmartCardUserInteractionForSecurePINVerification : TKSmartCardUserInteractionForPINOperation { } ``` |
| To | ``` class TKSmartCardUserInteractionForSecurePINVerification : TKSmartCardUserInteractionForPINOperation {     struct Completion : OptionSet {         init(rawValue rawValue: UInt)         static var maxLength: TKSmartCardUserInteractionForPINOperation.Completion { get }         static var key: TKSmartCardUserInteractionForPINOperation.Completion { get }         static var timeout: TKSmartCardUserInteractionForPINOperation.Completion { get }     } } ``` |

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
