---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Swift/MediaPlayer.html
archived_at: '2026-07-18T02:55:31.678811Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# MediaPlayer Changes for Swift

### MediaPlayer

Removed [MPMediaPlaylistAttribute.None](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistattribute/mpmediaplaylistattributenone)Removed [MPMovieLoadState.Unknown](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/mpmovieloadstateunknown)Removed [MPMovieMediaTypeMask.None](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask/mpmoviemediatypemasknone)Added [MPChangeLanguageOptionCommandEvent.setting](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent/1649697-setting)Added [MPChangeLanguageOptionSetting [enum]](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting)Added [MPChangeLanguageOptionSetting.none](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting/none)Added [MPChangeLanguageOptionSetting.nowPlayingItemOnly](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting/nowplayingitemonly)Added [MPChangeLanguageOptionSetting.permanent](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting/permanent)Added [MPChangeRepeatModeCommand](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommand)Added [MPChangeRepeatModeCommand.currentRepeatType](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommand/1648342-currentrepeattype)Added [MPChangeRepeatModeCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent)Added [MPChangeRepeatModeCommandEvent.preservesRepeatMode](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent/2097553-preservesrepeatmode)Added [MPChangeRepeatModeCommandEvent.repeatType](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent/1649689-repeattype)Added [MPChangeShuffleModeCommand](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommand)Added [MPChangeShuffleModeCommand.currentShuffleType](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommand/1648341-currentshuffletype)Added [MPChangeShuffleModeCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommandevent)Added [MPChangeShuffleModeCommandEvent.preservesShuffleMode](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommandevent/2097552-preservesshufflemode)Added [MPChangeShuffleModeCommandEvent.shuffleType](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommandevent/1649696-shuffletype)Added [MPContentItem.isExplicitContent](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1771744-explicitcontent)Added [MPContentItem.isStreamingContent](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1771745-isstreamingcontent)Added [MPError [struct]](https://developer.apple.com/documentation/mediaplayer/mperror)Added [MPError.cloudServiceCapabilityMissing](https://developer.apple.com/documentation/mediaplayer/mperror/2335085-cloudservicecapabilitymissing)Added MPError.init(_nsError: NSError)Added [MPError.networkConnectionFailed](https://developer.apple.com/documentation/mediaplayer/mperror/2335086-networkconnectionfailed)Added [MPError.notFound](https://developer.apple.com/documentation/mediaplayer/mperror/2335090-notfound)Added [MPError.notSupported](https://developer.apple.com/documentation/mediaplayer/mperror/2335087-notsupported)Added [MPError.permissionDenied](https://developer.apple.com/documentation/mediaplayer/mperror/2335088-permissiondenied)Added [MPError.unknown](https://developer.apple.com/documentation/mediaplayer/mperror/2335089-unknown)Added [MPMediaItem.dateAdded](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/2213358-dateadded)Added [MPMediaItem.isExplicitItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1649691-explicititem)Added [MPMediaItemArtwork.init(boundsSize: CGSize, requestHandler: (CGSize) -> UIImage)](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1649704-init)Added [MPNowPlayingInfoMediaType [enum]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype)Added [MPNowPlayingInfoMediaType.audio](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype/mpnowplayinginfomediatypeaudio)Added [MPNowPlayingInfoMediaType.none](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype/none)Added [MPNowPlayingInfoMediaType.video](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype/mpnowplayinginfomediatypevideo)Added [MPPlayableContentDataSource.contentItem(forIdentifier: String, completionHandler: (MPContentItem?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1649672-contentitem)Added [MPPlayableContentDelegate.playableContentManager(_: MPPlayableContentManager, initializePlaybackQueueWithContentItems: [Any]?, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1648205-playablecontentmanager)Added [MPPlayableContentManager.nowPlayingIdentifiers](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1649434-nowplayingidentifiers)Added [MPRemoteCommandCenter.changeRepeatModeCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1649694-changerepeatmodecommand)Added [MPRemoteCommandCenter.changeShuffleModeCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1649692-changeshufflemodecommand)Added [MPRepeatType [enum]](https://developer.apple.com/documentation/mediaplayer/mprepeattype)Added [MPRepeatType.all](https://developer.apple.com/documentation/mediaplayer/mprepeattype/all)Added [MPRepeatType.off](https://developer.apple.com/documentation/mediaplayer/mprepeattype/off)Added [MPRepeatType.one](https://developer.apple.com/documentation/mediaplayer/mprepeattype/mprepeattypeone)Added [MPShuffleType [enum]](https://developer.apple.com/documentation/mediaplayer/mpshuffletype)Added [MPShuffleType.collections](https://developer.apple.com/documentation/mediaplayer/mpshuffletype/mpshuffletypecollections)Added [MPShuffleType.items](https://developer.apple.com/documentation/mediaplayer/mpshuffletype/mpshuffletypeitems)Added [MPShuffleType.off](https://developer.apple.com/documentation/mediaplayer/mpshuffletype/off)Added [MPMediaItemPropertyDateAdded](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertydateadded)Added [MPMediaItemPropertyIsExplicit](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyisexplicit)Added [MPNowPlayingInfoCollectionIdentifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocollectionidentifier)Added [MPNowPlayingInfoPropertyExternalContentIdentifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyexternalcontentidentifier)Added [MPNowPlayingInfoPropertyExternalUserProfileIdentifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyexternaluserprofileidentifier)Added [MPNowPlayingInfoPropertyIsLiveStream](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyislivestream)Added [MPNowPlayingInfoPropertyMediaType](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertymediatype)Added [MPNowPlayingInfoPropertyPlaybackProgress](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyplaybackprogress)Modified [MPChangeLanguageOptionCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent)

|  | Declaration |
| --- | --- |
| From | ``` class MPChangeLanguageOptionCommandEvent : MPRemoteCommandEvent {     var languageOption: MPNowPlayingInfoLanguageOption { get } } ``` |
| To | ``` class MPChangeLanguageOptionCommandEvent : MPRemoteCommandEvent {     var languageOption: MPNowPlayingInfoLanguageOption { get }     var setting: MPChangeLanguageOptionSetting { get } } ``` |

Modified [MPChangePlaybackPositionCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackpositioncommandevent)

|  | Declaration |
| --- | --- |
| From | ``` class MPChangePlaybackPositionCommandEvent : MPRemoteCommandEvent {     var positionTime: NSTimeInterval { get } } ``` |
| To | ``` class MPChangePlaybackPositionCommandEvent : MPRemoteCommandEvent {     var positionTime: TimeInterval { get } } ``` |

Modified [MPChangePlaybackPositionCommandEvent.positionTime](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackpositioncommandevent/1616766-positiontime)

|  | Declaration |
| --- | --- |
| From | ``` var positionTime: NSTimeInterval { get } ``` |
| To | ``` var positionTime: TimeInterval { get } ``` |

Modified [MPContentItem](https://developer.apple.com/documentation/mediaplayer/mpcontentitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPContentItem : NSObject {     init(identifier identifier: String)     var identifier: String { get }     var title: String?     var subtitle: String?     var artwork: MPMediaItemArtwork?     var container: Bool     var playable: Bool     var playbackProgress: Float } ``` | -- |
| To | ``` class MPContentItem : NSObject {     init(identifier identifier: String)     var identifier: String { get }     var title: String?     var subtitle: String?     var artwork: MPMediaItemArtwork?     var playbackProgress: Float     var isStreamingContent: Bool     var isExplicitContent: Bool     var isContainer: Bool     var isPlayable: Bool     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPContentItem : CVarArg { } extension MPContentItem : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPContentItem.isContainer](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620154-container)

|  | Declaration |
| --- | --- |
| From | ``` var container: Bool ``` |
| To | ``` var isContainer: Bool ``` |

Modified [MPContentItem.isPlayable](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620158-playable)

|  | Declaration |
| --- | --- |
| From | ``` var playable: Bool ``` |
| To | ``` var isPlayable: Bool ``` |

Modified [MPError.Code [enum]](https://developer.apple.com/documentation/mediaplayer/mperrorcode)

|  | Declaration |
| --- | --- |
| From | ``` enum MPErrorCode : Int {     case Unknown     case PermissionDenied     case CloudServiceCapabilityMissing     case NetworkConnectionFailed     case NotFound     case NotSupported } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = MPError         case unknown         case permissionDenied         case cloudServiceCapabilityMissing         case networkConnectionFailed         case notFound         case notSupported     } ``` |

Modified [MPError.Code.cloudServiceCapabilityMissing](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrorcloudservicecapabilitymissing)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case CloudServiceCapabilityMissing ``` | iOS 9.3 |
| To | ``` case cloudServiceCapabilityMissing ``` | iOS 10.0 |

Modified [MPError.Code.networkConnectionFailed](https://developer.apple.com/documentation/mediaplayer/mperror/code/networkconnectionfailed)

|  | Declaration |
| --- | --- |
| From | ``` case NetworkConnectionFailed ``` |
| To | ``` case networkConnectionFailed ``` |

Modified [MPError.Code.notFound](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornotfound)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case NotFound ``` | iOS 9.3 |
| To | ``` case notFound ``` | iOS 10.0 |

Modified [MPError.Code.notSupported](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornotsupported)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case NotSupported ``` | iOS 9.3 |
| To | ``` case notSupported ``` | iOS 10.0 |

Modified [MPError.Code.permissionDenied](https://developer.apple.com/documentation/mediaplayer/mperror/code/permissiondenied)

|  | Declaration |
| --- | --- |
| From | ``` case PermissionDenied ``` |
| To | ``` case permissionDenied ``` |

Modified [MPError.Code.unknown](https://developer.apple.com/documentation/mediaplayer/mperror/code/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [MPFeedbackCommand](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommand)

|  | Declaration |
| --- | --- |
| From | ``` class MPFeedbackCommand : MPRemoteCommand {     var active: Bool     var localizedTitle: String     var localizedShortTitle: String } ``` |
| To | ``` class MPFeedbackCommand : MPRemoteCommand {     var isActive: Bool     var localizedTitle: String     var localizedShortTitle: String } ``` |

Modified [MPFeedbackCommand.isActive](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommand/1622900-isactive)

|  | Declaration |
| --- | --- |
| From | ``` var active: Bool ``` |
| To | ``` var isActive: Bool ``` |

Modified [MPFeedbackCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommandevent)

|  | Declaration |
| --- | --- |
| From | ``` class MPFeedbackCommandEvent : MPRemoteCommandEvent {     var negative: Bool { get } } ``` |
| To | ``` class MPFeedbackCommandEvent : MPRemoteCommandEvent {     var isNegative: Bool { get } } ``` |

Modified [MPFeedbackCommandEvent.isNegative](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommandevent/1616773-isnegative)

|  | Declaration |
| --- | --- |
| From | ``` var negative: Bool { get } ``` |
| To | ``` var isNegative: Bool { get } ``` |

Modified [MPMediaEntity](https://developer.apple.com/documentation/mediaplayer/mpmediaentity)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaEntity : NSObject, NSSecureCoding {     class func canFilterByProperty(_ property: String) -> Bool     func enumerateValuesForProperties(_ properties: Set<String>, usingBlock block: (String, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     subscript (_ key: AnyObject) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: AnyObject) -> AnyObject?     func valueForProperty(_ property: String) -> AnyObject?     var persistentID: MPMediaEntityPersistentID { get } } ``` | NSSecureCoding |
| To | ``` class MPMediaEntity : NSObject, NSSecureCoding {     class func canFilter(byProperty property: String) -> Bool     func enumerateValues(forProperties properties: Set<String>, using block: @escaping (String, Any, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)     subscript(_ key: Any) -> Any? { get }     func objectForKeyedSubscript(_ key: Any) -> Any?     func value(forProperty property: String) -> Any?     var persistentID: MPMediaEntityPersistentID { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMediaEntity : CVarArg { } extension MPMediaEntity : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [MPMediaEntity.canFilter(byProperty: String) -> Bool [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620123-canfilter)

|  | Declaration |
| --- | --- |
| From | ``` class func canFilterByProperty(_ property: String) -> Bool ``` |
| To | ``` class func canFilter(byProperty property: String) -> Bool ``` |

Modified [MPMediaEntity.enumerateValues(forProperties: Set<String>, using: (String, Any, UnsafeMutablePointer<ObjCBool>) -> Swift.Void)](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620122-enumeratevaluesforproperties)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateValuesForProperties(_ properties: Set<String>, usingBlock block: (String, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |
| To | ``` func enumerateValues(forProperties properties: Set<String>, using block: @escaping (String, Any, UnsafeMutablePointer<ObjCBool>) -> Swift.Void) ``` |

Modified [MPMediaEntity.subscript(_: Any) -> Any?](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620124-objectforkeyedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (_ key: AnyObject) -> AnyObject? { get } ``` |
| To | ``` subscript(_ key: Any) -> Any? { get } ``` |

Modified [MPMediaEntity.value(forProperty: String) -> Any?](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620128-value)

|  | Declaration |
| --- | --- |
| From | ``` func valueForProperty(_ property: String) -> AnyObject? ``` |
| To | ``` func value(forProperty property: String) -> Any? ``` |

Modified [MPMediaGrouping [enum]](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMediaGrouping : Int {     case Title     case Album     case Artist     case AlbumArtist     case Composer     case Genre     case Playlist     case PodcastTitle } ``` |
| To | ``` enum MPMediaGrouping : Int {     case title     case album     case artist     case albumArtist     case composer     case genre     case playlist     case podcastTitle } ``` |

Modified [MPMediaGrouping.album](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping/mpmediagroupingalbum)

|  | Declaration |
| --- | --- |
| From | ``` case Album ``` |
| To | ``` case album ``` |

Modified [MPMediaGrouping.albumArtist](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping/albumartist)

|  | Declaration |
| --- | --- |
| From | ``` case AlbumArtist ``` |
| To | ``` case albumArtist ``` |

Modified [MPMediaGrouping.artist](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping/mpmediagroupingartist)

|  | Declaration |
| --- | --- |
| From | ``` case Artist ``` |
| To | ``` case artist ``` |

Modified [MPMediaGrouping.composer](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping/mpmediagroupingcomposer)

|  | Declaration |
| --- | --- |
| From | ``` case Composer ``` |
| To | ``` case composer ``` |

Modified [MPMediaGrouping.genre](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping/mpmediagroupinggenre)

|  | Declaration |
| --- | --- |
| From | ``` case Genre ``` |
| To | ``` case genre ``` |

Modified [MPMediaGrouping.playlist](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping/playlist)

|  | Declaration |
| --- | --- |
| From | ``` case Playlist ``` |
| To | ``` case playlist ``` |

Modified [MPMediaGrouping.podcastTitle](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping/mpmediagroupingpodcasttitle)

|  | Declaration |
| --- | --- |
| From | ``` case PodcastTitle ``` |
| To | ``` case podcastTitle ``` |

Modified [MPMediaGrouping.title](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping/title)

|  | Declaration |
| --- | --- |
| From | ``` case Title ``` |
| To | ``` case title ``` |

Modified [MPMediaItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitem)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaItem : MPMediaEntity {     var persistentID: MPMediaEntityPersistentID { get }     var mediaType: MPMediaType { get }     var title: String? { get }     var albumTitle: String? { get }     var albumPersistentID: MPMediaEntityPersistentID { get }     var artist: String? { get }     var artistPersistentID: MPMediaEntityPersistentID { get }     var albumArtist: String? { get }     var albumArtistPersistentID: MPMediaEntityPersistentID { get }     var genre: String? { get }     var genrePersistentID: MPMediaEntityPersistentID { get }     var composer: String? { get }     var composerPersistentID: MPMediaEntityPersistentID { get }     var playbackDuration: NSTimeInterval { get }     var albumTrackNumber: Int { get }     var albumTrackCount: Int { get }     var discNumber: Int { get }     var discCount: Int { get }     var artwork: MPMediaItemArtwork? { get }     var lyrics: String? { get }     var compilation: Bool { get }     var releaseDate: NSDate? { get }     var beatsPerMinute: Int { get }     var comments: String? { get }     var assetURL: NSURL? { get }     var cloudItem: Bool { get }     var protectedAsset: Bool { get }     var podcastTitle: String? { get }     var podcastPersistentID: MPMediaEntityPersistentID { get }     var playCount: Int { get }     var skipCount: Int { get }     var rating: Int { get }     var lastPlayedDate: NSDate? { get }     var userGrouping: String? { get }     var bookmarkTime: NSTimeInterval { get } } extension MPMediaItem {     class func persistentIDPropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String     class func titlePropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String } ``` |
| To | ``` class MPMediaItem : MPMediaEntity {     var persistentID: MPMediaEntityPersistentID { get }     var mediaType: MPMediaType { get }     var title: String? { get }     var albumTitle: String? { get }     var albumPersistentID: MPMediaEntityPersistentID { get }     var artist: String? { get }     var artistPersistentID: MPMediaEntityPersistentID { get }     var albumArtist: String? { get }     var albumArtistPersistentID: MPMediaEntityPersistentID { get }     var genre: String? { get }     var genrePersistentID: MPMediaEntityPersistentID { get }     var composer: String? { get }     var composerPersistentID: MPMediaEntityPersistentID { get }     var playbackDuration: TimeInterval { get }     var albumTrackNumber: Int { get }     var albumTrackCount: Int { get }     var discNumber: Int { get }     var discCount: Int { get }     var artwork: MPMediaItemArtwork? { get }     var isExplicitItem: Bool { get }     var lyrics: String? { get }     var isCompilation: Bool { get }     var releaseDate: Date? { get }     var beatsPerMinute: Int { get }     var comments: String? { get }     var assetURL: URL? { get }     var isCloudItem: Bool { get }     var hasProtectedAsset: Bool { get }     var podcastTitle: String? { get }     var podcastPersistentID: MPMediaEntityPersistentID { get }     var playCount: Int { get }     var skipCount: Int { get }     var rating: Int { get }     var lastPlayedDate: Date? { get }     var userGrouping: String? { get }     var bookmarkTime: TimeInterval { get }     var dateAdded: Date { get }     class func persistentIDProperty(forGroupingType groupingType: MPMediaGrouping) -> String     class func titleProperty(forGroupingType groupingType: MPMediaGrouping) -> String } extension MPMediaItem {     class func persistentIDProperty(forGroupingType groupingType: MPMediaGrouping) -> String     class func titleProperty(forGroupingType groupingType: MPMediaGrouping) -> String } ``` |

Modified [MPMediaItem.assetURL](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621707-asseturl)

|  | Declaration |
| --- | --- |
| From | ``` var assetURL: NSURL? { get } ``` |
| To | ``` var assetURL: URL? { get } ``` |

Modified [MPMediaItem.bookmarkTime](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621727-bookmarktime)

|  | Declaration |
| --- | --- |
| From | ``` var bookmarkTime: NSTimeInterval { get } ``` |
| To | ``` var bookmarkTime: TimeInterval { get } ``` |

Modified [MPMediaItem.hasProtectedAsset](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621678-protectedasset)

|  | Declaration |
| --- | --- |
| From | ``` var protectedAsset: Bool { get } ``` |
| To | ``` var hasProtectedAsset: Bool { get } ``` |

Modified [MPMediaItem.isCloudItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621697-isclouditem)

|  | Declaration |
| --- | --- |
| From | ``` var cloudItem: Bool { get } ``` |
| To | ``` var isCloudItem: Bool { get } ``` |

Modified [MPMediaItem.isCompilation](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621745-iscompilation)

|  | Declaration |
| --- | --- |
| From | ``` var compilation: Bool { get } ``` |
| To | ``` var isCompilation: Bool { get } ``` |

Modified [MPMediaItem.lastPlayedDate](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621719-lastplayeddate)

|  | Declaration |
| --- | --- |
| From | ``` var lastPlayedDate: NSDate? { get } ``` |
| To | ``` var lastPlayedDate: Date? { get } ``` |

Modified [MPMediaItem.persistentIDProperty(forGroupingType: MPMediaGrouping) -> String [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621805-persistentidpropertyforgroupingt)

|  | Declaration |
| --- | --- |
| From | ``` class func persistentIDPropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String ``` |
| To | ``` class func persistentIDProperty(forGroupingType groupingType: MPMediaGrouping) -> String ``` |

Modified [MPMediaItem.playbackDuration](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621732-playbackduration)

|  | Declaration |
| --- | --- |
| From | ``` var playbackDuration: NSTimeInterval { get } ``` |
| To | ``` var playbackDuration: TimeInterval { get } ``` |

Modified [MPMediaItem.releaseDate](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621682-releasedate)

|  | Declaration |
| --- | --- |
| From | ``` var releaseDate: NSDate? { get } ``` |
| To | ``` var releaseDate: Date? { get } ``` |

Modified [MPMediaItem.titleProperty(forGroupingType: MPMediaGrouping) -> String [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621775-titlepropertyforgroupingtype)

|  | Declaration |
| --- | --- |
| From | ``` class func titlePropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String ``` |
| To | ``` class func titleProperty(forGroupingType groupingType: MPMediaGrouping) -> String ``` |

Modified [MPMediaItemArtwork](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaItemArtwork : NSObject {     init(image image: UIImage)     func imageWithSize(_ size: CGSize) -> UIImage?     var bounds: CGRect { get }     var imageCropRect: CGRect { get } } ``` | -- |
| To | ``` class MPMediaItemArtwork : NSObject {     init(boundsSize boundsSize: CGSize, requestHandler requestHandler: @escaping (CGSize) -> UIImage)     func image(at size: CGSize) -> UIImage?     var bounds: CGRect { get }     var imageCropRect: CGRect { get }     convenience init(image image: UIImage)     convenience init()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMediaItemArtwork : CVarArg { } extension MPMediaItemArtwork : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPMediaItemArtwork.image(at: CGSize) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621736-image)

|  | Declaration |
| --- | --- |
| From | ``` func imageWithSize(_ size: CGSize) -> UIImage? ``` |
| To | ``` func image(at size: CGSize) -> UIImage? ``` |

Modified [MPMediaItemArtwork.imageCropRect](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621760-imagecroprect)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 10.0 |

Modified [MPMediaItemArtwork.init(image: UIImage)](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621747-initwithimage)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` init(image image: UIImage) ``` | -- |
| To | ``` convenience init(image image: UIImage) ``` | iOS 10.0 |

Modified [MPMediaItemCollection](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaItemCollection : MPMediaEntity {      init(items items: [MPMediaItem])     class func collectionWithItems(_ items: [MPMediaItem]) -> MPMediaItemCollection     init(items items: [MPMediaItem])     var items: [MPMediaItem] { get }     var representativeItem: MPMediaItem? { get }     var count: Int { get }     var mediaTypes: MPMediaType { get } } ``` |
| To | ``` class MPMediaItemCollection : MPMediaEntity {      init(items items: [MPMediaItem])     class func withItems(_ items: [MPMediaItem]) -> MPMediaItemCollection     init(items items: [MPMediaItem])     var items: [MPMediaItem] { get }     var representativeItem: MPMediaItem? { get }     var count: Int { get }     var mediaTypes: MPMediaType { get } } ``` |

Modified [MPMediaLibrary](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaLibrary : NSObject, NSSecureCoding {     class func defaultMediaLibrary() -> MPMediaLibrary     var lastModifiedDate: NSDate { get }     func beginGeneratingLibraryChangeNotifications()     func endGeneratingLibraryChangeNotifications()     class func authorizationStatus() -> MPMediaLibraryAuthorizationStatus     class func requestAuthorization(_ handler: (MPMediaLibraryAuthorizationStatus) -> Void)     func addItemWithProductID(_ productID: String, completionHandler completionHandler: (([MPMediaEntity], NSError?) -> Void)?)     func getPlaylistWithUUID(_ uuid: NSUUID, creationMetadata creationMetadata: MPMediaPlaylistCreationMetadata?, completionHandler completionHandler: (MPMediaPlaylist?, NSError?) -> Void) } ``` | NSSecureCoding |
| To | ``` class MPMediaLibrary : NSObject, NSSecureCoding {     class func `default`() -> MPMediaLibrary     var lastModifiedDate: Date { get }     func beginGeneratingLibraryChangeNotifications()     func endGeneratingLibraryChangeNotifications()     class func authorizationStatus() -> MPMediaLibraryAuthorizationStatus     class func requestAuthorization(_ handler: @escaping (MPMediaLibraryAuthorizationStatus) -> Swift.Void)     func addItem(withProductID productID: String, completionHandler completionHandler: (@escaping ([MPMediaEntity], Error?) -> Swift.Void)? = nil)     func getPlaylist(with uuid: UUID, creationMetadata creationMetadata: MPMediaPlaylistCreationMetadata?, completionHandler completionHandler: @escaping (MPMediaPlaylist?, Error?) -> Swift.Void)     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMediaLibrary : CVarArg { } extension MPMediaLibrary : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [MPMediaLibrary.addItem(withProductID: String, completionHandler: ( ([MPMediaEntity], Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621278-additem)

|  | Declaration |
| --- | --- |
| From | ``` func addItemWithProductID(_ productID: String, completionHandler completionHandler: (([MPMediaEntity], NSError?) -> Void)?) ``` |
| To | ``` func addItem(withProductID productID: String, completionHandler completionHandler: (@escaping ([MPMediaEntity], Error?) -> Swift.Void)? = nil) ``` |

Modified [MPMediaLibrary.default() [class]](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621269-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultMediaLibrary() -> MPMediaLibrary ``` |
| To | ``` class func `default`() -> MPMediaLibrary ``` |

Modified [MPMediaLibrary.getPlaylist(with: UUID, creationMetadata: MPMediaPlaylistCreationMetadata?, completionHandler: (MPMediaPlaylist?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621273-getplaylistwithuuid)

|  | Declaration |
| --- | --- |
| From | ``` func getPlaylistWithUUID(_ uuid: NSUUID, creationMetadata creationMetadata: MPMediaPlaylistCreationMetadata?, completionHandler completionHandler: (MPMediaPlaylist?, NSError?) -> Void) ``` |
| To | ``` func getPlaylist(with uuid: UUID, creationMetadata creationMetadata: MPMediaPlaylistCreationMetadata?, completionHandler completionHandler: @escaping (MPMediaPlaylist?, Error?) -> Swift.Void) ``` |

Modified [MPMediaLibrary.lastModifiedDate](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621279-lastmodifieddate)

|  | Declaration |
| --- | --- |
| From | ``` var lastModifiedDate: NSDate { get } ``` |
| To | ``` var lastModifiedDate: Date { get } ``` |

Modified [MPMediaLibrary.requestAuthorization(_: (MPMediaLibraryAuthorizationStatus) -> Swift.Void) [class]](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621276-requestauthorization)

|  | Declaration |
| --- | --- |
| From | ``` class func requestAuthorization(_ handler: (MPMediaLibraryAuthorizationStatus) -> Void) ``` |
| To | ``` class func requestAuthorization(_ handler: @escaping (MPMediaLibraryAuthorizationStatus) -> Swift.Void) ``` |

Modified [MPMediaLibraryAuthorizationStatus [enum]](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMediaLibraryAuthorizationStatus : Int {     case NotDetermined     case Denied     case Restricted     case Authorized } ``` |
| To | ``` enum MPMediaLibraryAuthorizationStatus : Int {     case notDetermined     case denied     case restricted     case authorized } ``` |

Modified [MPMediaLibraryAuthorizationStatus.authorized](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/mpmedialibraryauthorizationstatusauthorized)

|  | Declaration |
| --- | --- |
| From | ``` case Authorized ``` |
| To | ``` case authorized ``` |

Modified [MPMediaLibraryAuthorizationStatus.denied](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/mpmedialibraryauthorizationstatusdenied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [MPMediaLibraryAuthorizationStatus.notDetermined](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/notdetermined)

|  | Declaration |
| --- | --- |
| From | ``` case NotDetermined ``` |
| To | ``` case notDetermined ``` |

Modified [MPMediaLibraryAuthorizationStatus.restricted](https://developer.apple.com/documentation/mediaplayer/mpmedialibraryauthorizationstatus/mpmedialibraryauthorizationstatusrestricted)

|  | Declaration |
| --- | --- |
| From | ``` case Restricted ``` |
| To | ``` case restricted ``` |

Modified [MPMediaPickerController](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaPickerController : UIViewController {     init(mediaTypes mediaTypes: MPMediaType)     var mediaTypes: MPMediaType { get }     weak var delegate: MPMediaPickerControllerDelegate?     var allowsPickingMultipleItems: Bool     var showsCloudItems: Bool     var showsItemsWithProtectedAssets: Bool     var prompt: String? } ``` | -- |
| To | ``` class MPMediaPickerController : UIViewController {     init(mediaTypes mediaTypes: MPMediaType)     var mediaTypes: MPMediaType { get }     weak var delegate: MPMediaPickerControllerDelegate?     var allowsPickingMultipleItems: Bool     var showsCloudItems: Bool     var showsItemsWithProtectedAssets: Bool     var prompt: String?     func presentMoviePlayerViewControllerAnimated(_ moviePlayerViewController: MPMoviePlayerViewController!)     func dismissMoviePlayerViewControllerAnimated()     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get }     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)     func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?     var transitionCoordinator: UIViewControllerTransitionCoordinator? { get }     var isModalInPopover: Bool     var contentSizeForViewInPopover: CGSize     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool)     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get }     var previewActionItems: [UIPreviewActionItem] { get }     func registerForPreviewing(with delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewing(withContext previewing: UIViewControllerPreviewing)     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get }     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand)     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get }     weak var transitioningDelegate: UIViewControllerTransitioningDelegate?     func updateViewConstraints()     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     var shouldAutomaticallyForwardAppearanceMethods: Bool { get }     func willMove(toParentViewController parent: UIViewController?)     func didMove(toParentViewController parent: UIViewController?)     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     var childViewControllerForStatusBarStyle: UIViewController? { get }     var childViewControllerForStatusBarHidden: UIViewController? { get }     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollection(forChildViewController childViewController: UIViewController) -> UITraitCollection?     var searchDisplayController: UISearchDisplayController? { get }     var isEditing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var editButtonItem: UIBarButtonItem { get }     class func attemptRotationToDeviceOrientation()     func shouldAutorotate(to toInterfaceOrientation: UIInterfaceOrientation) -> Bool     var shouldAutorotate: Bool { get }     var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }     var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotate(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didRotate(from fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func willAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotation(from fromInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMediaPickerController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension MPMediaPickerController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: UIViewControllerRestoration.Type?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func applicationFinishedRestoringState() } extension MPMediaPickerController : CVarArg { } extension MPMediaPickerController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSExtensionRequestHandling, UIStateRestoring |

Modified [MPMediaPlayback](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback)

|  | Declaration |
| --- | --- |
| From | ``` protocol MPMediaPlayback {     func prepareToPlay()     var isPreparedToPlay: Bool { get }     func play()     func pause()     func stop()     var currentPlaybackTime: NSTimeInterval { get set }     var currentPlaybackRate: Float { get set }     func beginSeekingForward()     func beginSeekingBackward()     func endSeeking() } ``` |
| To | ``` protocol MPMediaPlayback {     func prepareToPlay()     var isPreparedToPlay: Bool { get }     func play()     func pause()     func stop()     var currentPlaybackTime: TimeInterval { get set }     var currentPlaybackRate: Float { get set }     func beginSeekingForward()     func beginSeekingBackward()     func endSeeking() } ``` |

Modified [MPMediaPlayback.currentPlaybackTime](https://developer.apple.com/documentation/mediaplayer/mpmediaplayback/1616253-currentplaybacktime)

|  | Declaration |
| --- | --- |
| From | ``` var currentPlaybackTime: NSTimeInterval { get set } ``` |
| To | ``` var currentPlaybackTime: TimeInterval { get set } ``` |

Modified [MPMediaPlaylist](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaPlaylist : MPMediaItemCollection {     var persistentID: MPMediaEntityPersistentID { get }     var name: String? { get }     var playlistAttributes: MPMediaPlaylistAttribute { get }     var seedItems: [MPMediaItem]? { get }     var descriptionText: String? { get }     var authorDisplayName: String? { get }     func addItemWithProductID(_ productID: String, completionHandler completionHandler: ((NSError?) -> Void)?)     func addMediaItems(_ mediaItems: [MPMediaItem], completionHandler completionHandler: ((NSError?) -> Void)?) } ``` |
| To | ``` class MPMediaPlaylist : MPMediaItemCollection {     var persistentID: MPMediaEntityPersistentID { get }     var name: String? { get }     var playlistAttributes: MPMediaPlaylistAttribute { get }     var seedItems: [MPMediaItem]? { get }     var descriptionText: String? { get }     var authorDisplayName: String? { get }     func addItem(withProductID productID: String, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil)     func add(_ mediaItems: [MPMediaItem], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) } ``` |

Modified [MPMediaPlaylist.add(_: [MPMediaItem], completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618710-addmediaitems)

|  | Declaration |
| --- | --- |
| From | ``` func addMediaItems(_ mediaItems: [MPMediaItem], completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func add(_ mediaItems: [MPMediaItem], completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [MPMediaPlaylist.addItem(withProductID: String, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618706-additemwithproductid)

|  | Declaration |
| --- | --- |
| From | ``` func addItemWithProductID(_ productID: String, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func addItem(withProductID productID: String, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [MPMediaPlaylistAttribute [struct]](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistattribute)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MPMediaPlaylistAttribute : OptionSetType {     init(rawValue rawValue: UInt)     static var None: MPMediaPlaylistAttribute { get }     static var OnTheGo: MPMediaPlaylistAttribute { get }     static var Smart: MPMediaPlaylistAttribute { get }     static var Genius: MPMediaPlaylistAttribute { get } } ``` | OptionSetType |
| To | ``` struct MPMediaPlaylistAttribute : OptionSet {     init(rawValue rawValue: UInt)     static var none: MPMediaPlaylistAttribute { get }     static var onTheGo: MPMediaPlaylistAttribute { get }     static var smart: MPMediaPlaylistAttribute { get }     static var genius: MPMediaPlaylistAttribute { get }     func intersect(_ other: MPMediaPlaylistAttribute) -> MPMediaPlaylistAttribute     func exclusiveOr(_ other: MPMediaPlaylistAttribute) -> MPMediaPlaylistAttribute     mutating func unionInPlace(_ other: MPMediaPlaylistAttribute)     mutating func intersectInPlace(_ other: MPMediaPlaylistAttribute)     mutating func exclusiveOrInPlace(_ other: MPMediaPlaylistAttribute)     func isSubsetOf(_ other: MPMediaPlaylistAttribute) -> Bool     func isDisjointWith(_ other: MPMediaPlaylistAttribute) -> Bool     func isSupersetOf(_ other: MPMediaPlaylistAttribute) -> Bool     mutating func subtractInPlace(_ other: MPMediaPlaylistAttribute)     func isStrictSupersetOf(_ other: MPMediaPlaylistAttribute) -> Bool     func isStrictSubsetOf(_ other: MPMediaPlaylistAttribute) -> Bool } extension MPMediaPlaylistAttribute {     func union(_ other: MPMediaPlaylistAttribute) -> MPMediaPlaylistAttribute     func intersection(_ other: MPMediaPlaylistAttribute) -> MPMediaPlaylistAttribute     func symmetricDifference(_ other: MPMediaPlaylistAttribute) -> MPMediaPlaylistAttribute } extension MPMediaPlaylistAttribute {     func contains(_ member: MPMediaPlaylistAttribute) -> Bool     mutating func insert(_ newMember: MPMediaPlaylistAttribute) -> (inserted: Bool, memberAfterInsert: MPMediaPlaylistAttribute)     mutating func remove(_ member: MPMediaPlaylistAttribute) -> MPMediaPlaylistAttribute?     mutating func update(with newMember: MPMediaPlaylistAttribute) -> MPMediaPlaylistAttribute? } extension MPMediaPlaylistAttribute {     convenience init()     mutating func formUnion(_ other: MPMediaPlaylistAttribute)     mutating func formIntersection(_ other: MPMediaPlaylistAttribute)     mutating func formSymmetricDifference(_ other: MPMediaPlaylistAttribute) } extension MPMediaPlaylistAttribute {     convenience init<S : Sequence where S.Iterator.Element == MPMediaPlaylistAttribute>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MPMediaPlaylistAttribute...)     mutating func subtract(_ other: MPMediaPlaylistAttribute)     func isSubset(of other: MPMediaPlaylistAttribute) -> Bool     func isSuperset(of other: MPMediaPlaylistAttribute) -> Bool     func isDisjoint(with other: MPMediaPlaylistAttribute) -> Bool     func subtracting(_ other: MPMediaPlaylistAttribute) -> MPMediaPlaylistAttribute     var isEmpty: Bool { get }     func isStrictSuperset(of other: MPMediaPlaylistAttribute) -> Bool     func isStrictSubset(of other: MPMediaPlaylistAttribute) -> Bool } ``` | OptionSet |

Modified [MPMediaPlaylistAttribute.genius](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistattribute/1618700-genius)

|  | Declaration |
| --- | --- |
| From | ``` static var Genius: MPMediaPlaylistAttribute { get } ``` |
| To | ``` static var genius: MPMediaPlaylistAttribute { get } ``` |

Modified [MPMediaPlaylistAttribute.onTheGo](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistattribute/1618721-onthego)

|  | Declaration |
| --- | --- |
| From | ``` static var OnTheGo: MPMediaPlaylistAttribute { get } ``` |
| To | ``` static var onTheGo: MPMediaPlaylistAttribute { get } ``` |

Modified [MPMediaPlaylistAttribute.smart](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistattribute/mpmediaplaylistattributesmart)

|  | Declaration |
| --- | --- |
| From | ``` static var Smart: MPMediaPlaylistAttribute { get } ``` |
| To | ``` static var smart: MPMediaPlaylistAttribute { get } ``` |

Modified [MPMediaPlaylistCreationMetadata](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistcreationmetadata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaPlaylistCreationMetadata : NSObject {     convenience init()     init(name name: String)     var name: String { get }     var authorDisplayName: String!     var descriptionText: String } ``` | -- |
| To | ``` class MPMediaPlaylistCreationMetadata : NSObject {     convenience init()     init(name name: String)     var name: String { get }     var authorDisplayName: String!     var descriptionText: String     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMediaPlaylistCreationMetadata : CVarArg { } extension MPMediaPlaylistCreationMetadata : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPMediaPredicate](https://developer.apple.com/documentation/mediaplayer/mpmediapredicate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaPredicate : NSObject, NSSecureCoding { } ``` | NSSecureCoding |
| To | ``` class MPMediaPredicate : NSObject, NSSecureCoding {     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMediaPredicate : CVarArg { } extension MPMediaPredicate : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [MPMediaPredicateComparison [enum]](https://developer.apple.com/documentation/mediaplayer/mpmediapredicatecomparison)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMediaPredicateComparison : Int {     case EqualTo     case Contains } ``` |
| To | ``` enum MPMediaPredicateComparison : Int {     case equalTo     case contains } ``` |

Modified [MPMediaPredicateComparison.contains](https://developer.apple.com/documentation/mediaplayer/mpmediapredicatecomparison/mpmediapredicatecomparisoncontains)

|  | Declaration |
| --- | --- |
| From | ``` case Contains ``` |
| To | ``` case contains ``` |

Modified [MPMediaPredicateComparison.equalTo](https://developer.apple.com/documentation/mediaplayer/mpmediapredicatecomparison/equalto)

|  | Declaration |
| --- | --- |
| From | ``` case EqualTo ``` |
| To | ``` case equalTo ``` |

Modified [MPMediaPropertyPredicate](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaPropertyPredicate : MPMediaPredicate {      init(value value: AnyObject?, forProperty property: String)     class func predicateWithValue(_ value: AnyObject?, forProperty property: String) -> MPMediaPropertyPredicate      init(value value: AnyObject?, forProperty property: String, comparisonType comparisonType: MPMediaPredicateComparison)     class func predicateWithValue(_ value: AnyObject?, forProperty property: String, comparisonType comparisonType: MPMediaPredicateComparison) -> MPMediaPropertyPredicate     var property: String { get }     @NSCopying var value: AnyObject? { get }     var comparisonType: MPMediaPredicateComparison { get } } ``` |
| To | ``` class MPMediaPropertyPredicate : MPMediaPredicate {      init(value value: Any?, forProperty property: String)     class func withValue(_ value: Any?, forProperty property: String) -> MPMediaPropertyPredicate      init(value value: Any?, forProperty property: String, comparisonType comparisonType: MPMediaPredicateComparison)     class func withValue(_ value: Any?, forProperty property: String, comparisonType comparisonType: MPMediaPredicateComparison) -> MPMediaPropertyPredicate     var property: String { get }     var value: Any? { get }     var comparisonType: MPMediaPredicateComparison { get } } ``` |

Modified [MPMediaPropertyPredicate.init(value: Any?, forProperty: String)](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate/1621790-predicatewithvalue)

|  | Declaration |
| --- | --- |
| From | ``` init(value value: AnyObject?, forProperty property: String) ``` |
| To | ``` init(value value: Any?, forProperty property: String) ``` |

Modified [MPMediaPropertyPredicate.init(value: Any?, forProperty: String, comparisonType: MPMediaPredicateComparison)](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate/1621798-init)

|  | Declaration |
| --- | --- |
| From | ``` init(value value: AnyObject?, forProperty property: String, comparisonType comparisonType: MPMediaPredicateComparison) ``` |
| To | ``` init(value value: Any?, forProperty property: String, comparisonType comparisonType: MPMediaPredicateComparison) ``` |

Modified [MPMediaPropertyPredicate.value](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate/1621772-value)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var value: AnyObject? { get } ``` |
| To | ``` var value: Any? { get } ``` |

Modified [MPMediaQuery](https://developer.apple.com/documentation/mediaplayer/mpmediaquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaQuery : NSObject, NSSecureCoding, NSCopying {     init(filterPredicates filterPredicates: Set<MPMediaPredicate>?)     var filterPredicates: Set<MPMediaPredicate>?     func addFilterPredicate(_ predicate: MPMediaPredicate)     func removeFilterPredicate(_ predicate: MPMediaPredicate)     var items: [MPMediaItem]? { get }     var collections: [MPMediaItemCollection]? { get }     var groupingType: MPMediaGrouping     var itemSections: [MPMediaQuerySection]? { get }     var collectionSections: [MPMediaQuerySection]? { get }     class func albumsQuery() -> MPMediaQuery     class func artistsQuery() -> MPMediaQuery     class func songsQuery() -> MPMediaQuery     class func playlistsQuery() -> MPMediaQuery     class func podcastsQuery() -> MPMediaQuery     class func audiobooksQuery() -> MPMediaQuery     class func compilationsQuery() -> MPMediaQuery     class func composersQuery() -> MPMediaQuery     class func genresQuery() -> MPMediaQuery } ``` | NSCopying, NSSecureCoding |
| To | ``` class MPMediaQuery : NSObject, NSSecureCoding, NSCopying {     init(filterPredicates filterPredicates: Set<MPMediaPredicate>?)     var filterPredicates: Set<MPMediaPredicate>?     func addFilterPredicate(_ predicate: MPMediaPredicate)     func removeFilterPredicate(_ predicate: MPMediaPredicate)     var items: [MPMediaItem]? { get }     var collections: [MPMediaItemCollection]? { get }     var groupingType: MPMediaGrouping     var itemSections: [MPMediaQuerySection]? { get }     var collectionSections: [MPMediaQuerySection]? { get }     class func albums() -> MPMediaQuery     class func artists() -> MPMediaQuery     class func songs() -> MPMediaQuery     class func playlists() -> MPMediaQuery     class func podcasts() -> MPMediaQuery     class func audiobooks() -> MPMediaQuery     class func compilations() -> MPMediaQuery     class func composers() -> MPMediaQuery     class func genres() -> MPMediaQuery     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMediaQuery : CVarArg { } extension MPMediaQuery : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [MPMediaQuery.albums() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621780-albums)

|  | Declaration |
| --- | --- |
| From | ``` class func albumsQuery() -> MPMediaQuery ``` |
| To | ``` class func albums() -> MPMediaQuery ``` |

Modified [MPMediaQuery.artists() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621787-artistsquery)

|  | Declaration |
| --- | --- |
| From | ``` class func artistsQuery() -> MPMediaQuery ``` |
| To | ``` class func artists() -> MPMediaQuery ``` |

Modified [MPMediaQuery.audiobooks() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621783-audiobooks)

|  | Declaration |
| --- | --- |
| From | ``` class func audiobooksQuery() -> MPMediaQuery ``` |
| To | ``` class func audiobooks() -> MPMediaQuery ``` |

Modified [MPMediaQuery.compilations() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621786-compilations)

|  | Declaration |
| --- | --- |
| From | ``` class func compilationsQuery() -> MPMediaQuery ``` |
| To | ``` class func compilations() -> MPMediaQuery ``` |

Modified [MPMediaQuery.composers() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621796-composers)

|  | Declaration |
| --- | --- |
| From | ``` class func composersQuery() -> MPMediaQuery ``` |
| To | ``` class func composers() -> MPMediaQuery ``` |

Modified [MPMediaQuery.genres() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621788-genres)

|  | Declaration |
| --- | --- |
| From | ``` class func genresQuery() -> MPMediaQuery ``` |
| To | ``` class func genres() -> MPMediaQuery ``` |

Modified [MPMediaQuery.playlists() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621803-playlistsquery)

|  | Declaration |
| --- | --- |
| From | ``` class func playlistsQuery() -> MPMediaQuery ``` |
| To | ``` class func playlists() -> MPMediaQuery ``` |

Modified [MPMediaQuery.podcasts() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621793-podcasts)

|  | Declaration |
| --- | --- |
| From | ``` class func podcastsQuery() -> MPMediaQuery ``` |
| To | ``` class func podcasts() -> MPMediaQuery ``` |

Modified [MPMediaQuery.songs() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621791-songsquery)

|  | Declaration |
| --- | --- |
| From | ``` class func songsQuery() -> MPMediaQuery ``` |
| To | ``` class func songs() -> MPMediaQuery ``` |

Modified [MPMediaQuerySection](https://developer.apple.com/documentation/mediaplayer/mpmediaquerysection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaQuerySection : NSObject, NSSecureCoding, NSCopying {     var title: String { get }     var range: NSRange { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class MPMediaQuerySection : NSObject, NSSecureCoding, NSCopying {     var title: String { get }     var range: NSRange { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMediaQuerySection : CVarArg { } extension MPMediaQuerySection : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [MPMediaType [struct]](https://developer.apple.com/documentation/mediaplayer/mpmediatype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MPMediaType : OptionSetType {     init(rawValue rawValue: UInt)     static var Music: MPMediaType { get }     static var Podcast: MPMediaType { get }     static var AudioBook: MPMediaType { get }     static var AudioITunesU: MPMediaType { get }     static var AnyAudio: MPMediaType { get }     static var Movie: MPMediaType { get }     static var TVShow: MPMediaType { get }     static var VideoPodcast: MPMediaType { get }     static var MusicVideo: MPMediaType { get }     static var VideoITunesU: MPMediaType { get }     static var HomeVideo: MPMediaType { get }     static var AnyVideo: MPMediaType { get }     static var Any: MPMediaType { get } } ``` | OptionSetType |
| To | ``` struct MPMediaType : OptionSet {     init(rawValue rawValue: UInt)     static var music: MPMediaType { get }     static var podcast: MPMediaType { get }     static var audioBook: MPMediaType { get }     static var audioITunesU: MPMediaType { get }     static var anyAudio: MPMediaType { get }     static var movie: MPMediaType { get }     static var tvShow: MPMediaType { get }     static var videoPodcast: MPMediaType { get }     static var musicVideo: MPMediaType { get }     static var videoITunesU: MPMediaType { get }     static var homeVideo: MPMediaType { get }     static var anyVideo: MPMediaType { get }     static var any: MPMediaType { get }     func intersect(_ other: MPMediaType) -> MPMediaType     func exclusiveOr(_ other: MPMediaType) -> MPMediaType     mutating func unionInPlace(_ other: MPMediaType)     mutating func intersectInPlace(_ other: MPMediaType)     mutating func exclusiveOrInPlace(_ other: MPMediaType)     func isSubsetOf(_ other: MPMediaType) -> Bool     func isDisjointWith(_ other: MPMediaType) -> Bool     func isSupersetOf(_ other: MPMediaType) -> Bool     mutating func subtractInPlace(_ other: MPMediaType)     func isStrictSupersetOf(_ other: MPMediaType) -> Bool     func isStrictSubsetOf(_ other: MPMediaType) -> Bool } extension MPMediaType {     func union(_ other: MPMediaType) -> MPMediaType     func intersection(_ other: MPMediaType) -> MPMediaType     func symmetricDifference(_ other: MPMediaType) -> MPMediaType } extension MPMediaType {     func contains(_ member: MPMediaType) -> Bool     mutating func insert(_ newMember: MPMediaType) -> (inserted: Bool, memberAfterInsert: MPMediaType)     mutating func remove(_ member: MPMediaType) -> MPMediaType?     mutating func update(with newMember: MPMediaType) -> MPMediaType? } extension MPMediaType {     convenience init()     mutating func formUnion(_ other: MPMediaType)     mutating func formIntersection(_ other: MPMediaType)     mutating func formSymmetricDifference(_ other: MPMediaType) } extension MPMediaType {     convenience init<S : Sequence where S.Iterator.Element == MPMediaType>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MPMediaType...)     mutating func subtract(_ other: MPMediaType)     func isSubset(of other: MPMediaType) -> Bool     func isSuperset(of other: MPMediaType) -> Bool     func isDisjoint(with other: MPMediaType) -> Bool     func subtracting(_ other: MPMediaType) -> MPMediaType     var isEmpty: Bool { get }     func isStrictSuperset(of other: MPMediaType) -> Bool     func isStrictSubset(of other: MPMediaType) -> Bool } ``` | OptionSet |

Modified [MPMediaType.any](https://developer.apple.com/documentation/mediaplayer/mpmediatype/1621718-any)

|  | Declaration |
| --- | --- |
| From | ``` static var Any: MPMediaType { get } ``` |
| To | ``` static var any: MPMediaType { get } ``` |

Modified [MPMediaType.anyAudio](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypeanyaudio)

|  | Declaration |
| --- | --- |
| From | ``` static var AnyAudio: MPMediaType { get } ``` |
| To | ``` static var anyAudio: MPMediaType { get } ``` |

Modified [MPMediaType.anyVideo](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypeanyvideo)

|  | Declaration |
| --- | --- |
| From | ``` static var AnyVideo: MPMediaType { get } ``` |
| To | ``` static var anyVideo: MPMediaType { get } ``` |

Modified [MPMediaType.audioBook](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypeaudiobook)

|  | Declaration |
| --- | --- |
| From | ``` static var AudioBook: MPMediaType { get } ``` |
| To | ``` static var audioBook: MPMediaType { get } ``` |

Modified [MPMediaType.audioITunesU](https://developer.apple.com/documentation/mediaplayer/mpmediatype/1621726-audioitunesu)

|  | Declaration |
| --- | --- |
| From | ``` static var AudioITunesU: MPMediaType { get } ``` |
| To | ``` static var audioITunesU: MPMediaType { get } ``` |

Modified [MPMediaType.homeVideo](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypehomevideo)

|  | Declaration |
| --- | --- |
| From | ``` static var HomeVideo: MPMediaType { get } ``` |
| To | ``` static var homeVideo: MPMediaType { get } ``` |

Modified [MPMediaType.movie](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypemovie)

|  | Declaration |
| --- | --- |
| From | ``` static var Movie: MPMediaType { get } ``` |
| To | ``` static var movie: MPMediaType { get } ``` |

Modified [MPMediaType.music](https://developer.apple.com/documentation/mediaplayer/mpmediatype/1621689-music)

|  | Declaration |
| --- | --- |
| From | ``` static var Music: MPMediaType { get } ``` |
| To | ``` static var music: MPMediaType { get } ``` |

Modified [MPMediaType.musicVideo](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypemusicvideo)

|  | Declaration |
| --- | --- |
| From | ``` static var MusicVideo: MPMediaType { get } ``` |
| To | ``` static var musicVideo: MPMediaType { get } ``` |

Modified [MPMediaType.podcast](https://developer.apple.com/documentation/mediaplayer/mpmediatype/mpmediatypepodcast)

|  | Declaration |
| --- | --- |
| From | ``` static var Podcast: MPMediaType { get } ``` |
| To | ``` static var podcast: MPMediaType { get } ``` |

Modified [MPMediaType.tvShow](https://developer.apple.com/documentation/mediaplayer/mpmediatype/1621701-tvshow)

|  | Declaration |
| --- | --- |
| From | ``` static var TVShow: MPMediaType { get } ``` |
| To | ``` static var tvShow: MPMediaType { get } ``` |

Modified [MPMediaType.videoITunesU](https://developer.apple.com/documentation/mediaplayer/mpmediatype/1621764-videoitunesu)

|  | Declaration |
| --- | --- |
| From | ``` static var VideoITunesU: MPMediaType { get } ``` |
| To | ``` static var videoITunesU: MPMediaType { get } ``` |

Modified [MPMediaType.videoPodcast](https://developer.apple.com/documentation/mediaplayer/mpmediatype/1621765-videopodcast)

|  | Declaration |
| --- | --- |
| From | ``` static var VideoPodcast: MPMediaType { get } ``` |
| To | ``` static var videoPodcast: MPMediaType { get } ``` |

Modified [MPMovieAccessLog](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMovieAccessLog : NSObject, NSCopying {     var extendedLogData: NSData! { get }     var extendedLogDataStringEncoding: UInt { get }     var events: [AnyObject]! { get } } ``` | NSCopying |
| To | ``` class MPMovieAccessLog : NSObject, NSCopying {     var extendedLogData: Data! { get }     var extendedLogDataStringEncoding: UInt { get }     var events: [Any]! { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMovieAccessLog : CVarArg { } extension MPMovieAccessLog : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MPMovieAccessLog.events](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/1620820-events)

|  | Declaration |
| --- | --- |
| From | ``` var events: [AnyObject]! { get } ``` |
| To | ``` var events: [Any]! { get } ``` |

Modified [MPMovieAccessLog.extendedLogData](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/1620870-extendedlogdata)

|  | Declaration |
| --- | --- |
| From | ``` var extendedLogData: NSData! { get } ``` |
| To | ``` var extendedLogData: Data! { get } ``` |

Modified [MPMovieAccessLogEvent](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMovieAccessLogEvent : NSObject, NSCopying {     var numberOfSegmentsDownloaded: Int { get }     var playbackStartDate: NSDate! { get }     var URI: String! { get }     var serverAddress: String! { get }     var numberOfServerAddressChanges: Int { get }     var playbackSessionID: String! { get }     var playbackStartOffset: NSTimeInterval { get }     var segmentsDownloadedDuration: NSTimeInterval { get }     var durationWatched: NSTimeInterval { get }     var numberOfStalls: Int { get }     var numberOfBytesTransferred: Int64 { get }     var observedBitrate: Double { get }     var indicatedBitrate: Double { get }     var numberOfDroppedVideoFrames: Int { get } } ``` | NSCopying |
| To | ``` class MPMovieAccessLogEvent : NSObject, NSCopying {     var numberOfSegmentsDownloaded: Int { get }     var playbackStartDate: Date! { get }     var uri: String! { get }     var serverAddress: String! { get }     var numberOfServerAddressChanges: Int { get }     var playbackSessionID: String! { get }     var playbackStartOffset: TimeInterval { get }     var segmentsDownloadedDuration: TimeInterval { get }     var durationWatched: TimeInterval { get }     var numberOfStalls: Int { get }     var numberOfBytesTransferred: Int64 { get }     var observedBitrate: Double { get }     var indicatedBitrate: Double { get }     var numberOfDroppedVideoFrames: Int { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMovieAccessLogEvent : CVarArg { } extension MPMovieAccessLogEvent : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MPMovieAccessLogEvent.durationWatched](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620880-durationwatched)

|  | Declaration |
| --- | --- |
| From | ``` var durationWatched: NSTimeInterval { get } ``` |
| To | ``` var durationWatched: TimeInterval { get } ``` |

Modified [MPMovieAccessLogEvent.playbackStartDate](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620868-playbackstartdate)

|  | Declaration |
| --- | --- |
| From | ``` var playbackStartDate: NSDate! { get } ``` |
| To | ``` var playbackStartDate: Date! { get } ``` |

Modified [MPMovieAccessLogEvent.playbackStartOffset](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620902-playbackstartoffset)

|  | Declaration |
| --- | --- |
| From | ``` var playbackStartOffset: NSTimeInterval { get } ``` |
| To | ``` var playbackStartOffset: TimeInterval { get } ``` |

Modified [MPMovieAccessLogEvent.segmentsDownloadedDuration](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620944-segmentsdownloadedduration)

|  | Declaration |
| --- | --- |
| From | ``` var segmentsDownloadedDuration: NSTimeInterval { get } ``` |
| To | ``` var segmentsDownloadedDuration: TimeInterval { get } ``` |

Modified [MPMovieAccessLogEvent.uri](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620959-uri)

|  | Declaration |
| --- | --- |
| From | ``` var URI: String! { get } ``` |
| To | ``` var uri: String! { get } ``` |

Modified [MPMovieControlStyle [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMovieControlStyle : Int {     case None     case Embedded     case Fullscreen     static var Default: MPMovieControlStyle { get } } ``` |
| To | ``` enum MPMovieControlStyle : Int {     case none     case embedded     case fullscreen     static var `default`: MPMovieControlStyle { get } } ``` |

Modified [MPMovieControlStyle.default](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle/mpmoviecontrolstyledefault)

|  | Declaration |
| --- | --- |
| From | ``` static var Default: MPMovieControlStyle { get } ``` |
| To | ``` static var `default`: MPMovieControlStyle { get } ``` |

Modified [MPMovieControlStyle.embedded](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle/embedded)

|  | Declaration |
| --- | --- |
| From | ``` case Embedded ``` |
| To | ``` case embedded ``` |

Modified [MPMovieControlStyle.fullscreen](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle/mpmoviecontrolstylefullscreen)

|  | Declaration |
| --- | --- |
| From | ``` case Fullscreen ``` |
| To | ``` case fullscreen ``` |

Modified [MPMovieControlStyle.none](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MPMovieErrorLog](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMovieErrorLog : NSObject, NSCopying {     var extendedLogData: NSData! { get }     var extendedLogDataStringEncoding: UInt { get }     var events: [AnyObject]! { get } } ``` | NSCopying |
| To | ``` class MPMovieErrorLog : NSObject, NSCopying {     var extendedLogData: Data! { get }     var extendedLogDataStringEncoding: UInt { get }     var events: [Any]! { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMovieErrorLog : CVarArg { } extension MPMovieErrorLog : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MPMovieErrorLog.events](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/1620929-events)

|  | Declaration |
| --- | --- |
| From | ``` var events: [AnyObject]! { get } ``` |
| To | ``` var events: [Any]! { get } ``` |

Modified [MPMovieErrorLog.extendedLogData](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/1620797-extendedlogdata)

|  | Declaration |
| --- | --- |
| From | ``` var extendedLogData: NSData! { get } ``` |
| To | ``` var extendedLogData: Data! { get } ``` |

Modified [MPMovieErrorLogEvent](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMovieErrorLogEvent : NSObject, NSCopying {     var date: NSDate! { get }     var URI: String! { get }     var serverAddress: String! { get }     var playbackSessionID: String! { get }     var errorStatusCode: Int { get }     var errorDomain: String! { get }     var errorComment: String! { get } } ``` | NSCopying |
| To | ``` class MPMovieErrorLogEvent : NSObject, NSCopying {     var date: Date! { get }     var uri: String! { get }     var serverAddress: String! { get }     var playbackSessionID: String! { get }     var errorStatusCode: Int { get }     var errorDomain: String! { get }     var errorComment: String! { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMovieErrorLogEvent : CVarArg { } extension MPMovieErrorLogEvent : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying |

Modified [MPMovieErrorLogEvent.date](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620794-date)

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate! { get } ``` |
| To | ``` var date: Date! { get } ``` |

Modified [MPMovieErrorLogEvent.uri](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620913-uri)

|  | Declaration |
| --- | --- |
| From | ``` var URI: String! { get } ``` |
| To | ``` var uri: String! { get } ``` |

Modified [MPMovieFinishReason [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviefinishreason)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMovieFinishReason : Int {     case PlaybackEnded     case PlaybackError     case UserExited } ``` |
| To | ``` enum MPMovieFinishReason : Int {     case playbackEnded     case playbackError     case userExited } ``` |

Modified [MPMovieFinishReason.playbackEnded](https://developer.apple.com/documentation/mediaplayer/mpmoviefinishreason/mpmoviefinishreasonplaybackended)

|  | Declaration |
| --- | --- |
| From | ``` case PlaybackEnded ``` |
| To | ``` case playbackEnded ``` |

Modified [MPMovieFinishReason.playbackError](https://developer.apple.com/documentation/mediaplayer/mpmoviefinishreason/playbackerror)

|  | Declaration |
| --- | --- |
| From | ``` case PlaybackError ``` |
| To | ``` case playbackError ``` |

Modified [MPMovieFinishReason.userExited](https://developer.apple.com/documentation/mediaplayer/mpmoviefinishreason/userexited)

|  | Declaration |
| --- | --- |
| From | ``` case UserExited ``` |
| To | ``` case userExited ``` |

Modified [MPMovieLoadState [struct]](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MPMovieLoadState : OptionSetType {     init(rawValue rawValue: UInt)     static var Unknown: MPMovieLoadState { get }     static var Playable: MPMovieLoadState { get }     static var PlaythroughOK: MPMovieLoadState { get }     static var Stalled: MPMovieLoadState { get } } ``` | OptionSetType |
| To | ``` struct MPMovieLoadState : OptionSet {     init(rawValue rawValue: UInt)     static var unknown: MPMovieLoadState { get }     static var playable: MPMovieLoadState { get }     static var playthroughOK: MPMovieLoadState { get }     static var stalled: MPMovieLoadState { get }     func intersect(_ other: MPMovieLoadState) -> MPMovieLoadState     func exclusiveOr(_ other: MPMovieLoadState) -> MPMovieLoadState     mutating func unionInPlace(_ other: MPMovieLoadState)     mutating func intersectInPlace(_ other: MPMovieLoadState)     mutating func exclusiveOrInPlace(_ other: MPMovieLoadState)     func isSubsetOf(_ other: MPMovieLoadState) -> Bool     func isDisjointWith(_ other: MPMovieLoadState) -> Bool     func isSupersetOf(_ other: MPMovieLoadState) -> Bool     mutating func subtractInPlace(_ other: MPMovieLoadState)     func isStrictSupersetOf(_ other: MPMovieLoadState) -> Bool     func isStrictSubsetOf(_ other: MPMovieLoadState) -> Bool } extension MPMovieLoadState {     func union(_ other: MPMovieLoadState) -> MPMovieLoadState     func intersection(_ other: MPMovieLoadState) -> MPMovieLoadState     func symmetricDifference(_ other: MPMovieLoadState) -> MPMovieLoadState } extension MPMovieLoadState {     func contains(_ member: MPMovieLoadState) -> Bool     mutating func insert(_ newMember: MPMovieLoadState) -> (inserted: Bool, memberAfterInsert: MPMovieLoadState)     mutating func remove(_ member: MPMovieLoadState) -> MPMovieLoadState?     mutating func update(with newMember: MPMovieLoadState) -> MPMovieLoadState? } extension MPMovieLoadState {     convenience init()     mutating func formUnion(_ other: MPMovieLoadState)     mutating func formIntersection(_ other: MPMovieLoadState)     mutating func formSymmetricDifference(_ other: MPMovieLoadState) } extension MPMovieLoadState {     convenience init<S : Sequence where S.Iterator.Element == MPMovieLoadState>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MPMovieLoadState...)     mutating func subtract(_ other: MPMovieLoadState)     func isSubset(of other: MPMovieLoadState) -> Bool     func isSuperset(of other: MPMovieLoadState) -> Bool     func isDisjoint(with other: MPMovieLoadState) -> Bool     func subtracting(_ other: MPMovieLoadState) -> MPMovieLoadState     var isEmpty: Bool { get }     func isStrictSuperset(of other: MPMovieLoadState) -> Bool     func isStrictSubset(of other: MPMovieLoadState) -> Bool } ``` | OptionSet |

Modified [MPMovieLoadState.playable](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/1620892-playable)

|  | Declaration |
| --- | --- |
| From | ``` static var Playable: MPMovieLoadState { get } ``` |
| To | ``` static var playable: MPMovieLoadState { get } ``` |

Modified [MPMovieLoadState.playthroughOK](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/1620865-playthroughok)

|  | Declaration |
| --- | --- |
| From | ``` static var PlaythroughOK: MPMovieLoadState { get } ``` |
| To | ``` static var playthroughOK: MPMovieLoadState { get } ``` |

Modified [MPMovieLoadState.stalled](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/1620939-stalled)

|  | Declaration |
| --- | --- |
| From | ``` static var Stalled: MPMovieLoadState { get } ``` |
| To | ``` static var stalled: MPMovieLoadState { get } ``` |

Modified [MPMovieMediaTypeMask [struct]](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MPMovieMediaTypeMask : OptionSetType {     init(rawValue rawValue: UInt)     static var None: MPMovieMediaTypeMask { get }     static var Video: MPMovieMediaTypeMask { get }     static var Audio: MPMovieMediaTypeMask { get } } ``` | OptionSetType |
| To | ``` struct MPMovieMediaTypeMask : OptionSet {     init(rawValue rawValue: UInt)     static var none: MPMovieMediaTypeMask { get }     static var video: MPMovieMediaTypeMask { get }     static var audio: MPMovieMediaTypeMask { get }     func intersect(_ other: MPMovieMediaTypeMask) -> MPMovieMediaTypeMask     func exclusiveOr(_ other: MPMovieMediaTypeMask) -> MPMovieMediaTypeMask     mutating func unionInPlace(_ other: MPMovieMediaTypeMask)     mutating func intersectInPlace(_ other: MPMovieMediaTypeMask)     mutating func exclusiveOrInPlace(_ other: MPMovieMediaTypeMask)     func isSubsetOf(_ other: MPMovieMediaTypeMask) -> Bool     func isDisjointWith(_ other: MPMovieMediaTypeMask) -> Bool     func isSupersetOf(_ other: MPMovieMediaTypeMask) -> Bool     mutating func subtractInPlace(_ other: MPMovieMediaTypeMask)     func isStrictSupersetOf(_ other: MPMovieMediaTypeMask) -> Bool     func isStrictSubsetOf(_ other: MPMovieMediaTypeMask) -> Bool } extension MPMovieMediaTypeMask {     func union(_ other: MPMovieMediaTypeMask) -> MPMovieMediaTypeMask     func intersection(_ other: MPMovieMediaTypeMask) -> MPMovieMediaTypeMask     func symmetricDifference(_ other: MPMovieMediaTypeMask) -> MPMovieMediaTypeMask } extension MPMovieMediaTypeMask {     func contains(_ member: MPMovieMediaTypeMask) -> Bool     mutating func insert(_ newMember: MPMovieMediaTypeMask) -> (inserted: Bool, memberAfterInsert: MPMovieMediaTypeMask)     mutating func remove(_ member: MPMovieMediaTypeMask) -> MPMovieMediaTypeMask?     mutating func update(with newMember: MPMovieMediaTypeMask) -> MPMovieMediaTypeMask? } extension MPMovieMediaTypeMask {     convenience init()     mutating func formUnion(_ other: MPMovieMediaTypeMask)     mutating func formIntersection(_ other: MPMovieMediaTypeMask)     mutating func formSymmetricDifference(_ other: MPMovieMediaTypeMask) } extension MPMovieMediaTypeMask {     convenience init<S : Sequence where S.Iterator.Element == MPMovieMediaTypeMask>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: MPMovieMediaTypeMask...)     mutating func subtract(_ other: MPMovieMediaTypeMask)     func isSubset(of other: MPMovieMediaTypeMask) -> Bool     func isSuperset(of other: MPMovieMediaTypeMask) -> Bool     func isDisjoint(with other: MPMovieMediaTypeMask) -> Bool     func subtracting(_ other: MPMovieMediaTypeMask) -> MPMovieMediaTypeMask     var isEmpty: Bool { get }     func isStrictSuperset(of other: MPMovieMediaTypeMask) -> Bool     func isStrictSubset(of other: MPMovieMediaTypeMask) -> Bool } ``` | OptionSet |

Modified [MPMovieMediaTypeMask.audio](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask/mpmoviemediatypemaskaudio)

|  | Declaration |
| --- | --- |
| From | ``` static var Audio: MPMovieMediaTypeMask { get } ``` |
| To | ``` static var audio: MPMovieMediaTypeMask { get } ``` |

Modified [MPMovieMediaTypeMask.video](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask/mpmoviemediatypemaskvideo)

|  | Declaration |
| --- | --- |
| From | ``` static var Video: MPMovieMediaTypeMask { get } ``` |
| To | ``` static var video: MPMovieMediaTypeMask { get } ``` |

Modified [MPMoviePlaybackState [enum]](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMoviePlaybackState : Int {     case Stopped     case Playing     case Paused     case Interrupted     case SeekingForward     case SeekingBackward } ``` |
| To | ``` enum MPMoviePlaybackState : Int {     case stopped     case playing     case paused     case interrupted     case seekingForward     case seekingBackward } ``` |

Modified [MPMoviePlaybackState.interrupted](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstateinterrupted)

|  | Declaration |
| --- | --- |
| From | ``` case Interrupted ``` |
| To | ``` case interrupted ``` |

Modified [MPMoviePlaybackState.paused](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstatepaused)

|  | Declaration |
| --- | --- |
| From | ``` case Paused ``` |
| To | ``` case paused ``` |

Modified [MPMoviePlaybackState.playing](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstateplaying)

|  | Declaration |
| --- | --- |
| From | ``` case Playing ``` |
| To | ``` case playing ``` |

Modified [MPMoviePlaybackState.seekingBackward](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstateseekingbackward)

|  | Declaration |
| --- | --- |
| From | ``` case SeekingBackward ``` |
| To | ``` case seekingBackward ``` |

Modified [MPMoviePlaybackState.seekingForward](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstateseekingforward)

|  | Declaration |
| --- | --- |
| From | ``` case SeekingForward ``` |
| To | ``` case seekingForward ``` |

Modified [MPMoviePlaybackState.stopped](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstatestopped)

|  | Declaration |
| --- | --- |
| From | ``` case Stopped ``` |
| To | ``` case stopped ``` |

Modified [MPMoviePlayerController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMoviePlayerController : NSObject, MPMediaPlayback {     init!(contentURL url: NSURL!)     @NSCopying var contentURL: NSURL!     var view: UIView! { get }     var backgroundView: UIView! { get }     var playbackState: MPMoviePlaybackState { get }     var loadState: MPMovieLoadState { get }     var controlStyle: MPMovieControlStyle     var repeatMode: MPMovieRepeatMode     var shouldAutoplay: Bool     var fullscreen: Bool     func setFullscreen(_ fullscreen: Bool, animated animated: Bool)     var scalingMode: MPMovieScalingMode     var readyForDisplay: Bool { get } } extension MPMoviePlayerController {     var movieMediaTypes: MPMovieMediaTypeMask { get }     var movieSourceType: MPMovieSourceType     var duration: NSTimeInterval { get }     var playableDuration: NSTimeInterval { get }     var naturalSize: CGSize { get }     var initialPlaybackTime: NSTimeInterval     var endPlaybackTime: NSTimeInterval     var allowsAirPlay: Bool     var airPlayVideoActive: Bool { get } } extension MPMoviePlayerController {     func thumbnailImageAtTime(_ playbackTime: NSTimeInterval, timeOption option: MPMovieTimeOption) -> UIImage!     func requestThumbnailImagesAtTimes(_ playbackTimes: [AnyObject]!, timeOption option: MPMovieTimeOption)     func cancelAllThumbnailImageRequests() } extension MPMoviePlayerController {     var timedMetadata: [AnyObject]! { get } } extension MPMoviePlayerController {     var accessLog: MPMovieAccessLog! { get }     var errorLog: MPMovieErrorLog! { get } } extension MPMoviePlayerController {     var useApplicationAudioSession: Bool } extension MPMoviePlayerController {     class func preparePrerollAds()     func playPrerollAdWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     func cancelPreroll() } ``` | MPMediaPlayback |
| To | ``` class MPMoviePlayerController : NSObject, MPMediaPlayback {     init!(contentURL url: URL!)     var contentURL: URL!     var view: UIView! { get }     var backgroundView: UIView! { get }     var playbackState: MPMoviePlaybackState { get }     var loadState: MPMovieLoadState { get }     var controlStyle: MPMovieControlStyle     var repeatMode: MPMovieRepeatMode     var shouldAutoplay: Bool     var isFullscreen: Bool     func setFullscreen(_ fullscreen: Bool, animated animated: Bool)     var scalingMode: MPMovieScalingMode     var readyForDisplay: Bool { get }     var useApplicationAudioSession: Bool     var accessLog: MPMovieAccessLog! { get }     var errorLog: MPMovieErrorLog! { get }     var timedMetadata: [Any]! { get }     func thumbnailImage(atTime playbackTime: TimeInterval, timeOption option: MPMovieTimeOption) -> UIImage!     func requestThumbnailImages(atTimes playbackTimes: [Any]!, timeOption option: MPMovieTimeOption)     func cancelAllThumbnailImageRequests()     var movieMediaTypes: MPMovieMediaTypeMask { get }     var movieSourceType: MPMovieSourceType     var duration: TimeInterval { get }     var playableDuration: TimeInterval { get }     var naturalSize: CGSize { get }     var initialPlaybackTime: TimeInterval     var endPlaybackTime: TimeInterval     var allowsAirPlay: Bool     var isAirPlayVideoActive: Bool { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMoviePlayerController : CVarArg { } extension MPMoviePlayerController : Equatable, Hashable {     var hashValue: Int { get } } extension MPMoviePlayerController {     var movieMediaTypes: MPMovieMediaTypeMask { get }     var movieSourceType: MPMovieSourceType     var duration: TimeInterval { get }     var playableDuration: TimeInterval { get }     var naturalSize: CGSize { get }     var initialPlaybackTime: TimeInterval     var endPlaybackTime: TimeInterval     var allowsAirPlay: Bool     var isAirPlayVideoActive: Bool { get } } extension MPMoviePlayerController {     func thumbnailImage(atTime playbackTime: TimeInterval, timeOption option: MPMovieTimeOption) -> UIImage!     func requestThumbnailImages(atTimes playbackTimes: [Any]!, timeOption option: MPMovieTimeOption)     func cancelAllThumbnailImageRequests() } extension MPMoviePlayerController {     var timedMetadata: [Any]! { get } } extension MPMoviePlayerController {     var accessLog: MPMovieAccessLog! { get }     var errorLog: MPMovieErrorLog! { get } } extension MPMoviePlayerController {     var useApplicationAudioSession: Bool } extension MPMoviePlayerController {     class func preparePrerollAds()     func playPrerollAd(completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)!)     func cancelPreroll() } ``` | CVarArg, Equatable, Hashable, MPMediaPlayback |

Modified [MPMoviePlayerController.contentURL](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620847-contenturl)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var contentURL: NSURL! ``` |
| To | ``` var contentURL: URL! ``` |

Modified [MPMoviePlayerController.duration](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620784-duration)

|  | Declaration |
| --- | --- |
| From | ``` var duration: NSTimeInterval { get } ``` |
| To | ``` var duration: TimeInterval { get } ``` |

Modified [MPMoviePlayerController.endPlaybackTime](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620895-endplaybacktime)

|  | Declaration |
| --- | --- |
| From | ``` var endPlaybackTime: NSTimeInterval ``` |
| To | ``` var endPlaybackTime: TimeInterval ``` |

Modified [MPMoviePlayerController.init(contentURL: URL!)](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620850-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentURL url: NSURL!) ``` |
| To | ``` init!(contentURL url: URL!) ``` |

Modified [MPMoviePlayerController.initialPlaybackTime](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620796-initialplaybacktime)

|  | Declaration |
| --- | --- |
| From | ``` var initialPlaybackTime: NSTimeInterval ``` |
| To | ``` var initialPlaybackTime: TimeInterval ``` |

Modified [MPMoviePlayerController.isAirPlayVideoActive](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620906-airplayvideoactive)

|  | Declaration |
| --- | --- |
| From | ``` var airPlayVideoActive: Bool { get } ``` |
| To | ``` var isAirPlayVideoActive: Bool { get } ``` |

Modified [MPMoviePlayerController.isFullscreen](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620875-fullscreen)

|  | Declaration |
| --- | --- |
| From | ``` var fullscreen: Bool ``` |
| To | ``` var isFullscreen: Bool ``` |

Modified [MPMoviePlayerController.playableDuration](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620803-playableduration)

|  | Declaration |
| --- | --- |
| From | ``` var playableDuration: NSTimeInterval { get } ``` |
| To | ``` var playableDuration: TimeInterval { get } ``` |

Modified [MPMoviePlayerController.requestThumbnailImages(atTimes: [Any]!, timeOption: MPMovieTimeOption)](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620805-requestthumbnailimages)

|  | Declaration |
| --- | --- |
| From | ``` func requestThumbnailImagesAtTimes(_ playbackTimes: [AnyObject]!, timeOption option: MPMovieTimeOption) ``` |
| To | ``` func requestThumbnailImages(atTimes playbackTimes: [Any]!, timeOption option: MPMovieTimeOption) ``` |

Modified [MPMoviePlayerController.timedMetadata](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620853-timedmetadata)

|  | Declaration |
| --- | --- |
| From | ``` var timedMetadata: [AnyObject]! { get } ``` |
| To | ``` var timedMetadata: [Any]! { get } ``` |

Modified [MPMoviePlayerViewController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMoviePlayerViewController : UIViewController {     init!(contentURL contentURL: NSURL!)     var moviePlayer: MPMoviePlayerController! { get } } ``` | -- |
| To | ``` class MPMoviePlayerViewController : UIViewController {     init!(contentURL contentURL: URL!)     var moviePlayer: MPMoviePlayerController! { get }     func presentMoviePlayerViewControllerAnimated(_ moviePlayerViewController: MPMoviePlayerViewController!)     func dismissMoviePlayerViewControllerAnimated()     var tabBarItem: UITabBarItem!     var tabBarController: UITabBarController? { get }     var splitViewController: UISplitViewController? { get }     func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)     func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?     var transitionCoordinator: UIViewControllerTransitionCoordinator? { get }     var isModalInPopover: Bool     var contentSizeForViewInPopover: CGSize     var toolbarItems: [UIBarButtonItem]?     func setToolbarItems(_ toolbarItems: [UIBarButtonItem]?, animated animated: Bool)     var navigationItem: UINavigationItem { get }     var hidesBottomBarWhenPushed: Bool     var navigationController: UINavigationController? { get }     var previewActionItems: [UIPreviewActionItem] { get }     func registerForPreviewing(with delegate: UIViewControllerPreviewingDelegate, sourceView sourceView: UIView) -> UIViewControllerPreviewing     func unregisterForPreviewing(withContext previewing: UIViewControllerPreviewing)     var presentationController: UIPresentationController? { get }     var popoverPresentationController: UIPopoverPresentationController? { get }     func addKeyCommand(_ keyCommand: UIKeyCommand)     func removeKeyCommand(_ keyCommand: UIKeyCommand)     var topLayoutGuide: UILayoutSupport { get }     var bottomLayoutGuide: UILayoutSupport { get }     weak var transitioningDelegate: UIViewControllerTransitioningDelegate?     func updateViewConstraints()     func automaticallyForwardAppearanceAndRotationMethodsToChildViewControllers() -> Bool     func shouldAutomaticallyForwardRotationMethods() -> Bool     var shouldAutomaticallyForwardAppearanceMethods: Bool { get }     func willMove(toParentViewController parent: UIViewController?)     func didMove(toParentViewController parent: UIViewController?)     var childViewControllers: [UIViewController] { get }     func addChildViewController(_ childController: UIViewController)     func removeFromParentViewController()     func transition(from fromViewController: UIViewController, to toViewController: UIViewController, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     func beginAppearanceTransition(_ isAppearing: Bool, animated animated: Bool)     func endAppearanceTransition()     var childViewControllerForStatusBarStyle: UIViewController? { get }     var childViewControllerForStatusBarHidden: UIViewController? { get }     func setOverrideTraitCollection(_ collection: UITraitCollection?, forChildViewController childViewController: UIViewController)     func overrideTraitCollection(forChildViewController childViewController: UIViewController) -> UITraitCollection?     var searchDisplayController: UISearchDisplayController? { get }     var isEditing: Bool     func setEditing(_ editing: Bool, animated animated: Bool)     var editButtonItem: UIBarButtonItem { get }     class func attemptRotationToDeviceOrientation()     func shouldAutorotate(to toInterfaceOrientation: UIInterfaceOrientation) -> Bool     var shouldAutorotate: Bool { get }     var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }     var preferredInterfaceOrientationForPresentation: UIInterfaceOrientation { get }     func rotatingHeaderView() -> UIView?     func rotatingFooterView() -> UIView?     var interfaceOrientation: UIInterfaceOrientation { get }     func willRotate(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didRotate(from fromInterfaceOrientation: UIInterfaceOrientation)     func willAnimateRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func willAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     func didAnimateFirstHalfOfRotation(to toInterfaceOrientation: UIInterfaceOrientation)     func willAnimateSecondHalfOfRotation(from fromInterfaceOrientation: UIInterfaceOrientation, duration duration: TimeInterval)     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMoviePlayerViewController : NSExtensionRequestHandling {     var extensionContext: NSExtensionContext? { get } } extension MPMoviePlayerViewController : UIStateRestoring {     var restorationIdentifier: String?     var restorationClass: UIViewControllerRestoration.Type?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func applicationFinishedRestoringState() } extension MPMoviePlayerViewController : CVarArg { } extension MPMoviePlayerViewController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSExtensionRequestHandling, UIStateRestoring |

Modified [MPMoviePlayerViewController.init(contentURL: URL!)](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller/1622348-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentURL contentURL: NSURL!) ``` |
| To | ``` init!(contentURL contentURL: URL!) ``` |

Modified [MPMovieRepeatMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmovierepeatmode)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMovieRepeatMode : Int {     case None     case One } ``` |
| To | ``` enum MPMovieRepeatMode : Int {     case none     case one } ``` |

Modified [MPMovieRepeatMode.none](https://developer.apple.com/documentation/mediaplayer/mpmovierepeatmode/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MPMovieRepeatMode.one](https://developer.apple.com/documentation/mediaplayer/mpmovierepeatmode/one)

|  | Declaration |
| --- | --- |
| From | ``` case One ``` |
| To | ``` case one ``` |

Modified [MPMovieScalingMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMovieScalingMode : Int {     case None     case AspectFit     case AspectFill     case Fill } ``` |
| To | ``` enum MPMovieScalingMode : Int {     case none     case aspectFit     case aspectFill     case fill } ``` |

Modified [MPMovieScalingMode.aspectFill](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode/mpmoviescalingmodeaspectfill)

|  | Declaration |
| --- | --- |
| From | ``` case AspectFill ``` |
| To | ``` case aspectFill ``` |

Modified [MPMovieScalingMode.aspectFit](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode/aspectfit)

|  | Declaration |
| --- | --- |
| From | ``` case AspectFit ``` |
| To | ``` case aspectFit ``` |

Modified [MPMovieScalingMode.fill](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode/mpmoviescalingmodefill)

|  | Declaration |
| --- | --- |
| From | ``` case Fill ``` |
| To | ``` case fill ``` |

Modified [MPMovieScalingMode.none](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MPMovieSourceType [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetype)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMovieSourceType : Int {     case Unknown     case File     case Streaming } ``` |
| To | ``` enum MPMovieSourceType : Int {     case unknown     case file     case streaming } ``` |

Modified [MPMovieSourceType.file](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetype/file)

|  | Declaration |
| --- | --- |
| From | ``` case File ``` |
| To | ``` case file ``` |

Modified [MPMovieSourceType.streaming](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetype/streaming)

|  | Declaration |
| --- | --- |
| From | ``` case Streaming ``` |
| To | ``` case streaming ``` |

Modified [MPMovieSourceType.unknown](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetype/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [MPMovieTimeOption [enum]](https://developer.apple.com/documentation/mediaplayer/mpmovietimeoption)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMovieTimeOption : Int {     case NearestKeyFrame     case Exact } ``` |
| To | ``` enum MPMovieTimeOption : Int {     case nearestKeyFrame     case exact } ``` |

Modified [MPMovieTimeOption.exact](https://developer.apple.com/documentation/mediaplayer/mpmovietimeoption/mpmovietimeoptionexact)

|  | Declaration |
| --- | --- |
| From | ``` case Exact ``` |
| To | ``` case exact ``` |

Modified [MPMovieTimeOption.nearestKeyFrame](https://developer.apple.com/documentation/mediaplayer/mpmovietimeoption/mpmovietimeoptionnearestkeyframe)

|  | Declaration |
| --- | --- |
| From | ``` case NearestKeyFrame ``` |
| To | ``` case nearestKeyFrame ``` |

Modified [MPMusicPlaybackState [enum]](https://developer.apple.com/documentation/mediaplayer/mpmusicplaybackstate)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMusicPlaybackState : Int {     case Stopped     case Playing     case Paused     case Interrupted     case SeekingForward     case SeekingBackward } ``` |
| To | ``` enum MPMusicPlaybackState : Int {     case stopped     case playing     case paused     case interrupted     case seekingForward     case seekingBackward } ``` |

Modified [MPMusicPlaybackState.interrupted](https://developer.apple.com/documentation/mediaplayer/mpmusicplaybackstate/mpmusicplaybackstateinterrupted)

|  | Declaration |
| --- | --- |
| From | ``` case Interrupted ``` |
| To | ``` case interrupted ``` |

Modified [MPMusicPlaybackState.paused](https://developer.apple.com/documentation/mediaplayer/mpmusicplaybackstate/paused)

|  | Declaration |
| --- | --- |
| From | ``` case Paused ``` |
| To | ``` case paused ``` |

Modified [MPMusicPlaybackState.playing](https://developer.apple.com/documentation/mediaplayer/mpmusicplaybackstate/mpmusicplaybackstateplaying)

|  | Declaration |
| --- | --- |
| From | ``` case Playing ``` |
| To | ``` case playing ``` |

Modified [MPMusicPlaybackState.seekingBackward](https://developer.apple.com/documentation/mediaplayer/mpmusicplaybackstate/seekingbackward)

|  | Declaration |
| --- | --- |
| From | ``` case SeekingBackward ``` |
| To | ``` case seekingBackward ``` |

Modified [MPMusicPlaybackState.seekingForward](https://developer.apple.com/documentation/mediaplayer/mpmusicplaybackstate/mpmusicplaybackstateseekingforward)

|  | Declaration |
| --- | --- |
| From | ``` case SeekingForward ``` |
| To | ``` case seekingForward ``` |

Modified [MPMusicPlaybackState.stopped](https://developer.apple.com/documentation/mediaplayer/mpmusicplaybackstate/stopped)

|  | Declaration |
| --- | --- |
| From | ``` case Stopped ``` |
| To | ``` case stopped ``` |

Modified [MPMusicPlayerController](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMusicPlayerController : NSObject, MPMediaPlayback {     class func applicationMusicPlayer() -> MPMusicPlayerController     class func systemMusicPlayer() -> MPMusicPlayerController     class func iPodMusicPlayer() -> MPMusicPlayerController } extension MPMusicPlayerController {     var playbackState: MPMusicPlaybackState { get }     var repeatMode: MPMusicRepeatMode     var shuffleMode: MPMusicShuffleMode     var volume: Float     @NSCopying var nowPlayingItem: MPMediaItem?     var indexOfNowPlayingItem: Int { get }     func setQueueWithQuery(_ query: MPMediaQuery)     func setQueueWithItemCollection(_ itemCollection: MPMediaItemCollection)     func setQueueWithStoreIDs(_ storeIDs: [String])     func skipToNextItem()     func skipToBeginning()     func skipToPreviousItem()     func beginGeneratingPlaybackNotifications()     func endGeneratingPlaybackNotifications() } ``` | MPMediaPlayback |
| To | ``` class MPMusicPlayerController : NSObject, MPMediaPlayback {     class func applicationMusicPlayer() -> MPMusicPlayerController     class func systemMusicPlayer() -> MPMusicPlayerController     class func iPodMusicPlayer() -> MPMusicPlayerController     var playbackState: MPMusicPlaybackState { get }     var repeatMode: MPMusicRepeatMode     var shuffleMode: MPMusicShuffleMode     var volume: Float     @NSCopying var nowPlayingItem: MPMediaItem?     var indexOfNowPlayingItem: Int { get }     func setQueue(with query: MPMediaQuery)     func setQueue(with itemCollection: MPMediaItemCollection)     func setQueueWithStoreIDs(_ storeIDs: [String])     func skipToNextItem()     func skipToBeginning()     func skipToPreviousItem()     func beginGeneratingPlaybackNotifications()     func endGeneratingPlaybackNotifications()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPMusicPlayerController : CVarArg { } extension MPMusicPlayerController : Equatable, Hashable {     var hashValue: Int { get } } extension MPMusicPlayerController {     var playbackState: MPMusicPlaybackState { get }     var repeatMode: MPMusicRepeatMode     var shuffleMode: MPMusicShuffleMode     var volume: Float     @NSCopying var nowPlayingItem: MPMediaItem?     var indexOfNowPlayingItem: Int { get }     func setQueue(with query: MPMediaQuery)     func setQueue(with itemCollection: MPMediaItemCollection)     func setQueueWithStoreIDs(_ storeIDs: [String])     func skipToNextItem()     func skipToBeginning()     func skipToPreviousItem()     func beginGeneratingPlaybackNotifications()     func endGeneratingPlaybackNotifications() } ``` | CVarArg, Equatable, Hashable, MPMediaPlayback |

Modified [MPMusicPlayerController.setQueue(with: MPMediaItemCollection)](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624171-setqueuewithitemcollection)

|  | Declaration |
| --- | --- |
| From | ``` func setQueueWithItemCollection(_ itemCollection: MPMediaItemCollection) ``` |
| To | ``` func setQueue(with itemCollection: MPMediaItemCollection) ``` |

Modified [MPMusicPlayerController.setQueue(with: MPMediaQuery)](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624180-setqueue)

|  | Declaration |
| --- | --- |
| From | ``` func setQueueWithQuery(_ query: MPMediaQuery) ``` |
| To | ``` func setQueue(with query: MPMediaQuery) ``` |

Modified [MPMusicRepeatMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmusicrepeatmode)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMusicRepeatMode : Int {     case Default     case None     case One     case All } ``` |
| To | ``` enum MPMusicRepeatMode : Int {     case `default`     case none     case one     case all } ``` |

Modified [MPMusicRepeatMode.all](https://developer.apple.com/documentation/mediaplayer/mpmusicrepeatmode/all)

|  | Declaration |
| --- | --- |
| From | ``` case All ``` |
| To | ``` case all ``` |

Modified [MPMusicRepeatMode.default](https://developer.apple.com/documentation/mediaplayer/mpmusicrepeatmode/default)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [MPMusicRepeatMode.none](https://developer.apple.com/documentation/mediaplayer/mpmusicrepeatmode/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [MPMusicRepeatMode.one](https://developer.apple.com/documentation/mediaplayer/mpmusicrepeatmode/mpmusicrepeatmodeone)

|  | Declaration |
| --- | --- |
| From | ``` case One ``` |
| To | ``` case one ``` |

Modified [MPMusicShuffleMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmusicshufflemode)

|  | Declaration |
| --- | --- |
| From | ``` enum MPMusicShuffleMode : Int {     case Default     case Off     case Songs     case Albums } ``` |
| To | ``` enum MPMusicShuffleMode : Int {     case `default`     case off     case songs     case albums } ``` |

Modified [MPMusicShuffleMode.albums](https://developer.apple.com/documentation/mediaplayer/mpmusicshufflemode/mpmusicshufflemodealbums)

|  | Declaration |
| --- | --- |
| From | ``` case Albums ``` |
| To | ``` case albums ``` |

Modified [MPMusicShuffleMode.default](https://developer.apple.com/documentation/mediaplayer/mpmusicshufflemode/mpmusicshufflemodedefault)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [MPMusicShuffleMode.off](https://developer.apple.com/documentation/mediaplayer/mpmusicshufflemode/mpmusicshufflemodeoff)

|  | Declaration |
| --- | --- |
| From | ``` case Off ``` |
| To | ``` case off ``` |

Modified [MPMusicShuffleMode.songs](https://developer.apple.com/documentation/mediaplayer/mpmusicshufflemode/songs)

|  | Declaration |
| --- | --- |
| From | ``` case Songs ``` |
| To | ``` case songs ``` |

Modified [MPNowPlayingInfoCenter](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPNowPlayingInfoCenter : NSObject {     class func defaultCenter() -> MPNowPlayingInfoCenter     var nowPlayingInfo: [String : AnyObject]? } ``` | -- |
| To | ``` class MPNowPlayingInfoCenter : NSObject {     class func `default`() -> MPNowPlayingInfoCenter     var nowPlayingInfo: [String : Any]?     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPNowPlayingInfoCenter : CVarArg { } extension MPNowPlayingInfoCenter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPNowPlayingInfoCenter.default() [class]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/1615899-defaultcenter)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultCenter() -> MPNowPlayingInfoCenter ``` |
| To | ``` class func `default`() -> MPNowPlayingInfoCenter ``` |

Modified [MPNowPlayingInfoCenter.nowPlayingInfo](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/1615903-nowplayinginfo)

|  | Declaration |
| --- | --- |
| From | ``` var nowPlayingInfo: [String : AnyObject]? ``` |
| To | ``` var nowPlayingInfo: [String : Any]? ``` |

Modified [MPNowPlayingInfoLanguageOption](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPNowPlayingInfoLanguageOption : NSObject {     init(type languageOptionType: MPNowPlayingInfoLanguageOptionType, languageTag languageTag: String, characteristics languageOptionCharacteristics: [String]?, displayName displayName: String, identifier identifier: String)     func isAutomaticLegibleLanguageOption() -> Bool     func isAutomaticAudibleLanguageOption() -> Bool     var languageOptionType: MPNowPlayingInfoLanguageOptionType { get }     var languageTag: String? { get }     var languageOptionCharacteristics: [String]? { get }     var displayName: String? { get }     var identifier: String? { get } } ``` | -- |
| To | ``` class MPNowPlayingInfoLanguageOption : NSObject {     init(type languageOptionType: MPNowPlayingInfoLanguageOptionType, languageTag languageTag: String, characteristics languageOptionCharacteristics: [String]?, displayName displayName: String, identifier identifier: String)     func isAutomaticLegibleLanguageOption() -> Bool     func isAutomaticAudibleLanguageOption() -> Bool     var languageOptionType: MPNowPlayingInfoLanguageOptionType { get }     var languageTag: String? { get }     var languageOptionCharacteristics: [String]? { get }     var displayName: String? { get }     var identifier: String? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPNowPlayingInfoLanguageOption : CVarArg { } extension MPNowPlayingInfoLanguageOption : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPNowPlayingInfoLanguageOptionGroup](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPNowPlayingInfoLanguageOptionGroup : NSObject {     init(languageOptions languageOptions: [MPNowPlayingInfoLanguageOption], defaultLanguageOption defaultLanguageOption: MPNowPlayingInfoLanguageOption?, allowEmptySelection allowEmptySelection: Bool)     var languageOptions: [MPNowPlayingInfoLanguageOption] { get }     var defaultLanguageOption: MPNowPlayingInfoLanguageOption? { get }     var allowEmptySelection: Bool { get } } ``` | -- |
| To | ``` class MPNowPlayingInfoLanguageOptionGroup : NSObject {     init(languageOptions languageOptions: [MPNowPlayingInfoLanguageOption], defaultLanguageOption defaultLanguageOption: MPNowPlayingInfoLanguageOption?, allowEmptySelection allowEmptySelection: Bool)     var languageOptions: [MPNowPlayingInfoLanguageOption] { get }     var defaultLanguageOption: MPNowPlayingInfoLanguageOption? { get }     var allowEmptySelection: Bool { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPNowPlayingInfoLanguageOptionGroup : CVarArg { } extension MPNowPlayingInfoLanguageOptionGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPNowPlayingInfoLanguageOptionType [enum]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype)

|  | Declaration |
| --- | --- |
| From | ``` enum MPNowPlayingInfoLanguageOptionType : UInt {     case Audible     case Legible } ``` |
| To | ``` enum MPNowPlayingInfoLanguageOptionType : UInt {     case audible     case legible } ``` |

Modified [MPNowPlayingInfoLanguageOptionType.audible](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype/mpnowplayinginfolanguageoptiontypeaudible)

|  | Declaration |
| --- | --- |
| From | ``` case Audible ``` |
| To | ``` case audible ``` |

Modified [MPNowPlayingInfoLanguageOptionType.legible](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype/mpnowplayinginfolanguageoptiontypelegible)

|  | Declaration |
| --- | --- |
| From | ``` case Legible ``` |
| To | ``` case legible ``` |

Modified [MPPlayableContentDataSource](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource)

|  | Declaration |
| --- | --- |
| From | ``` protocol MPPlayableContentDataSource : NSObjectProtocol {     optional func beginLoadingChildItemsAtIndexPath(_ indexPath: NSIndexPath, completionHandler completionHandler: (NSError?) -> Void)     optional func childItemsDisplayPlaybackProgressAtIndexPath(_ indexPath: NSIndexPath) -> Bool     func numberOfChildItemsAtIndexPath(_ indexPath: NSIndexPath) -> Int     func contentItemAtIndexPath(_ indexPath: NSIndexPath) -> MPContentItem? } ``` |
| To | ``` protocol MPPlayableContentDataSource : NSObjectProtocol {     optional func beginLoadingChildItems(at indexPath: IndexPath, completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     optional func childItemsDisplayPlaybackProgress(at indexPath: IndexPath) -> Bool     optional func contentItem(forIdentifier identifier: String, completionHandler completionHandler: @escaping (MPContentItem?, Error?) -> Swift.Void)     func numberOfChildItems(at indexPath: IndexPath) -> Int     func contentItem(at indexPath: IndexPath) -> MPContentItem? } ``` |

Modified [MPPlayableContentDataSource.beginLoadingChildItems(at: IndexPath, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619508-beginloadingchilditems)

|  | Declaration |
| --- | --- |
| From | ``` optional func beginLoadingChildItemsAtIndexPath(_ indexPath: NSIndexPath, completionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` optional func beginLoadingChildItems(at indexPath: IndexPath, completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [MPPlayableContentDataSource.childItemsDisplayPlaybackProgress(at: IndexPath) -> Bool](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619509-childitemsdisplayplaybackprogres)

|  | Declaration |
| --- | --- |
| From | ``` optional func childItemsDisplayPlaybackProgressAtIndexPath(_ indexPath: NSIndexPath) -> Bool ``` |
| To | ``` optional func childItemsDisplayPlaybackProgress(at indexPath: IndexPath) -> Bool ``` |

Modified [MPPlayableContentDataSource.contentItem(at: IndexPath) -> MPContentItem?](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619505-contentitematindexpath)

|  | Declaration |
| --- | --- |
| From | ``` func contentItemAtIndexPath(_ indexPath: NSIndexPath) -> MPContentItem? ``` |
| To | ``` func contentItem(at indexPath: IndexPath) -> MPContentItem? ``` |

Modified [MPPlayableContentDataSource.numberOfChildItems(at: IndexPath) -> Int](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619506-numberofchilditems)

|  | Declaration |
| --- | --- |
| From | ``` func numberOfChildItemsAtIndexPath(_ indexPath: NSIndexPath) -> Int ``` |
| To | ``` func numberOfChildItems(at indexPath: IndexPath) -> Int ``` |

Modified [MPPlayableContentDelegate](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MPPlayableContentDelegate : NSObjectProtocol {     optional func playableContentManager(_ contentManager: MPPlayableContentManager, initiatePlaybackOfContentItemAtIndexPath indexPath: NSIndexPath, completionHandler completionHandler: (NSError?) -> Void)     optional func playableContentManager(_ contentManager: MPPlayableContentManager, initializePlaybackQueueWithCompletionHandler completionHandler: (NSError?) -> Void)     optional func playableContentManager(_ contentManager: MPPlayableContentManager, didUpdateContext context: MPPlayableContentManagerContext) } ``` |
| To | ``` protocol MPPlayableContentDelegate : NSObjectProtocol {     optional func playableContentManager(_ contentManager: MPPlayableContentManager, initiatePlaybackOfContentItemAt indexPath: IndexPath, completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     optional func playableContentManager(_ contentManager: MPPlayableContentManager, initializePlaybackQueueWithCompletionHandler completionHandler: @escaping (Error?) -> Swift.Void)     optional func playableContentManager(_ contentManager: MPPlayableContentManager, initializePlaybackQueueWithContentItems contentItems: [Any]?, completionHandler completionHandler: @escaping (Error?) -> Swift.Void)     optional func playableContentManager(_ contentManager: MPPlayableContentManager, didUpdate context: MPPlayableContentManagerContext) } ``` |

Modified [MPPlayableContentDelegate.playableContentManager(_: MPPlayableContentManager, didUpdate: MPPlayableContentManagerContext)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620291-playablecontentmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func playableContentManager(_ contentManager: MPPlayableContentManager, didUpdateContext context: MPPlayableContentManagerContext) ``` |
| To | ``` optional func playableContentManager(_ contentManager: MPPlayableContentManager, didUpdate context: MPPlayableContentManagerContext) ``` |

Modified [MPPlayableContentDelegate.playableContentManager(_: MPPlayableContentManager, initializePlaybackQueueWithCompletionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620294-playablecontentmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func playableContentManager(_ contentManager: MPPlayableContentManager, initializePlaybackQueueWithCompletionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` optional func playableContentManager(_ contentManager: MPPlayableContentManager, initializePlaybackQueueWithCompletionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [MPPlayableContentDelegate.playableContentManager(_: MPPlayableContentManager, initiatePlaybackOfContentItemAt: IndexPath, completionHandler: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620292-playablecontentmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func playableContentManager(_ contentManager: MPPlayableContentManager, initiatePlaybackOfContentItemAtIndexPath indexPath: NSIndexPath, completionHandler completionHandler: (NSError?) -> Void) ``` |
| To | ``` optional func playableContentManager(_ contentManager: MPPlayableContentManager, initiatePlaybackOfContentItemAt indexPath: IndexPath, completionHandler completionHandler: @escaping (Error?) -> Swift.Void) ``` |

Modified [MPPlayableContentManager](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPPlayableContentManager : NSObject {     weak var dataSource: MPPlayableContentDataSource?     weak var delegate: MPPlayableContentDelegate?     var context: MPPlayableContentManagerContext { get }     class func sharedContentManager() -> Self     func reloadData()     func beginUpdates()     func endUpdates() } ``` | -- |
| To | ``` class MPPlayableContentManager : NSObject {     weak var dataSource: MPPlayableContentDataSource?     weak var delegate: MPPlayableContentDelegate?     var context: MPPlayableContentManagerContext { get }     var nowPlayingIdentifiers: [String]     class func shared() -> Self     func reloadData()     func beginUpdates()     func endUpdates()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPPlayableContentManager : CVarArg { } extension MPPlayableContentManager : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPPlayableContentManager.shared() -> Self [class]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614806-sharedcontentmanager)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedContentManager() -> Self ``` |
| To | ``` class func shared() -> Self ``` |

Modified [MPPlayableContentManagerContext](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPPlayableContentManagerContext : NSObject {     var enforcedContentItemsCount: Int { get }     var enforcedContentTreeDepth: Int { get }     var contentLimitsEnforced: Bool { get }     var contentLimitsEnabled: Bool { get }     var endpointAvailable: Bool { get } } ``` | -- |
| To | ``` class MPPlayableContentManagerContext : NSObject {     var enforcedContentItemsCount: Int { get }     var enforcedContentTreeDepth: Int { get }     var contentLimitsEnforced: Bool { get }     var contentLimitsEnabled: Bool { get }     var endpointAvailable: Bool { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPPlayableContentManagerContext : CVarArg { } extension MPPlayableContentManagerContext : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPRemoteCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommand)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPRemoteCommand : NSObject {     var enabled: Bool     func addTarget(_ target: AnyObject, action action: Selector)     func removeTarget(_ target: AnyObject, action action: Selector)     func removeTarget(_ target: AnyObject?)     func addTargetWithHandler(_ handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> AnyObject } ``` | -- |
| To | ``` class MPRemoteCommand : NSObject {     var isEnabled: Bool     func addTarget(_ target: Any, action action: Selector)     func removeTarget(_ target: Any, action action: Selector?)     func removeTarget(_ target: Any?)     func addTarget(handler handler: @escaping (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any     init()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPRemoteCommand : CVarArg { } extension MPRemoteCommand : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPRemoteCommand.addTarget(_: Any, action: Selector)](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622895-addtarget)

|  | Declaration |
| --- | --- |
| From | ``` func addTarget(_ target: AnyObject, action action: Selector) ``` |
| To | ``` func addTarget(_ target: Any, action action: Selector) ``` |

Modified [MPRemoteCommand.addTarget(handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622910-addtarget)

|  | Declaration |
| --- | --- |
| From | ``` func addTargetWithHandler(_ handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> AnyObject ``` |
| To | ``` func addTarget(handler handler: @escaping (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> Any ``` |

Modified [MPRemoteCommand.isEnabled](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622908-enabled)

|  | Declaration |
| --- | --- |
| From | ``` var enabled: Bool ``` |
| To | ``` var isEnabled: Bool ``` |

Modified [MPRemoteCommand.removeTarget(_: Any?)](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622903-removetarget)

|  | Declaration |
| --- | --- |
| From | ``` func removeTarget(_ target: AnyObject?) ``` |
| To | ``` func removeTarget(_ target: Any?) ``` |

Modified [MPRemoteCommand.removeTarget(_: Any, action: Selector?)](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622896-removetarget)

|  | Declaration |
| --- | --- |
| From | ``` func removeTarget(_ target: AnyObject, action action: Selector) ``` |
| To | ``` func removeTarget(_ target: Any, action action: Selector?) ``` |

Modified [MPRemoteCommandCenter](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPRemoteCommandCenter : NSObject {     var pauseCommand: MPRemoteCommand { get }     var playCommand: MPRemoteCommand { get }     var stopCommand: MPRemoteCommand { get }     var togglePlayPauseCommand: MPRemoteCommand { get }     var enableLanguageOptionCommand: MPRemoteCommand { get }     var disableLanguageOptionCommand: MPRemoteCommand { get }     var nextTrackCommand: MPRemoteCommand { get }     var previousTrackCommand: MPRemoteCommand { get }     var skipForwardCommand: MPSkipIntervalCommand { get }     var skipBackwardCommand: MPSkipIntervalCommand { get }     var seekForwardCommand: MPRemoteCommand { get }     var seekBackwardCommand: MPRemoteCommand { get }     var ratingCommand: MPRatingCommand { get }     var changePlaybackRateCommand: MPChangePlaybackRateCommand { get }     var likeCommand: MPFeedbackCommand { get }     var dislikeCommand: MPFeedbackCommand { get }     var bookmarkCommand: MPFeedbackCommand { get }     var changePlaybackPositionCommand: MPChangePlaybackPositionCommand { get }     class func sharedCommandCenter() -> MPRemoteCommandCenter } ``` | -- |
| To | ``` class MPRemoteCommandCenter : NSObject {     var pauseCommand: MPRemoteCommand { get }     var playCommand: MPRemoteCommand { get }     var stopCommand: MPRemoteCommand { get }     var togglePlayPauseCommand: MPRemoteCommand { get }     var enableLanguageOptionCommand: MPRemoteCommand { get }     var disableLanguageOptionCommand: MPRemoteCommand { get }     var changePlaybackRateCommand: MPChangePlaybackRateCommand { get }     var changeRepeatModeCommand: MPChangeRepeatModeCommand { get }     var changeShuffleModeCommand: MPChangeShuffleModeCommand { get }     var nextTrackCommand: MPRemoteCommand { get }     var previousTrackCommand: MPRemoteCommand { get }     var skipForwardCommand: MPSkipIntervalCommand { get }     var skipBackwardCommand: MPSkipIntervalCommand { get }     var seekForwardCommand: MPRemoteCommand { get }     var seekBackwardCommand: MPRemoteCommand { get }     var changePlaybackPositionCommand: MPChangePlaybackPositionCommand { get }     var ratingCommand: MPRatingCommand { get }     var likeCommand: MPFeedbackCommand { get }     var dislikeCommand: MPFeedbackCommand { get }     var bookmarkCommand: MPFeedbackCommand { get }     class func shared() -> MPRemoteCommandCenter     init()     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPRemoteCommandCenter : CVarArg { } extension MPRemoteCommandCenter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPRemoteCommandCenter.shared() -> MPRemoteCommandCenter [class]](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618994-sharedcommandcenter)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedCommandCenter() -> MPRemoteCommandCenter ``` |
| To | ``` class func shared() -> MPRemoteCommandCenter ``` |

Modified [MPRemoteCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpremotecommandevent)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPRemoteCommandEvent : NSObject {     var command: MPRemoteCommand { get }     var timestamp: NSTimeInterval { get } } ``` | -- |
| To | ``` class MPRemoteCommandEvent : NSObject {     var command: MPRemoteCommand { get }     var timestamp: TimeInterval { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPRemoteCommandEvent : CVarArg { } extension MPRemoteCommandEvent : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPRemoteCommandEvent.timestamp](https://developer.apple.com/documentation/mediaplayer/mpremotecommandevent/1616784-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` var timestamp: NSTimeInterval { get } ``` |
| To | ``` var timestamp: TimeInterval { get } ``` |

Modified [MPRemoteCommandHandlerStatus [enum]](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum MPRemoteCommandHandlerStatus : Int {     case Success     case NoSuchContent     case NoActionableNowPlayingItem     case CommandFailed } ``` |
| To | ``` enum MPRemoteCommandHandlerStatus : Int {     case success     case noSuchContent     case noActionableNowPlayingItem     case commandFailed } ``` |

Modified [MPRemoteCommandHandlerStatus.commandFailed](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus/commandfailed)

|  | Declaration |
| --- | --- |
| From | ``` case CommandFailed ``` |
| To | ``` case commandFailed ``` |

Modified [MPRemoteCommandHandlerStatus.noActionableNowPlayingItem](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus/mpremotecommandhandlerstatusnoactionablenowplayingitem)

|  | Declaration |
| --- | --- |
| From | ``` case NoActionableNowPlayingItem ``` |
| To | ``` case noActionableNowPlayingItem ``` |

Modified [MPRemoteCommandHandlerStatus.noSuchContent](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus/mpremotecommandhandlerstatusnosuchcontent)

|  | Declaration |
| --- | --- |
| From | ``` case NoSuchContent ``` |
| To | ``` case noSuchContent ``` |

Modified [MPRemoteCommandHandlerStatus.success](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus/success)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [MPSeekCommandEventType [enum]](https://developer.apple.com/documentation/mediaplayer/mpseekcommandeventtype)

|  | Declaration |
| --- | --- |
| From | ``` enum MPSeekCommandEventType : UInt {     case BeginSeeking     case EndSeeking } ``` |
| To | ``` enum MPSeekCommandEventType : UInt {     case beginSeeking     case endSeeking } ``` |

Modified [MPSeekCommandEventType.beginSeeking](https://developer.apple.com/documentation/mediaplayer/mpseekcommandeventtype/mpseekcommandeventtypebeginseeking)

|  | Declaration |
| --- | --- |
| From | ``` case BeginSeeking ``` |
| To | ``` case beginSeeking ``` |

Modified [MPSeekCommandEventType.endSeeking](https://developer.apple.com/documentation/mediaplayer/mpseekcommandeventtype/endseeking)

|  | Declaration |
| --- | --- |
| From | ``` case EndSeeking ``` |
| To | ``` case endSeeking ``` |

Modified [MPSkipIntervalCommand](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommand)

|  | Declaration |
| --- | --- |
| From | ``` class MPSkipIntervalCommand : MPRemoteCommand {     var preferredIntervals: [AnyObject] } ``` |
| To | ``` class MPSkipIntervalCommand : MPRemoteCommand {     var preferredIntervals: [NSNumber] } ``` |

Modified [MPSkipIntervalCommand.preferredIntervals](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommand/1622899-preferredintervals)

|  | Declaration |
| --- | --- |
| From | ``` var preferredIntervals: [AnyObject] ``` |
| To | ``` var preferredIntervals: [NSNumber] ``` |

Modified [MPSkipIntervalCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommandevent)

|  | Declaration |
| --- | --- |
| From | ``` class MPSkipIntervalCommandEvent : MPRemoteCommandEvent {     var interval: NSTimeInterval { get } } ``` |
| To | ``` class MPSkipIntervalCommandEvent : MPRemoteCommandEvent {     var interval: TimeInterval { get } } ``` |

Modified [MPSkipIntervalCommandEvent.interval](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommandevent/1616767-interval)

|  | Declaration |
| --- | --- |
| From | ``` var interval: NSTimeInterval { get } ``` |
| To | ``` var interval: TimeInterval { get } ``` |

Modified [MPTimedMetadata](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPTimedMetadata : NSObject {     var key: String! { get }     var keyspace: String! { get }     var value: AnyObject! { get }     var timestamp: NSTimeInterval { get }     var allMetadata: [NSObject : AnyObject]! { get } } ``` | -- |
| To | ``` class MPTimedMetadata : NSObject {     var key: String! { get }     var keyspace: String! { get }     var value: Any! { get }     var timestamp: TimeInterval { get }     var allMetadata: [AnyHashable : Any]! { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPTimedMetadata : CVarArg { } extension MPTimedMetadata : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MPTimedMetadata.allMetadata](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/1620856-allmetadata)

|  | Declaration |
| --- | --- |
| From | ``` var allMetadata: [NSObject : AnyObject]! { get } ``` |
| To | ``` var allMetadata: [AnyHashable : Any]! { get } ``` |

Modified [MPTimedMetadata.timestamp](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/1620918-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` var timestamp: NSTimeInterval { get } ``` |
| To | ``` var timestamp: TimeInterval { get } ``` |

Modified [MPTimedMetadata.value](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/1620866-value)

|  | Declaration |
| --- | --- |
| From | ``` var value: AnyObject! { get } ``` |
| To | ``` var value: Any! { get } ``` |

Modified [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPVolumeView : UIView, NSCoding {     var showsVolumeSlider: Bool     var showsRouteButton: Bool     var wirelessRoutesAvailable: Bool { get }     var wirelessRouteActive: Bool { get }     func setMinimumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState)     func setMaximumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState)     func setVolumeThumbImage(_ image: UIImage?, forState state: UIControlState)     func minimumVolumeSliderImageForState(_ state: UIControlState) -> UIImage?     func maximumVolumeSliderImageForState(_ state: UIControlState) -> UIImage?     func volumeThumbImageForState(_ state: UIControlState) -> UIImage?     var volumeWarningSliderImage: UIImage?     func volumeSliderRectForBounds(_ bounds: CGRect) -> CGRect     func volumeThumbRectForBounds(_ bounds: CGRect, volumeSliderRect rect: CGRect, value value: Float) -> CGRect     func setRouteButtonImage(_ image: UIImage?, forState state: UIControlState)     func routeButtonImageForState(_ state: UIControlState) -> UIImage?     func routeButtonRectForBounds(_ bounds: CGRect) -> CGRect } ``` | NSCoding |
| To | ``` class MPVolumeView : UIView, NSCoding {     var showsVolumeSlider: Bool     var showsRouteButton: Bool     var areWirelessRoutesAvailable: Bool { get }     var isWirelessRouteActive: Bool { get }     func setMinimumVolumeSliderImage(_ image: UIImage?, for state: UIControlState)     func setMaximumVolumeSliderImage(_ image: UIImage?, for state: UIControlState)     func setVolumeThumbImage(_ image: UIImage?, for state: UIControlState)     func minimumVolumeSliderImage(for state: UIControlState) -> UIImage?     func maximumVolumeSliderImage(for state: UIControlState) -> UIImage?     func volumeThumbImage(for state: UIControlState) -> UIImage?     var volumeWarningSliderImage: UIImage?     func volumeSliderRect(forBounds bounds: CGRect) -> CGRect     func volumeThumbRect(forBounds bounds: CGRect, volumeSliderRect rect: CGRect, value value: Float) -> CGRect     func setRouteButtonImage(_ image: UIImage?, for state: UIControlState)     func routeButtonImage(for state: UIControlState) -> UIImage?     func routeButtonRect(forBounds bounds: CGRect) -> CGRect     func viewPrintFormatter() -> UIViewPrintFormatter     func draw(_ rect: CGRect, for formatter: UIViewPrintFormatter)     func endEditing(_ force: Bool) -> Bool     func snapshotView(afterScreenUpdates afterUpdates: Bool) -> UIView?     func resizableSnapshotView(from rect: CGRect, afterScreenUpdates afterUpdates: Bool, withCapInsets capInsets: UIEdgeInsets) -> UIView?     func drawHierarchy(in rect: CGRect, afterScreenUpdates afterUpdates: Bool) -> Bool     var restorationIdentifier: String?     func encodeRestorableState(with coder: NSCoder)     func decodeRestorableState(with coder: NSCoder)     func constraintsAffectingLayout(for axis: UILayoutConstraintAxis) -> [NSLayoutConstraint]     var hasAmbiguousLayout: Bool { get }     func exerciseAmbiguityInLayout()     var leadingAnchor: NSLayoutXAxisAnchor { get }     var trailingAnchor: NSLayoutXAxisAnchor { get }     var leftAnchor: NSLayoutXAxisAnchor { get }     var rightAnchor: NSLayoutXAxisAnchor { get }     var topAnchor: NSLayoutYAxisAnchor { get }     var bottomAnchor: NSLayoutYAxisAnchor { get }     var widthAnchor: NSLayoutDimension { get }     var heightAnchor: NSLayoutDimension { get }     var centerXAnchor: NSLayoutXAxisAnchor { get }     var centerYAnchor: NSLayoutYAxisAnchor { get }     var firstBaselineAnchor: NSLayoutYAxisAnchor { get }     var lastBaselineAnchor: NSLayoutYAxisAnchor { get }     var layoutGuides: [UILayoutGuide] { get }     func addLayoutGuide(_ layoutGuide: UILayoutGuide)     func removeLayoutGuide(_ layoutGuide: UILayoutGuide)     func systemLayoutSizeFitting(_ targetSize: CGSize) -> CGSize     func systemLayoutSizeFitting(_ targetSize: CGSize, withHorizontalFittingPriority horizontalFittingPriority: UILayoutPriority, verticalFittingPriority verticalFittingPriority: UILayoutPriority) -> CGSize     func alignmentRect(forFrame frame: CGRect) -> CGRect     func frame(forAlignmentRect alignmentRect: CGRect) -> CGRect     var alignmentRectInsets: UIEdgeInsets { get }     func forBaselineLayout() -> UIView     var forFirstBaselineLayout: UIView { get }     var forLastBaselineLayout: UIView { get }     var intrinsicContentSize: CGSize { get }     func invalidateIntrinsicContentSize()     func contentHuggingPriority(for axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentHuggingPriority(_ priority: UILayoutPriority, for axis: UILayoutConstraintAxis)     func contentCompressionResistancePriority(for axis: UILayoutConstraintAxis) -> UILayoutPriority     func setContentCompressionResistancePriority(_ priority: UILayoutPriority, for axis: UILayoutConstraintAxis)     var translatesAutoresizingMaskIntoConstraints: Bool     class var requiresConstraintBasedLayout: Bool { get }     func updateConstraintsIfNeeded()     func updateConstraints()     func needsUpdateConstraints() -> Bool     func setNeedsUpdateConstraints()     var constraints: [NSLayoutConstraint] { get }     func addConstraint(_ constraint: NSLayoutConstraint)     func addConstraints(_ constraints: [NSLayoutConstraint])     func removeConstraint(_ constraint: NSLayoutConstraint)     func removeConstraints(_ constraints: [NSLayoutConstraint])     func addMotionEffect(_ effect: UIMotionEffect)     func removeMotionEffect(_ effect: UIMotionEffect)     var motionEffects: [UIMotionEffect]     var gestureRecognizers: [UIGestureRecognizer]?     func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)     func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool     class func animateKeyframes(withDuration duration: TimeInterval, delay delay: TimeInterval, options options: UIViewKeyframeAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func addKeyframe(withRelativeStartTime frameStartTime: Double, relativeDuration frameDuration: Double, animations animations: @escaping () -> Void)     class func animate(withDuration duration: TimeInterval, delay delay: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Void)     class func animate(withDuration duration: TimeInterval, delay delay: TimeInterval, usingSpringWithDamping dampingRatio: CGFloat, initialSpringVelocity velocity: CGFloat, options options: UIViewAnimationOptions = [], animations animations: @escaping () -> Void, completion completion: (@escaping (Bool) -> Void)? = nil)     class func transition(with view: UIView, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], animations animations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     class func transition(from fromView: UIView, to toView: UIView, duration duration: TimeInterval, options options: UIViewAnimationOptions = [], completion completion: (@escaping (Bool) -> Void)? = nil)     class func perform(_ animation: UISystemAnimation, on views: [UIView], options options: UIViewAnimationOptions = [], animations parallelAnimations: (@escaping () -> Void)?, completion completion: (@escaping (Bool) -> Void)? = nil)     class func beginAnimations(_ animationID: String?, context context: UnsafeMutableRawPointer?)     class func commitAnimations()     class func setAnimationDelegate(_ delegate: Any?)     class func setAnimationWillStart(_ selector: Selector?)     class func setAnimationDidStop(_ selector: Selector?)     class func setAnimationDuration(_ duration: TimeInterval)     class func setAnimationDelay(_ delay: TimeInterval)     class func setAnimationStart(_ startDate: Date)     class func setAnimationCurve(_ curve: UIViewAnimationCurve)     class func setAnimationRepeatCount(_ repeatCount: Float)     class func setAnimationRepeatAutoreverses(_ repeatAutoreverses: Bool)     class func setAnimationBeginsFromCurrentState(_ fromCurrentState: Bool)     class func setAnimationTransition(_ transition: UIViewAnimationTransition, for view: UIView, cache cache: Bool)     class func setAnimationsEnabled(_ enabled: Bool)     class var areAnimationsEnabled: Bool { get }     class func performWithoutAnimation(_ actionsWithoutAnimation: () -> Void)     class var inheritedAnimationDuration: TimeInterval { get }     func draw(_ rect: CGRect)     func setNeedsDisplay()     func setNeedsDisplay(_ rect: CGRect)     var clipsToBounds: Bool     @NSCopying var backgroundColor: UIColor?     var alpha: CGFloat     var isOpaque: Bool     var clearsContextBeforeDrawing: Bool     var isHidden: Bool     var contentMode: UIViewContentMode     var contentStretch: CGRect     var mask: UIView?     var tintColor: UIColor!     var tintAdjustmentMode: UIViewTintAdjustmentMode     func tintColorDidChange()     var superview: UIView? { get }     var subviews: [UIView] { get }     var window: UIWindow? { get }     func removeFromSuperview()     func insertSubview(_ view: UIView, at index: Int)     func exchangeSubview(at index1: Int, withSubviewAt index2: Int)     func addSubview(_ view: UIView)     func insertSubview(_ view: UIView, belowSubview siblingSubview: UIView)     func insertSubview(_ view: UIView, aboveSubview siblingSubview: UIView)     func bringSubview(toFront view: UIView)     func sendSubview(toBack view: UIView)     func didAddSubview(_ subview: UIView)     func willRemoveSubview(_ subview: UIView)     func willMove(toSuperview newSuperview: UIView?)     func didMoveToSuperview()     func willMove(toWindow newWindow: UIWindow?)     func didMoveToWindow()     func isDescendant(of view: UIView) -> Bool     func viewWithTag(_ tag: Int) -> UIView?     func setNeedsLayout()     func layoutIfNeeded()     func layoutSubviews()     var layoutMargins: UIEdgeInsets     var preservesSuperviewLayoutMargins: Bool     func layoutMarginsDidChange()     var layoutMarginsGuide: UILayoutGuide { get }     var readableContentGuide: UILayoutGuide { get }     var frame: CGRect     var bounds: CGRect     var center: CGPoint     var transform: CGAffineTransform     var contentScaleFactor: CGFloat     var isMultipleTouchEnabled: Bool     var isExclusiveTouch: Bool     func hitTest(_ point: CGPoint, with event: UIEvent?) -> UIView?     func point(inside point: CGPoint, with event: UIEvent?) -> Bool     func convert(_ point: CGPoint, to view: UIView?) -> CGPoint     func convert(_ point: CGPoint, from view: UIView?) -> CGPoint     func convert(_ rect: CGRect, to view: UIView?) -> CGRect     func convert(_ rect: CGRect, from view: UIView?) -> CGRect     var autoresizesSubviews: Bool     var autoresizingMask: UIViewAutoresizing     func sizeThatFits(_ size: CGSize) -> CGSize     func sizeToFit()     var userActivity: NSUserActivity?     func updateUserActivityState(_ activity: NSUserActivity)     func restoreUserActivityState(_ activity: NSUserActivity)     var inputView: UIView? { get }     var inputAccessoryView: UIView? { get }     var inputAssistantItem: UITextInputAssistantItem { get }     var inputViewController: UIInputViewController? { get }     var inputAccessoryViewController: UIInputViewController? { get }     var textInputMode: UITextInputMode? { get }     var textInputContextIdentifier: String? { get }     class func clearTextInputContextIdentifier(_ identifier: String)     func reloadInputViews()     var keyCommands: [UIKeyCommand]? { get }     func awakeFromNib()     func prepareForInterfaceBuilder()     func accessibilityActivate() -> Bool     func accessibilityIncrement()     func accessibilityDecrement()     func accessibilityScroll(_ direction: UIAccessibilityScrollDirection) -> Bool     func accessibilityPerformEscape() -> Bool     func accessibilityPerformMagicTap() -> Bool     var accessibilityCustomActions: [UIAccessibilityCustomAction]?     func accessibilityElementDidBecomeFocused()     func accessibilityElementDidLoseFocus()     func accessibilityElementIsFocused() -> Bool     func accessibilityAssistiveTechnologyFocusedIdentifiers() -> Set<String>?     func accessibilityElementCount() -> Int     func accessibilityElement(at index: Int) -> Any?     func index(ofAccessibilityElement element: Any) -> Int     var accessibilityElements: [Any]?     var isAccessibilityElement: Bool     var accessibilityLabel: String?     var accessibilityHint: String?     var accessibilityValue: String?     var accessibilityTraits: UIAccessibilityTraits     var accessibilityFrame: CGRect     @NSCopying var accessibilityPath: UIBezierPath?     var accessibilityActivationPoint: CGPoint     var accessibilityLanguage: String?     var accessibilityElementsHidden: Bool     var accessibilityViewIsModal: Bool     var shouldGroupAccessibilityChildren: Bool     var accessibilityNavigationStyle: UIAccessibilityNavigationStyle     var accessibilityHeaderElements: [Any]?     var accessibilityCustomRotors: [UIAccessibilityCustomRotor]?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any?     func provideImageData(_ data: UnsafeMutableRawPointer, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: Any?) } extension MPVolumeView : UIAccessibilityIdentification { } extension MPVolumeView : CVarArg { } extension MPVolumeView : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCoding, UIAccessibilityIdentification |

Modified [MPVolumeView.areWirelessRoutesAvailable](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620073-wirelessroutesavailable)

|  | Declaration |
| --- | --- |
| From | ``` var wirelessRoutesAvailable: Bool { get } ``` |
| To | ``` var areWirelessRoutesAvailable: Bool { get } ``` |

Modified [MPVolumeView.isWirelessRouteActive](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620071-wirelessrouteactive)

|  | Declaration |
| --- | --- |
| From | ``` var wirelessRouteActive: Bool { get } ``` |
| To | ``` var isWirelessRouteActive: Bool { get } ``` |

Modified [MPVolumeView.maximumVolumeSliderImage(for: UIControlState) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620072-maximumvolumesliderimage)

|  | Declaration |
| --- | --- |
| From | ``` func maximumVolumeSliderImageForState(_ state: UIControlState) -> UIImage? ``` |
| To | ``` func maximumVolumeSliderImage(for state: UIControlState) -> UIImage? ``` |

Modified [MPVolumeView.minimumVolumeSliderImage(for: UIControlState) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620076-minimumvolumesliderimage)

|  | Declaration |
| --- | --- |
| From | ``` func minimumVolumeSliderImageForState(_ state: UIControlState) -> UIImage? ``` |
| To | ``` func minimumVolumeSliderImage(for state: UIControlState) -> UIImage? ``` |

Modified [MPVolumeView.routeButtonImage(for: UIControlState) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620078-routebuttonimageforstate)

|  | Declaration |
| --- | --- |
| From | ``` func routeButtonImageForState(_ state: UIControlState) -> UIImage? ``` |
| To | ``` func routeButtonImage(for state: UIControlState) -> UIImage? ``` |

Modified [MPVolumeView.routeButtonRect(forBounds: CGRect) -> CGRect](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620077-routebuttonrectforbounds)

|  | Declaration |
| --- | --- |
| From | ``` func routeButtonRectForBounds(_ bounds: CGRect) -> CGRect ``` |
| To | ``` func routeButtonRect(forBounds bounds: CGRect) -> CGRect ``` |

Modified [MPVolumeView.setMaximumVolumeSliderImage(_: UIImage?, for: UIControlState)](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620074-setmaximumvolumesliderimage)

|  | Declaration |
| --- | --- |
| From | ``` func setMaximumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState) ``` |
| To | ``` func setMaximumVolumeSliderImage(_ image: UIImage?, for state: UIControlState) ``` |

Modified [MPVolumeView.setMinimumVolumeSliderImage(_: UIImage?, for: UIControlState)](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620063-setminimumvolumesliderimage)

|  | Declaration |
| --- | --- |
| From | ``` func setMinimumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState) ``` |
| To | ``` func setMinimumVolumeSliderImage(_ image: UIImage?, for state: UIControlState) ``` |

Modified [MPVolumeView.setRouteButtonImage(_: UIImage?, for: UIControlState)](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620069-setroutebuttonimage)

|  | Declaration |
| --- | --- |
| From | ``` func setRouteButtonImage(_ image: UIImage?, forState state: UIControlState) ``` |
| To | ``` func setRouteButtonImage(_ image: UIImage?, for state: UIControlState) ``` |

Modified [MPVolumeView.setVolumeThumbImage(_: UIImage?, for: UIControlState)](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620062-setvolumethumbimage)

|  | Declaration |
| --- | --- |
| From | ``` func setVolumeThumbImage(_ image: UIImage?, forState state: UIControlState) ``` |
| To | ``` func setVolumeThumbImage(_ image: UIImage?, for state: UIControlState) ``` |

Modified [MPVolumeView.volumeSliderRect(forBounds: CGRect) -> CGRect](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620080-volumesliderrectforbounds)

|  | Declaration |
| --- | --- |
| From | ``` func volumeSliderRectForBounds(_ bounds: CGRect) -> CGRect ``` |
| To | ``` func volumeSliderRect(forBounds bounds: CGRect) -> CGRect ``` |

Modified [MPVolumeView.volumeThumbImage(for: UIControlState) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620064-volumethumbimageforstate)

|  | Declaration |
| --- | --- |
| From | ``` func volumeThumbImageForState(_ state: UIControlState) -> UIImage? ``` |
| To | ``` func volumeThumbImage(for state: UIControlState) -> UIImage? ``` |

Modified [MPVolumeView.volumeThumbRect(forBounds: CGRect, volumeSliderRect: CGRect, value: Float) -> CGRect](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620067-volumethumbrectforbounds)

|  | Declaration |
| --- | --- |
| From | ``` func volumeThumbRectForBounds(_ bounds: CGRect, volumeSliderRect rect: CGRect, value value: Float) -> CGRect ``` |
| To | ``` func volumeThumbRect(forBounds bounds: CGRect, volumeSliderRect rect: CGRect, value value: Float) -> CGRect ``` |

Modified [NSNotification.Name.MPMediaLibraryDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1621283-mpmedialibrarydidchange)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMediaLibraryDidChangeNotification | ``` let MPMediaLibraryDidChangeNotification: String ``` |
| To | MPMediaLibraryDidChange | ``` static let MPMediaLibraryDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMediaPlaybackIsPreparedToPlayDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1616250-mpmediaplaybackispreparedtoplayd)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMediaPlaybackIsPreparedToPlayDidChangeNotification | ``` let MPMediaPlaybackIsPreparedToPlayDidChangeNotification: String ``` |
| To | MPMediaPlaybackIsPreparedToPlayDidChange | ``` static let MPMediaPlaybackIsPreparedToPlayDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMovieDurationAvailable](https://developer.apple.com/documentation/mediaplayer/mpmoviedurationavailablenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMovieDurationAvailableNotification | ``` let MPMovieDurationAvailableNotification: String ``` |
| To | MPMovieDurationAvailable | ``` static let MPMovieDurationAvailable: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMovieMediaTypesAvailable](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypesavailablenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMovieMediaTypesAvailableNotification | ``` let MPMovieMediaTypesAvailableNotification: String ``` |
| To | MPMovieMediaTypesAvailable | ``` static let MPMovieMediaTypesAvailable: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMovieNaturalSizeAvailable](https://developer.apple.com/documentation/foundation/nsnotification/name/1620842-mpmovienaturalsizeavailable)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMovieNaturalSizeAvailableNotification | ``` let MPMovieNaturalSizeAvailableNotification: String ``` |
| To | MPMovieNaturalSizeAvailable | ``` static let MPMovieNaturalSizeAvailable: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerDidEnterFullscreen](https://developer.apple.com/documentation/foundation/nsnotification/name/1620816-mpmovieplayerdidenterfullscreen)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerDidEnterFullscreenNotification | ``` let MPMoviePlayerDidEnterFullscreenNotification: String ``` |
| To | MPMoviePlayerDidEnterFullscreen | ``` static let MPMoviePlayerDidEnterFullscreen: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerDidExitFullscreen](https://developer.apple.com/documentation/foundation/nsnotification/name/1620945-mpmovieplayerdidexitfullscreen)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerDidExitFullscreenNotification | ``` let MPMoviePlayerDidExitFullscreenNotification: String ``` |
| To | MPMoviePlayerDidExitFullscreen | ``` static let MPMoviePlayerDidExitFullscreen: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerIsAirPlayVideoActiveDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1620802-mpmovieplayerisairplayvideoactiv)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification | ``` let MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification: String ``` |
| To | MPMoviePlayerIsAirPlayVideoActiveDidChange | ``` static let MPMoviePlayerIsAirPlayVideoActiveDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerLoadStateDidChange](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerloadstatedidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerLoadStateDidChangeNotification | ``` let MPMoviePlayerLoadStateDidChangeNotification: String ``` |
| To | MPMoviePlayerLoadStateDidChange | ``` static let MPMoviePlayerLoadStateDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerNowPlayingMovieDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1620917-mpmovieplayernowplayingmoviedidc)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerNowPlayingMovieDidChangeNotification | ``` let MPMoviePlayerNowPlayingMovieDidChangeNotification: String ``` |
| To | MPMoviePlayerNowPlayingMovieDidChange | ``` static let MPMoviePlayerNowPlayingMovieDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerPlaybackDidFinish](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerplaybackdidfinishnotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerPlaybackDidFinishNotification | ``` let MPMoviePlayerPlaybackDidFinishNotification: String ``` |
| To | MPMoviePlayerPlaybackDidFinish | ``` static let MPMoviePlayerPlaybackDidFinish: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerPlaybackStateDidChange](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerplaybackstatedidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerPlaybackStateDidChangeNotification | ``` let MPMoviePlayerPlaybackStateDidChangeNotification: String ``` |
| To | MPMoviePlayerPlaybackStateDidChange | ``` static let MPMoviePlayerPlaybackStateDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerReadyForDisplayDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1620783-mpmovieplayerreadyfordisplaydidc)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerReadyForDisplayDidChangeNotification | ``` let MPMoviePlayerReadyForDisplayDidChangeNotification: String ``` |
| To | MPMoviePlayerReadyForDisplayDidChange | ``` static let MPMoviePlayerReadyForDisplayDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerScalingModeDidChange](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerscalingmodedidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerScalingModeDidChangeNotification | ``` let MPMoviePlayerScalingModeDidChangeNotification: String ``` |
| To | MPMoviePlayerScalingModeDidChange | ``` static let MPMoviePlayerScalingModeDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerThumbnailImageRequestDidFinish](https://developer.apple.com/documentation/foundation/nsnotification/name/1620907-mpmovieplayerthumbnailimagereque)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerThumbnailImageRequestDidFinishNotification | ``` let MPMoviePlayerThumbnailImageRequestDidFinishNotification: String ``` |
| To | MPMoviePlayerThumbnailImageRequestDidFinish | ``` static let MPMoviePlayerThumbnailImageRequestDidFinish: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerTimedMetadataUpdated](https://developer.apple.com/documentation/foundation/nsnotification/name/1620953-mpmovieplayertimedmetadataupdate)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerTimedMetadataUpdatedNotification | ``` let MPMoviePlayerTimedMetadataUpdatedNotification: String ``` |
| To | MPMoviePlayerTimedMetadataUpdated | ``` static let MPMoviePlayerTimedMetadataUpdated: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerWillEnterFullscreen](https://developer.apple.com/documentation/foundation/nsnotification/name/1620898-mpmovieplayerwillenterfullscreen)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerWillEnterFullscreenNotification | ``` let MPMoviePlayerWillEnterFullscreenNotification: String ``` |
| To | MPMoviePlayerWillEnterFullscreen | ``` static let MPMoviePlayerWillEnterFullscreen: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMoviePlayerWillExitFullscreen](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerwillexitfullscreennotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMoviePlayerWillExitFullscreenNotification | ``` let MPMoviePlayerWillExitFullscreenNotification: String ``` |
| To | MPMoviePlayerWillExitFullscreen | ``` static let MPMoviePlayerWillExitFullscreen: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMovieSourceTypeAvailable](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetypeavailablenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMovieSourceTypeAvailableNotification | ``` let MPMovieSourceTypeAvailableNotification: String ``` |
| To | MPMovieSourceTypeAvailable | ``` static let MPMovieSourceTypeAvailable: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMusicPlayerControllerNowPlayingItemDidChange](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollernowplayingitemdidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMusicPlayerControllerNowPlayingItemDidChangeNotification | ``` let MPMusicPlayerControllerNowPlayingItemDidChangeNotification: String ``` |
| To | MPMusicPlayerControllerNowPlayingItemDidChange | ``` static let MPMusicPlayerControllerNowPlayingItemDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMusicPlayerControllerPlaybackStateDidChange](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollerplaybackstatedidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMusicPlayerControllerPlaybackStateDidChangeNotification | ``` let MPMusicPlayerControllerPlaybackStateDidChangeNotification: String ``` |
| To | MPMusicPlayerControllerPlaybackStateDidChange | ``` static let MPMusicPlayerControllerPlaybackStateDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPMusicPlayerControllerVolumeDidChange](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollervolumedidchangenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPMusicPlayerControllerVolumeDidChangeNotification | ``` let MPMusicPlayerControllerVolumeDidChangeNotification: String ``` |
| To | MPMusicPlayerControllerVolumeDidChange | ``` static let MPMusicPlayerControllerVolumeDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPVolumeViewWirelessRouteActiveDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1620070-mpvolumeviewwirelessrouteactived)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPVolumeViewWirelessRouteActiveDidChangeNotification | ``` let MPVolumeViewWirelessRouteActiveDidChangeNotification: String ``` |
| To | MPVolumeViewWirelessRouteActiveDidChange | ``` static let MPVolumeViewWirelessRouteActiveDidChange: NSNotification.Name ``` |

Modified [NSNotification.Name.MPVolumeViewWirelessRoutesAvailableDidChange](https://developer.apple.com/documentation/foundation/nsnotification/name/1620065-mpvolumeviewwirelessroutesavaila)

|  | Name | Declaration |
| --- | --- | --- |
| From | MPVolumeViewWirelessRoutesAvailableDidChangeNotification | ``` let MPVolumeViewWirelessRoutesAvailableDidChangeNotification: String ``` |
| To | MPVolumeViewWirelessRoutesAvailableDidChange | ``` static let MPVolumeViewWirelessRoutesAvailableDidChange: NSNotification.Name ``` |

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
