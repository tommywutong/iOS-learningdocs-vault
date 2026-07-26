---
title: isEnabled
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avcaptureeventinteraction/isenabled
source_url: 'https://developer.apple.com/documentation/avkit/avcaptureeventinteraction/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avcaptureeventinteraction/isenabled.json'
content_hash: 'sha256:0978fb9646bc98cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVCaptureEventInteraction](../avcaptureeventinteraction.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether this capture event interaction is in an enabled state.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

Set this value to `false` when your app can’t or won’t respond to the action callbacks to avoid non-interactive buttons or UI elements.

## See Also

### Inspecting the interaction

- [defaultCaptureSoundDisabled](defaultcapturesounddisabled.md) — A Boolean value that indicates whether the default sound is in a disabled state.
