---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/MediaPlayer.html
archived_at: '2026-07-18T02:56:26.705464Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# MediaPlayer Changes

## MediaPlayer

Modified MPMediaEntity.enumerateValuesForProperties(Set<NSObject>!, usingBlock:((String!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)!)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateValuesForProperties(_ properties: NSSet!, usingBlock block: ((String!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateValuesForProperties(_ properties: Set<NSObject>!, usingBlock block: ((String!, AnyObject!, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |

Modified MPMediaQuery.filterPredicates

|  | Declaration |
| --- | --- |
| From | ``` var filterPredicates: NSSet! ``` |
| To | ``` var filterPredicates: Set<NSObject>! ``` |

Modified MPMediaQuery.init(filterPredicates: Set<NSObject>!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init!(filterPredicates filterPredicates: NSSet!) ``` | iOS 8.0 |
| To | ``` init!(filterPredicates filterPredicates: Set<NSObject>!) ``` | iOS 8.3 |

Modified MPMediaType.AnyVideo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPMediaType.AudioITunesU

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPMediaType.HomeVideo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MPMediaType.Movie

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPMediaType.MusicVideo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPMediaType.TVShow

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPMediaType.VideoITunesU

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPMediaType.VideoPodcast

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MPMediaEntityPropertyPersistentID

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaEntityPropertyPersistentID: NSString! ``` |
| To | ``` let MPMediaEntityPropertyPersistentID: String ``` |

Modified MPMediaItemPropertyAlbumArtist

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyAlbumArtist: NSString! ``` |
| To | ``` let MPMediaItemPropertyAlbumArtist: String ``` |

Modified MPMediaItemPropertyAlbumArtistPersistentID

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyAlbumArtistPersistentID: NSString! ``` |
| To | ``` let MPMediaItemPropertyAlbumArtistPersistentID: String ``` |

Modified MPMediaItemPropertyAlbumPersistentID

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyAlbumPersistentID: NSString! ``` |
| To | ``` let MPMediaItemPropertyAlbumPersistentID: String ``` |

Modified MPMediaItemPropertyAlbumTitle

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyAlbumTitle: NSString! ``` |
| To | ``` let MPMediaItemPropertyAlbumTitle: String ``` |

Modified MPMediaItemPropertyAlbumTrackCount

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyAlbumTrackCount: NSString! ``` |
| To | ``` let MPMediaItemPropertyAlbumTrackCount: String ``` |

Modified MPMediaItemPropertyAlbumTrackNumber

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyAlbumTrackNumber: NSString! ``` |
| To | ``` let MPMediaItemPropertyAlbumTrackNumber: String ``` |

Modified MPMediaItemPropertyArtist

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyArtist: NSString! ``` |
| To | ``` let MPMediaItemPropertyArtist: String ``` |

Modified MPMediaItemPropertyArtistPersistentID

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyArtistPersistentID: NSString! ``` |
| To | ``` let MPMediaItemPropertyArtistPersistentID: String ``` |

Modified MPMediaItemPropertyArtwork

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyArtwork: NSString! ``` |
| To | ``` let MPMediaItemPropertyArtwork: String ``` |

Modified MPMediaItemPropertyAssetURL

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyAssetURL: NSString! ``` |
| To | ``` let MPMediaItemPropertyAssetURL: String ``` |

Modified MPMediaItemPropertyBeatsPerMinute

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyBeatsPerMinute: NSString! ``` |
| To | ``` let MPMediaItemPropertyBeatsPerMinute: String ``` |

Modified MPMediaItemPropertyBookmarkTime

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyBookmarkTime: NSString! ``` |
| To | ``` let MPMediaItemPropertyBookmarkTime: String ``` |

Modified MPMediaItemPropertyComments

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyComments: NSString! ``` |
| To | ``` let MPMediaItemPropertyComments: String ``` |

Modified MPMediaItemPropertyComposer

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyComposer: NSString! ``` |
| To | ``` let MPMediaItemPropertyComposer: String ``` |

Modified MPMediaItemPropertyComposerPersistentID

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyComposerPersistentID: NSString! ``` |
| To | ``` let MPMediaItemPropertyComposerPersistentID: String ``` |

Modified MPMediaItemPropertyDiscCount

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyDiscCount: NSString! ``` |
| To | ``` let MPMediaItemPropertyDiscCount: String ``` |

Modified MPMediaItemPropertyDiscNumber

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyDiscNumber: NSString! ``` |
| To | ``` let MPMediaItemPropertyDiscNumber: String ``` |

Modified MPMediaItemPropertyGenre

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyGenre: NSString! ``` |
| To | ``` let MPMediaItemPropertyGenre: String ``` |

Modified MPMediaItemPropertyGenrePersistentID

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyGenrePersistentID: NSString! ``` |
| To | ``` let MPMediaItemPropertyGenrePersistentID: String ``` |

Modified MPMediaItemPropertyIsCloudItem

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyIsCloudItem: NSString! ``` |
| To | ``` let MPMediaItemPropertyIsCloudItem: String ``` |

Modified MPMediaItemPropertyIsCompilation

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyIsCompilation: NSString! ``` |
| To | ``` let MPMediaItemPropertyIsCompilation: String ``` |

Modified MPMediaItemPropertyLastPlayedDate

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyLastPlayedDate: NSString! ``` |
| To | ``` let MPMediaItemPropertyLastPlayedDate: String ``` |

Modified MPMediaItemPropertyLyrics

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyLyrics: NSString! ``` |
| To | ``` let MPMediaItemPropertyLyrics: String ``` |

Modified MPMediaItemPropertyMediaType

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyMediaType: NSString! ``` |
| To | ``` let MPMediaItemPropertyMediaType: String ``` |

Modified MPMediaItemPropertyPersistentID

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyPersistentID: NSString! ``` |
| To | ``` let MPMediaItemPropertyPersistentID: String ``` |

Modified MPMediaItemPropertyPlayCount

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyPlayCount: NSString! ``` |
| To | ``` let MPMediaItemPropertyPlayCount: String ``` |

Modified MPMediaItemPropertyPlaybackDuration

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyPlaybackDuration: NSString! ``` |
| To | ``` let MPMediaItemPropertyPlaybackDuration: String ``` |

Modified MPMediaItemPropertyPodcastPersistentID

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyPodcastPersistentID: NSString! ``` |
| To | ``` let MPMediaItemPropertyPodcastPersistentID: String ``` |

Modified MPMediaItemPropertyPodcastTitle

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyPodcastTitle: NSString! ``` |
| To | ``` let MPMediaItemPropertyPodcastTitle: String ``` |

Modified MPMediaItemPropertyRating

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyRating: NSString! ``` |
| To | ``` let MPMediaItemPropertyRating: String ``` |

Modified MPMediaItemPropertyReleaseDate

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyReleaseDate: NSString! ``` |
| To | ``` let MPMediaItemPropertyReleaseDate: String ``` |

Modified MPMediaItemPropertySkipCount

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertySkipCount: NSString! ``` |
| To | ``` let MPMediaItemPropertySkipCount: String ``` |

Modified MPMediaItemPropertyTitle

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyTitle: NSString! ``` |
| To | ``` let MPMediaItemPropertyTitle: String ``` |

Modified MPMediaItemPropertyUserGrouping

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaItemPropertyUserGrouping: NSString! ``` |
| To | ``` let MPMediaItemPropertyUserGrouping: String ``` |

Modified MPMediaLibraryDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaLibraryDidChangeNotification: NSString! ``` |
| To | ``` let MPMediaLibraryDidChangeNotification: String ``` |

Modified MPMediaPlaybackIsPreparedToPlayDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaPlaybackIsPreparedToPlayDidChangeNotification: NSString! ``` |
| To | ``` let MPMediaPlaybackIsPreparedToPlayDidChangeNotification: String ``` |

Modified MPMediaPlaylistPropertyName

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaPlaylistPropertyName: NSString! ``` |
| To | ``` let MPMediaPlaylistPropertyName: String ``` |

Modified MPMediaPlaylistPropertyPersistentID

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaPlaylistPropertyPersistentID: NSString! ``` |
| To | ``` let MPMediaPlaylistPropertyPersistentID: String ``` |

Modified MPMediaPlaylistPropertyPlaylistAttributes

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaPlaylistPropertyPlaylistAttributes: NSString! ``` |
| To | ``` let MPMediaPlaylistPropertyPlaylistAttributes: String ``` |

Modified MPMediaPlaylistPropertySeedItems

|  | Declaration |
| --- | --- |
| From | ``` let MPMediaPlaylistPropertySeedItems: NSString! ``` |
| To | ``` let MPMediaPlaylistPropertySeedItems: String ``` |

Modified MPMovieDurationAvailableNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMovieDurationAvailableNotification: NSString! ``` |
| To | ``` let MPMovieDurationAvailableNotification: String ``` |

Modified MPMovieMediaTypesAvailableNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMovieMediaTypesAvailableNotification: NSString! ``` |
| To | ``` let MPMovieMediaTypesAvailableNotification: String ``` |

Modified MPMovieNaturalSizeAvailableNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMovieNaturalSizeAvailableNotification: NSString! ``` |
| To | ``` let MPMovieNaturalSizeAvailableNotification: String ``` |

Modified MPMoviePlayerDidEnterFullscreenNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerDidEnterFullscreenNotification: NSString! ``` |
| To | ``` let MPMoviePlayerDidEnterFullscreenNotification: String ``` |

Modified MPMoviePlayerDidExitFullscreenNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerDidExitFullscreenNotification: NSString! ``` |
| To | ``` let MPMoviePlayerDidExitFullscreenNotification: String ``` |

Modified MPMoviePlayerFullscreenAnimationCurveUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerFullscreenAnimationCurveUserInfoKey: NSString! ``` |
| To | ``` let MPMoviePlayerFullscreenAnimationCurveUserInfoKey: String ``` |

Modified MPMoviePlayerFullscreenAnimationDurationUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerFullscreenAnimationDurationUserInfoKey: NSString! ``` |
| To | ``` let MPMoviePlayerFullscreenAnimationDurationUserInfoKey: String ``` |

Modified MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification: NSString! ``` |
| To | ``` let MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification: String ``` |

Modified MPMoviePlayerLoadStateDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerLoadStateDidChangeNotification: NSString! ``` |
| To | ``` let MPMoviePlayerLoadStateDidChangeNotification: String ``` |

Modified MPMoviePlayerNowPlayingMovieDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerNowPlayingMovieDidChangeNotification: NSString! ``` |
| To | ``` let MPMoviePlayerNowPlayingMovieDidChangeNotification: String ``` |

Modified MPMoviePlayerPlaybackDidFinishNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerPlaybackDidFinishNotification: NSString! ``` |
| To | ``` let MPMoviePlayerPlaybackDidFinishNotification: String ``` |

Modified MPMoviePlayerPlaybackDidFinishReasonUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerPlaybackDidFinishReasonUserInfoKey: NSString! ``` |
| To | ``` let MPMoviePlayerPlaybackDidFinishReasonUserInfoKey: String ``` |

Modified MPMoviePlayerPlaybackStateDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerPlaybackStateDidChangeNotification: NSString! ``` |
| To | ``` let MPMoviePlayerPlaybackStateDidChangeNotification: String ``` |

Modified MPMoviePlayerReadyForDisplayDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerReadyForDisplayDidChangeNotification: NSString! ``` |
| To | ``` let MPMoviePlayerReadyForDisplayDidChangeNotification: String ``` |

Modified MPMoviePlayerScalingModeDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerScalingModeDidChangeNotification: NSString! ``` |
| To | ``` let MPMoviePlayerScalingModeDidChangeNotification: String ``` |

Modified MPMoviePlayerThumbnailErrorKey

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerThumbnailErrorKey: NSString! ``` |
| To | ``` let MPMoviePlayerThumbnailErrorKey: String ``` |

Modified MPMoviePlayerThumbnailImageKey

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerThumbnailImageKey: NSString! ``` |
| To | ``` let MPMoviePlayerThumbnailImageKey: String ``` |

Modified MPMoviePlayerThumbnailImageRequestDidFinishNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerThumbnailImageRequestDidFinishNotification: NSString! ``` |
| To | ``` let MPMoviePlayerThumbnailImageRequestDidFinishNotification: String ``` |

Modified MPMoviePlayerThumbnailTimeKey

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerThumbnailTimeKey: NSString! ``` |
| To | ``` let MPMoviePlayerThumbnailTimeKey: String ``` |

Modified MPMoviePlayerTimedMetadataKeyDataType

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerTimedMetadataKeyDataType: NSString! ``` |
| To | ``` let MPMoviePlayerTimedMetadataKeyDataType: String ``` |

Modified MPMoviePlayerTimedMetadataKeyInfo

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerTimedMetadataKeyInfo: NSString! ``` |
| To | ``` let MPMoviePlayerTimedMetadataKeyInfo: String ``` |

Modified MPMoviePlayerTimedMetadataKeyLanguageCode

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerTimedMetadataKeyLanguageCode: NSString! ``` |
| To | ``` let MPMoviePlayerTimedMetadataKeyLanguageCode: String ``` |

Modified MPMoviePlayerTimedMetadataKeyMIMEType

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerTimedMetadataKeyMIMEType: NSString! ``` |
| To | ``` let MPMoviePlayerTimedMetadataKeyMIMEType: String ``` |

Modified MPMoviePlayerTimedMetadataKeyName

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerTimedMetadataKeyName: NSString! ``` |
| To | ``` let MPMoviePlayerTimedMetadataKeyName: String ``` |

Modified MPMoviePlayerTimedMetadataUpdatedNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerTimedMetadataUpdatedNotification: NSString! ``` |
| To | ``` let MPMoviePlayerTimedMetadataUpdatedNotification: String ``` |

Modified MPMoviePlayerTimedMetadataUserInfoKey

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerTimedMetadataUserInfoKey: NSString! ``` |
| To | ``` let MPMoviePlayerTimedMetadataUserInfoKey: String ``` |

Modified MPMoviePlayerWillEnterFullscreenNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerWillEnterFullscreenNotification: NSString! ``` |
| To | ``` let MPMoviePlayerWillEnterFullscreenNotification: String ``` |

Modified MPMoviePlayerWillExitFullscreenNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMoviePlayerWillExitFullscreenNotification: NSString! ``` |
| To | ``` let MPMoviePlayerWillExitFullscreenNotification: String ``` |

Modified MPMovieSourceTypeAvailableNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMovieSourceTypeAvailableNotification: NSString! ``` |
| To | ``` let MPMovieSourceTypeAvailableNotification: String ``` |

Modified MPMusicPlayerControllerNowPlayingItemDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMusicPlayerControllerNowPlayingItemDidChangeNotification: NSString! ``` |
| To | ``` let MPMusicPlayerControllerNowPlayingItemDidChangeNotification: String ``` |

Modified MPMusicPlayerControllerPlaybackStateDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMusicPlayerControllerPlaybackStateDidChangeNotification: NSString! ``` |
| To | ``` let MPMusicPlayerControllerPlaybackStateDidChangeNotification: String ``` |

Modified MPMusicPlayerControllerVolumeDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPMusicPlayerControllerVolumeDidChangeNotification: NSString! ``` |
| To | ``` let MPMusicPlayerControllerVolumeDidChangeNotification: String ``` |

Modified MPNowPlayingInfoPropertyChapterCount

|  | Declaration |
| --- | --- |
| From | ``` let MPNowPlayingInfoPropertyChapterCount: NSString! ``` |
| To | ``` let MPNowPlayingInfoPropertyChapterCount: String ``` |

Modified MPNowPlayingInfoPropertyChapterNumber

|  | Declaration |
| --- | --- |
| From | ``` let MPNowPlayingInfoPropertyChapterNumber: NSString! ``` |
| To | ``` let MPNowPlayingInfoPropertyChapterNumber: String ``` |

Modified MPNowPlayingInfoPropertyDefaultPlaybackRate

|  | Declaration |
| --- | --- |
| From | ``` let MPNowPlayingInfoPropertyDefaultPlaybackRate: NSString! ``` |
| To | ``` let MPNowPlayingInfoPropertyDefaultPlaybackRate: String ``` |

Modified MPNowPlayingInfoPropertyElapsedPlaybackTime

|  | Declaration |
| --- | --- |
| From | ``` let MPNowPlayingInfoPropertyElapsedPlaybackTime: NSString! ``` |
| To | ``` let MPNowPlayingInfoPropertyElapsedPlaybackTime: String ``` |

Modified MPNowPlayingInfoPropertyPlaybackQueueCount

|  | Declaration |
| --- | --- |
| From | ``` let MPNowPlayingInfoPropertyPlaybackQueueCount: NSString! ``` |
| To | ``` let MPNowPlayingInfoPropertyPlaybackQueueCount: String ``` |

Modified MPNowPlayingInfoPropertyPlaybackQueueIndex

|  | Declaration |
| --- | --- |
| From | ``` let MPNowPlayingInfoPropertyPlaybackQueueIndex: NSString! ``` |
| To | ``` let MPNowPlayingInfoPropertyPlaybackQueueIndex: String ``` |

Modified MPNowPlayingInfoPropertyPlaybackRate

|  | Declaration |
| --- | --- |
| From | ``` let MPNowPlayingInfoPropertyPlaybackRate: NSString! ``` |
| To | ``` let MPNowPlayingInfoPropertyPlaybackRate: String ``` |

Modified MPVolumeViewWirelessRouteActiveDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPVolumeViewWirelessRouteActiveDidChangeNotification: NSString! ``` |
| To | ``` let MPVolumeViewWirelessRouteActiveDidChangeNotification: String ``` |

Modified MPVolumeViewWirelessRoutesAvailableDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MPVolumeViewWirelessRoutesAvailableDidChangeNotification: NSString! ``` |
| To | ``` let MPVolumeViewWirelessRoutesAvailableDidChangeNotification: String ``` |

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
