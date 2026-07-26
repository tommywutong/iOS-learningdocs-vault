---
title: MPMoviePlayerPlaybackStateDidChangeNotification
framework: Media Player
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mediaplayer/mpmovieplayerplaybackstatedidchangenotification
source_url: 'https://developer.apple.com/documentation/mediaplayer/mpmovieplayerplaybackstatedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mediaplayer/mpmovieplayerplaybackstatedidchangenotification.json'
content_hash: 'sha256:0ef5b3bda755c17f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Media Player](../mediaplayer.md)

# MPMoviePlayerPlaybackStateDidChangeNotification

<sub>Global Variable</sub>

Posted when a movie player’s playback state has changed. There is no `userInfo` dictionary.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const MPMoviePlayerPlaybackStateDidChangeNotification;
```

## Discussion

Playback state can change programmatically (see [MPMediaPlayback](mpmediaplayback.md)) or by user interaction. To retrieve the playback state of a movie player, access its [playbackState](mpmovieplayercontroller/playbackstate.md) property. The movie player whose state has changed is available as the object associated with the notification.

## See Also

### Notifications

- [MPMoviePlayerDidEnterFullscreenNotification](mpmovieplayerdidenterfullscreennotification.md) — Posted when a movie player has entered full-screen mode. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerDidExitFullscreenNotification](mpmovieplayerdidexitfullscreennotification.md) — Posted when a movie player has exited full-screen mode. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerIsAirPlayVideoActiveDidChangeNotification](mpmovieplayerisairplayvideoactivedidchangenotification.md) — Posted when a movie player has started or ended playing a movie via AirPlay. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerLoadStateDidChangeNotification](mpmovieplayerloadstatedidchangenotification.md) — Posted when a movie player’s network buffering state has changed. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerNowPlayingMovieDidChangeNotification](mpmovieplayernowplayingmoviedidchangenotification.md) — Posted when the currently playing movie has changed. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerPlaybackDidFinishNotification](mpmovieplayerplaybackdidfinishnotification.md) — Posted when a movie has finished playing. The `userInfo` dictionary of this notification contains the [MPMoviePlayerPlaybackDidFinishReasonUserInfoKey](mpmovieplayerplaybackdidfinishreasonuserinfokey.md) key, which indicates the reason that playback finished. This notification is also sent when playback fails because of an error. _(deprecated)_
- [MPMoviePlayerReadyForDisplayDidChangeNotification](mpmovieplayerreadyfordisplaydidchangenotification.md) — Posted when the ready for display state changes. _(deprecated)_
- [MPMoviePlayerScalingModeDidChangeNotification](mpmovieplayerscalingmodedidchangenotification.md) — Posted when the scaling mode of a movie player has changed. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerThumbnailImageRequestDidFinishNotification](mpmovieplayerthumbnailimagerequestdidfinishnotification.md) — Posted when a request to capture a thumbnail from a movie has finished whether the request succeeded or failed. Upon successful capture of a thumbnail, the `userInfo` dictionary contains values for the following keys: _(deprecated)_
- [MPMoviePlayerTimedMetadataUpdatedNotification](mpmovieplayertimedmetadataupdatednotification.md) — Posted when new timed metadata arrives. _(deprecated)_
- [MPMoviePlayerWillEnterFullscreenNotification](mpmovieplayerwillenterfullscreennotification.md) — Posted when a movie player is about to enter full-screen mode. _(deprecated)_
- [MPMoviePlayerWillExitFullscreenNotification](mpmovieplayerwillexitfullscreennotification.md) — Posted when a movie player is about to exit full-screen mode. _(deprecated)_
- [MPMovieDurationAvailableNotification](mpmoviedurationavailablenotification.md) — Posted when the duration of a movie has been determined. There is no `userInfo` dictionary. _(deprecated)_
- [MPMovieMediaTypesAvailableNotification](mpmoviemediatypesavailablenotification.md) — Posted when the available media types in a movie are determined. There is no `userInfo` dictionary. _(deprecated)_
- [MPMovieNaturalSizeAvailableNotification](mpmovienaturalsizeavailablenotification.md) — Posted when the natural frame size of a movie is first determined or subsequently changes. There is no `userInfo` dictionary. _(deprecated)_
