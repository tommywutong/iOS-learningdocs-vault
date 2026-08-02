---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/MediaPlayer.html
archived_at: '2026-07-18T02:56:34.753631Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# MediaPlayer Changes for Objective-C

### MediaPlayer

#### AVFoundation+MPNowPlayingInfoLanguageOptionAdditions.h (Added)

Added [-[AVMediaSelectionGroup makeNowPlayingInfoLanguageOptionGroup]](https://developer.apple.com/documentation/avfoundation/avmediaselectiongroup/1623531-makenowplayinginfolanguageoption)Added [-[AVMediaSelectionOption makeNowPlayingInfoLanguageOption]](https://developer.apple.com/documentation/avfoundation/avmediaselectionoption/1623532-makenowplayinginfolanguageoption)Added AVMediaSelectionGroup(MPNowPlayingInfoLanguageOptionAdditions)Added AVMediaSelectionOption(MPNowPlayingInfoLanguageOptionAdditions)

#### MPMediaEntity.h

Modified [-[MPMediaEntity enumerateValuesForProperties:usingBlock:]](https://developer.apple.com/documentation/mediaplayer/mpmediaentity/1620122-enumeratevaluesforproperties)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateValuesForProperties:(NSSet *)properties usingBlock:(void (^)(NSString *property, id value, BOOL *stop))block ``` |
| To | ``` - (void)enumerateValuesForProperties:(NSSet<NSString *> * _Nonnull)properties usingBlock:(void (^ _Nonnull)(NSString * _Nonnull property, id _Nonnull value, BOOL * _Nonnull stop))block ``` |

#### MPMediaItemCollection.h

Modified [+[MPMediaItemCollection collectionWithItems:]](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/1614438-collectionwithitems)

|  | Declaration |
| --- | --- |
| From | ``` + (MPMediaItemCollection *)collectionWithItems:(NSArray *)items ``` |
| To | ``` + (MPMediaItemCollection * _Nonnull)collectionWithItems:(NSArray<MPMediaItem *> * _Nonnull)items ``` |

Modified [-[MPMediaItemCollection initWithItems:]](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/1614440-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithItems:(NSArray *)items ``` |
| To | ``` - (instancetype _Nonnull)initWithItems:(NSArray<MPMediaItem *> * _Nonnull)items ``` |

Modified [MPMediaItemCollection.items](https://developer.apple.com/documentation/mediaplayer/mpmediaitemcollection/1614441-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *items ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<MPMediaItem *> *items ``` |

#### MPMediaPlayback.h

Modified [MPMediaPlaybackIsPreparedToPlayDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1616250-mpmediaplaybackispreparedtoplayd)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### MPMediaPlaylist.h

Modified [MPMediaPlaylist.seedItems](https://developer.apple.com/documentation/mediaplayer/mpmediaplaylist/1618720-seeditems)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *seedItems ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<MPMediaItem *> *seedItems ``` |

#### MPMediaQuery.h

Modified [MPMediaQuery.collections](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621806-collections)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *collections ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<MPMediaItemCollection *> *collections ``` |

Modified [MPMediaQuery.collectionSections](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621779-collectionsections)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *collectionSections ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<MPMediaQuerySection *> *collectionSections ``` |

Modified [MPMediaQuery.filterPredicates](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621781-filterpredicates)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSSet *filterPredicates ``` |
| To | ``` @property(nonatomic, strong, nullable) NSSet<MPMediaPredicate *> *filterPredicates ``` |

Modified [-[MPMediaQuery initWithFilterPredicates:]](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621771-initwithfilterpredicates)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithFilterPredicates:(NSSet *)filterPredicates ``` |
| To | ``` - (instancetype _Nonnull)initWithFilterPredicates:(NSSet<MPMediaPredicate *> * _Nullable)filterPredicates ``` |

Modified [MPMediaQuery.items](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621770-items)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *items ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<MPMediaItem *> *items ``` |

Modified [MPMediaQuery.itemSections](https://developer.apple.com/documentation/mediaplayer/mpmediaquery/1621797-itemsections)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *itemSections ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSArray<MPMediaQuerySection *> *itemSections ``` |

#### MPMoviePlayerController.h

Modified [MPMovieAccessLog](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLog.events](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/1620820-events)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLog.extendedLogData](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/1620870-extendedlogdata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLog.extendedLogDataStringEncoding](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/1620814-extendedlogdatastringencoding)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.durationWatched](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620880-durationwatched)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.indicatedBitrate](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620932-indicatedbitrate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.numberOfBytesTransferred](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620949-numberofbytestransferred)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.numberOfDroppedVideoFrames](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620884-numberofdroppedvideoframes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.numberOfSegmentsDownloaded](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620937-numberofsegmentsdownloaded)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.numberOfServerAddressChanges](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620801-numberofserveraddresschanges)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.numberOfStalls](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620925-numberofstalls)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.observedBitrate](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620827-observedbitrate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.playbackSessionID](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620926-playbacksessionid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.playbackStartDate](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620868-playbackstartdate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.playbackStartOffset](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620902-playbackstartoffset)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.segmentsDownloadedDuration](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620944-segmentsdownloadedduration)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.serverAddress](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620862-serveraddress)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieAccessLogEvent.URI](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslogevent/1620959-uri)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLog](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLog.events](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/1620929-events)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLog.extendedLogData](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/1620797-extendedlogdata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLog.extendedLogDataStringEncoding](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/1620806-extendedlogdatastringencoding)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLogEvent](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLogEvent.date](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620794-date)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLogEvent.errorComment](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620941-errorcomment)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLogEvent.errorDomain](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620818-errordomain)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLogEvent.errorStatusCode](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620782-errorstatuscode)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLogEvent.playbackSessionID](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620890-playbacksessionid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLogEvent.serverAddress](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620908-serveraddress)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieErrorLogEvent.URI](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/1620913-uri)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.accessLog](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620922-accesslog)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.airPlayVideoActive](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620906-isairplayvideoactive)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.allowsAirPlay](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620781-allowsairplay)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.backgroundView](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620819-backgroundview)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[MPMoviePlayerController cancelAllThumbnailImageRequests]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620811-cancelallthumbnailimagerequests)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.contentURL](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620847-contenturl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.controlStyle](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620935-controlstyle)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.duration](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620784-duration)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 3.2 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.endPlaybackTime](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620895-endplaybacktime)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 3.2 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.errorLog](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620798-errorlog)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.fullscreen](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620875-isfullscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.initialPlaybackTime](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620796-initialplaybacktime)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 3.0 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [-[MPMoviePlayerController initWithContentURL:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620850-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.loadState](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620879-loadstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.movieMediaTypes](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620821-moviemediatypes)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 3.2 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.movieSourceType](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620793-moviesourcetype)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 3.2 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.naturalSize](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620877-naturalsize)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 3.2 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.playableDuration](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620803-playableduration)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 3.2 | -- |
| To | iOS 2.0 | iOS 9.0 |

