---
title: defaultCaptureSoundDisabled
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureeventinteraction/defaultcapturesounddisabled
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/defaultcapturesounddisabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureeventinteraction/defaultcapturesounddisabled.json'
content_hash: 'sha256:2581e8356fe04c49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureEventInteraction](../avcaptureeventinteraction.md)

# defaultCaptureSoundDisabled

<sub>Type Property</sub>

A Boolean value that indicates whether the default sound is in a disabled state.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class var defaultCaptureSoundDisabled: Bool { get set }
```

## Discussion

If `true`, you must handle sound playback for capture events manually using the [- playSound:](<../avcaptureevent/play(__).md>) method.

> [!important] Important
> To use AirPods Camera Control, it must be available in your country or region. AirPods Camera Control is not currently available in the European Union.

## See Also

### Inspecting the interaction

- [enabled](isenabled.md) — A Boolean value that indicates whether this capture event interaction is in an enabled state.
