---
title: MPMediaLibraryDidChangeNotification
framework: Media Player
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/mediaplayer/mpmedialibrarydidchangenotification
source_url: 'https://developer.apple.com/documentation/mediaplayer/mpmedialibrarydidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mediaplayer/mpmedialibrarydidchangenotification.json'
content_hash: 'sha256:38b435c4d3f31c48'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Media Player](../mediaplayer.md)

# MPMediaLibraryDidChangeNotification

<sub>Global Variable</sub>

Indicates the media library has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const MPMediaLibraryDidChangeNotification;
```

## Discussion

When the system posts this notification, your app should reevaluate items or playlists that you previously cached.

## See Also

### Receiving notifications when the user’s library changes

- [- beginGeneratingLibraryChangeNotifications](<mpmedialibrary/begingeneratinglibrarychangenotifications().md>) — Asks the media library to turn on notifications for whenever the library changes.
- [- endGeneratingLibraryChangeNotifications](<mpmedialibrary/endgeneratinglibrarychangenotifications().md>) — Asks the media library to turn off notifications for whenever the library changes.
- [lastModifiedDate](mpmedialibrary/lastmodifieddate.md) — The calendar date on which the media library was last modified.