Modified [MPMoviePlayerController.playbackState](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620841-playbackstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.readyForDisplay](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620831-readyfordisplay)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.repeatMode](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620962-repeatmode)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[MPMoviePlayerController requestThumbnailImagesAtTimes:timeOption:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620805-requestthumbnailimagesattimes)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.scalingMode](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620943-scalingmode)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[MPMoviePlayerController setFullscreen:animated:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620844-setfullscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.shouldAutoplay](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620812-shouldautoplay)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.timedMetadata](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620853-timedmetadata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerController.view](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller/1620869-view)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPTimedMetadata](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPTimedMetadata.allMetadata](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/1620856-allmetadata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPTimedMetadata.key](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/1620834-key)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPTimedMetadata.keyspace](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/1620846-keyspace)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPTimedMetadata.timestamp](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/1620918-timestamp)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPTimedMetadata.value](https://developer.apple.com/documentation/mediaplayer/mptimedmetadata/1620866-value)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieControlStyleDefault](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle/mpmoviecontrolstyledefault)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieControlStyleEmbedded](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle/mpmoviecontrolstyleembedded)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieControlStyleFullscreen](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle/fullscreen)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieControlStyleNone](https://developer.apple.com/documentation/mediaplayer/mpmoviecontrolstyle/mpmoviecontrolstylenone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieDurationAvailableNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620881-mpmoviedurationavailable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieFinishReasonPlaybackEnded](https://developer.apple.com/documentation/mediaplayer/mpmoviefinishreason/playbackended)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieFinishReasonPlaybackError](https://developer.apple.com/documentation/mediaplayer/mpmoviefinishreason/mpmoviefinishreasonplaybackerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieFinishReasonUserExited](https://developer.apple.com/documentation/mediaplayer/mpmoviefinishreason/mpmoviefinishreasonuserexited)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieLoadStatePlayable](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/1620892-playable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieLoadStatePlaythroughOK](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/mpmovieloadstateplaythroughok)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieLoadStateStalled](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/1620939-stalled)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieLoadStateUnknown](https://developer.apple.com/documentation/mediaplayer/mpmovieloadstate/mpmovieloadstateunknown)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieMediaTypeMaskAudio](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask/mpmoviemediatypemaskaudio)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieMediaTypeMaskNone](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask/mpmoviemediatypemasknone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieMediaTypeMaskVideo](https://developer.apple.com/documentation/mediaplayer/mpmoviemediatypemask/1620863-video)

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

Modified [MPMoviePlaybackStateInterrupted](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstateinterrupted)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlaybackStatePaused](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstatepaused)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlaybackStatePlaying](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/playing)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlaybackStateSeekingBackward](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstateseekingbackward)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlaybackStateSeekingForward](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstateseekingforward)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlaybackStateStopped](https://developer.apple.com/documentation/mediaplayer/mpmovieplaybackstate/mpmovieplaybackstatestopped)

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

Modified [MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620802-mpmovieplayerisairplayvideoactiv)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerLoadStateDidChangeNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerloadstatedidchangenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerNowPlayingMovieDidChangeNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayernowplayingmoviedidchangenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerPlaybackDidFinishNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620936-mpmovieplayerplaybackdidfinish)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerPlaybackDidFinishReasonUserInfoKey](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerplaybackdidfinishreasonuserinfokey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerPlaybackStateDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620957-mpmovieplayerplaybackstatedidcha)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerReadyForDisplayDidChangeNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerreadyfordisplaydidchangenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerScalingModeDidChangeNotification](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerscalingmodedidchangenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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

Modified [MPMovieRepeatModeNone](https://developer.apple.com/documentation/mediaplayer/mpmovierepeatmode/mpmovierepeatmodenone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieRepeatModeOne](https://developer.apple.com/documentation/mediaplayer/mpmovierepeatmode/one)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieScalingModeAspectFill](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode/aspectfill)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieScalingModeAspectFit](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode/mpmoviescalingmodeaspectfit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieScalingModeFill](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode/fill)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieScalingModeNone](https://developer.apple.com/documentation/mediaplayer/mpmoviescalingmode/mpmoviescalingmodenone)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieSourceTypeAvailableNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620951-mpmoviesourcetypeavailable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieSourceTypeFile](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetype/file)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieSourceTypeStreaming](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetype/mpmoviesourcetypestreaming)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieSourceTypeUnknown](https://developer.apple.com/documentation/mediaplayer/mpmoviesourcetype/mpmoviesourcetypeunknown)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieTimeOptionExact](https://developer.apple.com/documentation/mediaplayer/mpmovietimeoption/mpmovietimeoptionexact)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMovieTimeOptionNearestKeyFrame](https://developer.apple.com/documentation/mediaplayer/mpmovietimeoption/nearestkeyframe)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### MPMoviePlayerViewController.h

Modified [MPMoviePlayerViewController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[MPMoviePlayerViewController initWithContentURL:]](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller/1622348-initwithcontenturl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MPMoviePlayerViewController.moviePlayer](https://developer.apple.com/documentation/mediaplayer/mpmovieplayerviewcontroller/1622346-movieplayer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIViewController dismissMoviePlayerViewControllerAnimated]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1622345-dismissmovieplayerviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[UIViewController presentMoviePlayerViewControllerAnimated:]](https://developer.apple.com/documentation/uikit/uiviewcontroller/1622347-presentmovieplayerviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### MPNowPlayingInfoCenter.h

Added [MPNowPlayingInfoPropertyAvailableLanguageOptions](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertyavailablelanguageoptions)Added [MPNowPlayingInfoPropertyCurrentLanguageOptions](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfopropertycurrentlanguageoptions)Modified [MPNowPlayingInfoCenter.nowPlayingInfo](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfocenter/1615903-nowplayinginfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *nowPlayingInfo ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,id> *nowPlayingInfo ``` |

#### MPNowPlayingInfoLanguageOption.h (Added)

Added [MPNowPlayingInfoLanguageOption](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption)Added [MPNowPlayingInfoLanguageOption.displayName](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623145-displayname)Added [MPNowPlayingInfoLanguageOption.identifier](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623135-identifier)Added [-[MPNowPlayingInfoLanguageOption initWithType:languageTag:characteristics:displayName:identifier:]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623159-initwithtype)Added [-[MPNowPlayingInfoLanguageOption isAutomaticLegibleLanguageOption]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623144-isautomaticlegiblelanguageoption)Added [MPNowPlayingInfoLanguageOption.languageOptionCharacteristics](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623152-languageoptioncharacteristics)Added [MPNowPlayingInfoLanguageOption.languageOptionType](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623153-languageoptiontype)Added [MPNowPlayingInfoLanguageOption.languageTag](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoption/1623160-languagetag)Added [MPNowPlayingInfoLanguageOptionGroup](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup)Added [MPNowPlayingInfoLanguageOptionGroup.allowEmptySelection](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/1623161-allowemptyselection)Added [MPNowPlayingInfoLanguageOptionGroup.defaultLanguageOption](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/1623142-defaultlanguageoption)Added [-[MPNowPlayingInfoLanguageOptionGroup initWithLanguageOptions:defaultLanguageOption:allowEmptySelection:]](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/1623138-init)Added [MPNowPlayingInfoLanguageOptionGroup.languageOptions](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiongroup/1623157-languageoptions)Added [MPLanguageOptionCharacteristicContainsOnlyForcedSubtitles](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristiccontainsonlyforcedsubtitles)Added [MPLanguageOptionCharacteristicDescribesMusicAndSound](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicdescribesmusicandsound)Added [MPLanguageOptionCharacteristicDescribesVideo](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicdescribesvideo)Added [MPLanguageOptionCharacteristicDubbedTranslation](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicdubbedtranslation)Added [MPLanguageOptionCharacteristicEasyToRead](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristiceasytoread)Added [MPLanguageOptionCharacteristicIsAuxiliaryContent](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicisauxiliarycontent)Added [MPLanguageOptionCharacteristicIsMainProgramContent](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicismainprogramcontent)Added [MPLanguageOptionCharacteristicLanguageTranslation](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristiclanguagetranslation)Added [MPLanguageOptionCharacteristicTranscribesSpokenDialog](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristictranscribesspokendialog)Added [MPLanguageOptionCharacteristicVoiceOverTranslation](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristicvoiceovertranslation)Added [MPNowPlayingInfoLanguageOptionType](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype)Added [MPNowPlayingInfoLanguageOptionTypeAudible](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype/mpnowplayinginfolanguageoptiontypeaudible)Added [MPNowPlayingInfoLanguageOptionTypeLegible](https://developer.apple.com/documentation/mediaplayer/mpnowplayinginfolanguageoptiontype/legible)

#### MPPlayableContentDelegate.h

Added [-[MPPlayableContentDelegate playableContentManager:didUpdateContext:]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620291-playablecontentmanager)Added [-[MPPlayableContentDelegate playableContentManager:initializePlaybackQueueWithCompletionHandler:]](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentdelegate/1620294-playablecontentmanager)

#### MPPlayableContentManager.h

Added [MPPlayableContentManager.context](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/1614800-context)

#### MPPlayableContentManagerContext.h (Added)

Added [MPPlayableContentManagerContext](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext)Added [MPPlayableContentManagerContext.contentLimitsEnabled](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/1623567-contentlimitsenabled)Added [MPPlayableContentManagerContext.contentLimitsEnforced](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/1623570-contentlimitsenforced)Added [MPPlayableContentManagerContext.endpointAvailable](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/1623569-endpointavailable)Added [MPPlayableContentManagerContext.enforcedContentItemsCount](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/1623568-enforcedcontentitemscount)Added [MPPlayableContentManagerContext.enforcedContentTreeDepth](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanagercontext/1623572-enforcedcontenttreedepth)

#### MPRemoteCommand.h

Modified [MPChangePlaybackRateCommand.supportedPlaybackRates](https://developer.apple.com/documentation/mediaplayer/mpchangeplaybackratecommand/1622915-supportedplaybackrates)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *supportedPlaybackRates ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<NSNumber *> *supportedPlaybackRates ``` |

#### MPRemoteCommandCenter.h

Added [MPRemoteCommandCenter.disableLanguageOptionCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618988-disablelanguageoptioncommand)Added [MPRemoteCommandCenter.enableLanguageOptionCommand](https://developer.apple.com/documentation/mediaplayer/mpremotecommandcenter/1618980-enablelanguageoptioncommand)

#### MPRemoteCommandEvent.h

Added [MPChangeLanguageOptionCommandEvent](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent)Added [MPChangeLanguageOptionCommandEvent.languageOption](https://developer.apple.com/documentation/mediaplayer/mpchangelanguageoptioncommandevent/1616769-languageoption)

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
