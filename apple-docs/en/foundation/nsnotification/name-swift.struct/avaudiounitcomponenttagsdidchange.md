---
title: AVAudioUnitComponentTagsDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/avaudiounitcomponenttagsdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avaudiounitcomponenttagsdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/avaudiounitcomponenttagsdidchange.json'
content_hash: 'sha256:ed119604f55f09d2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# AVAudioUnitComponentTagsDidChange

<sub>Type Property</sub>

A notification that indicates when component tags change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let AVAudioUnitComponentTagsDidChange: NSNotification.Name
```

## Discussion

The notification object contains the `AVAudioUnitComponent` object with the tags.

## See Also

### AVFAudio

- [AVAudioEngineConfigurationChange](avaudioengineconfigurationchange.md) — A notification the framework posts when the audio engine configuration changes.
- [interruptionNotification](../../../avfaudio/avaudiosession/interruptionnotification.md) — A notification the system posts when an audio interruption occurs. _(deprecated)_
- [mediaServicesWereLostNotification](../../../avfaudio/avaudiosession/mediaserviceswerelostnotification.md) — A notification the system posts when it terminates the media server.
- [mediaServicesWereResetNotification](../../../avfaudio/avaudiosession/mediaserviceswereresetnotification.md) — A notification the system posts when the media server restarts.
- [routeChangeNotification](../../../avfaudio/avaudiosession/routechangenotification.md) — A notification the system posts when its audio route changes.
- [silenceSecondaryAudioHintNotification](../../../avfaudio/avaudiosession/silencesecondaryaudiohintnotification.md) — A notification the system posts when the primary audio from other apps starts and stops.
