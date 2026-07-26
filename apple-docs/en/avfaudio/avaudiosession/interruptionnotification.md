---
title: interruptionNotification
framework: AVFAudio
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudiosession/interruptionnotification
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudiosession/interruptionnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudiosession/interruptionnotification.json'
content_hash: 'sha256:bd5a9f1b0fa11337'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFAudio](../../avfaudio.md) · [AVAudioSession](../avaudiosession.md)

# interruptionNotification

<sub>Type Property</sub>

A notification the system posts when an audio interruption occurs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class let interruptionNotification: NSNotification.Name
```

## Discussion

The notification’s user-information dictionary contains the [AVAudioSessionInterruptionTypeKey](../avaudiosessioninterruptiontypekey.md) key. If the interruption type is [AVAudioSessionInterruptionTypeBegan](interruptiontype/began.md), the system interrupted your app’s audio session and it’s no longer active. If the interruption type is [AVAudioSessionInterruptionTypeEnded](interruptiontype/ended.md), this dictionary also contains the [AVAudioSessionInterruptionOptionKey](../avaudiosessioninterruptionoptionkey.md) key.

See [Handling audio interruptions](../handling-audio-interruptions.md) for more information on using this notification.

The system posts this notification on the main thread.

> [!note] Note
> Starting in iOS 10, the system deactivates an app’s audio session when it suspends the app process. When the app starts running again, it receives an interruption notification that the system has deactivated its audio session. This notification is necessarily delayed in time because the system can only deliver it once the app is running again. If the system suspended your app’s audio session for this reason, the user-information dictionary contains the [AVAudioSessionInterruptionWasSuspendedKey](../avaudiosessioninterruptionwassuspendedkey.md) key with a value of [true](../../swift/true.md).
>
> If you configured your audio session to be nonmixable (the default behavior for the [AVAudioSessionCategoryPlayback](category-swift.struct/playback.md), [AVAudioSessionCategoryPlayAndRecord](category-swift.struct/playandrecord.md), [AVAudioSessionCategorySoloAmbient](category-swift.struct/soloambient.md), and [AVAudioSessionCategoryMultiRoute](category-swift.struct/multiroute.md) categories), deactivate your audio session if you’re not actively using audio when you go into the background. Doing so avoids having your audio session deactivated by the system (and receiving this somewhat confusing notification).

## Topics

### User Info Keys

- [AVAudioSessionInterruptionTypeKey](../avaudiosessioninterruptiontypekey.md) — A user info key to retrieve the interruption type.
- [AVAudioSessionInterruptionOptionKey](../avaudiosessioninterruptionoptionkey.md) — A user info key to retrieve the interruption option.
- [AVAudioSessionInterruptionReasonKey](../avaudiosessioninterruptionreasonkey.md) — A user info key to retrieve the interruption reason.
- [AVAudioSessionInterruptionWasSuspendedKey](../avaudiosessioninterruptionwassuspendedkey.md) — A user info key used to determine if the interruption is due to the audio session being deactivated when the system suspended the app. _(deprecated)_

### User Info Values

- [InterruptionType](interruptiontype.md) — Constants that describe the type of an audio interruption. _(deprecated)_
- [InterruptionOptions](interruptionoptions.md) — Constants that indicate the state of an audio session after an interruption. _(deprecated)_
- [InterruptionReason](interruptionreason.md) — Constants that define the reasons for an audio session interruption.

## See Also

### Handling interruptions

- [prefersNoInterruptionsFromSystemAlerts](prefersnointerruptionsfromsystemalerts.md) — A Boolean value that indicates a preference for not interrupting the session with system alerts.
- [- setPrefersNoInterruptionsFromSystemAlerts:error:](<setprefersnointerruptionsfromsystemalerts(__).md>) — Sets the preference for not interrupting the audio session with system alerts.
- [prefersInterruptionOnRouteDisconnect](prefersinterruptiononroutedisconnect.md) — A Boolean value that indicates whether the system interrupts the audio session when the active route disconnects.
- [- setPrefersInterruptionOnRouteDisconnect:error:](<setprefersinterruptiononroutedisconnect(__).md>) — Sets a preference to interrupt the audio session when the active route disconnects.
