---
title: MPMoviePlayerTimedMetadataUpdated
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+（9.0 起废弃）, iPadOS 4.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（9.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/mpmovieplayertimedmetadataupdated
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/mpmovieplayertimedmetadataupdated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/mpmovieplayertimedmetadataupdated.json'
content_hash: 'sha256:fc1fef5992a4e10c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# MPMoviePlayerTimedMetadataUpdated

<sub>Type Property</sub>

Posted when new timed metadata arrives.

> [!warning] Deprecated
> Use AVFoundation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static let MPMoviePlayerTimedMetadataUpdated: NSNotification.Name
```

## See Also

### MediaPlayer

- [MPMusicPlayerControllerQueueDidChange](mpmusicplayercontrollerqueuedidchange.md) — Indicates the music player’s queue changed.
- [MPMediaLibraryDidChange](mpmedialibrarydidchange.md) — Indicates the media library has changed.
- [MPMediaPlaybackIsPreparedToPlayDidChange](mpmediaplaybackispreparedtoplaydidchange.md) — Indicates that the prepared to play status of the media player has changed. _(deprecated)_
- [MPMusicPlayerControllerNowPlayingItemDidChange](mpmusicplayercontrollernowplayingitemdidchange.md) — Posted when the currently playing media item has changed.
- [MPMusicPlayerControllerPlaybackStateDidChange](mpmusicplayercontrollerplaybackstatedidchange.md) — Posted when the playback state changes programmatically or by user action.
- [MPMusicPlayerControllerVolumeDidChange](mpmusicplayercontrollervolumedidchange.md) — Posted when the audio playback volume for the music player has changed.
- [MPMovieDurationAvailable](mpmoviedurationavailable.md) — Posted when the duration of a movie has been determined. There is no `userInfo` dictionary. _(deprecated)_
- [MPMovieMediaTypesAvailable](mpmoviemediatypesavailable.md) — Posted when the available media types in a movie are determined. There is no `userInfo` dictionary. _(deprecated)_
- [MPMovieNaturalSizeAvailable](mpmovienaturalsizeavailable.md) — Posted when the natural frame size of a movie is first determined or subsequently changes. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerDidEnterFullscreen](mpmovieplayerdidenterfullscreen.md) — Posted when a movie player has entered full-screen mode. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerDidExitFullscreen](mpmovieplayerdidexitfullscreen.md) — Posted when a movie player has exited full-screen mode. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerIsAirPlayVideoActiveDidChange](mpmovieplayerisairplayvideoactivedidchange.md) — Posted when a movie player has started or ended playing a movie via AirPlay. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerLoadStateDidChange](mpmovieplayerloadstatedidchange.md) — Posted when a movie player’s network buffering state has changed. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerNowPlayingMovieDidChange](mpmovieplayernowplayingmoviedidchange.md) — Posted when the currently playing movie has changed. There is no `userInfo` dictionary. _(deprecated)_
- [MPMoviePlayerPlaybackDidFinish](mpmovieplayerplaybackdidfinish.md) — Posted when a movie has finished playing. _(deprecated)_
