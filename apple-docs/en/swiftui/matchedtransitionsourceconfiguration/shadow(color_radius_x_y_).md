---
title: 'shadow(color:radius:x:y:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/matchedtransitionsourceconfiguration/shadow(color:radius:x:y:)'
source_url: 'https://developer.apple.com/documentation/swiftui/matchedtransitionsourceconfiguration/shadow(color:radius:x:y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/matchedtransitionsourceconfiguration/shadow%28color%3Aradius%3Ax%3Ay%3A%29.json'
content_hash: 'sha256:af848eb42617fd06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MatchedTransitionSourceConfiguration](../matchedtransitionsourceconfiguration.md)

# shadow(color:radius:x:y:)

<sub>Instance Method</sub>

Applies the specified shadow effect to the matched transition source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func shadow(color: Color = Color(.sRGBLinear, white: 0, opacity: 0.33), radius: CGFloat, x: CGFloat = 0, y: CGFloat = 0) -> some MatchedTransitionSourceConfiguration

```

## Parameters

- `color` — The shadow’s color.

- `radius` — A measure of how much to blur the shadow. Larger values result in more blur.

- `x` — An amount to offset the shadow horizontally from the view.

- `y` — An amount to offset the shadow vertically from the view.
