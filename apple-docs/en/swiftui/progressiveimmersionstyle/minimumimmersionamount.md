---
title: minimumImmersionAmount
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/progressiveimmersionstyle/minimumimmersionamount
source_url: 'https://developer.apple.com/documentation/swiftui/progressiveimmersionstyle/minimumimmersionamount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressiveimmersionstyle/minimumimmersionamount.json'
content_hash: 'sha256:e2bdbcad27787202'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressiveImmersionStyle](../progressiveimmersionstyle.md)

# minimumImmersionAmount

<sub>Instance Property</sub>

The minimum amount of immersion used for this instance of the style.

<sub>macOS, visionOS</sub>

```swift
let minimumImmersionAmount: Double?
```

## Discussion

The value represents the minimum amount of the spherical field of view of the user that can be covered by the portal effect of the style. The value can range from `0.0` to `1.0`. If this value is not set, a system default value will be used instead.
