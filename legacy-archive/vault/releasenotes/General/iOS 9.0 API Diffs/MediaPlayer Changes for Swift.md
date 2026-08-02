---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/MediaPlayer.html
archived_at: '2026-07-18T02:56:54.474481Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# MediaPlayer Changes for Swift

### MediaPlayer

Removed MPMediaPlaylistAttribute.init(_: UInt)Removed MPMediaType.init(_: UInt)Removed MPMovieLoadState.init(_: UInt)Removed MPMovieMediaTypeMask.init(_: UInt)Added [AVMediaSelectionGroup.makeNowPlayingInfoLanguageOptionGroup() -> MPNowPlayingInfoLanguageOptionGroup](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1623531-makenowplayinginfolanguageoption)Added [AVMediaSelectionOption.makeNowPlayingInfoLanguageOption() -> MPNowPlayingInfoLanguageOption?](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1623532-makenowplayinginfolanguageoption)Added [MPChangeLanguageOptionCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent)Added [MPChangeLanguageOptionCommandEvent.languageOption](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent/1616769-languageoption)Added [MPMovieControlStyle.Default](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle/mpmoviecontrolstyledefault)Added [MPNowPlayingInfoLanguageOption](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption)Added [MPNowPlayingInfoLanguageOption.displayName](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623145-displayname)Added [MPNowPlayingInfoLanguageOption.identifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623135-identifier)Added [MPNowPlayingInfoLanguageOption.init(type: MPNowPlayingInfoLanguageOptionType, languageTag: String, characteristics: [String]?, displayName: String, identifier: String)](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623159-init)Added [MPNowPlayingInfoLanguageOption.isAutomaticLegibleLanguageOption() -> Bool](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623144-isautomaticlegiblelanguageoption)Added [MPNowPlayingInfoLanguageOption.languageOptionCharacteristics](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623152-languageoptioncharacteristics)Added [MPNowPlayingInfoLanguageOption.languageOptionType](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623153-languageoptiontype)Added [MPNowPlayingInfoLanguageOption.languageTag](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623160-languagetag)Added [MPNowPlayingInfoLanguageOptionGroup](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup)Added [MPNowPlayingInfoLanguageOptionGroup.allowEmptySelection](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/1623161-allowemptyselection)Added [MPNowPlayingInfoLanguageOptionGroup.defaultLanguageOption](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/1623142-defaultlanguageoption)Added [MPNowPlayingInfoLanguageOptionGroup.init(languageOptions: [MPNowPlayingInfoLanguageOption], defaultLanguageOption: MPNowPlayingInfoLanguageOption?, allowEmptySelection: Bool)](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/1623138-init)Added [MPNowPlayingInfoLanguageOptionGroup.languageOptions](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/1623157-languageoptions)Added [MPNowPlayingInfoLanguageOptionType [enum]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype)Added [MPNowPlayingInfoLanguageOptionType.Audible](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype/mpnowplayinginfolanguageoptiontypeaudible)Added [MPNowPlayingInfoLanguageOptionType.Legible](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype/mpnowplayinginfolanguageoptiontypelegible)Added [MPPlayableContentDelegate.playableContentManager(_: MPPlayableContentManager, didUpdateContext: MPPlayableContentManagerContext)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620291-playablecontentmanager)Added [MPPlayableContentDelegate.playableContentManager(_: MPPlayableContentManager, initializePlaybackQueueWithCompletionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620294-playablecontentmanager)Added [MPPlayableContentManager.context](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614800-context)Added [MPPlayableContentManagerContext](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext)Added [MPPlayableContentManagerContext.contentLimitsEnabled](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/1623567-contentlimitsenabled)Added [MPPlayableContentManagerContext.contentLimitsEnforced](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/1623570-contentlimitsenforced)Added [MPPlayableContentManagerContext.endpointAvailable](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/1623569-endpointavailable)Added [MPPlayableContentManagerContext.enforcedContentItemsCount](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/1623568-enforcedcontentitemscount)Added [MPPlayableContentManagerContext.enforcedContentTreeDepth](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/1623572-enforcedcontenttreedepth)Added [MPRemoteCommandCenter.disableLanguageOptionCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618988-disablelanguageoptioncommand)Added [MPRemoteCommandCenter.enableLanguageOptionCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618980-enablelanguageoptioncommand)Added [MPLanguageOptionCharacteristicContainsOnlyForcedSubtitles](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristiccontainsonlyforcedsubtitles)Added [MPLanguageOptionCharacteristicDescribesMusicAndSound](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicdescribesmusicandsound)Added [MPLanguageOptionCharacteristicDescribesVideo](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicdescribesvideo)Added [MPLanguageOptionCharacteristicDubbedTranslation](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicdubbedtranslation)Added [MPLanguageOptionCharacteristicEasyToRead](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristiceasytoread)Added [MPLanguageOptionCharacteristicIsAuxiliaryContent](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicisauxiliarycontent)Added [MPLanguageOptionCharacteristicIsMainProgramContent](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicismainprogramcontent)Added [MPLanguageOptionCharacteristicLanguageTranslation](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristiclanguagetranslation)Added [MPLanguageOptionCharacteristicTranscribesSpokenDialog](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristictranscribesspokendialog)Added [MPLanguageOptionCharacteristicVoiceOverTranslation](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicvoiceovertranslation)Added [MPNowPlayingInfoPropertyAvailableLanguageOptions](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyavailablelanguageoptions)Added [MPNowPlayingInfoPropertyCurrentLanguageOptions](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertycurrentlanguageoptions)Modified [MPChangePlaybackRateCommand](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommand)

|  | Declaration |
| --- | --- |
| From | ``` class MPChangePlaybackRateCommand : MPRemoteCommand {     var supportedPlaybackRates: [AnyObject]! } ``` |
| To | ``` class MPChangePlaybackRateCommand : MPRemoteCommand {     var supportedPlaybackRates: [NSNumber] } ``` |

Modified [MPChangePlaybackRateCommand.supportedPlaybackRates](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommand/1622915-supportedplaybackrates)

|  | Declaration |
| --- | --- |
| From | ``` var supportedPlaybackRates: [AnyObject]! ``` |
| To | ``` var supportedPlaybackRates: [NSNumber] ``` |

Modified [MPContentItem](https://developer.apple.com/documentation/mediaplayer/mpcontentitem)

|  | Declaration |
| --- | --- |
| From | ``` class MPContentItem : NSObject {     var identifier: String! { get }     var title: String!     var subtitle: String!     var artwork: MPMediaItemArtwork!     var container: Bool     var playable: Bool     var playbackProgress: Float     init!(identifier identifier: String!) } ``` |
| To | ``` class MPContentItem : NSObject {     var identifier: String { get }     var title: String?     var subtitle: String?     var artwork: MPMediaItemArtwork?     var container: Bool     var playable: Bool     var playbackProgress: Float     init(identifier identifier: String) } ``` |

Modified [MPContentItem.artwork](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620160-artwork)

|  | Declaration |
| --- | --- |
| From | ``` var artwork: MPMediaItemArtwork! ``` |
| To | ``` var artwork: MPMediaItemArtwork? ``` |

Modified [MPContentItem.identifier](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620157-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String { get } ``` |

Modified [MPContentItem.init(identifier: String)](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620152-initwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(identifier identifier: String!) ``` |
| To | ``` init(identifier identifier: String) ``` |

Modified [MPContentItem.subtitle](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620155-subtitle)

|  | Declaration |
| --- | --- |
| From | ``` var subtitle: String! ``` |
| To | ``` var subtitle: String? ``` |

Modified [MPContentItem.title](https://developer.apple.com/documentation/mediaplayer/mpcontentitem/1620156-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String? ``` |

Modified [MPFeedbackCommand](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommand)

|  | Declaration |
| --- | --- |
| From | ``` class MPFeedbackCommand : MPRemoteCommand {     var active: Bool     var localizedTitle: String!     var localizedShortTitle: String! } ``` |
| To | ``` class MPFeedbackCommand : MPRemoteCommand {     var active: Bool     var localizedTitle: String     var localizedShortTitle: String } ``` |

Modified [MPFeedbackCommand.localizedShortTitle](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommand/1622916-localizedshorttitle)

|  | Declaration |
| --- | --- |
| From | ``` var localizedShortTitle: String! ``` |
| To | ``` var localizedShortTitle: String ``` |

Modified [MPFeedbackCommand.localizedTitle](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommand/1622905-localizedtitle)

|  | Declaration |
| --- | --- |
| From | ``` var localizedTitle: String! ``` |
| To | ``` var localizedTitle: String ``` |

Modified [MPMediaEntity](https://developer.apple.com/documentation/mediaplayer/mpmediaentity)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaEntity : NSObject, NSSecureCoding, NSCoding {     class func canFilterByProperty(_ property: String!) -> Bool     func enumerateValuesForProperties(_ properties: Set<NSObject>!, usingBlock block: ((String!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)!)     subscript (key: AnyObject!) -> AnyObject! { get }     func objectForKeyedSubscript(_ key: AnyObject!) -> AnyObject!     func valueForProperty(_ property: String!) -> AnyObject!     var persistentID: MPMediaEntityPersistentID { get } } ``` |
| To | ``` class MPMediaEntity : NSObject, NSSecureCoding, NSCoding {     class func canFilterByProperty(_ property: String) -> Bool     func enumerateValuesForProperties(_ properties: Set<String>, usingBlock block: (String, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     subscript (_ key: AnyObject) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: AnyObject) -> AnyObject?     func valueForProperty(_ property: String) -> AnyObject?     var persistentID: MPMediaEntityPersistentID { get } } ``` |

Modified [MPMediaEntity.canFilterByProperty(_: String) -> Bool [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620123-canfilter)

|  | Declaration |
| --- | --- |
| From | ``` class func canFilterByProperty(_ property: String!) -> Bool ``` |
| To | ``` class func canFilterByProperty(_ property: String) -> Bool ``` |

Modified [MPMediaEntity.enumerateValuesForProperties(_: Set<String>, usingBlock: (String, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620122-enumeratevaluesforproperties)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateValuesForProperties(_ properties: Set<NSObject>!, usingBlock block: ((String!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateValuesForProperties(_ properties: Set<String>, usingBlock block: (String, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [MPMediaEntity.subscript(_: AnyObject) -> AnyObject?](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620124-objectforkeyedsubscript)

|  | Declaration |
| --- | --- |
| From | ``` subscript (key: AnyObject!) -> AnyObject! { get } ``` |
| To | ``` subscript (_ key: AnyObject) -> AnyObject? { get } ``` |

Modified [MPMediaEntity.valueForProperty(_: String) -> AnyObject?](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620128-value)

|  | Declaration |
| --- | --- |
| From | ``` func valueForProperty(_ property: String!) -> AnyObject! ``` |
| To | ``` func valueForProperty(_ property: String) -> AnyObject? ``` |

Modified [MPMediaGrouping [enum]](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [MPMediaItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitem)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaItem : MPMediaEntity {     var persistentID: MPMediaEntityPersistentID { get }     var mediaType: MPMediaType { get }     var title: String! { get }     var albumTitle: String! { get }     var albumPersistentID: MPMediaEntityPersistentID { get }     var artist: String! { get }     var artistPersistentID: MPMediaEntityPersistentID { get }     var albumArtist: String! { get }     var albumArtistPersistentID: MPMediaEntityPersistentID { get }     var genre: String! { get }     var genrePersistentID: MPMediaEntityPersistentID { get }     var composer: String! { get }     var composerPersistentID: MPMediaEntityPersistentID { get }     var playbackDuration: NSTimeInterval { get }     var albumTrackNumber: Int { get }     var albumTrackCount: Int { get }     var discNumber: Int { get }     var discCount: Int { get }     var artwork: MPMediaItemArtwork! { get }     var lyrics: String! { get }     var compilation: Bool { get }     var releaseDate: NSDate! { get }     var beatsPerMinute: Int { get }     var comments: String! { get }     var assetURL: NSURL! { get }     var cloudItem: Bool { get }     var podcastTitle: String! { get }     var podcastPersistentID: MPMediaEntityPersistentID { get }     var playCount: Int { get }     var skipCount: Int { get }     var rating: Int { get }     var lastPlayedDate: NSDate! { get }     var userGrouping: String! { get }     var bookmarkTime: NSTimeInterval { get } } extension MPMediaItem {     class func persistentIDPropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String!     class func titlePropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String! } ``` |
| To | ``` class MPMediaItem : MPMediaEntity {     var persistentID: MPMediaEntityPersistentID { get }     var mediaType: MPMediaType { get }     var title: String? { get }     var albumTitle: String? { get }     var albumPersistentID: MPMediaEntityPersistentID { get }     var artist: String? { get }     var artistPersistentID: MPMediaEntityPersistentID { get }     var albumArtist: String? { get }     var albumArtistPersistentID: MPMediaEntityPersistentID { get }     var genre: String? { get }     var genrePersistentID: MPMediaEntityPersistentID { get }     var composer: String? { get }     var composerPersistentID: MPMediaEntityPersistentID { get }     var playbackDuration: NSTimeInterval { get }     var albumTrackNumber: Int { get }     var albumTrackCount: Int { get }     var discNumber: Int { get }     var discCount: Int { get }     var artwork: MPMediaItemArtwork? { get }     var lyrics: String? { get }     var compilation: Bool { get }     var releaseDate: NSDate? { get }     var beatsPerMinute: Int { get }     var comments: String? { get }     var assetURL: NSURL? { get }     var cloudItem: Bool { get }     var podcastTitle: String? { get }     var podcastPersistentID: MPMediaEntityPersistentID { get }     var playCount: Int { get }     var skipCount: Int { get }     var rating: Int { get }     var lastPlayedDate: NSDate? { get }     var userGrouping: String? { get }     var bookmarkTime: NSTimeInterval { get } } extension MPMediaItem {     class func persistentIDPropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String     class func titlePropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String } ``` |

Modified [MPMediaItem.albumArtist](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621734-albumartist)

|  | Declaration |
| --- | --- |
| From | ``` var albumArtist: String! { get } ``` |
| To | ``` var albumArtist: String? { get } ``` |

Modified [MPMediaItem.albumTitle](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621756-albumtitle)

|  | Declaration |
| --- | --- |
| From | ``` var albumTitle: String! { get } ``` |
| To | ``` var albumTitle: String? { get } ``` |

Modified [MPMediaItem.artist](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621714-artist)

|  | Declaration |
| --- | --- |
| From | ``` var artist: String! { get } ``` |
| To | ``` var artist: String? { get } ``` |

Modified [MPMediaItem.artwork](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621743-artwork)

|  | Declaration |
| --- | --- |
| From | ``` var artwork: MPMediaItemArtwork! { get } ``` |
| To | ``` var artwork: MPMediaItemArtwork? { get } ``` |

Modified [MPMediaItem.assetURL](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621707-asseturl)

|  | Declaration |
| --- | --- |
| From | ``` var assetURL: NSURL! { get } ``` |
| To | ``` var assetURL: NSURL? { get } ``` |

Modified [MPMediaItem.comments](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621767-comments)

|  | Declaration |
| --- | --- |
| From | ``` var comments: String! { get } ``` |
| To | ``` var comments: String? { get } ``` |

Modified [MPMediaItem.composer](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621681-composer)

|  | Declaration |
| --- | --- |
| From | ``` var composer: String! { get } ``` |
| To | ``` var composer: String? { get } ``` |

Modified [MPMediaItem.genre](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621762-genre)

|  | Declaration |
| --- | --- |
| From | ``` var genre: String! { get } ``` |
| To | ``` var genre: String? { get } ``` |

Modified [MPMediaItem.lastPlayedDate](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621719-lastplayeddate)

|  | Declaration |
| --- | --- |
| From | ``` var lastPlayedDate: NSDate! { get } ``` |
| To | ``` var lastPlayedDate: NSDate? { get } ``` |

Modified [MPMediaItem.lyrics](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621684-lyrics)

|  | Declaration |
| --- | --- |
| From | ``` var lyrics: String! { get } ``` |
| To | ``` var lyrics: String? { get } ``` |

Modified [MPMediaItem.persistentIDPropertyForGroupingType(_: MPMediaGrouping) -> String [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621805-persistentidpropertyforgroupingt)

|  | Declaration |
| --- | --- |
| From | ``` class func persistentIDPropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String! ``` |
| To | ``` class func persistentIDPropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String ``` |

Modified [MPMediaItem.podcastTitle](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621715-podcasttitle)

|  | Declaration |
| --- | --- |
| From | ``` var podcastTitle: String! { get } ``` |
| To | ``` var podcastTitle: String? { get } ``` |

Modified [MPMediaItem.releaseDate](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621682-releasedate)

|  | Declaration |
| --- | --- |
| From | ``` var releaseDate: NSDate! { get } ``` |
| To | ``` var releaseDate: NSDate? { get } ``` |

Modified [MPMediaItem.title](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621713-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String? { get } ``` |

Modified [MPMediaItem.titlePropertyForGroupingType(_: MPMediaGrouping) -> String [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621775-titlepropertyforgroupingtype)

|  | Declaration |
| --- | --- |
| From | ``` class func titlePropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String! ``` |
| To | ``` class func titlePropertyForGroupingType(_ groupingType: MPMediaGrouping) -> String ``` |

Modified [MPMediaItem.userGrouping](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621716-usergrouping)

|  | Declaration |
| --- | --- |
| From | ``` var userGrouping: String! { get } ``` |
| To | ``` var userGrouping: String? { get } ``` |

Modified [MPMediaItemArtwork](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaItemArtwork : NSObject {     init!(image image: UIImage!)     func imageWithSize(_ size: CGSize) -> UIImage!     var bounds: CGRect { get }     var imageCropRect: CGRect { get } } ``` |
| To | ``` class MPMediaItemArtwork : NSObject {     init(image image: UIImage)     func imageWithSize(_ size: CGSize) -> UIImage?     var bounds: CGRect { get }     var imageCropRect: CGRect { get } } ``` |

Modified [MPMediaItemArtwork.imageWithSize(_: CGSize) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621736-image)

|  | Declaration |
| --- | --- |
| From | ``` func imageWithSize(_ size: CGSize) -> UIImage! ``` |
| To | ``` func imageWithSize(_ size: CGSize) -> UIImage? ``` |

Modified [MPMediaItemArtwork.init(image: UIImage)](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621747-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` init!(image image: UIImage!) ``` |
| To | ``` init(image image: UIImage) ``` |

Modified [MPMediaItemCollection](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaItemCollection : MPMediaEntity {     init!(items items: [AnyObject]!) -> MPMediaItemCollection     class func collectionWithItems(_ items: [AnyObject]!) -> MPMediaItemCollection!     init!(items items: [AnyObject]!)     var items: [AnyObject]! { get }     var representativeItem: MPMediaItem! { get }     var count: Int { get }     var mediaTypes: MPMediaType { get } } ``` |
| To | ``` class MPMediaItemCollection : MPMediaEntity {      init(items items: [MPMediaItem])     class func collectionWithItems(_ items: [MPMediaItem]) -> MPMediaItemCollection     init(items items: [MPMediaItem])     var items: [MPMediaItem] { get }     var representativeItem: MPMediaItem? { get }     var count: Int { get }     var mediaTypes: MPMediaType { get } } ``` |

Modified [MPMediaItemCollection.init(items: [MPMediaItem])](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/1614440-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(items items: [AnyObject]!) ``` |
| To | ``` init(items items: [MPMediaItem]) ``` |

Modified [MPMediaItemCollection.items](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/1614441-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject]! { get } ``` |
| To | ``` var items: [MPMediaItem] { get } ``` |

Modified [MPMediaItemCollection.representativeItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/1614439-representativeitem)

|  | Declaration |
| --- | --- |
| From | ``` var representativeItem: MPMediaItem! { get } ``` |
| To | ``` var representativeItem: MPMediaItem? { get } ``` |

Modified [MPMediaLibrary](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaLibrary : NSObject, NSSecureCoding, NSCoding {     class func defaultMediaLibrary() -> MPMediaLibrary!     var lastModifiedDate: NSDate! { get }     func beginGeneratingLibraryChangeNotifications()     func endGeneratingLibraryChangeNotifications() } ``` |
| To | ``` class MPMediaLibrary : NSObject, NSSecureCoding, NSCoding {     class func defaultMediaLibrary() -> MPMediaLibrary     var lastModifiedDate: NSDate { get }     func beginGeneratingLibraryChangeNotifications()     func endGeneratingLibraryChangeNotifications() } ``` |

Modified [MPMediaLibrary.defaultMediaLibrary() -> MPMediaLibrary [class]](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621269-default)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultMediaLibrary() -> MPMediaLibrary! ``` |
| To | ``` class func defaultMediaLibrary() -> MPMediaLibrary ``` |

Modified [MPMediaLibrary.lastModifiedDate](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary/1621279-lastmodifieddate)

|  | Declaration |
| --- | --- |
| From | ``` var lastModifiedDate: NSDate! { get } ``` |
| To | ``` var lastModifiedDate: NSDate { get } ``` |

Modified [MPMediaPickerController](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaPickerController : UIViewController {     init!(mediaTypes mediaTypes: MPMediaType)     var mediaTypes: MPMediaType { get }     weak var delegate: MPMediaPickerControllerDelegate!     var allowsPickingMultipleItems: Bool     var showsCloudItems: Bool     var prompt: String! } ``` |
| To | ``` class MPMediaPickerController : UIViewController {     init(mediaTypes mediaTypes: MPMediaType)     var mediaTypes: MPMediaType { get }     weak var delegate: MPMediaPickerControllerDelegate?     var allowsPickingMultipleItems: Bool     var showsCloudItems: Bool     var prompt: String? } ``` |

Modified [MPMediaPickerController.delegate](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/1614655-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: MPMediaPickerControllerDelegate! ``` |
| To | ``` weak var delegate: MPMediaPickerControllerDelegate? ``` |

Modified [MPMediaPickerController.init(mediaTypes: MPMediaType)](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/1614663-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(mediaTypes mediaTypes: MPMediaType) ``` |
| To | ``` init(mediaTypes mediaTypes: MPMediaType) ``` |

Modified [MPMediaPickerController.prompt](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/1614669-prompt)

|  | Declaration |
| --- | --- |
| From | ``` var prompt: String! ``` |
| To | ``` var prompt: String? ``` |

Modified [MPMediaPickerControllerDelegate](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MPMediaPickerControllerDelegate : NSObjectProtocol {     optional func mediaPicker(_ mediaPicker: MPMediaPickerController!, didPickMediaItems mediaItemCollection: MPMediaItemCollection!)     optional func mediaPickerDidCancel(_ mediaPicker: MPMediaPickerController!) } ``` |
| To | ``` protocol MPMediaPickerControllerDelegate : NSObjectProtocol {     optional func mediaPicker(_ mediaPicker: MPMediaPickerController, didPickMediaItems mediaItemCollection: MPMediaItemCollection)     optional func mediaPickerDidCancel(_ mediaPicker: MPMediaPickerController) } ``` |

Modified [MPMediaPickerControllerDelegate.mediaPicker(_: MPMediaPickerController, didPickMediaItems: MPMediaItemCollection)](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontrollerdelegate/1614657-mediapicker)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func mediaPicker(_ mediaPicker: MPMediaPickerController!, didPickMediaItems mediaItemCollection: MPMediaItemCollection!) ``` | iOS 8.0 |
| To | ``` optional func mediaPicker(_ mediaPicker: MPMediaPickerController, didPickMediaItems mediaItemCollection: MPMediaItemCollection) ``` | iOS 3.0 |

Modified [MPMediaPickerControllerDelegate.mediaPickerDidCancel(_: MPMediaPickerController)](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontrollerdelegate/1614667-mediapickerdidcancel)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func mediaPickerDidCancel(_ mediaPicker: MPMediaPickerController!) ``` | iOS 8.0 |
| To | ``` optional func mediaPickerDidCancel(_ mediaPicker: MPMediaPickerController) ``` | iOS 3.0 |

Modified [MPMediaPlaylist](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaPlaylist : MPMediaItemCollection {     var persistentID: MPMediaEntityPersistentID { get }     var name: String! { get }     var playlistAttributes: MPMediaPlaylistAttribute { get }     var seedItems: [AnyObject]! { get } } ``` |
| To | ``` class MPMediaPlaylist : MPMediaItemCollection {     var persistentID: MPMediaEntityPersistentID { get }     var name: String? { get }     var playlistAttributes: MPMediaPlaylistAttribute { get }     var seedItems: [MPMediaItem]? { get } } ``` |

Modified [MPMediaPlaylist.name](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618716-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified [MPMediaPlaylist.seedItems](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618720-seeditems)

|  | Declaration |
| --- | --- |
| From | ``` var seedItems: [AnyObject]! { get } ``` |
| To | ``` var seedItems: [MPMediaItem]? { get } ``` |

Modified [MPMediaPlaylistAttribute [struct]](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylistattribute)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MPMediaPlaylistAttribute : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: MPMediaPlaylistAttribute { get }     static var OnTheGo: MPMediaPlaylistAttribute { get }     static var Smart: MPMediaPlaylistAttribute { get }     static var Genius: MPMediaPlaylistAttribute { get } } ``` | RawOptionSetType |
| To | ``` struct MPMediaPlaylistAttribute : OptionSetType {     init(rawValue rawValue: UInt)     static var None: MPMediaPlaylistAttribute { get }     static var OnTheGo: MPMediaPlaylistAttribute { get }     static var Smart: MPMediaPlaylistAttribute { get }     static var Genius: MPMediaPlaylistAttribute { get } } ``` | OptionSetType |

Modified [MPMediaPredicateComparison [enum]](https://developer.apple.com/documentation/mediaplayer/mpmediapredicatecomparison)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [MPMediaPropertyPredicate](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaPropertyPredicate : MPMediaPredicate {     init!(value value: AnyObject!, forProperty property: String!) -> MPMediaPropertyPredicate     class func predicateWithValue(_ value: AnyObject!, forProperty property: String!) -> MPMediaPropertyPredicate!     init!(value value: AnyObject!, forProperty property: String!, comparisonType comparisonType: MPMediaPredicateComparison) -> MPMediaPropertyPredicate     class func predicateWithValue(_ value: AnyObject!, forProperty property: String!, comparisonType comparisonType: MPMediaPredicateComparison) -> MPMediaPropertyPredicate!     var property: String! { get }     @NSCopying var value: AnyObject! { get }     var comparisonType: MPMediaPredicateComparison { get } } ``` |
| To | ``` class MPMediaPropertyPredicate : MPMediaPredicate {      init(value value: AnyObject?, forProperty property: String)     class func predicateWithValue(_ value: AnyObject?, forProperty property: String) -> MPMediaPropertyPredicate      init(value value: AnyObject?, forProperty property: String, comparisonType comparisonType: MPMediaPredicateComparison)     class func predicateWithValue(_ value: AnyObject?, forProperty property: String, comparisonType comparisonType: MPMediaPredicateComparison) -> MPMediaPropertyPredicate     var property: String { get }     @NSCopying var value: AnyObject? { get }     var comparisonType: MPMediaPredicateComparison { get } } ``` |

Modified [MPMediaPropertyPredicate.init(value: AnyObject?, forProperty: String)](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate/1621790-predicatewithvalue)

|  | Declaration |
| --- | --- |
| From | ``` init!(value value: AnyObject!, forProperty property: String!) -> MPMediaPropertyPredicate ``` |
| To | ``` init(value value: AnyObject?, forProperty property: String) ``` |

Modified [MPMediaPropertyPredicate.init(value: AnyObject?, forProperty: String, comparisonType: MPMediaPredicateComparison)](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate/1621798-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(value value: AnyObject!, forProperty property: String!, comparisonType comparisonType: MPMediaPredicateComparison) -> MPMediaPropertyPredicate ``` |
| To | ``` init(value value: AnyObject?, forProperty property: String, comparisonType comparisonType: MPMediaPredicateComparison) ``` |

Modified [MPMediaPropertyPredicate.property](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate/1621801-property)

|  | Declaration |
| --- | --- |
| From | ``` var property: String! { get } ``` |
| To | ``` var property: String { get } ``` |

Modified [MPMediaPropertyPredicate.value](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate/1621772-value)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var value: AnyObject! { get } ``` |
| To | ``` @NSCopying var value: AnyObject? { get } ``` |

Modified [MPMediaQuery](https://developer.apple.com/documentation/mediaplayer/mpmediaquery)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaQuery : NSObject, NSSecureCoding, NSCoding, NSCopying {     init!(filterPredicates filterPredicates: Set<NSObject>!)     var filterPredicates: Set<NSObject>!     func addFilterPredicate(_ predicate: MPMediaPredicate!)     func removeFilterPredicate(_ predicate: MPMediaPredicate!)     var items: [AnyObject]! { get }     var collections: [AnyObject]! { get }     var groupingType: MPMediaGrouping     var itemSections: [AnyObject]! { get }     var collectionSections: [AnyObject]! { get }     class func albumsQuery() -> MPMediaQuery!     class func artistsQuery() -> MPMediaQuery!     class func songsQuery() -> MPMediaQuery!     class func playlistsQuery() -> MPMediaQuery!     class func podcastsQuery() -> MPMediaQuery!     class func audiobooksQuery() -> MPMediaQuery!     class func compilationsQuery() -> MPMediaQuery!     class func composersQuery() -> MPMediaQuery!     class func genresQuery() -> MPMediaQuery! } ``` |
| To | ``` class MPMediaQuery : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(filterPredicates filterPredicates: Set<MPMediaPredicate>?)     var filterPredicates: Set<MPMediaPredicate>?     func addFilterPredicate(_ predicate: MPMediaPredicate)     func removeFilterPredicate(_ predicate: MPMediaPredicate)     var items: [MPMediaItem]? { get }     var collections: [MPMediaItemCollection]? { get }     var groupingType: MPMediaGrouping     var itemSections: [MPMediaQuerySection]? { get }     var collectionSections: [MPMediaQuerySection]? { get }     class func albumsQuery() -> MPMediaQuery     class func artistsQuery() -> MPMediaQuery     class func songsQuery() -> MPMediaQuery     class func playlistsQuery() -> MPMediaQuery     class func podcastsQuery() -> MPMediaQuery     class func audiobooksQuery() -> MPMediaQuery     class func compilationsQuery() -> MPMediaQuery     class func composersQuery() -> MPMediaQuery     class func genresQuery() -> MPMediaQuery } ``` |

Modified [MPMediaQuery.addFilterPredicate(_: MPMediaPredicate)](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621773-addfilterpredicate)

|  | Declaration |
| --- | --- |
| From | ``` func addFilterPredicate(_ predicate: MPMediaPredicate!) ``` |
| To | ``` func addFilterPredicate(_ predicate: MPMediaPredicate) ``` |

Modified [MPMediaQuery.albumsQuery() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621780-albums)

|  | Declaration |
| --- | --- |
| From | ``` class func albumsQuery() -> MPMediaQuery! ``` |
| To | ``` class func albumsQuery() -> MPMediaQuery ``` |

Modified [MPMediaQuery.artistsQuery() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621787-artistsquery)

|  | Declaration |
| --- | --- |
| From | ``` class func artistsQuery() -> MPMediaQuery! ``` |
| To | ``` class func artistsQuery() -> MPMediaQuery ``` |

Modified [MPMediaQuery.audiobooksQuery() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621783-audiobooks)

|  | Declaration |
| --- | --- |
| From | ``` class func audiobooksQuery() -> MPMediaQuery! ``` |
| To | ``` class func audiobooksQuery() -> MPMediaQuery ``` |

Modified [MPMediaQuery.collections](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621806-collections)

|  | Declaration |
| --- | --- |
| From | ``` var collections: [AnyObject]! { get } ``` |
| To | ``` var collections: [MPMediaItemCollection]? { get } ``` |

Modified [MPMediaQuery.collectionSections](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621779-collectionsections)

|  | Declaration |
| --- | --- |
| From | ``` var collectionSections: [AnyObject]! { get } ``` |
| To | ``` var collectionSections: [MPMediaQuerySection]? { get } ``` |

Modified [MPMediaQuery.compilationsQuery() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621786-compilations)

|  | Declaration |
| --- | --- |
| From | ``` class func compilationsQuery() -> MPMediaQuery! ``` |
| To | ``` class func compilationsQuery() -> MPMediaQuery ``` |

Modified [MPMediaQuery.composersQuery() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621796-composers)

|  | Declaration |
| --- | --- |
| From | ``` class func composersQuery() -> MPMediaQuery! ``` |
| To | ``` class func composersQuery() -> MPMediaQuery ``` |

Modified [MPMediaQuery.filterPredicates](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621781-filterpredicates)

|  | Declaration |
| --- | --- |
| From | ``` var filterPredicates: Set<NSObject>! ``` |
| To | ``` var filterPredicates: Set<MPMediaPredicate>? ``` |

Modified [MPMediaQuery.genresQuery() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621788-genres)

|  | Declaration |
| --- | --- |
| From | ``` class func genresQuery() -> MPMediaQuery! ``` |
| To | ``` class func genresQuery() -> MPMediaQuery ``` |

Modified [MPMediaQuery.init(filterPredicates: Set<MPMediaPredicate>?)](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621771-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(filterPredicates filterPredicates: Set<NSObject>!) ``` |
| To | ``` init(filterPredicates filterPredicates: Set<MPMediaPredicate>?) ``` |

Modified [MPMediaQuery.items](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621770-items)

|  | Declaration |
| --- | --- |
| From | ``` var items: [AnyObject]! { get } ``` |
| To | ``` var items: [MPMediaItem]? { get } ``` |

Modified [MPMediaQuery.itemSections](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621797-itemsections)

|  | Declaration |
| --- | --- |
| From | ``` var itemSections: [AnyObject]! { get } ``` |
| To | ``` var itemSections: [MPMediaQuerySection]? { get } ``` |

Modified [MPMediaQuery.playlistsQuery() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621803-playlistsquery)

|  | Declaration |
| --- | --- |
| From | ``` class func playlistsQuery() -> MPMediaQuery! ``` |
| To | ``` class func playlistsQuery() -> MPMediaQuery ``` |

Modified [MPMediaQuery.podcastsQuery() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621793-podcasts)

|  | Declaration |
| --- | --- |
| From | ``` class func podcastsQuery() -> MPMediaQuery! ``` |
| To | ``` class func podcastsQuery() -> MPMediaQuery ``` |

Modified [MPMediaQuery.removeFilterPredicate(_: MPMediaPredicate)](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621785-removefilterpredicate)

|  | Declaration |
| --- | --- |
| From | ``` func removeFilterPredicate(_ predicate: MPMediaPredicate!) ``` |
| To | ``` func removeFilterPredicate(_ predicate: MPMediaPredicate) ``` |

Modified [MPMediaQuery.songsQuery() -> MPMediaQuery [class]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621791-songsquery)

|  | Declaration |
| --- | --- |
| From | ``` class func songsQuery() -> MPMediaQuery! ``` |
| To | ``` class func songsQuery() -> MPMediaQuery ``` |

Modified [MPMediaQuerySection](https://developer.apple.com/documentation/mediaplayer/mpmediaquerysection)

|  | Declaration |
| --- | --- |
| From | ``` class MPMediaQuerySection : NSObject, NSSecureCoding, NSCoding, NSCopying {     var title: String! { get }     var range: NSRange { get } } ``` |
| To | ``` class MPMediaQuerySection : NSObject, NSSecureCoding, NSCoding, NSCopying {     var title: String { get }     var range: NSRange { get } } ``` |

Modified [MPMediaQuerySection.title](https://developer.apple.com/documentation/mediaplayer/mpmediaquerysection/1624170-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String { get } ``` |

Modified [MPMediaType [struct]](https://developer.apple.com/documentation/mediaplayer/mpmediatype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MPMediaType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Music: MPMediaType { get }     static var Podcast: MPMediaType { get }     static var AudioBook: MPMediaType { get }     static var AudioITunesU: MPMediaType { get }     static var AnyAudio: MPMediaType { get }     static var Movie: MPMediaType { get }     static var TVShow: MPMediaType { get }     static var VideoPodcast: MPMediaType { get }     static var MusicVideo: MPMediaType { get }     static var VideoITunesU: MPMediaType { get }     static var HomeVideo: MPMediaType { get }     static var AnyVideo: MPMediaType { get }     static var Any: MPMediaType { get } } ``` | RawOptionSetType |
| To | ``` struct MPMediaType : OptionSetType {     init(rawValue rawValue: UInt)     static var Music: MPMediaType { get }     static var Podcast: MPMediaType { get }     static var AudioBook: MPMediaType { get }     static var AudioITunesU: MPMediaType { get }     static var AnyAudio: MPMediaType { get }     static var Movie: MPMediaType { get }     static var TVShow: MPMediaType { get }     static var VideoPodcast: MPMediaType { get }     static var MusicVideo: MPMediaType { get }     static var VideoITunesU: MPMediaType { get }     static var HomeVideo: MPMediaType { get }     static var AnyVideo: MPMediaType { get }     static var Any: MPMediaType { get } } ``` | OptionSetType |

Modified [MPMovieControlStyle [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle)

|  | Declaration | Introduction | Deprecation | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` enum MPMovieControlStyle : Int {     case None     case Embedded     case Fullscreen } ``` | iOS 8.1 | -- | -- |
| To | ``` enum MPMovieControlStyle : Int {     case None     case Embedded     case Fullscreen     static var Default: MPMovieControlStyle { get } } ``` | iOS 3.2 | iOS 9.0 | Int |

Modified [MPMovieFinishReason [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviefinishreason)

|  | Introduction | Deprecation | Raw Value Type |
| --- | --- | --- | --- |
| From | iOS 8.1 | -- | -- |
| To | iOS 3.2 | iOS 9.0 | Int |

Modified [MPMovieLoadState [struct]](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate)

|  | Declaration | Protocols | Introduction | Deprecation |
| --- | --- | --- | --- | --- |
| From | ``` struct MPMovieLoadState : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Unknown: MPMovieLoadState { get }     static var Playable: MPMovieLoadState { get }     static var PlaythroughOK: MPMovieLoadState { get }     static var Stalled: MPMovieLoadState { get } } ``` | RawOptionSetType | iOS 8.1 | -- |
| To | ``` struct MPMovieLoadState : OptionSetType {     init(rawValue rawValue: UInt)     static var Unknown: MPMovieLoadState { get }     static var Playable: MPMovieLoadState { get }     static var PlaythroughOK: MPMovieLoadState { get }     static var Stalled: MPMovieLoadState { get } } ``` | OptionSetType | iOS 3.2 | iOS 9.0 |

Modified MPMovieLoadState.init(rawValue: UInt)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieLoadState.Playable](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/1620892-playable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieLoadState.PlaythroughOK](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/1620865-playthroughok)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieLoadState.Stalled](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/1620939-stalled)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieLoadState.Unknown](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/mpmovieloadstateunknown)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieMediaTypeMask [struct]](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask)

|  | Declaration | Protocols | Introduction | Deprecation |
| --- | --- | --- | --- | --- |
| From | ``` struct MPMovieMediaTypeMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: MPMovieMediaTypeMask { get }     static var Video: MPMovieMediaTypeMask { get }     static var Audio: MPMovieMediaTypeMask { get } } ``` | RawOptionSetType | iOS 8.1 | -- |
| To | ``` struct MPMovieMediaTypeMask : OptionSetType {     init(rawValue rawValue: UInt)     static var None: MPMovieMediaTypeMask { get }     static var Video: MPMovieMediaTypeMask { get }     static var Audio: MPMovieMediaTypeMask { get } } ``` | OptionSetType | iOS 3.2 | iOS 9.0 |

Modified [MPMovieMediaTypeMask.Audio](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask/mpmoviemediatypemaskaudio)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified MPMovieMediaTypeMask.init(rawValue: UInt)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieMediaTypeMask.None](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask/mpmoviemediatypemasknone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieMediaTypeMask.Video](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask/mpmoviemediatypemaskvideo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlaybackState [enum]](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate)

|  | Introduction | Deprecation | Raw Value Type |
| --- | --- | --- | --- |
| From | iOS 8.1 | -- | -- |
| To | iOS 3.2 | iOS 9.0 | Int |

Modified [MPMoviePlayerController.accessLog](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620922-accesslog)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.airPlayVideoActive](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620906-airplayvideoactive)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.allowsAirPlay](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620781-allowsairplay)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.cancelAllThumbnailImageRequests()](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620811-cancelallthumbnailimagerequests)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.duration](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620784-duration)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.endPlaybackTime](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620895-endplaybacktime)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.errorLog](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620798-errorlog)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.initialPlaybackTime](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620796-initialplaybacktime)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.movieMediaTypes](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620821-moviemediatypes)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.movieSourceType](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620793-moviesourcetype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.naturalSize](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620877-naturalsize)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.playableDuration](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620803-playableduration)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.requestThumbnailImagesAtTimes(_: [AnyObject]!, timeOption: MPMovieTimeOption)](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620805-requestthumbnailimages)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.timedMetadata](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620853-timedmetadata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieRepeatMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmovierepeatmode)

|  | Introduction | Deprecation | Raw Value Type |
| --- | --- | --- | --- |
| From | iOS 8.1 | -- | -- |
| To | iOS 3.2 | iOS 9.0 | Int |

Modified [MPMovieScalingMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode)

|  | Introduction | Deprecation | Raw Value Type |
| --- | --- | --- | --- |
| From | iOS 8.1 | -- | -- |
| To | iOS 2.0 | iOS 9.0 | Int |

Modified [MPMovieSourceType [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetype)

|  | Introduction | Deprecation | Raw Value Type |
| --- | --- | --- | --- |
| From | iOS 8.1 | -- | -- |
| To | iOS 3.2 | iOS 9.0 | Int |

Modified [MPMovieTimeOption [enum]](https://developer.apple.com/documentation/mediaplayer/mpmovietimeoption)

|  | Introduction | Deprecation | Raw Value Type |
| --- | --- | --- | --- |
| From | iOS 8.1 | -- | -- |
| To | iOS 3.2 | iOS 9.0 | Int |

Modified [MPMusicPlaybackState [enum]](https://developer.apple.com/documentation/mediaplayer/mpmusicplaybackstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [MPMusicPlayerController](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller)

|  | Declaration |
| --- | --- |
| From | ``` class MPMusicPlayerController : NSObject, MPMediaPlayback {     class func applicationMusicPlayer() -> MPMusicPlayerController!     class func systemMusicPlayer() -> MPMusicPlayerController!     class func iPodMusicPlayer() -> MPMusicPlayerController! } extension MPMusicPlayerController {     var playbackState: MPMusicPlaybackState { get }     var repeatMode: MPMusicRepeatMode     var shuffleMode: MPMusicShuffleMode     var volume: Float     @NSCopying var nowPlayingItem: MPMediaItem!     var indexOfNowPlayingItem: Int { get }     func setQueueWithQuery(_ query: MPMediaQuery!)     func setQueueWithItemCollection(_ itemCollection: MPMediaItemCollection!)     func skipToNextItem()     func skipToBeginning()     func skipToPreviousItem()     func beginGeneratingPlaybackNotifications()     func endGeneratingPlaybackNotifications() } ``` |
| To | ``` class MPMusicPlayerController : NSObject, MPMediaPlayback {     class func applicationMusicPlayer() -> MPMusicPlayerController     class func systemMusicPlayer() -> MPMusicPlayerController     class func iPodMusicPlayer() -> MPMusicPlayerController } extension MPMusicPlayerController {     var playbackState: MPMusicPlaybackState { get }     var repeatMode: MPMusicRepeatMode     var shuffleMode: MPMusicShuffleMode     var volume: Float     @NSCopying var nowPlayingItem: MPMediaItem?     var indexOfNowPlayingItem: Int { get }     func setQueueWithQuery(_ query: MPMediaQuery)     func setQueueWithItemCollection(_ itemCollection: MPMediaItemCollection)     func skipToNextItem()     func skipToBeginning()     func skipToPreviousItem()     func beginGeneratingPlaybackNotifications()     func endGeneratingPlaybackNotifications() } ``` |

Modified [MPMusicPlayerController.applicationMusicPlayer() -> MPMusicPlayerController [class]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624156-applicationmusicplayer)

|  | Declaration |
| --- | --- |
| From | ``` class func applicationMusicPlayer() -> MPMusicPlayerController! ``` |
| To | ``` class func applicationMusicPlayer() -> MPMusicPlayerController ``` |

Modified [MPMusicPlayerController.iPodMusicPlayer() -> MPMusicPlayerController [class]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624206-ipodmusicplayer)

|  | Declaration |
| --- | --- |
| From | ``` class func iPodMusicPlayer() -> MPMusicPlayerController! ``` |
| To | ``` class func iPodMusicPlayer() -> MPMusicPlayerController ``` |

Modified [MPMusicPlayerController.nowPlayingItem](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624245-nowplayingitem)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var nowPlayingItem: MPMediaItem! ``` |
| To | ``` @NSCopying var nowPlayingItem: MPMediaItem? ``` |

Modified [MPMusicPlayerController.setQueueWithItemCollection(_: MPMediaItemCollection)](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624171-setqueuewithitemcollection)

|  | Declaration |
| --- | --- |
| From | ``` func setQueueWithItemCollection(_ itemCollection: MPMediaItemCollection!) ``` |
| To | ``` func setQueueWithItemCollection(_ itemCollection: MPMediaItemCollection) ``` |

Modified [MPMusicPlayerController.setQueueWithQuery(_: MPMediaQuery)](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624180-setqueue)

|  | Declaration |
| --- | --- |
| From | ``` func setQueueWithQuery(_ query: MPMediaQuery!) ``` |
| To | ``` func setQueueWithQuery(_ query: MPMediaQuery) ``` |

Modified [MPMusicPlayerController.systemMusicPlayer() -> MPMusicPlayerController [class]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624179-systemmusicplayer)

|  | Declaration |
| --- | --- |
| From | ``` class func systemMusicPlayer() -> MPMusicPlayerController! ``` |
| To | ``` class func systemMusicPlayer() -> MPMusicPlayerController ``` |

Modified [MPMusicRepeatMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmusicrepeatmode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [MPMusicShuffleMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmusicshufflemode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [MPNowPlayingInfoCenter](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter)

|  | Declaration |
| --- | --- |
| From | ``` class MPNowPlayingInfoCenter : NSObject {     class func defaultCenter() -> MPNowPlayingInfoCenter!     var nowPlayingInfo: [NSObject : AnyObject]! } ``` |
| To | ``` class MPNowPlayingInfoCenter : NSObject {     class func defaultCenter() -> MPNowPlayingInfoCenter     var nowPlayingInfo: [String : AnyObject]? } ``` |

Modified [MPNowPlayingInfoCenter.defaultCenter() -> MPNowPlayingInfoCenter [class]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/1615899-defaultcenter)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultCenter() -> MPNowPlayingInfoCenter! ``` |
| To | ``` class func defaultCenter() -> MPNowPlayingInfoCenter ``` |

Modified [MPNowPlayingInfoCenter.nowPlayingInfo](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/1615903-nowplayinginfo)

|  | Declaration |
| --- | --- |
| From | ``` var nowPlayingInfo: [NSObject : AnyObject]! ``` |
| To | ``` var nowPlayingInfo: [String : AnyObject]? ``` |

Modified [MPPlayableContentDataSource](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource)

|  | Declaration |
| --- | --- |
| From | ``` protocol MPPlayableContentDataSource : NSObjectProtocol {     optional func beginLoadingChildItemsAtIndexPath(_ indexPath: NSIndexPath!, completionHandler completionHandler: ((NSError!) -> Void)!)     optional func childItemsDisplayPlaybackProgressAtIndexPath(_ indexPath: NSIndexPath!) -> Bool     func numberOfChildItemsAtIndexPath(_ indexPath: NSIndexPath!) -> Int     func contentItemAtIndexPath(_ indexPath: NSIndexPath!) -> MPContentItem! } ``` |
| To | ``` protocol MPPlayableContentDataSource : NSObjectProtocol {     optional func beginLoadingChildItemsAtIndexPath(_ indexPath: NSIndexPath, completionHandler completionHandler: (NSError?) -> Void)     optional func childItemsDisplayPlaybackProgressAtIndexPath(_ indexPath: NSIndexPath) -> Bool     func numberOfChildItemsAtIndexPath(_ indexPath: NSIndexPath) -> Int     func contentItemAtIndexPath(_ indexPath: NSIndexPath) -> MPContentItem? } ``` |

Modified [MPPlayableContentDataSource.beginLoadingChildItemsAtIndexPath(_: NSIndexPath, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619508-beginloadingchilditems)

|  | Declaration |
| --- | --- |
| From | ``` optional func beginLoadingChildItemsAtIndexPath(_ indexPath: NSIndexPath!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` optional func beginLoadingChildItemsAtIndexPath(_ indexPath: NSIndexPath, completionHandler completionHandler: (NSError?) -> Void) ``` |

Modified [MPPlayableContentDataSource.childItemsDisplayPlaybackProgressAtIndexPath(_: NSIndexPath) -> Bool](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619509-childitemsdisplayplaybackprogres)

|  | Declaration |
| --- | --- |
| From | ``` optional func childItemsDisplayPlaybackProgressAtIndexPath(_ indexPath: NSIndexPath!) -> Bool ``` |
| To | ``` optional func childItemsDisplayPlaybackProgressAtIndexPath(_ indexPath: NSIndexPath) -> Bool ``` |

Modified [MPPlayableContentDataSource.contentItemAtIndexPath(_: NSIndexPath) -> MPContentItem?](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619505-contentitematindexpath)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func contentItemAtIndexPath(_ indexPath: NSIndexPath!) -> MPContentItem! ``` | iOS 8.0 |
| To | ``` func contentItemAtIndexPath(_ indexPath: NSIndexPath) -> MPContentItem? ``` | iOS 7.1 |

Modified [MPPlayableContentDataSource.numberOfChildItemsAtIndexPath(_: NSIndexPath) -> Int](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619506-numberofchilditems)

|  | Declaration |
| --- | --- |
| From | ``` func numberOfChildItemsAtIndexPath(_ indexPath: NSIndexPath!) -> Int ``` |
| To | ``` func numberOfChildItemsAtIndexPath(_ indexPath: NSIndexPath) -> Int ``` |

Modified [MPPlayableContentDelegate](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MPPlayableContentDelegate : NSObjectProtocol {     optional func playableContentManager(_ contentManager: MPPlayableContentManager!, initiatePlaybackOfContentItemAtIndexPath indexPath: NSIndexPath!, completionHandler completionHandler: ((NSError!) -> Void)!) } ``` |
| To | ``` protocol MPPlayableContentDelegate : NSObjectProtocol {     optional func playableContentManager(_ contentManager: MPPlayableContentManager, initiatePlaybackOfContentItemAtIndexPath indexPath: NSIndexPath, completionHandler completionHandler: (NSError?) -> Void)     optional func playableContentManager(_ contentManager: MPPlayableContentManager, initializePlaybackQueueWithCompletionHandler completionHandler: (NSError?) -> Void)     optional func playableContentManager(_ contentManager: MPPlayableContentManager, didUpdateContext context: MPPlayableContentManagerContext) } ``` |

Modified [MPPlayableContentDelegate.playableContentManager(_: MPPlayableContentManager, initiatePlaybackOfContentItemAtIndexPath: NSIndexPath, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620292-playablecontentmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func playableContentManager(_ contentManager: MPPlayableContentManager!, initiatePlaybackOfContentItemAtIndexPath indexPath: NSIndexPath!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` | iOS 8.0 |
| To | ``` optional func playableContentManager(_ contentManager: MPPlayableContentManager, initiatePlaybackOfContentItemAtIndexPath indexPath: NSIndexPath, completionHandler completionHandler: (NSError?) -> Void) ``` | iOS 7.1 |

Modified [MPPlayableContentManager](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager)

|  | Declaration |
| --- | --- |
| From | ``` class MPPlayableContentManager : NSObject {     weak var dataSource: MPPlayableContentDataSource!     weak var delegate: MPPlayableContentDelegate!     class func sharedContentManager() -> Self!     func reloadData()     func beginUpdates()     func endUpdates() } ``` |
| To | ``` class MPPlayableContentManager : NSObject {     weak var dataSource: MPPlayableContentDataSource?     weak var delegate: MPPlayableContentDelegate?     var context: MPPlayableContentManagerContext { get }     class func sharedContentManager() -> Self     func reloadData()     func beginUpdates()     func endUpdates() } ``` |

Modified [MPPlayableContentManager.dataSource](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614805-datasource)

|  | Declaration |
| --- | --- |
| From | ``` weak var dataSource: MPPlayableContentDataSource! ``` |
| To | ``` weak var dataSource: MPPlayableContentDataSource? ``` |

Modified [MPPlayableContentManager.delegate](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614803-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: MPPlayableContentDelegate! ``` |
| To | ``` weak var delegate: MPPlayableContentDelegate? ``` |

Modified [MPPlayableContentManager.sharedContentManager() -> Self [class]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614806-sharedcontentmanager)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedContentManager() -> Self! ``` |
| To | ``` class func sharedContentManager() -> Self ``` |

Modified [MPRemoteCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommand)

|  | Declaration |
| --- | --- |
| From | ``` class MPRemoteCommand : NSObject {     var enabled: Bool     func addTarget(_ target: AnyObject!, action action: Selector)     func removeTarget(_ target: AnyObject!, action action: Selector)     func removeTarget(_ target: AnyObject!)     func addTargetWithHandler(_ handler: ((MPRemoteCommandEvent!) -> MPRemoteCommandHandlerStatus)!) -> AnyObject! } ``` |
| To | ``` class MPRemoteCommand : NSObject {     var enabled: Bool     func addTarget(_ target: AnyObject, action action: Selector)     func removeTarget(_ target: AnyObject, action action: Selector)     func removeTarget(_ target: AnyObject?)     func addTargetWithHandler(_ handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> AnyObject } ``` |

Modified [MPRemoteCommand.addTarget(_: AnyObject, action: Selector)](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622895-addtarget)

|  | Declaration |
| --- | --- |
| From | ``` func addTarget(_ target: AnyObject!, action action: Selector) ``` |
| To | ``` func addTarget(_ target: AnyObject, action action: Selector) ``` |

Modified [MPRemoteCommand.addTargetWithHandler(_: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> AnyObject](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622910-addtarget)

|  | Declaration |
| --- | --- |
| From | ``` func addTargetWithHandler(_ handler: ((MPRemoteCommandEvent!) -> MPRemoteCommandHandlerStatus)!) -> AnyObject! ``` |
| To | ``` func addTargetWithHandler(_ handler: (MPRemoteCommandEvent) -> MPRemoteCommandHandlerStatus) -> AnyObject ``` |

Modified [MPRemoteCommand.removeTarget(_: AnyObject?)](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622903-removetarget)

|  | Declaration |
| --- | --- |
| From | ``` func removeTarget(_ target: AnyObject!) ``` |
| To | ``` func removeTarget(_ target: AnyObject?) ``` |

Modified [MPRemoteCommand.removeTarget(_: AnyObject, action: Selector)](https://developer.apple.com/documentation/mediaplayer/mpremotecommand/1622896-removetarget)

|  | Declaration |
| --- | --- |
| From | ``` func removeTarget(_ target: AnyObject!, action action: Selector) ``` |
| To | ``` func removeTarget(_ target: AnyObject, action action: Selector) ``` |

Modified [MPRemoteCommandCenter](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter)

|  | Declaration |
| --- | --- |
| From | ``` class MPRemoteCommandCenter : NSObject {     var pauseCommand: MPRemoteCommand! { get }     var playCommand: MPRemoteCommand! { get }     var stopCommand: MPRemoteCommand! { get }     var togglePlayPauseCommand: MPRemoteCommand! { get }     var nextTrackCommand: MPRemoteCommand! { get }     var previousTrackCommand: MPRemoteCommand! { get }     var skipForwardCommand: MPSkipIntervalCommand! { get }     var skipBackwardCommand: MPSkipIntervalCommand! { get }     var seekForwardCommand: MPRemoteCommand! { get }     var seekBackwardCommand: MPRemoteCommand! { get }     var ratingCommand: MPRatingCommand! { get }     var changePlaybackRateCommand: MPChangePlaybackRateCommand! { get }     var likeCommand: MPFeedbackCommand! { get }     var dislikeCommand: MPFeedbackCommand! { get }     var bookmarkCommand: MPFeedbackCommand! { get }     class func sharedCommandCenter() -> MPRemoteCommandCenter! } ``` |
| To | ``` class MPRemoteCommandCenter : NSObject {     var pauseCommand: MPRemoteCommand { get }     var playCommand: MPRemoteCommand { get }     var stopCommand: MPRemoteCommand { get }     var togglePlayPauseCommand: MPRemoteCommand { get }     var enableLanguageOptionCommand: MPRemoteCommand { get }     var disableLanguageOptionCommand: MPRemoteCommand { get }     var nextTrackCommand: MPRemoteCommand { get }     var previousTrackCommand: MPRemoteCommand { get }     var skipForwardCommand: MPSkipIntervalCommand { get }     var skipBackwardCommand: MPSkipIntervalCommand { get }     var seekForwardCommand: MPRemoteCommand { get }     var seekBackwardCommand: MPRemoteCommand { get }     var ratingCommand: MPRatingCommand { get }     var changePlaybackRateCommand: MPChangePlaybackRateCommand { get }     var likeCommand: MPFeedbackCommand { get }     var dislikeCommand: MPFeedbackCommand { get }     var bookmarkCommand: MPFeedbackCommand { get }     class func sharedCommandCenter() -> MPRemoteCommandCenter } ``` |

Modified [MPRemoteCommandCenter.bookmarkCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1619002-bookmarkcommand)

|  | Declaration |
| --- | --- |
| From | ``` var bookmarkCommand: MPFeedbackCommand! { get } ``` |
| To | ``` var bookmarkCommand: MPFeedbackCommand { get } ``` |

Modified [MPRemoteCommandCenter.changePlaybackRateCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618991-changeplaybackratecommand)

|  | Declaration |
| --- | --- |
| From | ``` var changePlaybackRateCommand: MPChangePlaybackRateCommand! { get } ``` |
| To | ``` var changePlaybackRateCommand: MPChangePlaybackRateCommand { get } ``` |

Modified [MPRemoteCommandCenter.dislikeCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618995-dislikecommand)

|  | Declaration |
| --- | --- |
| From | ``` var dislikeCommand: MPFeedbackCommand! { get } ``` |
| To | ``` var dislikeCommand: MPFeedbackCommand { get } ``` |

Modified [MPRemoteCommandCenter.likeCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618998-likecommand)

|  | Declaration |
| --- | --- |
| From | ``` var likeCommand: MPFeedbackCommand! { get } ``` |
| To | ``` var likeCommand: MPFeedbackCommand { get } ``` |

Modified [MPRemoteCommandCenter.nextTrackCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618999-nexttrackcommand)

|  | Declaration |
| --- | --- |
| From | ``` var nextTrackCommand: MPRemoteCommand! { get } ``` |
| To | ``` var nextTrackCommand: MPRemoteCommand { get } ``` |

Modified [MPRemoteCommandCenter.pauseCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618979-pausecommand)

|  | Declaration |
| --- | --- |
| From | ``` var pauseCommand: MPRemoteCommand! { get } ``` |
| To | ``` var pauseCommand: MPRemoteCommand { get } ``` |

Modified [MPRemoteCommandCenter.playCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1619000-playcommand)

|  | Declaration |
| --- | --- |
| From | ``` var playCommand: MPRemoteCommand! { get } ``` |
| To | ``` var playCommand: MPRemoteCommand { get } ``` |

Modified [MPRemoteCommandCenter.previousTrackCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618978-previoustrackcommand)

|  | Declaration |
| --- | --- |
| From | ``` var previousTrackCommand: MPRemoteCommand! { get } ``` |
| To | ``` var previousTrackCommand: MPRemoteCommand { get } ``` |

Modified [MPRemoteCommandCenter.ratingCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618986-ratingcommand)

|  | Declaration |
| --- | --- |
| From | ``` var ratingCommand: MPRatingCommand! { get } ``` |
| To | ``` var ratingCommand: MPRatingCommand { get } ``` |

Modified [MPRemoteCommandCenter.seekBackwardCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618982-seekbackwardcommand)

|  | Declaration |
| --- | --- |
| From | ``` var seekBackwardCommand: MPRemoteCommand! { get } ``` |
| To | ``` var seekBackwardCommand: MPRemoteCommand { get } ``` |

Modified [MPRemoteCommandCenter.seekForwardCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618981-seekforwardcommand)

|  | Declaration |
| --- | --- |
| From | ``` var seekForwardCommand: MPRemoteCommand! { get } ``` |
| To | ``` var seekForwardCommand: MPRemoteCommand { get } ``` |

Modified [MPRemoteCommandCenter.sharedCommandCenter() -> MPRemoteCommandCenter [class]](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618994-sharedcommandcenter)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedCommandCenter() -> MPRemoteCommandCenter! ``` |
| To | ``` class func sharedCommandCenter() -> MPRemoteCommandCenter ``` |

Modified [MPRemoteCommandCenter.skipBackwardCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618996-skipbackwardcommand)

|  | Declaration |
| --- | --- |
| From | ``` var skipBackwardCommand: MPSkipIntervalCommand! { get } ``` |
| To | ``` var skipBackwardCommand: MPSkipIntervalCommand { get } ``` |

Modified [MPRemoteCommandCenter.skipForwardCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618990-skipforwardcommand)

|  | Declaration |
| --- | --- |
| From | ``` var skipForwardCommand: MPSkipIntervalCommand! { get } ``` |
| To | ``` var skipForwardCommand: MPSkipIntervalCommand { get } ``` |

Modified [MPRemoteCommandCenter.stopCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618984-stopcommand)

|  | Declaration |
| --- | --- |
| From | ``` var stopCommand: MPRemoteCommand! { get } ``` |
| To | ``` var stopCommand: MPRemoteCommand { get } ``` |

Modified [MPRemoteCommandCenter.togglePlayPauseCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618992-toggleplaypausecommand)

|  | Declaration |
| --- | --- |
| From | ``` var togglePlayPauseCommand: MPRemoteCommand! { get } ``` |
| To | ``` var togglePlayPauseCommand: MPRemoteCommand { get } ``` |

Modified [MPRemoteCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpremotecommandevent)

|  | Declaration |
| --- | --- |
| From | ``` class MPRemoteCommandEvent : NSObject {     var command: MPRemoteCommand! { get }     var timestamp: NSTimeInterval { get } } ``` |
| To | ``` class MPRemoteCommandEvent : NSObject {     var command: MPRemoteCommand { get }     var timestamp: NSTimeInterval { get } } ``` |

Modified [MPRemoteCommandEvent.command](https://developer.apple.com/documentation/mediaplayer/mpremotecommandevent/1616776-command)

|  | Declaration |
| --- | --- |
| From | ``` var command: MPRemoteCommand! { get } ``` |
| To | ``` var command: MPRemoteCommand { get } ``` |

Modified [MPRemoteCommandHandlerStatus [enum]](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [MPSeekCommandEventType [enum]](https://developer.apple.com/documentation/mediaplayer/mpseekcommandeventtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MPSkipIntervalCommand](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommand)

|  | Declaration |
| --- | --- |
| From | ``` class MPSkipIntervalCommand : MPRemoteCommand {     var preferredIntervals: [AnyObject]! } ``` |
| To | ``` class MPSkipIntervalCommand : MPRemoteCommand {     var preferredIntervals: [AnyObject] } ``` |

Modified [MPSkipIntervalCommand.preferredIntervals](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommand/1622899-preferredintervals)

|  | Declaration |
| --- | --- |
| From | ``` var preferredIntervals: [AnyObject]! ``` |
| To | ``` var preferredIntervals: [AnyObject] ``` |

Modified [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview)

|  | Declaration |
| --- | --- |
| From | ``` class MPVolumeView : UIView, NSCoding {     var showsVolumeSlider: Bool     var showsRouteButton: Bool     var wirelessRoutesAvailable: Bool { get }     var wirelessRouteActive: Bool { get }     func setMinimumVolumeSliderImage(_ image: UIImage!, forState state: UIControlState)     func setMaximumVolumeSliderImage(_ image: UIImage!, forState state: UIControlState)     func setVolumeThumbImage(_ image: UIImage!, forState state: UIControlState)     func minimumVolumeSliderImageForState(_ state: UIControlState) -> UIImage!     func maximumVolumeSliderImageForState(_ state: UIControlState) -> UIImage!     func volumeThumbImageForState(_ state: UIControlState) -> UIImage!     var volumeWarningSliderImage: UIImage!     func volumeSliderRectForBounds(_ bounds: CGRect) -> CGRect     func volumeThumbRectForBounds(_ bounds: CGRect, volumeSliderRect rect: CGRect, value value: Float) -> CGRect     func setRouteButtonImage(_ image: UIImage!, forState state: UIControlState)     func routeButtonImageForState(_ state: UIControlState) -> UIImage!     func routeButtonRectForBounds(_ bounds: CGRect) -> CGRect } ``` |
| To | ``` class MPVolumeView : UIView {     var showsVolumeSlider: Bool     var showsRouteButton: Bool     var wirelessRoutesAvailable: Bool { get }     var wirelessRouteActive: Bool { get }     func setMinimumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState)     func setMaximumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState)     func setVolumeThumbImage(_ image: UIImage?, forState state: UIControlState)     func minimumVolumeSliderImageForState(_ state: UIControlState) -> UIImage?     func maximumVolumeSliderImageForState(_ state: UIControlState) -> UIImage?     func volumeThumbImageForState(_ state: UIControlState) -> UIImage?     var volumeWarningSliderImage: UIImage?     func volumeSliderRectForBounds(_ bounds: CGRect) -> CGRect     func volumeThumbRectForBounds(_ bounds: CGRect, volumeSliderRect rect: CGRect, value value: Float) -> CGRect     func setRouteButtonImage(_ image: UIImage?, forState state: UIControlState)     func routeButtonImageForState(_ state: UIControlState) -> UIImage?     func routeButtonRectForBounds(_ bounds: CGRect) -> CGRect } ``` |

Modified [MPVolumeView.maximumVolumeSliderImageForState(_: UIControlState) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620072-maximumvolumesliderimage)

|  | Declaration |
| --- | --- |
| From | ``` func maximumVolumeSliderImageForState(_ state: UIControlState) -> UIImage! ``` |
| To | ``` func maximumVolumeSliderImageForState(_ state: UIControlState) -> UIImage? ``` |

Modified [MPVolumeView.minimumVolumeSliderImageForState(_: UIControlState) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620076-minimumvolumesliderimage)

|  | Declaration |
| --- | --- |
| From | ``` func minimumVolumeSliderImageForState(_ state: UIControlState) -> UIImage! ``` |
| To | ``` func minimumVolumeSliderImageForState(_ state: UIControlState) -> UIImage? ``` |

Modified [MPVolumeView.routeButtonImageForState(_: UIControlState) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620078-routebuttonimageforstate)

|  | Declaration |
| --- | --- |
| From | ``` func routeButtonImageForState(_ state: UIControlState) -> UIImage! ``` |
| To | ``` func routeButtonImageForState(_ state: UIControlState) -> UIImage? ``` |

Modified [MPVolumeView.setMaximumVolumeSliderImage(_: UIImage?, forState: UIControlState)](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620074-setmaximumvolumesliderimage)

|  | Declaration |
| --- | --- |
| From | ``` func setMaximumVolumeSliderImage(_ image: UIImage!, forState state: UIControlState) ``` |
| To | ``` func setMaximumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState) ``` |

Modified [MPVolumeView.setMinimumVolumeSliderImage(_: UIImage?, forState: UIControlState)](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620063-setminimumvolumesliderimage)

|  | Declaration |
| --- | --- |
| From | ``` func setMinimumVolumeSliderImage(_ image: UIImage!, forState state: UIControlState) ``` |
| To | ``` func setMinimumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState) ``` |

Modified [MPVolumeView.setRouteButtonImage(_: UIImage?, forState: UIControlState)](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620069-setroutebuttonimage)

|  | Declaration |
| --- | --- |
| From | ``` func setRouteButtonImage(_ image: UIImage!, forState state: UIControlState) ``` |
| To | ``` func setRouteButtonImage(_ image: UIImage?, forState state: UIControlState) ``` |

Modified [MPVolumeView.setVolumeThumbImage(_: UIImage?, forState: UIControlState)](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620062-setvolumethumbimage)

|  | Declaration |
| --- | --- |
| From | ``` func setVolumeThumbImage(_ image: UIImage!, forState state: UIControlState) ``` |
| To | ``` func setVolumeThumbImage(_ image: UIImage?, forState state: UIControlState) ``` |

Modified [MPVolumeView.volumeThumbImageForState(_: UIControlState) -> UIImage?](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620064-volumethumbimageforstate)

|  | Declaration |
| --- | --- |
| From | ``` func volumeThumbImageForState(_ state: UIControlState) -> UIImage! ``` |
| To | ``` func volumeThumbImageForState(_ state: UIControlState) -> UIImage? ``` |

Modified [MPVolumeView.volumeWarningSliderImage](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/1620066-volumewarningsliderimage)

|  | Declaration |
| --- | --- |
| From | ``` var volumeWarningSliderImage: UIImage! ``` |
| To | ``` var volumeWarningSliderImage: UIImage? ``` |

Modified [UIViewController.dismissMoviePlayerViewControllerAnimated()](https://developer.apple.com/documentation/uikit/uiviewcontroller/1622345-dismissmovieplayerviewcontroller)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 3.2 | iOS 9.0 |

Modified [UIViewController.presentMoviePlayerViewControllerAnimated(_: MPMoviePlayerViewController!)](https://developer.apple.com/documentation/uikit/uiviewcontroller/1622347-presentmovieplayerviewcontroller)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.1 | -- |
| To | iOS 3.2 | iOS 9.0 |

Modified [MPMediaPlaybackIsPreparedToPlayDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1616250-mpmediaplaybackispreparedtoplayd)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieDurationAvailableNotification](https://developer.apple.com/documentation/mediaplayer/mpmoviedurationavailablenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieMediaTypesAvailableNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620825-mpmoviemediatypesavailable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieNaturalSizeAvailableNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620842-mpmovienaturalsizeavailable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerDidEnterFullscreenNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620816-mpmovieplayerdidenterfullscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerDidExitFullscreenNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620945-mpmovieplayerdidexitfullscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerFullscreenAnimationCurveUserInfoKey](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerfullscreenanimationcurveuserinfokey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerFullscreenAnimationDurationUserInfoKey](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerfullscreenanimationdurationuserinfokey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerisairplayvideoactivedidchangenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerLoadStateDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620909-mpmovieplayerloadstatedidchange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerNowPlayingMovieDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620917-mpmovieplayernowplayingmoviedidc)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerPlaybackDidFinishNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerplaybackdidfinishnotification)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerPlaybackDidFinishReasonUserInfoKey](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerplaybackdidfinishreasonuserinfokey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerPlaybackStateDidChangeNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerplaybackstatedidchangenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerReadyForDisplayDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620783-mpmovieplayerreadyfordisplaydidc)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerScalingModeDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620838-mpmovieplayerscalingmodedidchang)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerThumbnailErrorKey](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerthumbnailerrorkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerThumbnailImageKey](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerthumbnailimagekey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerThumbnailImageRequestDidFinishNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerthumbnailimagerequestdidfinishnotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerThumbnailTimeKey](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerthumbnailtimekey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerTimedMetadataKeyDataType](https://developer.apple.com/documentation/mediaplayer/mpmovieplayertimedmetadatakeydatatype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerTimedMetadataKeyInfo](https://developer.apple.com/documentation/mediaplayer/mpmovieplayertimedmetadatakeyinfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerTimedMetadataKeyLanguageCode](https://developer.apple.com/documentation/mediaplayer/mpmovieplayertimedmetadatakeylanguagecode)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerTimedMetadataKeyMIMEType](https://developer.apple.com/documentation/mediaplayer/mpmovieplayertimedmetadatakeymimetype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerTimedMetadataKeyName](https://developer.apple.com/documentation/mediaplayer/mpmovieplayertimedmetadatakeyname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerTimedMetadataUpdatedNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayertimedmetadataupdatednotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerTimedMetadataUserInfoKey](https://developer.apple.com/documentation/mediaplayer/mpmovieplayertimedmetadatauserinfokey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerWillEnterFullscreenNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerwillenterfullscreennotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerWillExitFullscreenNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerwillexitfullscreennotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieSourceTypeAvailableNotification](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetypeavailablenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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
