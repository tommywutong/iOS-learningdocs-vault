---
title: AVAudioEngineConfigurationChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/avaudioengineconfigurationchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avaudioengineconfigurationchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/avaudioengineconfigurationchange.json'
content_hash: 'sha256:8c6bd6f7ed5ffb04'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# AVAudioEngineConfigurationChange

<sub>Type Property</sub>

A notification the framework posts when the audio engine configuration changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let AVAudioEngineConfigurationChange: NSNotification.Name
```

## Discussion

When the audio engine’s I/O unit observes a change to the audio input or output hardware’s channel count or sample rate, the audio engine stops, uninitializes itself, and issues this notification. The nodes remain in an attached and connected state with the previously set formats. The app must reestablish connections if the connection formats need to change.

> [!note] Note
> Don’t deallocate the engine from within the client’s notification handler. The callback happens on an internal dispatch queue and can deadlock while trying to tear down the engine synchronously.

## See Also

### AVFAudio

- [AVAudioUnitComponentTagsDidChange](avaudiounitcomponenttagsdidchange.md) — A notification that indicates when component tags change.
- [interruptionNotification](../../../avfaudio/avaudiosession/interruptionnotification.md) — A notification the system posts when an audio interruption occurs. _(deprecated)_
- [mediaServicesWereLostNotification](../../../avfaudio/avaudiosession/mediaserviceswerelostnotification.md) — A notification the system posts when it terminates the media server.
- [mediaServicesWereResetNotification](../../../avfaudio/avaudiosession/mediaserviceswereresetnotification.md) — A notification the system posts when the media server restarts.
- [routeChangeNotification](../../../avfaudio/avaudiosession/routechangenotification.md) — A notification the system posts when its audio route changes.
- [silenceSecondaryAudioHintNotification](../../../avfaudio/avaudiosession/silencesecondaryaudiohintnotification.md) — A notification the system posts when the primary audio from other apps starts and stops.
