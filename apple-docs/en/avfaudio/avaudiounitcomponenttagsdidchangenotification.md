---
title: AVAudioUnitComponentTagsDidChangeNotification
framework: AVFAudio
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfaudio/avaudiounitcomponenttagsdidchangenotification
source_url: 'https://developer.apple.com/documentation/avfaudio/avaudiounitcomponenttagsdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfaudio/avaudiounitcomponenttagsdidchangenotification.json'
content_hash: 'sha256:a982f481b5848bac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFAudio](../avfaudio.md)

# AVAudioUnitComponentTagsDidChangeNotification

<sub>Global Variable</sub>

A notification that indicates when component tags change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const AVAudioUnitComponentTagsDidChangeNotification;
```

## Discussion

The notification object contains the `AVAudioUnitComponent` object with the tags.
