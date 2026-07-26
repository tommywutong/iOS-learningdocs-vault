---
title: mediaServicesWereResetNotification
framework: AVFAudio
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudiosession/mediaserviceswereresetnotification
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudiosession/mediaserviceswereresetnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudiosession/mediaserviceswereresetnotification.json'
content_hash: 'sha256:010eeebc31a41f59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFAudio](../../avfaudio.md) · [AVAudioSession](../avaudiosession.md)

# mediaServicesWereResetNotification

<sub>Type Property</sub>

A notification the system posts when the media server restarts.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class let mediaServicesWereResetNotification: NSNotification.Name
```

## Discussion

Under rare circumstances, the system terminates and restarts its media services daemon. Respond to these events by reinitializing your app’s audio objects (such as players, recorders, converters, or audio queues) and resetting your audio session’s category, options, and mode configuration. Your app shouldn’t restart its media playback, recording, or processing until initiated by user action.

> [!note] Note
> You can trigger a media server reset by choosing the “Reset Media Services” selection under the Developer menu in the iOS Settings app. Using this utility helps to ensure that your app responds appropriately if media services were reset.

This notification has no [userInfo](../../foundation/nsnotification/userinfo.md) dictionary.

The system posts this notification on the main thread.

> [!important] Important
> Apps don’t need to reregister for any audio session notifications and don’t need to reset key-value observers on audio session properties after a media services reset.

## See Also

### Handling a change of media services

- [AVAudioSessionMediaServicesWereLostNotification](mediaserviceswerelostnotification.md) — A notification the system posts when it terminates the media server.
