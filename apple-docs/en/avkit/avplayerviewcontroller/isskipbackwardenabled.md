---
title: isSkipBackwardEnabled
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/isskipbackwardenabled
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/isskipbackwardenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/isskipbackwardenabled.json'
content_hash: 'sha256:0e41d807588dfbb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# isSkipBackwardEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether backward-skipping is available.

<sub>tvOS</sub>

```swift
var isSkipBackwardEnabled: Bool { get set }
```

## Discussion

This property affects the appearance of the backward-skipping indicator. The value you set for the player view controller’s [skippingBehavior](skippingbehavior.md) property determines its backward-skipping behavior.

## See Also

### Configuring skipping behavior

- [skipForwardEnabled](isskipforwardenabled.md) — A Boolean value that indicates whether forward-skipping is available.
- [skippingBehavior](skippingbehavior.md) — The behavior that skipping gestures perform.
- [AVPlayerViewControllerSkippingBehavior](../avplayerviewcontrollerskippingbehavior.md) — Constants that represent the player view controller’s skipping behavior.
