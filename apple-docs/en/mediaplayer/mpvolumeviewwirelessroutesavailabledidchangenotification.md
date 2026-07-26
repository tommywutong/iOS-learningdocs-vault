---
title: MPVolumeViewWirelessRoutesAvailableDidChangeNotification
framework: Media Player
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（13.0 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mediaplayer/mpvolumeviewwirelessroutesavailabledidchangenotification
source_url: 'https://developer.apple.com/documentation/mediaplayer/mpvolumeviewwirelessroutesavailabledidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mediaplayer/mpvolumeviewwirelessroutesavailabledidchangenotification.json'
content_hash: 'sha256:23102878ce5094a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Media Player](../mediaplayer.md)

# MPVolumeViewWirelessRoutesAvailableDidChangeNotification

<sub>Global Variable</sub>

Indicates the available wireless routes changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const MPVolumeViewWirelessRoutesAvailableDidChangeNotification;
```

## Discussion

The system posts this notification when the [wirelessRoutesAvailable](mpvolumeview/arewirelessroutesavailable.md) property changes.

## See Also

### Deprecated symbols

- [MPMovieAccessLog](mpmovieaccesslog.md) — Key metrics about network playback for an associated movie player that’s playing streamed content. _(deprecated)_
- [MPMovieAccessLogEvent](mpmovieaccesslogevent.md) — A single piece of information for a movie access log. _(deprecated)_
- [MPMovieErrorLog](mpmovieerrorlog.md) — Data describing network resource playback failures for the associated movie player, including timestamps indicating when each failure occurred. _(deprecated)_
- [MPMovieErrorLogEvent](mpmovieerrorlogevent.md) — A single piece of information for a movie error log. _(deprecated)_
- [MPMovieLoadState](mpmovieloadstate.md) — Constants describing the network load state of the movie player. _(deprecated)_
- [MPMovieMediaTypeMask](mpmoviemediatypemask.md) — The types of content available in the movie file. _(deprecated)_
- [MPMoviePlayerController](mpmovieplayercontroller.md) — A type of movie player that manages the playback of a movie from a file or a network stream. _(deprecated)_
- [MPMoviePlayerViewController](mpmovieplayerviewcontroller.md) — A simple view controller for displaying full-screen movies. _(deprecated)_
- [MPTimedMetadata](mptimedmetadata.md) — A _timed metadata object that_ carries time-based information within HTTP streamed media. _(deprecated)_
- [MPPlayableContentManager](mpplayablecontentmanager.md) — A shared content manager for controlling interactions between your media app and system-provided or external media player interfaces. _(deprecated)_
- [MPPlayableContentManagerContext](mpplayablecontentmanagercontext.md) — An object representing the current state of the playable endpoint. _(deprecated)_
- [iPodMusicPlayer](mpmusicplayercontroller/ipodmusicplayer.md) — Returns the iPod music player, which controls the iPod app’s state. _(deprecated)_
- [- initWithImage:](<mpmediaitemartwork/init(image_).md>) — Initializes a media item artwork instance with a full-size image. _(deprecated)_
- [imageCropRect](mpmediaitemartwork/imagecroprect.md) — The bounds, in points, of the content area for the full size image associated with the media item artwork. _(deprecated)_
- [showsRouteButton](mpvolumeview/showsroutebutton.md) — A Boolean value that indicates whether the route button is visible in the volume view. _(deprecated)_
