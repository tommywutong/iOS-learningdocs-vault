---
title: maximumImmersionAmount
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/progressiveimmersionstyle/maximumimmersionamount
source_url: 'https://developer.apple.com/documentation/swiftui/progressiveimmersionstyle/maximumimmersionamount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressiveimmersionstyle/maximumimmersionamount.json'
content_hash: 'sha256:7d0119c964d5e994'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressiveImmersionStyle](../progressiveimmersionstyle.md)

# maximumImmersionAmount

<sub>Instance Property</sub>

The maximum amount of immersion used for this instance of the style.

<sub>macOS, visionOS</sub>

```swift
let maximumImmersionAmount: Double?
```

## Discussion

The value represents the maximum amount of the spherical field of view of the user that can be covered by the portal effect of the style. The value can range from `0.0` to `1.0`. If this value is not set, a system default value will be used instead.
