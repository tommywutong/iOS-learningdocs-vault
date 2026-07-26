---
title: 'threshold(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrolltransitionconfiguration/threshold(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/threshold(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionconfiguration/threshold%28_%3A%29.json'
content_hash: 'sha256:d56b2cf42a07c6bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollTransitionConfiguration](../scrolltransitionconfiguration.md)

# threshold(_:)

<sub>Instance Method</sub>

Sets the threshold at which the view will be considered fully visible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func threshold(_ threshold: ScrollTransitionConfiguration.Threshold) -> ScrollTransitionConfiguration
```

## Parameters

- `threshold` — The threshold specifying how much of the view must intersect with the container before it is treated as visible.

## Return Value

A copy of this configuration with the threshold set to the given value.

## See Also

### Accessing the configuration

- [animation(_:)](<animation(__).md>) — Sets the animation with which the transition will be applied.
- [Threshold](threshold.md) — Describes a specific point in the progression of a target view within a container from hidden (fully outside the container) to visible.
