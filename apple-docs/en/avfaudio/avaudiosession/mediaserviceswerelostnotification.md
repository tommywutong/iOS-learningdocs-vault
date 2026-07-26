---
title: mediaServicesWereLostNotification
framework: AVFAudio
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudiosession/mediaserviceswerelostnotification
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudiosession/mediaserviceswerelostnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudiosession/mediaserviceswerelostnotification.json'
content_hash: 'sha256:f720ce04c7797c00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFAudio](../../avfaudio.md) · [AVAudioSession](../avaudiosession.md)

# mediaServicesWereLostNotification

<sub>Type Property</sub>

A notification the system posts when it terminates the media server.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class let mediaServicesWereLostNotification: NSNotification.Name
```

## Discussion

The system posts this notification when the media server first becomes unavailable. Most apps don’t need to subscribe to this notification and should instead subscribe to the [AVAudioSessionMediaServicesWereResetNotification](mediaserviceswereresetnotification.md) notification. However, you can use this notification as a cue to take any appropriate steps to handle requests that come in before the server restarts.

This notification has no [userInfo](../../foundation/nsnotification/userinfo.md) dictionary.

The system posts this notification on the main thread.

## See Also

### Handling a change of media services

- [AVAudioSessionMediaServicesWereResetNotification](mediaserviceswereresetnotification.md) — A notification the system posts when the media server restarts.
