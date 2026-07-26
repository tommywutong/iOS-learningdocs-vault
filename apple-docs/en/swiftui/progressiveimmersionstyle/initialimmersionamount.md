---
title: initialImmersionAmount
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/progressiveimmersionstyle/initialimmersionamount
source_url: 'https://developer.apple.com/documentation/swiftui/progressiveimmersionstyle/initialimmersionamount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressiveimmersionstyle/initialimmersionamount.json'
content_hash: 'sha256:2e83d9b80726a0e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressiveImmersionStyle](../progressiveimmersionstyle.md)

# initialImmersionAmount

<sub>Instance Property</sub>

The initial amount of immersion used for this instance of the style.

<sub>macOS, visionOS</sub>

```swift
let initialImmersionAmount: Double?
```

## Discussion

The value represents how much of the spherical field of view of the user is covered by the portal effect of the style initially. The value can range from `0.0` to `1.0`, and is capped by the minimum and maximum amount of immersion of this instance. If this value is not set, a system default value will be used instead.
