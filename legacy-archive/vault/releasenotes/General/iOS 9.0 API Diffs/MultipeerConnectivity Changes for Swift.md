---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/MultipeerConnectivity.html
archived_at: '2026-07-18T02:56:55.876183Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# MultipeerConnectivity Changes for Swift

### MultipeerConnectivity

Modified [MCAdvertiserAssistant](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant)

|  | Declaration |
| --- | --- |
| From | ``` class MCAdvertiserAssistant : NSObject {     init!(serviceType serviceType: String!, discoveryInfo info: [NSObject : AnyObject]!, session session: MCSession!)     func start()     func stop()     weak var delegate: MCAdvertiserAssistantDelegate!     var session: MCSession! { get }     var discoveryInfo: [NSObject : AnyObject]! { get }     var serviceType: String! { get } } ``` |
| To | ``` class MCAdvertiserAssistant : NSObject {     init(serviceType serviceType: String, discoveryInfo info: [String : String]?, session session: MCSession)     func start()     func stop()     weak var delegate: MCAdvertiserAssistantDelegate?     var session: MCSession { get }     var discoveryInfo: [String : String]? { get }     var serviceType: String { get } } ``` |

Modified [MCAdvertiserAssistant.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407041-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: MCAdvertiserAssistantDelegate! ``` |
| To | ``` weak var delegate: MCAdvertiserAssistantDelegate? ``` |

Modified [MCAdvertiserAssistant.discoveryInfo](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406952-discoveryinfo)

|  | Declaration |
| --- | --- |
| From | ``` var discoveryInfo: [NSObject : AnyObject]! { get } ``` |
| To | ``` var discoveryInfo: [String : String]? { get } ``` |

Modified [MCAdvertiserAssistant.init(serviceType: String, discoveryInfo: [String : String]?, session: MCSession)](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406990-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(serviceType serviceType: String!, discoveryInfo info: [NSObject : AnyObject]!, session session: MCSession!) ``` |
| To | ``` init(serviceType serviceType: String, discoveryInfo info: [String : String]?, session session: MCSession) ``` |

Modified [MCAdvertiserAssistant.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407062-servicetype)

|  | Declaration |
| --- | --- |
| From | ``` var serviceType: String! { get } ``` |
| To | ``` var serviceType: String { get } ``` |

Modified [MCAdvertiserAssistant.session](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406924-session)

|  | Declaration |
| --- | --- |
| From | ``` var session: MCSession! { get } ``` |
| To | ``` var session: MCSession { get } ``` |

Modified [MCAdvertiserAssistantDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MCAdvertiserAssistantDelegate : NSObjectProtocol {     optional func advertiserAssistantWillPresentInvitation(_ advertiserAssistant: MCAdvertiserAssistant!)     optional func advertiserAssistantDidDismissInvitation(_ advertiserAssistant: MCAdvertiserAssistant!) } ``` |
| To | ``` protocol MCAdvertiserAssistantDelegate : NSObjectProtocol {     optional func advertiserAssistantWillPresentInvitation(_ advertiserAssistant: MCAdvertiserAssistant)     optional func advertiserAssistantDidDismissInvitation(_ advertiserAssistant: MCAdvertiserAssistant) } ``` |

Modified [MCAdvertiserAssistantDelegate.advertiserAssistantDidDismissInvitation(_: MCAdvertiserAssistant)](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1406922-advertiserassistantdiddismissinv)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func advertiserAssistantDidDismissInvitation(_ advertiserAssistant: MCAdvertiserAssistant!) ``` | iOS 8.0 |
| To | ``` optional func advertiserAssistantDidDismissInvitation(_ advertiserAssistant: MCAdvertiserAssistant) ``` | iOS 7.0 |

Modified [MCAdvertiserAssistantDelegate.advertiserAssistantWillPresentInvitation(_: MCAdvertiserAssistant)](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1406978-advertiserassistantwillpresentin)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func advertiserAssistantWillPresentInvitation(_ advertiserAssistant: MCAdvertiserAssistant!) ``` | iOS 8.0 |
| To | ``` optional func advertiserAssistantWillPresentInvitation(_ advertiserAssistant: MCAdvertiserAssistant) ``` | iOS 7.0 |

Modified [MCBrowserViewController](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class MCBrowserViewController : UIViewController, MCNearbyServiceBrowserDelegate, NSObjectProtocol {     convenience init!(serviceType serviceType: String!, session session: MCSession!)     init!(browser browser: MCNearbyServiceBrowser!, session session: MCSession!)     weak var delegate: MCBrowserViewControllerDelegate!     var browser: MCNearbyServiceBrowser! { get }     var session: MCSession! { get }     var minimumNumberOfPeers: Int     var maximumNumberOfPeers: Int } ``` |
| To | ``` class MCBrowserViewController : UIViewController, MCNearbyServiceBrowserDelegate {     convenience init(serviceType serviceType: String, session session: MCSession)     init(browser browser: MCNearbyServiceBrowser, session session: MCSession)     weak var delegate: MCBrowserViewControllerDelegate?     var browser: MCNearbyServiceBrowser? { get }     var session: MCSession { get }     var minimumNumberOfPeers: Int     var maximumNumberOfPeers: Int } ``` |

Modified [MCBrowserViewController.browser](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406969-browser)

|  | Declaration |
| --- | --- |
| From | ``` var browser: MCNearbyServiceBrowser! { get } ``` |
| To | ``` var browser: MCNearbyServiceBrowser? { get } ``` |

Modified [MCBrowserViewController.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406982-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: MCBrowserViewControllerDelegate! ``` |
| To | ``` weak var delegate: MCBrowserViewControllerDelegate? ``` |

Modified [MCBrowserViewController.init(browser: MCNearbyServiceBrowser, session: MCSession)](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406963-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(browser browser: MCNearbyServiceBrowser!, session session: MCSession!) ``` |
| To | ``` init(browser browser: MCNearbyServiceBrowser, session session: MCSession) ``` |

Modified [MCBrowserViewController.init(serviceType: String, session: MCSession)](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406915-initwithservicetype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(serviceType serviceType: String!, session session: MCSession!) ``` |
| To | ``` convenience init(serviceType serviceType: String, session session: MCSession) ``` |

Modified [MCBrowserViewController.session](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406976-session)

|  | Declaration |
| --- | --- |
| From | ``` var session: MCSession! { get } ``` |
| To | ``` var session: MCSession { get } ``` |

Modified [MCBrowserViewControllerDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MCBrowserViewControllerDelegate : NSObjectProtocol {     func browserViewControllerDidFinish(_ browserViewController: MCBrowserViewController!)     func browserViewControllerWasCancelled(_ browserViewController: MCBrowserViewController!)     optional func browserViewController(_ browserViewController: MCBrowserViewController!, shouldPresentNearbyPeer peerID: MCPeerID!, withDiscoveryInfo info: [NSObject : AnyObject]!) -> Bool } ``` |
| To | ``` protocol MCBrowserViewControllerDelegate : NSObjectProtocol {     func browserViewControllerDidFinish(_ browserViewController: MCBrowserViewController)     func browserViewControllerWasCancelled(_ browserViewController: MCBrowserViewController)     optional func browserViewController(_ browserViewController: MCBrowserViewController, shouldPresentNearbyPeer peerID: MCPeerID, withDiscoveryInfo info: [String : String]?) -> Bool } ``` |

Modified [MCBrowserViewControllerDelegate.browserViewController(_: MCBrowserViewController, shouldPresentNearbyPeer: MCPeerID, withDiscoveryInfo: [String : String]?) -> Bool](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1407039-browserviewcontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func browserViewController(_ browserViewController: MCBrowserViewController!, shouldPresentNearbyPeer peerID: MCPeerID!, withDiscoveryInfo info: [NSObject : AnyObject]!) -> Bool ``` | iOS 8.0 |
| To | ``` optional func browserViewController(_ browserViewController: MCBrowserViewController, shouldPresentNearbyPeer peerID: MCPeerID, withDiscoveryInfo info: [String : String]?) -> Bool ``` | iOS 7.0 |

Modified [MCBrowserViewControllerDelegate.browserViewControllerDidFinish(_: MCBrowserViewController)](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1407002-browserviewcontrollerdidfinish)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func browserViewControllerDidFinish(_ browserViewController: MCBrowserViewController!) ``` | iOS 8.0 |
| To | ``` func browserViewControllerDidFinish(_ browserViewController: MCBrowserViewController) ``` | iOS 7.0 |

Modified [MCBrowserViewControllerDelegate.browserViewControllerWasCancelled(_: MCBrowserViewController)](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1406942-browserviewcontrollerwascancelle)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func browserViewControllerWasCancelled(_ browserViewController: MCBrowserViewController!) ``` | iOS 8.0 |
| To | ``` func browserViewControllerWasCancelled(_ browserViewController: MCBrowserViewController) ``` | iOS 7.0 |

Modified [MCEncryptionPreference [enum]](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [MCErrorCode [enum]](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum MCErrorCode : Int {     case Unknown     case NotConnected     case InvalidParameter     case Unsupported     case TimedOut     case Cancelled     case Unavailable } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum MCErrorCode : Int {     case Unknown     case NotConnected     case InvalidParameter     case Unsupported     case TimedOut     case Cancelled     case Unavailable } extension MCErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension MCErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [MCNearbyServiceAdvertiser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser)

|  | Declaration |
| --- | --- |
| From | ``` class MCNearbyServiceAdvertiser : NSObject {     init!(peer myPeerID: MCPeerID!, discoveryInfo info: [NSObject : AnyObject]!, serviceType serviceType: String!)     func startAdvertisingPeer()     func stopAdvertisingPeer()     weak var delegate: MCNearbyServiceAdvertiserDelegate!     var myPeerID: MCPeerID! { get }     var discoveryInfo: [NSObject : AnyObject]! { get }     var serviceType: String! { get } } ``` |
| To | ``` class MCNearbyServiceAdvertiser : NSObject {     init(peer myPeerID: MCPeerID, discoveryInfo info: [String : String]?, serviceType serviceType: String)     func startAdvertisingPeer()     func stopAdvertisingPeer()     weak var delegate: MCNearbyServiceAdvertiserDelegate?     var myPeerID: MCPeerID { get }     var discoveryInfo: [String : String]? { get }     var serviceType: String { get } } ``` |

Modified [MCNearbyServiceAdvertiser.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407031-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: MCNearbyServiceAdvertiserDelegate! ``` |
| To | ``` weak var delegate: MCNearbyServiceAdvertiserDelegate? ``` |

Modified [MCNearbyServiceAdvertiser.discoveryInfo](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1406967-discoveryinfo)

|  | Declaration |
| --- | --- |
| From | ``` var discoveryInfo: [NSObject : AnyObject]! { get } ``` |
| To | ``` var discoveryInfo: [String : String]? { get } ``` |

Modified [MCNearbyServiceAdvertiser.init(peer: MCPeerID, discoveryInfo: [String : String]?, serviceType: String)](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407102-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(peer myPeerID: MCPeerID!, discoveryInfo info: [NSObject : AnyObject]!, serviceType serviceType: String!) ``` |
| To | ``` init(peer myPeerID: MCPeerID, discoveryInfo info: [String : String]?, serviceType serviceType: String) ``` |

Modified [MCNearbyServiceAdvertiser.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407022-mypeerid)

|  | Declaration |
| --- | --- |
| From | ``` var myPeerID: MCPeerID! { get } ``` |
| To | ``` var myPeerID: MCPeerID { get } ``` |

Modified [MCNearbyServiceAdvertiser.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407108-servicetype)

|  | Declaration |
| --- | --- |
| From | ``` var serviceType: String! { get } ``` |
| To | ``` var serviceType: String { get } ``` |

Modified [MCNearbyServiceAdvertiserDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MCNearbyServiceAdvertiserDelegate : NSObjectProtocol {     func advertiser(_ advertiser: MCNearbyServiceAdvertiser!, didReceiveInvitationFromPeer peerID: MCPeerID!, withContext context: NSData!, invitationHandler invitationHandler: ((Bool, MCSession!) -> Void)!)     optional func advertiser(_ advertiser: MCNearbyServiceAdvertiser!, didNotStartAdvertisingPeer error: NSError!) } ``` |
| To | ``` protocol MCNearbyServiceAdvertiserDelegate : NSObjectProtocol {     func advertiser(_ advertiser: MCNearbyServiceAdvertiser, didReceiveInvitationFromPeer peerID: MCPeerID, withContext context: NSData?, invitationHandler invitationHandler: (Bool, MCSession) -> Void)     optional func advertiser(_ advertiser: MCNearbyServiceAdvertiser, didNotStartAdvertisingPeer error: NSError) } ``` |

Modified [MCNearbyServiceAdvertiserDelegate.advertiser(_: MCNearbyServiceAdvertiser, didNotStartAdvertisingPeer: NSError)](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/1407100-advertiser)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func advertiser(_ advertiser: MCNearbyServiceAdvertiser!, didNotStartAdvertisingPeer error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func advertiser(_ advertiser: MCNearbyServiceAdvertiser, didNotStartAdvertisingPeer error: NSError) ``` | iOS 7.0 |

Modified [MCNearbyServiceAdvertiserDelegate.advertiser(_: MCNearbyServiceAdvertiser, didReceiveInvitationFromPeer: MCPeerID, withContext: NSData?, invitationHandler: (Bool, MCSession) -> Void)](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/1406971-advertiser)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advertiser(_ advertiser: MCNearbyServiceAdvertiser!, didReceiveInvitationFromPeer peerID: MCPeerID!, withContext context: NSData!, invitationHandler invitationHandler: ((Bool, MCSession!) -> Void)!) ``` | iOS 8.0 |
| To | ``` func advertiser(_ advertiser: MCNearbyServiceAdvertiser, didReceiveInvitationFromPeer peerID: MCPeerID, withContext context: NSData?, invitationHandler invitationHandler: (Bool, MCSession) -> Void) ``` | iOS 7.0 |

Modified [MCNearbyServiceBrowser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser)

|  | Declaration |
| --- | --- |
| From | ``` class MCNearbyServiceBrowser : NSObject {     init!(peer myPeerID: MCPeerID!, serviceType serviceType: String!)     func startBrowsingForPeers()     func stopBrowsingForPeers()     func invitePeer(_ peerID: MCPeerID!, toSession session: MCSession!, withContext context: NSData!, timeout timeout: NSTimeInterval)     weak var delegate: MCNearbyServiceBrowserDelegate!     var myPeerID: MCPeerID! { get }     var serviceType: String! { get } } ``` |
| To | ``` class MCNearbyServiceBrowser : NSObject {     init(peer myPeerID: MCPeerID, serviceType serviceType: String)     func startBrowsingForPeers()     func stopBrowsingForPeers()     func invitePeer(_ peerID: MCPeerID, toSession session: MCSession, withContext context: NSData?, timeout timeout: NSTimeInterval)     weak var delegate: MCNearbyServiceBrowserDelegate?     var myPeerID: MCPeerID { get }     var serviceType: String { get } } ``` |

Modified [MCNearbyServiceBrowser.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407079-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: MCNearbyServiceBrowserDelegate! ``` |
| To | ``` weak var delegate: MCNearbyServiceBrowserDelegate? ``` |

Modified [MCNearbyServiceBrowser.init(peer: MCPeerID, serviceType: String)](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407094-initwithpeer)

|  | Declaration |
| --- | --- |
| From | ``` init!(peer myPeerID: MCPeerID!, serviceType serviceType: String!) ``` |
| To | ``` init(peer myPeerID: MCPeerID, serviceType serviceType: String) ``` |

Modified [MCNearbyServiceBrowser.invitePeer(_: MCPeerID, toSession: MCSession, withContext: NSData?, timeout: NSTimeInterval)](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1406944-invitepeer)

|  | Declaration |
| --- | --- |
| From | ``` func invitePeer(_ peerID: MCPeerID!, toSession session: MCSession!, withContext context: NSData!, timeout timeout: NSTimeInterval) ``` |
| To | ``` func invitePeer(_ peerID: MCPeerID, toSession session: MCSession, withContext context: NSData?, timeout timeout: NSTimeInterval) ``` |

Modified [MCNearbyServiceBrowser.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407050-mypeerid)

|  | Declaration |
| --- | --- |
| From | ``` var myPeerID: MCPeerID! { get } ``` |
| To | ``` var myPeerID: MCPeerID { get } ``` |

Modified [MCNearbyServiceBrowser.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407110-servicetype)

|  | Declaration |
| --- | --- |
| From | ``` var serviceType: String! { get } ``` |
| To | ``` var serviceType: String { get } ``` |

Modified [MCNearbyServiceBrowserDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MCNearbyServiceBrowserDelegate : NSObjectProtocol {     func browser(_ browser: MCNearbyServiceBrowser!, foundPeer peerID: MCPeerID!, withDiscoveryInfo info: [NSObject : AnyObject]!)     func browser(_ browser: MCNearbyServiceBrowser!, lostPeer peerID: MCPeerID!)     optional func browser(_ browser: MCNearbyServiceBrowser!, didNotStartBrowsingForPeers error: NSError!) } ``` |
| To | ``` protocol MCNearbyServiceBrowserDelegate : NSObjectProtocol {     func browser(_ browser: MCNearbyServiceBrowser, foundPeer peerID: MCPeerID, withDiscoveryInfo info: [String : String]?)     func browser(_ browser: MCNearbyServiceBrowser, lostPeer peerID: MCPeerID)     optional func browser(_ browser: MCNearbyServiceBrowser, didNotStartBrowsingForPeers error: NSError) } ``` |

Modified [MCNearbyServiceBrowserDelegate.browser(_: MCNearbyServiceBrowser, didNotStartBrowsingForPeers: NSError)](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1406913-browser)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func browser(_ browser: MCNearbyServiceBrowser!, didNotStartBrowsingForPeers error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func browser(_ browser: MCNearbyServiceBrowser, didNotStartBrowsingForPeers error: NSError) ``` | iOS 7.0 |

Modified [MCNearbyServiceBrowserDelegate.browser(_: MCNearbyServiceBrowser, foundPeer: MCPeerID, withDiscoveryInfo: [String : String]?)](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1406926-browser)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func browser(_ browser: MCNearbyServiceBrowser!, foundPeer peerID: MCPeerID!, withDiscoveryInfo info: [NSObject : AnyObject]!) ``` | iOS 8.0 |
| To | ``` func browser(_ browser: MCNearbyServiceBrowser, foundPeer peerID: MCPeerID, withDiscoveryInfo info: [String : String]?) ``` | iOS 7.0 |

Modified [MCNearbyServiceBrowserDelegate.browser(_: MCNearbyServiceBrowser, lostPeer: MCPeerID)](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1407014-browser)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func browser(_ browser: MCNearbyServiceBrowser!, lostPeer peerID: MCPeerID!) ``` | iOS 8.0 |
| To | ``` func browser(_ browser: MCNearbyServiceBrowser, lostPeer peerID: MCPeerID) ``` | iOS 7.0 |

Modified [MCPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid)

|  | Declaration |
| --- | --- |
| From | ``` class MCPeerID : NSObject, NSCopying, NSSecureCoding, NSCoding {     init!(displayName myDisplayName: String!)     var displayName: String! { get } } ``` |
| To | ``` class MCPeerID : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(displayName myDisplayName: String)     var displayName: String { get } } ``` |

Modified [MCPeerID.displayName](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/1407077-displayname)

|  | Declaration |
| --- | --- |
| From | ``` var displayName: String! { get } ``` |
| To | ``` var displayName: String { get } ``` |

Modified [MCPeerID.init(displayName: String)](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/1407089-initwithdisplayname)

|  | Declaration |
| --- | --- |
| From | ``` init!(displayName myDisplayName: String!) ``` |
| To | ``` init(displayName myDisplayName: String) ``` |

Modified [MCSession](https://developer.apple.com/documentation/multipeerconnectivity/mcsession)

|  | Declaration |
| --- | --- |
| From | ``` class MCSession : NSObject {     convenience init!(peer myPeerID: MCPeerID!)     init!(peer myPeerID: MCPeerID!, securityIdentity identity: [AnyObject]!, encryptionPreference encryptionPreference: MCEncryptionPreference)     func sendData(_ data: NSData!, toPeers peerIDs: [AnyObject]!, withMode mode: MCSessionSendDataMode, error error: NSErrorPointer) -> Bool     func disconnect()     func sendResourceAtURL(_ resourceURL: NSURL!, withName resourceName: String!, toPeer peerID: MCPeerID!, withCompletionHandler completionHandler: ((NSError!) -> Void)!) -> NSProgress!     func startStreamWithName(_ streamName: String!, toPeer peerID: MCPeerID!, error error: NSErrorPointer) -> NSOutputStream!     weak var delegate: MCSessionDelegate!     var myPeerID: MCPeerID! { get }     var securityIdentity: [AnyObject]! { get }     var encryptionPreference: MCEncryptionPreference { get }     var connectedPeers: [AnyObject]! { get } } extension MCSession {     func nearbyConnectionDataForPeer(_ peerID: MCPeerID!, withCompletionHandler completionHandler: ((NSData!, NSError!) -> Void)!)     func connectPeer(_ peerID: MCPeerID!, withNearbyConnectionData data: NSData!)     func cancelConnectPeer(_ peerID: MCPeerID!) } ``` |
| To | ``` class MCSession : NSObject {     convenience init(peer myPeerID: MCPeerID)     init(peer myPeerID: MCPeerID, securityIdentity identity: [AnyObject]?, encryptionPreference encryptionPreference: MCEncryptionPreference)     func sendData(_ data: NSData, toPeers peerIDs: [MCPeerID], withMode mode: MCSessionSendDataMode) throws     func disconnect()     func sendResourceAtURL(_ resourceURL: NSURL, withName resourceName: String, toPeer peerID: MCPeerID, withCompletionHandler completionHandler: ((NSError?) -> Void)?) -> NSProgress?     func startStreamWithName(_ streamName: String, toPeer peerID: MCPeerID) throws -> NSOutputStream     weak var delegate: MCSessionDelegate?     var myPeerID: MCPeerID { get }     var securityIdentity: [AnyObject]? { get }     var encryptionPreference: MCEncryptionPreference { get }     var connectedPeers: [MCPeerID] { get } } extension MCSession {     func nearbyConnectionDataForPeer(_ peerID: MCPeerID, withCompletionHandler completionHandler: (NSData, NSError?) -> Void)     func connectPeer(_ peerID: MCPeerID, withNearbyConnectionData data: NSData)     func cancelConnectPeer(_ peerID: MCPeerID) } ``` |

Modified [MCSession.cancelConnectPeer(_: MCPeerID)](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407106-cancelconnectpeer)

|  | Declaration |
| --- | --- |
| From | ``` func cancelConnectPeer(_ peerID: MCPeerID!) ``` |
| To | ``` func cancelConnectPeer(_ peerID: MCPeerID) ``` |

Modified [MCSession.connectedPeers](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406911-connectedpeers)

|  | Declaration |
| --- | --- |
| From | ``` var connectedPeers: [AnyObject]! { get } ``` |
| To | ``` var connectedPeers: [MCPeerID] { get } ``` |

Modified [MCSession.connectPeer(_: MCPeerID, withNearbyConnectionData: NSData)](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407054-connectpeer)

|  | Declaration |
| --- | --- |
| From | ``` func connectPeer(_ peerID: MCPeerID!, withNearbyConnectionData data: NSData!) ``` |
| To | ``` func connectPeer(_ peerID: MCPeerID, withNearbyConnectionData data: NSData) ``` |

Modified [MCSession.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407112-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: MCSessionDelegate! ``` |
| To | ``` weak var delegate: MCSessionDelegate? ``` |

Modified [MCSession.init(peer: MCPeerID)](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407000-initwithpeer)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(peer myPeerID: MCPeerID!) ``` |
| To | ``` convenience init(peer myPeerID: MCPeerID) ``` |

Modified [MCSession.init(peer: MCPeerID, securityIdentity: [AnyObject]?, encryptionPreference: MCEncryptionPreference)](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407025-initwithpeer)

|  | Declaration |
| --- | --- |
| From | ``` init!(peer myPeerID: MCPeerID!, securityIdentity identity: [AnyObject]!, encryptionPreference encryptionPreference: MCEncryptionPreference) ``` |
| To | ``` init(peer myPeerID: MCPeerID, securityIdentity identity: [AnyObject]?, encryptionPreference encryptionPreference: MCEncryptionPreference) ``` |

Modified [MCSession.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406992-mypeerid)

|  | Declaration |
| --- | --- |
| From | ``` var myPeerID: MCPeerID! { get } ``` |
| To | ``` var myPeerID: MCPeerID { get } ``` |

Modified [MCSession.nearbyConnectionDataForPeer(_: MCPeerID, withCompletionHandler: (NSData, NSError?) -> Void)](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407060-nearbyconnectiondataforpeer)

|  | Declaration |
| --- | --- |
| From | ``` func nearbyConnectionDataForPeer(_ peerID: MCPeerID!, withCompletionHandler completionHandler: ((NSData!, NSError!) -> Void)!) ``` |
| To | ``` func nearbyConnectionDataForPeer(_ peerID: MCPeerID, withCompletionHandler completionHandler: (NSData, NSError?) -> Void) ``` |

Modified [MCSession.securityIdentity](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406980-securityidentity)

|  | Declaration |
| --- | --- |
| From | ``` var securityIdentity: [AnyObject]! { get } ``` |
| To | ``` var securityIdentity: [AnyObject]? { get } ``` |

Modified [MCSession.sendData(_: NSData, toPeers: [MCPeerID], withMode: MCSessionSendDataMode) throws](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406997-send)

|  | Declaration |
| --- | --- |
| From | ``` func sendData(_ data: NSData!, toPeers peerIDs: [AnyObject]!, withMode mode: MCSessionSendDataMode, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func sendData(_ data: NSData, toPeers peerIDs: [MCPeerID], withMode mode: MCSessionSendDataMode) throws ``` |

Modified [MCSession.sendResourceAtURL(_: NSURL, withName: String, toPeer: MCPeerID, withCompletionHandler: ((NSError?) -> Void)?) -> NSProgress?](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407056-sendresource)

|  | Declaration |
| --- | --- |
| From | ``` func sendResourceAtURL(_ resourceURL: NSURL!, withName resourceName: String!, toPeer peerID: MCPeerID!, withCompletionHandler completionHandler: ((NSError!) -> Void)!) -> NSProgress! ``` |
| To | ``` func sendResourceAtURL(_ resourceURL: NSURL, withName resourceName: String, toPeer peerID: MCPeerID, withCompletionHandler completionHandler: ((NSError?) -> Void)?) -> NSProgress? ``` |

Modified [MCSession.startStreamWithName(_: String, toPeer: MCPeerID) throws -> NSOutputStream](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407071-startstreamwithname)

|  | Declaration |
| --- | --- |
| From | ``` func startStreamWithName(_ streamName: String!, toPeer peerID: MCPeerID!, error error: NSErrorPointer) -> NSOutputStream! ``` |
| To | ``` func startStreamWithName(_ streamName: String, toPeer peerID: MCPeerID) throws -> NSOutputStream ``` |

Modified [MCSessionDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MCSessionDelegate : NSObjectProtocol {     func session(_ session: MCSession!, peer peerID: MCPeerID!, didChangeState state: MCSessionState)     func session(_ session: MCSession!, didReceiveData data: NSData!, fromPeer peerID: MCPeerID!)     func session(_ session: MCSession!, didReceiveStream stream: NSInputStream!, withName streamName: String!, fromPeer peerID: MCPeerID!)     func session(_ session: MCSession!, didStartReceivingResourceWithName resourceName: String!, fromPeer peerID: MCPeerID!, withProgress progress: NSProgress!)     func session(_ session: MCSession!, didFinishReceivingResourceWithName resourceName: String!, fromPeer peerID: MCPeerID!, atURL localURL: NSURL!, withError error: NSError!)     optional func session(_ session: MCSession!, didReceiveCertificate certificate: [AnyObject]!, fromPeer peerID: MCPeerID!, certificateHandler certificateHandler: ((Bool) -> Void)!) } ``` |
| To | ``` protocol MCSessionDelegate : NSObjectProtocol {     func session(_ session: MCSession, peer peerID: MCPeerID, didChangeState state: MCSessionState)     func session(_ session: MCSession, didReceiveData data: NSData, fromPeer peerID: MCPeerID)     func session(_ session: MCSession, didReceiveStream stream: NSInputStream, withName streamName: String, fromPeer peerID: MCPeerID)     func session(_ session: MCSession, didStartReceivingResourceWithName resourceName: String, fromPeer peerID: MCPeerID, withProgress progress: NSProgress)     func session(_ session: MCSession, didFinishReceivingResourceWithName resourceName: String, fromPeer peerID: MCPeerID, atURL localURL: NSURL, withError error: NSError?)     optional func session(_ session: MCSession, didReceiveCertificate certificate: [AnyObject]?, fromPeer peerID: MCPeerID, certificateHandler certificateHandler: (Bool) -> Void) } ``` |

Modified [MCSessionDelegate.session(_: MCSession, didFinishReceivingResourceWithName: String, fromPeer: MCPeerID, atURL: NSURL, withError: NSError?)](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406984-session)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func session(_ session: MCSession!, didFinishReceivingResourceWithName resourceName: String!, fromPeer peerID: MCPeerID!, atURL localURL: NSURL!, withError error: NSError!) ``` | iOS 8.0 |
| To | ``` func session(_ session: MCSession, didFinishReceivingResourceWithName resourceName: String, fromPeer peerID: MCPeerID, atURL localURL: NSURL, withError error: NSError?) ``` | iOS 7.0 |

Modified [MCSessionDelegate.session(_: MCSession, didReceiveCertificate: [AnyObject]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1407067-session)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func session(_ session: MCSession!, didReceiveCertificate certificate: [AnyObject]!, fromPeer peerID: MCPeerID!, certificateHandler certificateHandler: ((Bool) -> Void)!) ``` | iOS 8.0 |
| To | ``` optional func session(_ session: MCSession, didReceiveCertificate certificate: [AnyObject]?, fromPeer peerID: MCPeerID, certificateHandler certificateHandler: (Bool) -> Void) ``` | iOS 7.0 |

Modified [MCSessionDelegate.session(_: MCSession, didReceiveData: NSData, fromPeer: MCPeerID)](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406934-session)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func session(_ session: MCSession!, didReceiveData data: NSData!, fromPeer peerID: MCPeerID!) ``` | iOS 8.0 |
| To | ``` func session(_ session: MCSession, didReceiveData data: NSData, fromPeer peerID: MCPeerID) ``` | iOS 7.0 |

Modified [MCSessionDelegate.session(_: MCSession, didReceiveStream: NSInputStream, withName: String, fromPeer: MCPeerID)](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406917-session)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func session(_ session: MCSession!, didReceiveStream stream: NSInputStream!, withName streamName: String!, fromPeer peerID: MCPeerID!) ``` | iOS 8.0 |
| To | ``` func session(_ session: MCSession, didReceiveStream stream: NSInputStream, withName streamName: String, fromPeer peerID: MCPeerID) ``` | iOS 7.0 |

Modified [MCSessionDelegate.session(_: MCSession, didStartReceivingResourceWithName: String, fromPeer: MCPeerID, withProgress: NSProgress)](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406965-session)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func session(_ session: MCSession!, didStartReceivingResourceWithName resourceName: String!, fromPeer peerID: MCPeerID!, withProgress progress: NSProgress!) ``` | iOS 8.0 |
| To | ``` func session(_ session: MCSession, didStartReceivingResourceWithName resourceName: String, fromPeer peerID: MCPeerID, withProgress progress: NSProgress) ``` | iOS 7.0 |

Modified [MCSessionDelegate.session(_: MCSession, peer: MCPeerID, didChangeState: MCSessionState)](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406958-session)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func session(_ session: MCSession!, peer peerID: MCPeerID!, didChangeState state: MCSessionState) ``` | iOS 8.0 |
| To | ``` func session(_ session: MCSession, peer peerID: MCPeerID, didChangeState state: MCSessionState) ``` | iOS 7.0 |

Modified [MCSessionSendDataMode [enum]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [MCSessionState [enum]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

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
