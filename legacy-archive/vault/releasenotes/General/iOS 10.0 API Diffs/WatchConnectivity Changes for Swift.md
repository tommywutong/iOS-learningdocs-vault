---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/WatchConnectivity.html
archived_at: '2026-07-18T02:55:45.819372Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# WatchConnectivity Changes for Swift

### WatchConnectivity

Added [WCError [struct]](https://developer.apple.com/documentation/watchconnectivity/wcerror)Added [WCError.deliveryFailed](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320698-deliveryfailed)Added [WCError.deviceNotPaired](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320693-devicenotpaired)Added [WCError.fileAccessDenied](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320697-fileaccessdenied)Added [WCError.genericError](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320704-genericerror)Added WCError.init(_nsError: NSError)Added [WCError.insufficientSpace](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320702-insufficientspace)Added [WCError.invalidParameter](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320694-invalidparameter)Added [WCError.messageReplyFailed](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320700-messagereplyfailed)Added [WCError.messageReplyTimedOut](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320706-messagereplytimedout)Added [WCError.notReachable](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320705-notreachable)Added [WCError.payloadTooLarge](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320707-payloadtoolarge)Added [WCError.payloadUnsupportedTypes](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320695-payloadunsupportedtypes)Added [WCError.sessionInactive](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320699-sessioninactive)Added [WCError.sessionMissingDelegate](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320709-sessionmissingdelegate)Added [WCError.sessionNotActivated](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320703-sessionnotactivated)Added [WCError.sessionNotSupported](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320696-sessionnotsupported)Added [WCError.transferTimedOut](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320701-transfertimedout)Added [WCError.watchAppNotInstalled](https://developer.apple.com/documentation/watchconnectivity/wcerror/2320708-watchappnotinstalled)Added [WCSession.hasContentPending](https://developer.apple.com/documentation/watchconnectivity/wcsession/1648961-hascontentpending)Added [WCSession.remainingComplicationUserInfoTransfers](https://developer.apple.com/documentation/watchconnectivity/wcsession/1771700-remainingcomplicationuserinfotra)Modified [WCError.Code [enum]](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum WCErrorCode : Int {     case GenericError     case SessionNotSupported     case SessionMissingDelegate     case SessionNotActivated     case DeviceNotPaired     case WatchAppNotInstalled     case NotReachable     case InvalidParameter     case PayloadTooLarge     case PayloadUnsupportedTypes     case MessageReplyFailed     case MessageReplyTimedOut     case FileAccessDenied     case DeliveryFailed     case InsufficientSpace     case SessionInactive     case TransferTimedOut } extension WCErrorCode : _BridgedNSError { } extension WCErrorCode : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = WCError         case genericError         case sessionNotSupported         case sessionMissingDelegate         case sessionNotActivated         case deviceNotPaired         case watchAppNotInstalled         case notReachable         case invalidParameter         case payloadTooLarge         case payloadUnsupportedTypes         case messageReplyFailed         case messageReplyTimedOut         case fileAccessDenied         case deliveryFailed         case insufficientSpace         case sessionInactive         case transferTimedOut     } ``` |

Modified [WCError.Code.deliveryFailed](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodedeliveryfailed)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case DeliveryFailed ``` | iOS 9.0 |
| To | ``` case deliveryFailed ``` | iOS 10.0 |

Modified [WCError.Code.deviceNotPaired](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/devicenotpaired)

|  | Declaration |
| --- | --- |
| From | ``` case DeviceNotPaired ``` |
| To | ``` case deviceNotPaired ``` |

Modified [WCError.Code.fileAccessDenied](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/fileaccessdenied)

|  | Declaration |
| --- | --- |
| From | ``` case FileAccessDenied ``` |
| To | ``` case fileAccessDenied ``` |

Modified [WCError.Code.genericError](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodegenericerror)

|  | Declaration |
| --- | --- |
| From | ``` case GenericError ``` |
| To | ``` case genericError ``` |

Modified [WCError.Code.insufficientSpace](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/insufficientspace)

|  | Declaration |
| --- | --- |
| From | ``` case InsufficientSpace ``` |
| To | ``` case insufficientSpace ``` |

Modified [WCError.Code.invalidParameter](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/invalidparameter)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidParameter ``` |
| To | ``` case invalidParameter ``` |

Modified [WCError.Code.messageReplyFailed](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/messagereplyfailed)

|  | Declaration |
| --- | --- |
| From | ``` case MessageReplyFailed ``` |
| To | ``` case messageReplyFailed ``` |

Modified [WCError.Code.messageReplyTimedOut](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodemessagereplytimedout)

|  | Declaration |
| --- | --- |
| From | ``` case MessageReplyTimedOut ``` |
| To | ``` case messageReplyTimedOut ``` |

Modified [WCError.Code.notReachable](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/notreachable)

|  | Declaration |
| --- | --- |
| From | ``` case NotReachable ``` |
| To | ``` case notReachable ``` |

Modified [WCError.Code.payloadTooLarge](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/payloadtoolarge)

|  | Declaration |
| --- | --- |
| From | ``` case PayloadTooLarge ``` |
| To | ``` case payloadTooLarge ``` |

Modified [WCError.Code.payloadUnsupportedTypes](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodepayloadunsupportedtypes)

|  | Declaration |
| --- | --- |
| From | ``` case PayloadUnsupportedTypes ``` |
| To | ``` case payloadUnsupportedTypes ``` |

Modified [WCError.Code.sessionInactive](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodesessioninactive)

|  | Declaration |
| --- | --- |
| From | ``` case SessionInactive ``` |
| To | ``` case sessionInactive ``` |

Modified [WCError.Code.sessionMissingDelegate](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodesessionmissingdelegate)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case SessionMissingDelegate ``` | iOS 9.0 |
| To | ``` case sessionMissingDelegate ``` | iOS 10.0 |

Modified [WCError.Code.sessionNotActivated](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodesessionnotactivated)

|  | Declaration |
| --- | --- |
| From | ``` case SessionNotActivated ``` |
| To | ``` case sessionNotActivated ``` |

Modified [WCError.Code.sessionNotSupported](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodesessionnotsupported)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case SessionNotSupported ``` | iOS 9.0 |
| To | ``` case sessionNotSupported ``` | iOS 10.0 |

Modified [WCError.Code.transferTimedOut](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/transfertimedout)

|  | Declaration |
| --- | --- |
| From | ``` case TransferTimedOut ``` |
| To | ``` case transferTimedOut ``` |

Modified [WCError.Code.watchAppNotInstalled](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodewatchappnotinstalled)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case WatchAppNotInstalled ``` | iOS 9.0 |
| To | ``` case watchAppNotInstalled ``` | iOS 10.0 |

Modified [WCSession](https://developer.apple.com/documentation/watchconnectivity/wcsession)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WCSession : NSObject {     class func isSupported() -> Bool     class func defaultSession() -> WCSession     init()     weak var delegate: WCSessionDelegate?     func activateSession()     var activationState: WCSessionActivationState { get }     var paired: Bool { get }     var watchAppInstalled: Bool { get }     var complicationEnabled: Bool { get }     var watchDirectoryURL: NSURL? { get }     var reachable: Bool { get }     var iOSDeviceNeedsUnlockAfterRebootForReachability: Bool { get }     func sendMessage(_ message: [String : AnyObject], replyHandler replyHandler: (([String : AnyObject]) -> Void)?, errorHandler errorHandler: ((NSError) -> Void)?)     func sendMessageData(_ data: NSData, replyHandler replyHandler: ((NSData) -> Void)?, errorHandler errorHandler: ((NSError) -> Void)?)     var applicationContext: [String : AnyObject] { get }     func updateApplicationContext(_ applicationContext: [String : AnyObject]) throws     var receivedApplicationContext: [String : AnyObject] { get }     func transferUserInfo(_ userInfo: [String : AnyObject]) -> WCSessionUserInfoTransfer     func transferCurrentComplicationUserInfo(_ userInfo: [String : AnyObject]) -> WCSessionUserInfoTransfer     var outstandingUserInfoTransfers: [WCSessionUserInfoTransfer] { get }     func transferFile(_ file: NSURL, metadata metadata: [String : AnyObject]?) -> WCSessionFileTransfer     var outstandingFileTransfers: [WCSessionFileTransfer] { get } } ``` | -- |
| To | ``` class WCSession : NSObject {     class func isSupported() -> Bool     class func `default`() -> WCSession     init()     weak var delegate: WCSessionDelegate?     func activate()     var activationState: WCSessionActivationState { get }     var hasContentPending: Bool { get }     var isPaired: Bool { get }     var isWatchAppInstalled: Bool { get }     var isComplicationEnabled: Bool { get }     var remainingComplicationUserInfoTransfers: Int { get }     var watchDirectoryURL: URL? { get }     var isReachable: Bool { get }     var iOSDeviceNeedsUnlockAfterRebootForReachability: Bool { get }     func sendMessage(_ message: [String : Any], replyHandler replyHandler: (@escaping ([String : Any]) -> Swift.Void)?, errorHandler errorHandler: (@escaping (Error) -> Swift.Void)? = nil)     func sendMessageData(_ data: Data, replyHandler replyHandler: (@escaping (Data) -> Swift.Void)?, errorHandler errorHandler: (@escaping (Error) -> Swift.Void)? = nil)     var applicationContext: [String : Any] { get }     func updateApplicationContext(_ applicationContext: [String : Any]) throws     var receivedApplicationContext: [String : Any] { get }     func transferUserInfo(_ userInfo: [String : Any] = [:]) -> WCSessionUserInfoTransfer     func transferCurrentComplicationUserInfo(_ userInfo: [String : Any] = [:]) -> WCSessionUserInfoTransfer     var outstandingUserInfoTransfers: [WCSessionUserInfoTransfer] { get }     func transferFile(_ file: URL, metadata metadata: [String : Any]?) -> WCSessionFileTransfer     var outstandingFileTransfers: [WCSessionFileTransfer] { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WCSession : CVarArg { } extension WCSession : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WCSession.activate()](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615655-activate)

|  | Declaration |
| --- | --- |
| From | ``` func activateSession() ``` |
| To | ``` func activate() ``` |

Modified [WCSession.applicationContext](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615643-applicationcontext)

|  | Declaration |
| --- | --- |
| From | ``` var applicationContext: [String : AnyObject] { get } ``` |
| To | ``` var applicationContext: [String : Any] { get } ``` |

Modified [WCSession.default() [class]](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615673-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultSession() -> WCSession ``` |
| To | ``` class func `default`() -> WCSession ``` |

Modified [WCSession.isComplicationEnabled](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615625-complicationenabled)

|  | Declaration |
| --- | --- |
| From | ``` var complicationEnabled: Bool { get } ``` |
| To | ``` var isComplicationEnabled: Bool { get } ``` |

Modified [WCSession.isPaired](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615665-ispaired)

|  | Declaration |
| --- | --- |
| From | ``` var paired: Bool { get } ``` |
| To | ``` var isPaired: Bool { get } ``` |

Modified [WCSession.isReachable](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615683-isreachable)

|  | Declaration |
| --- | --- |
| From | ``` var reachable: Bool { get } ``` |
| To | ``` var isReachable: Bool { get } ``` |

Modified [WCSession.isWatchAppInstalled](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615623-watchappinstalled)

|  | Declaration |
| --- | --- |
| From | ``` var watchAppInstalled: Bool { get } ``` |
| To | ``` var isWatchAppInstalled: Bool { get } ``` |

Modified [WCSession.receivedApplicationContext](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615635-receivedapplicationcontext)

|  | Declaration |
| --- | --- |
| From | ``` var receivedApplicationContext: [String : AnyObject] { get } ``` |
| To | ``` var receivedApplicationContext: [String : Any] { get } ``` |

Modified [WCSession.sendMessage(_: [String : Any], replyHandler: ( ([String : Any]) -> Swift.Void)?, errorHandler: ( (Error) -> Swift.Void)?)](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615687-sendmessage)

|  | Declaration |
| --- | --- |
| From | ``` func sendMessage(_ message: [String : AnyObject], replyHandler replyHandler: (([String : AnyObject]) -> Void)?, errorHandler errorHandler: ((NSError) -> Void)?) ``` |
| To | ``` func sendMessage(_ message: [String : Any], replyHandler replyHandler: (@escaping ([String : Any]) -> Swift.Void)?, errorHandler errorHandler: (@escaping (Error) -> Swift.Void)? = nil) ``` |

Modified [WCSession.sendMessageData(_: Data, replyHandler: ( (Data) -> Swift.Void)?, errorHandler: ( (Error) -> Swift.Void)?)](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615617-sendmessagedata)

|  | Declaration |
| --- | --- |
| From | ``` func sendMessageData(_ data: NSData, replyHandler replyHandler: ((NSData) -> Void)?, errorHandler errorHandler: ((NSError) -> Void)?) ``` |
| To | ``` func sendMessageData(_ data: Data, replyHandler replyHandler: (@escaping (Data) -> Swift.Void)?, errorHandler errorHandler: (@escaping (Error) -> Swift.Void)? = nil) ``` |

Modified [WCSession.transferCurrentComplicationUserInfo(_: [String : Any]) -> WCSessionUserInfoTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615639-transfercurrentcomplicationuseri)

|  | Declaration |
| --- | --- |
| From | ``` func transferCurrentComplicationUserInfo(_ userInfo: [String : AnyObject]) -> WCSessionUserInfoTransfer ``` |
| To | ``` func transferCurrentComplicationUserInfo(_ userInfo: [String : Any] = [:]) -> WCSessionUserInfoTransfer ``` |

Modified [WCSession.transferFile(_: URL, metadata: [String : Any]?) -> WCSessionFileTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615667-transferfile)

|  | Declaration |
| --- | --- |
| From | ``` func transferFile(_ file: NSURL, metadata metadata: [String : AnyObject]?) -> WCSessionFileTransfer ``` |
| To | ``` func transferFile(_ file: URL, metadata metadata: [String : Any]?) -> WCSessionFileTransfer ``` |

Modified [WCSession.transferUserInfo(_: [String : Any]) -> WCSessionUserInfoTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615671-transferuserinfo)

|  | Declaration |
| --- | --- |
| From | ``` func transferUserInfo(_ userInfo: [String : AnyObject]) -> WCSessionUserInfoTransfer ``` |
| To | ``` func transferUserInfo(_ userInfo: [String : Any] = [:]) -> WCSessionUserInfoTransfer ``` |

Modified [WCSession.updateApplicationContext(_: [String : Any]) throws](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615621-updateapplicationcontext)

|  | Declaration |
| --- | --- |
| From | ``` func updateApplicationContext(_ applicationContext: [String : AnyObject]) throws ``` |
| To | ``` func updateApplicationContext(_ applicationContext: [String : Any]) throws ``` |

Modified [WCSession.watchDirectoryURL](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615645-watchdirectoryurl)

|  | Declaration |
| --- | --- |
| From | ``` var watchDirectoryURL: NSURL? { get } ``` |
| To | ``` var watchDirectoryURL: URL? { get } ``` |

Modified [WCSessionActivationState [enum]](https://developer.apple.com/documentation/watchconnectivity/wcsessionactivationstate)

|  | Declaration |
| --- | --- |
| From | ``` enum WCSessionActivationState : Int {     case NotActivated     case Inactive     case Activated } ``` |
| To | ``` enum WCSessionActivationState : Int {     case notActivated     case inactive     case activated } ``` |

Modified [WCSessionActivationState.activated](https://developer.apple.com/documentation/watchconnectivity/wcsessionactivationstate/wcsessionactivationstateactivated)

|  | Declaration |
| --- | --- |
| From | ``` case Activated ``` |
| To | ``` case activated ``` |

Modified [WCSessionActivationState.inactive](https://developer.apple.com/documentation/watchconnectivity/wcsessionactivationstate/wcsessionactivationstateinactive)

|  | Declaration |
| --- | --- |
| From | ``` case Inactive ``` |
| To | ``` case inactive ``` |

Modified [WCSessionActivationState.notActivated](https://developer.apple.com/documentation/watchconnectivity/wcsessionactivationstate/wcsessionactivationstatenotactivated)

|  | Declaration |
| --- | --- |
| From | ``` case NotActivated ``` |
| To | ``` case notActivated ``` |

Modified [WCSessionDelegate](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol WCSessionDelegate : NSObjectProtocol {     optional func session(_ session: WCSession, activationDidCompleteWithState activationState: WCSessionActivationState, error error: NSError?)     optional func sessionDidBecomeInactive(_ session: WCSession)     optional func sessionDidDeactivate(_ session: WCSession)     optional func sessionWatchStateDidChange(_ session: WCSession)     optional func sessionReachabilityDidChange(_ session: WCSession)     optional func session(_ session: WCSession, didReceiveMessage message: [String : AnyObject])     optional func session(_ session: WCSession, didReceiveMessage message: [String : AnyObject], replyHandler replyHandler: ([String : AnyObject]) -> Void)     optional func session(_ session: WCSession, didReceiveMessageData messageData: NSData)     optional func session(_ session: WCSession, didReceiveMessageData messageData: NSData, replyHandler replyHandler: (NSData) -> Void)     optional func session(_ session: WCSession, didReceiveApplicationContext applicationContext: [String : AnyObject])     optional func session(_ session: WCSession, didFinishUserInfoTransfer userInfoTransfer: WCSessionUserInfoTransfer, error error: NSError?)     optional func session(_ session: WCSession, didReceiveUserInfo userInfo: [String : AnyObject])     optional func session(_ session: WCSession, didFinishFileTransfer fileTransfer: WCSessionFileTransfer, error error: NSError?)     optional func session(_ session: WCSession, didReceiveFile file: WCSessionFile) } ``` |
| To | ``` protocol WCSessionDelegate : NSObjectProtocol {     func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error error: Error?)     func sessionDidBecomeInactive(_ session: WCSession)     func sessionDidDeactivate(_ session: WCSession)     optional func sessionWatchStateDidChange(_ session: WCSession)     optional func sessionReachabilityDidChange(_ session: WCSession)     optional func session(_ session: WCSession, didReceiveMessage message: [String : Any])     optional func session(_ session: WCSession, didReceiveMessage message: [String : Any], replyHandler replyHandler: @escaping ([String : Any]) -> Swift.Void)     optional func session(_ session: WCSession, didReceiveMessageData messageData: Data)     optional func session(_ session: WCSession, didReceiveMessageData messageData: Data, replyHandler replyHandler: @escaping (Data) -> Swift.Void)     optional func session(_ session: WCSession, didReceiveApplicationContext applicationContext: [String : Any])     optional func session(_ session: WCSession, didFinish userInfoTransfer: WCSessionUserInfoTransfer, error error: Error?)     optional func session(_ session: WCSession, didReceiveUserInfo userInfo: [String : Any] = [:])     optional func session(_ session: WCSession, didFinish fileTransfer: WCSessionFileTransfer, error error: Error?)     optional func session(_ session: WCSession, didReceive file: WCSessionFile) } ``` |

Modified [WCSessionDelegate.session(_: WCSession, activationDidCompleteWith: WCSessionActivationState, error: Error?)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615679-session)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func session(_ session: WCSession, activationDidCompleteWithState activationState: WCSessionActivationState, error error: NSError?) ``` | yes |
| To | ``` func session(_ session: WCSession, activationDidCompleteWith activationState: WCSessionActivationState, error error: Error?) ``` | -- |

Modified [WCSessionDelegate.session(_: WCSession, didFinish: WCSessionFileTransfer, error: Error?)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615657-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: WCSession, didFinishFileTransfer fileTransfer: WCSessionFileTransfer, error error: NSError?) ``` |
| To | ``` optional func session(_ session: WCSession, didFinish fileTransfer: WCSessionFileTransfer, error error: Error?) ``` |

Modified [WCSessionDelegate.session(_: WCSession, didFinish: WCSessionUserInfoTransfer, error: Error?)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615668-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: WCSession, didFinishUserInfoTransfer userInfoTransfer: WCSessionUserInfoTransfer, error error: NSError?) ``` |
| To | ``` optional func session(_ session: WCSession, didFinish userInfoTransfer: WCSessionUserInfoTransfer, error error: Error?) ``` |

Modified [WCSessionDelegate.session(_: WCSession, didReceive: WCSessionFile)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615651-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: WCSession, didReceiveFile file: WCSessionFile) ``` |
| To | ``` optional func session(_ session: WCSession, didReceive file: WCSessionFile) ``` |

Modified [WCSessionDelegate.session(_: WCSession, didReceiveApplicationContext: [String : Any])](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615619-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: WCSession, didReceiveApplicationContext applicationContext: [String : AnyObject]) ``` |
| To | ``` optional func session(_ session: WCSession, didReceiveApplicationContext applicationContext: [String : Any]) ``` |

Modified [WCSessionDelegate.session(_: WCSession, didReceiveMessage: [String : Any])](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615637-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: WCSession, didReceiveMessage message: [String : AnyObject]) ``` |
| To | ``` optional func session(_ session: WCSession, didReceiveMessage message: [String : Any]) ``` |

Modified [WCSessionDelegate.session(_: WCSession, didReceiveMessage: [String : Any], replyHandler: ([String : Any]) -> Swift.Void)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615677-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: WCSession, didReceiveMessage message: [String : AnyObject], replyHandler replyHandler: ([String : AnyObject]) -> Void) ``` |
| To | ``` optional func session(_ session: WCSession, didReceiveMessage message: [String : Any], replyHandler replyHandler: @escaping ([String : Any]) -> Swift.Void) ``` |

Modified [WCSessionDelegate.session(_: WCSession, didReceiveMessageData: Data)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615686-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: WCSession, didReceiveMessageData messageData: NSData) ``` |
| To | ``` optional func session(_ session: WCSession, didReceiveMessageData messageData: Data) ``` |

Modified [WCSessionDelegate.session(_: WCSession, didReceiveMessageData: Data, replyHandler: (Data) -> Swift.Void)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615653-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: WCSession, didReceiveMessageData messageData: NSData, replyHandler replyHandler: (NSData) -> Void) ``` |
| To | ``` optional func session(_ session: WCSession, didReceiveMessageData messageData: Data, replyHandler replyHandler: @escaping (Data) -> Swift.Void) ``` |

Modified [WCSessionDelegate.session()](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615633-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: WCSession, didReceiveUserInfo userInfo: [String : AnyObject]) ``` |
| To | ``` optional func session(_ session: WCSession, didReceiveUserInfo userInfo: [String : Any] = [:]) ``` |

Modified [WCSessionDelegate.sessionDidBecomeInactive(_: WCSession)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615684-sessiondidbecomeinactive)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func sessionDidBecomeInactive(_ session: WCSession) ``` | yes |
| To | ``` func sessionDidBecomeInactive(_ session: WCSession) ``` | -- |

Modified [WCSessionDelegate.sessionDidDeactivate(_: WCSession)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615670-sessiondiddeactivate)

|  | Declaration | Optional |
| --- | --- | --- |
| From | ``` optional func sessionDidDeactivate(_ session: WCSession) ``` | yes |
| To | ``` func sessionDidDeactivate(_ session: WCSession) ``` | -- |

Modified [WCSessionFile](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WCSessionFile : NSObject {     var fileURL: NSURL { get }     var metadata: [String : AnyObject]? { get } } ``` | -- |
| To | ``` class WCSessionFile : NSObject {     var fileURL: URL { get }     var metadata: [String : Any]? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WCSessionFile : CVarArg { } extension WCSessionFile : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WCSessionFile.fileURL](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile/1622170-fileurl)

|  | Declaration |
| --- | --- |
| From | ``` var fileURL: NSURL { get } ``` |
| To | ``` var fileURL: URL { get } ``` |

Modified [WCSessionFile.metadata](https://developer.apple.com/documentation/watchconnectivity/wcsessionfile/1622172-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: [String : AnyObject]? { get } ``` |
| To | ``` var metadata: [String : Any]? { get } ``` |

Modified [WCSessionFileTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WCSessionFileTransfer : NSObject {     var file: WCSessionFile { get }     var transferring: Bool { get }     func cancel() } ``` | -- |
| To | ``` class WCSessionFileTransfer : NSObject {     var file: WCSessionFile { get }     var isTransferring: Bool { get }     func cancel()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WCSessionFileTransfer : CVarArg { } extension WCSessionFileTransfer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WCSessionFileTransfer.isTransferring](https://developer.apple.com/documentation/watchconnectivity/wcsessionfiletransfer/1622167-istransferring)

|  | Declaration |
| --- | --- |
| From | ``` var transferring: Bool { get } ``` |
| To | ``` var isTransferring: Bool { get } ``` |

Modified [WCSessionUserInfoTransfer](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WCSessionUserInfoTransfer : NSObject, NSSecureCoding {     var currentComplicationInfo: Bool { get }     var userInfo: [String : AnyObject] { get }     var transferring: Bool { get }     func cancel() } ``` | NSSecureCoding |
| To | ``` class WCSessionUserInfoTransfer : NSObject, NSSecureCoding {     var isCurrentComplicationInfo: Bool { get }     var userInfo: [String : Any] { get }     var isTransferring: Bool { get }     func cancel()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WCSessionUserInfoTransfer : CVarArg { } extension WCSessionUserInfoTransfer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [WCSessionUserInfoTransfer.isCurrentComplicationInfo](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/1623891-currentcomplicationinfo)

|  | Declaration |
| --- | --- |
| From | ``` var currentComplicationInfo: Bool { get } ``` |
| To | ``` var isCurrentComplicationInfo: Bool { get } ``` |

Modified [WCSessionUserInfoTransfer.isTransferring](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/1623892-transferring)

|  | Declaration |
| --- | --- |
| From | ``` var transferring: Bool { get } ``` |
| To | ``` var isTransferring: Bool { get } ``` |

Modified [WCSessionUserInfoTransfer.userInfo](https://developer.apple.com/documentation/watchconnectivity/wcsessionuserinfotransfer/1623888-userinfo)

|  | Declaration |
| --- | --- |
| From | ``` var userInfo: [String : AnyObject] { get } ``` |
| To | ``` var userInfo: [String : Any] { get } ``` |

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
