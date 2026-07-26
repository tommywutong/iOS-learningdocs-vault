---
title: silenceSecondaryAudioHintNotification
framework: AVFAudio
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudiosession/silencesecondaryaudiohintnotification
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudiosession/silencesecondaryaudiohintnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudiosession/silencesecondaryaudiohintnotification.json'
content_hash: 'sha256:3135019e1b01f098'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFAudio](../../avfaudio.md) · [AVAudioSession](../avaudiosession.md)

# silenceSecondaryAudioHintNotification

<sub>Type Property</sub>

A notification the system posts when the primary audio from other apps starts and stops.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class let silenceSecondaryAudioHintNotification: NSNotification.Name
```

## Discussion

Subscribe to this notification to ensure that the system notifies your app when optional secondary audio muting should begin or end. The system sends this notification only to registered listeners who are currently in the foreground and have an active audio session.

This notification’s [userInfo](../../foundation/nsnotification/userinfo.md) dictionary contains a [SilenceSecondaryAudioHintType](silencesecondaryaudiohinttype.md) value for the [AVAudioSessionSilenceSecondaryAudioHintTypeKey](../avaudiosessionsilencesecondaryaudiohinttypekey.md). Use the audio hint type to determine if your secondary audio muting should begin or end.

```swift
func handleSecondaryAudio(notification: Notification) {
    // Determine hint type
    guard let userInfo = notification.userInfo,
        let typeValue = userInfo[AVAudioSessionSilenceSecondaryAudioHintTypeKey] as? UInt,
        let type = AVAudioSession.SilenceSecondaryAudioHintType(rawValue: typeValue) else {
            return
    }
    
    if type == .begin {
        // Other app audio started playing - mute secondary audio.
    } else {
        // Other app audio stopped playing - restart secondary audio.
    }
}
```

The system posts this notification on the main thread.

## Topics

### User Info Keys

- [AVAudioSessionSilenceSecondaryAudioHintTypeKey](../avaudiosessionsilencesecondaryaudiohinttypekey.md) — A user info key that you use to retrieve the silence secondary audio hint type.

### User Info Values

- [SilenceSecondaryAudioHintType](silencesecondaryaudiohinttype.md) — Constants that indicate whether optional secondary audio muting should begin or end.

## See Also

### Mixing with other audio

- [otherAudioPlaying](isotheraudioplaying.md) — A Boolean value that indicates whether another app is playing audio.
- [secondaryAudioShouldBeSilencedHint](secondaryaudioshouldbesilencedhint.md) — A Boolean value that indicates whether another app, with a nonmixable audio session, is playing audio.
- [allowHapticsAndSystemSoundsDuringRecording](allowhapticsandsystemsoundsduringrecording.md) — A Boolean value that indicates whether system sounds and haptics play while recording from audio input.
- [- setAllowHapticsAndSystemSoundsDuringRecording:error:](<setallowhapticsandsystemsoundsduringrecording(__).md>) — Sets a Boolean value that indicates whether system sounds and haptics play while recording from audio input.
