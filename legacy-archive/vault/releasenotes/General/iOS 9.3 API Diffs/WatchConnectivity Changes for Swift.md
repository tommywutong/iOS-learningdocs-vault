---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/WatchConnectivity.html
archived_at: '2026-07-18T02:57:17.028582Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# WatchConnectivity Changes for Swift

### WatchConnectivity

Added [WCErrorCode.SessionInactive](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode/wcerrorcodesessioninactive)Added [WCErrorCode.TransferTimedOut](https://developer.apple.com/documentation/watchconnectivity/wcerror/code/transfertimedout)Added [WCSession.activationState](https://developer.apple.com/documentation/watchconnectivity/wcsession/1615663-activationstate)Added [WCSessionActivationState [enum]](https://developer.apple.com/documentation/watchconnectivity/wcsessionactivationstate)Added [WCSessionActivationState.Activated](https://developer.apple.com/documentation/watchconnectivity/wcsessionactivationstate/wcsessionactivationstateactivated)Added [WCSessionActivationState.Inactive](https://developer.apple.com/documentation/watchconnectivity/wcsessionactivationstate/wcsessionactivationstateinactive)Added [WCSessionActivationState.NotActivated](https://developer.apple.com/documentation/watchconnectivity/wcsessionactivationstate/wcsessionactivationstatenotactivated)Added [WCSessionDelegate.session(_: WCSession, activationDidCompleteWithState: WCSessionActivationState, error: NSError?)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615679-session)Added [WCSessionDelegate.sessionDidBecomeInactive(_: WCSession)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615684-sessiondidbecomeinactive)Added [WCSessionDelegate.sessionDidDeactivate(_: WCSession)](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/1615670-sessiondiddeactivate)Modified [WCErrorCode [enum]](https://developer.apple.com/documentation/watchconnectivity/wcerrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum WCErrorCode : Int {     case GenericError     case SessionNotSupported     case SessionMissingDelegate     case SessionNotActivated     case DeviceNotPaired     case WatchAppNotInstalled     case NotReachable     case InvalidParameter     case PayloadTooLarge     case PayloadUnsupportedTypes     case MessageReplyFailed     case MessageReplyTimedOut     case FileAccessDenied     case DeliveryFailed     case InsufficientSpace } extension WCErrorCode : _BridgedNSError { } extension WCErrorCode : _BridgedNSError { } ``` |
| To | ``` enum WCErrorCode : Int {     case GenericError     case SessionNotSupported     case SessionMissingDelegate     case SessionNotActivated     case DeviceNotPaired     case WatchAppNotInstalled     case NotReachable     case InvalidParameter     case PayloadTooLarge     case PayloadUnsupportedTypes     case MessageReplyFailed     case MessageReplyTimedOut     case FileAccessDenied     case DeliveryFailed     case InsufficientSpace     case SessionInactive     case TransferTimedOut } extension WCErrorCode : _BridgedNSError { } extension WCErrorCode : _BridgedNSError { } ``` |

Modified [WCSession](https://developer.apple.com/documentation/watchconnectivity/wcsession)

|  | Declaration |
| --- | --- |
| From | ``` class WCSession : NSObject {     class func isSupported() -> Bool     class func defaultSession() -> WCSession     init()     weak var delegate: WCSessionDelegate?     func activateSession()     var paired: Bool { get }     var watchAppInstalled: Bool { get }     var complicationEnabled: Bool { get }     var watchDirectoryURL: NSURL? { get }     var reachable: Bool { get }     var iOSDeviceNeedsUnlockAfterRebootForReachability: Bool { get }     func sendMessage(_ message: [String : AnyObject], replyHandler replyHandler: (([String : AnyObject]) -> Void)?, errorHandler errorHandler: ((NSError) -> Void)?)     func sendMessageData(_ data: NSData, replyHandler replyHandler: ((NSData) -> Void)?, errorHandler errorHandler: ((NSError) -> Void)?)     var applicationContext: [String : AnyObject] { get }     func updateApplicationContext(_ applicationContext: [String : AnyObject]) throws     var receivedApplicationContext: [String : AnyObject] { get }     func transferUserInfo(_ userInfo: [String : AnyObject]) -> WCSessionUserInfoTransfer     func transferCurrentComplicationUserInfo(_ userInfo: [String : AnyObject]) -> WCSessionUserInfoTransfer     var outstandingUserInfoTransfers: [WCSessionUserInfoTransfer] { get }     func transferFile(_ file: NSURL, metadata metadata: [String : AnyObject]?) -> WCSessionFileTransfer     var outstandingFileTransfers: [WCSessionFileTransfer] { get } } ``` |
| To | ``` class WCSession : NSObject {     class func isSupported() -> Bool     class func defaultSession() -> WCSession     init()     weak var delegate: WCSessionDelegate?     func activateSession()     var activationState: WCSessionActivationState { get }     var paired: Bool { get }     var watchAppInstalled: Bool { get }     var complicationEnabled: Bool { get }     var watchDirectoryURL: NSURL? { get }     var reachable: Bool { get }     var iOSDeviceNeedsUnlockAfterRebootForReachability: Bool { get }     func sendMessage(_ message: [String : AnyObject], replyHandler replyHandler: (([String : AnyObject]) -> Void)?, errorHandler errorHandler: ((NSError) -> Void)?)     func sendMessageData(_ data: NSData, replyHandler replyHandler: ((NSData) -> Void)?, errorHandler errorHandler: ((NSError) -> Void)?)     var applicationContext: [String : AnyObject] { get }     func updateApplicationContext(_ applicationContext: [String : AnyObject]) throws     var receivedApplicationContext: [String : AnyObject] { get }     func transferUserInfo(_ userInfo: [String : AnyObject]) -> WCSessionUserInfoTransfer     func transferCurrentComplicationUserInfo(_ userInfo: [String : AnyObject]) -> WCSessionUserInfoTransfer     var outstandingUserInfoTransfers: [WCSessionUserInfoTransfer] { get }     func transferFile(_ file: NSURL, metadata metadata: [String : AnyObject]?) -> WCSessionFileTransfer     var outstandingFileTransfers: [WCSessionFileTransfer] { get } } ``` |

Modified [WCSessionDelegate](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol WCSessionDelegate : NSObjectProtocol {     optional func sessionWatchStateDidChange(_ session: WCSession)     optional func sessionReachabilityDidChange(_ session: WCSession)     optional func session(_ session: WCSession, didReceiveMessage message: [String : AnyObject])     optional func session(_ session: WCSession, didReceiveMessage message: [String : AnyObject], replyHandler replyHandler: ([String : AnyObject]) -> Void)     optional func session(_ session: WCSession, didReceiveMessageData messageData: NSData)     optional func session(_ session: WCSession, didReceiveMessageData messageData: NSData, replyHandler replyHandler: (NSData) -> Void)     optional func session(_ session: WCSession, didReceiveApplicationContext applicationContext: [String : AnyObject])     optional func session(_ session: WCSession, didFinishUserInfoTransfer userInfoTransfer: WCSessionUserInfoTransfer, error error: NSError?)     optional func session(_ session: WCSession, didReceiveUserInfo userInfo: [String : AnyObject])     optional func session(_ session: WCSession, didFinishFileTransfer fileTransfer: WCSessionFileTransfer, error error: NSError?)     optional func session(_ session: WCSession, didReceiveFile file: WCSessionFile) } ``` |
| To | ``` protocol WCSessionDelegate : NSObjectProtocol {     optional func session(_ session: WCSession, activationDidCompleteWithState activationState: WCSessionActivationState, error error: NSError?)     optional func sessionDidBecomeInactive(_ session: WCSession)     optional func sessionDidDeactivate(_ session: WCSession)     optional func sessionWatchStateDidChange(_ session: WCSession)     optional func sessionReachabilityDidChange(_ session: WCSession)     optional func session(_ session: WCSession, didReceiveMessage message: [String : AnyObject])     optional func session(_ session: WCSession, didReceiveMessage message: [String : AnyObject], replyHandler replyHandler: ([String : AnyObject]) -> Void)     optional func session(_ session: WCSession, didReceiveMessageData messageData: NSData)     optional func session(_ session: WCSession, didReceiveMessageData messageData: NSData, replyHandler replyHandler: (NSData) -> Void)     optional func session(_ session: WCSession, didReceiveApplicationContext applicationContext: [String : AnyObject])     optional func session(_ session: WCSession, didFinishUserInfoTransfer userInfoTransfer: WCSessionUserInfoTransfer, error error: NSError?)     optional func session(_ session: WCSession, didReceiveUserInfo userInfo: [String : AnyObject])     optional func session(_ session: WCSession, didFinishFileTransfer fileTransfer: WCSessionFileTransfer, error error: NSError?)     optional func session(_ session: WCSession, didReceiveFile file: WCSessionFile) } ``` |

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
