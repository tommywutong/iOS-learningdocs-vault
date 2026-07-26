---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidraginteraction/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteraction/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteraction/delegate.json'
content_hash: 'sha256:0735b725f4257ea4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteraction](../uidraginteraction.md)

# delegate

<sub>Instance Property</sub>

An object that configures and controls a drag interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UIDragInteractionDelegate)? { get }
```

## See Also

### Managing drag interactions

- [allowsSimultaneousRecognitionDuringLift](allowssimultaneousrecognitionduringlift.md) — A Boolean value that determines whether the interaction allows recognition of other gestures during the lift activity.
- [UIDragInteractionDelegate](../uidraginteractiondelegate.md) — The interface for configuring and controlling a drag interaction.
