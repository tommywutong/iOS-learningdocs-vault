---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/MediaPlayer.html
archived_at: '2026-07-18T02:57:09.335667Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# MediaPlayer Changes for Swift

### MediaPlayer

Added [MPChangePlaybackPositionCommand](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackpositioncommand)Added [MPChangePlaybackPositionCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackpositioncommandevent)Added [MPChangePlaybackPositionCommandEvent.positionTime](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackpositioncommandevent/1616766-positiontime)Added [MPNowPlayingInfoLanguageOption.isAutomaticAudibleLanguageOption() -> Bool](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623151-isautomaticaudiblelanguageoption)Added [MPRemoteCommandCenter.changePlaybackPositionCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618997-changeplaybackpositioncommand)Added [MPRemoteCommandHandlerStatus.NoActionableNowPlayingItem](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus/mpremotecommandhandlerstatusnoactionablenowplayingitem)Modified [MPChangeLanguageOptionCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPChangePlaybackRateCommand](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommand)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPChangePlaybackRateCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommandevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPContentItem](https://developer.apple.com/documentation/mediaplayer/mpcontentitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPFeedbackCommand](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommand)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPFeedbackCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommandevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPMediaEntity](https://developer.apple.com/documentation/mediaplayer/mpmediaentity)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaEntity : NSObject, NSSecureCoding, NSCoding {     class func canFilterByProperty(_ property: String) -> Bool     func enumerateValuesForProperties(_ properties: Set<String>, usingBlock block: (String, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     subscript (_ key: AnyObject) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: AnyObject) -> AnyObject?     func valueForProperty(_ property: String) -> AnyObject?     var persistentID: MPMediaEntityPersistentID { get } } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class MPMediaEntity : NSObject, NSSecureCoding {     class func canFilterByProperty(_ property: String) -> Bool     func enumerateValuesForProperties(_ properties: Set<String>, usingBlock block: (String, AnyObject, UnsafeMutablePointer<ObjCBool>) -> Void)     subscript (_ key: AnyObject) -> AnyObject? { get }     func objectForKeyedSubscript(_ key: AnyObject) -> AnyObject?     func valueForProperty(_ property: String) -> AnyObject?     var persistentID: MPMediaEntityPersistentID { get } } ``` | NSSecureCoding |

Modified [MPMediaGrouping [enum]](https://developer.apple.com/documentation/mediaplayer/mpmediagrouping)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMediaItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPMediaItemArtwork](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPMediaItemCollection](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPMediaLibrary](https://developer.apple.com/documentation/mediaplayer/mpmedialibrary)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaLibrary : NSObject, NSSecureCoding, NSCoding {     class func defaultMediaLibrary() -> MPMediaLibrary     var lastModifiedDate: NSDate { get }     func beginGeneratingLibraryChangeNotifications()     func endGeneratingLibraryChangeNotifications() } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class MPMediaLibrary : NSObject, NSSecureCoding {     class func defaultMediaLibrary() -> MPMediaLibrary     var lastModifiedDate: NSDate { get }     func beginGeneratingLibraryChangeNotifications()     func endGeneratingLibraryChangeNotifications() } ``` | NSSecureCoding |

Modified [MPMediaPickerController](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPMediaPlaylist](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPMediaPredicate](https://developer.apple.com/documentation/mediaplayer/mpmediapredicate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaPredicate : NSObject, NSSecureCoding, NSCoding { } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class MPMediaPredicate : NSObject, NSSecureCoding { } ``` | NSSecureCoding |

Modified [MPMediaPredicateComparison [enum]](https://developer.apple.com/documentation/mediaplayer/mpmediapredicatecomparison)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMediaPropertyPredicate](https://developer.apple.com/documentation/mediaplayer/mpmediapropertypredicate)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPMediaQuery](https://developer.apple.com/documentation/mediaplayer/mpmediaquery)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaQuery : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(filterPredicates filterPredicates: Set<MPMediaPredicate>?)     var filterPredicates: Set<MPMediaPredicate>?     func addFilterPredicate(_ predicate: MPMediaPredicate)     func removeFilterPredicate(_ predicate: MPMediaPredicate)     var items: [MPMediaItem]? { get }     var collections: [MPMediaItemCollection]? { get }     var groupingType: MPMediaGrouping     var itemSections: [MPMediaQuerySection]? { get }     var collectionSections: [MPMediaQuerySection]? { get }     class func albumsQuery() -> MPMediaQuery     class func artistsQuery() -> MPMediaQuery     class func songsQuery() -> MPMediaQuery     class func playlistsQuery() -> MPMediaQuery     class func podcastsQuery() -> MPMediaQuery     class func audiobooksQuery() -> MPMediaQuery     class func compilationsQuery() -> MPMediaQuery     class func composersQuery() -> MPMediaQuery     class func genresQuery() -> MPMediaQuery } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class MPMediaQuery : NSObject, NSSecureCoding, NSCopying {     init(filterPredicates filterPredicates: Set<MPMediaPredicate>?)     var filterPredicates: Set<MPMediaPredicate>?     func addFilterPredicate(_ predicate: MPMediaPredicate)     func removeFilterPredicate(_ predicate: MPMediaPredicate)     var items: [MPMediaItem]? { get }     var collections: [MPMediaItemCollection]? { get }     var groupingType: MPMediaGrouping     var itemSections: [MPMediaQuerySection]? { get }     var collectionSections: [MPMediaQuerySection]? { get }     class func albumsQuery() -> MPMediaQuery     class func artistsQuery() -> MPMediaQuery     class func songsQuery() -> MPMediaQuery     class func playlistsQuery() -> MPMediaQuery     class func podcastsQuery() -> MPMediaQuery     class func audiobooksQuery() -> MPMediaQuery     class func compilationsQuery() -> MPMediaQuery     class func composersQuery() -> MPMediaQuery     class func genresQuery() -> MPMediaQuery } ``` | NSCopying, NSSecureCoding |

Modified [MPMediaQuerySection](https://developer.apple.com/documentation/mediaplayer/mpmediaquerysection)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPMediaQuerySection : NSObject, NSSecureCoding, NSCoding, NSCopying {     var title: String { get }     var range: NSRange { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class MPMediaQuerySection : NSObject, NSSecureCoding, NSCopying {     var title: String { get }     var range: NSRange { get } } ``` | NSCopying, NSSecureCoding |

Modified [MPMovieAccessLog](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MPMovieAccessLogEvent](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MPMovieControlStyle [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMovieErrorLog](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MPMovieErrorLogEvent](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MPMovieFinishReason [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviefinishreason)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMoviePlaybackState [enum]](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMoviePlayerController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject, MPMediaPlayback |
| To | MPMediaPlayback |

Modified [MPMoviePlayerViewController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPMovieRepeatMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmovierepeatmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMovieScalingMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMovieSourceType [enum]](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMovieTimeOption [enum]](https://developer.apple.com/documentation/mediaplayer/mpmovietimeoption)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMusicPlaybackState [enum]](https://developer.apple.com/documentation/mediaplayer/mpmusicplaybackstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMusicPlayerController](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject, MPMediaPlayback |
| To | MPMediaPlayback |

Modified [MPMusicRepeatMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmusicrepeatmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPMusicShuffleMode [enum]](https://developer.apple.com/documentation/mediaplayer/mpmusicshufflemode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPNowPlayingInfoCenter](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPNowPlayingInfoLanguageOption](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPNowPlayingInfoLanguageOption : NSObject {     init(type languageOptionType: MPNowPlayingInfoLanguageOptionType, languageTag languageTag: String, characteristics languageOptionCharacteristics: [String]?, displayName displayName: String, identifier identifier: String)     func isAutomaticLegibleLanguageOption() -> Bool     var languageOptionType: MPNowPlayingInfoLanguageOptionType { get }     var languageTag: String? { get }     var languageOptionCharacteristics: [String]? { get }     var displayName: String? { get }     var identifier: String? { get } } ``` | AnyObject |
| To | ``` class MPNowPlayingInfoLanguageOption : NSObject {     init(type languageOptionType: MPNowPlayingInfoLanguageOptionType, languageTag languageTag: String, characteristics languageOptionCharacteristics: [String]?, displayName displayName: String, identifier identifier: String)     func isAutomaticLegibleLanguageOption() -> Bool     func isAutomaticAudibleLanguageOption() -> Bool     var languageOptionType: MPNowPlayingInfoLanguageOptionType { get }     var languageTag: String? { get }     var languageOptionCharacteristics: [String]? { get }     var displayName: String? { get }     var identifier: String? { get } } ``` | -- |

Modified [MPNowPlayingInfoLanguageOptionGroup](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPNowPlayingInfoLanguageOptionType [enum]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPPlayableContentDelegate.playableContentManager(_: MPPlayableContentManager, didUpdateContext: MPPlayableContentManagerContext)](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620291-playablecontentmanager)

|  | Introduction |
| --- | --- |
| From | iOS 9.0 |
| To | iOS 8.4 |

Modified [MPPlayableContentManager](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPPlayableContentManagerContext](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPRatingCommand](https://developer.apple.com/documentation/mediaplayer/mpratingcommand)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPRatingCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpratingcommandevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPRemoteCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommand)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPRemoteCommandCenter](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPRemoteCommandCenter : NSObject {     var pauseCommand: MPRemoteCommand { get }     var playCommand: MPRemoteCommand { get }     var stopCommand: MPRemoteCommand { get }     var togglePlayPauseCommand: MPRemoteCommand { get }     var enableLanguageOptionCommand: MPRemoteCommand { get }     var disableLanguageOptionCommand: MPRemoteCommand { get }     var nextTrackCommand: MPRemoteCommand { get }     var previousTrackCommand: MPRemoteCommand { get }     var skipForwardCommand: MPSkipIntervalCommand { get }     var skipBackwardCommand: MPSkipIntervalCommand { get }     var seekForwardCommand: MPRemoteCommand { get }     var seekBackwardCommand: MPRemoteCommand { get }     var ratingCommand: MPRatingCommand { get }     var changePlaybackRateCommand: MPChangePlaybackRateCommand { get }     var likeCommand: MPFeedbackCommand { get }     var dislikeCommand: MPFeedbackCommand { get }     var bookmarkCommand: MPFeedbackCommand { get }     class func sharedCommandCenter() -> MPRemoteCommandCenter } ``` | AnyObject |
| To | ``` class MPRemoteCommandCenter : NSObject {     var pauseCommand: MPRemoteCommand { get }     var playCommand: MPRemoteCommand { get }     var stopCommand: MPRemoteCommand { get }     var togglePlayPauseCommand: MPRemoteCommand { get }     var enableLanguageOptionCommand: MPRemoteCommand { get }     var disableLanguageOptionCommand: MPRemoteCommand { get }     var nextTrackCommand: MPRemoteCommand { get }     var previousTrackCommand: MPRemoteCommand { get }     var skipForwardCommand: MPSkipIntervalCommand { get }     var skipBackwardCommand: MPSkipIntervalCommand { get }     var seekForwardCommand: MPRemoteCommand { get }     var seekBackwardCommand: MPRemoteCommand { get }     var ratingCommand: MPRatingCommand { get }     var changePlaybackRateCommand: MPChangePlaybackRateCommand { get }     var likeCommand: MPFeedbackCommand { get }     var dislikeCommand: MPFeedbackCommand { get }     var bookmarkCommand: MPFeedbackCommand { get }     var changePlaybackPositionCommand: MPChangePlaybackPositionCommand { get }     class func sharedCommandCenter() -> MPRemoteCommandCenter } ``` | -- |

Modified [MPRemoteCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpremotecommandevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPRemoteCommandHandlerStatus [enum]](https://developer.apple.com/documentation/mediaplayer/mpremotecommandhandlerstatus)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum MPRemoteCommandHandlerStatus : Int {     case Success     case NoSuchContent     case CommandFailed } ``` | Equatable, Hashable, RawRepresentable |
| To | ``` enum MPRemoteCommandHandlerStatus : Int {     case Success     case NoSuchContent     case NoActionableNowPlayingItem     case CommandFailed } ``` | -- |

Modified [MPSeekCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpseekcommandevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPSeekCommandEventType [enum]](https://developer.apple.com/documentation/mediaplayer/mpseekcommandeventtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPSkipIntervalCommand](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommand)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPSkipIntervalCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpskipintervalcommandevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPTimedMetadata](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MPVolumeView](https://developer.apple.com/documentation/mediaplayer/mpvolumeview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MPVolumeView : UIView {     var showsVolumeSlider: Bool     var showsRouteButton: Bool     var wirelessRoutesAvailable: Bool { get }     var wirelessRouteActive: Bool { get }     func setMinimumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState)     func setMaximumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState)     func setVolumeThumbImage(_ image: UIImage?, forState state: UIControlState)     func minimumVolumeSliderImageForState(_ state: UIControlState) -> UIImage?     func maximumVolumeSliderImageForState(_ state: UIControlState) -> UIImage?     func volumeThumbImageForState(_ state: UIControlState) -> UIImage?     var volumeWarningSliderImage: UIImage?     func volumeSliderRectForBounds(_ bounds: CGRect) -> CGRect     func volumeThumbRectForBounds(_ bounds: CGRect, volumeSliderRect rect: CGRect, value value: Float) -> CGRect     func setRouteButtonImage(_ image: UIImage?, forState state: UIControlState)     func routeButtonImageForState(_ state: UIControlState) -> UIImage?     func routeButtonRectForBounds(_ bounds: CGRect) -> CGRect } ``` | AnyObject, NSCoding |
| To | ``` class MPVolumeView : UIView, NSCoding {     var showsVolumeSlider: Bool     var showsRouteButton: Bool     var wirelessRoutesAvailable: Bool { get }     var wirelessRouteActive: Bool { get }     func setMinimumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState)     func setMaximumVolumeSliderImage(_ image: UIImage?, forState state: UIControlState)     func setVolumeThumbImage(_ image: UIImage?, forState state: UIControlState)     func minimumVolumeSliderImageForState(_ state: UIControlState) -> UIImage?     func maximumVolumeSliderImageForState(_ state: UIControlState) -> UIImage?     func volumeThumbImageForState(_ state: UIControlState) -> UIImage?     var volumeWarningSliderImage: UIImage?     func volumeSliderRectForBounds(_ bounds: CGRect) -> CGRect     func volumeThumbRectForBounds(_ bounds: CGRect, volumeSliderRect rect: CGRect, value value: Float) -> CGRect     func setRouteButtonImage(_ image: UIImage?, forState state: UIControlState)     func routeButtonImageForState(_ state: UIControlState) -> UIImage?     func routeButtonRectForBounds(_ bounds: CGRect) -> CGRect } ``` | NSCoding |

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
