---
title: Handling audio interruptions
framework: AVFAudio
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/handling-audio-interruptions
source_url: 'https://developer.apple.com/documentation/avfaudio/handling-audio-interruptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/handling-audio-interruptions.json'
content_hash: 'sha256:5d9b720871dc37aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# Handling audio interruptions

<sub>Article</sub>

Observe audio session notifications to ensure that your app responds appropriately to interruptions.

## Overview

Interruptions are a common part of the iOS and watchOS user experiences. For example, consider the scenario of receiving a phone call while you’re watching a movie in the TV app on your iPhone. In this case, the movie’s audio fades out, playback pauses, and the sound of the call’s ringtone fades in. If you decline the call, control returns to the TV app, and playback begins again as the movie’s audio fades in.

At the center of this behavior is your app’s audio session. As interruptions begin and end, the audio session notifies any registered observers so they can take appropriate action. For example, [AVPlayer](../avfoundation/avplayer.md) monitors your app’s audio session and automatically pauses playback in response to interruption events. You can monitor these changes by key-value observing the player’s [timeControlStatus](../avfoundation/avplayer/timecontrolstatus-swift.property.md) property, and update your user interface as necessary when the player pauses and resumes playback.

### Customize the interruption behavior

Most apps rely on the system’s default interruption behavior. However, [AVAudioSession](avaudiosession.md) provides ways to customize the default behavior to better accommodate your app’s needs:

- Recent iPad models provide a feature that mutes the built-in microphone at the hardware level when the user closes the device’s Smart Folio cover. If your app plays and records audio, you may want to continue playback even if the system mutes the microphone. You can disable the default interruption behavior by setting the [AVAudioSessionCategoryOptionOverrideMutedMicrophoneInterruption](avaudiosession/categoryoptions-swift.struct/overridemutedmicrophoneinterruption.md) option when configuring your audio session.
- System alerts, such as receiving an incoming phone call, interrupt the active audio session. If you prefer that the system not interrupt your app’s audio session in these cases, you can indicate this preference by setting a value for the [- setPrefersNoInterruptionsFromSystemAlerts:error:](<avaudiosession/setprefersnointerruptionsfromsystemalerts(__).md>) method.

### Observe audio session interruptions

You can directly observe interruption notifications that [AVAudioSession](avaudiosession.md) posts. This might be useful if you want to know when the system pauses playback due to an interruption or another reason, such as a route change. To respond to audio interruptions, observe notifications of type [AVAudioSessionInterruptionNotification](avaudiosession/interruptionnotification.md).

```swift
func observeInterruptions() async {
    // Observe interruption notifications using async sequences.
    for await notification in NotificationCenter.default.notifications(
        named: AVAudioSession.interruptionNotification,
        object: AVAudioSession.sharedInstance()
    ) {
        handleInterruption(notification: notification)
    }
}

func handleInterruption(notification: Notification) {
    // To implement.
}
```

### Handle audio session interruptions

The posted [Notification](../foundation/notification.md) object contains a populated user-information dictionary that provides the details of the interruption. You determine the type of interruption by retrieving the [InterruptionType](avaudiosession/interruptiontype.md) value from the [userInfo](../foundation/notification/userinfo.md) dictionary. The interruption type indicates whether the interruption is beginning or ending.

```swift
func handleInterruption(notification: Notification) {
    guard let userInfo = notification.userInfo,
        let typeValue = userInfo[AVAudioSessionInterruptionTypeKey] as? UInt,
        let type = AVAudioSession.InterruptionType(rawValue: typeValue) else {
            return
    }

    // Switch over the interruption type.
    switch type {

    case .began:
        // An interruption began. Update the UI as necessary.

    case .ended:
       // An interruption ended. Resume playback, if appropriate.

        guard let optionsValue = userInfo[AVAudioSessionInterruptionOptionKey] as? UInt else { return }
        let options = AVAudioSession.InterruptionOptions(rawValue: optionsValue)
        if options.contains(.shouldResume) {
            // An interruption ended. Resume playback.
        } else {
            // An interruption ended. Don't resume playback.
        }

    default: ()
    }
}
```

If the interruption type is [AVAudioSessionInterruptionTypeEnded](avaudiosession/interruptiontype/ended.md), the [userInfo](../foundation/notification/userinfo.md) dictionary contains an [InterruptionOptions](avaudiosession/interruptionoptions.md) value, which you use to determine whether playback automatically resumes.

## See Also

### System audio

- [Responding to audio route changes](responding-to-audio-route-changes.md) — Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Routing audio to specific devices in multidevice sessions](routing-audio-to-specific-devices-in-multidevice-sessions.md) — Map audio channels to specific devices in multiroute sessions for recording and playback.
- [Adding synthesized speech to calls](adding-synthesized-speech-to-calls.md) — Provide a more accessible experience by adding your app’s audio to a call.
- [Capturing stereo audio from built-In microphones](capturing-stereo-audio-from-built-in-microphones.md) — Configure an iOS device’s built-in microphones to add stereo recording capabilities to your app.
- [AVAudioSession](avaudiosession.md) — An object that communicates to the system how you intend to use audio in your app.
- [AVAudioApplication](avaudioapplication.md) — An object that manages one or more audio sessions that belong to an app.
- [AVAudioRoutingArbiter](avaudioroutingarbiter.md) — An object for configuring macOS apps to participate in AirPods Automatic Switching.
