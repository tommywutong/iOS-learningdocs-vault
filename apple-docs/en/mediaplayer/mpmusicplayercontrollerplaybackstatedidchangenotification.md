---
title: MPMusicPlayerControllerPlaybackStateDidChangeNotification
framework: Media Player
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mediaplayer/mpmusicplayercontrollerplaybackstatedidchangenotification
source_url: 'https://developer.apple.com/documentation/mediaplayer/mpmusicplayercontrollerplaybackstatedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mediaplayer/mpmusicplayercontrollerplaybackstatedidchangenotification.json'
content_hash: 'sha256:8000b0f9d489f10a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Media Player](../mediaplayer.md)

# MPMusicPlayerControllerPlaybackStateDidChangeNotification

<sub>Global Variable</sub>

Posted when the playback state changes programmatically or by user action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSNotificationName const MPMusicPlayerControllerPlaybackStateDidChangeNotification;
```

## Discussion

The object associated with the notification is the music player whose playback state changed. The notification has no `userInfo` dictionary.

## See Also

### Using music player notifications

- [- beginGeneratingPlaybackNotifications](<mpmusicplayercontroller/begingeneratingplaybacknotifications().md>) — Starts the generation of playback notifications.
- [- endGeneratingPlaybackNotifications](<mpmusicplayercontroller/endgeneratingplaybacknotifications().md>) — Ends the generation of playback notifications.
- [MPMusicPlayerControllerNowPlayingItemDidChangeNotification](mpmusicplayercontrollernowplayingitemdidchangenotification.md) — Posted when the currently playing media item has changed.
- [MPMusicPlayerControllerVolumeDidChangeNotification](mpmusicplayercontrollervolumedidchangenotification.md) — Posted when the audio playback volume for the music player has changed.
