---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/GameKit.html
archived_at: '2026-07-18T02:57:48.670382Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# GameKit Changes for Swift

### GameKit

Added [GKBasePlayer](https://developer.apple.com/documentation/gamekit/gkbaseplayer)Added [GKBasePlayer.displayName](https://developer.apple.com/documentation/gamekit/gkbaseplayer/1641907-displayname)Added [GKBasePlayer.playerID](https://developer.apple.com/documentation/gamekit/gkbaseplayer/1641912-playerid)Added [GKCloudPlayer](https://developer.apple.com/documentation/gamekit/gkcloudplayer)Added [GKCloudPlayer.getCurrentSignedInPlayer(forContainer: String?, completionHandler: (GKCloudPlayer?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/gamekit/gkcloudplayer/2172413-getcurrentsignedinplayerforconta)Added [GKConnectionState [enum]](https://developer.apple.com/documentation/gamekit/gkconnectionstate)Added [GKConnectionState.connected](https://developer.apple.com/documentation/gamekit/gkconnectionstate/connected)Added [GKConnectionState.notConnected](https://developer.apple.com/documentation/gamekit/gkconnectionstate/gkconnectionstatenotconnected)Added [GKError [struct]](https://developer.apple.com/documentation/gamekit/gkerror)Added [GKError.authenticationInProgress](https://developer.apple.com/documentation/gamekit/gkerror/2325569-authenticationinprogress)Added [GKError.cancelled](https://developer.apple.com/documentation/gamekit/gkerror/2325545-cancelled)Added [GKError.challengeInvalid](https://developer.apple.com/documentation/gamekit/gkerror/2325547-challengeinvalid)Added [GKError.communicationsFailure](https://developer.apple.com/documentation/gamekit/gkerror/2325550-communicationsfailure)Added [GKError.gameSessionRequestInvalid](https://developer.apple.com/documentation/gamekit/gkerror/2325554-gamesessionrequestinvalid)Added [GKError.gameUnrecognized](https://developer.apple.com/documentation/gamekit/gkerror/2325501-gameunrecognized)Added GKError.init(_nsError: NSError)Added [GKError.invalidCredentials](https://developer.apple.com/documentation/gamekit/gkerror/2325571-invalidcredentials)Added [GKError.invalidParameter](https://developer.apple.com/documentation/gamekit/gkerror/2325566-invalidparameter)Added [GKError.invalidPlayer](https://developer.apple.com/documentation/gamekit/gkerror/2325507-invalidplayer)Added [GKError.invitationsDisabled](https://developer.apple.com/documentation/gamekit/gkerror/2325534-invitationsdisabled)Added [GKError.matchNotConnected](https://developer.apple.com/documentation/gamekit/gkerror/2325520-matchnotconnected)Added [GKError.matchRequestInvalid](https://developer.apple.com/documentation/gamekit/gkerror/2325555-matchrequestinvalid)Added [GKError.notAuthenticated](https://developer.apple.com/documentation/gamekit/gkerror/2325539-notauthenticated)Added [GKError.notSupported](https://developer.apple.com/documentation/gamekit/gkerror/2325512-notsupported)Added [GKError.parentalControlsBlocked](https://developer.apple.com/documentation/gamekit/gkerror/2325523-parentalcontrolsblocked)Added [GKError.playerPhotoFailure](https://developer.apple.com/documentation/gamekit/gkerror/2325568-playerphotofailure)Added [GKError.playerStatusExceedsMaximumLength](https://developer.apple.com/documentation/gamekit/gkerror/2325546-playerstatusexceedsmaximumlength)Added [GKError.playerStatusInvalid](https://developer.apple.com/documentation/gamekit/gkerror/2325529-playerstatusinvalid)Added [GKError.scoreNotSet](https://developer.apple.com/documentation/gamekit/gkerror/2325540-scorenotset)Added [GKError.turnBasedInvalidParticipant](https://developer.apple.com/documentation/gamekit/gkerror/2325563-turnbasedinvalidparticipant)Added [GKError.turnBasedInvalidState](https://developer.apple.com/documentation/gamekit/gkerror/2325504-turnbasedinvalidstate)Added [GKError.turnBasedInvalidTurn](https://developer.apple.com/documentation/gamekit/gkerror/2325519-turnbasedinvalidturn)Added [GKError.turnBasedMatchDataTooLarge](https://developer.apple.com/documentation/gamekit/gkerror/2325557-turnbasedmatchdatatoolarge)Added [GKError.turnBasedTooManySessions](https://developer.apple.com/documentation/gamekit/gkerror/2325549-turnbasedtoomanysessions)Added [GKError.ubiquityContainerUnavailable](https://developer.apple.com/documentation/gamekit/gkerror/2325505-ubiquitycontainerunavailable)Added [GKError.underage](https://developer.apple.com/documentation/gamekit/gkerror/2325552-underage)Added [GKError.unexpectedConnection](https://developer.apple.com/documentation/gamekit/gkerror/2325516-unexpectedconnection)Added [GKError.unknown](https://developer.apple.com/documentation/gamekit/gkerror/2325536-unknown)Added [GKError.userDenied](https://developer.apple.com/documentation/gamekit/gkerror/2325564-userdenied)Added [GKError.Code.gameSessionRequestInvalid](https://developer.apple.com/documentation/gamekit/gkerror/code/gamesessionrequestinvalid)Added [GKError.Code.matchNotConnected](https://developer.apple.com/documentation/gamekit/gkerror/code/matchnotconnected)Added [GKGameSession](https://developer.apple.com/documentation/gamekit/gkgamesession)Added [GKGameSession.add(listener: GKGameSessionEventListener) [class]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641889-add)Added [GKGameSession.badgedPlayers](https://developer.apple.com/documentation/gamekit/gkgamesession/1641884-badgedplayers)Added [GKGameSession.clearBadge(for: [GKCloudPlayer], completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/gamekit/gkgamesession/1641900-clearbadge)Added [GKGameSession.createSession(inContainer: String?, withTitle: String, maxConnectedPlayers: Int, completionHandler: (GKGameSession?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641863-createsessionincontainer)Added [GKGameSession.getShareURL(completionHandler: (URL?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/gamekit/gkgamesession/1641893-getshareurlwithcompletionhandler)Added [GKGameSession.identifier](https://developer.apple.com/documentation/gamekit/gkgamesession/1641891-identifier)Added [GKGameSession.lastModifiedDate](https://developer.apple.com/documentation/gamekit/gkgamesession/1641854-lastmodifieddate)Added [GKGameSession.lastModifiedPlayer](https://developer.apple.com/documentation/gamekit/gkgamesession/1641882-lastmodifiedplayer)Added [GKGameSession.load(withIdentifier: String, completionHandler: (GKGameSession?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641894-load)Added [GKGameSession.loadData(completionHandler: (Data?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/gamekit/gkgamesession/1641899-loaddata)Added [GKGameSession.loadSessions(inContainer: String?, completionHandler: ([GKGameSession]?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641908-loadsessionsincontainer)Added [GKGameSession.maxNumberOfConnectedPlayers](https://developer.apple.com/documentation/gamekit/gkgamesession/1641876-maxnumberofconnectedplayers)Added [GKGameSession.owner](https://developer.apple.com/documentation/gamekit/gkgamesession/1641896-owner)Added [GKGameSession.players](https://developer.apple.com/documentation/gamekit/gkgamesession/1641906-players)Added [GKGameSession.players(with: GKConnectionState) -> [GKCloudPlayer]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641877-players)Added [GKGameSession.remove(listener: GKGameSessionEventListener) [class]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641886-removeeventlistener)Added [GKGameSession.remove(withIdentifier: String, completionHandler: (Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641875-remove)Added [GKGameSession.save(_: Data, completionHandler: (Data?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/gamekit/gkgamesession/1641903-savedata)Added [GKGameSession.send(_: Data, with: GKTransportType, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/gamekit/gkgamesession/1641880-senddata)Added [GKGameSession.sendMessage(withLocalizedFormatKey: String, arguments: [String], data: Data?, to: [GKCloudPlayer], badgePlayers: Bool, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/gamekit/gkgamesession/1641868-sendmessage)Added [GKGameSession.setConnectionState(_: GKConnectionState, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/gamekit/gkgamesession/1641885-setconnectionstate)Added [GKGameSession.title](https://developer.apple.com/documentation/gamekit/gkgamesession/1641910-title)Added [GKGameSessionError [struct]](https://developer.apple.com/documentation/gamekit/gkgamesessionerror)Added [GKGameSessionError.badContainer](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325508-badcontainer)Added [GKGameSessionError.cloudDriveDisabled](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325562-clouddrivedisabled)Added [GKGameSessionError.cloudQuotaExceeded](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325570-cloudquotaexceeded)Added [GKGameSessionError.connectionCancelledByUser](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325506-connectioncancelledbyuser)Added [GKGameSessionError.connectionFailed](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325514-connectionfailed)Added GKGameSessionError.init(_nsError: NSError)Added [GKGameSessionError.invalidSession](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325530-invalidsession)Added [GKGameSessionError.networkFailure](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325524-networkfailure)Added [GKGameSessionError.notAuthenticated](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325518-notauthenticated)Added [GKGameSessionError.sendDataNoRecipients](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325577-senddatanorecipients)Added [GKGameSessionError.sendDataNotConnected](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325521-senddatanotconnected)Added [GKGameSessionError.sendDataNotReachable](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325558-senddatanotreachable)Added [GKGameSessionError.sendRateLimitReached](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325511-sendratelimitreached)Added [GKGameSessionError.sessionConflict](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325541-sessionconflict)Added [GKGameSessionError.sessionHasMaxConnectedPlayers](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325517-sessionhasmaxconnectedplayers)Added [GKGameSessionError.sessionNotShared](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325532-sessionnotshared)Added [GKGameSessionError.unknown](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/2325548-unknown)Added [GKGameSessionError.Code [enum]](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code)Added [GKGameSessionError.Code.badContainer](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/badcontainer)Added [GKGameSessionError.Code.cloudDriveDisabled](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorclouddrivedisabled)Added [GKGameSessionError.Code.cloudQuotaExceeded](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorcloudquotaexceeded)Added [GKGameSessionError.Code.connectionCancelledByUser](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorconnectioncancelledbyuser)Added [GKGameSessionError.Code.connectionFailed](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/connectionfailed)Added [GKGameSessionError.Code.invalidSession](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/invalidsession)Added [GKGameSessionError.Code.networkFailure](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/networkfailure)Added [GKGameSessionError.Code.notAuthenticated](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrornotauthenticated)Added [GKGameSessionError.Code.sendDataNoRecipients](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsenddatanorecipients)Added [GKGameSessionError.Code.sendDataNotConnected](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsenddatanotconnected)Added [GKGameSessionError.Code.sendDataNotReachable](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsenddatanotreachable)Added [GKGameSessionError.Code.sendRateLimitReached](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsendratelimitreached)Added [GKGameSessionError.Code.sessionConflict](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsessionconflict)Added [GKGameSessionError.Code.sessionHasMaxConnectedPlayers](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsessionhasmaxconnectedplayers)Added [GKGameSessionError.Code.sessionNotShared](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsessionnotshared)Added [GKGameSessionError.Code.unknown](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/unknown)Added [GKGameSessionEventListener](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener)Added [GKGameSessionEventListener.session(_: GKGameSession, didAdd: GKCloudPlayer)](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641867-session)Added [GKGameSessionEventListener.session(_: GKGameSession, didReceive: Data, from: GKCloudPlayer)](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641857-session)Added [GKGameSessionEventListener.session(_: GKGameSession, didReceiveMessage: String, with: Data, from: GKCloudPlayer)](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641879-session)Added [GKGameSessionEventListener.session(_: GKGameSession, didRemove: GKCloudPlayer)](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641881-session)Added [GKGameSessionEventListener.session(_: GKGameSession, player: GKCloudPlayer, didChange: GKConnectionState)](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641861-session)Added [GKGameSessionEventListener.session(_: GKGameSession, player: GKCloudPlayer, didSave: Data)](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641888-session)Added [GKGameSessionSharingViewController](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontroller)Added [GKGameSessionSharingViewController.delegate](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontroller/1650986-delegate)Added [GKGameSessionSharingViewController.init(session: GKGameSession)](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontroller/1650985-initwithsession)Added [GKGameSessionSharingViewController.session](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontroller/1650982-session)Added [GKGameSessionSharingViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontrollerdelegate)Added [GKGameSessionSharingViewControllerDelegate.sharingViewController(_: GKGameSessionSharingViewController, didFinishWithError: Error?)](https://developer.apple.com/documentation/gamekit/gkgamesessionsharingviewcontrollerdelegate/1650984-sharingviewcontroller)Added [GKLocalPlayer.loadRecentPlayers(completionHandler: ( ([GKPlayer]?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1833711-loadrecentplayerswithcompletionh)Added [GKTransportType [enum]](https://developer.apple.com/documentation/gamekit/gktransporttype)Added [GKTransportType.reliable](https://developer.apple.com/documentation/gamekit/gktransporttype/reliable)Added [GKTransportType.unreliable](https://developer.apple.com/documentation/gamekit/gktransporttype/gktransporttypeunreliable)Added [GKGameSessionErrorDomain](https://developer.apple.com/documentation/gamekit/gkgamesessionerrordomain)Modified [GKAchievement](https://developer.apple.com/documentation/gamekit/gkachievement)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKAchievement : NSObject, NSCoding, NSSecureCoding {     class func loadAchievementsWithCompletionHandler(_ completionHandler: (([GKAchievement]?, NSError?) -> Void)?)     class func resetAchievementsWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     init(identifier identifier: String?)     init(identifier identifier: String?, player player: GKPlayer)     class func reportAchievements(_ achievements: [GKAchievement], withCompletionHandler completionHandler: ((NSError?) -> Void)?)     var identifier: String?     var percentComplete: Double     var completed: Bool { get }     @NSCopying var lastReportedDate: NSDate { get }     var showsCompletionBanner: Bool     var player: GKPlayer { get } } extension GKAchievement {     func reportAchievementWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     init(identifier identifier: String?, forPlayer playerID: String)     var hidden: Bool { get }     var playerID: String { get } } extension GKAchievement {     func challengeComposeControllerWithMessage(_ message: String?, players players: [GKPlayer], completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController     func issueChallengeToPlayers(_ playerIDs: [String]?, message message: String?)     func selectChallengeablePlayers(_ players: [GKPlayer], withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?)     class func reportAchievements(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: ((NSError?) -> Void)?) } extension GKAchievement {     func selectChallengeablePlayerIDs(_ playerIDs: [String]?, withCompletionHandler completionHandler: (([String]?, NSError?) -> Void)?)     func challengeComposeControllerWithPlayers(_ playerIDs: [String]?, message message: String?, completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController? } ``` | NSCoding, NSSecureCoding |
| To | ``` class GKAchievement : NSObject, NSCoding, NSSecureCoding {     class func loadAchievements(completionHandler completionHandler: (@escaping ([GKAchievement]?, Error?) -> Swift.Void)? = nil)     class func resetAchievements(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     init(identifier identifier: String?)     init(identifier identifier: String?, player player: GKPlayer)     class func report(_ achievements: [GKAchievement], withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     var identifier: String?     var percentComplete: Double     var isCompleted: Bool { get }     var lastReportedDate: Date { get }     var showsCompletionBanner: Bool     var player: GKPlayer? { get }     func selectChallengeablePlayerIDs(_ playerIDs: [String]?, withCompletionHandler completionHandler: (@escaping ([String]?, Error?) -> Swift.Void)? = nil)     func issueChallenge(toPlayers playerIDs: [String]?, message message: String?)     func challengeComposeController(withPlayers playerIDs: [String]?, message message: String?, completionHandler completionHandler: GameKit.GKChallengeComposeCompletionBlock? = nil) -> UIViewController?     func challengeComposeController(withMessage message: String?, players players: [GKPlayer], completionHandler completionHandler: GameKit.GKChallengeComposeCompletionBlock? = nil) -> UIViewController     func selectChallengeablePlayers(_ players: [GKPlayer], withCompletionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil)     class func report(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func report(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     init(identifier identifier: String?, forPlayer playerID: String)     var isHidden: Bool { get }     var playerID: String { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKAchievement : CVarArg { } extension GKAchievement : Equatable, Hashable {     var hashValue: Int { get } } extension GKAchievement {     func report(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     init(identifier identifier: String?, forPlayer playerID: String)     var isHidden: Bool { get }     var playerID: String { get } } extension GKAchievement {     func challengeComposeController(withMessage message: String?, players players: [GKPlayer], completionHandler completionHandler: GameKit.GKChallengeComposeCompletionBlock? = nil) -> UIViewController     func selectChallengeablePlayers(_ players: [GKPlayer], withCompletionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil)     class func report(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) } extension GKAchievement {     func selectChallengeablePlayerIDs(_ playerIDs: [String]?, withCompletionHandler completionHandler: (@escaping ([String]?, Error?) -> Swift.Void)? = nil)     func issueChallenge(toPlayers playerIDs: [String]?, message message: String?)     func challengeComposeController(withPlayers playerIDs: [String]?, message message: String?, completionHandler completionHandler: GameKit.GKChallengeComposeCompletionBlock? = nil) -> UIViewController? } ``` | CVarArg, Equatable, Hashable, NSCoding, NSSecureCoding |

Modified [GKAchievement.challengeComposeController(withMessage: String?, players: [GKPlayer], completionHandler: GameKit.GKChallengeComposeCompletionBlock?) -> UIViewController](https://developer.apple.com/documentation/gamekit/gkachievement/1520805-challengecomposecontrollerwithme)

|  | Declaration |
| --- | --- |
| From | ``` func challengeComposeControllerWithMessage(_ message: String?, players players: [GKPlayer], completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController ``` |
| To | ``` func challengeComposeController(withMessage message: String?, players players: [GKPlayer], completionHandler completionHandler: GameKit.GKChallengeComposeCompletionBlock? = nil) -> UIViewController ``` |

Modified [GKAchievement.isCompleted](https://developer.apple.com/documentation/gamekit/gkachievement/1521050-iscompleted)

|  | Declaration |
| --- | --- |
| From | ``` var completed: Bool { get } ``` |
| To | ``` var isCompleted: Bool { get } ``` |

Modified [GKAchievement.lastReportedDate](https://developer.apple.com/documentation/gamekit/gkachievement/1520993-lastreporteddate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var lastReportedDate: NSDate { get } ``` |
| To | ``` var lastReportedDate: Date { get } ``` |

Modified [GKAchievement.loadAchievements(completionHandler: ( ([GKAchievement]?, Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkachievement/1520748-loadachievements)

|  | Declaration |
| --- | --- |
| From | ``` class func loadAchievementsWithCompletionHandler(_ completionHandler: (([GKAchievement]?, NSError?) -> Void)?) ``` |
| To | ``` class func loadAchievements(completionHandler completionHandler: (@escaping ([GKAchievement]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKAchievement.player](https://developer.apple.com/documentation/gamekit/gkachievement/1520943-player)

|  | Declaration |
| --- | --- |
| From | ``` var player: GKPlayer { get } ``` |
| To | ``` var player: GKPlayer? { get } ``` |

Modified [GKAchievement.report(_: [GKAchievement], withCompletionHandler: ( (Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkachievement/1520509-reportachievements)

|  | Declaration |
| --- | --- |
| From | ``` class func reportAchievements(_ achievements: [GKAchievement], withCompletionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` class func report(_ achievements: [GKAchievement], withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKAchievement.report(_: [GKAchievement], withEligibleChallenges: [GKChallenge], withCompletionHandler: ( (Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkachievement/1520558-report)

|  | Declaration |
| --- | --- |
| From | ``` class func reportAchievements(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` class func report(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKAchievement.resetAchievements(completionHandler: ( (Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkachievement/1520717-resetachievementswithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` class func resetAchievementsWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` class func resetAchievements(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKAchievement.selectChallengeablePlayers(_: [GKPlayer], withCompletionHandler: ( ([GKPlayer]?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkachievement/1520504-selectchallengeableplayers)

|  | Declaration |
| --- | --- |
| From | ``` func selectChallengeablePlayers(_ players: [GKPlayer], withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?) ``` |
| To | ``` func selectChallengeablePlayers(_ players: [GKPlayer], withCompletionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKAchievementDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKAchievementDescription : NSObject, NSCoding, NSSecureCoding {     class func loadAchievementDescriptionsWithCompletionHandler(_ completionHandler: (([GKAchievementDescription]?, NSError?) -> Void)?)     var identifier: String? { get }     var groupIdentifier: String? { get }     var title: String? { get }     var achievedDescription: String? { get }     var unachievedDescription: String? { get }     var maximumPoints: Int { get }     var hidden: Bool { get }     var replayable: Bool { get } } extension GKAchievementDescription {     var image: UIImage? { get }     func loadImageWithCompletionHandler(_ completionHandler: ((UIImage?, NSError?) -> Void)?)     class func incompleteAchievementImage() -> UIImage     class func placeholderCompletedAchievementImage() -> UIImage } ``` | NSCoding, NSSecureCoding |
| To | ``` class GKAchievementDescription : NSObject, NSCoding, NSSecureCoding {     class func loadAchievementDescriptions(completionHandler completionHandler: (@escaping ([GKAchievementDescription]?, Error?) -> Swift.Void)? = nil)     var identifier: String? { get }     var groupIdentifier: String? { get }     var title: String? { get }     var achievedDescription: String? { get }     var unachievedDescription: String? { get }     var maximumPoints: Int { get }     var isHidden: Bool { get }     var isReplayable: Bool { get }     var image: UIImage? { get }     func loadImage(completionHandler completionHandler: (@escaping (UIImage?, Error?) -> Swift.Void)? = nil)     class func incompleteAchievementImage() -> UIImage     class func placeholderCompletedAchievementImage() -> UIImage     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKAchievementDescription : CVarArg { } extension GKAchievementDescription : Equatable, Hashable {     var hashValue: Int { get } } extension GKAchievementDescription {     var image: UIImage? { get }     func loadImage(completionHandler completionHandler: (@escaping (UIImage?, Error?) -> Swift.Void)? = nil)     class func incompleteAchievementImage() -> UIImage     class func placeholderCompletedAchievementImage() -> UIImage } ``` | CVarArg, Equatable, Hashable, NSCoding, NSSecureCoding |

Modified [GKAchievementDescription.isHidden](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416582-hidden)

|  | Declaration |
| --- | --- |
| From | ``` var hidden: Bool { get } ``` |
| To | ``` var isHidden: Bool { get } ``` |

Modified [GKAchievementDescription.isReplayable](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416578-replayable)

|  | Declaration |
| --- | --- |
| From | ``` var replayable: Bool { get } ``` |
| To | ``` var isReplayable: Bool { get } ``` |

Modified [GKAchievementDescription.loadAchievementDescriptions(completionHandler: ( ([GKAchievementDescription]?, Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416601-loadachievementdescriptionswithc)

|  | Declaration |
| --- | --- |
| From | ``` class func loadAchievementDescriptionsWithCompletionHandler(_ completionHandler: (([GKAchievementDescription]?, NSError?) -> Void)?) ``` |
| To | ``` class func loadAchievementDescriptions(completionHandler completionHandler: (@escaping ([GKAchievementDescription]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKAchievementDescription.loadImage(completionHandler: ( (UIImage?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416596-loadimage)

|  | Declaration |
| --- | --- |
| From | ``` func loadImageWithCompletionHandler(_ completionHandler: ((UIImage?, NSError?) -> Void)?) ``` |
| To | ``` func loadImage(completionHandler completionHandler: (@escaping (UIImage?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKChallenge](https://developer.apple.com/documentation/gamekit/gkchallenge)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKChallenge : NSObject, NSCoding, NSSecureCoding {     class func loadReceivedChallengesWithCompletionHandler(_ completionHandler: (([GKChallenge]?, NSError?) -> Void)?)     func decline()     var issuingPlayerID: String? { get }     var receivingPlayerID: String? { get }     @NSCopying var issuingPlayer: GKPlayer? { get }     @NSCopying var receivingPlayer: GKPlayer? { get }     var state: GKChallengeState { get }     var issueDate: NSDate { get }     var completionDate: NSDate? { get }     var message: String? { get } } ``` | NSCoding, NSSecureCoding |
| To | ``` class GKChallenge : NSObject, NSCoding, NSSecureCoding {     class func loadReceivedChallenges(completionHandler completionHandler: (@escaping ([GKChallenge]?, Error?) -> Swift.Void)? = nil)     func decline()     var issuingPlayerID: String? { get }     var receivingPlayerID: String? { get }     @NSCopying var issuingPlayer: GKPlayer? { get }     @NSCopying var receivingPlayer: GKPlayer? { get }     var state: GKChallengeState { get }     var issueDate: Date { get }     var completionDate: Date? { get }     var message: String? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKChallenge : CVarArg { } extension GKChallenge : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, NSSecureCoding |

Modified [GKChallenge.completionDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520928-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` var completionDate: NSDate? { get } ``` |
| To | ``` var completionDate: Date? { get } ``` |

Modified [GKChallenge.issueDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520803-issuedate)

|  | Declaration |
| --- | --- |
| From | ``` var issueDate: NSDate { get } ``` |
| To | ``` var issueDate: Date { get } ``` |

Modified [GKChallenge.loadReceivedChallenges(completionHandler: ( ([GKChallenge]?, Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkchallenge/1520864-loadreceivedchallengeswithcomple)

|  | Declaration |
| --- | --- |
| From | ``` class func loadReceivedChallengesWithCompletionHandler(_ completionHandler: (([GKChallenge]?, NSError?) -> Void)?) ``` |
| To | ``` class func loadReceivedChallenges(completionHandler completionHandler: (@escaping ([GKChallenge]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKChallengeListener](https://developer.apple.com/documentation/gamekit/gkchallengelistener)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKChallengeListener : NSObjectProtocol {     optional func player(_ player: GKPlayer, wantsToPlayChallenge challenge: GKChallenge)     optional func player(_ player: GKPlayer, didReceiveChallenge challenge: GKChallenge)     optional func player(_ player: GKPlayer, didCompleteChallenge challenge: GKChallenge, issuedByFriend friendPlayer: GKPlayer)     optional func player(_ player: GKPlayer, issuedChallengeWasCompleted challenge: GKChallenge, byFriend friendPlayer: GKPlayer) } ``` |
| To | ``` protocol GKChallengeListener : NSObjectProtocol {     optional func player(_ player: GKPlayer, wantsToPlay challenge: GKChallenge)     optional func player(_ player: GKPlayer, didReceive challenge: GKChallenge)     optional func player(_ player: GKPlayer, didComplete challenge: GKChallenge, issuedByFriend friendPlayer: GKPlayer)     optional func player(_ player: GKPlayer, issuedChallengeWasCompleted challenge: GKChallenge, byFriend friendPlayer: GKPlayer) } ``` |

Modified [GKChallengeListener.player(_: GKPlayer, didComplete: GKChallenge, issuedByFriend: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494688-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer, didCompleteChallenge challenge: GKChallenge, issuedByFriend friendPlayer: GKPlayer) ``` |
| To | ``` optional func player(_ player: GKPlayer, didComplete challenge: GKChallenge, issuedByFriend friendPlayer: GKPlayer) ``` |

Modified [GKChallengeListener.player(_: GKPlayer, didReceive: GKChallenge)](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494691-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer, didReceiveChallenge challenge: GKChallenge) ``` |
| To | ``` optional func player(_ player: GKPlayer, didReceive challenge: GKChallenge) ``` |

Modified [GKChallengeListener.player(_: GKPlayer, wantsToPlay: GKChallenge)](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494684-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer, wantsToPlayChallenge challenge: GKChallenge) ``` |
| To | ``` optional func player(_ player: GKPlayer, wantsToPlay challenge: GKChallenge) ``` |

Modified [GKChallengeState [enum]](https://developer.apple.com/documentation/gamekit/gkchallengestate)

|  | Declaration |
| --- | --- |
| From | ``` enum GKChallengeState : Int {     case Invalid     case Pending     case Completed     case Declined } ``` |
| To | ``` enum GKChallengeState : Int {     case invalid     case pending     case completed     case declined } ``` |

Modified [GKChallengeState.completed](https://developer.apple.com/documentation/gamekit/gkchallengestate/completed)

|  | Declaration |
| --- | --- |
| From | ``` case Completed ``` |
| To | ``` case completed ``` |

Modified [GKChallengeState.declined](https://developer.apple.com/documentation/gamekit/gkchallengestate/declined)

|  | Declaration |
| --- | --- |
| From | ``` case Declined ``` |
| To | ``` case declined ``` |

Modified [GKChallengeState.invalid](https://developer.apple.com/documentation/gamekit/gkchallengestate/invalid)

|  | Declaration |
| --- | --- |
| From | ``` case Invalid ``` |
| To | ``` case invalid ``` |

Modified [GKChallengeState.pending](https://developer.apple.com/documentation/gamekit/gkchallengestate/pending)

|  | Declaration |
| --- | --- |
| From | ``` case Pending ``` |
| To | ``` case pending ``` |

Modified [GKError.Code [enum]](https://developer.apple.com/documentation/gamekit/gkerrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum GKErrorCode : Int {     case Unknown     case Cancelled     case CommunicationsFailure     case UserDenied     case InvalidCredentials     case NotAuthenticated     case AuthenticationInProgress     case InvalidPlayer     case ScoreNotSet     case ParentalControlsBlocked     case PlayerStatusExceedsMaximumLength     case PlayerStatusInvalid     case MatchRequestInvalid     case Underage     case GameUnrecognized     case NotSupported     case InvalidParameter     case UnexpectedConnection     case ChallengeInvalid     case TurnBasedMatchDataTooLarge     case TurnBasedTooManySessions     case TurnBasedInvalidParticipant     case TurnBasedInvalidTurn     case TurnBasedInvalidState     case InvitationsDisabled     case PlayerPhotoFailure     case UbiquityContainerUnavailable } extension GKErrorCode : _BridgedNSError { } extension GKErrorCode : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = GKError         case unknown         case cancelled         case communicationsFailure         case userDenied         case invalidCredentials         case notAuthenticated         case authenticationInProgress         case invalidPlayer         case scoreNotSet         case parentalControlsBlocked         case playerStatusExceedsMaximumLength         case playerStatusInvalid         case matchRequestInvalid         case underage         case gameUnrecognized         case notSupported         case invalidParameter         case unexpectedConnection         case challengeInvalid         case turnBasedMatchDataTooLarge         case turnBasedTooManySessions         case turnBasedInvalidParticipant         case turnBasedInvalidTurn         case turnBasedInvalidState         case invitationsDisabled         case playerPhotoFailure         case ubiquityContainerUnavailable         case matchNotConnected         case gameSessionRequestInvalid     } ``` |

Modified [GKError.Code.authenticationInProgress](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorauthenticationinprogress)

|  | Declaration |
| --- | --- |
| From | ``` case AuthenticationInProgress ``` |
| To | ``` case authenticationInProgress ``` |

Modified [GKError.Code.cancelled](https://developer.apple.com/documentation/gamekit/gkerror/code/cancelled)

|  | Declaration |
| --- | --- |
| From | ``` case Cancelled ``` |
| To | ``` case cancelled ``` |

Modified [GKError.Code.challengeInvalid](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorchallengeinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case ChallengeInvalid ``` |
| To | ``` case challengeInvalid ``` |

Modified [GKError.Code.communicationsFailure](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorcommunicationsfailure)

|  | Declaration |
| --- | --- |
| From | ``` case CommunicationsFailure ``` |
| To | ``` case communicationsFailure ``` |

Modified [GKError.Code.gameUnrecognized](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorgameunrecognized)

|  | Declaration |
| --- | --- |
| From | ``` case GameUnrecognized ``` |
| To | ``` case gameUnrecognized ``` |

Modified [GKError.Code.invalidCredentials](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorinvalidcredentials)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidCredentials ``` |
| To | ``` case invalidCredentials ``` |

Modified [GKError.Code.invalidParameter](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorinvalidparameter)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case InvalidParameter ``` | tvOS 9.0 |
| To | ``` case invalidParameter ``` | tvOS 10.0 |

Modified [GKError.Code.invalidPlayer](https://developer.apple.com/documentation/gamekit/gkerror/code/invalidplayer)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidPlayer ``` |
| To | ``` case invalidPlayer ``` |

Modified [GKError.Code.invitationsDisabled](https://developer.apple.com/documentation/gamekit/gkerror/code/invitationsdisabled)

|  | Declaration |
| --- | --- |
| From | ``` case InvitationsDisabled ``` |
| To | ``` case invitationsDisabled ``` |

Modified [GKError.Code.matchRequestInvalid](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrormatchrequestinvalid)

|  | Declaration |
| --- | --- |
| From | ``` case MatchRequestInvalid ``` |
| To | ``` case matchRequestInvalid ``` |

Modified [GKError.Code.notAuthenticated](https://developer.apple.com/documentation/gamekit/gkerror/code/notauthenticated)

|  | Declaration |
| --- | --- |
| From | ``` case NotAuthenticated ``` |
| To | ``` case notAuthenticated ``` |

Modified [GKError.Code.notSupported](https://developer.apple.com/documentation/gamekit/gkerror/code/notsupported)

|  | Declaration |
| --- | --- |
| From | ``` case NotSupported ``` |
| To | ``` case notSupported ``` |

Modified [GKError.Code.parentalControlsBlocked](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorparentalcontrolsblocked)

|  | Declaration |
| --- | --- |
| From | ``` case ParentalControlsBlocked ``` |
| To | ``` case parentalControlsBlocked ``` |

Modified [GKError.Code.playerPhotoFailure](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorplayerphotofailure)

|  | Declaration |
| --- | --- |
| From | ``` case PlayerPhotoFailure ``` |
| To | ``` case playerPhotoFailure ``` |

Modified [GKError.Code.playerStatusExceedsMaximumLength](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorplayerstatusexceedsmaximumlength)

|  | Declaration |
| --- | --- |
| From | ``` case PlayerStatusExceedsMaximumLength ``` |
| To | ``` case playerStatusExceedsMaximumLength ``` |

Modified [GKError.Code.playerStatusInvalid](https://developer.apple.com/documentation/gamekit/gkerror/code/playerstatusinvalid)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case PlayerStatusInvalid ``` | tvOS 9.0 |
| To | ``` case playerStatusInvalid ``` | tvOS 10.0 |

Modified [GKError.Code.scoreNotSet](https://developer.apple.com/documentation/gamekit/gkerror/code/scorenotset)

|  | Declaration |
| --- | --- |
| From | ``` case ScoreNotSet ``` |
| To | ``` case scoreNotSet ``` |

Modified [GKError.Code.turnBasedInvalidParticipant](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorturnbasedinvalidparticipant)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case TurnBasedInvalidParticipant ``` | tvOS 9.0 |
| To | ``` case turnBasedInvalidParticipant ``` | tvOS 10.0 |

Modified [GKError.Code.turnBasedInvalidState](https://developer.apple.com/documentation/gamekit/gkerror/code/turnbasedinvalidstate)

|  | Declaration |
| --- | --- |
| From | ``` case TurnBasedInvalidState ``` |
| To | ``` case turnBasedInvalidState ``` |

Modified [GKError.Code.turnBasedInvalidTurn](https://developer.apple.com/documentation/gamekit/gkerror/code/turnbasedinvalidturn)

|  | Declaration |
| --- | --- |
| From | ``` case TurnBasedInvalidTurn ``` |
| To | ``` case turnBasedInvalidTurn ``` |

Modified [GKError.Code.turnBasedMatchDataTooLarge](https://developer.apple.com/documentation/gamekit/gkerror/code/turnbasedmatchdatatoolarge)

|  | Declaration |
| --- | --- |
| From | ``` case TurnBasedMatchDataTooLarge ``` |
| To | ``` case turnBasedMatchDataTooLarge ``` |

Modified [GKError.Code.turnBasedTooManySessions](https://developer.apple.com/documentation/gamekit/gkerror/code/turnbasedtoomanysessions)

|  | Declaration |
| --- | --- |
| From | ``` case TurnBasedTooManySessions ``` |
| To | ``` case turnBasedTooManySessions ``` |

Modified [GKError.Code.ubiquityContainerUnavailable](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorubiquitycontainerunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case UbiquityContainerUnavailable ``` |
| To | ``` case ubiquityContainerUnavailable ``` |

Modified [GKError.Code.underage](https://developer.apple.com/documentation/gamekit/gkerror/code/underage)

|  | Declaration |
| --- | --- |
| From | ``` case Underage ``` |
| To | ``` case underage ``` |

Modified [GKError.Code.unexpectedConnection](https://developer.apple.com/documentation/gamekit/gkerror/code/unexpectedconnection)

|  | Declaration |
| --- | --- |
| From | ``` case UnexpectedConnection ``` |
| To | ``` case unexpectedConnection ``` |

Modified [GKError.Code.unknown](https://developer.apple.com/documentation/gamekit/gkerror/code/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [GKError.Code.userDenied](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerroruserdenied)

|  | Declaration |
| --- | --- |
| From | ``` case UserDenied ``` |
| To | ``` case userDenied ``` |

Modified [GKFriendRequestComposeViewController.addRecipients(withEmailAddresses: [String])](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437190-addrecipientswithemailaddresses)

|  | Declaration |
| --- | --- |
| From | ``` func addRecipientsWithEmailAddresses(_ emailAddresses: [String]) ``` |
| To | ``` func addRecipients(withEmailAddresses emailAddresses: [String]) ``` |

Modified [GKGameCenterViewController](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class GKGameCenterViewController : UINavigationController { } extension GKGameCenterViewController {     unowned(unsafe) var gameCenterDelegate: GKGameCenterControllerDelegate?     var viewState: GKGameCenterViewControllerState } extension GKGameCenterViewController {     var leaderboardTimeScope: GKLeaderboardTimeScope     var leaderboardIdentifier: String?     var leaderboardCategory: String? } ``` |
| To | ``` class GKGameCenterViewController : UINavigationController {     var leaderboardTimeScope: GKLeaderboardTimeScope     var leaderboardIdentifier: String?     var leaderboardCategory: String?     unowned(unsafe) var gameCenterDelegate: GKGameCenterControllerDelegate?     var viewState: GKGameCenterViewControllerState } extension GKGameCenterViewController {     unowned(unsafe) var gameCenterDelegate: GKGameCenterControllerDelegate?     var viewState: GKGameCenterViewControllerState } extension GKGameCenterViewController {     var leaderboardTimeScope: GKLeaderboardTimeScope     var leaderboardIdentifier: String?     var leaderboardCategory: String? } ``` |

Modified [GKGameCenterViewControllerState [enum]](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate)

|  | Declaration |
| --- | --- |
| From | ``` enum GKGameCenterViewControllerState : Int {     case Default     case Leaderboards     case Achievements     case Challenges } ``` |
| To | ``` enum GKGameCenterViewControllerState : Int {     case `default`     case leaderboards     case achievements     case challenges } ``` |

Modified [GKGameCenterViewControllerState.achievements](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate/achievements)

|  | Declaration |
| --- | --- |
| From | ``` case Achievements ``` |
| To | ``` case achievements ``` |

Modified [GKGameCenterViewControllerState.challenges](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate/gkgamecenterviewcontrollerstatechallenges)

|  | Declaration |
| --- | --- |
| From | ``` case Challenges ``` |
| To | ``` case challenges ``` |

Modified [GKGameCenterViewControllerState.default](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate/gkgamecenterviewcontrollerstatedefault)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [GKGameCenterViewControllerState.leaderboards](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate/gkgamecenterviewcontrollerstateleaderboards)

|  | Declaration |
| --- | --- |
| From | ``` case Leaderboards ``` |
| To | ``` case leaderboards ``` |

Modified [GKInvite](https://developer.apple.com/documentation/gamekit/gkinvite)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKInvite : NSObject {     var sender: GKPlayer { get }     var inviter: String { get }     var hosted: Bool { get }     var playerGroup: Int { get }     var playerAttributes: UInt32 { get } } ``` | -- |
| To | ``` class GKInvite : NSObject {     var sender: GKPlayer { get }     var inviter: String { get }     var isHosted: Bool { get }     var playerGroup: Int { get }     var playerAttributes: UInt32 { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKInvite : CVarArg { } extension GKInvite : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GKInvite.isHosted](https://developer.apple.com/documentation/gamekit/gkinvite/1520458-hosted)

|  | Declaration |
| --- | --- |
| From | ``` var hosted: Bool { get } ``` |
| To | ``` var isHosted: Bool { get } ``` |

Modified [GKInviteEventListener](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKInviteEventListener {     optional func player(_ player: GKPlayer, didAcceptInvite invite: GKInvite)     optional func player(_ player: GKPlayer, didRequestMatchWithRecipients recipientPlayers: [GKPlayer])     optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String]) } ``` |
| To | ``` protocol GKInviteEventListener {     optional func player(_ player: GKPlayer, didAccept invite: GKInvite)     optional func player(_ player: GKPlayer, didRequestMatchWithRecipients recipientPlayers: [GKPlayer])     optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String]) } ``` |

Modified [GKInviteEventListener.player(_: GKPlayer, didAccept: GKInvite)](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520672-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer, didAcceptInvite invite: GKInvite) ``` |
| To | ``` optional func player(_ player: GKPlayer, didAccept invite: GKInvite) ``` |

Modified [GKInviteRecipientResponse [enum]](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse)

|  | Declaration |
| --- | --- |
| From | ``` enum GKInviteRecipientResponse : Int {     case InviteRecipientResponseAccepted     case InviteRecipientResponseDeclined     case InviteRecipientResponseFailed     case InviteRecipientResponseIncompatible     case InviteRecipientResponseUnableToConnect     case InviteRecipientResponseNoAnswer     static var InviteeResponseAccepted: GKInviteRecipientResponse { get }     static var InviteeResponseDeclined: GKInviteRecipientResponse { get }     static var InviteeResponseFailed: GKInviteRecipientResponse { get }     static var InviteeResponseIncompatible: GKInviteRecipientResponse { get }     static var InviteeResponseUnableToConnect: GKInviteRecipientResponse { get }     static var InviteeResponseNoAnswer: GKInviteRecipientResponse { get } } ``` |
| To | ``` enum GKInviteRecipientResponse : Int {     case inviteRecipientResponseAccepted     case inviteRecipientResponseDeclined     case inviteRecipientResponseFailed     case inviteRecipientResponseIncompatible     case inviteRecipientResponseUnableToConnect     case inviteRecipientResponseNoAnswer     static var inviteeResponseAccepted: GKInviteRecipientResponse { get }     static var inviteeResponseDeclined: GKInviteRecipientResponse { get }     static var inviteeResponseFailed: GKInviteRecipientResponse { get }     static var inviteeResponseIncompatible: GKInviteRecipientResponse { get }     static var inviteeResponseUnableToConnect: GKInviteRecipientResponse { get }     static var inviteeResponseNoAnswer: GKInviteRecipientResponse { get } } ``` |

Modified [GKInviteRecipientResponse.inviteeResponseAccepted](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponseaccepted)

|  | Declaration |
| --- | --- |
| From | ``` static var InviteeResponseAccepted: GKInviteRecipientResponse { get } ``` |
| To | ``` static var inviteeResponseAccepted: GKInviteRecipientResponse { get } ``` |

Modified [GKInviteRecipientResponse.inviteeResponseDeclined](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/1520841-inviteeresponsedeclined)

|  | Declaration |
| --- | --- |
| From | ``` static var InviteeResponseDeclined: GKInviteRecipientResponse { get } ``` |
| To | ``` static var inviteeResponseDeclined: GKInviteRecipientResponse { get } ``` |

Modified [GKInviteRecipientResponse.inviteeResponseFailed](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponsefailed)

|  | Declaration |
| --- | --- |
| From | ``` static var InviteeResponseFailed: GKInviteRecipientResponse { get } ``` |
| To | ``` static var inviteeResponseFailed: GKInviteRecipientResponse { get } ``` |

Modified [GKInviteRecipientResponse.inviteeResponseIncompatible](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponseincompatible)

|  | Declaration |
| --- | --- |
| From | ``` static var InviteeResponseIncompatible: GKInviteRecipientResponse { get } ``` |
| To | ``` static var inviteeResponseIncompatible: GKInviteRecipientResponse { get } ``` |

Modified [GKInviteRecipientResponse.inviteeResponseNoAnswer](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/1520715-inviteeresponsenoanswer)

|  | Declaration |
| --- | --- |
| From | ``` static var InviteeResponseNoAnswer: GKInviteRecipientResponse { get } ``` |
| To | ``` static var inviteeResponseNoAnswer: GKInviteRecipientResponse { get } ``` |

Modified [GKInviteRecipientResponse.inviteeResponseUnableToConnect](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponseunabletoconnect)

|  | Declaration |
| --- | --- |
| From | ``` static var InviteeResponseUnableToConnect: GKInviteRecipientResponse { get } ``` |
| To | ``` static var inviteeResponseUnableToConnect: GKInviteRecipientResponse { get } ``` |

Modified [GKInviteRecipientResponse.inviteRecipientResponseAccepted](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviterecipientresponseaccepted)

|  | Declaration |
| --- | --- |
| From | ``` case InviteRecipientResponseAccepted ``` |
| To | ``` case inviteRecipientResponseAccepted ``` |

Modified [GKInviteRecipientResponse.inviteRecipientResponseDeclined](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponsedeclined)

|  | Declaration |
| --- | --- |
| From | ``` case InviteRecipientResponseDeclined ``` |
| To | ``` case inviteRecipientResponseDeclined ``` |

Modified [GKInviteRecipientResponse.inviteRecipientResponseFailed](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponsefailed)

|  | Declaration |
| --- | --- |
| From | ``` case InviteRecipientResponseFailed ``` |
| To | ``` case inviteRecipientResponseFailed ``` |

Modified [GKInviteRecipientResponse.inviteRecipientResponseIncompatible](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponseincompatible)

|  | Declaration |
| --- | --- |
| From | ``` case InviteRecipientResponseIncompatible ``` |
| To | ``` case inviteRecipientResponseIncompatible ``` |

Modified [GKInviteRecipientResponse.inviteRecipientResponseNoAnswer](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviterecipientresponsenoanswer)

|  | Declaration |
| --- | --- |
| From | ``` case InviteRecipientResponseNoAnswer ``` |
| To | ``` case inviteRecipientResponseNoAnswer ``` |

Modified [GKInviteRecipientResponse.inviteRecipientResponseUnableToConnect](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponseunabletoconnect)

|  | Declaration |
| --- | --- |
| From | ``` case InviteRecipientResponseUnableToConnect ``` |
| To | ``` case inviteRecipientResponseUnableToConnect ``` |

Modified [GKLeaderboard](https://developer.apple.com/documentation/gamekit/gkleaderboard)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKLeaderboard : NSObject {     var timeScope: GKLeaderboardTimeScope     var playerScope: GKLeaderboardPlayerScope     var identifier: String?     var title: String? { get }     var range: NSRange     var scores: [GKScore]? { get }     var maxRange: Int { get }     var localPlayerScore: GKScore? { get }     var loading: Bool { get }     var groupIdentifier: String? { get }     init()     init(players players: [GKPlayer])     func loadScoresWithCompletionHandler(_ completionHandler: (([GKScore]?, NSError?) -> Void)?)     class func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([GKLeaderboard]?, NSError?) -> Void)?) } extension GKLeaderboard {     var category: String?     init?(playerIDs playerIDs: [String]?)     class func loadCategoriesWithCompletionHandler(_ completionHandler: (([String]?, [String]?, NSError?) -> Void)?)     class func setDefaultLeaderboard(_ leaderboardIdentifier: String?, withCompletionHandler completionHandler: ((NSError?) -> Void)?) } extension GKLeaderboard {     func loadImageWithCompletionHandler(_ completionHandler: ((UIImage?, NSError?) -> Void)?) } ``` | -- |
| To | ``` class GKLeaderboard : NSObject {     var timeScope: GKLeaderboardTimeScope     var playerScope: GKLeaderboardPlayerScope     var identifier: String?     var title: String? { get }     var range: NSRange     var scores: [GKScore]? { get }     var maxRange: Int { get }     var localPlayerScore: GKScore? { get }     var isLoading: Bool { get }     var groupIdentifier: String? { get }     init()     init(players players: [GKPlayer])     func loadScores(completionHandler completionHandler: (@escaping ([GKScore]?, Error?) -> Swift.Void)? = nil)     class func loadLeaderboards(completionHandler completionHandler: (@escaping ([GKLeaderboard]?, Error?) -> Swift.Void)? = nil)     func loadImage(completionHandler completionHandler: (@escaping (UIImage?, Error?) -> Swift.Void)? = nil)     var category: String?     init?(playerIDs playerIDs: [String]?)     class func loadCategories(completionHandler completionHandler: (@escaping ([String]?, [String]?, Error?) -> Swift.Void)? = nil)     class func setDefault(_ leaderboardIdentifier: String?, withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKLeaderboard : CVarArg { } extension GKLeaderboard : Equatable, Hashable {     var hashValue: Int { get } } extension GKLeaderboard {     var category: String?     init?(playerIDs playerIDs: [String]?)     class func loadCategories(completionHandler completionHandler: (@escaping ([String]?, [String]?, Error?) -> Swift.Void)? = nil)     class func setDefault(_ leaderboardIdentifier: String?, withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) } extension GKLeaderboard {     func loadImage(completionHandler completionHandler: (@escaping (UIImage?, Error?) -> Swift.Void)? = nil) } ``` | CVarArg, Equatable, Hashable |

Modified [GKLeaderboard.isLoading](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503163-loading)

|  | Declaration |
| --- | --- |
| From | ``` var loading: Bool { get } ``` |
| To | ``` var isLoading: Bool { get } ``` |

Modified [GKLeaderboard.loadLeaderboards(completionHandler: ( ([GKLeaderboard]?, Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503128-loadleaderboardswithcompletionha)

|  | Declaration |
| --- | --- |
| From | ``` class func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([GKLeaderboard]?, NSError?) -> Void)?) ``` |
| To | ``` class func loadLeaderboards(completionHandler completionHandler: (@escaping ([GKLeaderboard]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKLeaderboard.loadScores(completionHandler: ( ([GKScore]?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503160-loadscores)

|  | Declaration |
| --- | --- |
| From | ``` func loadScoresWithCompletionHandler(_ completionHandler: (([GKScore]?, NSError?) -> Void)?) ``` |
| To | ``` func loadScores(completionHandler completionHandler: (@escaping ([GKScore]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKLeaderboardPlayerScope [enum]](https://developer.apple.com/documentation/gamekit/gkleaderboardplayerscope)

|  | Declaration |
| --- | --- |
| From | ``` enum GKLeaderboardPlayerScope : Int {     case Global     case FriendsOnly } ``` |
| To | ``` enum GKLeaderboardPlayerScope : Int {     case global     case friendsOnly } ``` |

Modified [GKLeaderboardPlayerScope.friendsOnly](https://developer.apple.com/documentation/gamekit/gkleaderboardplayerscope/friendsonly)

|  | Declaration |
| --- | --- |
| From | ``` case FriendsOnly ``` |
| To | ``` case friendsOnly ``` |

Modified [GKLeaderboardPlayerScope.global](https://developer.apple.com/documentation/gamekit/gkleaderboardplayerscope/gkleaderboardplayerscopeglobal)

|  | Declaration |
| --- | --- |
| From | ``` case Global ``` |
| To | ``` case global ``` |

Modified [GKLeaderboardSet](https://developer.apple.com/documentation/gamekit/gkleaderboardset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKLeaderboardSet : NSObject, NSCoding, NSSecureCoding {     var title: String { get }     var groupIdentifier: String? { get }     var identifier: String?     class func loadLeaderboardSetsWithCompletionHandler(_ completionHandler: (([GKLeaderboardSet]?, NSError?) -> Void)?)     func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([GKLeaderboard]?, NSError?) -> Void)?) } extension GKLeaderboardSet {     func loadImageWithCompletionHandler(_ completionHandler: ((UIImage?, NSError?) -> Void)?) } ``` | NSCoding, NSSecureCoding |
| To | ``` class GKLeaderboardSet : NSObject, NSCoding, NSSecureCoding {     var title: String { get }     var groupIdentifier: String? { get }     var identifier: String?     class func loadLeaderboardSets(completionHandler completionHandler: (@escaping ([GKLeaderboardSet]?, Error?) -> Swift.Void)? = nil)     func loadLeaderboards(completionHandler completionHandler: (@escaping ([GKLeaderboard]?, Error?) -> Swift.Void)? = nil)     func loadImage(completionHandler completionHandler: (@escaping (UIImage?, Error?) -> Swift.Void)? = nil)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKLeaderboardSet : CVarArg { } extension GKLeaderboardSet : Equatable, Hashable {     var hashValue: Int { get } } extension GKLeaderboardSet {     func loadImage(completionHandler completionHandler: (@escaping (UIImage?, Error?) -> Swift.Void)? = nil) } ``` | CVarArg, Equatable, Hashable, NSCoding, NSSecureCoding |

Modified [GKLeaderboardSet.loadLeaderboards(completionHandler: ( ([GKLeaderboard]?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451810-loadleaderboardswithcompletionha)

|  | Declaration |
| --- | --- |
| From | ``` func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([GKLeaderboard]?, NSError?) -> Void)?) ``` |
| To | ``` func loadLeaderboards(completionHandler completionHandler: (@escaping ([GKLeaderboard]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKLeaderboardSet.loadLeaderboardSets(completionHandler: ( ([GKLeaderboardSet]?, Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451798-loadleaderboardsets)

|  | Declaration |
| --- | --- |
| From | ``` class func loadLeaderboardSetsWithCompletionHandler(_ completionHandler: (([GKLeaderboardSet]?, NSError?) -> Void)?) ``` |
| To | ``` class func loadLeaderboardSets(completionHandler completionHandler: (@escaping ([GKLeaderboardSet]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKLeaderboardTimeScope [enum]](https://developer.apple.com/documentation/gamekit/gkleaderboardtimescope)

|  | Declaration |
| --- | --- |
| From | ``` enum GKLeaderboardTimeScope : Int {     case Today     case Week     case AllTime } ``` |
| To | ``` enum GKLeaderboardTimeScope : Int {     case today     case week     case allTime } ``` |

Modified [GKLeaderboardTimeScope.allTime](https://developer.apple.com/documentation/gamekit/gkleaderboardtimescope/gkleaderboardtimescopealltime)

|  | Declaration |
| --- | --- |
| From | ``` case AllTime ``` |
| To | ``` case allTime ``` |

Modified [GKLeaderboardTimeScope.today](https://developer.apple.com/documentation/gamekit/gkleaderboardtimescope/today)

|  | Declaration |
| --- | --- |
| From | ``` case Today ``` |
| To | ``` case today ``` |

Modified [GKLeaderboardTimeScope.week](https://developer.apple.com/documentation/gamekit/gkleaderboardtimescope/week)

|  | Declaration |
| --- | --- |
| From | ``` case Week ``` |
| To | ``` case week ``` |

Modified [GKLocalPlayer](https://developer.apple.com/documentation/gamekit/gklocalplayer)

|  | Declaration |
| --- | --- |
| From | ``` class GKLocalPlayer : GKPlayer {     class func localPlayer() -> GKLocalPlayer     var authenticated: Bool { get }     var underage: Bool { get }     var authenticateHandler: ((UIViewController?, NSError?) -> Void)?     func loadFriendPlayersWithCompletionHandler(_ completionHandler: (([GKPlayer]?, NSError?) -> Void)?)     func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String, completionHandler completionHandler: ((NSError?) -> Void)?)     func loadDefaultLeaderboardIdentifierWithCompletionHandler(_ completionHandler: ((String?, NSError?) -> Void)?)     func generateIdentityVerificationSignatureWithCompletionHandler(_ completionHandler: ((NSURL?, NSData?, NSData?, UInt64, NSError?) -> Void)?) } extension GKLocalPlayer {     func registerListener(_ listener: GKLocalPlayerListener)     func unregisterListener(_ listener: GKLocalPlayerListener)     func unregisterAllListeners() } extension GKLocalPlayer {     func setDefaultLeaderboardCategoryID(_ categoryID: String?, completionHandler completionHandler: ((NSError?) -> Void)?)     func loadDefaultLeaderboardCategoryIDWithCompletionHandler(_ completionHandler: ((String?, NSError?) -> Void)?)     func loadFriendsWithCompletionHandler(_ completionHandler: (([String]?, NSError?) -> Void)?)     func authenticateWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     var friends: [String]? { get } } extension GKLocalPlayer : GKSavedGameListener {     func fetchSavedGamesWithCompletionHandler(_ handler: (([GKSavedGame]?, NSError?) -> Void)?)     func saveGameData(_ data: NSData, withName name: String, completionHandler handler: ((GKSavedGame?, NSError?) -> Void)?)     func deleteSavedGamesWithName(_ name: String, completionHandler handler: ((NSError?) -> Void)?)     func resolveConflictingSavedGames(_ conflictingSavedGames: [GKSavedGame], withData data: NSData, completionHandler handler: (([GKSavedGame]?, NSError?) -> Void)?) } ``` |
| To | ``` class GKLocalPlayer : GKPlayer {     class func localPlayer() -> GKLocalPlayer     var isAuthenticated: Bool { get }     var isUnderage: Bool { get }     var authenticateHandler: ((UIViewController?, Error?) -> Swift.Void)?     func loadRecentPlayers(completionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil)     func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func loadDefaultLeaderboardIdentifier(completionHandler completionHandler: (@escaping (String?, Error?) -> Swift.Void)? = nil)     func generateIdentityVerificationSignature(completionHandler completionHandler: (@escaping (URL?, Data?, Data?, UInt64, Error?) -> Swift.Void)? = nil)     func setDefaultLeaderboardCategoryID(_ categoryID: String?, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func loadDefaultLeaderboardCategoryID(completionHandler completionHandler: (@escaping (String?, Error?) -> Swift.Void)? = nil)     func loadFriends(completionHandler completionHandler: (@escaping ([String]?, Error?) -> Swift.Void)? = nil)     func authenticate(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     var friends: [String]? { get }     func loadFriendPlayers(completionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil)     func register(_ listener: GKLocalPlayerListener)     func unregisterListener(_ listener: GKLocalPlayerListener)     func unregisterAllListeners()     var isFriend: Bool { get }     func loadPhoto(forSize size: GKPhotoSize, withCompletionHandler completionHandler: (@escaping (UIImage?, Error?) -> Void)? = nil) } extension GKLocalPlayer : GKSavedGameListener {     func fetchSavedGames(completionHandler handler: (@escaping ([GKSavedGame]?, Error?) -> Swift.Void)? = nil)     func saveGameData(_ data: Data, withName name: String, completionHandler handler: (@escaping (GKSavedGame?, Error?) -> Swift.Void)? = nil)     func deleteSavedGames(withName name: String, completionHandler handler: (@escaping (Error?) -> Swift.Void)? = nil)     func resolveConflictingSavedGames(_ conflictingSavedGames: [GKSavedGame], with data: Data, completionHandler handler: (@escaping ([GKSavedGame]?, Error?) -> Swift.Void)? = nil) } extension GKLocalPlayer {     func register(_ listener: GKLocalPlayerListener)     func unregisterListener(_ listener: GKLocalPlayerListener)     func unregisterAllListeners() } extension GKLocalPlayer {     func setDefaultLeaderboardCategoryID(_ categoryID: String?, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func loadDefaultLeaderboardCategoryID(completionHandler completionHandler: (@escaping (String?, Error?) -> Swift.Void)? = nil)     func loadFriends(completionHandler completionHandler: (@escaping ([String]?, Error?) -> Swift.Void)? = nil)     func authenticate(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     var friends: [String]? { get }     func loadFriendPlayers(completionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil) } extension GKLocalPlayer : GKSavedGameListener {     func fetchSavedGames(completionHandler handler: (@escaping ([GKSavedGame]?, Error?) -> Swift.Void)? = nil)     func saveGameData(_ data: Data, withName name: String, completionHandler handler: (@escaping (GKSavedGame?, Error?) -> Swift.Void)? = nil)     func deleteSavedGames(withName name: String, completionHandler handler: (@escaping (Error?) -> Swift.Void)? = nil)     func resolveConflictingSavedGames(_ conflictingSavedGames: [GKSavedGame], with data: Data, completionHandler handler: (@escaping ([GKSavedGame]?, Error?) -> Swift.Void)? = nil) } ``` |

Modified [GKLocalPlayer.authenticateHandler](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515399-authenticatehandler)

|  | Declaration |
| --- | --- |
| From | ``` var authenticateHandler: ((UIViewController?, NSError?) -> Void)? ``` |
| To | ``` var authenticateHandler: ((UIViewController?, Error?) -> Swift.Void)? ``` |

Modified [GKLocalPlayer.generateIdentityVerificationSignature(completionHandler: ( (URL?, Data?, Data?, UInt64, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515407-generateidentityverificationsign)

|  | Declaration |
| --- | --- |
| From | ``` func generateIdentityVerificationSignatureWithCompletionHandler(_ completionHandler: ((NSURL?, NSData?, NSData?, UInt64, NSError?) -> Void)?) ``` |
| To | ``` func generateIdentityVerificationSignature(completionHandler completionHandler: (@escaping (URL?, Data?, Data?, UInt64, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKLocalPlayer.isAuthenticated](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515402-authenticated)

|  | Declaration |
| --- | --- |
| From | ``` var authenticated: Bool { get } ``` |
| To | ``` var isAuthenticated: Bool { get } ``` |

Modified [GKLocalPlayer.isUnderage](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515394-isunderage)

|  | Declaration |
| --- | --- |
| From | ``` var underage: Bool { get } ``` |
| To | ``` var isUnderage: Bool { get } ``` |

Modified [GKLocalPlayer.loadDefaultLeaderboardIdentifier(completionHandler: ( (String?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515404-loaddefaultleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func loadDefaultLeaderboardIdentifierWithCompletionHandler(_ completionHandler: ((String?, NSError?) -> Void)?) ``` |
| To | ``` func loadDefaultLeaderboardIdentifier(completionHandler completionHandler: (@escaping (String?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKLocalPlayer.loadFriendPlayers(completionHandler: ( ([GKPlayer]?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515386-loadfriendplayerswithcompletionh)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func loadFriendPlayersWithCompletionHandler(_ completionHandler: (([GKPlayer]?, NSError?) -> Void)?) ``` | -- |
| To | ``` func loadFriendPlayers(completionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil) ``` | tvOS 10.0 |

Modified [GKLocalPlayer.register(_: GKLocalPlayerListener)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515393-register)

|  | Declaration |
| --- | --- |
| From | ``` func registerListener(_ listener: GKLocalPlayerListener) ``` |
| To | ``` func register(_ listener: GKLocalPlayerListener) ``` |

Modified [GKLocalPlayer.setDefaultLeaderboardIdentifier(_: String, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515408-setdefaultleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKMatch](https://developer.apple.com/documentation/gamekit/gkmatch)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKMatch : NSObject {     var players: [GKPlayer] { get }     unowned(unsafe) var delegate: GKMatchDelegate?     var expectedPlayerCount: Int { get }     func sendData(_ data: NSData, toPlayers players: [GKPlayer], dataMode mode: GKMatchSendDataMode) throws     func sendDataToAllPlayers(_ data: NSData, withDataMode mode: GKMatchSendDataMode) throws     func disconnect()     func voiceChatWithName(_ name: String) -> GKVoiceChat?     func chooseBestHostingPlayerWithCompletionHandler(_ completionHandler: (GKPlayer?) -> Void)     func rematchWithCompletionHandler(_ completionHandler: ((GKMatch?, NSError?) -> Void)?) } extension GKMatch {     func chooseBestHostPlayerWithCompletionHandler(_ completionHandler: (String?) -> Void)     func sendData(_ data: NSData, toPlayers playerIDs: [String], withDataMode mode: GKMatchSendDataMode) throws     var playerIDs: [String] { get } } ``` | -- |
| To | ``` class GKMatch : NSObject {     var players: [GKPlayer] { get }     unowned(unsafe) var delegate: GKMatchDelegate?     var expectedPlayerCount: Int { get }     func send(_ data: Data, to players: [GKPlayer], dataMode mode: GKMatchSendDataMode) throws     func sendData(toAllPlayers data: Data, with mode: GKMatchSendDataMode) throws     func disconnect()     func voiceChat(withName name: String) -> GKVoiceChat?     func chooseBestHostingPlayer(completionHandler completionHandler: @escaping (GKPlayer?) -> Swift.Void)     func rematch(completionHandler completionHandler: (@escaping (GKMatch?, Error?) -> Swift.Void)? = nil)     func chooseBestHostPlayer(completionHandler completionHandler: @escaping (String?) -> Swift.Void)     func send(_ data: Data, toPlayers playerIDs: [String], with mode: GKMatchSendDataMode) throws     var playerIDs: [String] { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKMatch : CVarArg { } extension GKMatch : Equatable, Hashable {     var hashValue: Int { get } } extension GKMatch {     func chooseBestHostPlayer(completionHandler completionHandler: @escaping (String?) -> Swift.Void)     func send(_ data: Data, toPlayers playerIDs: [String], with mode: GKMatchSendDataMode) throws     var playerIDs: [String] { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GKMatch.chooseBestHostingPlayer(completionHandler: (GKPlayer?) -> Swift.Void)](https://developer.apple.com/documentation/gamekit/gkmatch/1502072-choosebesthostingplayerwithcompl)

|  | Declaration |
| --- | --- |
| From | ``` func chooseBestHostingPlayerWithCompletionHandler(_ completionHandler: (GKPlayer?) -> Void) ``` |
| To | ``` func chooseBestHostingPlayer(completionHandler completionHandler: @escaping (GKPlayer?) -> Swift.Void) ``` |

Modified [GKMatch.rematch(completionHandler: ( (GKMatch?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkmatch/1502042-rematch)

|  | Declaration |
| --- | --- |
| From | ``` func rematchWithCompletionHandler(_ completionHandler: ((GKMatch?, NSError?) -> Void)?) ``` |
| To | ``` func rematch(completionHandler completionHandler: (@escaping (GKMatch?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKMatch.send(_: Data, to: [GKPlayer], dataMode: GKMatchSendDataMode) throws](https://developer.apple.com/documentation/gamekit/gkmatch/1502056-senddata)

|  | Declaration |
| --- | --- |
| From | ``` func sendData(_ data: NSData, toPlayers players: [GKPlayer], dataMode mode: GKMatchSendDataMode) throws ``` |
| To | ``` func send(_ data: Data, to players: [GKPlayer], dataMode mode: GKMatchSendDataMode) throws ``` |

Modified [GKMatch.sendData(toAllPlayers: Data, with: GKMatchSendDataMode) throws](https://developer.apple.com/documentation/gamekit/gkmatch/1502029-senddata)

|  | Declaration |
| --- | --- |
| From | ``` func sendDataToAllPlayers(_ data: NSData, withDataMode mode: GKMatchSendDataMode) throws ``` |
| To | ``` func sendData(toAllPlayers data: Data, with mode: GKMatchSendDataMode) throws ``` |

Modified [GKMatch.voiceChat(withName: String) -> GKVoiceChat?](https://developer.apple.com/documentation/gamekit/gkmatch/1502066-voicechatwithname)

|  | Declaration |
| --- | --- |
| From | ``` func voiceChatWithName(_ name: String) -> GKVoiceChat? ``` |
| To | ``` func voiceChat(withName name: String) -> GKVoiceChat? ``` |

Modified [GKMatchDelegate](https://developer.apple.com/documentation/gamekit/gkmatchdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKMatchDelegate : NSObjectProtocol {     optional func match(_ match: GKMatch, didReceiveData data: NSData, fromRemotePlayer player: GKPlayer)     optional func match(_ match: GKMatch, didReceiveData data: NSData, forRecipient recipient: GKPlayer, fromRemotePlayer player: GKPlayer)     optional func match(_ match: GKMatch, didReceiveData data: NSData, fromPlayer playerID: String)     optional func match(_ match: GKMatch, player player: GKPlayer, didChangeConnectionState state: GKPlayerConnectionState)     optional func match(_ match: GKMatch, player playerID: String, didChangeState state: GKPlayerConnectionState)     optional func match(_ match: GKMatch, didFailWithError error: NSError?)     optional func match(_ match: GKMatch, shouldReinviteDisconnectedPlayer player: GKPlayer) -> Bool     optional func match(_ match: GKMatch, shouldReinvitePlayer playerID: String) -> Bool } ``` |
| To | ``` protocol GKMatchDelegate : NSObjectProtocol {     optional func match(_ match: GKMatch, didReceive data: Data, fromRemotePlayer player: GKPlayer)     optional func match(_ match: GKMatch, didReceive data: Data, forRecipient recipient: GKPlayer, fromRemotePlayer player: GKPlayer)     optional func match(_ match: GKMatch, didReceive data: Data, fromPlayer playerID: String)     optional func match(_ match: GKMatch, player player: GKPlayer, didChange state: GKPlayerConnectionState)     optional func match(_ match: GKMatch, player playerID: String, didChange state: GKPlayerConnectionState)     optional func match(_ match: GKMatch, didFailWithError error: Error?)     optional func match(_ match: GKMatch, shouldReinviteDisconnectedPlayer player: GKPlayer) -> Bool     optional func match(_ match: GKMatch, shouldReinvitePlayer playerID: String) -> Bool } ``` |

Modified [GKMatchDelegate.match(_: GKMatch, didFailWithError: Error?)](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502025-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch, didFailWithError error: NSError?) ``` |
| To | ``` optional func match(_ match: GKMatch, didFailWithError error: Error?) ``` |

Modified [GKMatchDelegate.match(_: GKMatch, didReceive: Data, forRecipient: GKPlayer, fromRemotePlayer: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502034-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch, didReceiveData data: NSData, forRecipient recipient: GKPlayer, fromRemotePlayer player: GKPlayer) ``` |
| To | ``` optional func match(_ match: GKMatch, didReceive data: Data, forRecipient recipient: GKPlayer, fromRemotePlayer player: GKPlayer) ``` |

Modified [GKMatchDelegate.match(_: GKMatch, didReceive: Data, fromRemotePlayer: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502069-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch, didReceiveData data: NSData, fromRemotePlayer player: GKPlayer) ``` |
| To | ``` optional func match(_ match: GKMatch, didReceive data: Data, fromRemotePlayer player: GKPlayer) ``` |

Modified [GKMatchDelegate.match(_: GKMatch, player: GKPlayer, didChange: GKPlayerConnectionState)](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502048-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch, player player: GKPlayer, didChangeConnectionState state: GKPlayerConnectionState) ``` |
| To | ``` optional func match(_ match: GKMatch, player player: GKPlayer, didChange state: GKPlayerConnectionState) ``` |

Modified [GKMatchmaker](https://developer.apple.com/documentation/gamekit/gkmatchmaker)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKMatchmaker : NSObject {     class func sharedMatchmaker() -> GKMatchmaker     func matchForInvite(_ invite: GKInvite, completionHandler completionHandler: ((GKMatch?, NSError?) -> Void)?)     func findMatchForRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: ((GKMatch?, NSError?) -> Void)?)     func findPlayersForHostedRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?)     func addPlayersToMatch(_ match: GKMatch, matchRequest matchRequest: GKMatchRequest, completionHandler completionHandler: ((NSError?) -> Void)?)     func cancel()     func cancelPendingInviteToPlayer(_ player: GKPlayer)     func finishMatchmakingForMatch(_ match: GKMatch)     func queryPlayerGroupActivity(_ playerGroup: Int, withCompletionHandler completionHandler: ((Int, NSError?) -> Void)?)     func queryActivityWithCompletionHandler(_ completionHandler: ((Int, NSError?) -> Void)?)     func startBrowsingForNearbyPlayersWithHandler(_ reachableHandler: ((GKPlayer, Bool) -> Void)?)     func stopBrowsingForNearbyPlayers() } extension GKMatchmaker {     var inviteHandler: ((GKInvite, [AnyObject]?) -> Void)?     func startBrowsingForNearbyPlayersWithReachableHandler(_ reachableHandler: ((String, Bool) -> Void)?)     func cancelInviteToPlayer(_ playerID: String)     func findPlayersForHostedMatchRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (([String]?, NSError?) -> Void)?) } ``` | -- |
| To | ``` class GKMatchmaker : NSObject {     class func shared() -> GKMatchmaker     func match(for invite: GKInvite, completionHandler completionHandler: (@escaping (GKMatch?, Error?) -> Swift.Void)? = nil)     func findMatch(for request: GKMatchRequest, withCompletionHandler completionHandler: (@escaping (GKMatch?, Error?) -> Swift.Void)? = nil)     func findPlayers(forHostedRequest request: GKMatchRequest, withCompletionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil)     func addPlayers(to match: GKMatch, matchRequest matchRequest: GKMatchRequest, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func cancel()     func cancelPendingInvite(to player: GKPlayer)     func finishMatchmaking(for match: GKMatch)     func queryPlayerGroupActivity(_ playerGroup: Int, withCompletionHandler completionHandler: (@escaping (Int, Error?) -> Swift.Void)? = nil)     func queryActivity(completionHandler completionHandler: (@escaping (Int, Error?) -> Swift.Void)? = nil)     func startBrowsingForNearbyPlayers(handler reachableHandler: (@escaping (GKPlayer, Bool) -> Swift.Void)? = nil)     func stopBrowsingForNearbyPlayers()     var inviteHandler: ((GKInvite, [Any]?) -> Swift.Void)?     func startBrowsingForNearbyPlayers(reachableHandler reachableHandler: (@escaping (String, Bool) -> Swift.Void)? = nil)     func cancelInvite(toPlayer playerID: String)     func findPlayers(forHostedMatchRequest request: GKMatchRequest, withCompletionHandler completionHandler: (@escaping ([String]?, Error?) -> Swift.Void)? = nil)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKMatchmaker : CVarArg { } extension GKMatchmaker : Equatable, Hashable {     var hashValue: Int { get } } extension GKMatchmaker {     var inviteHandler: ((GKInvite, [Any]?) -> Swift.Void)?     func startBrowsingForNearbyPlayers(reachableHandler reachableHandler: (@escaping (String, Bool) -> Swift.Void)? = nil)     func cancelInvite(toPlayer playerID: String)     func findPlayers(forHostedMatchRequest request: GKMatchRequest, withCompletionHandler completionHandler: (@escaping ([String]?, Error?) -> Swift.Void)? = nil) } ``` | CVarArg, Equatable, Hashable |

Modified [GKMatchmaker.addPlayers(to: GKMatch, matchRequest: GKMatchRequest, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520561-addplayerstomatch)

|  | Declaration |
| --- | --- |
| From | ``` func addPlayersToMatch(_ match: GKMatch, matchRequest matchRequest: GKMatchRequest, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func addPlayers(to match: GKMatch, matchRequest matchRequest: GKMatchRequest, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKMatchmaker.cancelPendingInvite(to: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520773-cancelpendinginvitetoplayer)

|  | Declaration |
| --- | --- |
| From | ``` func cancelPendingInviteToPlayer(_ player: GKPlayer) ``` |
| To | ``` func cancelPendingInvite(to player: GKPlayer) ``` |

Modified [GKMatchmaker.findMatch(for: GKMatchRequest, withCompletionHandler: ( (GKMatch?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520777-findmatch)

|  | Declaration |
| --- | --- |
| From | ``` func findMatchForRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: ((GKMatch?, NSError?) -> Void)?) ``` |
| To | ``` func findMatch(for request: GKMatchRequest, withCompletionHandler completionHandler: (@escaping (GKMatch?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKMatchmaker.findPlayers(forHostedRequest: GKMatchRequest, withCompletionHandler: ( ([GKPlayer]?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520973-findplayersforhostedrequest)

|  | Declaration |
| --- | --- |
| From | ``` func findPlayersForHostedRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?) ``` |
| To | ``` func findPlayers(forHostedRequest request: GKMatchRequest, withCompletionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKMatchmaker.finishMatchmaking(for: GKMatch)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520518-finishmatchmaking)

|  | Declaration |
| --- | --- |
| From | ``` func finishMatchmakingForMatch(_ match: GKMatch) ``` |
| To | ``` func finishMatchmaking(for match: GKMatch) ``` |

Modified [GKMatchmaker.match(for: GKInvite, completionHandler: ( (GKMatch?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520847-match)

|  | Declaration |
| --- | --- |
| From | ``` func matchForInvite(_ invite: GKInvite, completionHandler completionHandler: ((GKMatch?, NSError?) -> Void)?) ``` |
| To | ``` func match(for invite: GKInvite, completionHandler completionHandler: (@escaping (GKMatch?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKMatchmaker.queryActivity(completionHandler: ( (Int, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520930-queryactivitywithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func queryActivityWithCompletionHandler(_ completionHandler: ((Int, NSError?) -> Void)?) ``` |
| To | ``` func queryActivity(completionHandler completionHandler: (@escaping (Int, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKMatchmaker.queryPlayerGroupActivity(_: Int, withCompletionHandler: ( (Int, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521189-queryplayergroupactivity)

|  | Declaration |
| --- | --- |
| From | ``` func queryPlayerGroupActivity(_ playerGroup: Int, withCompletionHandler completionHandler: ((Int, NSError?) -> Void)?) ``` |
| To | ``` func queryPlayerGroupActivity(_ playerGroup: Int, withCompletionHandler completionHandler: (@escaping (Int, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKMatchmaker.shared() -> GKMatchmaker [class]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520781-shared)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedMatchmaker() -> GKMatchmaker ``` |
| To | ``` class func shared() -> GKMatchmaker ``` |

Modified [GKMatchmaker.startBrowsingForNearbyPlayers(handler: ( (GKPlayer, Bool) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521043-startbrowsingfornearbyplayers)

|  | Declaration |
| --- | --- |
| From | ``` func startBrowsingForNearbyPlayersWithHandler(_ reachableHandler: ((GKPlayer, Bool) -> Void)?) ``` |
| To | ``` func startBrowsingForNearbyPlayers(handler reachableHandler: (@escaping (GKPlayer, Bool) -> Swift.Void)? = nil) ``` |

Modified [GKMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class GKMatchmakerViewController : UINavigationController {     unowned(unsafe) var matchmakerDelegate: GKMatchmakerViewControllerDelegate?     var matchRequest: GKMatchRequest { get }     var hosted: Bool     init?(matchRequest request: GKMatchRequest)     init?(invite invite: GKInvite)     func addPlayersToMatch(_ match: GKMatch)     func setHostedPlayer(_ playerID: String, connected connected: Bool)     func setHostedPlayer(_ player: GKPlayer, didConnect connected: Bool)     func setHostedPlayerReady(_ playerID: String)     var defaultInvitationMessage: String? } ``` |
| To | ``` class GKMatchmakerViewController : UINavigationController {     unowned(unsafe) var matchmakerDelegate: GKMatchmakerViewControllerDelegate?     var matchRequest: GKMatchRequest { get }     var isHosted: Bool     init?(matchRequest request: GKMatchRequest)     init?(invite invite: GKInvite)     func addPlayers(to match: GKMatch)     func setHostedPlayer(_ playerID: String, connected connected: Bool)     func setHostedPlayer(_ player: GKPlayer, didConnect connected: Bool)     func setHostedPlayerReady(_ playerID: String)     var defaultInvitationMessage: String? } ``` |

Modified [GKMatchmakerViewController.addPlayers(to: GKMatch)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492425-addplayerstomatch)

|  | Declaration |
| --- | --- |
| From | ``` func addPlayersToMatch(_ match: GKMatch) ``` |
| To | ``` func addPlayers(to match: GKMatch) ``` |

Modified [GKMatchmakerViewController.isHosted](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492414-hosted)

|  | Declaration |
| --- | --- |
| From | ``` var hosted: Bool ``` |
| To | ``` var isHosted: Bool ``` |

Modified [GKMatchmakerViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKMatchmakerViewControllerDelegate : NSObjectProtocol {     func matchmakerViewControllerWasCancelled(_ viewController: GKMatchmakerViewController)     func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFailWithError error: NSError)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindMatch match: GKMatch)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindHostedPlayers players: [GKPlayer])     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindPlayers playerIDs: [String])     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, hostedPlayerDidAccept player: GKPlayer)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didReceiveAcceptFromHostedPlayer playerID: String) } ``` |
| To | ``` protocol GKMatchmakerViewControllerDelegate : NSObjectProtocol {     func matchmakerViewControllerWasCancelled(_ viewController: GKMatchmakerViewController)     func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFailWithError error: Error)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFind match: GKMatch)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindHostedPlayers players: [GKPlayer])     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindPlayers playerIDs: [String])     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, hostedPlayerDidAccept player: GKPlayer)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didReceiveAcceptFromHostedPlayer playerID: String) } ``` |

Modified [GKMatchmakerViewControllerDelegate.matchmakerViewController(_: GKMatchmakerViewController, didFailWithError: Error)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492419-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFailWithError error: NSError) ``` |
| To | ``` func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFailWithError error: Error) ``` |

Modified [GKMatchmakerViewControllerDelegate.matchmakerViewController(_: GKMatchmakerViewController, didFind: GKMatch)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492416-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindMatch match: GKMatch) ``` |
| To | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFind match: GKMatch) ``` |

Modified [GKMatchRequest](https://developer.apple.com/documentation/gamekit/gkmatchrequest)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKMatchRequest : NSObject {     var minPlayers: Int     var maxPlayers: Int     var playerGroup: Int     var playerAttributes: UInt32     var recipients: [GKPlayer]?     var playersToInvite: [String]?     var inviteMessage: String?     var defaultNumberOfPlayers: Int     var recipientResponseHandler: ((GKPlayer, GKInviteRecipientResponse) -> Void)?     var inviteeResponseHandler: ((String, GKInviteeResponse) -> Void)?     class func maxPlayersAllowedForMatchOfType(_ matchType: GKMatchType) -> Int } ``` | -- |
| To | ``` class GKMatchRequest : NSObject {     var minPlayers: Int     var maxPlayers: Int     var playerGroup: Int     var playerAttributes: UInt32     var recipients: [GKPlayer]?     var playersToInvite: [String]?     var inviteMessage: String?     var defaultNumberOfPlayers: Int     var recipientResponseHandler: ((GKPlayer, GKInviteRecipientResponse) -> Swift.Void)?     var inviteeResponseHandler: ((String, GKInviteeResponse) -> Swift.Void)?     class func maxPlayersAllowedForMatch(of matchType: GKMatchType) -> Int     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKMatchRequest : CVarArg { } extension GKMatchRequest : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GKMatchRequest.maxPlayersAllowedForMatch(of: GKMatchType) -> Int [class]](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521150-maxplayersallowedformatchoftype)

|  | Declaration |
| --- | --- |
| From | ``` class func maxPlayersAllowedForMatchOfType(_ matchType: GKMatchType) -> Int ``` |
| To | ``` class func maxPlayersAllowedForMatch(of matchType: GKMatchType) -> Int ``` |

Modified [GKMatchRequest.recipientResponseHandler](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521004-recipientresponsehandler)

|  | Declaration |
| --- | --- |
| From | ``` var recipientResponseHandler: ((GKPlayer, GKInviteRecipientResponse) -> Void)? ``` |
| To | ``` var recipientResponseHandler: ((GKPlayer, GKInviteRecipientResponse) -> Swift.Void)? ``` |

Modified [GKMatchSendDataMode [enum]](https://developer.apple.com/documentation/gamekit/gkmatchsenddatamode)

|  | Declaration |
| --- | --- |
| From | ``` enum GKMatchSendDataMode : Int {     case Reliable     case Unreliable } ``` |
| To | ``` enum GKMatchSendDataMode : Int {     case reliable     case unreliable } ``` |

Modified [GKMatchSendDataMode.reliable](https://developer.apple.com/documentation/gamekit/gkmatchsenddatamode/gkmatchsenddatareliable)

|  | Declaration |
| --- | --- |
| From | ``` case Reliable ``` |
| To | ``` case reliable ``` |

Modified [GKMatchSendDataMode.unreliable](https://developer.apple.com/documentation/gamekit/gkmatchsenddatamode/gkmatchsenddataunreliable)

|  | Declaration |
| --- | --- |
| From | ``` case Unreliable ``` |
| To | ``` case unreliable ``` |

Modified [GKMatchType [enum]](https://developer.apple.com/documentation/gamekit/gkmatchtype)

|  | Declaration |
| --- | --- |
| From | ``` enum GKMatchType : UInt {     case PeerToPeer     case Hosted     case TurnBased } ``` |
| To | ``` enum GKMatchType : UInt {     case peerToPeer     case hosted     case turnBased } ``` |

Modified [GKMatchType.hosted](https://developer.apple.com/documentation/gamekit/gkmatchtype/hosted)

|  | Declaration |
| --- | --- |
| From | ``` case Hosted ``` |
| To | ``` case hosted ``` |

Modified [GKMatchType.peerToPeer](https://developer.apple.com/documentation/gamekit/gkmatchtype/peertopeer)

|  | Declaration |
| --- | --- |
| From | ``` case PeerToPeer ``` |
| To | ``` case peerToPeer ``` |

Modified [GKMatchType.turnBased](https://developer.apple.com/documentation/gamekit/gkmatchtype/turnbased)

|  | Declaration |
| --- | --- |
| From | ``` case TurnBased ``` |
| To | ``` case turnBased ``` |

Modified [GKNotificationBanner](https://developer.apple.com/documentation/gamekit/gknotificationbanner)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKNotificationBanner : NSObject {     class func showBannerWithTitle(_ title: String?, message message: String?, completionHandler completionHandler: (() -> Void)?)     class func showBannerWithTitle(_ title: String?, message message: String?, duration duration: NSTimeInterval, completionHandler completionHandler: (() -> Void)?) } ``` | -- |
| To | ``` class GKNotificationBanner : NSObject {     class func show(withTitle title: String?, message message: String?, completionHandler completionHandler: (@escaping () -> Swift.Void)? = nil)     class func show(withTitle title: String?, message message: String?, duration duration: TimeInterval, completionHandler completionHandler: (@escaping () -> Swift.Void)? = nil)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKNotificationBanner : CVarArg { } extension GKNotificationBanner : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GKNotificationBanner.show(withTitle: String?, message: String?, completionHandler: ( () -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515370-showbannerwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` class func showBannerWithTitle(_ title: String?, message message: String?, completionHandler completionHandler: (() -> Void)?) ``` |
| To | ``` class func show(withTitle title: String?, message message: String?, completionHandler completionHandler: (@escaping () -> Swift.Void)? = nil) ``` |

Modified [GKNotificationBanner.show(withTitle: String?, message: String?, duration: TimeInterval, completionHandler: ( () -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515368-showbannerwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` class func showBannerWithTitle(_ title: String?, message message: String?, duration duration: NSTimeInterval, completionHandler completionHandler: (() -> Void)?) ``` |
| To | ``` class func show(withTitle title: String?, message message: String?, duration duration: TimeInterval, completionHandler completionHandler: (@escaping () -> Swift.Void)? = nil) ``` |

Modified [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer)

|  | Declaration | Superclasses |
| --- | --- | --- |
| From | ``` class GKPlayer : NSObject {     class func loadPlayersForIdentifiers(_ identifiers: [String], withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?)     var playerID: String? { get }     var displayName: String? { get }     var alias: String? { get }     class func anonymousGuestPlayerWithIdentifier(_ guestIdentifier: String) -> Self     var guestIdentifier: String? { get } } extension GKPlayer {     func loadPhotoForSize(_ size: GKPhotoSize, withCompletionHandler completionHandler: ((UIImage?, NSError?) -> Void)?) } extension GKPlayer {     var isFriend: Bool { get } } ``` | NSObject |
| To | ``` class GKPlayer : GKBasePlayer {     class func loadPlayers(forIdentifiers identifiers: [String], withCompletionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil)     var playerID: String? { get }     var displayName: String? { get }     var alias: String? { get }     class func anonymousGuestPlayer(withIdentifier guestIdentifier: String) -> Self     var guestIdentifier: String? { get }     var isFriend: Bool { get }     func loadPhoto(forSize size: GKPhotoSize, withCompletionHandler completionHandler: (@escaping (UIImage?, Error?) -> Swift.Void)? = nil) } extension GKPlayer {     func loadPhoto(forSize size: GKPhotoSize, withCompletionHandler completionHandler: (@escaping (UIImage?, Error?) -> Swift.Void)? = nil) } extension GKPlayer {     var isFriend: Bool { get } } ``` | GKBasePlayer |

Modified [GKPlayer.anonymousGuestPlayer(withIdentifier: String) -> Self [class]](https://developer.apple.com/documentation/gamekit/gkplayer/1520559-anonymousguestplayer)

|  | Declaration |
| --- | --- |
| From | ``` class func anonymousGuestPlayerWithIdentifier(_ guestIdentifier: String) -> Self ``` |
| To | ``` class func anonymousGuestPlayer(withIdentifier guestIdentifier: String) -> Self ``` |

Modified [GKPlayer.loadPhoto(forSize: GKPhotoSize, withCompletionHandler: ( (UIImage?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkplayer/1521176-loadphoto)

|  | Declaration |
| --- | --- |
| From | ``` func loadPhotoForSize(_ size: GKPhotoSize, withCompletionHandler completionHandler: ((UIImage?, NSError?) -> Void)?) ``` |
| To | ``` func loadPhoto(forSize size: GKPhotoSize, withCompletionHandler completionHandler: (@escaping (UIImage?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKPlayer.loadPlayers(forIdentifiers: [String], withCompletionHandler: ( ([GKPlayer]?, Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkplayer/1520723-loadplayers)

|  | Declaration |
| --- | --- |
| From | ``` class func loadPlayersForIdentifiers(_ identifiers: [String], withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?) ``` |
| To | ``` class func loadPlayers(forIdentifiers identifiers: [String], withCompletionHandler completionHandler: (@escaping ([GKPlayer]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKPlayerConnectionState [enum]](https://developer.apple.com/documentation/gamekit/gkplayerconnectionstate)

|  | Declaration |
| --- | --- |
| From | ``` enum GKPlayerConnectionState : Int {     case StateUnknown     case StateConnected     case StateDisconnected } ``` |
| To | ``` enum GKPlayerConnectionState : Int {     case stateUnknown     case stateConnected     case stateDisconnected } ``` |

Modified [GKPlayerConnectionState.stateConnected](https://developer.apple.com/documentation/gamekit/gkplayerconnectionstate/stateconnected)

|  | Declaration |
| --- | --- |
| From | ``` case StateConnected ``` |
| To | ``` case stateConnected ``` |

Modified [GKPlayerConnectionState.stateDisconnected](https://developer.apple.com/documentation/gamekit/gkplayerconnectionstate/gkplayerstatedisconnected)

|  | Declaration |
| --- | --- |
| From | ``` case StateDisconnected ``` |
| To | ``` case stateDisconnected ``` |

Modified [GKPlayerConnectionState.stateUnknown](https://developer.apple.com/documentation/gamekit/gkplayerconnectionstate/stateunknown)

|  | Declaration |
| --- | --- |
| From | ``` case StateUnknown ``` |
| To | ``` case stateUnknown ``` |

Modified [GKScore](https://developer.apple.com/documentation/gamekit/gkscore)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKScore : NSObject, NSCoding, NSSecureCoding {     init(leaderboardIdentifier identifier: String)     init(leaderboardIdentifier identifier: String, player player: GKPlayer)     var value: Int64     var formattedValue: String? { get }     var leaderboardIdentifier: String     var context: UInt64     var date: NSDate { get }     var player: GKPlayer { get }     var rank: Int { get }     var shouldSetDefaultLeaderboard: Bool     class func reportScores(_ scores: [GKScore], withCompletionHandler completionHandler: ((NSError?) -> Void)?) } extension GKScore {     func challengeComposeControllerWithMessage(_ message: String?, players players: [GKPlayer]?, completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController     func issueChallengeToPlayers(_ playerIDs: [String]?, message message: String?)     class func reportScores(_ scores: [GKScore], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: ((NSError?) -> Void)?) } extension GKScore {     func challengeComposeControllerWithPlayers(_ playerIDs: [String]?, message message: String?, completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController? } extension GKScore {     init(leaderboardIdentifier identifier: String, forPlayer playerID: String)     func reportScoreWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     init(category category: String?)     var playerID: String { get }     var category: String? } ``` | NSCoding, NSSecureCoding |
| To | ``` class GKScore : NSObject, NSCoding, NSSecureCoding {     init(leaderboardIdentifier identifier: String)     init(leaderboardIdentifier identifier: String, player player: GKPlayer)     var value: Int64     var formattedValue: String? { get }     var leaderboardIdentifier: String     var context: UInt64     var date: Date { get }     var player: GKPlayer? { get }     var rank: Int { get }     var shouldSetDefaultLeaderboard: Bool     class func report(_ scores: [GKScore], withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func challengeComposeController(withPlayers playerIDs: [String]?, message message: String?, completionHandler completionHandler: GameKit.GKChallengeComposeCompletionBlock? = nil) -> UIViewController?     func challengeComposeController(withMessage message: String?, players players: [GKPlayer]?, completionHandler completionHandler: GameKit.GKChallengeComposeCompletionBlock? = nil) -> UIViewController     func issueChallenge(toPlayers playerIDs: [String]?, message message: String?)     class func report(_ scores: [GKScore], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     init(leaderboardIdentifier identifier: String, forPlayer playerID: String)     func report(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     init(category category: String?)     var playerID: String { get }     var category: String?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKScore {     func challengeComposeController(withMessage message: String?, players players: [GKPlayer]?, completionHandler completionHandler: GameKit.GKChallengeComposeCompletionBlock? = nil) -> UIViewController     func issueChallenge(toPlayers playerIDs: [String]?, message message: String?)     class func report(_ scores: [GKScore], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) } extension GKScore {     func challengeComposeController(withPlayers playerIDs: [String]?, message message: String?, completionHandler completionHandler: GameKit.GKChallengeComposeCompletionBlock? = nil) -> UIViewController? } extension GKScore : CVarArg { } extension GKScore : Equatable, Hashable {     var hashValue: Int { get } } extension GKScore {     init(leaderboardIdentifier identifier: String, forPlayer playerID: String)     func report(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     init(category category: String?)     var playerID: String { get }     var category: String? } ``` | CVarArg, Equatable, Hashable, NSCoding, NSSecureCoding |

Modified [GKScore.challengeComposeController(withMessage: String?, players: [GKPlayer]?, completionHandler: GameKit.GKChallengeComposeCompletionBlock?) -> UIViewController](https://developer.apple.com/documentation/gamekit/gkscore/1521227-challengecomposecontroller)

|  | Declaration |
| --- | --- |
| From | ``` func challengeComposeControllerWithMessage(_ message: String?, players players: [GKPlayer]?, completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController ``` |
| To | ``` func challengeComposeController(withMessage message: String?, players players: [GKPlayer]?, completionHandler completionHandler: GameKit.GKChallengeComposeCompletionBlock? = nil) -> UIViewController ``` |

Modified [GKScore.date](https://developer.apple.com/documentation/gamekit/gkscore/1399234-date)

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate { get } ``` |
| To | ``` var date: Date { get } ``` |

Modified [GKScore.player](https://developer.apple.com/documentation/gamekit/gkscore/1399246-player)

|  | Declaration |
| --- | --- |
| From | ``` var player: GKPlayer { get } ``` |
| To | ``` var player: GKPlayer? { get } ``` |

Modified [GKScore.report(_: [GKScore], withCompletionHandler: ( (Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkscore/1399252-reportscores)

|  | Declaration |
| --- | --- |
| From | ``` class func reportScores(_ scores: [GKScore], withCompletionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` class func report(_ scores: [GKScore], withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKScore.report(_: [GKScore], withEligibleChallenges: [GKChallenge], withCompletionHandler: ( (Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkscore/1520627-report)

|  | Declaration |
| --- | --- |
| From | ``` class func reportScores(_ scores: [GKScore], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` class func report(_ scores: [GKScore], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKSessionDelegate](https://developer.apple.com/documentation/gamekit/gksessiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKSessionDelegate : NSObjectProtocol {     optional func session(_ session: GKSession, peer peerID: String, didChangeState state: GKPeerConnectionState)     optional func session(_ session: GKSession, didReceiveConnectionRequestFromPeer peerID: String)     optional func session(_ session: GKSession, connectionWithPeerFailed peerID: String, withError error: NSError)     optional func session(_ session: GKSession, didFailWithError error: NSError) } ``` |
| To | ``` protocol GKSessionDelegate : NSObjectProtocol {     optional func session(_ session: GKSession, peer peerID: String, didChange state: GKPeerConnectionState)     optional func session(_ session: GKSession, didReceiveConnectionRequestFromPeer peerID: String)     optional func session(_ session: GKSession, connectionWithPeerFailed peerID: String, withError error: Error)     optional func session(_ session: GKSession, didFailWithError error: Error) } ``` |

Modified [GKSessionDelegate.session(_: GKSession, connectionWithPeerFailed: String, withError: Error)](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1521160-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: GKSession, connectionWithPeerFailed peerID: String, withError error: NSError) ``` |
| To | ``` optional func session(_ session: GKSession, connectionWithPeerFailed peerID: String, withError error: Error) ``` |

Modified [GKSessionDelegate.session(_: GKSession, didFailWithError: Error)](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520662-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: GKSession, didFailWithError error: NSError) ``` |
| To | ``` optional func session(_ session: GKSession, didFailWithError error: Error) ``` |

Modified [GKSessionDelegate.session(_: GKSession, peer: String, didChange: GKPeerConnectionState)](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520885-session)

|  | Declaration |
| --- | --- |
| From | ``` optional func session(_ session: GKSession, peer peerID: String, didChangeState state: GKPeerConnectionState) ``` |
| To | ``` optional func session(_ session: GKSession, peer peerID: String, didChange state: GKPeerConnectionState) ``` |

Modified [GKTurnBasedEventListener](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKTurnBasedEventListener {     optional func player(_ player: GKPlayer, didRequestMatchWithOtherPlayers playersToInvite: [GKPlayer])     optional func player(_ player: GKPlayer, receivedTurnEventForMatch match: GKTurnBasedMatch, didBecomeActive didBecomeActive: Bool)     optional func player(_ player: GKPlayer, matchEnded match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, receivedExchangeRequest exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, receivedExchangeCancellation exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, receivedExchangeReplies replies: [GKTurnBasedExchangeReply], forCompletedExchange exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, wantsToQuitMatch match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String]) } ``` |
| To | ``` protocol GKTurnBasedEventListener {     optional func player(_ player: GKPlayer, didRequestMatchWithOtherPlayers playersToInvite: [GKPlayer])     optional func player(_ player: GKPlayer, receivedTurnEventFor match: GKTurnBasedMatch, didBecomeActive didBecomeActive: Bool)     optional func player(_ player: GKPlayer, matchEnded match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, receivedExchangeRequest exchange: GKTurnBasedExchange, for match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, receivedExchangeCancellation exchange: GKTurnBasedExchange, for match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, receivedExchangeReplies replies: [GKTurnBasedExchangeReply], forCompletedExchange exchange: GKTurnBasedExchange, for match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, wantsToQuitMatch match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String]) } ``` |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, receivedExchangeCancellation: GKTurnBasedExchange, for: GKTurnBasedMatch)](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520649-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer, receivedExchangeCancellation exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch) ``` |
| To | ``` optional func player(_ player: GKPlayer, receivedExchangeCancellation exchange: GKTurnBasedExchange, for match: GKTurnBasedMatch) ``` |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, receivedExchangeReplies: [GKTurnBasedExchangeReply], forCompletedExchange: GKTurnBasedExchange, for: GKTurnBasedMatch)](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520827-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer, receivedExchangeReplies replies: [GKTurnBasedExchangeReply], forCompletedExchange exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch) ``` |
| To | ``` optional func player(_ player: GKPlayer, receivedExchangeReplies replies: [GKTurnBasedExchangeReply], forCompletedExchange exchange: GKTurnBasedExchange, for match: GKTurnBasedMatch) ``` |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, receivedExchangeRequest: GKTurnBasedExchange, for: GKTurnBasedMatch)](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521209-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer, receivedExchangeRequest exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch) ``` |
| To | ``` optional func player(_ player: GKPlayer, receivedExchangeRequest exchange: GKTurnBasedExchange, for match: GKTurnBasedMatch) ``` |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, receivedTurnEventFor: GKTurnBasedMatch, didBecomeActive: Bool)](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521017-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer, receivedTurnEventForMatch match: GKTurnBasedMatch, didBecomeActive didBecomeActive: Bool) ``` |
| To | ``` optional func player(_ player: GKPlayer, receivedTurnEventFor match: GKTurnBasedMatch, didBecomeActive didBecomeActive: Bool) ``` |

Modified [GKTurnBasedExchange](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKTurnBasedExchange : NSObject {     var exchangeID: String? { get }     var sender: GKTurnBasedParticipant? { get }     var recipients: [GKTurnBasedParticipant]? { get }     var status: GKTurnBasedExchangeStatus { get }     var message: String? { get }     var data: NSData? { get }     var sendDate: NSDate? { get }     var timeoutDate: NSDate? { get }     var completionDate: NSDate? { get }     var replies: [GKTurnBasedExchangeReply]? { get }     func cancelWithLocalizableMessageKey(_ key: String, arguments arguments: [String], completionHandler completionHandler: ((NSError?) -> Void)?)     func replyWithLocalizableMessageKey(_ key: String, arguments arguments: [String], data data: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) } ``` | -- |
| To | ``` class GKTurnBasedExchange : NSObject {     var exchangeID: String? { get }     var sender: GKTurnBasedParticipant? { get }     var recipients: [GKTurnBasedParticipant]? { get }     var status: GKTurnBasedExchangeStatus { get }     var message: String? { get }     var data: Data? { get }     var sendDate: Date? { get }     var timeoutDate: Date? { get }     var completionDate: Date? { get }     var replies: [GKTurnBasedExchangeReply]? { get }     func cancel(withLocalizableMessageKey key: String, arguments arguments: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func reply(withLocalizableMessageKey key: String, arguments arguments: [String], data data: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKTurnBasedExchange : CVarArg { } extension GKTurnBasedExchange : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GKTurnBasedExchange.cancel(withLocalizableMessageKey: String, arguments: [String], completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520779-cancel)

|  | Declaration |
| --- | --- |
| From | ``` func cancelWithLocalizableMessageKey(_ key: String, arguments arguments: [String], completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func cancel(withLocalizableMessageKey key: String, arguments arguments: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedExchange.completionDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520994-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` var completionDate: NSDate? { get } ``` |
| To | ``` var completionDate: Date? { get } ``` |

Modified [GKTurnBasedExchange.data](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521121-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData? { get } ``` |
| To | ``` var data: Data? { get } ``` |

Modified [GKTurnBasedExchange.reply(withLocalizableMessageKey: String, arguments: [String], data: Data, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520478-reply)

|  | Declaration |
| --- | --- |
| From | ``` func replyWithLocalizableMessageKey(_ key: String, arguments arguments: [String], data data: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func reply(withLocalizableMessageKey key: String, arguments arguments: [String], data data: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedExchange.sendDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521131-senddate)

|  | Declaration |
| --- | --- |
| From | ``` var sendDate: NSDate? { get } ``` |
| To | ``` var sendDate: Date? { get } ``` |

Modified [GKTurnBasedExchange.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521105-timeoutdate)

|  | Declaration |
| --- | --- |
| From | ``` var timeoutDate: NSDate? { get } ``` |
| To | ``` var timeoutDate: Date? { get } ``` |

Modified [GKTurnBasedExchangeReply](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKTurnBasedExchangeReply : NSObject {     var recipient: GKTurnBasedParticipant? { get }     var message: String? { get }     var data: NSData? { get }     var replyDate: NSDate? { get } } ``` | -- |
| To | ``` class GKTurnBasedExchangeReply : NSObject {     var recipient: GKTurnBasedParticipant? { get }     var message: String? { get }     var data: Data? { get }     var replyDate: Date? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKTurnBasedExchangeReply : CVarArg { } extension GKTurnBasedExchangeReply : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GKTurnBasedExchangeReply.data](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520729-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData? { get } ``` |
| To | ``` var data: Data? { get } ``` |

Modified [GKTurnBasedExchangeReply.replyDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520727-replydate)

|  | Declaration |
| --- | --- |
| From | ``` var replyDate: NSDate? { get } ``` |
| To | ``` var replyDate: Date? { get } ``` |

Modified [GKTurnBasedExchangeStatus [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus)

|  | Declaration |
| --- | --- |
| From | ``` enum GKTurnBasedExchangeStatus : Int8 {     case Unknown     case Active     case Complete     case Resolved     case Canceled } ``` |
| To | ``` enum GKTurnBasedExchangeStatus : Int8 {     case unknown     case active     case complete     case resolved     case canceled } ``` |

Modified [GKTurnBasedExchangeStatus.active](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/active)

|  | Declaration |
| --- | --- |
| From | ``` case Active ``` |
| To | ``` case active ``` |

Modified [GKTurnBasedExchangeStatus.canceled](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/gkturnbasedexchangestatuscanceled)

|  | Declaration |
| --- | --- |
| From | ``` case Canceled ``` |
| To | ``` case canceled ``` |

Modified [GKTurnBasedExchangeStatus.complete](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/complete)

|  | Declaration |
| --- | --- |
| From | ``` case Complete ``` |
| To | ``` case complete ``` |

Modified [GKTurnBasedExchangeStatus.resolved](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/resolved)

|  | Declaration |
| --- | --- |
| From | ``` case Resolved ``` |
| To | ``` case resolved ``` |

Modified [GKTurnBasedExchangeStatus.unknown](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [GKTurnBasedMatch](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKTurnBasedMatch : NSObject {     var matchID: String? { get }     var creationDate: NSDate? { get }     var participants: [GKTurnBasedParticipant]? { get }     var status: GKTurnBasedMatchStatus { get }     var currentParticipant: GKTurnBasedParticipant? { get }     var matchData: NSData? { get }     func setLocalizableMessageWithKey(_ key: String, arguments arguments: [String]?)     var message: String?     var matchDataMaximumSize: Int { get }     var exchanges: [GKTurnBasedExchange]? { get }     var activeExchanges: [GKTurnBasedExchange]? { get }     var completedExchanges: [GKTurnBasedExchange]? { get }     var exchangeDataMaximumSize: Int { get }     var exchangeMaxInitiatedExchangesPerPlayer: Int { get }     class func findMatchForRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (GKTurnBasedMatch?, NSError?) -> Void)     class func loadMatchesWithCompletionHandler(_ completionHandler: (([GKTurnBasedMatch]?, NSError?) -> Void)?)     class func loadMatchWithID(_ matchID: String, withCompletionHandler completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?)     func rematchWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?)     func acceptInviteWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?)     func declineInviteWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     func removeWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     func loadMatchDataWithCompletionHandler(_ completionHandler: ((NSData?, NSError?) -> Void)?)     func endTurnWithNextParticipants(_ nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: NSTimeInterval, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func participantQuitInTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, nextParticipants nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: NSTimeInterval, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func participantQuitOutOfTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, withCompletionHandler completionHandler: ((NSError?) -> Void)?)     func endMatchInTurnWithMatchData(_ matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func endMatchInTurnWithMatchData(_ matchData: NSData, scores scores: [GKScore]?, achievements achievements: [GKAchievement]?, completionHandler completionHandler: ((NSError?) -> Void)?)     func saveCurrentTurnWithMatchData(_ matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func saveMergedMatchData(_ matchData: NSData, withResolvedExchanges exchanges: [GKTurnBasedExchange], completionHandler completionHandler: ((NSError?) -> Void)?)     func sendExchangeToParticipants(_ participants: [GKTurnBasedParticipant], data data: NSData, localizableMessageKey key: String, arguments arguments: [String], timeout timeout: NSTimeInterval, completionHandler completionHandler: ((GKTurnBasedExchange, NSError) -> Void)?)     func sendReminderToParticipants(_ participants: [GKTurnBasedParticipant], localizableMessageKey key: String, arguments arguments: [String], completionHandler completionHandler: ((NSError?) -> Void)?)     func endTurnWithNextParticipant(_ nextParticipant: GKTurnBasedParticipant, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func participantQuitInTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, nextParticipant nextParticipant: GKTurnBasedParticipant, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) } ``` | -- |
| To | ``` class GKTurnBasedMatch : NSObject {     var matchID: String? { get }     var creationDate: Date? { get }     var participants: [GKTurnBasedParticipant]? { get }     var status: GKTurnBasedMatchStatus { get }     var currentParticipant: GKTurnBasedParticipant? { get }     var matchData: Data? { get }     func setLocalizableMessageWithKey(_ key: String, arguments arguments: [String]?)     var message: String?     var matchDataMaximumSize: Int { get }     var exchanges: [GKTurnBasedExchange]? { get }     var activeExchanges: [GKTurnBasedExchange]? { get }     var completedExchanges: [GKTurnBasedExchange]? { get }     var exchangeDataMaximumSize: Int { get }     var exchangeMaxInitiatedExchangesPerPlayer: Int { get }     class func find(for request: GKMatchRequest, withCompletionHandler completionHandler: @escaping (GKTurnBasedMatch?, Error?) -> Swift.Void)     class func loadMatches(completionHandler completionHandler: (@escaping ([GKTurnBasedMatch]?, Error?) -> Swift.Void)? = nil)     class func load(withID matchID: String, withCompletionHandler completionHandler: (@escaping (GKTurnBasedMatch?, Error?) -> Swift.Void)? = nil)     func rematch(completionHandler completionHandler: (@escaping (GKTurnBasedMatch?, Error?) -> Swift.Void)? = nil)     func acceptInvite(completionHandler completionHandler: (@escaping (GKTurnBasedMatch?, Error?) -> Swift.Void)? = nil)     func declineInvite(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func remove(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func loadMatchData(completionHandler completionHandler: (@escaping (Data?, Error?) -> Swift.Void)? = nil)     func endTurn(withNextParticipants nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: TimeInterval, match matchData: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func participantQuitInTurn(with matchOutcome: GKTurnBasedMatchOutcome, nextParticipants nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: TimeInterval, match matchData: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func participantQuitOutOfTurn(with matchOutcome: GKTurnBasedMatchOutcome, withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func endMatchInTurn(withMatch matchData: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func endMatchInTurn(withMatch matchData: Data, scores scores: [GKScore]?, achievements achievements: [GKAchievement]?, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func saveCurrentTurn(withMatch matchData: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func saveMergedMatch(_ matchData: Data, withResolvedExchanges exchanges: [GKTurnBasedExchange], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func sendExchange(to participants: [GKTurnBasedParticipant], data data: Data, localizableMessageKey key: String, arguments arguments: [String], timeout timeout: TimeInterval, completionHandler completionHandler: (@escaping (GKTurnBasedExchange, Error) -> Swift.Void)? = nil)     func sendReminder(to participants: [GKTurnBasedParticipant], localizableMessageKey key: String, arguments arguments: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func endTurn(withNextParticipant nextParticipant: GKTurnBasedParticipant, match matchData: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func participantQuitInTurn(with matchOutcome: GKTurnBasedMatchOutcome, nextParticipant nextParticipant: GKTurnBasedParticipant, match matchData: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKTurnBasedMatch : CVarArg { } extension GKTurnBasedMatch : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GKTurnBasedMatch.acceptInvite(completionHandler: ( (GKTurnBasedMatch?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520515-acceptinvitewithcompletionhandle)

|  | Declaration |
| --- | --- |
| From | ``` func acceptInviteWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?) ``` |
| To | ``` func acceptInvite(completionHandler completionHandler: (@escaping (GKTurnBasedMatch?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.creationDate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521168-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate? { get } ``` |
| To | ``` var creationDate: Date? { get } ``` |

Modified [GKTurnBasedMatch.declineInvite(completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520940-declineinvitewithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func declineInviteWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func declineInvite(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.endMatchInTurn(withMatch: Data, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520907-endmatchinturnwithmatchdata)

|  | Declaration |
| --- | --- |
| From | ``` func endMatchInTurnWithMatchData(_ matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func endMatchInTurn(withMatch matchData: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.endMatchInTurn(withMatch: Data, scores: [GKScore]?, achievements: [GKAchievement]?, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521006-endmatchinturn)

|  | Declaration |
| --- | --- |
| From | ``` func endMatchInTurnWithMatchData(_ matchData: NSData, scores scores: [GKScore]?, achievements achievements: [GKAchievement]?, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func endMatchInTurn(withMatch matchData: Data, scores scores: [GKScore]?, achievements achievements: [GKAchievement]?, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.endTurn(withNextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520765-endturnwithnextparticipants)

|  | Declaration |
| --- | --- |
| From | ``` func endTurnWithNextParticipants(_ nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: NSTimeInterval, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func endTurn(withNextParticipants nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: TimeInterval, match matchData: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.find(for: GKMatchRequest, withCompletionHandler: (GKTurnBasedMatch?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521008-findmatchforrequest)

|  | Declaration |
| --- | --- |
| From | ``` class func findMatchForRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (GKTurnBasedMatch?, NSError?) -> Void) ``` |
| To | ``` class func find(for request: GKMatchRequest, withCompletionHandler completionHandler: @escaping (GKTurnBasedMatch?, Error?) -> Swift.Void) ``` |

Modified [GKTurnBasedMatch.load(withID: String, withCompletionHandler: ( (GKTurnBasedMatch?, Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521102-load)

|  | Declaration |
| --- | --- |
| From | ``` class func loadMatchWithID(_ matchID: String, withCompletionHandler completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?) ``` |
| To | ``` class func load(withID matchID: String, withCompletionHandler completionHandler: (@escaping (GKTurnBasedMatch?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.loadMatchData(completionHandler: ( (Data?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521005-loadmatchdatawithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func loadMatchDataWithCompletionHandler(_ completionHandler: ((NSData?, NSError?) -> Void)?) ``` |
| To | ``` func loadMatchData(completionHandler completionHandler: (@escaping (Data?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.loadMatches(completionHandler: ( ([GKTurnBasedMatch]?, Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521207-loadmatcheswithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` class func loadMatchesWithCompletionHandler(_ completionHandler: (([GKTurnBasedMatch]?, NSError?) -> Void)?) ``` |
| To | ``` class func loadMatches(completionHandler completionHandler: (@escaping ([GKTurnBasedMatch]?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.matchData](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520991-matchdata)

|  | Declaration |
| --- | --- |
| From | ``` var matchData: NSData? { get } ``` |
| To | ``` var matchData: Data? { get } ``` |

Modified [GKTurnBasedMatch.participantQuitInTurn(with: GKTurnBasedMatchOutcome, nextParticipants: [GKTurnBasedParticipant], turnTimeout: TimeInterval, match: Data, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520500-participantquitinturn)

|  | Declaration |
| --- | --- |
| From | ``` func participantQuitInTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, nextParticipants nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: NSTimeInterval, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func participantQuitInTurn(with matchOutcome: GKTurnBasedMatchOutcome, nextParticipants nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: TimeInterval, match matchData: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.participantQuitOutOfTurn(with: GKTurnBasedMatchOutcome, withCompletionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521106-participantquitoutofturn)

|  | Declaration |
| --- | --- |
| From | ``` func participantQuitOutOfTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, withCompletionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func participantQuitOutOfTurn(with matchOutcome: GKTurnBasedMatchOutcome, withCompletionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.rematch(completionHandler: ( (GKTurnBasedMatch?, Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520794-rematchwithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func rematchWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?) ``` |
| To | ``` func rematch(completionHandler completionHandler: (@escaping (GKTurnBasedMatch?, Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.remove(completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520651-removewithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func removeWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func remove(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.saveCurrentTurn(withMatch: Data, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520761-savecurrentturnwithmatchdata)

|  | Declaration |
| --- | --- |
| From | ``` func saveCurrentTurnWithMatchData(_ matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func saveCurrentTurn(withMatch matchData: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.saveMergedMatch(_: Data, withResolvedExchanges: [GKTurnBasedExchange], completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521154-savemergedmatch)

|  | Declaration |
| --- | --- |
| From | ``` func saveMergedMatchData(_ matchData: NSData, withResolvedExchanges exchanges: [GKTurnBasedExchange], completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func saveMergedMatch(_ matchData: Data, withResolvedExchanges exchanges: [GKTurnBasedExchange], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.sendExchange(to: [GKTurnBasedParticipant], data: Data, localizableMessageKey: String, arguments: [String], timeout: TimeInterval, completionHandler: ( (GKTurnBasedExchange, Error) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520451-sendexchangetoparticipants)

|  | Declaration |
| --- | --- |
| From | ``` func sendExchangeToParticipants(_ participants: [GKTurnBasedParticipant], data data: NSData, localizableMessageKey key: String, arguments arguments: [String], timeout timeout: NSTimeInterval, completionHandler completionHandler: ((GKTurnBasedExchange, NSError) -> Void)?) ``` |
| To | ``` func sendExchange(to participants: [GKTurnBasedParticipant], data data: Data, localizableMessageKey key: String, arguments arguments: [String], timeout timeout: TimeInterval, completionHandler completionHandler: (@escaping (GKTurnBasedExchange, Error) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatch.sendReminder(to: [GKTurnBasedParticipant], localizableMessageKey: String, arguments: [String], completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520947-sendremindertoparticipants)

|  | Declaration |
| --- | --- |
| From | ``` func sendReminderToParticipants(_ participants: [GKTurnBasedParticipant], localizableMessageKey key: String, arguments arguments: [String], completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func sendReminder(to participants: [GKTurnBasedParticipant], localizableMessageKey key: String, arguments arguments: [String], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [GKTurnBasedMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class GKTurnBasedMatchmakerViewController : UINavigationController { } extension GKTurnBasedMatchmakerViewController {     unowned(unsafe) var turnBasedMatchmakerDelegate: GKTurnBasedMatchmakerViewControllerDelegate?     var showExistingMatches: Bool     init(matchRequest request: GKMatchRequest) } ``` |
| To | ``` class GKTurnBasedMatchmakerViewController : UINavigationController {     unowned(unsafe) var turnBasedMatchmakerDelegate: GKTurnBasedMatchmakerViewControllerDelegate?     var showExistingMatches: Bool     init(matchRequest request: GKMatchRequest) } extension GKTurnBasedMatchmakerViewController {     unowned(unsafe) var turnBasedMatchmakerDelegate: GKTurnBasedMatchmakerViewControllerDelegate?     var showExistingMatches: Bool     init(matchRequest request: GKMatchRequest) } ``` |

Modified [GKTurnBasedMatchmakerViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKTurnBasedMatchmakerViewControllerDelegate : NSObjectProtocol {     func turnBasedMatchmakerViewControllerWasCancelled(_ viewController: GKTurnBasedMatchmakerViewController)     func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFailWithError error: NSError)     optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFindMatch match: GKTurnBasedMatch)     optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, playerQuitForMatch match: GKTurnBasedMatch) } ``` |
| To | ``` protocol GKTurnBasedMatchmakerViewControllerDelegate : NSObjectProtocol {     func turnBasedMatchmakerViewControllerWasCancelled(_ viewController: GKTurnBasedMatchmakerViewController)     func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFailWithError error: Error)     optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFind match: GKTurnBasedMatch)     optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, playerQuitFor match: GKTurnBasedMatch) } ``` |

Modified [GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewController(_: GKTurnBasedMatchmakerViewController, didFailWithError: Error)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1521028-turnbasedmatchmakerviewcontrolle)

|  | Declaration |
| --- | --- |
| From | ``` func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFailWithError error: NSError) ``` |
| To | ``` func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFailWithError error: Error) ``` |

Modified [GKTurnBasedMatchOutcome [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome)

|  | Declaration |
| --- | --- |
| From | ``` enum GKTurnBasedMatchOutcome : Int {     case None     case Quit     case Won     case Lost     case Tied     case TimeExpired     case First     case Second     case Third     case Fourth     case CustomRange } ``` |
| To | ``` enum GKTurnBasedMatchOutcome : Int {     case none     case quit     case won     case lost     case tied     case timeExpired     case first     case second     case third     case fourth     case customRange } ``` |

Modified [GKTurnBasedMatchOutcome.customRange](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/customrange)

|  | Declaration |
| --- | --- |
| From | ``` case CustomRange ``` |
| To | ``` case customRange ``` |

Modified [GKTurnBasedMatchOutcome.first](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/first)

|  | Declaration |
| --- | --- |
| From | ``` case First ``` |
| To | ``` case first ``` |

Modified [GKTurnBasedMatchOutcome.fourth](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/gkturnbasedmatchoutcomefourth)

|  | Declaration |
| --- | --- |
| From | ``` case Fourth ``` |
| To | ``` case fourth ``` |

Modified [GKTurnBasedMatchOutcome.lost](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/lost)

|  | Declaration |
| --- | --- |
| From | ``` case Lost ``` |
| To | ``` case lost ``` |

Modified [GKTurnBasedMatchOutcome.none](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/gkturnbasedmatchoutcomenone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [GKTurnBasedMatchOutcome.quit](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/gkturnbasedmatchoutcomequit)

|  | Declaration |
| --- | --- |
| From | ``` case Quit ``` |
| To | ``` case quit ``` |

Modified [GKTurnBasedMatchOutcome.second](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/second)

|  | Declaration |
| --- | --- |
| From | ``` case Second ``` |
| To | ``` case second ``` |

Modified [GKTurnBasedMatchOutcome.third](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/third)

|  | Declaration |
| --- | --- |
| From | ``` case Third ``` |
| To | ``` case third ``` |

Modified [GKTurnBasedMatchOutcome.tied](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/tied)

|  | Declaration |
| --- | --- |
| From | ``` case Tied ``` |
| To | ``` case tied ``` |

Modified [GKTurnBasedMatchOutcome.timeExpired](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/timeexpired)

|  | Declaration |
| --- | --- |
| From | ``` case TimeExpired ``` |
| To | ``` case timeExpired ``` |

Modified [GKTurnBasedMatchOutcome.won](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome/won)

|  | Declaration |
| --- | --- |
| From | ``` case Won ``` |
| To | ``` case won ``` |

Modified [GKTurnBasedMatchStatus [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum GKTurnBasedMatchStatus : Int {     case Unknown     case Open     case Ended     case Matching } ``` |
| To | ``` enum GKTurnBasedMatchStatus : Int {     case unknown     case open     case ended     case matching } ``` |

Modified [GKTurnBasedMatchStatus.ended](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus/ended)

|  | Declaration |
| --- | --- |
| From | ``` case Ended ``` |
| To | ``` case ended ``` |

Modified [GKTurnBasedMatchStatus.matching](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus/matching)

|  | Declaration |
| --- | --- |
| From | ``` case Matching ``` |
| To | ``` case matching ``` |

Modified [GKTurnBasedMatchStatus.open](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus/open)

|  | Declaration |
| --- | --- |
| From | ``` case Open ``` |
| To | ``` case open ``` |

Modified [GKTurnBasedMatchStatus.unknown](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus/gkturnbasedmatchstatusunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [GKTurnBasedParticipant](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKTurnBasedParticipant : NSObject {     var player: GKPlayer? { get }     @NSCopying var lastTurnDate: NSDate? { get }     var status: GKTurnBasedParticipantStatus { get }     var matchOutcome: GKTurnBasedMatchOutcome     @NSCopying var timeoutDate: NSDate? { get }     var playerID: String? { get } } ``` | -- |
| To | ``` class GKTurnBasedParticipant : NSObject {     var player: GKPlayer? { get }     var lastTurnDate: Date? { get }     var status: GKTurnBasedParticipantStatus { get }     var matchOutcome: GKTurnBasedMatchOutcome     var timeoutDate: Date? { get }     var playerID: String? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKTurnBasedParticipant : CVarArg { } extension GKTurnBasedParticipant : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [GKTurnBasedParticipant.lastTurnDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520941-lastturndate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var lastTurnDate: NSDate? { get } ``` |
| To | ``` var lastTurnDate: Date? { get } ``` |

Modified [GKTurnBasedParticipant.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521187-timeoutdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timeoutDate: NSDate? { get } ``` |
| To | ``` var timeoutDate: Date? { get } ``` |

Modified [GKTurnBasedParticipantStatus [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum GKTurnBasedParticipantStatus : Int {     case Unknown     case Invited     case Declined     case Matching     case Active     case Done } ``` |
| To | ``` enum GKTurnBasedParticipantStatus : Int {     case unknown     case invited     case declined     case matching     case active     case done } ``` |

Modified [GKTurnBasedParticipantStatus.active](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/active)

|  | Declaration |
| --- | --- |
| From | ``` case Active ``` |
| To | ``` case active ``` |

Modified [GKTurnBasedParticipantStatus.declined](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/gkturnbasedparticipantstatusdeclined)

|  | Declaration |
| --- | --- |
| From | ``` case Declined ``` |
| To | ``` case declined ``` |

Modified [GKTurnBasedParticipantStatus.done](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/done)

|  | Declaration |
| --- | --- |
| From | ``` case Done ``` |
| To | ``` case done ``` |

Modified [GKTurnBasedParticipantStatus.invited](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/gkturnbasedparticipantstatusinvited)

|  | Declaration |
| --- | --- |
| From | ``` case Invited ``` |
| To | ``` case invited ``` |

Modified [GKTurnBasedParticipantStatus.matching](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/matching)

|  | Declaration |
| --- | --- |
| From | ``` case Matching ``` |
| To | ``` case matching ``` |

Modified [GKTurnBasedParticipantStatus.unknown](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [GKVoiceChat](https://developer.apple.com/documentation/gamekit/gkvoicechat)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKVoiceChat : NSObject {     func start()     func stop()     func setPlayer(_ player: GKPlayer, muted isMuted: Bool)     var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChatPlayerState) -> Void     var name: String { get }     var active: Bool     var volume: Float     var players: [GKPlayer] { get }     class func isVoIPAllowed() -> Bool } extension GKVoiceChat {     var playerIDs: [String] { get }     var playerStateUpdateHandler: (String, GKVoiceChatPlayerState) -> Void     func setMute(_ isMuted: Bool, forPlayer playerID: String) } ``` | -- |
| To | ``` class GKVoiceChat : NSObject {     func start()     func stop()     func setPlayer(_ player: GKPlayer, muted isMuted: Bool)     var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChatPlayerState) -> Swift.Void     var name: String { get }     var isActive: Bool     var volume: Float     var players: [GKPlayer] { get }     class func isVoIPAllowed() -> Bool     var playerIDs: [String] { get }     var playerStateUpdateHandler: (String, GKVoiceChatPlayerState) -> Swift.Void     func setMute(_ isMuted: Bool, forPlayer playerID: String)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension GKVoiceChat : CVarArg { } extension GKVoiceChat : Equatable, Hashable {     var hashValue: Int { get } } extension GKVoiceChat {     var playerIDs: [String] { get }     var playerStateUpdateHandler: (String, GKVoiceChatPlayerState) -> Swift.Void     func setMute(_ isMuted: Bool, forPlayer playerID: String) } ``` | CVarArg, Equatable, Hashable |

Modified [GKVoiceChat.isActive](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385697-active)

|  | Declaration |
| --- | --- |
| From | ``` var active: Bool ``` |
| To | ``` var isActive: Bool ``` |

Modified [GKVoiceChat.playerVoiceChatStateDidChangeHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385713-playervoicechatstatedidchangehan)

|  | Declaration |
| --- | --- |
| From | ``` var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChatPlayerState) -> Void ``` |
| To | ``` var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChatPlayerState) -> Swift.Void ``` |

Modified [GKVoiceChatClient](https://developer.apple.com/documentation/gamekit/gkvoicechatclient)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKVoiceChatClient : NSObjectProtocol {     func voiceChatService(_ voiceChatService: GKVoiceChatService, sendData data: NSData, toParticipantID participantID: String)     func participantID() -> String     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, sendRealTimeData data: NSData, toParticipantID participantID: String)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStartWithParticipantID participantID: String)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didNotStartWithParticipantID participantID: String, error error: NSError?)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStopWithParticipantID participantID: String, error error: NSError?)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didReceiveInvitationFromParticipantID participantID: String, callID callID: Int) } ``` |
| To | ``` protocol GKVoiceChatClient : NSObjectProtocol {     func voiceChatService(_ voiceChatService: GKVoiceChatService, send data: Data, toParticipantID participantID: String)     func participantID() -> String     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, sendRealTime data: Data, toParticipantID participantID: String)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStartWithParticipantID participantID: String)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didNotStartWithParticipantID participantID: String, error error: Error?)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStopWithParticipantID participantID: String, error error: Error?)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didReceiveInvitationFromParticipantID participantID: String, callID callID: Int) } ``` |

Modified [GKVoiceChatClient.voiceChatService(_: GKVoiceChatService, didNotStartWithParticipantID: String, error: Error?)](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521047-voicechatservice)

|  | Declaration |
| --- | --- |
| From | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didNotStartWithParticipantID participantID: String, error error: NSError?) ``` |
| To | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didNotStartWithParticipantID participantID: String, error error: Error?) ``` |

Modified [GKVoiceChatClient.voiceChatService(_: GKVoiceChatService, didStopWithParticipantID: String, error: Error?)](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520681-voicechatservice)

|  | Declaration |
| --- | --- |
| From | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStopWithParticipantID participantID: String, error error: NSError?) ``` |
| To | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStopWithParticipantID participantID: String, error error: Error?) ``` |

Modified [GKVoiceChatClient.voiceChatService(_: GKVoiceChatService, send: Data, toParticipantID: String)](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521075-voicechatservice)

|  | Declaration |
| --- | --- |
| From | ``` func voiceChatService(_ voiceChatService: GKVoiceChatService, sendData data: NSData, toParticipantID participantID: String) ``` |
| To | ``` func voiceChatService(_ voiceChatService: GKVoiceChatService, send data: Data, toParticipantID participantID: String) ``` |

Modified [GKVoiceChatClient.voiceChatService(_: GKVoiceChatService, sendRealTime: Data, toParticipantID: String)](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521009-voicechatservice)

|  | Declaration |
| --- | --- |
| From | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, sendRealTimeData data: NSData, toParticipantID participantID: String) ``` |
| To | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, sendRealTime data: Data, toParticipantID participantID: String) ``` |

Modified [GKVoiceChatPlayerState [enum]](https://developer.apple.com/documentation/gamekit/gkvoicechatplayerstate)

|  | Declaration |
| --- | --- |
| From | ``` enum GKVoiceChatPlayerState : Int {     case Connected     case Disconnected     case Speaking     case Silent     case Connecting } ``` |
| To | ``` enum GKVoiceChatPlayerState : Int {     case connected     case disconnected     case speaking     case silent     case connecting } ``` |

Modified [GKVoiceChatPlayerState.connected](https://developer.apple.com/documentation/gamekit/gkvoicechatplayerstate/connected)

|  | Declaration |
| --- | --- |
| From | ``` case Connected ``` |
| To | ``` case connected ``` |

Modified [GKVoiceChatPlayerState.connecting](https://developer.apple.com/documentation/gamekit/gkvoicechatplayerstate/connecting)

|  | Declaration |
| --- | --- |
| From | ``` case Connecting ``` |
| To | ``` case connecting ``` |

Modified [GKVoiceChatPlayerState.disconnected](https://developer.apple.com/documentation/gamekit/gkvoicechatplayerstate/disconnected)

|  | Declaration |
| --- | --- |
| From | ``` case Disconnected ``` |
| To | ``` case disconnected ``` |

Modified [GKVoiceChatPlayerState.silent](https://developer.apple.com/documentation/gamekit/gkvoicechatplayerstate/silent)

|  | Declaration |
| --- | --- |
| From | ``` case Silent ``` |
| To | ``` case silent ``` |

Modified [GKVoiceChatPlayerState.speaking](https://developer.apple.com/documentation/gamekit/gkvoicechatplayerstate/speaking)

|  | Declaration |
| --- | --- |
| From | ``` case Speaking ``` |
| To | ``` case speaking ``` |

Modified [GKChallengeComposeCompletionBlock](https://developer.apple.com/documentation/gamekit/gkchallengecomposecompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias GKChallengeComposeCompletionBlock = (UIViewController, Bool, [String]?) -> Void ``` |
| To | ``` typealias GKChallengeComposeCompletionBlock = (UIViewController, Bool, [String]?) -> Swift.Void ``` |

Modified [GKExchangeTimeoutDefault](https://developer.apple.com/documentation/gamekit/gkexchangetimeoutdefault)

|  | Declaration |
| --- | --- |
| From | ``` var GKExchangeTimeoutDefault: NSTimeInterval ``` |
| To | ``` var GKExchangeTimeoutDefault: TimeInterval ``` |

Modified [GKExchangeTimeoutNone](https://developer.apple.com/documentation/gamekit/gkexchangetimeoutnone)

|  | Declaration |
| --- | --- |
| From | ``` var GKExchangeTimeoutNone: NSTimeInterval ``` |
| To | ``` var GKExchangeTimeoutNone: TimeInterval ``` |

Modified [GKTurnTimeoutDefault](https://developer.apple.com/documentation/gamekit/gkturntimeoutdefault)

|  | Declaration |
| --- | --- |
| From | ``` var GKTurnTimeoutDefault: NSTimeInterval ``` |
| To | ``` var GKTurnTimeoutDefault: TimeInterval ``` |

Modified [GKTurnTimeoutNone](https://developer.apple.com/documentation/gamekit/gkturntimeoutnone)

|  | Declaration |
| --- | --- |
| From | ``` var GKTurnTimeoutNone: NSTimeInterval ``` |
| To | ``` var GKTurnTimeoutNone: TimeInterval ``` |

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
