---
title: mediaPlayingPaused()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensioncontext/mediaplayingpaused()
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/mediaplayingpaused()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/mediaplayingpaused%28%29.json'
content_hash: 'sha256:4a1e7c1131a2fd20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# mediaPlayingPaused()

<sub>Instance Method</sub>

Tells the system that the Notification Content app extension stopped playing a media file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func mediaPlayingPaused()
```

## Discussion

In your Notification Content app extension code, call this method when you programmatically stop playing a media file. When called, the system updates the appearance of the media playback button displayed in the notification content extension’s interface. For more information about implementing a notification content extension, see [UNNotificationContentExtension](../../usernotificationsui/unnotificationcontentextension.md).

## See Also

### Controlling media playback in notification content extensions

- [- mediaPlayingStarted](<mediaplayingstarted().md>) — Tells the system that the Notification Content app extension began playing a media file.
