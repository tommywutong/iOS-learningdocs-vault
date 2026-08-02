---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/MediaPlayer.html
archived_at: '2026-07-18T02:56:14.544032Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# MediaPlayer Changes

## MediaPlayer

Removed MPMediaEntity.objectForKeyedSubscript(AnyObject!) -> AnyObject!Removed MPMediaPlaylistAttribute.valueRemoved MPMediaType.valueRemoved MPMovieLoadState.valueRemoved MPMovieMediaTypeMask.valueAdded MPMediaPlaylistAttribute.init(rawValue: UInt)Added MPMediaType.init(rawValue: UInt)Added MPMovieLoadState.init(rawValue: UInt)Added MPMovieMediaTypeMask.init(rawValue: UInt)Added UIViewController.dismissMoviePlayerViewControllerAnimated()Added UIViewController.presentMoviePlayerViewControllerAnimated(MPMoviePlayerViewController!)Modified MPChangePlaybackRateCommand

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPChangePlaybackRateCommandEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPContentItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPContentItem.init(identifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier identifier: String!) ``` |
| To | ``` init!(identifier identifier: String!) ``` |

Modified MPFeedbackCommand

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPFeedbackCommandEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPMediaEntity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaEntity.enumerateValuesForProperties(NSSet!, usingBlock:((String!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMediaEntity.persistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaGrouping [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaItem.albumArtist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.albumTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.albumTrackNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.artist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.artwork

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.bookmarkTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.composer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.discNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.genre

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.lastPlayedDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.mediaType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.persistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPMediaItem.persistentIDPropertyForGroupingType(MPMediaGrouping) -> String! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaItem.playCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.playbackDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.podcastTitle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.rating

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.releaseDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.skipCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.title

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaItem.titlePropertyForGroupingType(MPMediaGrouping) -> String! [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaItemArtwork

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaItemArtwork.init(image: UIImage!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(image image: UIImage!) ``` | iOS 8.0 |
| To | ``` init!(image image: UIImage!) ``` | iOS 5.0 |

