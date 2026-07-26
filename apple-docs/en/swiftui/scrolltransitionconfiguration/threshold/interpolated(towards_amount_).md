---
title: 'interpolated(towards:amount:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrolltransitionconfiguration/threshold/interpolated(towards:amount:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/threshold/interpolated(towards:amount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionconfiguration/threshold/interpolated%28towards%3Aamount%3A%29.json'
content_hash: 'sha256:ec4a1cd6a88feaae'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [ScrollTransitionConfiguration](../../scrolltransitionconfiguration.md) · [Threshold](../threshold.md)

# interpolated(towards:amount:)

<sub>Instance Method</sub>

Creates a new threshold that combines this threshold value with another threshold, interpolated by the given amount.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func interpolated(towards other: ScrollTransitionConfiguration.Threshold, amount: Double) -> ScrollTransitionConfiguration.Threshold
```

## Parameters

- `other` — The second threshold value.

- `amount` — The ratio with which this threshold is combined with the given threshold, where zero is equal to this threshold, 1.0 is equal to `other`, and values in between combine the two thresholds.

## See Also

### Modifying the threshold

- [inset(by:)](<inset(by_).md>) — Returns a threshold that is met when the target view is closer to the center of the container by `distance`. Use negative values to move the threshold away from the center.
