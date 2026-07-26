---
title: mediaPlayingStarted()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensioncontext/mediaplayingstarted()
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/mediaplayingstarted()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/mediaplayingstarted%28%29.json'
content_hash: 'sha256:6bec26b29ddff7a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# mediaPlayingStarted()

<sub>Instance Method</sub>

Tells the system that the Notification Content app extension began playing a media file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func mediaPlayingStarted()
```

## Discussion

In your Notification Content app extension code, call this method when you programmatically begin playing a media file. When called, the system updates the appearance of the media playback button displayed in the notification content extension’s interface. For more information about implementing a notification content extension, see [UNNotificationContentExtension](../../usernotificationsui/unnotificationcontentextension.md).

## See Also

### Controlling media playback in notification content extensions

- [- mediaPlayingPaused](<mediaplayingpaused().md>) — Tells the system that the Notification Content app extension stopped playing a media file.
