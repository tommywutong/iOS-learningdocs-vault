---
title: ScrollTransitionConfiguration.Threshold
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltransitionconfiguration/threshold
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/threshold'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionconfiguration/threshold.json'
content_hash: 'sha256:7855c260ac3ce34a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTransitionConfiguration](../scrolltransitionconfiguration.md)

# ScrollTransitionConfiguration.Threshold

<sub>Structure</sub>

Describes a specific point in the progression of a target view within a container from hidden (fully outside the container) to visible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Threshold
```

## Topics

### Getting the threshold

- [centered](threshold/centered.md) — The target view is centered within the container
- [hidden](threshold/hidden.md)
- [visible](threshold/visible.md)
- [visible(_:)](<threshold/visible(__).md>) — The target view is visible by the given amount, where zero is fully hidden, and one is fully visible.

### Modifying the threshold

- [inset(by:)](<threshold/inset(by_).md>) — Returns a threshold that is met when the target view is closer to the center of the container by `distance`. Use negative values to move the threshold away from the center.
- [interpolated(towards:amount:)](<threshold/interpolated(towards_amount_).md>) — Creates a new threshold that combines this threshold value with another threshold, interpolated by the given amount.

## See Also

### Accessing the configuration

- [animation(_:)](<animation(__).md>) — Sets the animation with which the transition will be applied.
- [threshold(_:)](<threshold(__).md>) — Sets the threshold at which the view will be considered fully visible.
