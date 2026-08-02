---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/MediaPlayer.html
archived_at: '2026-07-18T02:57:51.132666Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# MediaPlayer Changes for Swift

### MediaPlayer

Added [MPChangeLanguageOptionCommandEvent.setting](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent/1649697-setting)Added [MPChangeLanguageOptionSetting [enum]](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting)Added [MPChangeLanguageOptionSetting.none](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting/none)Added [MPChangeLanguageOptionSetting.nowPlayingItemOnly](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting/nowplayingitemonly)Added [MPChangeLanguageOptionSetting.permanent](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptionsetting/permanent)Added [MPChangeRepeatModeCommand](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommand)Added [MPChangeRepeatModeCommand.currentRepeatType](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommand/1648342-currentrepeattype)Added [MPChangeRepeatModeCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent)Added [MPChangeRepeatModeCommandEvent.preservesRepeatMode](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent/2097553-preservesrepeatmode)Added [MPChangeRepeatModeCommandEvent.repeatType](https://developer.apple.com/documentation/mediaplayer/mpchangerepeatmodecommandevent/1649689-repeattype)Added [MPChangeShuffleModeCommand](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommand)Added [MPChangeShuffleModeCommand.currentShuffleType](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommand/1648341-currentshuffletype)Added [MPChangeShuffleModeCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommandevent)Added [MPChangeShuffleModeCommandEvent.preservesShuffleMode](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommandevent/2097552-preservesshufflemode)Added [MPChangeShuffleModeCommandEvent.shuffleType](https://developer.apple.com/documentation/mediaplayer/mpchangeshufflemodecommandevent/1649696-shuffletype)Added [MPContentItem.isExplicitContent](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1771744-explicitcontent)Added [MPContentItem.isStreamingContent](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1771745-isstreamingcontent)Added [MPError [struct]](https://developer.apple.com/documentation/mediaplayer/mperror)Added [MPError.cloudServiceCapabilityMissing](https://developer.apple.com/documentation/mediaplayer/mperror/2335085-cloudservicecapabilitymissing)Added MPError.init(_nsError: NSError)Added [MPError.networkConnectionFailed](https://developer.apple.com/documentation/mediaplayer/mperror/2335086-networkconnectionfailed)Added [MPError.notFound](https://developer.apple.com/documentation/mediaplayer/mperror/2335090-notfound)Added [MPError.notSupported](https://developer.apple.com/documentation/mediaplayer/mperror/2335087-notsupported)Added [MPError.permissionDenied](https://developer.apple.com/documentation/mediaplayer/mperror/2335088-permissiondenied)Added [MPError.unknown](https://developer.apple.com/documentation/mediaplayer/mperror/2335089-unknown)Added [MPMediaItemArtwork](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork)Added [MPMediaItemArtwork.bounds](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621723-bounds)Added [MPMediaItemArtwork.image(at: CGSize) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621736-image)Added [MPMediaItemArtwork.imageCropRect](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621760-imagecroprect)Added [MPMediaItemArtwork.init(boundsSize: CGSize, requestHandler: (CGSize) -> UIImage)](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1649704-init)Added [MPMediaItemArtwork.init(image: UIImage)](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621747-initwithimage)Added [MPNowPlayingInfoMediaType [enum]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype)Added [MPNowPlayingInfoMediaType.audio](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype/mpnowplayinginfomediatypeaudio)Added [MPNowPlayingInfoMediaType.none](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype/none)Added [MPNowPlayingInfoMediaType.video](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfomediatype/mpnowplayinginfomediatypevideo)Added [MPRemoteCommandCenter.changeRepeatModeCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1649694-changerepeatmodecommand)Added [MPRemoteCommandCenter.changeShuffleModeCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1649692-changeshufflemodecommand)Added [MPRepeatType [enum]](https://developer.apple.com/documentation/mediaplayer/mprepeattype)Added [MPRepeatType.all](https://developer.apple.com/documentation/mediaplayer/mprepeattype/all)Added [MPRepeatType.off](https://developer.apple.com/documentation/mediaplayer/mprepeattype/off)Added [MPRepeatType.one](https://developer.apple.com/documentation/mediaplayer/mprepeattype/mprepeattypeone)Added [MPShuffleType [enum]](https://developer.apple.com/documentation/mediaplayer/mpshuffletype)Added [MPShuffleType.collections](https://developer.apple.com/documentation/mediaplayer/mpshuffletype/mpshuffletypecollections)Added [MPShuffleType.items](https://developer.apple.com/documentation/mediaplayer/mpshuffletype/mpshuffletypeitems)Added [MPShuffleType.off](https://developer.apple.com/documentation/mediaplayer/mpshuffletype/off)Added [MPMediaItemPropertyDateAdded](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertydateadded)Added [MPMediaItemPropertyIsExplicit](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertyisexplicit)Added [MPNowPlayingInfoCollectionIdentifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocollectionidentifier)Added [MPNowPlayingInfoPropertyExternalContentIdentifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyexternalcontentidentifier)Added [MPNowPlayingInfoPropertyExternalUserProfileIdentifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyexternaluserprofileidentifier)Added [MPNowPlayingInfoPropertyIsLiveStream](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyislivestream)Added [MPNowPlayingInfoPropertyMediaType](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertymediatype)Added [MPNowPlayingInfoPropertyPlaybackProgress](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyplaybackprogress)Modified [MPChangeLanguageOptionCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent)

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
| From | ``` case CloudServiceCapabilityMissing ``` | tvOS 9.2 |
| To | ``` case cloudServiceCapabilityMissing ``` | tvOS 10.0 |

Modified [MPError.Code.networkConnectionFailed](https://developer.apple.com/documentation/mediaplayer/mperror/code/networkconnectionfailed)

|  | Declaration |
| --- | --- |
| From | ``` case NetworkConnectionFailed ``` |
| To | ``` case networkConnectionFailed ``` |

Modified [MPError.Code.notFound](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornotfound)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case NotFound ``` | tvOS 9.2 |
| To | ``` case notFound ``` | tvOS 10.0 |

Modified [MPError.Code.notSupported](https://developer.apple.com/documentation/mediaplayer/mperrorcode/mperrornotsupported)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case NotSupported ``` | tvOS 9.2 |
| To | ``` case notSupported ``` | tvOS 10.0 |

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

Modified [MPMediaItem.persistentIDProperty(forGroupingType: MPMediaGrouping) -> String [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621805-persistentidpropertyforgroupingt)

|  | Declaration |
| --- | --- |
| From | ``` class func persistentIDPropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String ``` |
| To | ``` class func persistentIDProperty(forGroupingType groupingType: MPMediaGrouping) -> String ``` |

Modified [MPMediaItem.titleProperty(forGroupingType: MPMediaGrouping) -> String [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621775-titlepropertyforgroupingtype)

|  | Declaration |
| --- | --- |
| From | ``` class func titlePropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String ``` |
| To | ``` class func titleProperty(forGroupingType groupingType: MPMediaGrouping) -> String ``` |

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

Modified [MPRemoteCommandCenter.changePlaybackPositionCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618997-changeplaybackpositioncommand)

|  | Introduction |
| --- | --- |
| From | tvOS 9.0 |
| To | tvOS 9.1 |

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
