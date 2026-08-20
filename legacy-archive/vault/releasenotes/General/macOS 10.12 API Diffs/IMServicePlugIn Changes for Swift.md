---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/IMServicePlugIn.html
archived_at: '2026-07-18T02:51:25.840426Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# IMServicePlugIn Changes for Swift

### IMServicePlugIn

Modified IMGroupListPermissions [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum IMGroupListPermissions : UInt {     case CanReorderGroup     case CanRenameGroup     case CanAddNewMembers     case CanRemoveMembers     case CanReorderMembers } ``` |
| To | ``` enum IMGroupListPermissions : UInt {     case canReorderGroup     case canRenameGroup     case canAddNewMembers     case canRemoveMembers     case canReorderMembers } ``` |

Modified IMGroupListPermissions.canAddNewMembers

|  | Declaration |
| --- | --- |
| From | ``` case CanAddNewMembers ``` |
| To | ``` case canAddNewMembers ``` |

Modified IMGroupListPermissions.canRemoveMembers

|  | Declaration |
| --- | --- |
| From | ``` case CanRemoveMembers ``` |
| To | ``` case canRemoveMembers ``` |

Modified IMGroupListPermissions.canRenameGroup

|  | Declaration |
| --- | --- |
| From | ``` case CanRenameGroup ``` |
| To | ``` case canRenameGroup ``` |

Modified IMGroupListPermissions.canReorderGroup

|  | Declaration |
| --- | --- |
| From | ``` case CanReorderGroup ``` |
| To | ``` case canReorderGroup ``` |

Modified IMGroupListPermissions.canReorderMembers

|  | Declaration |
| --- | --- |
| From | ``` case CanReorderMembers ``` |
| To | ``` case canReorderMembers ``` |

Modified IMHandleAuthorizationStatus [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum IMHandleAuthorizationStatus : Int {     case Accepted     case Pending     case Declined } ``` |
| To | ``` enum IMHandleAuthorizationStatus : Int {     case accepted     case pending     case declined } ``` |

Modified IMHandleAuthorizationStatus.accepted

|  | Declaration |
| --- | --- |
| From | ``` case Accepted ``` |
| To | ``` case accepted ``` |

Modified IMHandleAuthorizationStatus.declined

|  | Declaration |
| --- | --- |
| From | ``` case Declined ``` |
| To | ``` case declined ``` |

Modified IMHandleAuthorizationStatus.pending

|  | Declaration |
| --- | --- |
| From | ``` case Pending ``` |
| To | ``` case pending ``` |

Modified IMHandleAvailability [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum IMHandleAvailability : Int {     case Unknown     case Offline     case Away     case Available } ``` |
| To | ``` enum IMHandleAvailability : Int {     case unknown     case offline     case away     case available } ``` |

Modified IMHandleAvailability.available

|  | Declaration |
| --- | --- |
| From | ``` case Available ``` |
| To | ``` case available ``` |

Modified IMHandleAvailability.away

|  | Declaration |
| --- | --- |
| From | ``` case Away ``` |
| To | ``` case away ``` |

Modified IMHandleAvailability.offline

|  | Declaration |
| --- | --- |
| From | ``` case Offline ``` |
| To | ``` case offline ``` |

Modified IMHandleAvailability.unknown

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified IMServiceApplication

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServiceApplication : NSObjectProtocol {     func plugInDidLogIn()     func plugInDidLogOutWithError(_ error: NSError!, reconnect reconnect: Bool)     func plugInDidFailToAuthenticate()     func plugInDidUpdateProperties(_ changes: [NSObject : AnyObject]!, ofHandle handle: String!) } ``` |
| To | ``` protocol IMServiceApplication : NSObjectProtocol {     func plugInDidLogIn()     func plugInDidLogOutWithError(_ error: Error!, reconnect reconnect: Bool)     func plugInDidFailToAuthenticate()     func plugInDidUpdateProperties(_ changes: [AnyHashable : Any]!, ofHandle handle: String!) } ``` |

Modified IMServiceApplication.plugInDidLogOutWithError(_: Error!, reconnect: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func plugInDidLogOutWithError(_ error: NSError!, reconnect reconnect: Bool) ``` |
| To | ``` func plugInDidLogOutWithError(_ error: Error!, reconnect reconnect: Bool) ``` |

Modified IMServiceApplication.plugInDidUpdateProperties(_: [AnyHashable : Any]!, ofHandle: String!)

|  | Declaration |
| --- | --- |
| From | ``` func plugInDidUpdateProperties(_ changes: [NSObject : AnyObject]!, ofHandle handle: String!) ``` |
| To | ``` func plugInDidUpdateProperties(_ changes: [AnyHashable : Any]!, ofHandle handle: String!) ``` |

Modified IMServiceApplicationChatRoomSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServiceApplicationChatRoomSupport : IMServiceApplication {     func plugInDidReceiveInvitation(_ invitation: IMServicePlugInMessage!, forChatRoom roomName: String!, fromHandle handle: String!)     func plugInDidReceiveMessage(_ message: IMServicePlugInMessage!, forChatRoom roomName: String!, fromHandle handle: String!)     func plugInDidReceiveNotice(_ notice: String!, forChatRoom roomName: String!)     func plugInDidSendMessage(_ message: IMServicePlugInMessage!, toChatRoom roomName: String!, error error: NSError!)     func plugInDidJoinChatRoom(_ roomName: String!)     func plugInDidLeaveChatRoom(_ roomName: String!, error error: NSError!)     func handles(_ handles: [AnyObject]!, didJoinChatRoom roomName: String!)     func handles(_ handles: [AnyObject]!, didLeaveChatRoom roomName: String!) } ``` |
| To | ``` protocol IMServiceApplicationChatRoomSupport : IMServiceApplication {     func plugInDidReceiveInvitation(_ invitation: IMServicePlugInMessage!, forChatRoom roomName: String!, fromHandle handle: String!)     func plugInDidReceive(_ message: IMServicePlugInMessage!, forChatRoom roomName: String!, fromHandle handle: String!)     func plugInDidReceiveNotice(_ notice: String!, forChatRoom roomName: String!)     func plugInDidSend(_ message: IMServicePlugInMessage!, toChatRoom roomName: String!, error error: Error!)     func plugInDidJoinChatRoom(_ roomName: String!)     func plugInDidLeaveChatRoom(_ roomName: String!, error error: Error!)     func handles(_ handles: [Any]!, didJoinChatRoom roomName: String!)     func handles(_ handles: [Any]!, didLeaveChatRoom roomName: String!) } ``` |

Modified IMServiceApplicationChatRoomSupport.handles(_: [Any]!, didJoinChatRoom: String!)

|  | Declaration |
| --- | --- |
| From | ``` func handles(_ handles: [AnyObject]!, didJoinChatRoom roomName: String!) ``` |
| To | ``` func handles(_ handles: [Any]!, didJoinChatRoom roomName: String!) ``` |

Modified IMServiceApplicationChatRoomSupport.handles(_: [Any]!, didLeaveChatRoom: String!)

|  | Declaration |
| --- | --- |
| From | ``` func handles(_ handles: [AnyObject]!, didLeaveChatRoom roomName: String!) ``` |
| To | ``` func handles(_ handles: [Any]!, didLeaveChatRoom roomName: String!) ``` |

Modified IMServiceApplicationChatRoomSupport.plugInDidLeaveChatRoom(_: String!, error: Error!)

|  | Declaration |
| --- | --- |
| From | ``` func plugInDidLeaveChatRoom(_ roomName: String!, error error: NSError!) ``` |
| To | ``` func plugInDidLeaveChatRoom(_ roomName: String!, error error: Error!) ``` |

Modified IMServiceApplicationChatRoomSupport.plugInDidReceive(_: IMServicePlugInMessage!, forChatRoom: String!, fromHandle: String!)

|  | Declaration |
| --- | --- |
| From | ``` func plugInDidReceiveMessage(_ message: IMServicePlugInMessage!, forChatRoom roomName: String!, fromHandle handle: String!) ``` |
| To | ``` func plugInDidReceive(_ message: IMServicePlugInMessage!, forChatRoom roomName: String!, fromHandle handle: String!) ``` |

Modified IMServiceApplicationChatRoomSupport.plugInDidSend(_: IMServicePlugInMessage!, toChatRoom: String!, error: Error!)

|  | Declaration |
| --- | --- |
| From | ``` func plugInDidSendMessage(_ message: IMServicePlugInMessage!, toChatRoom roomName: String!, error error: NSError!) ``` |
| To | ``` func plugInDidSend(_ message: IMServicePlugInMessage!, toChatRoom roomName: String!, error error: Error!) ``` |

Modified IMServiceApplicationGroupListAuthorizationSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServiceApplicationGroupListAuthorizationSupport : IMServiceApplicationGroupListSupport {     func plugInDidReceiveAuthorizationRequestFromHandle(_ handle: String!) } ``` |
| To | ``` protocol IMServiceApplicationGroupListAuthorizationSupport : IMServiceApplicationGroupListSupport {     func plugInDidReceiveAuthorizationRequest(fromHandle handle: String!) } ``` |

Modified IMServiceApplicationGroupListAuthorizationSupport.plugInDidReceiveAuthorizationRequest(fromHandle: String!)

|  | Declaration |
| --- | --- |
| From | ``` func plugInDidReceiveAuthorizationRequestFromHandle(_ handle: String!) ``` |
| To | ``` func plugInDidReceiveAuthorizationRequest(fromHandle handle: String!) ``` |

Modified IMServiceApplicationGroupListSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServiceApplicationGroupListSupport : IMServiceApplication {     func plugInDidUpdateGroupList(_ groups: [AnyObject]!, error error: NSError!) } ``` |
| To | ``` protocol IMServiceApplicationGroupListSupport : IMServiceApplication {     func plugInDidUpdateGroupList(_ groups: [Any]!, error error: Error!) } ``` |

Modified IMServiceApplicationGroupListSupport.plugInDidUpdateGroupList(_: [Any]!, error: Error!)

|  | Declaration |
| --- | --- |
| From | ``` func plugInDidUpdateGroupList(_ groups: [AnyObject]!, error error: NSError!) ``` |
| To | ``` func plugInDidUpdateGroupList(_ groups: [Any]!, error error: Error!) ``` |

Modified IMServiceApplicationInstantMessagingSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServiceApplicationInstantMessagingSupport {     func handleDidStartTyping(_ handle: String!)     func handleDidStopTyping(_ handle: String!)     func plugInDidReceiveMessage(_ message: IMServicePlugInMessage!, fromHandle handle: String!)     func plugInDidSendMessage(_ message: IMServicePlugInMessage!, toHandle handle: String!, error error: NSError!) } ``` |
| To | ``` protocol IMServiceApplicationInstantMessagingSupport {     func handleDidStartTyping(_ handle: String!)     func handleDidStopTyping(_ handle: String!)     func plugInDidReceive(_ message: IMServicePlugInMessage!, fromHandle handle: String!)     func plugInDidSend(_ message: IMServicePlugInMessage!, toHandle handle: String!, error error: Error!) } ``` |

Modified IMServiceApplicationInstantMessagingSupport.plugInDidReceive(_: IMServicePlugInMessage!, fromHandle: String!)

|  | Declaration |
| --- | --- |
| From | ``` func plugInDidReceiveMessage(_ message: IMServicePlugInMessage!, fromHandle handle: String!) ``` |
| To | ``` func plugInDidReceive(_ message: IMServicePlugInMessage!, fromHandle handle: String!) ``` |

Modified IMServiceApplicationInstantMessagingSupport.plugInDidSend(_: IMServicePlugInMessage!, toHandle: String!, error: Error!)

|  | Declaration |
| --- | --- |
| From | ``` func plugInDidSendMessage(_ message: IMServicePlugInMessage!, toHandle handle: String!, error error: NSError!) ``` |
| To | ``` func plugInDidSend(_ message: IMServicePlugInMessage!, toHandle handle: String!, error error: Error!) ``` |

Modified IMServicePlugIn

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServicePlugIn : NSObjectProtocol {     init!(serviceApplication serviceApplication: IMServiceApplication!)     func updateAccountSettings(_ accountSettings: [NSObject : AnyObject]!)     func login()     func logout() } ``` |
| To | ``` protocol IMServicePlugIn : NSObjectProtocol {     init!(serviceApplication serviceApplication: IMServiceApplication!)     func updateAccountSettings(_ accountSettings: [AnyHashable : Any]!)     func login()     func logout() } ``` |

Modified IMServicePlugIn.updateAccountSettings(_: [AnyHashable : Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func updateAccountSettings(_ accountSettings: [NSObject : AnyObject]!) ``` |
| To | ``` func updateAccountSettings(_ accountSettings: [AnyHashable : Any]!) ``` |

Modified IMServicePlugInChatRoomSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServicePlugInChatRoomSupport {     func joinChatRoom(_ roomName: String!)     func leaveChatRoom(_ roomName: String!)     func inviteHandles(_ handles: [AnyObject]!, toChatRoom roomName: String!, withMessage message: IMServicePlugInMessage!)     func sendMessage(_ message: IMServicePlugInMessage!, toChatRoom roomName: String!)     func declineChatRoomInvitation(_ roomName: String!) } ``` |
| To | ``` protocol IMServicePlugInChatRoomSupport {     func joinChatRoom(_ roomName: String!)     func leaveChatRoom(_ roomName: String!)     func inviteHandles(_ handles: [Any]!, toChatRoom roomName: String!, with message: IMServicePlugInMessage!)     func send(_ message: IMServicePlugInMessage!, toChatRoom roomName: String!)     func declineChatRoomInvitation(_ roomName: String!) } ``` |

Modified IMServicePlugInChatRoomSupport.inviteHandles(_: [Any]!, toChatRoom: String!, with: IMServicePlugInMessage!)

|  | Declaration |
| --- | --- |
| From | ``` func inviteHandles(_ handles: [AnyObject]!, toChatRoom roomName: String!, withMessage message: IMServicePlugInMessage!) ``` |
| To | ``` func inviteHandles(_ handles: [Any]!, toChatRoom roomName: String!, with message: IMServicePlugInMessage!) ``` |

Modified IMServicePlugInChatRoomSupport.send(_: IMServicePlugInMessage!, toChatRoom: String!)

|  | Declaration |
| --- | --- |
| From | ``` func sendMessage(_ message: IMServicePlugInMessage!, toChatRoom roomName: String!) ``` |
| To | ``` func send(_ message: IMServicePlugInMessage!, toChatRoom roomName: String!) ``` |

Modified IMServicePlugInGroupListAuthorizationSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServicePlugInGroupListAuthorizationSupport : IMServicePlugInGroupListSupport {     func sendAuthorizationRequestToHandle(_ handle: String!)     func acceptAuthorizationRequestFromHandle(_ handle: String!)     func declineAuthorizationRequestFromHandle(_ handle: String!) } ``` |
| To | ``` protocol IMServicePlugInGroupListAuthorizationSupport : IMServicePlugInGroupListSupport {     func sendAuthorizationRequest(toHandle handle: String!)     func acceptAuthorizationRequest(fromHandle handle: String!)     func declineAuthorizationRequest(fromHandle handle: String!) } ``` |

Modified IMServicePlugInGroupListAuthorizationSupport.acceptAuthorizationRequest(fromHandle: String!)

|  | Declaration |
| --- | --- |
| From | ``` func acceptAuthorizationRequestFromHandle(_ handle: String!) ``` |
| To | ``` func acceptAuthorizationRequest(fromHandle handle: String!) ``` |

Modified IMServicePlugInGroupListAuthorizationSupport.declineAuthorizationRequest(fromHandle: String!)

|  | Declaration |
| --- | --- |
| From | ``` func declineAuthorizationRequestFromHandle(_ handle: String!) ``` |
| To | ``` func declineAuthorizationRequest(fromHandle handle: String!) ``` |

Modified IMServicePlugInGroupListAuthorizationSupport.sendAuthorizationRequest(toHandle: String!)

|  | Declaration |
| --- | --- |
| From | ``` func sendAuthorizationRequestToHandle(_ handle: String!) ``` |
| To | ``` func sendAuthorizationRequest(toHandle handle: String!) ``` |

Modified IMServicePlugInGroupListEditingSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServicePlugInGroupListEditingSupport : IMServicePlugInGroupListSupport {     func addGroups(_ groupNames: [AnyObject]!)     func removeGroups(_ groupNames: [AnyObject]!)     func renameGroup(_ oldGroupName: String!, toGroup newGroupName: String!)     func addHandles(_ handles: [AnyObject]!, toGroup groupName: String!)     func removeHandles(_ handles: [AnyObject]!, fromGroup groupName: String!) } ``` |
| To | ``` protocol IMServicePlugInGroupListEditingSupport : IMServicePlugInGroupListSupport {     func addGroups(_ groupNames: [Any]!)     func removeGroups(_ groupNames: [Any]!)     func renameGroup(_ oldGroupName: String!, toGroup newGroupName: String!)     func addHandles(_ handles: [Any]!, toGroup groupName: String!)     func removeHandles(_ handles: [Any]!, fromGroup groupName: String!) } ``` |

Modified IMServicePlugInGroupListEditingSupport.addGroups(_: [Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func addGroups(_ groupNames: [AnyObject]!) ``` |
| To | ``` func addGroups(_ groupNames: [Any]!) ``` |

Modified IMServicePlugInGroupListEditingSupport.addHandles(_: [Any]!, toGroup: String!)

|  | Declaration |
| --- | --- |
| From | ``` func addHandles(_ handles: [AnyObject]!, toGroup groupName: String!) ``` |
| To | ``` func addHandles(_ handles: [Any]!, toGroup groupName: String!) ``` |

Modified IMServicePlugInGroupListEditingSupport.removeGroups(_: [Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func removeGroups(_ groupNames: [AnyObject]!) ``` |
| To | ``` func removeGroups(_ groupNames: [Any]!) ``` |

Modified IMServicePlugInGroupListEditingSupport.removeHandles(_: [Any]!, fromGroup: String!)

|  | Declaration |
| --- | --- |
| From | ``` func removeHandles(_ handles: [AnyObject]!, fromGroup groupName: String!) ``` |
| To | ``` func removeHandles(_ handles: [Any]!, fromGroup groupName: String!) ``` |

Modified IMServicePlugInGroupListHandlePictureSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServicePlugInGroupListHandlePictureSupport : NSObjectProtocol {     func requestPictureForHandle(_ handle: String!, withIdentifier identifier: String!) } ``` |
| To | ``` protocol IMServicePlugInGroupListHandlePictureSupport : NSObjectProtocol {     func requestPicture(forHandle handle: String!, withIdentifier identifier: String!) } ``` |

Modified IMServicePlugInGroupListHandlePictureSupport.requestPicture(forHandle: String!, withIdentifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` func requestPictureForHandle(_ handle: String!, withIdentifier identifier: String!) ``` |
| To | ``` func requestPicture(forHandle handle: String!, withIdentifier identifier: String!) ``` |

Modified IMServicePlugInGroupListOrderingSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServicePlugInGroupListOrderingSupport : IMServicePlugInGroupListSupport {     func reorderGroups(_ groupNames: [AnyObject]!)     func reorderHandles(_ handles: [AnyObject]!, inGroup groupName: String!) } ``` |
| To | ``` protocol IMServicePlugInGroupListOrderingSupport : IMServicePlugInGroupListSupport {     func reorderGroups(_ groupNames: [Any]!)     func reorderHandles(_ handles: [Any]!, inGroup groupName: String!) } ``` |

Modified IMServicePlugInGroupListOrderingSupport.reorderGroups(_: [Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func reorderGroups(_ groupNames: [AnyObject]!) ``` |
| To | ``` func reorderGroups(_ groupNames: [Any]!) ``` |

Modified IMServicePlugInGroupListOrderingSupport.reorderHandles(_: [Any]!, inGroup: String!)

|  | Declaration |
| --- | --- |
| From | ``` func reorderHandles(_ handles: [AnyObject]!, inGroup groupName: String!) ``` |
| To | ``` func reorderHandles(_ handles: [Any]!, inGroup groupName: String!) ``` |

Modified IMServicePlugInInstantMessagingSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServicePlugInInstantMessagingSupport {     func userDidStartTypingToHandle(_ handle: String!)     func userDidStopTypingToHandle(_ handle: String!)     func sendMessage(_ message: IMServicePlugInMessage!, toHandle handle: String!) } ``` |
| To | ``` protocol IMServicePlugInInstantMessagingSupport {     func userDidStartTyping(toHandle handle: String!)     func userDidStopTyping(toHandle handle: String!)     func send(_ message: IMServicePlugInMessage!, toHandle handle: String!) } ``` |

Modified IMServicePlugInInstantMessagingSupport.send(_: IMServicePlugInMessage!, toHandle: String!)

|  | Declaration |
| --- | --- |
| From | ``` func sendMessage(_ message: IMServicePlugInMessage!, toHandle handle: String!) ``` |
| To | ``` func send(_ message: IMServicePlugInMessage!, toHandle handle: String!) ``` |

Modified IMServicePlugInInstantMessagingSupport.userDidStartTyping(toHandle: String!)

|  | Declaration |
| --- | --- |
| From | ``` func userDidStartTypingToHandle(_ handle: String!) ``` |
| To | ``` func userDidStartTyping(toHandle handle: String!) ``` |

Modified IMServicePlugInInstantMessagingSupport.userDidStopTyping(toHandle: String!)

|  | Declaration |
| --- | --- |
| From | ``` func userDidStopTypingToHandle(_ handle: String!) ``` |
| To | ``` func userDidStopTyping(toHandle handle: String!) ``` |

Modified IMServicePlugInMessage

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class IMServicePlugInMessage : NSObject, NSCoding, NSCopying {     class func servicePlugInMessageWithContent(_ content: NSAttributedString!) -> AnyObject!     init!(content content: NSAttributedString!)     class func servicePlugInMessageWithContent(_ content: NSAttributedString!, date date: NSDate!) -> AnyObject!     init!(content content: NSAttributedString!, date date: NSDate!)     var guid: String! { get }     @NSCopying var content: NSAttributedString!     @NSCopying var date: NSDate! } ``` | NSCoding, NSCopying |
| To | ``` class IMServicePlugInMessage : NSObject, NSCoding, NSCopying {     class func servicePlugInMessage(withContent content: NSAttributedString!) -> Any!     init!(content content: NSAttributedString!)     class func servicePlugInMessage(withContent content: NSAttributedString!, date date: Date!) -> Any!     init!(content content: NSAttributedString!, date date: Date!)     var guid: String! { get }     @NSCopying var content: NSAttributedString!     var date: Date!     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension IMServicePlugInMessage : CVarArg { } extension IMServicePlugInMessage : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSCopying |

Modified IMServicePlugInMessage.date

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var date: NSDate! ``` |
| To | ``` var date: Date! ``` |

Modified IMServicePlugInMessage.init(content: NSAttributedString!, date: Date!)

|  | Declaration |
| --- | --- |
| From | ``` init!(content content: NSAttributedString!, date date: NSDate!) ``` |
| To | ``` init!(content content: NSAttributedString!, date date: Date!) ``` |

Modified IMServicePlugInMessage.servicePlugInMessage(withContent: NSAttributedString!) -> Any! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func servicePlugInMessageWithContent(_ content: NSAttributedString!) -> AnyObject! ``` |
| To | ``` class func servicePlugInMessage(withContent content: NSAttributedString!) -> Any! ``` |

Modified IMServicePlugInMessage.servicePlugInMessage(withContent: NSAttributedString!, date: Date!) -> Any! [class]

|  | Declaration |
| --- | --- |
| From | ``` class func servicePlugInMessageWithContent(_ content: NSAttributedString!, date date: NSDate!) -> AnyObject! ``` |
| To | ``` class func servicePlugInMessage(withContent content: NSAttributedString!, date date: Date!) -> Any! ``` |

Modified IMServicePlugInPresenceSupport

|  | Declaration |
| --- | --- |
| From | ``` protocol IMServicePlugInPresenceSupport {     func updateSessionProperties(_ properties: [NSObject : AnyObject]!) } ``` |
| To | ``` protocol IMServicePlugInPresenceSupport {     func updateSessionProperties(_ properties: [AnyHashable : Any]!) } ``` |

Modified IMServicePlugInPresenceSupport.updateSessionProperties(_: [AnyHashable : Any]!)

|  | Declaration |
| --- | --- |
| From | ``` func updateSessionProperties(_ properties: [NSObject : AnyObject]!) ``` |
| To | ``` func updateSessionProperties(_ properties: [AnyHashable : Any]!) ``` |

Modified IMSessionAvailability [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum IMSessionAvailability : Int {     case Away     case Available } ``` |
| To | ``` enum IMSessionAvailability : Int {     case away     case available } ``` |

Modified IMSessionAvailability.available

|  | Declaration |
| --- | --- |
| From | ``` case Available ``` |
| To | ``` case available ``` |

Modified IMSessionAvailability.away

|  | Declaration |
| --- | --- |
| From | ``` case Away ``` |
| To | ``` case away ``` |

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
