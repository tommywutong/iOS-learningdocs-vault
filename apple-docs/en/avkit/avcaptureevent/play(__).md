---
title: 'play(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avcaptureevent/play(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureevent/play(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureevent/play%28_%3A%29.json'
content_hash: 'sha256:5bedea1718ee81c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureEvent](../avcaptureevent.md)

# play(_:)

<sub>Instance Method</sub>

Plays the specified capture sound through AirPods.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func play(_ sound: AVCaptureEventSound) -> Bool
```

## Parameters

- `sound` — The capture sound to play for this event.

## Return Value

A Boolean value that indicates whether the system played the sound.

## Discussion

This method has no effect if [shouldPlaySound](shouldplaysound.md) is `false` or if the event object’s lifetime exceeds 15 seconds.

> [!important] Important
> To use AirPods Camera Control, it must be available in your country or region. AirPods Camera Control is not currently available in the European Union.

## See Also

### Playing a sound

- [shouldPlaySound](shouldplaysound.md) — A Boolean value that indicates whether you must play a sound manually.
