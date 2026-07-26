---
title: 'background(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/matchedtransitionsourceconfiguration/background(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/matchedtransitionsourceconfiguration/background(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/matchedtransitionsourceconfiguration/background%28_%3A%29.json'
content_hash: 'sha256:c672611201f93318'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MatchedTransitionSourceConfiguration](../matchedtransitionsourceconfiguration.md)

# background(_:)

<sub>Instance Method</sub>

Specifies a color that will be drawn behind the content within the matched transition source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func background(_ style: Color) -> some MatchedTransitionSourceConfiguration

```

## Parameters

- `style` — The color to apply behind the content within the matched transition source..

## Discussion

During a zoom transition, the background color fills the interpolated shape as it groes from the matched transition source.
