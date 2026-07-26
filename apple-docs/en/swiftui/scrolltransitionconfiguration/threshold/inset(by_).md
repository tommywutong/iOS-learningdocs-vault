---
title: 'inset(by:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrolltransitionconfiguration/threshold/inset(by:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration/threshold/inset(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionconfiguration/threshold/inset%28by%3A%29.json'
content_hash: 'sha256:40b5fa35feba70ad'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [ScrollTransitionConfiguration](../../scrolltransitionconfiguration.md) · [Threshold](../threshold.md)

# inset(by:)

<sub>Instance Method</sub>

Returns a threshold that is met when the target view is closer to the center of the container by `distance`. Use negative values to move the threshold away from the center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func inset(by distance: Double) -> ScrollTransitionConfiguration.Threshold
```

## See Also

### Modifying the threshold

- [interpolated(towards:amount:)](<interpolated(towards_amount_).md>) — Creates a new threshold that combines this threshold value with another threshold, interpolated by the given amount.