Modified MPMediaItemCollection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaItemCollection.init(items: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(items items: [AnyObject]!) ``` |
| To | ``` init!(items items: [AnyObject]!) ``` |

Modified MPMediaLibrary

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaPickerController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaPickerController.init(mediaTypes: MPMediaType)

|  | Declaration |
| --- | --- |
| From | ``` init(mediaTypes mediaTypes: MPMediaType) ``` |
| To | ``` init!(mediaTypes mediaTypes: MPMediaType) ``` |

Modified MPMediaPickerController.showsCloudItems

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPMediaPlaylist

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaPlaylist.name

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaPlaylist.persistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaPlaylist.playlistAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaPlaylistAttribute [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct MPMediaPlaylistAttribute : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: MPMediaPlaylistAttribute { get }     static var OnTheGo: MPMediaPlaylistAttribute { get }     static var Smart: MPMediaPlaylistAttribute { get }     static var Genius: MPMediaPlaylistAttribute { get } } ``` | iOS 8.0 |
| To | ``` struct MPMediaPlaylistAttribute : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: MPMediaPlaylistAttribute { get }     static var OnTheGo: MPMediaPlaylistAttribute { get }     static var Smart: MPMediaPlaylistAttribute { get }     static var Genius: MPMediaPlaylistAttribute { get } } ``` | iOS 3.0 |

Modified MPMediaPlaylistAttribute.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified MPMediaPredicate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaPredicateComparison [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaPropertyPredicate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaPropertyPredicate.init(value: AnyObject!, forProperty: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(value value: AnyObject!, forProperty property: String!) -> MPMediaPropertyPredicate ``` |
| To | ``` init!(value value: AnyObject!, forProperty property: String!) -> MPMediaPropertyPredicate ``` |

Modified MPMediaPropertyPredicate.init(value: AnyObject!, forProperty: String!, comparisonType: MPMediaPredicateComparison)

|  | Declaration |
| --- | --- |
| From | ``` init(value value: AnyObject!, forProperty property: String!, comparisonType comparisonType: MPMediaPredicateComparison) -> MPMediaPropertyPredicate ``` |
| To | ``` init!(value value: AnyObject!, forProperty property: String!, comparisonType comparisonType: MPMediaPredicateComparison) -> MPMediaPropertyPredicate ``` |

Modified MPMediaQuery

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMediaQuery.collectionSections

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaQuery.init(filterPredicates: NSSet!)

|  | Declaration |
| --- | --- |
| From | ``` init(filterPredicates filterPredicates: NSSet!) ``` |
| To | ``` init!(filterPredicates filterPredicates: NSSet!) ``` |

Modified MPMediaQuery.itemSections

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaQuerySection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaType [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct MPMediaType : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Music: MPMediaType { get }     static var Podcast: MPMediaType { get }     static var AudioBook: MPMediaType { get }     static var AudioITunesU: MPMediaType { get }     static var AnyAudio: MPMediaType { get }     static var Movie: MPMediaType { get }     static var TVShow: MPMediaType { get }     static var VideoPodcast: MPMediaType { get }     static var MusicVideo: MPMediaType { get }     static var VideoITunesU: MPMediaType { get }     static var HomeVideo: MPMediaType { get }     static var AnyVideo: MPMediaType { get }     static var Any: MPMediaType { get } } ``` | iOS 8.0 |
| To | ``` struct MPMediaType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Music: MPMediaType { get }     static var Podcast: MPMediaType { get }     static var AudioBook: MPMediaType { get }     static var AudioITunesU: MPMediaType { get }     static var AnyAudio: MPMediaType { get }     static var Movie: MPMediaType { get }     static var TVShow: MPMediaType { get }     static var VideoPodcast: MPMediaType { get }     static var MusicVideo: MPMediaType { get }     static var VideoITunesU: MPMediaType { get }     static var HomeVideo: MPMediaType { get }     static var AnyVideo: MPMediaType { get }     static var Any: MPMediaType { get } } ``` | iOS 3.0 |

Modified MPMediaType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified MPMovieAccessLog

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified MPMovieAccessLogEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified MPMovieErrorLog

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified MPMovieErrorLogEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified MPMovieLoadState [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MPMovieLoadState : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Unknown: MPMovieLoadState { get }     static var Playable: MPMovieLoadState { get }     static var PlaythroughOK: MPMovieLoadState { get }     static var Stalled: MPMovieLoadState { get } } ``` |
| To | ``` struct MPMovieLoadState : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Unknown: MPMovieLoadState { get }     static var Playable: MPMovieLoadState { get }     static var PlaythroughOK: MPMovieLoadState { get }     static var Stalled: MPMovieLoadState { get } } ``` |

Modified MPMovieLoadState.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified MPMovieMediaTypeMask [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MPMovieMediaTypeMask : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var None: MPMovieMediaTypeMask { get }     static var Video: MPMovieMediaTypeMask { get }     static var Audio: MPMovieMediaTypeMask { get } } ``` |
| To | ``` struct MPMovieMediaTypeMask : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: MPMovieMediaTypeMask { get }     static var Video: MPMovieMediaTypeMask { get }     static var Audio: MPMovieMediaTypeMask { get } } ``` |

Modified MPMovieMediaTypeMask.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified MPMoviePlayerController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified MPMoviePlayerController.accessLog

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified MPMoviePlayerController.airPlayVideoActive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPMoviePlayerController.allowsAirPlay

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified MPMoviePlayerController.cancelAllThumbnailImageRequests()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerController.init(contentURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(contentURL url: NSURL!) ``` |
| To | ``` init!(contentURL url: NSURL!) ``` |

Modified MPMoviePlayerController.errorLog

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified MPMoviePlayerController.readyForDisplay

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPMoviePlayerController.requestThumbnailImagesAtTimes([AnyObject]!, timeOption: MPMovieTimeOption)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerController.timedMetadata

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMoviePlayerViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerViewController.init(contentURL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(contentURL contentURL: NSURL!) ``` |
| To | ``` init!(contentURL contentURL: NSURL!) ``` |

Modified MPMusicPlayerController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MPMusicPlayerController.iPodMusicPlayer() -> MPMusicPlayerController! [class]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 3.0 | iOS 8.0 |

Modified MPMusicPlayerController.indexOfNowPlayingItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPNowPlayingInfoCenter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPPlayableContentManager

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPRatingCommand

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPRatingCommandEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPRemoteCommand

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPRemoteCommandCenter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPRemoteCommandEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPRemoteCommandHandlerStatus [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPSeekCommandEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPSeekCommandEventType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPSkipIntervalCommand

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPSkipIntervalCommandEvent

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MPTimedMetadata

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPVolumeView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified MPVolumeView.maximumVolumeSliderImageForState(UIControlState) -> UIImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.minimumVolumeSliderImageForState(UIControlState) -> UIImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.routeButtonImageForState(UIControlState) -> UIImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.routeButtonRectForBounds(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.setMaximumVolumeSliderImage(UIImage!, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.setMinimumVolumeSliderImage(UIImage!, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.setRouteButtonImage(UIImage!, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.setVolumeThumbImage(UIImage!, forState: UIControlState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.showsRouteButton

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPVolumeView.showsVolumeSlider

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPVolumeView.volumeSliderRectForBounds(CGRect) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.volumeThumbImageForState(UIControlState) -> UIImage!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.volumeThumbRectForBounds(CGRect, volumeSliderRect: CGRect, value: Float) -> CGRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPVolumeView.volumeWarningSliderImage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPVolumeView.wirelessRouteActive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPVolumeView.wirelessRoutesAvailable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaEntityPropertyPersistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaItemPropertyAlbumArtistPersistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaItemPropertyAlbumPersistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaItemPropertyArtistPersistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaItemPropertyAssetURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMediaItemPropertyBeatsPerMinute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMediaItemPropertyBookmarkTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPMediaItemPropertyComments

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMediaItemPropertyComposerPersistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaItemPropertyGenrePersistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaItemPropertyIsCloudItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPMediaItemPropertyPersistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaItemPropertyPodcastPersistentID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MPMediaItemPropertyReleaseDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMediaItemPropertyUserGrouping

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMediaPlaybackIsPreparedToPlayDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMovieDurationAvailableNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMovieMediaTypesAvailableNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMovieNaturalSizeAvailableNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerDidEnterFullscreenNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerDidExitFullscreenNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerFullscreenAnimationCurveUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerFullscreenAnimationDurationUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPMoviePlayerLoadStateDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerNowPlayingMovieDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerPlaybackDidFinishReasonUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerPlaybackStateDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerReadyForDisplayDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MPMoviePlayerThumbnailErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerThumbnailImageKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerThumbnailImageRequestDidFinishNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerThumbnailTimeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerTimedMetadataKeyDataType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMoviePlayerTimedMetadataKeyInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMoviePlayerTimedMetadataKeyLanguageCode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMoviePlayerTimedMetadataKeyMIMEType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMoviePlayerTimedMetadataKeyName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMoviePlayerTimedMetadataUpdatedNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMoviePlayerTimedMetadataUserInfoKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MPMoviePlayerWillEnterFullscreenNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMoviePlayerWillExitFullscreenNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPMovieSourceTypeAvailableNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified MPNowPlayingInfoPropertyChapterCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPNowPlayingInfoPropertyChapterNumber

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPNowPlayingInfoPropertyElapsedPlaybackTime

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPNowPlayingInfoPropertyPlaybackQueueCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPNowPlayingInfoPropertyPlaybackQueueIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPNowPlayingInfoPropertyPlaybackRate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPVolumeViewWirelessRouteActiveDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPVolumeViewWirelessRoutesAvailableDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

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
