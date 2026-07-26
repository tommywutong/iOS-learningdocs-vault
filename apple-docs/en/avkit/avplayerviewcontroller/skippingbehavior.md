---
title: skippingBehavior
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/skippingbehavior
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/skippingbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/skippingbehavior.json'
content_hash: 'sha256:76385b005dac741e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# skippingBehavior

<sub>Instance Property</sub>

The behavior that skipping gestures perform.

<sub>tvOS</sub>

```swift
var skippingBehavior: AVPlayerViewControllerSkippingBehavior { get set }
```

## Discussion

This property lets you override the default skipping behavior in tvOS, which is to skip forward or backward 10 seconds when a user presses the right or left sides, respectively, of the Touch surface on the Siri Remote.

## See Also

### Configuring skipping behavior

- [skipForwardEnabled](isskipforwardenabled.md) — A Boolean value that indicates whether forward-skipping is available.
- [skipBackwardEnabled](isskipbackwardenabled.md) — A Boolean value that indicates whether backward-skipping is available.
- [AVPlayerViewControllerSkippingBehavior](../avplayerviewcontrollerskippingbehavior.md) — Constants that represent the player view controller’s skipping behavior.
