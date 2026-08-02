---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/MediaPlayer.html
archived_at: '2026-07-18T02:55:58.940030Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# MediaPlayer Changes

## MediaPlayer

MPMediaEntity.hAdded [-[MPMediaEntity objectForKeyedSubscript:]](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620124-objectforkeyedsubscript)Added [MPMediaEntity.persistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620126-persistentid)Added [MPMediaEntityPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaentitypersistentid)MPMediaItem.hAdded [MPMediaItem.albumArtist](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621734-albumartist)Added [MPMediaItem.albumArtistPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621740-albumartistpersistentid)Added [MPMediaItem.albumPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621703-albumpersistentid)Added [MPMediaItem.albumTitle](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621756-albumtitle)Added [MPMediaItem.albumTrackCount](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621757-albumtrackcount)Added [MPMediaItem.albumTrackNumber](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621729-albumtracknumber)Added [MPMediaItem.artist](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621714-artist)Added [MPMediaItem.artistPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621742-artistpersistentid)Added [MPMediaItem.artwork](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621743-artwork)Added [MPMediaItem.assetURL](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621707-asseturl)Added [MPMediaItem.beatsPerMinute](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621751-beatsperminute)Added [MPMediaItem.bookmarkTime](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621727-bookmarktime)Added [MPMediaItem.cloudItem](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621697-clouditem)Added [MPMediaItem.comments](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621767-comments)Added [MPMediaItem.compilation](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621745-compilation)Added [MPMediaItem.composer](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621681-composer)Added [MPMediaItem.composerPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621709-composerpersistentid)Added [MPMediaItem.discCount](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621702-disccount)Added [MPMediaItem.discNumber](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621749-discnumber)Added [MPMediaItem.genre](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621762-genre)Added [MPMediaItem.genrePersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621738-genrepersistentid)Added [MPMediaItem.lastPlayedDate](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621719-lastplayeddate)Added [MPMediaItem.lyrics](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621684-lyrics)Added [MPMediaItem.mediaType](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621753-mediatype)Added [MPMediaItem.persistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621766-persistentid)Added [MPMediaItem.playCount](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621694-playcount)Added [MPMediaItem.playbackDuration](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621732-playbackduration)Added [MPMediaItem.podcastPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621695-podcastpersistentid)Added [MPMediaItem.podcastTitle](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621715-podcasttitle)Added [MPMediaItem.rating](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621750-rating)Added [MPMediaItem.releaseDate](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621682-releasedate)Added [MPMediaItem.skipCount](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621693-skipcount)Added [MPMediaItem.title](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621713-title)Added [MPMediaItem.userGrouping](https://developer.apple.com/documentation/mediaplayer/mpmediaitem/1621716-usergrouping)Modified [-[MPMediaItemArtwork initWithImage:]](https://developer.apple.com/documentation/mediaplayer/mpmediaitemartwork/1621747-initwithimage)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithImage:(UIImage *)image ``` |
| To | ``` - (instancetype)initWithImage:(UIImage *)image ``` |

Modified [MPMediaItemPropertyPersistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaitempropertypersistentid)

|  | Introduction |
| --- | --- |
| From | iOS 3.0 |
| To | iOS 4.2 |

MPMediaItemCollection.hModified [-[MPMediaItemCollection initWithItems:]](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/1614440-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithItems:(NSArray *)items ``` |
| To | ``` - (instancetype)initWithItems:(NSArray *)items ``` |

MPMediaPickerController.hRemoved [-[MPMediaPickerController init]](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontroller/1808935-init)Modified [-[MPMediaPickerControllerDelegate mediaPicker:didPickMediaItems:]](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontrollerdelegate/1614657-mediapicker)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MPMediaPickerControllerDelegate mediaPickerDidCancel:]](https://developer.apple.com/documentation/mediaplayer/mpmediapickercontrollerdelegate/1614667-mediapickerdidcancel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MPMediaPlaylist.hAdded [MPMediaPlaylist.name](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618716-name)Added [MPMediaPlaylist.persistentID](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618718-persistentid)Added [MPMediaPlaylist.playlistAttributes](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618709-playlistattributes)Added [MPMediaPlaylist.seedItems](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618720-seeditems)MPMediaQuery.hRemoved [-[MPMediaQuery init]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1808932-init)Modified [-[MPMediaQuery initWithFilterPredicates:]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621771-initwithfilterpredicates)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFilterPredicates:(NSSet *)filterPredicates ``` |
| To | ``` - (instancetype)initWithFilterPredicates:(NSSet *)filterPredicates ``` |

MPMoviePlayerController.hRemoved -[MPMoviePlayerController backgroundColor]Removed -[MPMoviePlayerController movieControlMode]Removed -[MPMoviePlayerController setBackgroundColor:]Removed -[MPMoviePlayerController setMovieControlMode:]Removed [-[MPMoviePlayerController timedMetadata]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620853-timedmetadata)Removed [MPMovieControlMode](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/mpmoviecontrolmode)Removed [MPMovieControlModeDefault](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/mpmoviecontrolmode/mpmoviecontrolmodedefault)Removed [MPMovieControlModeHidden](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/mpmoviecontrolmode/mpmoviecontrolmodehidden)Removed [MPMovieControlModeVolumeOnly](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/mpmoviecontrolmode/mpmoviecontrolmodevolumeonly)Removed MPMoviePlayerContentPreloadDidFinishNotificationAdded [MPMoviePlayerController.timedMetadata](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620853-timedmetadata)Modified [-[MPMoviePlayerController initWithContentURL:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620850-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithContentURL:(NSURL *)url ``` |

MPMoviePlayerViewController.hRemoved -[MPMoviePlayerViewController shouldAutorotate]Removed -[MPMoviePlayerViewController supportedInterfaceOrientations]Modified [-[MPMoviePlayerViewController initWithContentURL:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller/1622348-initwithcontenturl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentURL:(NSURL *)contentURL ``` |
| To | ``` - (instancetype)initWithContentURL:(NSURL *)contentURL ``` |

MPMusicPlayerController.hAdded [+[MPMusicPlayerController systemMusicPlayer]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624179-systemmusicplayer)Modified [+[MPMusicPlayerController iPodMusicPlayer]](https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontroller/1624206-ipodmusicplayer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

MPNowPlayingInfoCenter.hAdded [MPNowPlayingInfoPropertyDefaultPlaybackRate](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertydefaultplaybackrate)MPPlayableContentDataSource.hModified [-[MPPlayableContentDataSource beginLoadingChildItemsAtIndexPath:completionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619508-beginloadingchilditemsatindexpat)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MPPlayableContentDataSource childItemsDisplayPlaybackProgressAtIndexPath:]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdatasource/1619509-childitemsdisplayplaybackprogres)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MPPlayableContentDelegate.hModified [-[MPPlayableContentDelegate playableContentManager:initiatePlaybackOfContentItemAtIndexPath:completionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620292-playablecontentmanager)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MPVolumeView.hRemoved -[MPVolumeView sizeThatFits:]

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
