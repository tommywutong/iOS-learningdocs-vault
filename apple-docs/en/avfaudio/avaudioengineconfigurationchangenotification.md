---
title: AVAudioEngineConfigurationChangeNotification
framework: AVFAudio
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudioengineconfigurationchangenotification
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudioengineconfigurationchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudioengineconfigurationchangenotification.json'
content_hash: 'sha256:4495d2010eff5638'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVAudioEngineConfigurationChangeNotification

<sub>Global Variable</sub>

A notification the framework posts when the audio engine configuration changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const AVAudioEngineConfigurationChangeNotification;
```

## Discussion

When the audio engine’s I/O unit observes a change to the audio input or output hardware’s channel count or sample rate, the audio engine stops, uninitializes itself, and issues this notification. The nodes remain in an attached and connected state with the previously set formats. The app must reestablish connections if the connection formats need to change.

> [!note] Note
> Don’t deallocate the engine from within the client’s notification handler. The callback happens on an internal dispatch queue and can deadlock while trying to tear down the engine synchronously.
