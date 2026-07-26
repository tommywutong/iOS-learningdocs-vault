---
title: MPMusicPlayerControllerNowPlayingItemDidChangeNotification
framework: Media Player
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mediaplayer/mpmusicplayercontrollernowplayingitemdidchangenotification
source_url: 'https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollernowplayingitemdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mediaplayer/mpmusicplayercontrollernowplayingitemdidchangenotification.json'
content_hash: 'sha256:0f43775db07cc1e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Media Player](../mediaplayer.md)

# MPMusicPlayerControllerNowPlayingItemDidChangeNotification

<sub>Global Variable</sub>

Posted when the currently playing media item has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSNotificationName const MPMusicPlayerControllerNowPlayingItemDidChangeNotification;
```

## Discussion

The object associated with the notification is the music player whose Now Playing item changed. The notification has no `userInfo` dictionary.

## See Also

### Using music player notifications

- [- beginGeneratingPlaybackNotifications](<mpmusicplayercontroller/begingeneratingplaybacknotifications().md>) — Starts the generation of playback notifications.
- [- endGeneratingPlaybackNotifications](<mpmusicplayercontroller/endgeneratingplaybacknotifications().md>) — Ends the generation of playback notifications.
- [MPMusicPlayerControllerPlaybackStateDidChangeNotification](mpmusicplayercontrollerplaybackstatedidchangenotification.md) — Posted when the playback state changes programmatically or by user action.
- [MPMusicPlayerControllerVolumeDidChangeNotification](mpmusicplayercontrollervolumedidchangenotification.md) — Posted when the audio playback volume for the music player has changed.
