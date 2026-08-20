---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CryptoTokenKit.html
archived_at: '2026-07-18T02:53:30.520489Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CryptoTokenKit Changes for Swift

### CryptoTokenKit

Removed TKSmartCardProtocol.init(_: UInt)Added [TKErrorCode.AuthenticationFailed](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodeauthenticationfailed)Added [TKErrorCode.BadParameter](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodebadparameter)Added [TKErrorCode.ObjectNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodeobjectnotfound)Added [TKErrorCode.TokenNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/tokennotfound)Added [TKSmartCard.userInteractionForSecurePINChangeWithPINFormat(_: TKSmartCardPINFormat, APDU: NSData, currentPINByteOffset: Int, newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange?](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390312-userinteractionforsecurepinchang)Added [TKSmartCard.userInteractionForSecurePINVerificationWithPINFormat(_: TKSmartCardPINFormat, APDU: NSData, PINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification?](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390289-userinteractionforsecurepinverif)Added [TKSmartCardPINCharset [enum]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/charset)Added [TKSmartCardPINCharset.Alphanumeric](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/charset/alphanumeric)Added [TKSmartCardPINCharset.Numeric](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpincharset/tksmartcardpincharsetnumeric)Added [TKSmartCardPINCharset.UpperAlphanumeric](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpincharset/tksmartcardpincharsetupperalphanumeric)Added [TKSmartCardPINCompletion [struct]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpincompletion)Added TKSmartCardPINCompletion.init(rawValue: UInt)Added [TKSmartCardPINCompletion.Key](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion/1390220-key)Added [TKSmartCardPINCompletion.MaxLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion/1390298-maxlength)Added [TKSmartCardPINCompletion.Timeout](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/completion/1390196-timeout)Added [TKSmartCardPINConfirmation [struct]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/confirmation)Added [TKSmartCardPINConfirmation.Current](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinconfirmation/tksmartcardpinconfirmationcurrent)Added TKSmartCardPINConfirmation.init(rawValue: UInt)Added [TKSmartCardPINConfirmation.New](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/confirmation/1390318-new)Added [TKSmartCardPINConfirmation.None](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinconfirmation/tksmartcardpinconfirmationnone)Added [TKSmartCardPINEncoding [enum]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/encoding)Added [TKSmartCardPINEncoding.ASCII](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinencoding/tksmartcardpinencodingascii)Added [TKSmartCardPINEncoding.BCD](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinencoding/tksmartcardpinencodingbcd)Added [TKSmartCardPINEncoding.Binary](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinencoding/tksmartcardpinencodingbinary)Added [TKSmartCardPINFormat](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat)Added [TKSmartCardPINFormat.charset](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390176-charset)Added [TKSmartCardPINFormat.encoding](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390241-encoding)Added [TKSmartCardPINFormat.maxPINLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390182-maxpinlength)Added [TKSmartCardPINFormat.minPINLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390188-minpinlength)Added [TKSmartCardPINFormat.PINBitOffset](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390269-pinbitoffset)Added [TKSmartCardPINFormat.PINBlockByteLength](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390198-pinblockbytelength)Added [TKSmartCardPINFormat.PINJustification](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390190-pinjustification)Added [TKSmartCardPINFormat.PINLengthBitOffset](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390291-pinlengthbitoffset)Added [TKSmartCardPINFormat.PINLengthBitSize](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/1390314-pinlengthbitsize)Added [TKSmartCardPINJustification [enum]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/justification)Added [TKSmartCardPINJustification.Left](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinformat/justification/left)Added [TKSmartCardPINJustification.Right](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardpinjustification/tksmartcardpinjustificationright)Added [TKSmartCardUserInteraction](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction)Added [TKSmartCardUserInteraction.cancel() -> Bool](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390231-cancel)Added [TKSmartCardUserInteraction.delegate](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390166-delegate)Added [TKSmartCardUserInteraction.initialTimeout](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390178-initialtimeout)Added [TKSmartCardUserInteraction.interactionTimeout](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390206-interactiontimeout)Added [TKSmartCardUserInteraction.runWithReply(_: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction/1390212-run)Added [TKSmartCardUserInteractionDelegate](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate)Added [TKSmartCardUserInteractionDelegate.characterEnteredInUserInteraction(_: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390259-characterentered)Added [TKSmartCardUserInteractionDelegate.correctionKeyPressedInUserInteraction(_: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390160-correctionkeypressed)Added [TKSmartCardUserInteractionDelegate.invalidCharacterEnteredInUserInteraction(_: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390180-invalidcharacterentered)Added [TKSmartCardUserInteractionDelegate.newPINConfirmationRequestedInUserInteraction(_: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390263-newpinconfirmationrequested)Added [TKSmartCardUserInteractionDelegate.newPINRequestedInUserInteraction(_: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390300-newpinrequestedinuserinteraction)Added [TKSmartCardUserInteractionDelegate.oldPINRequestedInUserInteraction(_: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390316-oldpinrequested)Added [TKSmartCardUserInteractionDelegate.validationKeyPressedInUserInteraction(_: TKSmartCardUserInteraction)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractiondelegate/1390164-validationkeypressedinuserintera)Added [TKSmartCardUserInteractionForPINOperation](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation)Added [TKSmartCardUserInteractionForPINOperation.locale](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390202-locale)Added [TKSmartCardUserInteractionForPINOperation.PINCompletion](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390184-pincompletion)Added [TKSmartCardUserInteractionForPINOperation.PINMessageIndices](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390192-pinmessageindices)Added [TKSmartCardUserInteractionForPINOperation.resultData](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390308-resultdata)Added [TKSmartCardUserInteractionForPINOperation.resultSW](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation/1390200-resultsw)Added [TKSmartCardUserInteractionForSecurePINChange](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange)Added [TKSmartCardUserInteractionForSecurePINChange.PINConfirmation](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange/1390310-pinconfirmation)Added [TKSmartCardUserInteractionForSecurePINVerification](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinverification)Modified [TKErrorCode [enum]](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum TKErrorCode : Int {     case CodeNotImplemented     case CodeCommunicationError     case CodeCorruptedData     case CodeCanceledByUser     case AuthenticationFailed     case ObjectNotFound     case TokenNotFound } ``` | -- |
| To | ``` enum TKErrorCode : Int {     case NotImplemented     case CommunicationError     case CorruptedData     case CanceledByUser     case AuthenticationFailed     case ObjectNotFound     case TokenNotFound     case BadParameter     static var TKErrorAuthenticationFailed: TKErrorCode { get }     static var TKErrorObjectNotFound: TKErrorCode { get }     static var TKErrorTokenNotFound: TKErrorCode { get } } ``` | Int |

Modified [TKErrorCode.CanceledByUser](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/canceledbyuser)

|  | Declaration |
| --- | --- |
| From | ``` case CodeCanceledByUser ``` |
| To | ``` case CanceledByUser ``` |

Modified [TKErrorCode.CommunicationError](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/communicationerror)

|  | Declaration |
| --- | --- |
| From | ``` case CodeCommunicationError ``` |
| To | ``` case CommunicationError ``` |

Modified [TKErrorCode.CorruptedData](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodecorrupteddata)

|  | Declaration |
| --- | --- |
| From | ``` case CodeCorruptedData ``` |
| To | ``` case CorruptedData ``` |

Modified [TKErrorCode.NotImplemented](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorcodenotimplemented)

|  | Declaration |
| --- | --- |
| From | ``` case CodeNotImplemented ``` |
| To | ``` case NotImplemented ``` |

Modified [TKErrorCode.TKErrorAuthenticationFailed](https://developer.apple.com/documentation/cryptotokenkit/tkerrorcode/tkerrorauthenticationfailed)

|  | Name | Declaration | Deprecation |
| --- | --- | --- | --- |
| From | AuthenticationFailed | ``` case AuthenticationFailed ``` | -- |
| To | TKErrorAuthenticationFailed | ``` static var TKErrorAuthenticationFailed: TKErrorCode { get } ``` | OS X 10.11 |

Modified [TKErrorCode.TKErrorObjectNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/1393807-tkerrorobjectnotfound)

|  | Name | Declaration | Deprecation |
| --- | --- | --- | --- |
| From | ObjectNotFound | ``` case ObjectNotFound ``` | -- |
| To | TKErrorObjectNotFound | ``` static var TKErrorObjectNotFound: TKErrorCode { get } ``` | OS X 10.11 |

Modified [TKErrorCode.TKErrorTokenNotFound](https://developer.apple.com/documentation/cryptotokenkit/tkerror/code/1393801-tkerrortokennotfound)

|  | Name | Declaration | Deprecation |
| --- | --- | --- | --- |
| From | TokenNotFound | ``` case TokenNotFound ``` | -- |
| To | TKErrorTokenNotFound | ``` static var TKErrorTokenNotFound: TKErrorCode { get } ``` | OS X 10.11 |

Modified [TKSmartCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard)

|  | Declaration |
| --- | --- |
| From | ``` class TKSmartCard : NSObject {     var slot: TKSmartCardSlot! { get }     var valid: Bool { get }     var allowedProtocols: TKSmartCardProtocol     var currentProtocol: TKSmartCardProtocol { get }     var sensitive: Bool     var context: AnyObject!     func beginSessionWithReply(_ reply: ((Bool, NSError!) -> Void)!)     func transmitRequest(_ request: NSData!, reply reply: ((NSData!, NSError!) -> Void)!)     func endSession() } extension TKSmartCard {     var cla: UInt8     var useExtendedLength: Bool     func sendIns(_ ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data requestData: NSData!, le le: NSNumber!, reply reply: ((NSData!, UInt16, NSError!) -> Void)!) } ``` |
| To | ``` class TKSmartCard : NSObject {     var slot: TKSmartCardSlot { get }     var valid: Bool { get }     var allowedProtocols: TKSmartCardProtocol     var currentProtocol: TKSmartCardProtocol { get }     var sensitive: Bool     var context: AnyObject?     func beginSessionWithReply(_ reply: (Bool, NSError?) -> Void)     func transmitRequest(_ request: NSData, reply reply: (NSData?, NSError?) -> Void)     func endSession()     func userInteractionForSecurePINVerificationWithPINFormat(_ PINFormat: TKSmartCardPINFormat, APDU APDU: NSData, PINByteOffset PINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification?     func userInteractionForSecurePINChangeWithPINFormat(_ PINFormat: TKSmartCardPINFormat, APDU APDU: NSData, currentPINByteOffset currentPINByteOffset: Int, newPINByteOffset newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange? } extension TKSmartCard {     var cla: UInt8     var useExtendedLength: Bool     func sendIns(_ ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data requestData: NSData, le le: NSNumber?, reply reply: (NSData?, UInt16, NSError?) -> Void) } ``` |

Modified [TKSmartCard.beginSessionWithReply(_: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390168-beginsessionwithreply)

|  | Declaration |
| --- | --- |
| From | ``` func beginSessionWithReply(_ reply: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func beginSessionWithReply(_ reply: (Bool, NSError?) -> Void) ``` |

Modified [TKSmartCard.context](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390243-context)

|  | Declaration |
| --- | --- |
| From | ``` var context: AnyObject! ``` |
| To | ``` var context: AnyObject? ``` |

Modified [TKSmartCard.sendIns(_: UInt8, p1: UInt8, p2: UInt8, data: NSData, le: NSNumber?, reply: (NSData?, UInt16, NSError?) -> Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390283-sendins)

|  | Declaration |
| --- | --- |
| From | ``` func sendIns(_ ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data requestData: NSData!, le le: NSNumber!, reply reply: ((NSData!, UInt16, NSError!) -> Void)!) ``` |
| To | ``` func sendIns(_ ins: UInt8, p1 p1: UInt8, p2 p2: UInt8, data requestData: NSData, le le: NSNumber?, reply reply: (NSData?, UInt16, NSError?) -> Void) ``` |

Modified [TKSmartCard.slot](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390281-slot)

|  | Declaration |
| --- | --- |
| From | ``` var slot: TKSmartCardSlot! { get } ``` |
| To | ``` var slot: TKSmartCardSlot { get } ``` |

Modified [TKSmartCard.transmitRequest(_: NSData, reply: (NSData?, NSError?) -> Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/1390161-transmit)

|  | Declaration |
| --- | --- |
| From | ``` func transmitRequest(_ request: NSData!, reply reply: ((NSData!, NSError!) -> Void)!) ``` |
| To | ``` func transmitRequest(_ request: NSData, reply reply: (NSData?, NSError?) -> Void) ``` |

Modified [TKSmartCardATR](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr)

|  | Declaration |
| --- | --- |
| From | ``` class TKSmartCardATR : NSObject {     init!(bytes bytes: NSData!)     init!(source source: (() -> Int32)!)     var bytes: NSData! { get }     var protocols: [AnyObject]! { get }     func interfaceGroupAtIndex(_ index: Int) -> TKSmartCardATRInterfaceGroup!     func interfaceGroupForProtocol(_ `protocol`: TKSmartCardProtocol) -> TKSmartCardATRInterfaceGroup!     var historicalBytes: NSData! { get } } ``` |
| To | ``` class TKSmartCardATR : NSObject {     init?(bytes bytes: NSData)     init?(source source: () -> Int32)     var bytes: NSData { get }     var protocols: [NSNumber] { get }     func interfaceGroupAtIndex(_ index: Int) -> TKSmartCardATRInterfaceGroup?     func interfaceGroupForProtocol(_ `protocol`: TKSmartCardProtocol) -> TKSmartCardATRInterfaceGroup?     var historicalBytes: NSData { get } } ``` |

Modified [TKSmartCardATR.bytes](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403518-bytes)

|  | Declaration |
| --- | --- |
| From | ``` var bytes: NSData! { get } ``` |
| To | ``` var bytes: NSData { get } ``` |

Modified [TKSmartCardATR.historicalBytes](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403513-historicalbytes)

|  | Declaration |
| --- | --- |
| From | ``` var historicalBytes: NSData! { get } ``` |
| To | ``` var historicalBytes: NSData { get } ``` |

Modified [TKSmartCardATR.init(bytes: NSData)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403560-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(bytes bytes: NSData!) ``` |
| To | ``` init?(bytes bytes: NSData) ``` |

Modified [TKSmartCardATR.init(source: () -> Int32)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403516-initwithsource)

|  | Declaration |
| --- | --- |
| From | ``` init!(source source: (() -> Int32)!) ``` |
| To | ``` init?(source source: () -> Int32) ``` |

Modified [TKSmartCardATR.interfaceGroupAtIndex(_: Int) -> TKSmartCardATRInterfaceGroup?](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403537-interfacegroup)

|  | Declaration |
| --- | --- |
| From | ``` func interfaceGroupAtIndex(_ index: Int) -> TKSmartCardATRInterfaceGroup! ``` |
| To | ``` func interfaceGroupAtIndex(_ index: Int) -> TKSmartCardATRInterfaceGroup? ``` |

Modified [TKSmartCardATR.interfaceGroupForProtocol(_: TKSmartCardProtocol) -> TKSmartCardATRInterfaceGroup?](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403483-interfacegroup)

|  | Declaration |
| --- | --- |
| From | ``` func interfaceGroupForProtocol(_ `protocol`: TKSmartCardProtocol) -> TKSmartCardATRInterfaceGroup! ``` |
| To | ``` func interfaceGroupForProtocol(_ `protocol`: TKSmartCardProtocol) -> TKSmartCardATRInterfaceGroup? ``` |

Modified [TKSmartCardATR.protocols](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/1403472-protocols)

|  | Declaration |
| --- | --- |
| From | ``` var protocols: [AnyObject]! { get } ``` |
| To | ``` var protocols: [NSNumber] { get } ``` |

Modified [TKSmartCardATRInterfaceGroup](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatrinterfacegroup)

|  | Declaration |
| --- | --- |
| From | ``` class TKSmartCardATRInterfaceGroup : NSObject {     var TA: NSNumber! { get }     var TB: NSNumber! { get }     var TC: NSNumber! { get }     var `protocol`: NSNumber! { get } } ``` |
| To | ``` class TKSmartCardATRInterfaceGroup : NSObject {     var TA: NSNumber? { get }     var TB: NSNumber? { get }     var TC: NSNumber? { get }     var `protocol`: NSNumber? { get } } ``` |

Modified [TKSmartCardATRInterfaceGroup.protocol](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup/1403429-protocol)

|  | Declaration |
| --- | --- |
| From | ``` var `protocol`: NSNumber! { get } ``` |
| To | ``` var `protocol`: NSNumber? { get } ``` |

Modified [TKSmartCardATRInterfaceGroup.TA](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatrinterfacegroup/1403499-ta)

|  | Declaration |
| --- | --- |
| From | ``` var TA: NSNumber! { get } ``` |
| To | ``` var TA: NSNumber? { get } ``` |

Modified [TKSmartCardATRInterfaceGroup.TB](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup/1403452-tb)

|  | Declaration |
| --- | --- |
| From | ``` var TB: NSNumber! { get } ``` |
| To | ``` var TB: NSNumber? { get } ``` |

Modified [TKSmartCardATRInterfaceGroup.TC](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatrinterfacegroup/1403438-tc)

|  | Declaration |
| --- | --- |
| From | ``` var TC: NSNumber! { get } ``` |
| To | ``` var TC: NSNumber? { get } ``` |

Modified [TKSmartCardProtocol [struct]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardprotocol)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct TKSmartCardProtocol : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: TKSmartCardProtocol { get }     static var T0: TKSmartCardProtocol { get }     static var T1: TKSmartCardProtocol { get }     static var T15: TKSmartCardProtocol { get }     static var Any: TKSmartCardProtocol { get } } ``` | RawOptionSetType |
| To | ``` struct TKSmartCardProtocol : OptionSetType {     init(rawValue rawValue: UInt)     static var None: TKSmartCardProtocol { get }     static var T0: TKSmartCardProtocol { get }     static var T1: TKSmartCardProtocol { get }     static var T15: TKSmartCardProtocol { get }     static var Any: TKSmartCardProtocol { get } } ``` | OptionSetType |

Modified [TKSmartCardSlot](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot)

|  | Declaration |
| --- | --- |
| From | ``` class TKSmartCardSlot : NSObject {     var state: TKSmartCardSlotState { get }     var ATR: TKSmartCardATR! { get }     var name: String! { get }     var maxInputLength: Int { get }     var maxOutputLength: Int { get }     func makeSmartCard() -> TKSmartCard! } ``` |
| To | ``` class TKSmartCardSlot : NSObject {     var state: TKSmartCardSlotState { get }     var ATR: TKSmartCardATR? { get }     var name: String { get }     var maxInputLength: Int { get }     var maxOutputLength: Int { get }     func makeSmartCard() -> TKSmartCard? } ``` |

Modified [TKSmartCardSlot.ATR](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390285-atr)

|  | Declaration |
| --- | --- |
| From | ``` var ATR: TKSmartCardATR! { get } ``` |
| To | ``` var ATR: TKSmartCardATR? { get } ``` |

Modified [TKSmartCardSlot.makeSmartCard() -> TKSmartCard?](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390225-makesmartcard)

|  | Declaration |
| --- | --- |
| From | ``` func makeSmartCard() -> TKSmartCard! ``` |
| To | ``` func makeSmartCard() -> TKSmartCard? ``` |

Modified [TKSmartCardSlot.name](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/1390186-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [TKSmartCardSlotManager](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager)

|  | Declaration |
| --- | --- |
| From | ``` class TKSmartCardSlotManager : NSObject {     class func defaultManager() -> Self!     var slotNames: [AnyObject]! { get }     func getSlotWithName(_ name: String!, reply reply: ((TKSmartCardSlot!) -> Void)!) } ``` |
| To | ``` class TKSmartCardSlotManager : NSObject {     class func defaultManager() -> Self?     var slotNames: [String] { get }     func getSlotWithName(_ name: String, reply reply: (TKSmartCardSlot?) -> Void) } ``` |

Modified [TKSmartCardSlotManager.defaultManager() -> Self? [class]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390245-defaultmanager)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultManager() -> Self! ``` |
| To | ``` class func defaultManager() -> Self? ``` |

Modified [TKSmartCardSlotManager.getSlotWithName(_: String, reply: (TKSmartCardSlot?) -> Void)](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390265-getslot)

|  | Declaration |
| --- | --- |
| From | ``` func getSlotWithName(_ name: String!, reply reply: ((TKSmartCardSlot!) -> Void)!) ``` |
| To | ``` func getSlotWithName(_ name: String, reply reply: (TKSmartCardSlot?) -> Void) ``` |

Modified [TKSmartCardSlotManager.slotNames](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/1390156-slotnames)

|  | Declaration |
| --- | --- |
| From | ``` var slotNames: [AnyObject]! { get } ``` |
| To | ``` var slotNames: [String] { get } ``` |

Modified [TKSmartCardSlotState [enum]](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum TKSmartCardSlotState : Int {     case SlotStateMissing     case SlotStateEmpty     case SlotStateProbing     case SlotStateMuteCard     case SlotStateValidCard } ``` | -- |
| To | ``` enum TKSmartCardSlotState : Int {     case Missing     case Empty     case Probing     case MuteCard     case ValidCard } ``` | Int |

Modified [TKSmartCardSlotState.Empty](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state/empty)

|  | Declaration |
| --- | --- |
| From | ``` case SlotStateEmpty ``` |
| To | ``` case Empty ``` |

Modified [TKSmartCardSlotState.Missing](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state/missing)

|  | Declaration |
| --- | --- |
| From | ``` case SlotStateMissing ``` |
| To | ``` case Missing ``` |

Modified [TKSmartCardSlotState.MuteCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state/mutecard)

|  | Declaration |
| --- | --- |
| From | ``` case SlotStateMuteCard ``` |
| To | ``` case MuteCard ``` |

Modified [TKSmartCardSlotState.Probing](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotstate/tksmartcardslotstateprobing)

|  | Declaration |
| --- | --- |
| From | ``` case SlotStateProbing ``` |
| To | ``` case Probing ``` |

Modified [TKSmartCardSlotState.ValidCard](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state/validcard)

|  | Declaration |
| --- | --- |
| From | ``` case SlotStateValidCard ``` |
| To | ``` case ValidCard ``` |

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
