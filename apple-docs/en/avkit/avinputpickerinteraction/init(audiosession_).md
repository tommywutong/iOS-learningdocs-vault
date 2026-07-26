---
title: 'init(audioSession:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avinputpickerinteraction/init(audiosession:)'
source_url: 'https://developer.apple.com/documentation/avkit/avinputpickerinteraction/init(audiosession:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinputpickerinteraction/init%28audiosession%3A%29.json'
content_hash: 'sha256:deb18c5a4f99c2c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInputPickerInteraction](../avinputpickerinteraction.md)

# init(audioSession:)

<sub>Initializer</sub>

Creates a new instance of AVInputPickerInteraction using a specific `AVAudioSession`.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(audioSession: AVAudioSession?)
```

## Parameters

- `audioSession` — An optional recording configured audio session. If you provide a non-recording session, the input list will be empty.

## Discussion

Use this initializer when the provided `AVAudioSession` is in .record mode or you plan to switch it to record mode.

If nil session is passed in object will use a sharedInstance from `AVAudioSession`.

## See Also

### Creating an input picker

- [- init](<init().md>) — Creates a new instance of AVInputPickerController using a default sharedInstance from `AVAudioSession`.
