---
title: MPMediaPlaybackIsPreparedToPlayDidChangeNotification
framework: Media Player
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS, tvOS（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mediaplayer/mpmediaplaybackispreparedtoplaydidchangenotification
source_url: 'https://developer.apple.com/documentation/mediaplayer/mpmediaplaybackispreparedtoplaydidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mediaplayer/mpmediaplaybackispreparedtoplaydidchangenotification.json'
content_hash: 'sha256:babb26ec0633c8ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Media Player](../mediaplayer.md)

# MPMediaPlaybackIsPreparedToPlayDidChangeNotification

<sub>Global Variable</sub>

Indicates that the prepared to play status of the media player has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const MPMediaPlaybackIsPreparedToPlayDidChangeNotification;
```

## Discussion

Posted upon change in the prepared-to-play state of an object conforming to the [MPMediaPlayback](mpmediaplayback.md) protocol. The object whose state has changed is available as the object associated with the notification.
