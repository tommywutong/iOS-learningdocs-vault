---
title: AVAudioApplication
framework: AVFAudio
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudioapplication
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudioapplication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudioapplication.json'
content_hash: 'sha256:63fbe5e614c56005'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVAudioApplication

<sub>Class</sub>

An object that manages one or more audio sessions that belong to an app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVAudioApplication
```

## Overview

Access the shared audio application instance to control app-level audio operations, such as requesting microphone permission and controlling audio input muting.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the shared instance

- [sharedInstance](avaudioapplication/shared.md) — Accesses the shared audio application instance.

### Requesting audio recording permission

- [+ requestRecordPermissionWithCompletionHandler:](<avaudioapplication/requestrecordpermission(completionhandler_).md>) — Determines whether the app has permission to record audio.
- [recordPermission](avaudioapplication/recordpermission-swift.property.md) — The app’s permission to record audio.
- [recordPermission](avaudioapplication/recordpermission-swift.enum.md) — Constants that indicate the app’s permission to record audio.

### Requesting microphone injection permission

- [+ requestMicrophoneInjectionPermissionWithCompletionHandler:](<avaudioapplication/requestmicrophoneinjectionpermission(completionhandler_).md>) — Requests the app’s permission to add audio to calls.
- [microphoneInjectionPermission](avaudioapplication/microphoneinjectionpermission-swift.property.md) — A value that indicates an app’s permission to add audio to calls.
- [MicrophoneInjectionPermission](avaudioapplication/microphoneinjectionpermission-swift.enum.md) — Constants that indicate an app’s permission to add audio to calls.

### Managing audio input mute state

- [inputMuted](avaudioapplication/isinputmuted.md) — A Boolean value that indicates whether the app’s audio input is in a muted state.
- [- setInputMuted:error:](<avaudioapplication/setinputmuted(__).md>) — Sets a Boolean value that indicates whether the app’s audio input is in a muted state.
- [AVAudioApplicationInputMuteStateChangeNotification](avaudioapplication/inputmutestatechangenotification.md) — A notification the system posts when the app’s audio input mute state changes.
- [- setInputMuteStateChangeHandler:error:](<avaudioapplication/setinputmutestatechangehandler(__).md>) — Sets a callback to handle changes to application-level audio muting states.

## See Also

### System audio

- [Handling audio interruptions](handling-audio-interruptions.md) — Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Responding to audio route changes](responding-to-audio-route-changes.md) — Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Routing audio to specific devices in multidevice sessions](routing-audio-to-specific-devices-in-multidevice-sessions.md) — Map audio channels to specific devices in multiroute sessions for recording and playback.
- [Adding synthesized speech to calls](adding-synthesized-speech-to-calls.md) — Provide a more accessible experience by adding your app’s audio to a call.
- [Capturing stereo audio from built-In microphones](capturing-stereo-audio-from-built-in-microphones.md) — Configure an iOS device’s built-in microphones to add stereo recording capabilities to your app.
- [AVAudioSession](avaudiosession.md) — An object that communicates to the system how you intend to use audio in your app.
- [AVAudioRoutingArbiter](avaudioroutingarbiter.md) — An object for configuring macOS apps to participate in AirPods Automatic Switching.
