---
title: shouldPlaySound
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureevent/shouldplaysound
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureevent/shouldplaysound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureevent/shouldplaysound.json'
content_hash: 'sha256:837d97dff25aea96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureEvent](../avcaptureevent.md)

# shouldPlaySound

<sub>Instance Property</sub>

A Boolean value that indicates whether you must play a sound manually.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var shouldPlaySound: Bool { get }
```

## Discussion

This property is `true` only when both of the following conditions are true:

1. A person performs an AirPod stem click.
2. You disable the default capture sound.

If this property is `false`, calling [- playSound:](<play(__).md>) has no effect. Omitting the sound when expected can significantly impact the user experience.

> [!important] Important
> To use AirPods Camera Control, it must be available in your country or region. AirPods Camera Control is not currently available in the European Union.

## See Also

### Playing a sound

- [- playSound:](<play(__).md>) — Plays the specified capture sound through AirPods.
